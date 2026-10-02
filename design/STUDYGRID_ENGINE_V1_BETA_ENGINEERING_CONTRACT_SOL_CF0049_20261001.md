# StudyGrid Engine v1 — minimal beta engineering contract

Prepared by Sol engineering CF-0049 for General CF-0047 · 2026-10-01

**Disposition: AMEND.** Draft 2 is a viable behavioural basis, but its logical records and freshness promises are not yet an executable engineering contract. Adopt the amendments below through General reconciliation before a builder receives implementation authority. This is a design return: no implementation, migrations, provider changes, frontend changes, release or canonical promotion.

## 1. Smallest defensible architecture and scope

One application, one PostgreSQL database, one typed command/read adapter. A database-polled evaluation queue is sufficient; no external event bus, graph service, feature store or second learner-state database. Pure policy calculation runs outside short database transactions; database commands accept its result under explicit guards. PostgreSQL on Supabase is the proposed deployment target, subject to provider compatibility and isolated acceptance.

Proposed first beta: online-only, one reviewed course-local package, low-stakes study, fixed approved teaching artifacts, deterministic D2-BETA-P0 policy, contract-evaluated evidence profiles. Single-choice and plain-text constructed responses are the proposed initial interaction subset; constructed responses remain pending human rubric review. Other interaction types refuse before presentation until separately supported and tested. No real learner scope or pilot size is authorised by this proposal.

The existing prototype can continue as a labelled synthetic fixture. Its display, rewards, navigation, local storage and calculated progress have no backend authority.

**Attack:** a small demo quietly becomes a general adaptive assessment platform. **Invariant:** publication declares supported types, stakes, scorers, reviewed claims and permitted uses; absent required declarations block the affected operation. Safe approved teaching may continue despite inference abstention.

## 2. Independent amendments to Draft 2

| Corruption path | Required smallest repair |
|---|---|
| Two tabs compute from one sequence while a score, support fact or mapping changes | Validate an input manifest and shared authority/stream guards in the acceptance transaction, not decision sequence alone. |
| A previously successful retry returns an answer after membership or reveal permission is revoked | Reauthorise every read/retry; command identity replays the accepted identity, never grants perpetual content access. |
| Hint reaches the browser, acknowledgement is lost, resume claims unaided performance | Record potential release before sending bytes; distinguish release, acknowledgement and uncertainty. Unknown answer exposure disqualifies unaided evidence. |
| Response commits, process crashes before scheduling evaluation | Commit recoverable pending evaluation state in the response transaction. A separate enqueue is insufficient. |
| Deadline/review window changes only because time passes | Re-evaluate trusted-time predicates at delivery; row-version equality alone is insufficient. |
| Old callbacks or cached snapshots resurrect deleted evidence | Deletion fences the subject/context before purge; jobs, retries, receipts, caches and snapshots obey that fence. |
| Late automatic score defeats a reviewed adjudication | Explicit evaluation-purpose head and expected-head compare-and-swap; arrival time is never adjudication authority. |

## 3. Concrete relational families and ownership

All IDs are server-issued opaque UUIDs; every foreign key involving scoped data includes `context_id`. Stable definition identity and version identity are different. Personal, course, preview and synthetic contexts never share runtime identities. Authentication subject IDs come from verified provider identity.

The following is the physical-schema target, not migration code. These relations can share the private application schema. Fixed discriminators and versioned payload schemas keep small definition/event families compact; they are not arbitrary EAV objects or a general relation graph.

