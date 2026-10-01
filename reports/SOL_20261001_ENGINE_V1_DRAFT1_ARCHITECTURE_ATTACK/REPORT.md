# StudyGrid Engine v1 Draft 1 — independent architecture attack

Sol CF-0043 → General CF-0047 · 2026-10-01 · Design review only

**Disposition: REVISE before implementation specification.** Keep the epistemic boundaries. Replace the catalogue of concepts with a small operational decision contract. Draft 1 has not yet specified a policy that can decide, an evidence contract that can declare sufficiency, or a lifecycle that can safely execute a stale recommendation. These are design defects, not demonstrated software bugs. No code, installation, product mutation or release was performed.

## 1. Architecture chosen from first principles

The first question is what decision the product must make, and what evidence can legitimately change that decision. I would choose a bounded, context-local decision service over an approved learning package. It receives a learner's selected context, permissible actions and evidence references; returns an authorised, available next activity with a reason or a truthful no-action outcome. It does not need a universal cognitive ontology or a probability of mastery to do that job.

Five responsibilities are sufficient:

1. **Learning package:** versioned sources, operational claims, tasks/resources, rubrics, approved mappings and a small policy profile. Optional external curriculum references. Approval has a named authority and scope. A personal draft package is distinguishable from course-approved instruction.
2. **Attempt history:** version-bound task presentations, committed responses, support deliveries and evaluation revisions. Events describe what the software or assessor recorded; they do not prove what happened in the learner's mind or outside the app.
3. **Evidence view:** claim/construct/condition-specific summaries, validity flags and unresolved uncertainty. Computed from evaluations and mappings. No universal learner score or need-for-teaching field.
4. **Decision function:** eligible action instances, a small ordered branching policy, explicit tie-breaking and bounded remediation. Assessment administration and session control have their own contracts.
5. **Execution/reconstruction envelope:** decision identity, input versions, reason codes and references; expiry/revalidation before delivery; outcome linkage. References have retention/access rules. Reconstruction may become unavailable after deletion.

Separate meanings do not imply five services, fifteen tables or full event sourcing. An initial implementation could later use one application and a few versioned records with derived views; Claude must choose the representation after attacking transactions. No architecture here authorises that implementation.

**Independence limitation:** the route required Draft 1 and its feeders to be read first. The baseline above is a first-principles derivation presented before the comparison, not a claim of a blind review. My earlier Q-SOL3 is product design evidence; it has no authority over this engine. Agreement among models is not validation.

## 2. Strongest concrete defects and smallest repairs

