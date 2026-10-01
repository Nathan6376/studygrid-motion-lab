-- StudyGrid Q-S12 read-only staging static acceptance scaffold
-- PREP ONLY. Do not run against production. This file contains SELECT-only inspection queries.
-- Named consumer: future Stuart real-Supabase staging acceptance after General explicitly releases a staging target.
-- Source: Claude C-A backend implementation-readiness contract + non-applied candidate.
-- Expected private schema: app
-- Expected client schema: api

\set ON_ERROR_STOP 1

-- STATIC-01: every app table must have RLS enabled AND forced.
select
  n.nspname as schema_name,
  c.relname as table_name,
  c.relrowsecurity as rls_enabled,
  c.relforcerowsecurity as rls_forced
from pg_class c
join pg_namespace n on n.oid=c.relnamespace
where n.nspname='app' and c.relkind='r'
order by c.relname;

-- Gate query: must return zero rows.
select c.relname as violation
from pg_class c
join pg_namespace n on n.oid=c.relnamespace
where n.nspname='app' and c.relkind='r'
  and (not c.relrowsecurity or not c.relforcerowsecurity);

-- STATIC-02: authenticated must have no direct writes on app tables.
-- Gate query: must return zero rows.
select table_schema, table_name, privilege_type
from information_schema.role_table_grants
where grantee='authenticated'
  and table_schema='app'
  and privilege_type in ('INSERT','UPDATE','DELETE','TRUNCATE','REFERENCES','TRIGGER')
order by table_name, privilege_type;

-- STATIC-03: no authenticated write RLS policy exists.
-- Gate query: must return zero rows.
select schemaname, tablename, policyname, cmd, roles
from pg_policies
where schemaname='app'
  and cmd in ('INSERT','UPDATE','DELETE','ALL')
  and ('authenticated' = any(roles))
order by tablename, policyname;

-- STATIC-04 / STATIC-05: every api.cmd_* function must be SECURITY DEFINER,
-- have a pinned search_path, and be owned by non-login app_owner.
select
  n.nspname as schema_name,
  p.proname,
  p.prosecdef as security_definer,
  r.rolname as owner_role,
  r.rolcanlogin as owner_can_login,
  p.proconfig
from pg_proc p
join pg_namespace n on n.oid=p.pronamespace
join pg_roles r on r.oid=p.proowner
where n.nspname='api' and p.proname like 'cmd\_%' escape '\'
order by p.proname;

-- Gate query: must return zero rows.
select p.proname as violation, p.prosecdef, r.rolname, r.rolcanlogin, p.proconfig
from pg_proc p
join pg_namespace n on n.oid=p.pronamespace
join pg_roles r on r.oid=p.proowner
where n.nspname='api' and p.proname like 'cmd\_%' escape '\'
  and (
    not p.prosecdef
    or r.rolname <> 'app_owner'
    or r.rolcanlogin
    or p.proconfig is null
    or not exists (
      select 1 from unnest(p.proconfig) cfg
      where cfg like 'search_path=%'
        and cfg like '%pg_catalog%'
        and cfg not like '%"$user"%'
    )
  );

-- STATIC-06: anon/public must not have api command EXECUTE.
-- Gate query: must return zero rows for api.cmd_*.
select routine_schema, routine_name, grantee, privilege_type
from information_schema.routine_privileges
where routine_schema='api'
  and routine_name like 'cmd\_%' escape '\'
  and grantee in ('PUBLIC','anon')
  and privilege_type='EXECUTE'
order by routine_name, grantee;

-- STATIC-07: client read models must be security_invoker.
-- PostgreSQL stores this as a reloption on the view.
select
  n.nspname as schema_name,
  c.relname as view_name,
  c.reloptions
from pg_class c
join pg_namespace n on n.oid=c.relnamespace
where n.nspname='api' and c.relkind='v'
order by c.relname;

-- Gate query: must return zero rows for released client views.
select c.relname as violation, c.reloptions
from pg_class c
join pg_namespace n on n.oid=c.relnamespace
where n.nspname='api' and c.relkind='v'
  and c.relname in ('v_student_timeline','v_assessment_desk','v_attention_queue')
  and not ('security_invoker=true' = any(coalesce(c.reloptions, array[]::text[])));

-- STATIC-09: sensitive operational tables must not be SELECT-able by authenticated.
-- Gate query: every has_table_privilege value must be false.
select t.table_name,
       has_table_privilege('authenticated', format('app.%I', t.table_name), 'SELECT') as authenticated_can_select
from (values
  ('audit_events'),
  ('command_log'),
  ('outbox'),
  ('join_attempts'),
  ('platform_admins'),
  ('instructor_verifications')
) as t(table_name)
order by t.table_name;

-- STATIC-10: inspect AI worker privileges/policies. The released contract must explicitly
-- bind whether worker reads are global trusted-worker reads or scoped to assigned jobs/sections.
select table_schema, table_name, privilege_type
from information_schema.role_table_grants
where grantee='ai_worker'
order by table_schema, table_name, privilege_type;

select schemaname, tablename, policyname, cmd, roles, qual, with_check
from pg_policies
where schemaname='app' and 'ai_worker' = any(roles)
order by tablename, policyname;

-- POSTGREST EXPOSURE CHECK (STATIC-08)
-- Provider-specific inspection belongs in the staging run because the concrete Supabase
-- configuration surface may vary. Acceptance oracle: client PostgREST can use api views/RPCs,
-- while app schema/table routes are not exposed at all.
