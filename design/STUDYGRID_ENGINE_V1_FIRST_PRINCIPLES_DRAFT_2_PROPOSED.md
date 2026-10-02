# StudyGrid Engine v1 — Proposed Draft 2

Prepared by Sol CF-0043 for General CF-0047 · 2026-10-01
Status: PROPOSED DRAFT 2 — design complete; pending General reconciliation, engineering review and owner approval. No implementation, installation or release authority.

This is the proposed engine contract. MUST and MUST NOT describe behaviour a later accepted specification would require; they do not claim existing software does it. Deterministic defaults below are trial policy choices, not validated learning effects. Section keys S01–S18 are stable review anchors. Test keys F01 onward identify falsification specifications, not executed passes.

The engine's value is an inspectable integration and decision policy over real course material and bounded evidence. It does not reinvent public learning science or claim exclusive scientific validity. Its experience remains simple: one permitted next activity, a short honest reason and an appropriate escape.

## S01. Purpose and non-goals

StudyGrid selects and delivers a defensible next learning action in the learner's selected course or personal-study context. It can teach, give an example, support practice, elicit evidence and schedule review. It preserves the difference between what was recorded, how it was scored, what that may support and why an action was selected.

The central question is: which available permitted action is defensible now, for this context, with these evidence limits and rules? The answer may be an approved learning action or a truthful abstention. Sparse competence evidence does not prohibit useful approved teaching.

Beta purpose: find content/mapping/scoring/policy/explanation defects and test the usefulness and inspectability of a small course-local loop. Completion, correctness, recommendation acceptance and usage are separate descriptive measures.

Non-goals: universal mastery, aptitude or motivation inference; calibrated competence percentages; universal forgetting prediction; causal instructional-effect estimates; automatic high-stakes grading; institutional-scale reliability claims; cross-course optimisation; replacing instructors; a full conversational product shell; general ontology or ML platform.

**Reason:** choosing an available action is operationally achievable without pretending to know its unique causal benefit.
**Strongest counterexample:** an easy-question policy wins on immediate correctness while failing novel or delayed performance.
**Smallest repair:** name the selected rule and evidence scope; evaluate delayed/transfer outcomes separately rather than call acceptance a learning benefit.
**Falsification F01:** two policies with different immediate correctness cannot be ranked for learning efficacy without an appropriate outcome protocol.

## S02. Smallest primitive set and logical boundaries

Five primary record families suffice. These are logical contracts, not prescriptions for five tables or services.

| Record family | Contents / ownership |
|---|---|
| LearningPackageVersion | Scoped authority, source references, sparse content units, operational claims/evidence contracts, resources/tasks/rubrics, approved mappings, bounded prerequisite declarations and policy references. Content owner approves definitions. |
| Opportunity / Response records | Exact presentation/episode/selection identity, support-delivery facts, raw committed response or missingness disposition. Runtime records facts about delivery and learner input. |
| EvaluationArtifact | Versioned scoring act/result, component rubric output, scorer provenance, uncertainty/status and correction lineage. Evaluator/reviewer owns interpretation of the response. |
| DecisionRecord / Execution facts | Accepted decision with as-of manifest, eligible candidate IDs/reasons, chosen action, tie path, agency constraint and delivery/outcome links. Policy selection is separate from execution. |
| Authority / Correction / Disposition records | Approvals, mapping challenges, impact classifications, supersession, regrade activation, void/redaction and authorised declarations. Explicit scope and provenance; no duplicate general graph semantics. |

Evidence contributions, learner profiles, misconception/error-pattern hypotheses and instructor views are derived over these records. A reviewed hypothesis influencing a material decision may have a retained annotation/reference, but it is never raw competence evidence.

A source is not an assertion; an official outcome is not an operational claim; a KC is not either. Optional external outcomes and sparse assertion identities may exist inside the package. KCs are a deferred extension for a future model that genuinely needs them. No universal LearningTarget atom, mandatory sentence extraction or schema-free RelationEdge exists in beta.

Use bounded relationship contracts: source support, external-outcome alignment, task-to-claim evidence mapping and claim sequencing/readiness declarations. Version lineage and provenance each have their own metadata; they are not duplicated as generic graph edges.

One deployable application is the beta architecture preference. Logical access/retention boundaries may share storage. Concrete database, transaction and hosting decisions remain engineering-review work; no new service follows merely from a named concept.

**Reason:** semantic separation prevents false inference; compact ownership prevents contradictory durable copies.
**Strongest counterexample:** an “assesses” edge and evidence mapping disagree, while two current learner-state stores each appear authoritative.
**Smallest repair:** one authoritative definition per relation/use; derived views reference exact versions.
**Falsification F02:** changing a mapping updates its single authority and invalidates all affected derived uses, without editing a second graph edge or raw response.

## S03. Durable, derived and transient state

| Class | Required state | Rules |
|---|---|---|
| DURABLE, versioned | Used package/source/content/claim/task/rubric/mapping/policy definitions; approvals and impact decisions; bounded goals/agency declarations when actually used | Stable object identity plus immutable version identity/hash and authority scope. Retention/access are explicit. |
| DURABLE, logically append-only | Presentation/response/support events; evaluation revisions; accepted decisions; execution dispositions; corrections and void records | No silent rewrite while retained. Idempotent operations. Deletion/redaction can supersede retention; logical immutability never means physically undeletable. |
| DERIVED | Evidence interpretation, profiles, uncertainty/readiness/error patterns, exposure/completion views, candidate generation, instructor aggregates, reason projections | Recomputable under explicit input versions/cursors. Optional caches are keyed by full dependency identity, not current learner truth. |
| TRANSIENT | Uncommitted response edits, pre-acceptance candidate buffers, rendering state, open drawer/tab/focus, calculation work | Not evidence until committed. Session resume location may have a purpose-limited operational checkpoint; it does not become competence evidence. |

A profile's dependency key includes learner/context/claim version, response cursor, support cursor, evaluation cursor/effective-score manifest, mapping/authority epoch, derivation config and as-of instant. A late score or regrade therefore changes the key even with no new response. Reusable caches may have a manifest reference instead of copying full history.

All material identity and cache keys are context-qualified: course, personal/provisional, instructor preview and synthetic QA evidence cannot cross by matching a claim name. Used definitions have stable object IDs plus immutable version IDs; presentations have unique opportunity IDs; responses additionally occupy a semantic response slot; evaluations have response/scoring-purpose lineage IDs; decisions have learner/context stream IDs and accepted sequence numbers. Authority and correction records name target versions and reviewer scope. Exact physical identifier encoding remains engineering work.

Policy-only changes stale decisions relying on that policy, not automatically all learner profiles. Semantic source/mapping/scorer changes stale affected interpretations/profiles. Cosmetic version changes preserve comparability only through authorised equivalence metadata. Currentness is dependency-specific.

**Reason:** current derivation and historical reconstruction answer different questions.
**Strongest counterexample:** an old profile keyed only by response count survives a late score, then drives an incorrect current recommendation.
**Smallest repair:** include scoring/support/authority dependencies and reject stale caches at decision acceptance.
**Falsification F03:** a late effective evaluation changes the active profile and new decision, while the committed response and earlier decision remain unchanged.

## S04. Content, source and authority model

A package declares context/owner, language/domain labels, version, allowed uses and authority scope: COURSE_APPROVED or PERSONAL_PROVISIONAL. Approval concerns an exact artifact/version and use; it is not proof of universal truth.

Source metadata: stable identity/version, retrievable artifact reference/hash, span locator when used, scope/effective conditions, provenance, rights/access where applicable and supersession/impact state. Sparse content-unit identities are created only when an authority-bearing proposition/procedure needs independent review or dependency tracking. A teaching resource can reference source spans directly.

Definition authority has independent review and validity dimensions. Review: DRAFT / APPROVED_FOR_SCOPE. Eligibility: USABLE / UNDER_REVIEW / INVALID / SUPERSEDED. “Approved-valid” means currently usable within reviewed scope, not scientifically proven. A challenge can quarantine an approved mapping/resource immediately. Unknown or conflicting authority never silently chooses the newest filename.

Course teaching/actions require approval for that scope. Personal provisional material may support explicitly provisional study under its own package policy; it must not establish consequential course readiness/grades. AI proposes material/mappings/explanations; its outputs acquire no course authority without the review path. Generated content actually delivered must be retained as an authorised artifact/version, not reconstructed by calling a later model.