| ID / Draft 1 locator | Counterexample / consequence | Decision and smallest repair |
|---|---|---|
| A01 · §§11,22,27.7 | Prerequisite gap, tomorrow's assessment, learner's selected topic and overdue recall all apply. Draft names factors but neither dominance nor tie behaviour. Two engineers can implement incompatible policies while both claim compliance. | **REVISE:** adopt the explicit branching policy in §4 below as a beta hypothesis. Enumerate empty, unknown, tied and all-excluded outcomes. |
| A02 · §§3,6,27.2 | Contract lists an observed response and estimator version, but never the evidence pattern sufficient to support the claim. Three near-identical recognition items can satisfy an accidental count threshold for application. | **SPLIT:** author-time contract declares construct, conditions, coverage, disqualifiers and bounded sufficient pattern. Runtime evidence records its observations/evaluations against that contract. Do not put a future response into the definition. |
| A03 · §§5,25B/K | Recognition success and application failure are called conflicting evidence. They may be entirely compatible facts about different capabilities. Within-channel success then failure may reflect difficulty, learning or error, not logical contradiction. | **REVISE:** separate channel divergence, comparable mixed results, scorer disagreement and provenance invalidity. Only a declared comparability rule creates a conflict flag. Do not require mathematical uncertainty to increase after every mixed response. |
| A04 · §10 vs Research D1-07 | ADVANCE and COMPLETE are still listed as pedagogical types alongside EXPLAIN and ASSESS, despite the feeder explicitly requiring a split. REVIEW and REMEDIATE do not specify an operation. | **SPLIT:** learning operation (instruction/example/practice/probe), purpose and support policy, concrete resource/task instance, and session control. Review/remediation describe why an operation is chosen. |
| A05 · §§1,22 | Mandatory source assertions + outcomes + claims + general relation graph requires an instructor to build an ontology before twenty students can study. Personal notes may have no official outcome. | **REMOVE** mandatory universal assertion decomposition, KC subsystem and general graph from beta. Keep explicit operational claims and source pointers. Reify assertions only where conflicting/revised propositions need dependency identity. External outcomes are optional references. |
| A06 · §§4,19,20.1 | A scorer output is treated as something observed. Regrading it changes the result while the original response remains. 'Immutable facts' can accidentally preserve a wrong evaluator as final truth, or prevent correction/deletion. | **SPLIT:** response/presentation record, evaluation revision, interpretation revision. Append corrections/revocations; current views exclude superseded results. Logical append-only history is subordinate to declared deletion/retention rules. |
| A07 · §§11.2,13 | Unknown mastery of a hard prerequisite excludes every candidate, including the probe needed to resolve it. A soft cycle A→B→A traps a learner. Override could also bypass a genuinely protected assessment rule. | **REVISE:** unknown ≠ failed. Separate access/safety/assessment constraints from pedagogical readiness preferences. Invalid cycles quarantine affected edges, not learner ability. Override may switch eligible learning actions; it cannot grant forbidden access/support. |
| A08 · §§3,4,19 | A learner sees the answer, changes tab, resumes the same task as a nominally new attempt and is labelled unaided. Support count inside the second attempt is zero. | **ADD:** presentation/learning-episode identity and exposure lineage; support must be recorded when delivered, not merely requested. Prior answer exposure follows item/family and relevant claim conditions. Explicit unknown exposure prevents an unaided claim. |
| A09 · §§2,6 | Author labels five surface variants as five independent families. All share the same solution template. Diversity falsely satisfies transfer coverage. | **REVISE:** family identity describes assessed variation and dependency, with reviewer rationale. Correlated repeats count as practice, not independent coverage units. Transfer must have its own approved evidence contract. |
| A10 · §§11,19 | Recommendation issued under practice; activity becomes protected before the learner opens it. Cached explanation now leaks the answer. Versions recorded after delivery cannot prevent it. | **ADD:** issue→open→deliver→respond/evaluate lifecycle; revalidate policy/access/content at use, bind presentation to the permitted support/reveal snapshot, expire/recompute stale decisions. Server-authoritative enforcement is a later implementation requirement, not tested here. |
| A11 · §§11,19,20.9 | Trace records only candidates generated by a buggy generator. The best eligible source-linked task was never generated. 'Why this?' cannot reveal that omission. Full snapshots also duplicate free text and accommodation data. | **REVISE:** generator version + package/candidate-pool revision + scope + selected/excluded IDs/reasons + decisive rule path. Retain an authorised reconstruction manifest; no repeated raw response copies. Explicit FULL / PARTIAL / UNAVAILABLE status. |
| A12 · §§8,11,12 | Two misses trigger misconception M; all subsequent items diagnose M; policy interprets their errors as stronger M. Learner gets endless repairs. | **ADD:** diagnostic specificity, competing explanations, hypothesis expiry/revocation, a disconfirming probe option and episode-level help/remediation budget. Beta should label item/rubric error patterns, not persist an AI diagnosis graph. |
| A13 · §§1B,11.2,16 | Personal uploaded notes are unapproved course assertions. A blanket canonical-content exclusion makes personal study unusable. Conversely course approval can hide an internally contradictory source. | **REVISE:** authority scope (personal draft/course-approved), approval and source validity are independent. Personal provisional study may be explicit; unreviewed material cannot feed consequential course claims. Conflict/quarantine is still possible after approval. |
| A14 · §§15,17 | 'Three learners struggled' is descriptive but may be re-identifiable in a class of twenty; copying evidence into an instructor card expands access. An absence denominator makes six respondents look like all twenty. | **REVISE:** roster versus observed versus evaluated denominators; authorised individual/aggregate scope; item family/source filters; suppression/access policy. Start with inspectable item quality and coverage lists, no automated causal class insights. |
| A15 · §§7,11,22 | Age since practice becomes 'retention risk' despite no delayed evidence/model. A deadline changes, yet a cached urgency rank persists. | **REVISE:** author-scheduled review eligibility is an explicit scheduling hypothesis. Retention estimates absent unless construct/model justified. Policy inputs include current trusted clock and versioned deadline facts; absence is unknown, not zero. |
| A16 · §§14,26 | A shell choice or 'proprietary centre' framing becomes an engine invariant. Good policy implementation cannot rescue wrong claims, content or scoring. | **REMOVE** navigation/visual prescription and moat claim from normative engine contract. Link Q-SOL3/Gemini as separate product hypotheses. Preserve only execution, agency, reason and accessibility interfaces. |

