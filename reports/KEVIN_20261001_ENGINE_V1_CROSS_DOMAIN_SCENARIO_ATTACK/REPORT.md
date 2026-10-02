# StudyGrid Engine v1 — Kevin cross-domain scenario / behaviour attack

**From:** StudyGrid Worker Kevin  
**To:** ChatGPT General CF-0047  
**Date:** 2026-10-01  
**Status:** DESIGN / BEHAVIOUR QA ONLY — NO IMPLEMENTATION

## 1. Exact authority and inputs

Owner activation: “Check routing — Kevin. Consume General CF-0047’s current StudyGrid Engine v1 cross-domain scenario/behaviour attack route. Do not implement.”

Exact current route consumed:
- `routes/GENERAL_20261001_2006_KEVIN_ENGINE_V1_CROSS_DOMAIN_SCENARIO_ATTACK.txt` @ `5e7d22ed3b1ba8082faea93c22c4952be73083a0`

Mandatory inputs consumed in full before this return:
- Draft 1: `design/STUDYGRID_ENGINE_V1_FIRST_PRINCIPLES_DRAFT_1.txt` @ `bc1a346cf6c6a95d081804e2d60d980533d16d61`
- Research adversarial return @ `93dbc55c00579128a2b96cbb44c8094c5ff9b007`
- Sol independent architecture attack @ `1e5c05892101d566ae316f4eb34c3f5a477ba8fa`
- Bob implementation-contradiction return @ `4b2849f6fda9e75205cb4cad516a550080cdfa7d`

Scenario artifacts:
- `SCENARIOS_A_K01_K20.md`
- `SCENARIOS_B_K21_K38.md`

This report does not adopt another lane by agreement. The other inputs were treated as required hypotheses/constraints and then attacked with concrete learner/course histories.

## 2. Bottom line

**Disposition: REVISE before implementation specification.**

Draft 1’s most important epistemic boundaries survive the scenario attack: observation is not interpretation; missing data is not learner weakness; learner override is not mastery/motivation evidence; protected assessment can forbid tutoring while accessibility remains available; source/version authority matters; repeated answer-exposed success is not automatically transfer; no universal retained/mastery truth is justified.

The remaining problem is behavioural completeness. Draft 1 often names the right factors but does not always tell the engine what to do when several factors collide, when no safe action exists, when evidence is pending/invalid/incomparable, when a recommendation becomes stale before delivery, or when its own adaptive choices shape the evidence it later sees. In those cases two implementations can both claim Draft-1 compliance and make materially different learner decisions.

The 38 scenarios therefore do **not** justify more learner-model sophistication. They justify a smaller, more explicit runtime decision contract.

## 3. Required-route scenario coverage

| Routed scenario type | Covered by |
|---|---|
| Brand-new learner / no evidence | K01, K31 |
| Correct recognition / failed application | K02 |
| Repeated correct after answer exposure | K03, K22 |
| One hard miss after strong performance | K09, K28 |
| Repeated comparable errors | K10, K25 |
| Invalid/broken question | K17 |
| Scorer disagreement / late regrade | K07, K34 |
| Prerequisite unknown vs weak | K12 |
| Prerequisite cycle | K13 |
| Imminent assessment vs weak prerequisite | K06, K31 |
| Learner explicitly asks for help | K05, K19 |
| Learner rejects recommendation | K20 |
| Learner wants to keep going despite struggle | K21 |
| Protected quiz/exam where coaching forbidden | K05, K30 |
| Low-stakes practice where gentle help is useful | K19, K25 |
| Stale recommendation after source/policy change | K29 |
| Two valid next actions tied | K16 |
| No valid next action | K18 |
| Accommodation/support present | K15, K30 |
| Incomplete/missing telemetry | K24 |
| Offline attempt syncing later | K14 |
| Long gap since prior success | K23, K26 |
| Course source conflict/supersession | K04, K27 |
| Multi-part problem covering several skills | K11 |
| Self-directed topic outside immediate sequence | K08, K35 |
| Prior recommendation becoming its own evidence | K37 |
| Nudge overuse / no graceful escape | K20, K21, K36 |

Domains represented independently: law/policy, engineering, mathematics, biology/health science, reading/writing/humanities, plus cross-domain feedback-loop cases.

## 4. Concrete remaining defects and smallest repairs

### K-R1 — The policy needs normative precedence, not a factor list
**Failure exposed:** K06, K08, K16, K20, K31, K35. A deadline, learner-selected goal, prerequisite signal, scheduled review and package sequence can all be valid simultaneously. Draft 1 names them but does not fully define dominance/ties.