A teaching-only resource needs approved provenance and claim/topic relevance, not an artificial task-to-claim assessment mapping. An evidence-producing task does require an approved usable mapping for any claim inference.

**Reason:** source grounding and scope are necessary, but approval can still be wrong.
**Strongest counterexample:** legitimate personal notes are excluded by a blanket canonical-content rule, while an approved incorrect course mapping continues increasing confidence.
**Smallest repair:** scope provisional study separately and keep challenge/quarantine independent of approval.
**Falsification F04:** provisional personal instruction is available under its policy; challenged course evidence cannot support a strong claim during review.

## S05. Claim and definition-time evidence contract

Every operational learning claim defines: capability/construct, relevant conditions and modality, temporal scope, generalisation/transfer boundary, intended use, success criteria and claim version. “Can apply X” requires an explicit description of the instances and conditions encompassed.

The author-time evidence contract includes:

- intended interpretation and permitted use;
- admissible task/response/rubric features and channels;
- warrant: why criterion performance supports this claim;
- rebuttals: guessing, prior answer exposure, template dependence, support, language/modality load, ambiguity, scorer uncertainty and source/mapping uncertainty;
- condition requirements, including permissible supports and minimum evidence freshness/delay where relevant;
- task-family/dependence grouping and how variations differ substantively;
- component-attributable versus JOINT evidence semantics;
- a testable sufficiency predicate and disqualifying/review conditions;
- transfer/generalisation requirements distinct from simple family count;
- accessibility/validity review scope and limits.

Definition-time mappings reference task version, claim version, rubric components, evidence role, approved rationale, mapping version/eligibility and retrospective policy. They contain no learner response, personal attempt or inference-run output. Estimator version is an interpretation/run dependency, not a field requiring every evidence contract to change.

Positive or negative per-claim evidence must be attributable to a rubric component that actually isolates it. A whole-task outcome can remain joint/diagnostic evidence; failure of a conjunctive task does not diagnose every constituent claim. JOINT evidence is stored/represented once with its scope, not copied as independent confirmations.

If no approved sufficient pattern exists, the profile may show bounded observations and unmet evidence requirements; it MUST abstain from a strong claim. Learning may continue. Author approval is a review warrant, not calibration.

**Illustrative trial contract:** “solve supplied single-variable linear equations, including a check, without answer-bearing assistance.” Two reviewed families with materially different required transformations, all essential method/check criteria met, one deliberately novel instance, no unresolved scorer/source dispute. This supports that bounded practice claim only. It does not establish broad algebra ability or retention. The pattern is an authorable test hypothesis, not a universal threshold.

**Reason:** field completeness alone cannot establish validity or sufficient evidence.
**Strongest counterexample:** five cosmetically varied questions after the same example satisfy an accidental count threshold for transfer.
**Smallest repair:** explicit dependence, rubric, novelty and conditions predicates; no general numeric mastery conversion.
**Falsification F05:** repeated/template-dependent supported successes fail a contract requiring novel unaided performance.

## S06. Opportunity, attempts, responses and scoring

Before evidence is interpreted, preserve the opportunity that produced it: presentation ID, learner/context/role, episode ID, concrete action/task/version, decision or non-adaptive author-sequence reference, selection policy/scope, support available/delivered, reveal rules and relevant authorised capability codes. Instructor preview is a separate role/context and produces no learner evidence or reward.

An episode groups related delivery and response opportunities, including resume and duplicate tabs. A retry creates a new response opportunity but retains prior item/family answer exposure and support lineage. A fresh attempt ID does not erase known prior help. Material unknown exposure remains unknown.

Committed response records preserve response IDs/artifact and schema, task/presentation version, operation identity, trusted receipt sequence/time, optional client occurrence time with clock provenance, confidence if voluntarily supplied before feedback, and operational disposition. Do not bake inferred objective/claim mastery into the raw response.

Each presentation/explicit attempt owns one semantic response slot. At most one final committed response occupies it, even when double clicks or duplicate tabs generate different transport operation keys. Conflicting commits return the existing response or an explicit conflict; they cannot overwrite it. An authorised reattempt creates a new slot with retained exposure lineage. Persist a bounded accepted-result receipt for supported retry windows; expired transport receipts do not remove semantic uniqueness. If scoring scheduling fails after response commit, recover pending evaluation work without losing the response or fabricating failure.

Missingness is distinct: NOT_OFFERED, OFFERED_SKIPPED, ABORTED, NOT_REACHED, TECHNICAL_FAILURE, or RESPONSE_COMMITTED. NOT_OFFERED can be derived from a candidate-pool/selection manifest rather than generating an event for every unseen item. Timeout is an administration outcome. A declared grading rule may assign credit for non-response; that grade is separate from a competence interpretation. Unsupported or broken input cannot become an ordinary wrong answer.

Support is recorded on actual delivery/answer reveal, not merely request or button visibility. A delivery uncertainty cannot assert “no support.” The engine does not claim it can detect unseen offline help. Pre/post support evidence stays distinguishable.

An EvaluationArtifact references response, rubric/scorer/model/rater/config and its retained output, component results, uncertainty/validation state, received sequence, supersession/adjudication lineage and status: PENDING / EFFECTIVE / DISPUTED / SUPERSEDED / VOID. Deterministic scoring is still a versioned scoring act. Human or AI scoring is interpretation, not learner fact. Late output never mutates the response.

Only the authorised active evaluation lineage contributes; concurrent evaluators may disagree. Arrival order cannot silently override reviewer authority. A reviewer/adjudication activation selects the effective revision using an expected-lineage token; inconsistent branches become DISPUTED until resolved. Idempotent response/evaluation writes return the accepted record on identical retry; the same key with different payload is a conflict, not another attempt.

Lineage is scoped to response and scoring purpose. Different grade/evidence uses may have distinct reviewed contracts; multiple scoring revisions for one use are never multiple learner performances. Malformed/out-of-contract output is VOID or pending review, never default zero/incorrect. Duplicate scorer callbacks cannot create another revision. Unconfirmed transport commitment remains operationally PENDING/UNKNOWN until idempotency/status lookup resolves it; no response absence inference is made during uncertainty.

Constructed responses default to pending human rubric review in beta where a reliable bounded evaluator is unavailable. Experimental AI scores are annotations pending review; no strong learner claim or consequential grade from unvalidated output. Validated-for-bounded-use scorers require relevant validation, disagreement handling, monitoring and version-change review. Model agreement with synthetic labels is not validation.

Trusted receipt ordering is authoritative for ingestion. Client timestamps cannot prove delayed recall. Delay validity needs the actual reviewed occurrence/protocol interval; if offline timing is uncertain, abstain from a delayed-performance claim.

**Reason:** administration, learner artifact and scoring have different owners and times.
**Strongest counterexample:** double submit plus a late AI score creates two successes, then a reviewer correction overwrites both history and the old recommendation.
**Smallest repair:** unique operation/response identity, append-only evaluations and one authorised effective lineage with full input cutoff.
**Falsification F06:** five identical submit retries yield one response; late/regraded scores change only the active interpretation; old response and evaluations survive while retained.
The fixture also uses two different transport keys for the same semantic slot, conflicting tab payloads, failed scorer scheduling and malformed/duplicated callbacks: one response, recoverable pending work and no fabricated failure are required.

## S07. Derived evidence profiles, uncertainty and abstention

The beta baseline is a contract-evaluated evidence profile, not a latent mastery probability. It summarises eligible observations by claim version/channel/conditions/dependence group and references the effective evaluations/mappings. Store compact counts, criterion coverage and last relevant valid occurrence only where justified; history is referenced, not repeatedly copied.

Profile result: UNMEASURED / OBSERVED_INSUFFICIENT / CONTRACT_MET_UNDER_CONDITIONS / REVIEW_REQUIRED. These are evidence dispositions, not a universal ordinal scale of learner competence.

Independent reason flags distinguish: SPARSE; MEASUREMENT_OR_SCORER_UNCERTAIN; INVALID_EVIDENCE; SOURCE_OR_MAPPING_UNCERTAIN; NONCOMPARABLE_CHANNELS; COMPARABLE_MIXED_RESULTS; DEPENDENT_REPEATS; SUPPORT_CONDITION_UNKNOWN; TEMPORAL_CONTEXT_UNKNOWN; STALE; CONSTRUCT_OR_MODEL_UNSUPPORTED. Coverage/opportunity and scorer uncertainty are separate from sparse learner evidence.

