# StudyGrid — Stuart Q-S12 Backend Acceptance Prep

**Status:** PREP ONLY — this is not backend acceptance, not Supabase validation, and not release authority.

**Named downstream consumer:** future Stuart real-Supabase staging acceptance after General explicitly releases a staging target. Secondary consumers are Claude backend implementation/hardening and Bob adapter integration where the shared gateway contract must match.

## Exact source basis

- Current Stuart queue: `queues/STUART_QUEUE.txt` @ `1277bdf3770377459cd7faa3e0bfdf7d8cae367e`.
- General accepted Slice 2 pointer: `routes/GENERAL_ACCEPTED_SLICE2_QB15.txt` @ `969c58a6e9d436476e63560228b4461e1e25269a`; this pointer explicitly allows non-mutating backend/security/test preparation while visible Slice 3 UI is held for owner review.
- Claude C-A contract: Drive `1Tii11WZH9MhdKY3c8NrAOg9FTnRKTvzY`, 21,128 bytes, current provider-byte SHA-256 `af06ce9e32f48b299025e35172b81c5a7044493889d287bdcb53d6446efb19dc`.
- Claude C-A non-applied SQL/test attachment: Drive `1nZe0lyT9QzoP49nIlGCiSZCYjrueT7kR`, 58,936 bytes, current provider-byte SHA-256 `999a30d396278803c66cb9a3085db62a1bb056ae11c13b6077d40735e5866632`.
- Claude reports its locally executed bundle passed 34/34 in PostgreSQL 16.15 with a Supabase-like auth shim and had local SHA-256 `25a01e87ec7705080c0dbf9a1cf26de9eb3727234018efd3d65f6816e1eebd13`. The current Drive attachment was re-emitted with a header, so its provider SHA is recorded separately; this prep does **not** claim byte identity with the locally executed file.

## What future staging acceptance must prove

1. Real Supabase auth/JWT/PostgREST behaviour, not just the local shim.
2. FORCE RLS and no authenticated direct-write path on every private `app` table.
3. Exact cross-section, profile, question, source-state, draft/tentative and operational-table non-leakage.
4. Gateway command authorization, stale/no-mutation behaviour, one-truth revision semantics, idempotency and audit/outbox effects.
5. Parallel races: revision, confirmation, idempotency, delivery, join-code issue and audit-chain integrity.
6. Adapter parity with the accepted product boundary: envelope, section identity, server-derived role, time zone, opaque revision id, idempotency key and `api`-only transport.
7. Migration/release boundary: synthetic staging only; no production/canonical claim; no real learner data until later institutional gates.

## RLS table matrix

Legend: `—` no access; `SELF` self row only; `OWN` active-member section; `READY` active section + ready source only; `CONF` active section + confirmed non-tentative revision only; `STAFF` current C-A `is_staff` behaviour; `EDITOR` verified editor only; `SELF*` current SQL keeps self-history even without active membership and requires final contract binding; `GLOBAL?` current SQL grants global AI-worker read and requires explicit release decision; `INS-PEND` AI worker insert-pending only.

| table | ANON | OUT | P-STU | STU-A | STU-B | TA-A | INST-A | CO-UNV | REM-A | AI-W |
|---|---|---|---|---|---|---|---|---|---|---|
| `profiles` | — | SELF | SELF | SELF | SELF | STAFF | STAFF | STAFF | SELF | — |
| `platform_admins` | — | — | — | — | — | — | — | — | — | — |
| `instructor_verifications` | — | — | — | — | — | — | — | — | — | — |
| `courses` | — | — | — | OWN | OWN | STAFF | STAFF | STAFF | — | — |
| `class_sections` | — | — | — | OWN | OWN | STAFF | STAFF | STAFF | — | — |
| `memberships` | — | — | SELF | SELF | SELF | STAFF | STAFF | STAFF | SELF | — |
| `join_codes` | — | — | — | — | — | — | EDITOR | — | — | — |
| `join_attempts` | — | — | — | — | — | — | — | — | — | — |
| `sources` | — | — | — | OWN | OWN | STAFF | STAFF | STAFF | — | — |
| `source_revisions` | — | — | — | READY | READY | STAFF | STAFF | STAFF | — | — |
| `source_blocks` | — | — | — | READY | READY | STAFF | STAFF | STAFF | — | GLOBAL? |
| `assessments` | — | — | — | OWN | OWN | STAFF | STAFF | STAFF | — | — |
| `assessment_revisions` | — | — | — | CONF | CONF | STAFF | STAFF | STAFF | — | — |
| `field_provenance` | — | — | — | — | — | STAFF | STAFF | STAFF | — | — |
| `delivery_plans` | — | — | — | — | — | STAFF | STAFF | STAFF | — | — |
| `student_questions` | — | — | SELF* | SELF | SELF | STAFF | STAFF | STAFF | SELF* | — |
| `resolution_signals` | — | — | SELF* | SELF | SELF | STAFF | STAFF | STAFF | SELF* | — |
| `attention_items` | — | — | — | — | — | STAFF | STAFF | STAFF | — | — |
| `audit_events` | — | — | — | — | — | — | — | — | — | — |
| `outbox` | — | — | — | — | — | — | — | — | — | — |
| `command_log` | — | — | — | — | — | — | — | — | — | — |
| `ai_jobs` | — | — | — | — | — | STAFF | STAFF | STAFF | — | GLOBAL? |
| `ai_candidates` | — | — | — | — | — | STAFF | STAFF | STAFF | — | INS-PEND |

