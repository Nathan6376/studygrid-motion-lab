# StudyGrid — Prototype ↔ Engine v1 Adapter Contract

Prepared by Sol Adapter CF-0050 for General CF-0047 · October 1, 2026
Status: PROPOSED INTEGRATION CONTRACT — design deliverable only. General owns acceptance. No implementation or backend release.

## Decision

Keep **one application gateway, one replaceable provider, three asynchronous operations**:

| Operation | Job |
|---|---|
| `read(scope)` | Return an authorised, internally consistent WorkspaceView. Reading does not start an activity, commit evidence or earn rewards. |
| `command(envelope)` | Accept one typed intent; return an operation receipt and refreshed WorkspaceView or a bounded failure. |
| `operation(context_ref, operation_id)` | Resolve a submission whose transport outcome is uncertain. No second submission identity merely because a response timed out. |

These are application contracts, not three prescribed HTTP routes or services. The fixture provider and future API provider have identical observable shapes and Promise behaviour. No generic CRUD, learner-state patch API, event bus or UI copy of the engine is needed.

**Reuse the existing StudyGridProductGateway composition point.** The exact accepted HTML already has readModels/commands and a private SG_PRODUCT_FIXTURE_ADAPTER for instructor data. Extend that gateway through a small learner-facing facade; retain existing instructor facades as delegates where useful. Do not put a second parallel gateway beside it. UI renderers use the gateway; only its selected provider accesses fixture records, fixture storage or HTTP. The existing instructor admin commands stay outside this learning-loop contract.

## Evidence and scope

Sources actually consumed:
- General adapter route `GENERAL_20261001_2056_SOL_PARALLEL_UI_ENGINE_ADAPTER_CONTRACT.txt`, blob `d84be44e7c2cb7b944ef06f093ce5b88042ba698`.
- General Draft 2 reconciliation, blob `8900f6925098f8b147b7eaa2657d4b2811a25f05`; website build-prep, blob `ea3dadfed8af410731629fa7a77c1cb97b76cc95`.
- Later Bob build release `GENERAL_20261001_2047_BOB_WEBSITE_PROTOTYPE_BUILD.txt`, blob `663ce91af3c34b5252bbbef9d37023ebdcbe0f47`: supersedes preparation-only frontend hold for Bob's bounded build. Backend implementation remains held.
- Owner product-flow, domain-neutral interaction and beta/non-timer UX deltas, read in full at their current repository paths.
- Complete proposed Draft 2, Library `libfile_d96012326aa881919348e1fb00590a81`, including S03/S06/S07/S10–S14/S16. Proposal is not independent accepted authority.
- Bob data/replay return, blob `a24c51ac09e978b8f1cd1c7a3488bd99a907ae82`.
- Research source/construct feeder, blob `217eb1ab0b0fbce86af28b93d5f30361fbe5766c`: source adjudication reported by Research, not independently repeated against its course PDF here.
- Exact accepted frontend downloaded and independently hashed: `StudyGrid-CF0042-QB17R2-stuart-defect-repair.html`, 1,063,586 bytes, SHA-256 `874e4a743050d308759a9dcaefa9cc3296f8841c37b12e3acf5df2225ea49aab`.

Source anchors: defaultState/storage at lines 1339–1425; legacy evidence/priority functions at 1520–1569; start/commit/finish families plus later overrides; domain-specific Branchline at 2345 onward; gateway at 3331–3354. Older function declarations are not proof of final runtime behaviour. Inspection confirms these coupling points; this work does not claim browser/native-input acceptance.

This packet proposes an application seam. It does not select database schema, authentication provider, RLS, retention periods, actual beta claim thresholds or production assessment enforcement.

## 1. Context and one read model

`read` takes a selected scope, such as a course or personal package, plus an optional episode to resume. It resolves the caller's permitted context and returns an opaque `context_ref`. Future services derive identity, role and permissions from authenticated authority; a client-supplied persona/learner ID is never authorisation.