PENDING_EVALUATION and TRANSPORT_UNCONFIRMED preserve operational uncertainty separately from those measurement flags. They cannot become an ordinary incorrect answer or a learner attribute.

The profile names its claim/use/scope, input window/manifests, derivation config, as-of instant, sufficiency clauses met/unmet and freshness conditions. No raw observation has an intrinsic mastery weight. No policy output, misconception label, reward, confidence self-report, override or exposure is recycled as proof of competence. Optional confidence remains a self-report; beta does not weight it into strong claims.

Conflict rules: invalid evidence is excluded/quarantined; non-comparable constructs/channels remain separate; comparable mixed results preserve history and the approved contract's review rule; scorer disagreement routes to adjudication. Recognition success/application failure need not contradict one another. A later valid demonstration can support a current bounded claim without erasing prior error. No universal requirement forces numerical uncertainty to rise after every mixed result.

INFERENCE_ABSTAIN refuses an unsupported claim. POLICY_ABSTAIN refuses a recommendation for absent/invalid context or no eligible defensible action. They are different: an unmeasured learner may receive approved instruction. Neither is permission to invent a stronger UI label.

**Reason:** uncertainty comes from several different failures and needs different responses.
**Strongest counterexample:** invalid-item misses generate remediation while ten repeats cancel an application failure into “moderate mastery.”
**Smallest repair:** separate validity, comparability and sufficiency; branch on their actual reasons.
**Falsification F07:** a quarantined scorer/mapping contributes no success/failure; channel divergence stays separate; a safe approved teaching action can remain available.

## S08. Exposed, demonstrated, learned, retention and transfer

EXPOSED denotes recorded instructional delivery/history under a defined presentation contract. A page open establishes only that the page was opened; it does not prove attention or understanding. Reviewed/completed are explicit work-history events, never competence.

DEMONSTRATED denotes a contract-met bounded performance: claim X, under conditions Y, at time/window T, on evidence E, with identified limits. A short label must have access to those limits and MUST NOT imply a broader claim.

LEARNED and MASTERED are not default beta states. No categorical RETAINED flag exists. Beta records actual delayed demonstrations under justified timing/conditions and author-scheduled review eligibility. “Due for review” describes a schedule rule, not an estimated forgetting probability.

TRANSFER is its own generalisation requirement/channel. Family diversity is necessary only where the approved contract requires it; it is not sufficient proof of transfer. Screen sequence competence is not physical execution. If an authentic assessment pathway is absent, physical claims abstain. A later external pathway needs protocol/rater/rubric/conditions and disagreement review, not an unconditional instructor-truth import.

**Reason:** current supported performance, delayed evidence and novel transfer answer different questions.
**Strongest counterexample:** one seven-day recall success creates a permanent retained badge and screen sequence results create a physical-competence claim.
**Smallest repair:** bounded time/condition claims, separate transfer contract and explicit unsupported-state pathway.
**Falsification F08:** advancing time cannot preserve an unqualified retention label; screen-only evidence cannot authorise physical execution competence.

## S09. Action taxonomy and teaching loop

| Dimension | Proposed values / responsibility |
|---|---|
| Concrete learning operation | INSTRUCTION/EXPLANATION; WORKED_EXAMPLE; GUIDED_PRACTICE; RETRIEVAL_PRACTICE; ASSESSMENT_PROBE. Each names an available resource/task and delivery contract. |
| Purpose | Learning/practice, diagnostic/formative or summative assessment. Same task definition can serve different purposes with different presentations. |
| Intent / reason | Introduction, repair, review, readiness check, coverage or learner request. “Review/remediate” cannot substitute for a concrete deliverable. |
| Support/reveal | Independently authorised capabilities and feedback timing; scoring and accessibility rules separate. |
| Session control | Start/resume, continue, switch, pause, finish/exit. ADVANCE/NEXT/COMPLETE are controls, not ranked pedagogical treatments. |

The smallest coherent learning loop is approved instruction/example when selected → explicit practice/probe opportunity → response → optional pre-feedback confidence → effective/pending evaluation → policy-permitted feedback → eligible follow-on. It may begin with a diagnostic if explicitly allowed. It does not have to teach before every probe or test after every resource.

Supported interaction discriminators remain single, unordered set, sequence/partial-order, match, category and constructed response; numeric/formula/diagram are explicit extensions. Only the beta's declared supported subset is delivered. Unsupported types refuse before presentation; no silent MCQ or “wrong” fallback. Ordering has equivalent click/tap and keyboard move/position operations; drag is optional. The response/scoring contract, not domain label, determines meaning.

Session finish reports actual work and pending evaluations. Completed work does not imply satisfied competence contracts or completed required assessment. A resource or question becomes eligible through capability/authority validation, not because a desired abstract action label exists.

**Reason:** the engine must deliver learning as well as measurement without conflating either with navigation.
**Strongest counterexample:** policy ranks ADVANCE against EXPLAIN and the application cannot tell what resource to deliver.
**Smallest repair:** rank concrete permitted actions; session control follows execution/work state.
**Falsification F09:** the same task can be practice or diagnostic under distinct policies; Continue cannot itself update competence or leak an answer.

## S10. Protected assessment and authorised accessibility

Assessment purpose, stakes/consequence, assistance capabilities, feedback/reveal timing, scoring and accessibility authorisations are independent versioned dimensions. “Graded” does not universally mean no feedback; the exact protected administration contract controls.

For each task/capability resolve course default plus explicit authorised task/construct-specific accommodation exception, then enforce role/access/integrity constraints. An exception requires authority and scope; a generic “accessibility” flag is no coaching permission. Store minimum capability/authorisation reference, not a diagnosis. If an authorised capability changes the assessed construct, preserve that validity/comparability disposition without inferring a deficit.

Unknown required policy returns BLOCKED_POLICY. Prohibited coaching/reveal is excluded before delivery, including preambles, source excerpts, worked answers, chat help and correctness-correlated rewards. UI suppression alone is insufficient. Revalidate at request and delivery; an old practice recommendation cannot deliver prohibited content after a protection change. Pending protected assessments follow their approved blueprint/session path, with no inserted adaptive tutoring/probing outside that contract.

Protection cannot retroactively remove already delivered information. If policy changes after exposure, record contamination/admin disposition and require an authorised new opportunity or assessment review. Do not relabel the existing attempt unaided.

A permitted override can choose eligible activity or exit under the assessment contract; it cannot grant access or bypass assistance restrictions. Backend/service enforcement remains a later implementation acceptance requirement, not a claim of tested capability.

**Reason:** assessment integrity and equitable access both require explicit capability semantics.
**Strongest counterexample:** read-aloud is useful access support for one construct but reveals the tested skill in another; a stale hint remains cached after protected mode starts.
**Smallest repair:** authorised task-scoped exception resolution, construct-validity disposition and delivery revalidation.
**Falsification F10:** authorised access works without a diagnosis; tutoring is denied through every route; a changed policy blocks stale explanation delivery.

## S11. Context, cold start, learner declarations and overrides

Inputs have distinct owners: package/course obligations and deadlines; access/assessment policy; user-selected context/topic/goal; optional declared effort constraint; operational history; evidence-derived readiness. A mutable Context god object is unnecessary. Each material input has source/version/as-of state; missing is unknown.

Cold start has no global ability prior. Start from the selected scope's approved instruction/guided activity or a permitted bounded probe-first path. Lack of observed exposure does not imply lack of knowledge. If scope cannot be recovered from selected context/package defaults, output NEED_MORE_CONTEXT with a simple selection action, not a fabricated pedagogical recommendation.

“I already studied this elsewhere” is a purpose-limited learner declaration and recommendation constraint. It may reduce repeated introduction or offer an optional check; it does not satisfy demonstration. Reviewed assessor evidence is a separate pathway. A declared time budget filters activities only if reviewed effort estimates actually fit; absent estimates do not mean zero effort. Time is optional context, not the study engine's centre.

Beta override scope is the current session: dismissing an unsolicited recommendation/help offer suppresses its action/pattern in that session unless the learner requests it, explicitly changes the topic/goal, or a new administration contract requires a different mandatory action. It changes recommendation history/context, not the evidence profile. A fresh session can reconsider but shows the relevant reason; never calls the learner disengaged. Protected obligations retain their own rules. If an override exhausts permitted actions, explain POLICY_ABSTAIN rather than nag.