These are independently reasoned additions/refinements. Research already raised source cascades, missingness, policy-selected evidence and privacy collisions; those are preserved, not claimed as new discoveries. A04 is a concrete feeder coverage miss in Draft 1.

## 3. Semantic layer diff

| Layer | Decision | Beta representation / boundary |
|---|---|---|
| Source artifact | **KEEP** | Stable artifact/version + source locator; content access separate from learner evidence. |
| Assertion/procedure | **REVISE** | Optional named source dependency where useful; do not normalise every sentence into an entity. Approval never proves universal truth. |
| Curriculum outcome | **REVISE** | Optional imported/approved external identifier; not required for personal contexts and not a KC. |
| Learning claim | **KEEP / REVISE** | Small operational claim + construct/conditions/sufficiency contract; bounded scope rather than general 'understands'. |
| Knowledge component | **REMOVE** from beta | Reserve extension boundary. No latent decomposition machinery without a decision that requires it. |
| Relation | **REVISE / SPLIT** | Typed source dependencies, task mappings and limited prerequisite declarations. These have different validation and authority rules; no universal graph editor. |
| Task and scoring | **SPLIT** | Task definition + response contract; evaluation artifact/revision; purpose/support belongs to presentation policy. One task can serve practice or diagnostic purpose. |
| Observation | **KEEP / REVISE** | Recorded presentation/response/support fact with episode identity; no intrinsic diagnostic weight. Software failure is explicit missing/invalid evidence. |
| Evidence interpretation | **KEEP / REVISE** | Versioned mapping/evaluation-use rule. Can be a derived result rather than another authored object per answer. |
| Learner estimate | **REVISE** | Evidence profile by construct and conditions; no beta latent probability. Separate performance history from evidence quality and freshness. |
| Misconception hypothesis | **REVISE / POSTPONE** | Reviewable rubric error pattern in beta; competing explanations, specificity and expiry. No permanent learner trait. |
| Context and policy | **SPLIT** | Owned input facts, explicit learner declarations, permissions and selected package/session versions. Unknown policy must not default to coaching. |
| Pedagogical action | **SPLIT** | Concrete operation + purpose + resource + support/reveal contract; navigation and completion outside the pedagogical ranking. |
| Policy decision | **KEEP / ADD** | Generator/pool scope, eligible candidates, ordered rule path, no-action outcomes, execution validity and outcome linkage. |
| Reason trace | **REVISE** | Derived from decision record; different learner/instructor/debug projections. Bounded references and stated reconstruction status. |

Merge storage where it simplifies ownership: claim + evidence contract may be one versioned definition; task + scorer specification may be one versioned package entry; decision + reconstruction manifest may be one record. Do not merge their meanings with historical response/evaluation results.

## 4. Explicit V1 policy that actually decides

The following is a **proposed beta policy**, not an established optimal pedagogy. It uses branch order and ordinal ties; it has no disguised additive score. Priority rule versions are hypotheses. Integrity/access constraints are contracts.

**Input:** selected context/package; course obligations; optional explicit topic/goal; active session stage; valid evidence profiles; available action instances; current permissions; current clock; bounded recommendation/help history. Every fact has source/owner/version; absent fields stay unknown.

**0 — Validate request and execution context.** Missing context/policy or invalid package yields BLOCKED_CONFIGURATION with source-review/setup option, not a diagnosis. An existing task resumes only if its presentation/content/policy remain usable; otherwise show a version-bound restart/recovery choice. Navigation recovery is outside learning ranking.

**1 — Protected assessment takes its declared blueprint path.** Do not insert tutoring or exploratory learner-model tasks. If no approved compatible task exists, PAUSE_UNAVAILABLE. Assistance and authorised accessibility remain independent. User may exit according to assessment rules; override cannot disable those rules.

**2 — Determine bounded scope.** An explicit eligible learner topic/action chooses scope. Otherwise use the instructor's ordered current unit/obligation; otherwise the approved package order. Deadline facts may select an obligation only through a declared urgency window and deterministic earliest-date tie. No deadline → no invented urgency. No cross-context portfolio planner.

**3 — Generate and filter concrete actions within scope.** Validate content/source/approval scope, task response/evaluator capability, access/modality, support/reveal policy and any truly mandatory access prerequisite. Soft readiness creates a candidate repair/probe, not exclusion. Apply episode repetition/help budgets. Save generator and pool versions; all-excluded → NO_ELIGIBLE_ACTION with dominant exclusion reason and permitted alternatives. Do not say Session complete if required work is unavailable.