| Context | Effect boundary |
|---|---|
| COURSE_LEARNER | Enrolled/authorised learner and course/package scope. Evidence and rewards can exist only under accepted backend policy. |
| PERSONAL_STUDY | Separate personal package and evidence namespace; provisional source status visible. No course credit/readiness transfer by matching names. |
| INSTRUCTOR_PREVIEW | Authorised preview of a package under its assessment policy. Synthetic episode only; no learner evidence, course progress, reward or publication. |
| Tonight's fixtures | All three scenarios carry `origin=FIXTURE`, synthetic identities and isolated namespaces. COURSE_LEARNER here simulates a learner; it is not a real learner record. |

Context reference binds principal/purpose/scope/environment and is opaque to UI. Switching class, personal scope or preview clears response drafts, support/feedback caches and outstanding display callbacks. Never rebind an existing presentation to a new context. An instructor choosing genuine personal study gets a new PERSONAL_STUDY context, not a relabelled preview episode.

A **WorkspaceView** contains just these optional sections, with shared envelope identity:

| Section | Minimum content |
|---|---|
| home | Current scope title, selectable authorised contexts, unfinished-work reference and meaningful upcoming items with source/status. Signed-in root is UI navigation; it never implies a new attempt. |
| up_next | Discriminated outcome: ACTION / NEED_CONTEXT / NO_ELIGIBLE_ACTION / BLOCKED / WORK_COMPLETE; one action reference/type/title, decision reference, actual reason code + short text, permitted alternatives. Optional effort estimate is descriptive, not the primary selector. |
| evidence | Bounded claim summaries: claim/version reference, disposition UNMEASURED / OBSERVED_INSUFFICIENT / CONTRACT_MET_UNDER_CONDITIONS / REVIEW_REQUIRED, conditions/time scope/reason flags and counts with denominators. Pending/invalid/dependent evidence is explicit. No mastery percentage or timeless retained flag. |
| activity | Episode/status, delivered presentation identity, task/content version, action type, prompt/instruction, typed interaction, visible option IDs/order, response-slot reference, submission/evaluation status and policy-permitted feedback/support. Lesson instructions and worked examples are valid activities, not empty quiz wrappers. |
| assessment | Mode/policy revision plus explicit permissions for coaching, examples, answer reveal, result reveal, pause/exit and content-bearing access support; missing policy blocks presentation. Presentation-scoped authorised access support is separate from tutoring. |
| completion | Work finished, outstanding/pending evaluations, actual bounded evidence change or no change, next action and optional reward receipt. Work completion is not competence completion. |
| preview | Explicit non-learner banner/effects-disabled field and synthetic result provenance; no live learner response body or unapproved cohort aggregates. |

Do not return every source body or full decision history. Supply source locators and a diagnostic reference; the backend retains its full version/cursor manifest. Per-section state is ready / pending / review_required / unavailable / error. `null` means not applicable, never zero evidence or false competence.

One view uses one opaque `view_revision`; UI cannot combine evidence from one view with next-action/assessment permissions from another. A returned view replaces the previous snapshot. Cosmetic filtering/tab/focus changes can remain local.

## 2. Minimum envelope and field ownership

Every reply names:
- `contract_version` (initial proposed major `sg-adapter/1`);
- `origin`: FIXTURE or SERVICE, and `environment`: prototype / staging / production;
- `context_ref`, `view_revision`, trusted `as_of` and clock provenance;
- version references actually needed by the client: `package_ref`, `policy_ref`, `content_ref` where delivered;
- `decision_ref`, `presentation_ref`, `response_ref`, `evaluation_ref` only where those records exist.

A fixture additionally identifies `fixture_set_ref`, deterministic scenario/clock and synthetic status. Fixture clocks are labelled fixture clocks. A content hash can be an integrity reference; it is not a substitute for retained content or replay inputs.