| Relation | Minimum authoritative columns and constraints | Writer / mutability |
|---|---|---|
| `context` | id, kind, owning subject/organisation reference, lifecycle, authority generation, deletion generation | Authorised administration; revision-guarded current row. |
| `membership` | context, subject, role, permitted purpose, status, revision; unique context/subject/role | Authorised membership administrator; current authorisation, not client claims. |
| `package_version` | context, package stable id, version id, predecessor, immutable manifest, digest | Content publisher; immutable after publication/use. |
| `definition_version` | context, stable id, version id, kind, payload-schema version, typed payload, digest | Reviewed author. Fixed kinds: SOURCE, CONTENT, CLAIM, RESOURCE_TASK, RUBRIC, MAPPING, RELATION, ASSISTANCE_POLICY, NEXT_POLICY, RELEASE_RETENTION_POLICY. Semantic version immutable after use. |
| `definition_dependency` | context, dependent version, dependency version, fixed purpose, scoped endpoint kinds | Publisher; immutable version dependency. Mapping owns task/claim attribution; this relation records dependency, not a second assesses assertion. |
| `authority_head` | context, stable definition/use, active version, review state, usability, revision, latest review-event ref | Authorised reviewer; one current head per use. APPROVED and USABLE remain separate. |
| `learner_stream` | context, subject, event_seq, input_revision, decision_seq, session id, current decision/presentation refs, deletion generation | Commands only; unique subject/context. Sessions are subordinate; new session cannot erase exposure. |
| `presentation` | context, subject, stream, id/semantic slot, episode, decision ref or approved author sequence, task/resource/package/policy versions, selection/support contract refs, trusted sequence/time | Delivery command; immutable facts. Reattempt needs a new server-authorised slot retaining relevant exposure lineage. |
| `runtime_event` | context, stream or authority target, event id/kind, operation ref, sequence/time, bounded typed payload, actor/provenance | Append-only retained facts: release/acknowledgement, support, agency, missingness, review, correction, execution disposition. No raw-response copy. |
| `response` | context, subject, presentation/slot, response id/schema, raw artifact, digest, operation identity, server receipt sequence/time, optional untrusted client time | Response command; unique semantic slot. No score, claim mapping, mastery or inferred need. |
| `evaluation_revision` | context, response, purpose, revision, rubric/scorer/rater/config refs, operation id, typed result, validation, parent/head expected, provenance/time | Authorised evaluator/reviewer; append-only. Unique evaluator operation identity within response/purpose. |
| `evaluation_head` | context, response, purpose, active revision or null, resolution status, head revision, pending-work/lease fields | Evaluation command; one row per response/purpose. Recoverable PENDING marker doubles as the small evaluation queue. |
| `decision` | context, subject, stream, seq, request identity/digest, immutable input manifest, bounded actual features, complete candidate IDs/exclusions, branch/ties, action/version or no-action, reason codes, time boundary | Acceptance command; unique stream/seq and request scope. History immutable while retained. Current validity comes from heads/events, not rewritten historical inputs. |
| `command_receipt` | context, verified actor, command kind, operation id, payload identity, accepted record refs, bounded result metadata, expiry | Command transaction; unique actor/context/kind/operation. Contains no reusable answer payload or raw evidence. |
| `derived_cache` | context, subject/use, full dependency key, bounded projection, expiry | Replaceable computation only; omit initially if direct derivation suffices. Never learner truth. |
| `deletion_request` | context/subject scope, authorised purpose/disposition, generation, progress, permitted completion receipt | Governance command; current work state plus attributable events. Required before real personal data. |

Type-qualified foreign keys/checks prevent a task ref pointing to a rubric, cross-context links and evaluation heads pointing to another response/purpose. Package publication validates mandatory fields, endpoint kinds, cycles, rubric/component attribution and allowed response types. Typed personal payloads have explicit size limits; trace candidate pool is capped at 100. Do not put large raw artifacts in decisions.

Authority changes and runtime facts have one owner each. Current heads/leases may update; retained response, definition version, evaluation and decision meaning may not. Corrections append provenance and change current heads. Privacy deletion/redaction is an explicit exception to logical immutability, including identifying hashes and links where required.

**Attack:** two durable fields independently claim the current score or mapping. **Invariant:** exactly one purpose-qualified effective head; projections always name its revision. Effective score count is zero while pending/disputed/invalid, at most one otherwise.