**4 — First matching pedagogical branch wins.**

- Explicit help request → the first eligible approved explanation/example/help operation appropriate to the request. No mastery inference from the request.
- Approved direct evidence of a local prerequisite gap, relevant to the selected task → one targeted repair if its budget remains. Unknown readiness may offer a bounded probe or prerequisite material; it does not establish a gap. If no prerequisite evidence contract exists, follow approved package instruction.
- Repeated valid, comparable error pattern → one approved alternative explanation/example/guided practice, if not already delivered in this episode. Item/scorer/mapping invalidity routes to review and another valid task; it never routes to learner remediation.
- UNMEASURED/SPARSE selected claim → one eligible diagnostic probe if the package explicitly prefers probe-first and a probe budget remains; otherwise introduction/approved guided practice. Learner exposure is not required before an optional diagnostic. Lack of logged exposure does not establish ignorance.
- Eligible author-scheduled delayed review → a permitted retrieval/performance task. Label reason 'scheduled review', not quantified forgetting risk.
- Otherwise → the next approved package learning/practice operation not yet completed in this bounded session. Completion here means the job was done, not competence.

**5 — Resolve within-branch ties.** Authored sequence position, then least recently delivered compatible family, then stable action identifier. Recency cannot bypass a construct/validity constraint. Optional effort/time may restrict explicitly fitting actions; missing estimates cannot become zero-effort favourites. If none fits, offer an honest shorter option or pause rather than claim an invented fit.

**6 — Output and bound loops.** One primary action + decisive rule reason + optional eligible alternative/escape. At beta default, one unsolicited help offer per episode and no second automatic repair of the same pattern before an independent probe, scope change or explicit learner request. These budgets are tunable anti-loop hypotheses. Repeated requests for help remain allowed where policy permits. A consumed/dismissed action cannot silently regenerate after a refresh. No unsupported progress claim follows from dismissal.

**7 — Revalidate at delivery, then link outcome.** No old reason can justify newly prohibited content. Record new decision if inputs materially changed. Record support actually delivered before response commitment. Successful completion does not prove comparative benefit of the policy.

This order deliberately gives explicit learner intent precedence in practice, caps remediation and uses curriculum order as the fallback. General may prefer another order, but Draft 2 must write it down with counterexamples. Urgency never overrides integrity. Opaque 'similarly defensible' is replaced by ties under named rules.

## 5. Minimum evidence profile and sufficiency

For each claim version and evidence channel, retain references to eligible evaluation revisions, family/episode grouping, conditions, dates, and the contract result. Derived profile: UNMEASURED, OBSERVED_INSUFFICIENT, CONTRACT_MET_UNDER_CONDITIONS, or REVIEW_REQUIRED. Keep validity/conflict/freshness reasons as independent flags; they are not one ordinal mastery scale. Invalid or pending evaluations contribute no pass/fail evidence. Historical evidence remains inspectable after supersession if authorised, but is not active current-course evidence by default.

Author each claim contract using: the exact performance being supported; task/response/rubric features eliciting it; conditions/support allowed; which task families vary materially; criterion-level coverage; sufficient pattern; disqualifying contradictions; valid time/delay interpretation; known limits and permissible use. A beta rule might require two separately authored equivalent-construct families with all essential rubric criteria met without answer-bearing support. That is a claim-specific trial rule, not a validated universal threshold. Where suitable families/scoring are unavailable, report insufficient evidence and still allow appropriate learning.

**Coached evidence:** useful for supported performance, separate from unaided evidence. 'Unaided' means no known answer-bearing support within the contract's relevant exposure window, not simply hintCount=0. Unknown/offline help cannot be guaranteed absent; preserve the limit rather than claiming forensic certainty.

**Repeated items:** subsequent successes after answer reveal demonstrate practice/response memory. Surface variants sharing a solution path remain correlated. They do not add independent sufficiency units. A task may support multiple claims only through separately scored criterion mappings; one final numerical answer must not be copied as universal success across algebra, units and reasoning.

**Conflict:** distinguish different constructs (no contradiction), comparable mixed results (history with uncertainty), scorer disagreement (evaluation review), and source/mapping invalidity (content quarantine). A newer valid novel performance may justify a current bounded demonstration without erasing an older failure. The hard rule is not to manufacture certainty by arbitrary averaging; the estimator need not obey a universal 'every conflict widens posterior uncertainty' mathematical law.