| Backend/provider-owned, UI read-only | UI-owned |
|---|---|
| Authorised context, presented IDs/versions/order, eligibility, recommendation/reason, evidence disposition, score/lineage/status, assessment permissions, persisted response receipt, delivered support facts, completion disposition, awarded reward receipt | Uncommitted answer/sequence draft, voluntarily selected pre-feedback confidence, chosen context/action intent, open panel, route, theme, focus, reduced motion, loading indicator |
| Effective package/source/mapping/rubric/scorer versions and trusted sequence/time | Optional client occurrence time, explicitly untrusted provenance |

UI never sends `correct`, `mastered`, `retained`, a score, a claim-state patch, a reward amount, `hintUsed=false` or an assertion of “no prior exposure.” A response supplies learner input; the provider resolves scoring/evidence/support lineage. Teacher/admin authoring has its own authority contract and does not patch learner views.

## 3. Typed commands and outcomes

All material commands carry `operation_id`, `context_ref`, `expected_view_revision`, `kind` and a kind-specific payload. IDs supplied by the view are opaque; never fabricate a new presentation/response slot on retry.

| kind | Payload | Normal receipt / view effect |
|---|---|---|
| START | Offered `action_ref` and `decision_ref`; optional supported scope preference | Delivery is revalidated; an episode/presentation is issued or existing active one returned. No evidence merely from start. |
| RESUME | Existing `episode_ref` | Current permitted activity and saved committed state; expired content/policy becomes blocked/review, not a silent new attempt. |
| COMMIT_RESPONSE | `presentation_ref`, `response_slot_ref`, `content_ref`, typed answer, optional pre-feedback confidence | One committed response receipt; evaluation separately pending/effective/review; policy-filtered feedback. Commit accepted does not mean scored. |
| REQUEST_HELP | Active presentation plus requested permitted support kind (instruction / worked_example / hint / approved_access_support) | Denial or authorised support artifact/delivery reference. A request alone is not help exposure. |
| ACK_DELIVERY | Provider-issued delivery reference and outcome RENDERED / FAILED / UNKNOWN | Records bounded rendering outcome, not reading/understanding. Needed only for evidence-relevant presented/support artifacts, not every screen/hover. |
| AGENCY | SKIP / DISMISS / ALTERNATIVE plus offered target/decision reference | Explicit agency disposition, refreshed eligible next action or no-action. Skip offered activity and dismiss unopened recommendation are distinct. Neither proves weakness. |
| SESSION | PAUSE / CONTINUE / COMPLETE / EXIT plus episode reference | Permitted operational transition, forward completion view or refusal. CONTINUE requests the next delivered activity; it does not increment a question index or grade locally. |

START may include an authorised offered teaching alternative; it does not force a diagnostic question because evidence is sparse. Choosing an arbitrary unknown action returns INVALID_COMMAND or UNAVAILABLE. COMPLETE means complete declared work/exit disposition; it cannot manufacture missing responses or credit.

For score delays, `read` retrieves a refreshed view when useful; no subscription/event-bus contract is required. Polling is bounded/backed off, cancellable on context change, and never generates a new decision just because a timer fires.

### Receipt meanings

Command result `outcome`: ACCEPTED / PENDING / REJECTED / UNKNOWN.
- ACCEPTED includes operation status and any created/existing response/delivery references. It acknowledges that command's effect only.
- PENDING names the stage: command acceptance versus evaluation. A committed answer with pending score remains submitted and cannot be resubmitted as a new performance.
- REJECTED has a stable code, safe short message, retry disposition and optional current view. No side effect is assumed beyond any explicit receipt.
- UNKNOWN is a client transport observation, not “server failed.” Preserve the draft and operation identity; lookup resolves it.

Normal command replies include the current WorkspaceView. Where a view is temporarily unavailable, a receipt remains valid and the UI reads later; it must not invent a success screen from a partial transport reply.

## 4. Interaction payload union