### Required leakage probes

- **LEAK-01 — Cross-section raw-table row counts:** For every section-scoped app table, section-B-only user sees zero section-A rows; counts, min/max ids, existence probes and aggregates remain zero/null.
- **LEAK-02 — Cross-section api view row counts:** v_student_timeline, v_assessment_desk and v_attention_queue expose only caller-authorized sections; aggregate count does not reveal hidden rows.
- **LEAK-03 — Student hidden-state leakage:** Student sees no tentative/unconfirmed assessment revisions, delivery plans, attention, provenance, AI jobs/candidates, or non-ready source revisions/blocks.
- **LEAK-04 — Profile visibility:** Student cannot enumerate classmates' profiles; staff visibility is limited to users sharing an active staff section; other-section profiles remain hidden.
- **LEAK-05 — Join-code enumeration:** Invalid, disabled and expired code probes have the same public error class/body shape and reveal no section identity; wrong confirmed section label changes no membership/use counters.
- **LEAK-06 — Join-code timing heuristic:** Run repeated invalid/disabled/expired probes and flag material systematic timing separation for review; timing alone is not a pass/fail oracle, but observable metadata/body must be indistinguishable.
- **LEAK-07 — Removed-member access:** Removed member loses class_sections/courses/sources/revisions/blocks/assessments/read-model access and cannot invoke student commands. Self-profile/membership/question-history visibility is a contract ambiguity and must be explicitly bound before terminal acceptance.
- **LEAK-08 — Unverified co-instructor lapse:** All editor commands must fail. Current C-A SQL still grants staff-read visibility through app.is_staff; terminal staging acceptance must bind whether those reads remain allowed or become verification-gated.
- **LEAK-09 — AI worker section scope:** Current C-A SQL gives ai_worker global SELECT on ai_jobs/source_blocks via USING(true), while prose says blocks/jobs 'it is given'. Real staging target must explicitly authorize global trusted-worker scope or narrow it; no silent acceptance.
- **LEAK-10 — Operational-table secrecy:** audit_events, command_log, outbox, join_attempts, platform_admins and instructor_verifications are not client-readable; app schema itself is not exposed through PostgREST.
- **LEAK-11 — Question privacy:** Classmate cannot read or signal on another student's question; instructor/TA own-section visibility does not cross sections.
- **LEAK-12 — Secret/free-text hygiene:** Join-code plaintext is absent from persisted tables/logs/outbox/audit; question body is absent from audit and command_log request/result payloads except cryptographic hashes.

## Command authorization / state contract

| Command | Allowed | Must deny / guard | Acceptance oracle |
|---|---|---|---|
| `cmd_create_section` | platform_admin | anon, outsider, pending_student_a, active_student_a, ta_a, verified_instructor_a_without_admin | Only platform admin can bootstrap; no client-supplied role elevates. |
| `cmd_issue_join_code` | verified_instructor_or_co_own_section | ta, student, unverified_co, other_section_staff, anon | One live code per section; plaintext returned once; stored/logged result contains no plaintext code. |
| `cmd_preview_join_code` | authenticated_user_with_valid_code | anon | Invalid/disabled/expired code is generic INVALID_CODE; valid code reveals only intended course/section/term confirmation data. |
| `cmd_redeem_join_code` | authenticated_nonmember_with_valid_code_and_confirmed_label | anon, wrong_label, rate_limited | Role is server-fixed student; approval requirement controls pending vs active; no existing membership mutation. |
| `cmd_approve_member` | verified_instructor_or_co_own_section | ta, student, unverified_co, other_section_staff | Only pending member in same section may be approved. |
| `cmd_create_assessment` | verified_instructor_or_co_own_section | ta, student, unverified_co, other_section_staff | Creates draft truth only; provenance and attention created as contract specifies. |
| `cmd_revise_assessment` | verified_instructor_or_co_own_section | ta, student, unverified_co, other_section_staff | Expected revision required; stale returns STALE_REVISION with no mutation. |
| `cmd_confirm_assessment` | verified_instructor_or_co_own_section | ta, student, unverified_co, other_section_staff | Tentative/undated guarded; exactly one confirmed revision; downstream delivery/attention effects bound to same truth. |
| `cmd_schedule_delivery` | verified_instructor_or_co_own_section | ta, student, unverified_co, other_section_staff | Confirmed truth required; scheduled plan bound to confirmed revision and server-computed time. |
| `cmd_submit_question` | active_student_own_section | pending_student, removed_student, student_other_section, staff_role_without_student_membership, anon | Only active student membership; body text never copied into audit/command metadata. |
| `cmd_signal_resolution` | question_author_with_active_membership | classmate, removed_author, other_section_user, anon | Author + active membership required; still_need_help reopens attention. |
| `cmd_decide_candidate` | verified_instructor_or_co_own_section | ta, student, unverified_co, other_section_staff, ai_worker | AI cannot decide or write truth; accepted schema_ok candidate creates draft, not confirmed truth. |