## 4. Transactions, locks and crash recovery

Use the same lock protocol for every consequential writer. For this small beta, take the context authority guard first, then affected learner-stream rows in stable ID order, then evaluation/receipt rows. Membership, publication/revocation, grading activation, response/support/agency and deletion writers must participate. Context locking is a short commit guard, not a global recomputation request. Do not hold it across scoring, network I/O or policy calculation.

Snapshot calculation reads a consistent PostgreSQL snapshot and records context authority generation, stream input revision, event/evaluation/support heads, session/decision sequence, deletion generation and exact definition versions. Acceptance locks and compares current tokens. A mismatch returns STALE_INPUT and requires fresh calculation; it never substitutes another topic's decision. Bounded transaction retries handle serialization/deadlock failures with the same operation identity. Every material writer increments the appropriate input revision/generation in its transaction. No application-only mutex or read-then-write race is sufficient.

| Command / boundary | Atomic database work | Failure / recovery |
|---|---|---|
| Publish/review | Authorise reviewer; validate immutable definitions/dependencies; append review; update scoped heads/generation and affected-use barrier together | Failed publication leaves previous state. Unknown semantic impact quarantines affected dependencies before consumption. |
| Issue decision | Reauthorise; validate receipt/payload; compare snapshot, sequence, session and time; append decision/no-action, advance sequence/current head and receipt together | One distinct request can win from a given expected sequence. Stale different request is rejected; identical retry resolves its decision subject to current read permission. |
| Activate presentation | Lock/revalidate current head, authority, membership, support/reveal, artifact availability and trusted-time predicates; append presentation/slot and release intent, advance stream and receipt together | No protected/content bytes before commit. Duplicate activation reuses presentation identity. No-action decisions cannot activate. |
| Release support/feedback | Resolve task-scoped capability and accommodation authority; append release intent against existing episode, bump support/input revision; commit before bytes | Missing acknowledgement leaves possible exposure. Support retries need fresh permission and cannot reset exposure or create evidence. |
| Acknowledge display | Verify presentation/release ownership; append deduplicated acknowledgement | Acknowledgement is operational provenance, not attention or understanding proof. Lost acknowledgement is not absence of exposure. |
| Commit response | Verify actor owns historical presentation; validate typed payload/slot; check current submit authority and administration disposition; insert response, pending evaluation head/work marker, event/input revision and receipt together | Unique slot prevents two payloads/keys becoming two responses. Scheduling outage leaves durable PENDING work. No response overwrite. |
| Append/activate evaluation | Authenticate authorised rater/scorer; dedupe operation; validate pinned rubric/purpose; append revision; compare expected head and authority; update effective head and stream revision atomically | Stale/conflicting branch stays non-effective/review required. Callback retry is one revision. Invalid output never becomes zero. |
| Dismiss/finish/void | Verify scoped actor/expected current state; append disposition, change operational head and input revision, receipt | Agency/technical failure changes policy history only; not competence. Completing work is separate from satisfying a claim. |
| Delete/redact | Fence scope and cancel acceptance/jobs first; then bounded resumable purge of primary and dependent personal material; completion only after verified disposition | Late worker/retry with old generation refuses. Historical replay degrades. Purge failures stay pending, never reported complete. |

Submission after a task/source/policy revision remains bound to the original presentation and artifact. If authorised to submit, it can be retained with REVIEW_REQUIRED/CONTAMINATED disposition; it is not silently scored against the new task or treated as current usable evidence. Removed membership rejects submission. A denied submission creates no incorrect answer. A previously accepted response may be looked up only under present read permission.

### Delivery linearisation and uncertainty

The database release transaction is the permission linearisation point. A revocation committed before it prevents release. A revocation after it cannot retract bytes already authorised/in flight. Draft 2 must not promise instantaneous recall of information or exactly-once browser display. No reusable client delivery token, service-worker cache, prefetch or public artifact URL may bypass a new release check.