Every task declares one interaction `type`, version/schema, option IDs and constraints. Stable IDs are independent of displayed labels, letters and shuffled indexes.

| type | Answer payload | Validation / limits |
|---|---|---|
| single_select | `{"option_id":"o2"}` | Exactly one permitted ID. |
| multi_select_unordered | `{"option_ids":["o1","o3"]}` | Unique permitted IDs; semantic set equality ignores click order. Selection count constraints supplied by task; never scalar fallback. |
| sequence_order | `{"ordered_ids":["s2","s1","s3"]}` | Complete or explicitly permitted partial permutation; order retained. Numbered UI plus Move up/down/Choose position; dragging optional. |
| match_pair | `{"pairs":[{"left_id":"l1","right_id":"r2"}]}` | Cardinality/reuse rules declared, not guessed. |
| categorize | `{"placements":[{"item_id":"i1","category_id":"c2"}]}` | Permitted items/categories and completeness rules declared. |
| constructed_response | `{"text":"..."}` or an approved artifact reference | Versioned rubric; scoring pending/human review permitted. No fabricated automatic correct result. |
| numeric_formula | `{"value_text":"3.25","unit_id":"m"}` or `{"expression_text":"x+2"}` | Task declares numeric versus expression subtype, units/format; provider owns tolerances/equivalence. |
| hotspot_diagram | `{"region_ids":["region-a"]}` | Regions/diagram version stable. Coordinates only under an explicit coordinate-system schema; accessible labelled-region alternative required. |

Do not implement every family tonight to satisfy a shape. Fixture capability declaration lists implemented families. Unsupported type is UNAVAILABLE / UNSUPPORTED_INTERACTION before evidence presentation; no fallback to MCQ or “wrong.” Neutral sequence fixture proves the reusable interaction; it does not convert a component-identification task into ordering.

Research's current q4m disposition is **multi_select_unordered**; preserve source wording/IDs and remove misleading sequence language only through the accepted content repair. Correct/selected feedback is source text resolved from stable IDs, never “0,1,2.” Macooh source terminology stays; answer-bearing examples are withheld before commitment when the evidence/assessment contract requires it. Unresolved “Canascape” is not guessed into a legal term.

## 5. Errors, freshness and protected assessment

| State/code | UI response / evidence effect |
|---|---|
| EVALUATION_PENDING | “Submitted; review pending.” No correctness/competence conclusion. |
| REVIEW_REQUIRED / INVALID_CONTENT / SCORER_INVALID | Neutral content/technical review state; no learner failure or seed success. |
| NO_ELIGIBLE_ACTION | Honest bounded reason and permitted escape. Never call an all-excluded set complete. |
| UNSUPPORTED_INTERACTION / UNAVAILABLE | Preserve work; permitted alternative or retry. No substitute scoring type. |
| STALE_VIEW / STALE_DECISION / POLICY_CHANGED | Refresh; revalidate exact command target. Do not auto-send a response against a new task version. |
| OPERATION_CONFLICT / RESPONSE_SLOT_CONFLICT | Resolve existing receipt; changed answer under same slot requires explicit authorised reattempt. |
| UNAUTHORISED / CONTEXT_MISMATCH | Stop dependent delivery; clear sensitive caches and request authorised scope. |
| TRANSPORT_UNKNOWN / LOCAL_SAVE_FAILED | Preserve draft/receipt ID; resolve/retry same identity. No claim saved, awarded or failed as learner evidence. |
| SESSION_WORK_COMPLETE | Show completed work with pending evaluations separately; next action from provider. |

Hard policy is checked **inside the provider** at command acceptance and immediately before delivery. A client “assessment” toggle cannot create/remove protection. START/help/alternative/resume all enforce it; protected assessments may permit access support while denying tutoring. Pure UI access controls such as focus/zoom remain available; content-bearing aids use their separate authorised policy.