**Reason:** agency must change policy behaviour without masquerading as knowledge.
**Strongest counterexample:** ten overrides are recorded but the same recommendation returns after every click, or an offline-study statement immediately raises mastery.
**Smallest repair:** explicit session-bound suppression/declaration semantics and zero evidence-profile change.
**Falsification F11:** override changes eligible recommendation history but no competence field; offline self-report offers another path without a demonstration label.

## S12. Explicit deterministic beta next-action policy

Policy version D2-BETA-P0 is a proposed trial baseline. No weighted sum, expected-learning-value score, inferred motivation or estimated forgetting probability enters selection.

Rule classes: HARD = authority/access/assessment/evidence-integrity contract; COURSE = approved package/administration choice; HEURISTIC = product/learning-design trial priority. A generally plausible teaching mechanism does not validate this exact branch order.

### Inputs and scope

Request identity and kind (CONTINUE / SELECT_TOPIC / REQUEST_HELP / SELECT_ACTION), learner/context/role/session, expected decision sequence, frozen package/authority/policy versions, trusted evaluation instant, evidence dependency manifest, available capability set, current goal/declaration/override constraints, bounded recommendation history and assessment administration state. Unknowns remain explicit.

Default trial constants: urgency window 48 hours when a real deadline exists; maximum generated pool 100 concrete action IDs within selected scope; one automatic diagnostic per claim and two per session; one unsolicited help/repair offer per claim/error-pattern per session. These defaults are HEURISTIC safety/usability choices, require beta evaluation and can change only through a versioned config. They are not universal learning thresholds. A per-claim error trigger/sufficiency contract is authored; no trigger means no automatic misconception diagnosis.

### Ordered decision stages

| Stage | Deterministic operation / result |
|---|---|
| P0 Validate | Resolve input identity, required policy, supported role and package scope. Invalid configuration → BLOCKED_CONFIGURATION/BLOCKED_POLICY. Stale affected dependencies → refresh/recompute or POLICY_ABSTAIN with STALE_INPUT; never mix old/new versions. |
| P1 Current presentation | A CONTINUE request on a valid unfinished presentation resumes that exact authorised stage through session control. It does not rank a new teaching treatment. Invalid/revised presentation → recovery/version-bound restart choice, preserving old response. |
| P2 Protected administration | A protected task/session uses its approved blueprint order and capability/reveal rules. Select the next authorised blueprint task; no added coaching/probe. Missing/incompatible required task → PAUSE_UNAVAILABLE. Blueprint finished → administration-defined finish/pending-review outcome. |
| P3 Agency scope | Explicit SELECT_ACTION fixes the requested action and scope, with honouring deferred until full P5/P6 eligibility and P9/P10 checks pass; explicit topic/goal selects its approved scope. REQUEST_HELP attempts the requested permitted capability in the selected scope. An unavailable requested action/help returns NO_ELIGIBLE_REQUESTED_ACTION with eligible alternatives; it does not pretend another task fulfils the request. |
| P4 Default scope | Without explicit topic/action, use the approved current unit/obligation. If package permits urgency selection, choose an obligation with a verified deadline inside 48 hours, earliest instant first, then authored order/stable obligation ID. Otherwise use package order. No relevant deadline → no urgency factor. No inferable approved scope → NEED_MORE_CONTEXT. |
| P5 Complete bounded generation | Generate every concrete learning action in declared selected scope plus approved relevant prerequisite/help options; tag resource/task and purpose/support versions. Count >100 → POLICY_ABSTAIN/SCOPE_TOO_LARGE, requiring a smaller approved scope. Never silently truncate to an attractive shortlist. Preserve generator/scope/catalogue manifest and complete generated IDs. |
| P6 Hard eligibility | Apply usable authority for scope, access/capability, valid resource/response/evaluator support, policy/reveal, agency suppression and actual mandatory availability rules. For evidence claims require usable mapping/scoring conditions; teaching-only actions require approved relevance/provenance. Quarantined evidence cannot drive strong-claim/readiness branches. Unknown prerequisite is not failed. Soft/logical learning preferences do not become access locks without explicit policy authority. |
| P7 Pedagogical branch | Among eligible actions, first applicable branch B0–B5 below wins. No candidate in a branch → proceed to the next branch unless the explicit request or mandatory assessment contract requires abstention. |
| P8 Within-branch ties | Order by approved authored action position (missing after present), then least recently delivered compatible dependence group (unseen first), then stable action ID. “Recent” uses trusted delivery sequence/time, not a possibly wrong client clock. Variation is a tie heuristic, not proof of greater learning benefit. |
| P9 Accept | Recheck dependency/authority/sequence tokens and idempotency, persist selected/no-action decision and reason manifest. A changed dependency forces refresh or explicit abstention; no hybrid acceptance. |
| P10 Deliver | Revalidate access, support/reveal, usable content and role immediately before delivery. Record actual delivery/support; link response/evaluation/outcome. This stage is separate from the pure decision calculation. |

The optional effort constraint is applied only to actions with reviewed comparable effort estimates: declared non-fitting actions are excluded; unknown effort returns an explicit unknown-fit choice/alternative rather than being ranked as zero. Lack of effort data must not favour another activity silently.

### First matching pedagogical branch

| Branch / class | Predicate and chosen action |
|---|---|
| B0 Requested help · COURSE/HEURISTIC | REQUEST_HELP under permitted policy → first compatible approved explanation/example/guided action matching that request. Explicit request may exceed unsolicited-help budget; no competence inference. |
| B1 Relevant prerequisite repair · HEURISTIC | Approved component-specific evidence meets the claim's error/gap trigger for a prerequisite relevant to the selected task, and repair budget remains → approved repair resource/practice. Administrative sequence compliance is separate. Unknown gap is not a reason to repair; a permitted prerequisite probe may enter B3. |
| B2 Supported error-pattern repair · HEURISTIC | Repeated valid comparable criterion-specific errors meet the authored trigger, item/scorer/mapping validity is usable, and repair not already offered/used this session → approved alternative explanation/example/guided practice. No automatic learner-misconception probability. |
| B3 Bounded cold-start/coverage · COURSE/HEURISTIC | Claim UNMEASURED/OBSERVED_INSUFFICIENT and approved probe-first is permitted with budget → compatible diagnostic. Otherwise → approved introduction/guided-practice action. Optional diagnostic can precede introduction. Review-required invalidity does not call for another invalid probe; independently approved teaching may still qualify. |
| B4 Scheduled review · COURSE/HEURISTIC | Author-scheduled review is due for the supported construct under valid timing and episode history → compatible retrieval/performance task. Reason says scheduled review, not calibrated retention risk. |
| B5 Package continuation · COURSE | Next eligible not-yet-completed learning/practice operation in the approved bounded session/package order. Work completion cannot unlock a competence-dependent gate unless its evidence contract is independently met. |

An already achieved bounded claim may select a permitted novel/delayed task or next package activity; it does not force endless easier confirmation. If the only actions are suppressed or unavailable, abstain and offer a permitted scope change/exit. A learner-requested repeat remains permitted practice where authorised, but cannot add independent transfer evidence.

Default error trigger, only if explicitly adopted into a claim's reviewed contract: two comparable criterion-specific errors from materially distinct dependence groups, with no unresolved validity/scoring issue. This activates an offer, not a scientific diagnosis. Without a suitable alternate resource the engine cannot invent one at delivery.

Prerequisite declarations are validated for cycles/dangling endpoints before their use. Soft/empirical cycles quarantine those relations and cannot block otherwise eligible package actions. A contradictory mandatory availability cycle returns BLOCKED_CONFIGURATION for the affected administration and routes author review; it does not mark learner failure or erase direct downstream evidence. A relevant prerequisite repair is a recommendation with a permitted continue/alternative, unless a separately authorised mandatory policy actually requires it.

### Outcomes and overrides

Normal selection returns one primary concrete action, a rule-bound reason and at most two permitted alternatives. Other outcomes:

- NEED_MORE_CONTEXT: selected context/scope cannot be resolved; request the minimum selection.
- BLOCKED_CONFIGURATION / BLOCKED_POLICY: missing required authorisation/definition.
- POLICY_ABSTAIN with SOURCE_REVIEW, STALE_INPUT, UNSUPPORTED or SCOPE_TOO_LARGE: no defensible policy result under the available contract.
- NO_ELIGIBLE_ACTION: scope exists, all generated actions excluded; name dominant exclusion and permitted escape.
- NO_ELIGIBLE_REQUESTED_ACTION: exact user request cannot be fulfilled; distinguish alternatives.
- SESSION_WORK_COMPLETE: declared session work done; list pending scores/unsatisfied requirements separately.
- PAUSE_UNAVAILABLE: mandatory administration cannot proceed safely.