**Retention/cold start:** no model of retention in beta; record actual delayed demonstrations and author-scheduled review separately. Cold start starts with selected-topic/package instruction or a permitted probe; no global ability prior. Do not treat missing/aborted responses as incorrect. Real-world skill claims remain unsupported until a relevant assessor pathway exists.

## 6. Cross-domain attacks — same engine, different contracts

| Domain/construct | Falsifying fixture | Required disposition |
|---|---|---|
| Law/policy reasoning | Two approved sources conflict; old version answer is defensible under old authority. | Scope response to source/claim version; source review/alternative rubric, not blanket learner weakness. These are fictional contract fixtures, not legal guidance. |
| Engineering/math | Correct final value despite invalid units; valid method with arithmetic error. | Criterion-level evaluation supports different claims separately. Numeric/formula automation only if declared supported; human rubric can evaluate constructed response without masquerading as a calculator engine. |
| Science/forensics | Learner chooses right conclusion for an unjustified reason; procedure allows two parallel steps. | Assess reasoning/evidence quality separately; order rubric allows declared alternatives. No universal total ordering. |
| Memorisation | Twenty correct retries after answer reveal, then failed delayed fresh prompt. | Practice history stays; no twenty independent demonstrations or RETAINED badge. Delayed evidence remains distinct. |
| Constructed response | Two raters disagree on one essential criterion; LLM service unavailable. | Pending/review-required evaluation, human path or compatible different task. A missing scorer is not an incorrect answer. |
| Procedural/physical | Perfect on-screen sequence, failed supervised physical execution. | Distinct claims/channels; no physical competence from screen proxy. Beta may abstain rather than build an external assessment system now. |

Portability means these definitions and evidence limits fit the same contracts. It does not mean every interaction, domain rubric and memory model is implemented on day one. Changing a domain label must not require a branch in the recommendation or scoring logic.

## 7. Beta cuts, product boundaries and hard invariants

For ~20 students and one professor: one bounded course package; context-local personal packages labelled provisional; a small author-reviewed claim set; deterministic response scoring for the needed simple types; constructed responses pending human review where needed; evidence history views; the policy above; simple learner reasons; item/mapping review and coverage lists for the professor. Authoring is a small reviewed workflow, not a universal knowledge modeller.

Design discriminators for single, set, order, match, category and constructed response remain distinct. Beta delivery need only support the course's declared subset; unsupported type returns UNSUPPORTED before presentation. Prefer a narrow vertical slice including set/order distinction and one human-reviewed constructed response, not six half-working evaluators. Accessibility alternatives are part of each supported type's contract. Numeric/formula/hotspot execution, QTI import/export and CASE synchronisation are later adapters, not current commitments.

**Cut now:** all latent KC/KT model fitting; optional BKT/PFA comparator inside production; calibrated forgetting; generated automatic misconception profiles; general graph editor; exhaustive assertion extraction; predictive class alerts; external physical-assessor workflow unless required by the beta course; learned ranking; multi-course optimiser; model microservices. Preserve absence/unsupported pathways rather than building placeholders that pretend capability.

**Product versus stored meaning:** Up Next, Ready to advance, Due for review, Progress, exposed/demonstrated labels and insight cards are projections with reasons, not mutable learner truth fields. Session complete is a control outcome. Reviewed is a user action. Study/Materials/Progress and spatial presentation belong to the shell. Role/context/presentation policy are execution inputs. Instructor preview must not create learner evidence or awards. An implementation must preserve that earlier Q-SOL3 contract without importing its navigation into engine ontology.

**Hard contracts:** version-bound evidence/mappings; explicit correction lineage; integrity/access enforcement; assessment support separated from accessibility; no unauthorised coaching; no mastery from exposure/reward/non-response/override; no sensitive behavioural trait inference; optional telemetry off preserves the core; stale execution cannot use obsolete permissions; no unsupported scoring/type fallback; explanation derives from actual decision path; no cross-context evidence leakage; authorised privacy deletion is not defeated by trace duplication. Immutable history means no silent rewrite while retained, not eternal retention.

**Tunable hypotheses:** sufficiency pattern per claim; channel comparability warrants; priority order; probe/repair budgets; scheduled delay; misconception specificity; freshness windows; learner vocabulary; professor review thresholds. None gains scientific authority by being deterministic or agreed upon by several agents. Protected-assessment invariants and role isolation require concrete enforcement evidence later.