Before any answer-bearing bytes leave the server, persist `RELEASE_AUTHORISED`; a matching display receipt adds `DISPLAY_ACKNOWLEDGED`. Crash/lost acknowledgement produces `EXPOSURE_UNCERTAIN`. Relevant contract logic treats known or uncertain answer-bearing release conservatively, including across resume and fresh attempts. A later protection change marks affected existing opportunities contaminated and requires administration review/new authorised opportunity. The contract never claims to detect external/offline assistance.

**Attack:** a check outside the transaction races a policy writer; a crash loses the hint fact. **Invariant:** all authority writers share the guard, release provenance commits first, and uncertainty cannot support unaided evidence.

## 5. Idempotency, two tabs and evaluation precedence

Operation keys identify intent, not identity or permission. Scope is verified actor + context + command kind + key. Reuse with different payload returns IDEMPOTENCY_CONFLICT. Typed canonical payload identity must include task/presentation/version and preserve response-type semantics. Retrying a response after an unknown network result keeps the original key and slot, then performs status lookup; no automatic new attempt.

Same slot/same artifact with a different key returns ALREADY_COMMITTED to the existing response. Different artifact returns SLOT_CONFLICT with an authorised recovery option. Neither overwrites or doubles evidence. After receipt expiry, semantic constraints still prevent duplicate history. A decision's retained request identity is not forgotten merely because a receipt expired. After authorised deletion, old-generation operations refuse; they cannot recreate history.

One learner/context stream serialises accepted next actions and active presentation. A second tab may resume that presentation; a new action while it is active needs an explicit authorised abandon/switch disposition. Different devices do not invent independent slots by sending their own attempt ordinal. Accepting a newer decision invalidates any older undelivered head. An identical stale decision retry returns historical identity/status, not permission to reopen it.

Proposed beta score authority: a supported deterministic scorer can activate one validated initial result under its pinned rubric. The named authorised human reviewer may supersede it by expected-head adjudication. Automatic results cannot supersede human adjudication. A legitimate conflicting human branch with the same expected head sets the current head to DISPUTED with no effective revision until explicit resolution; unauthorised/malformed callbacks cannot force that state. No last-arrival winner. AI output is a non-effective annotation until a reviewed human act. Grade and evidence purposes remain separate if both are ever introduced; high-stakes grades are excluded here. General/content authority must approve this precedence before build release.

**Attack:** transport deduplication works but double-clicks generate new keys, or worker retry becomes a second performance. **Invariant:** semantic slot uniqueness, purpose-qualified evaluation head and stream-sequence uniqueness supplement receipts.

## 6. Pure decisions, replay and time

Keep Draft 2's ordered P0–P10/B0–B5 grammar, complete selected scope, pool cap 100, authored/recency/stable-ID ties and explicit no-action outcomes. Keep its versioned trial defaults: verified deadline window 48 hours, one automatic probe/claim and two/session, one unsolicited repair/pattern/session. These are policy hypotheses, not learning thresholds. SELECT_ACTION/REQUEST_HELP still need full eligibility. Invalid prerequisites do not imply learner failure; soft cycles quarantine relations, mandatory cycles block the affected administration.

The accepted manifest identifies actual then-used effective evaluations, support/exposure/dependence lineage, mappings/authority, policy/generator/derivation versions, session agency/budgets, scope/catalogue, trusted calculation instant, decisive features, candidate IDs/exclusions, selected alternatives and reason codes. Its snapshot has actual bounded feature values or authorised retained references; hashes alone are insufficient. No raw response, full source or accommodation declaration is duplicated into each decision.