Permission booleans are display hints, not bearer permissions. The provider exposes permitted support/action references and classifies the actual requested artifact; renaming a tutoring request “access support” cannot authorise it. Confidence is optional, validated as pre-feedback when accepted, and remains a self-report outside strong competence claims. Delivery ACK binds the issued artifact even after a view changes; stale display state must not erase an actual historical delivery fact.

A protected reply omits answer keys, scoring rubric secrets, coaching/explanation/example artifacts and disallowed result feedback altogether. Hiding fields with CSS is insufficient. On practice→protected transition, invalidate/hide existing help panels immediately and remove route/global Explain/Ask/lesson shortcuts that would deliver barred content; replies from old contexts/views cannot reopen them. Previously delivered practice content cannot be made unseen: the provider preserves exposure and decides evidence eligibility honestly.

Support facts distinguish requested, issued, rendered/failed/unknown and revealed. If issuing already exposed answer-bearing content, do not let a missing ACK downgrade exposure to “unaided.” During uncertain delivery, use conservative unknown/support conditions, not `hintUsed=false`. Feedback reveal also contributes exposure to later attempts.

## 6. Retry, concurrency and UI freshness

1. Generate one operation identity per user intent before sending; retain it until resolved. Identical retries resolve the same effect; same ID with changed payload is conflict.
2. One final response per server-issued semantic response slot, even with different operation IDs or tabs. Reattempt requires a new authorised opportunity retaining prior exposure.
3. Start/delivery is semantically unique for the accepted decision; pause/complete/reward cannot duplicate on refresh or lost acknowledgement.
4. `expected_view_revision` is an opaque comparison token. The provider uses the engineering contract's context sequence/authority guards, not browser timestamps.
5. UI binds every response to context and request generation. An old/slower read cannot overwrite a newer view or changed scope. A duplicate commit receipt may be historical: show its receipt, then read current state; do not regress current view.
6. Commit binds the actually delivered task/version/support facts. New policy may mark an administration review-required; never silently score historical input under the newest rubric.
7. `operation` returns known receipt, pending, not_found, unavailable or unknown. Not_found does not prove the first request failed; retry the same identity. No automatic new ID.
8. Baseline real beta is online-only unless engineering accepts offline semantics. Local prototype persistence is labelled device/demo persistence. It is not an offline queue for production.

## 7. Example fixture request/reply shapes

Illustrative identities only; these JSON shapes are contract examples, not executable provider code. Omitted view sections are unchanged only in this printed excerpt; actual replies return one full consistent snapshot.

Read result for a synthetic course learner:

```json
{
  "contract_version": "sg-adapter/1",
  "origin": "FIXTURE",
  "environment": "prototype",
  "fixture_set_ref": "adapter-demo-v1",
  "context_ref": "fixture/course-learner-a",
  "view_revision": "fv12",
  "as_of": "2026-10-01T21:00:00-04:00",
  "clock": "FIXTURE",
  "package_ref": "demo-package:v2",
  "policy_ref": "practice-policy:v1",
  "view": {
    "home": {"scope_title": "Example class", "resume_episode_ref": null},
    "up_next": {
      "state": "ready",
      "outcome": "ACTION",
      "action_ref": "worked-example-1:v1",
      "type": "WORKED_EXAMPLE",
      "decision_ref": "fd7",
      "title": "Work through an example",
      "reason": {"code": "APPROVED_SEQUENCE", "text": "This unit starts with a worked example."},
      "alternatives": [{"action_ref": "practice-1:v1", "label": "Try practice"}]
    },
    "evidence": {
      "state": "ready",
      "claims": [{
        "claim_ref": "demo-claim:v1",
        "disposition": "UNMEASURED",
        "conditions": [],
        "usable_count": 0,
        "pending_count": 0,
        "denominator": 0
      }]
    },
    "activity": null,
    "assessment": {
      "mode": "PRACTICE",
      "policy_ref": "practice-policy:v1",
      "permissions": {"coaching": true, "examples": true, "answer_reveal": true, "result_reveal": true, "pause": true, "exit": true, "access_support": true}
    },
    "completion": null,
    "preview": {"synthetic": true, "live_learner_effects": false}
  }
}
```