**Smallest repair:** Write a short ordered decision grammar for beta. Integrity/access constraints filter first. An eligible explicit learner request sets scope unless a real hard course/assessment rule forbids it. Within scope, explicit help requests, attributable repeated-error support, cold-start/insufficient-evidence handling, declared scheduled review and package fallback must have a named order. Ties use a stable declared rule. Do not use an opaque weighted utility to hide unresolved precedence.

### K-R2 — First-class no-action outcomes are required
**Failure exposed:** K18. If every action is inaccessible, unsupported, invalid or unavailable, forcing an action creates either an integrity failure or a lie such as “complete.”

**Smallest repair:** Add explicit terminal decision outcomes such as `NO_ELIGIBLE_ACTION`, `BLOCKED_CONFIGURATION`, `PENDING_REVIEW` and `UNSUPPORTED`, each with permitted learner escape routes. “No safe action” is a valid engine result.

### K-R3 — Evidence status needs more than one generic uncertainty bucket
**Failure exposed:** K02, K07, K12, K14, K17, K24, K27, K33. Channel divergence, missing evidence, pending submission, invalid item, source conflict and scorer disagreement demand different actions.

**Smallest repair:** Preserve separate reason states at least for `UNMEASURED`, `PENDING`, `INVALID/LOW_QUALITY`, `CHANNEL_DIVERGENCE/INCOMPARABLE`, `COMPARABLE_CONFLICT`, `SOURCE_OR_MAPPING_UNCERTAIN`, `STALE`, and `MODEL/CONSTRUCT_UNSUPPORTED`. These may coexist as flags; do not force them into one ordinal mastery/uncertainty value.

### K-R4 — Evidence sufficiency must be author-time and claim/condition specific
**Failure exposed:** K02, K03, K11, K22, K32, K33. A count of correct answers cannot decide whether recognition, application, transfer or constructed reasoning is demonstrated.

**Smallest repair:** Each operational claim/evidence contract must define construct, valid task families/conditions, criterion coverage, support/exposure rules, sufficient pattern and disqualifiers. Runtime responses satisfy or fail that contract; they are not part of the contract definition itself.

### K-R5 — Exposure and task-family lineage must survive UI/attempt boundaries
**Failure exposed:** K03, K19, K22. Answer exposure followed by a new nominal attempt can otherwise be mislabeled unaided; cosmetic variants can masquerade as independent transfer evidence.

**Smallest repair:** Add episode/exposure lineage and task-family dependency semantics. “Unaided” means no known answer-bearing support within the relevant contract window, not `hintCount == 0` inside the current screen/attempt.

### K-R6 — Multi-claim evidence needs joint/component attribution rules
**Failure exposed:** K11 and K34. One wrong multi-skill response cannot automatically decrement every mapped claim, and a remap cannot make one response count twice.

**Smallest repair:** Evidence mappings declare `COMPONENT_ATTRIBUTABLE` versus `JOINT/CONJUNCTIVE/DIAGNOSTIC`. Per-claim positive/negative evidence requires a rubric component that isolates that claim. Mapping revisions define retrospective applicability and exactly one effective interpretation lineage.

### K-R7 — Immutable response and revisable scoring must be split
**Failure exposed:** K07, K34. A response can be stable while a score/rubric/mapping is corrected later.

**Smallest repair:** Keep committed response/presentation facts immutable while retained; make score/evaluation results append-only with scorer/rubric/version and supersession. Interpretations/estimates consume the effective result, never duplicate the learner performance.

### K-R8 — Unknown prerequisite and bad graph must never become learner failure
**Failure exposed:** K12, K13. Missing evidence can deadlock a hard-prerequisite implementation, while a soft cycle can trap a learner indefinitely.

**Smallest repair:** `UNKNOWN ≠ FAILED`. Hard access prerequisites require approved authority. Soft/hypothesised readiness edges may create a probe/repair candidate but not an absolute block. Invalid cycles quarantine the relation, not the learner.

### K-R9 — Unsolicited help needs an episode budget; explicit help stays available
**Failure exposed:** K20, K21, K25, K36. A rule like “struggle detected → help” can become nagging or forced remediation.

**Smallest repair:** One unsolicited help/repair offer per relevant episode/pattern by default for beta; after dismissal/Keep going, suppress repetition until a materially new pattern, scope change or independent probe. A new explicit learner help request can still be honoured where policy permits. Override/dismissal never changes mastery/motivation state.

### K-R10 — Recommendations must be revalidated at delivery
**Failure exposed:** K29. Source, mapping, access or assessment policy can change after recommendation issue and before content opens.