## 8. Reconstruction without surveillance

Retain decision ID, context/role/package versions, candidate-pool/generator revision, candidate IDs/exclusion codes, selected action, decisive ordered rule path, profile reference/as-of time, mapping/evaluator/config versions, current clock/deadline inputs and action execution status. Material stochastic/generated outputs need the actual approved artifact reference/hash, not an assumption that a later service call reproduces them. No new prompt logging solely for replay; a hash alone is not a recoverable artifact.

Learner reason uses a bounded template derived from the winning rule and valid evidence scope, e.g. 'An example for the unit you chose' or 'A fresh practice task after the supported attempt.' It must not claim evidence that was excluded or a causal benefit. The instructor gets authorised references and descriptive denominators; debugging gets access-limited engineering reasons. These projections need not expose another student's data or accommodation details.

Raw responses are stored once in their authorised evidence domain. Decision references must not outlive permitted identifying links merely because trace reconstruction is desirable. After deletion, mark reconstruction PARTIAL/UNAVAILABLE and explain the missing category; do not save hidden raw copies or identity-bearing hashes as a substitute. Historical policy reconstruction uses historical versions, while current estimates use approved current interpretation rules. Those are two different questions.

## 9. Claude attack questions — exact engineering feeder

1. What is the smallest record ownership model implementing package versions, attempts, evaluation revisions and decision records without full event sourcing? Which semantic distinctions can share storage safely?
2. Where is the atomic boundary for response commit, support-exposure record and evaluation enqueue? Demonstrate duplicate submit, callback retry, crash after commit, stale tabs and simultaneous sessions. No duplicate evidence units.
3. Can policy change after recommendation issuance but before content delivery? Identify the authoritative revalidation boundary, invalidation token and safe stale response handling; cached answer-bearing content must not leak.
4. How do two in-flight scorer revisions/regrades update current evaluation once without rewriting the original response? Show cancellation, late callback and reviewer override precedence.
5. Which source/mapping changes invalidate which package entries and evidence profiles? Can historical reconstruction still use its old approved versions without becoming current-course authority?
6. How is episode identity established across resume, tab duplication and re-presentation? What exposure lineage prevents a repeat from appearing unaided? Explicitly bound cross-item/claim leakage detection.
7. How do candidate generation and eligibility prove coverage of the selected package scope? How are missing content, unknown prerequisites, cycles and all-excluded states represented without deadlock?
8. How are learner/course/personal/preview contexts isolated in IDs, queries and derived caches? Instructor preview must produce zero learner evidence/reward.
9. Which artifacts are immutable/versioned versus recomputable versus deletable? Show deletion traversing caches/traces/generated summaries without hidden response copies; report reconstruction degradation honestly.
10. What are the supported response/evaluator capability checks? Show unsupported schema, unscored constructed response, partial-order rubric and unit-level criterion mapping; no automatic wrong fallback.
11. What happens when an explanation/scorer service is unavailable? Approved fixed content and policy continue; dependent scores remain pending. Bound retries and stale model callbacks.
12. Can the same finite input package generate the same eligible candidates, ordered decision and reason under a pinned policy/clock? Identify deliberately nondeterministic artifacts and how actual outputs are retained.

These questions are a feeder to General's authorised Claude gate, not a wake instruction or code assignment from Sol.

## 10. Falsification specifications — not executed product tests