## Concurrency / idempotency gates

- **CONC-01 — Revision race / distinct idempotency keys**. Setup: Two verified editors issue cmd_revise_assessment against same assessment and same expected revision with different keys. **Pass:** Exactly one mutation wins; the other returns stale_revision; current_revision advances once; one new revision row; no partial provenance/audit artifacts from loser.
- **CONC-02 — Same idempotency key / same request**. Setup: Two parallel identical mutating RPCs use the same actor+idempotency key. **Pass:** Both callers resolve to the same logical result, exactly one mutation/audit/outbox effect occurs, and one response is a replay or equivalent deterministic duplicate-safe response. No unique-violation escapes the gateway envelope.
- **CONC-03 — Same idempotency key / different request**. Setup: Two parallel RPCs use same actor+key but different payload/request hashes. **Pass:** At most one mutation commits; loser returns IDEMPOTENCY_CONFLICT envelope; no raw SQL exception and no mixed partial state.
- **CONC-04 — Confirm race**. Setup: Two parallel confirmations target the same current revision. **Pass:** Exactly one set of confirmation side effects (truth transition, outbox, audit, attention resolution, delivery recompute). Second call is deterministic already/replay/stale per released contract, without duplicate side effects.
- **CONC-05 — Delivery schedule replay/race**. Setup: Two parallel schedule commands with identical key and request. **Pass:** One delivery plan only; retry returns deterministic duplicate-safe envelope; no duplicate outbox/audit effects.
- **CONC-06 — Join-code issue replay/race**. Setup: Two parallel issue-code calls use same key. **Pass:** One active code row only; no second valid code is created; persisted logs remain redacted. Retry semantics must be explicitly documented because plaintext is intentionally returned once.
- **CONC-07 — Audit chain same-section concurrency**. Setup: Generate concurrent accepted mutations in one section. **Pass:** Per-section hash chain has no fork/gap: every prev_sha256 equals preceding committed row_sha256 in id order.
- **CONC-08 — Audit independence across sections**. Setup: Concurrent mutations in sections A and B. **Pass:** Each section chain is internally valid and no row points to another section's hash.
- **CONC-09 — Attention uniqueness race**. Setup: Concurrent paths try to open same attention (section,kind,object_ref). **Pass:** Partial unique index leaves exactly one open item; no duplicate visible attention row.

## Static fail-closed checks

- **STATIC-01:** Every app table has relrowsecurity=true and relforcerowsecurity=true.
- **STATIC-02:** authenticated has no INSERT/UPDATE/DELETE/TRUNCATE on any app table.
- **STATIC-03:** No authenticated write policy exists on app tables.
- **STATIC-04:** Every api.cmd_* function is SECURITY DEFINER and has a pinned search_path with pg_catalog before app/api; no unpinned public/$user resolution.
- **STATIC-05:** Every api.cmd_* function owner is the dedicated non-login app_owner (not postgres/service_role); app_owner rolcanlogin=false.
- **STATIC-06:** anon/public cannot EXECUTE api command functions or SELECT api read models.
- **STATIC-07:** api read models used by clients are security_invoker=true.
- **STATIC-08:** PostgREST exposes only api for this backend contract; app is not an exposed schema.
- **STATIC-09:** Sensitive ops tables remain without authenticated SELECT grant.
- **STATIC-10:** ai_worker grants are exactly bounded: SELECT only approved job/block scope and INSERT pending ai_candidates; no truth mutation/decision privileges.

## Adapter parity gates