An all-excluded set is not completion. Inference insufficiency alone is not no-action. Dominant exclusion uses stable precedence: integrity/policy → authority validity → access/capability → mandatory sequence → stale/unsupported measurement → agency/fit. The record retains all exclusion codes; the visible reason is the highest applicable safe category.

Session-bound override alters scope/suppression/history as S11 specifies. It does not remove hard rules. Concurrent requests use the same accepted history sequence; no two stale requests may both advance it. Identical retries return the accepted decision. A distinct stale request refreshes or is rejected; it is not silently substituted with another topic's action.

**Reason:** an explicit order makes choices inspectable without inventing commensurable utility.
**Strongest counterexample:** urgency, uncertainty and remediation simultaneously dominate, causing incompatible implementations or perpetual probing.
**Smallest repair:** separate scope selection from eligibility and branch priority, bound probes/repairs, specify ties and abstention.
**Falsification F12:** goal B, deadline A, valid gap B and due review B yield the declared scope/branch and stable tie. Changing one trial rule config may change selection but cannot change competence evidence.
**Falsification F13:** all excluded → honest no-action; unknown prerequisite → no inferred failure; over-limit catalogue → no silent candidate loss.
**Falsification F14:** a declined repair stays suppressed in-session; a requested permitted repeat remains practice; no loop consumes the learner as a calibration instrument.

## S13. Decision record, reconstruction and execution lifecycle

The calculation is pure over a frozen input manifest. Acceptance and delivery create later durable facts. A decision contains:

- identity/request payload identity, learner/context/role/session and monotonic accepted sequence;
- package/authority snapshot, source/claim/task/resource/mapping/rubric/effective-score versions actually used;
- response/support/evaluation cutoffs and derivation config/as-of instant;
- only material bounded learner-declared context and policy references;
- generator revision, exact declared scope/pool manifest, generated candidate IDs, eligibility/exclusion codes, evaluated branch/order and tie rule;
- selected concrete action/version or abstention outcome, reason codes, relevant alternatives and uncertainty limits;
- bounded actual feature values or authorised recoverable snapshot reference; a digest verifies integrity but cannot reconstruct missing values;
- decision invalidation/degraded flags and execution/outcome links.

No full raw response or sensitive accommodation declaration is copied into every decision. Actual approved generated/scored artifacts have retained references/hashes where authorised. Generating again from the same prompt is not historical reconstruction. Runtime stochasticity is absent in beta; later randomisation would require actual policy/assignment probability/seed semantics under an explicit experiment protocol.

Complete candidate generation over the bounded scope is auditable. A shortlist can be derived after named transparent pruning, but omitted candidates remain represented by IDs/reasons or recoverable scope manifest. Saving only emitted favourites cannot prove completeness. Scope overflow abstains instead of selecting from an undisclosed partial set.

Reconstruction states:

| State | Meaning |
|---|---|
| FULL | Retained authorised inputs/versions and required outputs suffice to reconstruct the then-accepted candidate eligibility/order/selection. Pure beta calculation must reproduce selection and reason codes. |
| PARTIAL | Some required inputs were deleted/redacted or an authorised dependency is unavailable; the retained decision/outcome is inspectable within stated limits. Missing categories named. |
| UNAVAILABLE | Insufficient retained authorised inputs even for the declared reconstruction job; do not claim replay. |

Historical reconstruction uses then-effective versions. Current re-evaluation uses current authority/mapping/evaluations and may differ. Historical errors remain explainable, not approved for present use.

Execution states: ISSUED → ACCEPTED_FOR_DELIVERY → DELIVERED → RESPONSE_COMMITTED or SKIPPED/ABORTED/TECHNICAL_FAILURE → EVALUATED/PENDING_REVIEW → FINISHED. Invalidated/expired decisions cannot advance to delivery; abort/recompute is explicit. A display/navigation retry is not a new response or reward.

Immediately before acceptance, compare the manifest's authority/derivation/session/decision-sequence tokens with current versions. Immediately before delivery compare content and access/assessment tokens again. A relevant authority change creates a freshness barrier before affected cached derivations can be reused; recomputation may be asynchronous but consumption cannot cross that barrier. No global epoch forces unrelated profile recomputation. Decision history records what was accepted before a change; execution cannot use obsolete permission afterwards.

Proposed beta freshness default: no soft-policy TTL exemption. Any material change in the used goal/deadline, effective score/mapping, support, branch eligibility, policy/generator or accepted session sequence before delivery expires the undelivered decision and recomputes or abstains. Nonmaterial display changes do not. Eligibility permission and a current reason must both remain valid; a permitted activity cannot be presented with an obsolete “exam tomorrow” rationale. Offline creation/delivery is outside baseline beta; delayed online retries still preserve historical presentation, semantic uniqueness and clock limits.

Response commit binds to the actual presentation and support/reveal facts, even if newer policy now exists. A stale or contaminated administration remains historical and gets an explicit disposition; it is not silently graded under a new task/rubric or relabelled unaided.

Logical operation identities cover response commits, score writes, decision requests and delivery activation. Exact retries resolve existing records; mismatched payload under a used identity is a conflict. Optimistic sequence/effective-lineage control prevents two tabs creating accepted “next” from the same stale state. Concrete atomic boundaries/crash recovery are engineering review requirements; this proposal does not claim the platform can already enforce them.

**Reason:** recording versions after the event cannot prevent stale-authority delivery or reproduce missing input values.
**Strongest counterexample:** practice hint issued before policy protection is opened afterwards; regraded feature cache then makes the old choice unreplayable.
**Smallest repair:** frozen input manifest, explicit acceptance/delivery barriers and privacy-bounded retained reconstruction inputs.
**Falsification F15:** policy/content/scorer changes during calculation reject hybrid acceptance; two stale tab requests accept at most one sequence advancement.
**Falsification F16:** old pure decision reconstructs under historical retained inputs; current re-evaluation differs legitimately; deletion changes reconstruction status without hidden copies.

## S14. Source revision, remapping, rescoring, corrections and deletion

Revision operations have author, scope, effective instant, reason, reviewed impact and disposition. No writer silently overwrites a retained raw attempt or retroactively approves a new source.

| Change | Required semantics |
|---|---|
| Source cosmetic change | Authorised NONSEMANTIC_EQUIVALENT impact record identifies unchanged assessed meaning; retain usable mappings/evidence through explicit equivalence lineage. Version number alone does not invalidate everything. |
| Source semantic change | Named affected content/tasks/claim contracts/mappings become under-review/unusable before current consumption. Historical evidence remains scoped to its old authority. New comparability requires review. |
| Unknown impact | Quarantine dependent uses whose validity cannot be confirmed; preserve unrelated verified package components. Abstain from strong affected claims until review. |
| Mapping correction | Choose FUTURE_ONLY / RETROACTIVE_SAFE / INVALIDATE_PRIOR / HUMAN_REVIEW_REQUIRED. Explicit criterion/construct warrant for retrospective use; activate one effective interpretation lineage per observation/claim/use. |
| Rescore/regrade | Append evaluation, preserve prior output and authority, resolve active lineage via authorised adjudication. Recompute affected current profiles with fresh evaluation manifest. Historical decisions retain their former effective score reference. |
| Data-entry correction/void | Append attributable correction/void. Current authorised views reflect the correction; raw retained original stays historically attributable. No correction is competence evidence itself. |
| Policy/model update | New version plus scope/effective state. Recompute only relevant derivations/decisions. Future model cannot silently relabel old features as then-known. |
| Privacy retention/deletion | Apply authorised record, reference, cache and artifact disposition. Remove personal raw/derived duplicates and identifying links as required. Tombstone only non-sensitive disposition metadata if permitted. Reconstruction honestly degrades. |

For A→B remapping, invalidating A does not automatically establish B. RETROACTIVE_SAFE needs a reviewed statement that the recorded response/rubric components validly elicited B under those original conditions. A legitimate multi-claim task may support multiple attributable claims, but the same contribution is not duplicated across old/new effective lineages. JOINT evidence remains joint.

Deleting an evidence artifact must traverse profiles, cached reasons, instructor summaries and decision snapshots containing derived personal information. Retention is not guaranteed merely because a hash exists; identity-bearing hashes/references also follow the authorised policy. Optional debug/research data cannot be retained secretly to maintain replay. The proposal supplies no legal retention duration; the beta's authorised governance profile must.