| ID | Fixture | Required observable result |
|---|---|---|
| T01 | Goal topic B, exam A tomorrow, gap A, review B due | Declared scope/order produces one reproducible reason; urgency cannot silently change the goal policy. |
| T02 | All available candidates excluded | NO_ELIGIBLE_ACTION, exclusion reason, permitted escape; no false completion/mastery. |
| T03 | Hard prerequisite unknown; soft A↔B cycle | Unknown not failed; probe/material allowed where authorised; bad edge quarantined; no loop. |
| T04 | One correct recognition item | Only bounded observation; application/retention sufficiency unmet. |
| T05 | Recognition success, application failure | Two channel profiles; no fabricated scalar conflict/mastery. |
| T06 | Comparable varied outcomes and later valid novel success | History preserved; explicitly scoped current claim; no unconditional uncertainty monotonicity rule. |
| T07 | Same answer after hint, new tab, resumed attempt | Episode/exposure follows; not relabelled unaided. |
| T08 | Five template variants mislabelled independent | Reviewer family-dependency check rejects false coverage; practice remains recorded. |
| T09 | Incorrect mapping corrected after ten attempts | Responses unchanged; affected interpretations/profile recomputed; prior decisions retain old mapping. |
| T10 | Source changes one proposition | Named dependents reviewed/quarantined selectively; no global learner regression. |
| T11 | Wrong automatic score → two simultaneous regrades | Evaluation lineage/precedence explicit; one active interpretation; no duplicate evidence. |
| T12 | Practice decision opened after protected-policy change | Revalidate before support delivery; prohibited explanation unavailable; authorised accommodation remains. |
| T13 | Response commit retried after crash | One logical response/evidence unit; pending evaluation truth shown. |
| T14 | Repeated errors after already offered repair | Budget prevents automatic repair loop; disconfirming probe/eligible choice; no nagging. |
| T15 | Ten overrides, non-response, slow input | No mastery/engagement/ability penalty; only permitted user context/history changes. |
| T16 | Teacher preview of same task | No learner evidence, progression or reward; role projection explicit. |
| T17 | Delete response/debug/accommodation records per policy | No hidden trace copies; reconstruction status degraded accurately; optional telemetry off still works. |
| T18 | Candidate generator omits eligible task | Scope/pool review detects omission; recording only emitted candidates does not pass completeness check. |
| T19 | Personal provisional notes vs unapproved course explanation | Authority scopes visible; personal study allowed under its policy; consequential course use blocked. |
| T20 | Six evaluated responses out of roster twenty; one bad item | Denominators and item-quality alternative visible; no universal class weakness or private inference. |
| T21 | Correct numerical result with failed units criterion | Separate criterion mappings; no copied success to every claim. |
| T22 | Two valid partial orders / unfamiliar interaction | Valid alternate accepted; unsupported contract refuses presentation, no MCQ substitution. |
| T23 | AI outage and scorer-version switch | Pending scores and safe available action; historical scorer identity preserved. |
| T24 | Clock advances; deadline corrected; no retention model | Review schedule changes only by declared rules; no fake forgetting probability; fresh deadline used. |
| T25 | Perfect screen sequence, failed physical assessment | No physical competence claim; explicit evidence gap. |
| T26 | Every valid input pinned, catalogue order shuffled | Same declared tie result under stable IDs; reason names actual branch. |
| T27 | Hidden support, UI selection failure or incomplete submission | Unknown/invalid/pending evidence; no learner weakness from software failure. |
| T28 | Repeated fresh probes selected by current policy | Log selection scope; do not claim neutral sampling, efficacy or calibration from policy acceptance alone. |

Draft 1 A–O coverage remains, with amendments to B/K as above. These 28 are design fixtures for later independent verification. They are not PASS counts, a released QA suite or proof that storage/permissions work. Beta preconditions should require every integrity fixture to pass on exact implemented bytes; pause immediately on unauthorised coaching, cross-context evidence leakage or destructive evidence corruption. Other numeric study/experience thresholds belong to a predeclared beta protocol with named review owner.

## 11. Recommended Draft 2 skeleton

1. **Purpose, supported beta scope and explicit non-claims.** Context-local decision support; no mastery oracle, efficacy promise or required universal ontology.
2. **Authority and ownership.** Approved learning package, provisional personal package, source conflicts, reviewer roles, role/preview boundaries.
3. **Operational claims and evidence contracts.** Constructs, conditions, scoring criteria, sufficiency patterns, dependency/family grouping, comparability and validity limits.
4. **Task/presentation/evaluation model.** Supported type contracts, capability checks, assessment purpose, stakes, support/reveal/accessibility, episode lineage, pending/regrade outcomes.
5. **Recorded evidence and derived profiles.** Version-bound records, correction rules, channel-specific evidence, unknown/invalid states; no beta latent learner model.
6. **Action instances and bounded selection.** Concrete operations separated from session control; explicit branching order, ties, budgets, no-action and override semantics.
7. **Issue-to-outcome lifecycle.** Idempotency, resume, stale-policy/content revalidation, support delivery and outcome linkage; Claude supplies engineering alternatives.
8. **Reason and reconstruction contract.** Decision path, pool/generator completeness, version manifest, authorised projections, retention/deletion degradation.
9. **Professor inspection and content correction.** Descriptive counts/coverage/item quality, denominators/access rules; optional action proposals require review.
10. **Beta fixtures, protocol and stop conditions.** Integrity tests, evidence/claim review, learner reason comprehension, instructor usefulness; no causal or population claim.
11. **Deferred adapters/challenger gate.** KCs, learner models, memory models, external authentic-performance assessment, standards interoperability and richer UI only when needed and independently justified.