- **ADAPT-01:** RPC envelope remains {ok,state,data} or {ok,state,error{code,message,detail}} with accepted state vocabulary; no transport/raw SQL error leaks.
- **ADAPT-02:** class_section_id is distinct from doc_heading_key; source section/document-heading identifiers never serve as tenancy/privacy identity.
- **ADAPT-03:** Client actor_role is ignored/absent for real adapter; server derives role from JWT + active membership + verification where required.
- **ADAPT-04:** Time values are stored as timestamptz and rendered using section.tz; client does not compute delivery fire-time arithmetic.
- **ADAPT-05:** revision_id is opaque; revision_seq is display-only if surfaced.
- **ADAPT-06:** Every mutating adapter action supplies a stable idempotency_key generated once per user action and reused on retry.
- **ADAPT-07:** save_draft/confirm mappings hit released cmd_* functions without product redesign; delivery reads from released read model.
- **ADAPT-08:** Gateway central mapper covers IDEMPOTENCY_CONFLICT, GUARD_FAILED, RATE_LIMITED, INVALID_CODE, SECTION_NOT_CONFIRMED, ALREADY_MEMBER plus inherited codes.
- **ADAPT-09:** source_revision_id/source_block_id/display_locator come from backend source identities; display_locator is server-generated.
- **ADAPT-10:** Client transport targets exposed api schema only; no client query references app; realtime is not required for pilot.

## Contract ambiguities that must be resolved before terminal staging acceptance

- **AMB-01 — Unverified co-instructor read access**. Evidence: C-A prose asks Stuart to add a verification-lapse test and labels the main staff matrix as 'instructor/co (verified editor)', but current SQL app.is_staff checks role only while app.is_editor adds verification. Required resolution: Before terminal staging acceptance, released backend contract must say whether verification loss revokes staff reads or only editor commands.
- **AMB-02 — Removed member historical self-data**. Evidence: Current SQL removes active class access via app.is_member, but profiles/memberships/student_questions/resolution_signals contain self-only policies independent of active membership. Required resolution: Bind whether removed users may retain self-profile, membership-state and historical own-question/signal reads; class/course/source/assessment/read-model access must be gone.
- **AMB-03 — AI worker global read scope**. Evidence: Current SQL policies w_read use USING(true) on ai_jobs/source_blocks, while C-A prose says the worker may read jobs and blocks 'it is given'. Required resolution: Release contract must explicitly authorize trusted global worker scope or add job/section-scoped worker isolation.
- **AMB-04 — Concurrent idempotency claim**. Evidence: Current candidate performs idem_lookup before mutation and idem_store afterward; the sequential 34-test suite does not exercise two same-key calls racing. Required resolution: Real staging gate CONC-02/03 must prove duplicate-safe envelope semantics under parallel calls; implementation may need an atomic key-claim/lock strategy.

These are not owner-review UI questions and do not authorize Slice 3. They are backend contract points for General/Claude to bind before Stuart can issue a terminal real-staging PASS.

## Strengthening Claude's weak tests

- Replace C-A T08's vacuous source half with fixtures in both sections: ready + processing/partial/rejected revisions and blocks. Assert student A sees only section-A ready records, student B sees only section-B ready records, staff A sees all section-A states, outsider/pending/removed see zero.
- Replace C-A T31 with a sentinel free-text question whose raw text is searched across `audit_events`, `command_log`, `outbox` and serialized results. Assert only the expected hashes appear, never the raw question body. Independently validate the audit payload hash against the canonical hash-object payload rather than the raw question text.

## Known prep findings from the current non-applied candidate

- `app.is_editor` requires instructor verification, but `app.is_staff` does not. Therefore the current SQL denies editor commands to an unverified co-instructor while still allowing staff-scoped reads. C-A asks for a verification-lapse test but does not unambiguously state the read expectation.
- Removed membership disables `app.is_member`, so class/course/source/assessment access goes away, but self-only policies still expose the user's own profile, membership row, question history and resolution signals. The retention expectation must be bound explicitly.
- The AI worker policies use `USING (true)` for `ai_jobs` and `source_blocks`; C-A prose says the worker may read jobs/blocks 'it is given'. Staging acceptance must not silently treat global cross-section worker read as approved.
- Idempotency is tested sequentially in C-A. The current candidate does `idem_lookup` before mutation and `idem_store` afterward. Parallel same-key requests therefore require an explicit race test; a raw unique-violation, duplicate side effect, or divergent response is a fail.

## Terminal disposition rules

A future real-staging **PASS** requires an exact released staging target, synthetic fixtures, all applicable table/static/leakage/command/concurrency/adapter gates passing, and AMB-01..04 bound by the released contract. A failure in any cross-section/profile/removed-member privacy gate, direct-write boundary, or parallel mutation integrity is **FAIL/AMEND** with the smallest correction. Missing target/release/real-auth evidence or unresolved contract ambiguity is **HOLD**, not a guessed PASS.

## Current boundary

Q-S12 changes no StudyGrid product/runtime/UI bytes and applies no SQL. It does not validate, pre-approve or influence unreleased Slice 3 UI. It does not claim Supabase staging, production, deployment or canonical acceptance.