**Reason:** correction must change current interpretation without fabricating historical performance or duplicating competence.
**Strongest counterexample:** a punctuation fix destroys every profile, while a substantive rule change does nothing; a corrected mapping makes one response count for both its old invalid claim and new claim.
**Smallest repair:** semantic impact/equivalence records, immediate affected-use barrier and explicit retrospective applicability/active lineage.
**Falsification F17:** cosmetic change preserves authorised usable evidence, semantic change selectively quarantines; remap never silently transfers or double-counts competence.
**Falsification F18:** delete authorised evidence and dependent personal copies; old trace reports PARTIAL/UNAVAILABLE rather than retaining forbidden content.

## S15. Anti-loop, self-confirmation and future-model safeguards

A recommendation is a policy output, not new evidence about the learner. The following MUST NOT enter a competence profile as performance: model-generated learner labels, recommendation acceptance, a repair offer, clicking an explanation, a learner declaration, or repeated practice treated as independent novel evidence.

The unsolicited diagnostic/help budgets in S12 limit intervention, not eligibility for an explicitly requested learning action. A declined repair stays suppressed for that session unless the learner changes the request or a separately authorised mandatory administration changes. Completing the offered repair does not prove that the hypothesised difficulty was resolved. Subsequent permitted assessment may contradict it; the engine MUST retain competing explanations such as ambiguous item, scoring error, unsupported mapping, language/access mismatch or inconsistent conditions. If the only available task repeats the same exposed answer, report the evidence limit rather than force another confirmation.

Where an approved diagnostic can distinguish competing hypotheses, the claim/package marks that discriminating purpose and authored priority. It remains subject to the ordinary probe budget and assistance/agency rules. The engine cannot escalate a hypothesis solely through confirmatory selections; absent a valid discriminating opportunity, retain uncertainty or request authorised review. This adds no unbounded probe branch.

Selection context belongs to every opportunity: requested versus policy-selected, candidate scope and rule, task/dependence group, prior exposure/support and relevant administration conditions. A deterministic policy has no invented random assignment probability. Observed performance on selected tasks is conditional on that selection; it is not an unbiased sample of all course competence.

Future model/experiment gate, outside beta: specify the intended decision and outcome window, purpose/access permissions, consent or applicable institutional authorisation, comparison protocol and actual assignment probabilities where randomisation exists. Evaluation MUST avoid learner, item-family, source-version, course and time leakage appropriate to the intended deployment claim; holdout choice and resulting generalisation limit are explicit. Features cannot use future responses or post-outcome scoring revisions at historical prediction time. Synthetic/model-generated scores are not independent gold labels. Scorer drift and policy-induced selection must be assessed separately from learner change. Debug telemetry cannot silently become research/training data; that requires a new authorised purpose and validity review.

**Reason:** a policy that measures only its own preferred questions can manufacture apparent certainty.
**Strongest counterexample:** the engine repeatedly teaches an exposed answer, observes correct repeats and trains a model to predict its own mastery label.
**Smallest repair:** dependence-aware evidence, intervention budgets, selection provenance and a separate model/purpose promotion gate.
**Falsification F19:** ten exposed repeats and accepted recommendations add no independent novel evidence; an alternative valid result can rebut the repair hypothesis.
**Falsification F20:** an offline evaluation using future scoring or overlapping answer families is rejected for its intended claim; deterministic logs contain no fabricated propensity.

## S16. Instructor evidence and role-appropriate explanations

Instructor reporting has three separate layers: recorded observations, a bounded interpretation under the reviewed claim contract, and an optional review/teaching action. A proposed class difficulty is a hypothesis, accompanied by plausible item/scorer/conditions alternatives and inspectable authorised evidence. It is never automatically a diagnosis of motivation, aptitude or misconception.

Every aggregate states its population and denominator: enrolled/eligible, offered the relevant opportunity, committed a response, effectively evaluated and eligible for this inference. Pending scores, skips, missingness and invalid items remain visible as distinct counts. Summaries name the task/dependence groups, construct, support/conditions, source/mapping/scoring versions and time scope; percentages cannot hide that only a selected subset was tested.

A reviewed release profile specifies role/scope permissions, permitted fields, minimum usable evidence, privacy/small-cell rules and suppression behaviour. Missing release policy means no aggregate hypothesis release. Failing aggregate privacy rules MUST NOT fall back to raw responses. An individually authorised teaching view is a separate access decision, with its own purpose and permissions; it is not an automatic workaround. Cross-course/cohort comparison requires compatible contracts and its own authorised use.

Learner projection: one primary activity, a short reason describing the actual decisive rule, and a permitted escape/alternative. Example templates: “You asked for a worked example”; “This unit schedules a review now”; “There is not enough usable evidence for this requirement yet”; “This assessment permits access support but not coaching.” The text must match the record. A repair offer can say “These responses suggest reviewing this criterion” only when that criterion-specific evidence is usable; it cannot say “You have misconception X” merely because a branch fired.

Instructor projection: scoped observations, bounded contract conclusion, alternatives and review links. Authorised engineering projection: dependency manifest, exclusions, rule/ties and reconstruction status. Rich internals do not prescribe navigation, animation or expose a technical metadata wall to learners.

| Backend condition | Maximum honest product claim |
|---|---|
| UNMEASURED / insufficient evidence | Not enough usable evidence; no “not learned” or numeric ability estimate. |
| Supported success | Demonstrated under recorded support; no unaided transfer claim. |
| Contract met | Named construct under named conditions/time; no universal mastery. |
| Novel or delayed check | That transfer/delay scope only; neither substitutes for the other. |
| Stale/quarantined evidence | Current conclusion unavailable/review required; no retained current badge from stale cache. |
| Scheduled review | Review scheduled; no calculated forgetting probability. |
| Session work complete / explanation viewed | Work/review activity complete; no inferred competence change. |
| Next action / repair offer | Policy recommendation or bounded hypothesis; no proven causal benefit or learner diagnosis. |
| Screen-only task | Screen performance; no physical execution competence. |

**Reason:** an explanation is useful only when its evidence and permissions constrain its wording.
**Strongest counterexample:** a class dashboard diagnoses weakness from five policy-selected responses and reveals a small group when aggregate release fails.
**Smallest repair:** explicit denominators, bounded alternative-aware claims and independent role/release decisions.
**Falsification F21:** pending/skipped/invalid opportunities change their own denominators without becoming failures; privacy suppression never triggers raw fallback.
**Falsification F22:** each visible label is checked against its actual evidence/rule/version; a stale profile cannot render a current competence badge.

## S17. Small beta, acceptance gates and explicit cuts

The proposed first beta is approximately 20 learners in one approved course-local package, with a bounded set of instructor-reviewed claims and supported task types. This is a proposed scope for owner confirmation, not a committed deployment. Its purpose is defect discovery and descriptive usefulness/inspectability. It cannot establish population reliability, calibrated mastery, efficacy, fairness across groups or universal instructional sequencing. Before/after improvement and recommendation acceptance are not causal effect estimates.

Minimum included loop: approved instruction/example; guided practice; a permitted retrieval/probe; preserved response and reviewed evaluation; bounded evidence conclusion; one deterministic next action with alternatives; correction/quarantine; learner escape; and a scoped instructor view if separately authorised. Human-reviewed constructed response is allowed with honest pending states and reviewed rubrics. AI scoring may remain an experimental annotation; it cannot silently become effective evidence. The chosen pilot determines the supported subset rather than requiring every assessment type.

Before pilot use, the accountable owners MUST approve: source scope/content and evidence contracts; task/rubric and scorer authority; availability/protected/access policies; privacy/release/retention/deletion rules; action resources and policy defaults; response/evaluation correction procedures; and the fixture acceptance protocol. An undefined required field produces the specified blocked or review state. The proposal does not invent institutional permissions.

Beta cuts: no required KC ontology, BKT/PFA/IRT model, universal memory scheduler, learned policy, off-policy optimisation, general service graph, QTI import/export, high-stakes automated grading, cross-course optimisation or physical competence inference. A pilot requiring authentic physical evidence needs a reviewed protocol/rater/rubric pathway before that use; otherwise abstain. No legacy-studygrid product shell or particular database/API deployment is implied.

Cross-domain fixtures are hypothetical contract tests, not authoritative curriculum or regulatory claims:

| Domain | Bounded construct / adversarial distinction |
|---|---|
| Mathematics | Applying a transformation with a novel expression versus repeating the same worked answer; joint reasoning must not split into independent mastery credits. |
| Medicine | Course-approved reasoning on a hypothetical case versus clinical competence; screen explanation cannot authorise patient care performance. |
| Physical skill | A recorded explanation versus observed execution under a reviewed protocol; absent authentic evidence means unsupported physical claim. |
| Law | Source- and jurisdiction-versioned hypothetical interpretation versus general legal competence; changed source quarantines affected claims. |
| Software engineering | Explaining a concept versus constructing/debugging under specified tools/support; executed tool assistance is part of conditions. |
| Literature/humanities | Rubric-scoped argumentation with legitimate alternatives; multiple valid interpretations cannot become one answer-key misconception. |

These fixtures check that domain specificity lives in reviewed content/evidence contracts while common lifecycle and integrity rules remain stable. They do not claim that one evidence threshold works in all domains.

A later implementation must pass the applicable F01–F25 fixture specifications with exact versioned inputs and expected dispositions, plus independent concurrency/integrity/privacy checks and role/device delivery checks. Falsification tests here are specifications; none is represented as executed software validation. General's separately routed engineering, regression and cross-domain reviews remain acceptance inputs.

Pilot stop/containment conditions: coaching leak in protected assessment, cross-context access leak or raw-response corruption requires immediate affected-flow stop and incident review. Mapping/scoring/source defects quarantine affected inference and decisions before recomputation; unaffected approved teaching may continue. Unavailable reconstruction/privacy outcomes must be visible and obey their policies. Experience/completion/uptake thresholds and observation windows are predeclared for the selected pilot, not invented after observing results.

Duplicate evidence corruption, destructive history rewrite, or consequential UI/backend evidence-strength inversion also stops the affected flow. Stuart's 20-case integrity subset is a required future gate alongside applicable full-matrix cases; a green specification checklist alone is not a software PASS.

**Reason:** a small pilot can discover broken contracts but cannot validate a general intelligence model.
**Strongest counterexample:** a smooth 20-person demo is promoted as mastery accuracy and teaching efficacy while late scores or protected help corrupt evidence.
**Smallest repair:** narrow included loop, pre-use authority gates, explicit stop/containment conditions and descriptive claims only.
**Falsification F23:** each hypothetical domain supports the appropriate bounded claim or explicit abstention without domain-specific data leaking into another learner/context.
**Falsification F24:** injecting a protected coaching leak or invalid mapping triggers its containment rule; pilot success metrics cannot override integrity or validity.

## S18. Unresolved hypotheses and owner decisions

This draft fully specifies proposed default behaviour. The following remain research/policy hypotheses, not hidden runtime discretion. HARD integrity/access rules require authorised policies; a default heuristic cannot override them.

| Key / type | Exact unresolved proposition | Smallest next validation / consequence |
|---|---|---|
| H01 · HEURISTIC | The B0–B5 order is more useful than reviewed alternatives for the selected pilot. | Inspect decisions and predeclared outcomes; compare only under an appropriate protocol. No efficacy claim from uptake. |
| H02 · HEURISTIC | A 48-hour urgency window is useful and does not distort explicit goals. | Check real obligation conflicts; explicit selected scope still wins. Version change if needed. |
| H03 · HEURISTIC | Pool cap 100 is sufficient for a useful bounded scope. | Catalogue fixtures and abstention frequency; raise/split scope explicitly, never truncate silently. |
| H04 · HEURISTIC | One automatic probe per claim/two per session balances usefulness and interruption. | Inspect declines, escapes and unresolved evidence; change versioned budget, not competence thresholds. |
| H05 · HEURISTIC | One unsolicited repair and the proposed two-distinct-error offer trigger are acceptable. | Reviewed criterion-specific cases/competing item explanations; retain agency and no diagnosis. |
| H06 · MEASUREMENT | Each pilot claim's sufficiency, dependence and novelty predicates support its intended use. | Author review and counterexamples, scorer agreement where appropriate; revise/quarantine claim when unsupported. No universal count. |
| H07 · MEASUREMENT | The selected rubric/scorer and conditions yield usable evidence for that claim. | Reviewed samples, disputes and access/conditions checks; pending/human review when unproven. |
| H08 · TEACHING SEQUENCE | The authored introduction/probe/practice ordering serves this course. | Inspect learners with prior knowledge and alternative needs; retain approved optional paths. Not a logical prerequisite. |
| H09 · EMPIRICAL | Proposed prerequisite relations predict meaningful difficulty. | Test competing explanations and domain cases; remain soft unless independent course access authority exists. |
| H10 · EMPIRICAL | Scheduled review or a delayed/novel check supports a specific retention/transfer use. | Define actual timing/novelty/outcomes and warrant; no universal forgetting curve or causal conclusion. |
| H11 · PRODUCT/POLICY | Reason templates, suppression and alternatives are understandable and useful. | Descriptive learner/instructor feedback and explanation-binding checks; revise projection without altering evidence. |
| H12 · GOVERNANCE/ENGINEERING | Selected retention and input manifests permit required reconstruction without excess sensitive retention. | Purpose/access/deletion review and deletion fixtures; accept explicit PARTIAL/UNAVAILABLE or revise permitted scope. |

Smallest owner decisions before any beta authorisation:
1. Choose the bounded course/package, accountable content/claim reviewer, learner scope and supported task types.
2. Choose assessment stakes/protected modes and effective scoring/access authority, including task-scoped accommodations.
3. Approve role-specific privacy/release/retention/deletion purposes and whether any future research/training use exists.
4. Confirm the beta's descriptive success/stop protocol and proposed policy defaults after General reconciles engineering/regression/cross-domain returns.

These decisions do not block producing this proposal. General owns reconciliation and any next owner ask; Sol does not start implementation or wake peers.

**Reason:** explicit unresolved propositions keep a crisp implementation contract from pretending scientific certainty.
**Strongest counterexample:** an engineer treats arbitrary probe counts or authored prerequisite edges as validated universal learning rules.
**Smallest repair:** typed hypotheses, named owners and versioned policy/claim acceptance; hard integrity remains separate.
**Falsification F25:** changing a heuristic cannot bypass protected/access rules or retroactively convert old activity into stronger evidence.

## Explicit synthesis adjudications

This proposal resolves disagreements rather than averaging incompatible claims. “Keep” preserves an intended function under a narrower contract; it does not mean the original draft was already implementable.

| Disagreement | Decision incorporated in Draft 2 |
|---|---|
| Observation includes scores (Research1917) versus separated evaluation (Bob; Research1956) | SPLIT response/presentation facts from scoring acts and effective interpretation (S06). |
| Large primitive graph versus compact beta | KEEP semantic boundaries; REVISE into five logical record families and sparse relations (S02). No mandatory graph/KC service. |
| Evidence checklist versus validity argument | ADD intended use, warrant, rebuttals, sufficiency, conditions and generalisation at definition time (S05). |
| Recognition/application treated as contradiction | REVISE to separate comparability, disagreement, invalidity and source change (S07). |
| Approved mapping assumed correct | SPLIT approval from usable validity; ADD immediate affected-use quarantine (S04/S14). |
| Introduction must always precede probe | REMOVE universal ordering; approved probe-first remains possible (S09/S11). |
| Readiness, sequence and prerequisite as one hard gate | SPLIT course availability, logical requirement, empirical relation and teaching preference (S12/S18). |
| Accessibility capability OR versus generic intersection | REVISE to authorised task-scoped exception resolution followed by integrity/access guards (S10). No blanket bypass. |
| Exact replay capsule versus privacy/trace growth | KEEP exact retained input values or recoverable references; REVISE to bounded manifest, complete scoped candidate IDs and FULL/PARTIAL/UNAVAILABLE (S13). Digests alone fail. |
| Observation-only cache watermark | ADD support and evaluation/effective lineage plus authority/mapping/config dependencies (S03). |
| Bounded shortlist versus candidate omission | REVISE to complete generation within declared bounded scope; over-limit abstains (S12). |
| Authentic physical evidence versus tiny beta | KEEP capability contract; CUT unsupported physical inference and defer implementation unless selected pilot requires it (S08/S17). |
| Optional BKT/PFA comparator | REMOVE from beta; reserve a separately justified future challenger (S15/S17). |
| Transport-only idempotency versus Bob's semantic uniqueness | ADD response-slot uniqueness independent of request keys and scoring-purpose lineage; pending work is recoverable (S06). |
| Kevin/QA soft prerequisite cycles versus hard availability cycles | SPLIT quarantined optional relations from affected BLOCKED_CONFIGURATION administration; neither is learner failure (S12). |
| Bob's unresolved soft TTL versus a complete proposed default | ADD recomputation on material used-input change before delivery, with no beta soft TTL exemption; physical implementation remains engineering work (S13). |
| Every version change invalidates everything | REVISE to reviewed semantic impact/equivalence and affected-use barrier (S14). |
| Historical remapping silently moves competence | REMOVE silent transfer; ADD explicit retrospective dispositions and one effective lineage (S14). |
| Overrides merely change UI while nagging persists | REVISE session suppression and zero competence change (S11/S12). |
| Earlier Sol removal of proprietary framing versus current owner direction | KEEP inspectable policy/integration value proposition; REMOVE proprietary-science/efficacy claim (S01). |
| Failed aggregate privacy falls back to raw data | REMOVE automatic fallback; independent individual access decision only (S16). |
| Missing response grade treated as competence failure | SPLIT declared grade policy from construct-valid learner evidence (S06). |
| Sparse evidence forces shutdown or arbitrary probing | SPLIT inference and policy abstention; approved teaching remains possible (S07/S12). |
| Future propensity logging under deterministic policy | REMOVE invented probabilities; KEEP selection context and future actual-assignment gate (S15). |
| Sophisticated internals require a complicated product | REMOVE shell prescription; ADD role-appropriate evidence-capped projections (S16). |
| Follow-on diagnostic fixtures versus blind confirming repair | ADD discriminating approved probe purpose/priority within existing budgets, never automatic hypothesis escalation (S15). |