Pure policy cannot read ambient current time, UI state or mutable global configuration. Time is an explicit trusted input. Record the earliest upcoming predicate boundary (deadline window, due review, expiry), when determinable. At delivery, recompute time-dependent predicates at the current trusted instant and recheck all material dependencies. No soft TTL exempts a material change. Changed scope/branch/tie/reason expires the decision even if the activity itself remains permitted.

FULL replay reproduces then-accepted candidate eligibility/order, selection and reason codes from retained authorised inputs, pinned definitions and pure calculator version. PARTIAL names missing categories and the narrower inspectable result; UNAVAILABLE refuses reconstruction. Current recomputation is a different operation and may disagree. Historical replay cannot regenerate AI output, use future scores or restore removed private inputs from logs/backups.

**Attack:** feature digest or current catalogue is presented as exact historical replay. **Invariant:** executable pure input manifest, exact retained versions/values and explicit replay availability. No learning-efficacy claim follows from deterministic conformance.

## 7. Revision invalidation

| Change | Current-use barrier and effect |
|---|---|
| Reviewed cosmetic source edit | New version plus authorised equivalence; preserve approved interpretation. Version increment alone does not regress evidence. |
| Semantic/unknown source impact | Quarantine named affected uses/dependency closure atomically before new consumption. Unknown affected closure requires conservative block of that bounded package until review, not unsupported selective certainty. |
| Mapping correction | Record FUTURE_ONLY / RETROACTIVE_SAFE / INVALIDATE_PRIOR / HUMAN_REVIEW_REQUIRED. One effective interpretation per response/purpose; A invalidation is not B credit. Joint evidence remains joint. |
| Evaluation activation/regrade | Change effective head and stream input revision; affected profiles/decisions refresh even without new response. Preserve raw response and previous result. |
| Derivation/model version | Re-key affected profiles/current decisions; retain historical config. Beta has no learned latent model. |
| Policy/goal/deadline/support/agency change | Expire dependent undelivered decisions and reasons; change learner profile only when actual evidence-validity conditions change. |
| Membership/assistance/availability revocation | Immediate current-release barrier and reauthorisation on reads/retries. Existing released content cannot be recalled. |
| Correction/void/deletion | Stop affected evidence contribution, bump generations, invalidate dependent personal projections; deletion also purges under governance. |

Use existing definition dependencies and runtime manifests for affected-use selection. A coarse context generation can conservatively reject in-flight acceptance; it must not compel recomputation of every unrelated profile. If exact dependency information is missing, fail safely within the bounded affected scope.

**Attack:** a late score leaves response-count cache unchanged, or remap counts A and B twice. **Invariant:** cache keys include all effective-head/support/authority dependencies and only one approved current interpretation lineage contributes.

## 8. Auth, RLS and API trust boundary

The browser supplies operation IDs, expected revisions and scoped requested actions. It never supplies an authoritative learner identity, actor role, membership, score, eligibility, approved mapping or permission. A learner command resolves its subject from verified JWT identity; instructor commands name a target subject only after database membership/purpose checks. Do not authorise from editable user metadata or rely on stale JWT role metadata to prove current membership.

Proposed seam: authenticated user JWT invokes a small `api` schema of SECURITY INVOKER read/command wrappers. Data and privileged helpers remain in private `app` schema. Any necessary private SECURITY DEFINER helper has explicit identity/purpose checks, empty search path, fully qualified objects, minimal EXECUTE grants and a non-login/non-BYPASSRLS owner. Revoke default PUBLIC function execution. Do not put a privileged definer helper in the exposed schema. RLS protects every scoped table; FORCE RLS applies to the proposed app-owner design. Views use invoker security or are replaced by guarded read functions. Privilege/role-bootstrap feasibility is a provider gate, not an assumed installed fact.

RLS is not the entire command contract: tables have no client direct-write grants, and typed commands check workflow invariants. Composite scoped foreign keys defend against cross-context mistakes even inside privileged code. Test impersonation through request payloads, private function/schema discovery, direct writes and stale/removed membership. A service-role key is never a browser key or shortcut for ordinary learner commands; it bypasses RLS. Evaluation work uses a narrowly scoped worker claim interface, never broad cross-section AI reads. If real provider privileges cannot support this seam, hold and choose one audited server gateway; do not silently switch to service-role CRUD.