**Smallest repair:** Treat recommendation `ISSUE` and content/support `DELIVERY` as separate lifecycle points. Revalidate material authority, support/reveal policy, mapping/access and availability at delivery; expire/recompute stale actions. Historical reason traces remain historical, not current execution authority.

### K-R11 — Authoritative chronology must be explicit
**Failure exposed:** K14, K23. Offline/client clocks cannot safely establish delay, recency or retention evidence.

**Smallest repair:** Store server-received ordering/sequence as authoritative ingestion chronology plus optional client occurrence time and clock provenance. Any delayed-retrieval claim must state which chronology is trusted; uncertain time cannot become quantified forgetting/retention evidence.

### K-R12 — Content/software/scoring defects need a non-learner route
**Failure exposed:** K17, K24, K33, K34. Broken item, pending transport, confounded prompt or bad mapping can otherwise trigger remediation.

**Smallest repair:** Before learner-state update, evidence validity gates can return `INVALID`, `PENDING`, `REVIEW_REQUIRED` or `CONFOUND`. Those states route to content/software/scoring review or a valid replacement task, not learner weakness.

### K-R13 — Source revision must change authority selectively, not competence globally
**Failure exposed:** K04, K27, K29. A changed rule may invalidate current content interpretations without making the learner broadly less capable.

**Smallest repair:** Source revisions carry semantic-impact scope/affected dependencies. Historical observations remain historical; current interpretations are selectively revalidated. Source conflict is an authority problem until learner evidence actually demonstrates confusion.

### K-R14 — Adaptive selection must be recorded as a confound, not validation
**Failure exposed:** K37. The engine chooses what evidence it gets to observe. If it repeatedly samples a suspected gap, later misses are not independent proof that the original hypothesis/recommendation was causally correct.

**Smallest repair:** Observations link to the triggering decision/intervention and candidate scope. Learner estimates may consume the actual performance but never the prior recommendation/hypothesis as evidence. Escalating a hypothesis requires independent/disconfirming opportunities where practical. Instructor analytics must disclose policy-selected sampling and avoid causal claims from it.

### K-R15 — Authority scope must separate personal study from course authority
**Failure exposed:** K08, K27, K38. “Unapproved” cannot mean “unusable for any personal study,” and personal notes cannot silently become course truth.

**Smallest repair:** Make authority scope explicit: personal/provisional versus course-approved/consequential. Personal material may support labelled private study where permitted; graded/course claims use authorised course sources. Approval and factual/source validity remain separate concepts.

## 5. What Draft 1 already gets right and should not be weakened

Keep these as hard behavioural constraints:
- observation/history is not learner truth;
- exposure/completion is not mastery;
- coached performance stays distinguishable from unaided performance;
- repeated identical/answer-exposed success is not automatic transfer;
- override/nonresponse/latency are not motivation, intelligence or engagement evidence;
- accessibility is not generic tutoring assistance;
- protected assessment forbids unauthorised coaching;
- missing/invalid evidence can block a strong claim;
- no universal durable `retained=true` or fake precision;
- source/model/policy versions and decision reasons remain inspectable;
- optional intrusive telemetry is not required for the core engine;
- learner can escape a misguided recommendation whenever assessment/access policy permits.

## 6. Behavioural acceptance fixtures for Draft 2

The 38 scenarios should become design-level acceptance fixtures before implementation release. The minimum pass condition is not “the engine picked Kevin’s favourite pedagogy.” It is that, for each fixture, the implemented policy produces only an allowed action/outcome, never a forbidden inference/action, emits a simple learner reason consistent with the real decision path, and records enough internal reason/version lineage to explain why.

Draft 2 should specifically prove deterministic handling of: policy precedence/ties; no-action; unknown vs invalid vs pending vs divergent evidence; answer-exposure lineage; multi-claim attribution; regrade/remap; prerequisite cycles; nudge budgets; issue-to-delivery staleness; offline chronology; and policy-selected evidence.

These are specification fixtures, not executed software PASS results and not evidence of educational efficacy.

## 7. Terminal recommendation to General CF-0047

**AMEND / REVISE Draft 1 before any implementation specification.** Keep the conservative epistemic model. Make the runtime policy smaller and more explicit rather than adding sophisticated learner models.

The scenario attack most strongly supports four structural changes for Draft 2:
1. an explicit ordered decision grammar with ties and no-action outcomes;
2. a richer evidence-status/sufficiency contract with exposure and component lineage;
3. a recommendation execution lifecycle that handles staleness, regrades/remaps and authoritative chronology;
4. bounded agency/help semantics that prevent remediation loops and self-confirming adaptation.

No code, frontend, backend, auth, Supabase, deploy, canonical product state or peer-worker state was changed by Kevin.