## Exact-source register

All sources below were read as exact bodies, not inferred from titles or snippets. Review judgments were independently adjudicated; none supplies new empirical validation.

| Source | Exact commit / blob |
|---|---|
| General current route: `routes/GENERAL_20261001_2006_SOL_ENGINE_V1_DRAFT2_SYNTHESIS.txt` | Discovery/frozen commit `5e7d22ed3b1ba8082faea93c22c4952be73083a0`; blob `17f63cedbc7d4edd7935265626ec3c1bc0fadd56`. |
| Draft 1: `design/STUDYGRID_ENGINE_V1_FIRST_PRINCIPLES_DRAFT_1.txt` | Commit `bc1a346cf6c6a95d081804e2d60d980533d16d61`; blob `6d0560091b587220609740970154e64541f4b7c4`. |
| Research primitive review: `routes/RESEARCH_CF0044_20261001_1917_ENGINE_V1_PRIMITIVES_ADVERSARIAL_REVIEW_DONE.txt` | Commit `93dbc55c00579128a2b96cbb44c8094c5ff9b007`; blob `b4077d8d0331e75158856ef632925910f7903bb6`. |
| Bob contradiction attack: `routes/BOB_20261001_1947_ENGINE_V1_DRAFT1_IMPLEMENTATION_CONTRADICTION_ATTACK_DONE.txt` | Commit `4b2849f6fda9e75205cb4cad516a550080cdfa7d`; blob `59cc9556ecc1b856ff87540642ba57e886ee8a57`. |
| Sol independent return: `routes/SOL_20261001_CF0043_ENGINE_V1_DRAFT1_ARCHITECTURE_ATTACK_DONE.txt` | Commit `1e5c05892101d566ae316f4eb34c3f5a477ba8fa`; blob `cc6690dde6c841e6701f53cc1e8e06d01f2c4183`; full report `reports/SOL_20261001_ENGINE_V1_DRAFT1_ARCHITECTURE_ATTACK/REPORT.md`, blob `8d116679e646a89e63fe3b32356015b86c97b75b`. |
| Additional completed Research measurement attack: `routes/RESEARCH_CF0044_20261001_1956_ENGINE_V1_DRAFT1_MEASUREMENT_VALIDITY_ATTACK_DONE.txt` | Read at frozen discovery `5e7d22ed3b1ba8082faea93c22c4952be73083a0`; blob `4ff0c17116ad152488cf35e059e0557e650e5b39`. |
| Additional completed Stuart regression attack | Terminal route `routes/STUART_20261001_1948_ENGINE_V1_DRAFT1_REGRESSION_FALSIFICATION_AMEND.txt` at frozen discovery, blob `92fef8f26bb564b91cf10f88345e25717d401b19`; full report `reports/STUART_ENGINE_V1_DRAFT1_REGRESSION_FALSIFICATION_REPORT.txt` at `efdfacf694ed7272710d65719a0978ae832bfd96`, blob `2e699d42b3a30c1a9a1b8cb37464f304a4248dcc`. |
| Bob complete follow-on contract | `routes/BOB_20261001_2014_ENGINE_V1_DATA_REPLAY_CONTRACT_DONE.txt` at frozen pre-publication main `7f5926287f17310b6b3e54b87cc69f9ef1d807bc`; blob `a24c51ac09e978b8f1cd1c7a3488bd99a907ae82`. Full contract is inside this route. |
| Stuart follow-on matrix | Terminal `routes/STUART_20261001_2017_ENGINE_V1_FALSIFICATION_MATRIX_AMEND.txt` at pre-publication main, blob `28c8fb8be695b4863da5319635abe0678a4956e4`; full `reports/STUART_ENGINE_V1_ADVERSARIAL_FALSIFICATION_REGRESSION_MATRIX.txt` at `1b4e37a8638ef226785f530d92eb67a53fa71863`, blob `5dd981a86590b5d5314e5f0f3d538a6557effa06`. |
| Kevin follow-on cross-domain fixtures | Terminal `routes/KEVIN_20261001_2029_ENGINE_V1_CROSS_DOMAIN_SCENARIO_ATTACK_DONE.txt` at pre-publication main, blob `df7131918b1ac08b49db406214c68810eca6c512`; report and both scenario sets at `0aa96f5f832744f9bf051ab9bcb663c00398571e` under `reports/KEVIN_20261001_ENGINE_V1_CROSS_DOMAIN_SCENARIO_ATTACK/`: `REPORT.md` blob `8c8bede84f386d2a982ebecefd3087d853195cbe`, `SCENARIOS_A_K01_K20.md` blob `b946e2f8bbdea26b8a77ca0584dd24ea788555a1`, `SCENARIOS_B_K21_K38.md` blob `01074848da1ad57321a9be13f6060d41b495b146`. |

Current owner direction supplied through General's route: first principles; fact/interpretation separation; teach and test; non-timer-centred; domain neutrality; protected no-coaching; learner agency; simple experience with inspectable internals; no fake precision; proprietary policy/integration value. Current Base CGPTBASE-R0004-N8V6, Active Corrections and verified CF-0043/CF-0047 identities govern this worker execution.

Already-terminal follow-on returns were additionally consumed at pre-publication refresh: Bob's complete data/replay contract, Stuart's full 76-case matrix and Kevin's full report plus both 38-scenario files. They informed the explicit semantic-slot, cycle, freshness, discriminating-probe and critical-stop refinements above. They have not reviewed this new Draft 2. General still owns acceptance and reconciliation; this is not a canonical promotion.

## Route coverage register

| Required contract | Location / falsification anchors |
|---|---|
| 1 Purpose and non-goals | S01 / F01 |
| 2 Smallest primitive set | S02 / F02 |
| 3 Durable/derived/transient | S03 / F03 |
| 4 Content/source/authority | S04 / F04 |
| 5 Attempt/response/scoring/evidence | S05–S06 / F05–F06 |
| 6 Learner state, uncertainty, abstention | S07 / F07 |
| 7 Exposed/demonstrated/learned/retention | S08 / F08 |
| 8 Action dimensions and teaching loop | S09 / F09 |
| 9 Protected assessment/access | S10 / F10 |
| 10 Lexicographic policy, ties, no action, unknown, override | S11–S12 / F11–F14 |
| 11 Decision reconstruction/revalidation | S13 / F15–F16 |
| 12 Revision/remap/regrade/deletion | S14 / F17–F18 |
| 13 Anti-loop/self-confirmation | S15 / F19–F20 |
| 14 Instructor evidence boundaries | S16 / F21 |
| 15 Explainability projections | S16 / F22 |
| 16 Cold start/declarations | S11–S12 / F11–F14 |
| 17 Beta boundaries/cuts | S17 / F23–F24 |
| 18 Exact unresolved hypotheses | S18 / F25 |

Each S01–S18 contract includes its reason, strongest counterexample, smallest repair and at least one falsification specification. The complete proposal specifies behaviour while leaving named empirical hypotheses and owner-authority choices honestly unresolved.