No real responses, secrets or identifying institutional records enter the public repository. This return contains design and synthetic scenarios only.

**Attack:** a technically typed RPC still accepts client `actor_role`, or a definer bypasses the RLS test matrix. **Invariant:** verified subject, current database membership, scoped constraints, least privilege and real-provider JWT tests jointly enforce the boundary.

## 9. Privacy, deletion and instructor release

Before real personal data, approve a purpose/role-specific retention profile covering raw artifacts, evaluations, decision features/refs, receipts, accommodation capability refs, caches, debug logs and provider backups. Exact periods are governance decisions; this report supplies no legal retention rule. No optional telemetry or training use is implied.

Store the minimum task-scoped capability/authorisation ref needed for validity, never a diagnosis. Raw response is retained in one authorised location. Derived personal features and identity-bearing digests are still personal material, not anonymous merely because hashed. Delete traversal includes projections, instructor summaries, personal snapshot features, artifacts, queued work, logs where retained, and reference links. Minimal non-sensitive deletion receipt exists only if the approved profile permits it. Backup expiry/restore purge behaviour needs explicit provider evidence; restore must reapply deletion fences before access.

Instructor aggregates expose eligible/enrolled, presented, responded, effectively evaluated and inference-eligible denominators separately. No release without an approved field/scope/small-cell policy; suppression never falls back to raw evidence. Individual teaching access is a separate authorisation. Item/scorer invalidity remains an alternative to learner difficulty; no motivation, aptitude or instructor-quality inference.

**Attack:** deleting responses preserves the same private content in decision/debug snapshots. **Invariant:** deletion inventory and fenced resumable purge are accepted before COMPLETE; replay degrades honestly.

## 10. Offline and prototype migration

Beta is online-only for authoritative presentation, answer/support release, response commit, scoring and decisions. No offline queue or client-created decision. Connectivity loss preserves only an uncommitted in-memory draft and its original slot/key while the session remains authorised; it shows transport uncertainty until status lookup. No answer-bearing service-worker cache or prefetch. A user statement about offline study is bounded context, not evidence. Server receipt chronology cannot establish delayed recall when the actual occurrence is uncertain.

Preserve the existing `{ok,state,data|error}` gateway envelope. Add explicit typed state/version/identity fields without redesigning the product shell. Fixture and real adapters implement the same commands/read models, but fixture mode is conspicuous and uses separate synthetic context IDs. Current fixture data is not migrated as real learner evidence.

Migration sequence, only under a later release: inventory existing seam; define typed DTOs/statuses; demonstrate synthetic contract fixtures; independently accept backend; swap gateway adapter; accept integration. The frontend renders authorised projections and sends commands, then refetches. Optimistic interaction may show pending input but cannot locally mint scores, progress, claim strength or next decisions. A failed backend call cannot fall back to invented fixture success. Imported reviewed content needs an explicit versioned import; legacy contraction is separately held.

**Attack:** local progress synchronises into the backend as authoritative competence. **Invariant:** no learner-state write API; server projection owns evidence strength. UI strings cannot exceed UNMEASURED/INSUFFICIENT/CONTRACT_MET_UNDER_CONDITIONS/REVIEW_REQUIRED limits. No Learned/Mastered/Retained badge.

## 11. Minimum automated acceptance before staging

These are required suites for a future build, not tests executed in this review. Tie every result to exact build, migration/config bytes, versioned fixtures and retained receipts. Builder results are distinct from Stuart's independent acceptance.