Committed unordered response (task/presentation came from an earlier START):

```json
{
  "operation_id": "op-response-19",
  "context_ref": "fixture/course-learner-a",
  "expected_view_revision": "fv15",
  "kind": "COMMIT_RESPONSE",
  "payload": {
    "presentation_ref": "fp9",
    "response_slot_ref": "slot-fp9",
    "content_ref": "demo-multi:v1",
    "answer": {"type": "multi_select_unordered", "option_ids": ["identity", "purpose", "entry"]},
    "confidence": {"value": "fairly_sure", "timing": "BEFORE_FEEDBACK"}
  }
}
```

Receipt excerpt when answer is stored but review is pending:

```json
{
  "contract_version": "sg-adapter/1",
  "origin": "FIXTURE",
  "environment": "prototype",
  "context_ref": "fixture/course-learner-a",
  "view_revision": "fv16",
  "outcome": "ACCEPTED",
  "operation": {"operation_id": "op-response-19", "status": "COMMITTED"},
  "receipt": {
    "response_ref": "fr9",
    "response_slot_ref": "slot-fp9",
    "evaluation": {"status": "PENDING", "evaluation_ref": null},
    "reward": {"status": "NOT_AWARDED"}
  },
  "view": {
    "activity": {"presentation_ref": "fp9", "submission": "COMMITTED", "evaluation": "PENDING", "feedback": null},
    "completion": null
  }
}
```

Help blocked by current protected policy, even if the previous page enabled it:

```json
{
  "contract_version": "sg-adapter/1",
  "origin": "FIXTURE",
  "environment": "prototype",
  "context_ref": "fixture/course-learner-a",
  "view_revision": "fv20",
  "outcome": "REJECTED",
  "operation": {"operation_id": "op-help-21", "status": "REJECTED"},
  "error": {
    "code": "BLOCKED_POLICY",
    "message": "Coaching is unavailable during this assessment.",
    "retry": "REFRESH",
    "diagnostic_ref": "diag-21"
  },
  "view": {
    "assessment": {"mode": "PROTECTED", "policy_ref": "protected:v2", "permissions": {"coaching": false, "examples": false, "answer_reveal": false, "result_reveal": false, "pause": true, "exit": true, "access_support": true}},
    "activity": {"presentation_ref": "fp10", "feedback": null, "support": null}
  }
}
```

Sequence answer uses `{"type":"sequence_order","ordered_ids":["step-2","step-1","step-3"]}`. Input cannot contain the correct sequence. Preview commands can simulate the same receipts, with synthetic context and `live_learner_effects=false`; their result never merges into a learner context.

## 8. Small fixture set for tonight

Use deterministic private fixture records and the same asynchronous gateway, not live backend calls:

1. Approved instruction/example → practice → committed response → effective evaluation → bounded summary/next.
2. Unmeasured learner with useful approved teaching; no timer entry requirement.
3. Unordered multi-select and a separate neutral ordered task with non-drag controls.
4. Constructed response pending review; invalid item/scorer neutral state.
5. Practice→protected permission change while help response is in flight; approved access support remains.
6. Instructor preview and personal/course same-name claims remain isolated.
7. Lost submit reply/duplicate different keys/changed payload/stale view/out-of-order read.
8. Work completion with scores pending; no eligible action distinct from completion; failed local persistence/reward receipt.
9. Unsupported family and source-review hold.

These are proposed acceptance scenarios, not reported executed passes. Fixture fault injection/reset is test-only, separate from production capability. Correct keys/rubrics can live inside the fixture provider in self-contained HTML; label that build a demonstration and never claim it secures real exams. Future service responses must keep protected material server-side.

For rewards, automatically render an awarded receipt once; no extra Collect command. Pending/failed/not-awarded remain honest. Fixture awards are simulated rewards, never spendable live currency.