The skeleton moves engineering lifecycle ahead of broad model ambition and removes shell aesthetics from the normative engine spec. General can reconcile this with Research/Gemini/Claude on the merits of counterexamples, not votes.

**Owner decisions:** none blocks this review or Draft 2 editing. Before a beta specification is released, General/Nathan must name the bounded pilot package/constructs and whether protected assessment is actually in scope. If it is excluded, state that explicitly; keep policy/type contracts but do not claim enforcement already proven. The proposed branch order and budgets can remain labelled trial defaults until protocol review. Privacy/access/retention settings require their authorised beta governance decision, not an invented universal number here.

## 12. Exact source register and research boundary

Consumed required inputs in route order:

| Input | Frozen path / commit | Blob |
|---|---|---|
| Current route | routes/GENERAL_20261001_1935_SOL_ENGINE_V1_DRAFT1_INDEPENDENT_ARCHITECTURE_ATTACK.txt @ 4e9a5a2de2f8e75045712fc991091a1c080557ae | 366faeead2899b357c821878d68dae4afaa40490 |
| Draft 1 | design/STUDYGRID_ENGINE_V1_FIRST_PRINCIPLES_DRAFT_1.txt @ bc1a346cf6c6a95d081804e2d60d980533d16d61 | 6d0560091b587220609740970154e64541f4b7c4 |
| Research terminal | routes/RESEARCH_CF0044_20261001_1917_ENGINE_V1_PRIMITIVES_ADVERSARIAL_REVIEW_DONE.txt @ 93dbc55c00579128a2b96cbb44c8094c5ff9b007 | b4077d8d0331e75158856ef632925910f7903bb6 |
| Sol Q-SOL3 | reports/SOL_20261001_QSOL3_PRODUCT_DESIGN_GATE/REPORT.md @ 4ce6057ac91ad200e5b0032ed71146745faae3c1 | 7f78c823139113f78ed1c6f26f5f851b20b3d6c0 |
| Gemini reconciliation | reports/GENERAL_20261001_1918_GEMINI_CREATIVE_UX_RECONCILIATION.txt @ d09ee92ab06afbe57e3207eebe2ac69a375ddfc4 | 2a52b0208a77d37e5cca18fb5c7fc232260efbc1 |

Current registry46/50, CGPTBASE-R0004-N8V6, Active Corrections and canonical Config were read. STARTED WORKER66 / TX0272 preceded substantive review. Discovery queue at 4e9a5a2 still projects old Q-SOL3 AVAILABLE despite provider-visible prior DONE; this is a coordinator projection mismatch, not authority to repeat the old task. Current owner-activated Draft1 route supersedes the earlier 1914 challenge. No RA-098 resumption or worker wake.

Primary sources checked 2026-10-01, limited to architecture/assessment boundaries:

- [ETS, Evidence-Centered Design for Learning, Hansen 2011, RM-11-02](https://www.ets.org/research/policy_research_reports/publications/report/2011/imbu.html): the abstract separates student/proficiency, evidence and task models from a pedagogical model concerned with fostering learning. This supports keeping measurement and action-selection meanings distinct; it does not validate this proposed policy.
- [ETS, A Brief Introduction to Evidence-Centered Design, Mislevy/Almond/Lukas 2003, RR-03-16](https://www.ets.org/research/policy_research_reports/publications/report/2003/hsgs.html): bibliographic/abstract cross-check of Research's foundational reference. No full-paper claims inferred from the short retrieved abstract.
- [1EdTech QTI specification register](https://www.1edtech.org/standards/qti/index): exchanges assessment content/results and separately lists item/test models and conformance. This supports preserving an interoperability boundary; it does not require QTI conformance or prove teaching effectiveness.

All ontology cuts, sufficiency examples, branch rules, storage suggestions and falsification fixtures here are Sol architecture judgements. No new empirical efficacy, legal, psychometric calibration or current software-functionality claim is made. No external UX research was performed.

**General disposition:** consume the 16 concrete repairs, 15-layer diff, explicit beta policy, 12 Claude questions, 28 falsification fixtures and eleven-part Draft 2 skeleton. Status becomes DONE when exact report/return and lifecycle readbacks are persisted. Sol stops; General owns reconciliation and any later implementation authority.