| Suite | Minimum assertions / existing anchors |
|---|---|
| Publication and pure policy | Typed definitions, supported types, component/joint attribution, cycles, complete pool/overflow, deterministic branches/ties/no-action, agency/probe budgets, time-only boundary changes, no recommendation-as-evidence. Draft 2 F01–F25; Kevin's 38 scenarios with allowed/forbidden outcome assertions. |
| Database integrity and races | Five retries; two keys/one slot; conflicting two-tab payloads; simultaneous next/action activation; head-CAS score conflicts; late automatic vs human review; remap uniqueness; cross-context FKs; invalid/NaN score; expired receipts; preserved historical bytes. Bob C01–C36 corruption requirements. |
| Crash and recovery | Kill after response commit/before worker claim; after release commit/before send/ack; after evaluation append; during delete; retry after authority revocation. One response, recoverable pending work, conservative exposure and no private-data resurrection. |
| Security and delivery | Anon, learner, instructor, preview, removed member, wrong context, forged identity/role; direct-table write denial; grants/definer/search-path audit; protected input denial and independent authorised accommodation; no content cache bypass. Real JWT/provider execution is a separate isolated-stage gate. |
| Replay and privacy | FULL deterministic reconstruction; late score changes current state but not history; PARTIAL/UNAVAILABLE after purge; all dependent personal copies gone; revoked retry cannot release content; backup restore/deletion fence acceptance. |
| Adapter/projection/accessibility | Pending/conflict/stale/unsupported states; no fixture fallback; no stronger labels; exact denominators/privacy suppression; supported input keyboard/touch/access equivalents; preview produces no learner evidence. |

Stuart M01–M20 is mandatory. The full 76-case matrix and Kevin 38-case set must be dispositioned by applicable scope: unsupported features have explicit refusal tests and remain held, never silently omitted or called PASS. Synthetic unit/database suites run before isolated staging; real JWTs, exposed-schema/grant settings, pooler races, advisors and deployment readback run on isolated synthetic staging before any backend conformance claim. No local auth shim or historical 1223/1223 count proves this Engine-v1 provider seam.

Hard stops: protected coaching leak, cross-context access/evidence leak, duplicate evidence, destructive history rewrite or consequential UI evidence-strength inversion. Source/scoring/mapping defects quarantine affected flows. Green integrity fixtures prove programmed behaviour, not psychometric validity, retention calibration or causal learning benefit.

## 12. Exact remaining decisions and holds

| Decision / evidence | Accountable owner | Required before |
|---|---|---|
| Adopt this engineering amendment, initial single-choice/plain-text subset, online-only low-stakes baseline and proposed score precedence | General, content/scoring authority; owner for pilot scope | Builder release. This report is a proposal, not that release. |
| Selected package, reviewers, sufficient evidence/use contracts, fixed resources, approved response/rubric contracts and policy defaults | Content/research authority through General | Package publication/pilot. No universal sufficiency thresholds. |
| Actual learner cohort, protected stakes, task accommodations, individual/instructor release and descriptive stop protocol | Owner/institutional authority through General | Real pilot authorisation. Live protected administration is held from baseline. |
| Retention periods, purge inventory, receipt lifetime, deletion workflow, permitted log/backup disposition and purposes | Accountable governance/provider owners | Any real personal data. Transport key expiry never weakens semantic uniqueness. |
| Reconciled C-F successor vs C-E assumptions; role bootstrap/grants/private helper model, crypto, join-code retry, job-scoped worker and exposed API configuration | Claude/backend and General; provider evidence | Isolated provider installation. Reuse compatible pieces only after explicit gap mapping; Engine-v1 meaning is not inferred from older SQL. |
| Isolated environment organisation and exact quoted cost, real Auth/JWT/RLS/pooler behaviour, advisors/readback | Owner/provider via General; independent Stuart acceptance | Creation/installation and later real adapter release. No environment was created here. |