## 9. Migration without a renderer rewrite

| Stage | Work | Exit evidence |
|---|---|---|
| Prototype facade | Route bounded Home/Up Next/activity/summary/preview reads and learning commands through existing gateway; move their local simulation behind provider; keep UI preferences local. | Exact candidate inspected against checklist; deterministic fixture interaction evidence; no direct learner-truth writes in affected handlers. |
| Staging API provider | Map these application contracts to engineering-approved API/auth/transactions. Use authenticated authorised scopes, server ordering/versions, semantic uniqueness and real evaluation/receipt lookups. Reject fixture IDs on service writes. | Real provider tests for duplicate/tab races, unknown-write recovery, source/policy changes, access/preview isolation and held states. Simulated passes do not substitute. |
| Production provider | Explicit accepted environment/config/auth/retention/release gates; same renderers and version-compatible facade. | Separate production approval/deployment/provider checks. This packet supplies no authority to perform them. |

Legacy local attempts/derived Strong/remembered flags/rewards are not automatically imported as valid learner history. Start a new service namespace; any future import requires explicit migration/source/conditions review. Never import instructor preview as evidence. Service failure does not silently fall back to fixture success. Adapter selection is one configuration choice at the composition root; production has no user-toggleable demo-write fallback.

Do not refactor unrelated instructor authoring/global feedback/notes merely to complete this seam. Preserve their existing contracts. The professor recruitment/questionnaire request is a separate product scope for General; it is not hidden inside the learner engine API.

## 10. Bob candidate inspection checklist

- [ ] One gateway/provider seam; existing instructor gateway retained/delegated, no competing engine.
- [ ] All bounded learning-loop reads/commands are awaitable; pending/failure/context-switch paths work.
- [ ] Current view/context/version gates prevent stale replies and hybrid policy/evidence displays.
- [ ] No renderer/handler computes authoritative correctness, mastery, retained state, next policy or reward.
- [ ] No direct pushes to state.attempts/coinAwards/current evidence from the migrated learning handlers; those live behind the fixture provider only.
- [ ] Stable IDs/types, multi as set, sequence as ordered permutation; no display-index/scalar feedback fallback.
- [ ] Unsupported interactions refuse before evidence, not wrong or silent MCQ.
- [ ] Commit receipt/evaluation/feedback/completion/reward statuses remain separate.
- [ ] Duplicate keys/slots/lost replies resolve honestly; edited payload conflicts; no new opportunity on refresh.
- [ ] Explicit help/skip/dismiss/alternative are agency; no trait/competence inference.
- [ ] Protected payloads omit barred content; global/cached help paths obey current policy; access support remains independent.
- [ ] Delivery uncertainty never asserts unaided evidence; answer reveal carries exposure into later attempts.
- [ ] Instructor preview has no learner/reward effects; personal material cannot inherit course authority.
- [ ] Completion moves forward, reports pending work and bounded change; no permanent learned/retained percentage.
- [ ] Local storage/save failure cannot report submitted/awarded success; fixture provenance stays visible.
- [ ] Demo/service selection and namespaces are explicit; no automatic production fallback/import.
- [ ] Source-specific q4m/Macooh repairs follow Research/General; no guessed legal terminology.

Reject source-level anti-patterns: direct state-truth mutation; subject-specific scoring in renderer; Date.now as trusted ordering; client actor_role as authority; correct answers hidden in protected DOM; per-page fake scores/recommendations; “mark reviewed” advancing competence; completion assigning reward before persistence; shared preview/learner storage; switching adapter semantics from sync success to async network without pending handling.

**Acceptance scope:** this contract is complete as a proposed seam and fixture specification. Candidate compliance, real API behaviour, backend security and learning efficacy remain untested. Physical schema, effective-score precedence, hard policy versions/validity, exact beta interaction subset, retention and production authorisation remain engineering/General decisions.