The accessible staging preflight is dated 2026-10-01 11:09 ET. It identifies compatibility gaps and a non-applied C-E pack; its provider observations are not independently refreshed by this review. The current C-F completion/application outcome is not verified here. General must resolve exact successor bytes and current environment state; do not classify a newer repair as missing merely from this source.

**Must not implement yet:** production engine or migrations from this review; live protected/high-stakes administration; AI scores as effective authority; unrestricted AI worker/service-role access; storage ingestion; offline authoring/submit queues; universal KC/graph/learner models; BKT/PFA/IRT, mastery/retention percentages, learned policies or causal efficacy dashboards; physical competence inference; cross-course evidence transfer; behavioural surveillance; broad analytics without release policy; deployment or M8 legacy contraction. No frontend or existing provider mutation is authorised by this task.

## 13. Source and route receipt

This is a distinct engineering lane CF-0049; CF-0043's website guard was not claimed or changed. General CF-0047 owns reconciliation and later releases. Direct return is persisted in the authorised project repository; no owner courier or peer wake is needed.

| Consumed input | Exact locator |
|---|---|
| Current engineering route | `routes/GENERAL_20261001_2055_SOL_PARALLEL_ENGINEERING_INTEGRITY_REVIEW.txt` at `e06c25ecc48889ab5924537551ce37bcc30ce514`; blob `71f90d7129c402ea8c349146f0634fac4ed1a6ee`. |
| General reconciliation | `design/STUDYGRID_ENGINE_V1_DRAFT2_GENERAL_RECONCILIATION_20261001.md` at `b6ac02d321293a46002636f6e6286e1f067e9ea8`; blob `8900f6925098f8b147b7eaa2657d4b2811a25f05`. |
| Proposed Draft 2, complete body | Library `libfile_d96012326aa881919348e1fb00590a81`, 567 lines, 79,729 bytes; publication pointer `fa11e4fb728a899ae65df2a42c15887359dba14d`, `design/STUDYGRID_ENGINE_V1_FIRST_PRINCIPLES_DRAFT_2_PROPOSED.md`. Body consumed from Library, not assumed fetched from the publication pointer. |
| Bob complete data/replay contract | `routes/BOB_20261001_2014_ENGINE_V1_DATA_REPLAY_CONTRACT_DONE.txt` at `7c637cf86bf9d7727f2f1928bb74276af8d72f7f`; blob `a24c51ac09e978b8f1cd1c7a3488bd99a907ae82`. |
| Stuart return and matrix | Return at `2454712068900e8d87599582c8841ed8e32925c1`, blob `28c8fb8be695b4863da5319635abe0678a4956e4`; matrix `reports/STUART_ENGINE_V1_ADVERSARIAL_FALSIFICATION_REGRESSION_MATRIX.txt`, blob `5dd981a86590b5d5314e5f0f3d538a6557effa06`. |
| Kevin return and report | Return at `7f5926287f17310b6b3e54b87cc69f9ef1d807bc`, blob `df7131918b1ac08b49db406214c68810eca6c512`; REPORT.md at `0aa96f5f832744f9bf051ab9bcb663c00398571e`, blob `8c8bede84f386d2a982ebecefd3087d853195cbe`. This review consumed return/report; the underlying 38 scenario bodies were not independently re-audited. |
| Staging preflight | Drive-native document titled “StudyGrid — Supabase Staging Preflight & Repair Packet — 2026-10-01”, prepared General CF-0047 11:09 ET; read as dated evidence only. Private provider details are not exported here. |

Current primary technical references checked 2026-10-01: [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security), [securing the Data API](https://supabase.com/docs/guides/api/securing-your-api), [custom schemas](https://supabase.com/docs/guides/api/using-custom-schemas), [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html), [explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html). These establish mechanism boundaries, not evidence that this project is configured or conforms. No changelog compatibility claim is made.

Final engineering judgement: **AMEND with this bounded contract; implementation and provider readiness remain gated.** The required design work is complete. None of the future suites is represented as executed or passed.
