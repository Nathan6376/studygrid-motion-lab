# StudyGrid Engine v1 — General Draft 2 Reconciliation

Prepared by: ChatGPT General CF-0047
Date: 2026-10-01
Status: GENERAL RECONCILIATION COMPLETE — DESIGN ONLY — NO IMPLEMENTATION RELEASE

## Inputs reconciled
- Draft 1: `design/STUDYGRID_ENGINE_V1_FIRST_PRINCIPLES_DRAFT_1.txt`
- Research measurement/validity attack: `265b0c644382563bc99042bef79b9a261b4c8009`
- Sol independent architecture attack: `1e5c05892101d566ae316f4eb34c3f5a477ba8fa`
- Sol proposed Draft 2 provider artifact: `StudyGrid-Engine-v1-Draft-2-PROPOSED.md` / Drive `1Ap0p-ua7L-lrR53EjEnx4JxqBuK7vfwR`
- Bob implementation contradiction attack: `4b2849f6fda9e75205cb4cad516a550080cdfa7d`
- Bob implementation-safe data/replay contract: `7c637cf86bf9d7727f2f1928bb74276af8d72f7f`
- Stuart adversarial falsification/regression return: `2454712068900e8d87599582c8841ed8e32925c1`
- Kevin cross-domain scenario attack: `7f5926287f17310b6b3e54b87cc69f9ef1d807bc`
- Current owner directions: first-principles, domain-neutral, non-timer-centric, teach as well as test, protected assessment blocks coaching, learner agency preserved, simple UI over inspectable intelligence, no fake mastery precision, no implementation before design gate.

## General disposition
The current Draft 2 direction is coherent enough to become the single design basis for the next gate, but it is not yet an implementation release. The workers converge on the same core repairs for independent reasons. No majority vote is used; the accepted items below are those that survive the scientific, implementation, regression and cross-domain counterexamples.

## Accepted Draft 2 contract

### 1. Facts, interpretations, estimates and decisions stay separate
StudyGrid must preserve the distinction between:
1. what opportunity/activity was presented;
2. what the learner actually submitted or did;
3. how that response was scored/evaluated;
4. what evidence that may support under an explicit claim/use contract;
5. the current derived learner evidence profile and uncertainty;
6. the pedagogical hypothesis about what could help;
7. the policy decision for the next permitted action;
8. what was actually delivered and what happened next.

A correct or incorrect answer is not, by itself, "knowledge" or "lack of knowledge".

### 2. Few durable facts; derived state is replaceable
Beta should use one deployable application and one relational store unless later engineering evidence justifies otherwise. Durable authority should stay small: versioned package/source/task/claim/mapping/rubric/policy definitions; presentation/response/support facts; evaluation revisions; accepted decisions/execution facts; approvals/corrections/dispositions. Learner profiles, misconception/error-pattern hypotheses, recommendation candidates, instructor summaries and UI projections are derived and recomputable.

No microservice, event-bus, graph-database, universal ontology or one-table-per-noun requirement is accepted for beta.

### 3. No universal Learning Target atom
Course outcomes, operational learning claims, source assertions/procedures and optional model-level knowledge components are different things. Beta requires operational claims tied to course/personal-study authority and evidence contracts. Knowledge components remain optional/deferred unless a future validated model actually requires them.

### 4. Evidence validity begins before the answer
Each evidence-producing activity must have an author-time contract describing the intended claim/use, conditions, scoring/rubric, sufficiency, task-family/dependence rules, attribution, support/exposure limits, known validity threats and transfer/generalisation requirements where applicable.

Repeated surface variants, answer-exposed repeats or several tasks sharing one solution template cannot automatically count as independent proof.

### 5. Raw response and score are different records
A learner response/artifact is the historical fact. A score/rubric/AI-or-human judgement is a revisable evaluation artifact with its own version and lineage. Regrading never rewrites the original response. Invalid or unsupported evaluators cannot manufacture learner failure.

### 6. Evidence profile, not fake mastery percentage
The beta learner model is a conservative evidence profile, not a universal probability of mastery. Its top-level states are bounded evidence dispositions such as:
- UNMEASURED
- OBSERVED_INSUFFICIENT
- CONTRACT_MET_UNDER_CONDITIONS
- REVIEW_REQUIRED

Separate reason flags distinguish sparse, pending, invalid, dependent repeats, source/mapping uncertainty, scorer uncertainty, non-comparable channels, comparable mixed results, stale evidence and unsupported constructs. Missing data is never automatically wrong.

### 7. Demonstrated is bounded; retained is not a timeless flag
StudyGrid may say the learner demonstrated a bounded capability under stated conditions and time. It must not create a permanent `retained=true` or universal `mastered` truth from thin evidence. Delayed/retention claims require an actual justified model or delayed evidence contract. Transfer/generalisation is separate from repetition.

### 8. Action types stay concrete
Learning operations are concrete things such as instruction/explanation, worked example, guided practice, retrieval/performance practice and diagnostic/assessment probe. Review/remediation describe purpose, not a magical action type. Navigation/session controls such as advance, pause, complete, exit and resume are separate from pedagogy.

### 9. Protected assessment is a hard policy boundary
Assessment purpose/stakes, coaching/reveal permissions, feedback/scoring and accessibility/accommodation are separate dimensions. Protected assessment blocks tutoring/coaching that would invalidate the assessment, while authorised accessibility support remains available. Learner override cannot bypass assessment-integrity rules.

### 10. Beta next-action policy must actually decide
The engine must use an explicit ordered policy rather than an opaque score. At minimum:
1. validate context/package/policy;
2. enforce protected-assessment/access rules;
3. determine the bounded learner/course scope;
4. generate concrete eligible actions;
5. filter by authority, validity, modality/access, repetition/help budgets and hard constraints;
6. apply ordered branches for explicit help, supported local prerequisite repair, repeated comparable error pattern, insufficient evidence/probe-or-teach, scheduled review, then approved package sequence;
7. use deterministic tie rules;
8. allow first-class no-action/blocked outcomes;
9. record one primary action, short reason and graceful alternative/escape;
10. revalidate at delivery.

Deadline/urgency, retention risk and prerequisite weakness may only affect the decision when explicitly supported; unknown does not mean failed.

### 11. Learner agency is preserved without turning choice into evidence
Accept, skip, dismiss, choose another eligible action, ask for help, continue, pause or change scope may affect the next decision. Those actions do not themselves prove knowledge, weakness, motivation, confidence or disengagement.

### 12. Help/remediation is bounded and non-shaming
Low-stakes practice may offer gentle help. Explicit help remains available when policy permits. Unsolicited remediation is episode-bounded and cannot loop indefinitely. Repeated automatic repair of the same pattern requires independent new evidence or a disconfirming probe before the engine keeps strengthening the same hypothesis.

### 13. Recommendation issue and delivery are separate
A recommendation can become stale after a source, mapping, policy, assessment state or access change. The engine must revalidate before delivery. Cached explanations must not leak answers into a newly protected assessment.

### 14. Concurrency and retries cannot create extra evidence
Semantic response slots, operation idempotency, evaluation lineage and per-learner/context decision sequencing prevent double submits, duplicate scoring and two-tab/device duplicate recommendations from silently becoming extra learner evidence.

### 15. Source/mapping/regrade/model changes are selective
History is never rewritten. Source or mapping revisions carry explicit impact/retroactivity semantics. Cosmetic source changes do not invalidate everything; meaningful changes quarantine/review only affected current uses. Historical decisions keep the versions they actually used. Model/policy updates create new derived views, not rewritten past facts.

### 16. Decision reconstruction is deletion-aware
Material decisions preserve enough bounded version/cursor/reason information for FULL, PARTIAL or UNAVAILABLE reconstruction. Privacy/retention deletion overrides any naive idea of physical immutability. Decision traces reference authoritative records instead of copying raw responses, source bodies or sensitive declarations everywhere.

### 17. Instructor evidence is evidence, not surveillance
Instructor views should use actual response/evaluation patterns, misconception/error-pattern candidates, coverage, item quality, source/mapping problems and denominators. Small-cohort/privacy suppression and scope rules are required. Hover time, cursor behaviour, delete latency and similar behavioural surveillance are not accepted as competence/confusion evidence.

### 18. AI is a helper, not course truth
AI may generate candidate explanations/questions/mappings or assist bounded scoring where separately validated. It cannot silently promote course truth, rewrite learner state, fabricate missing evidence or become the sole authority for consequential scoring. Generated content actually delivered must have retained/versioned identity.

## Beta cuts
Explicitly postpone unless later evidence justifies them:
- universal KC graph;
- BKT/PFA/deep knowledge-tracing requirement;
- universal memory/forgetting model;
- generic ontology graph;
- causal "best learning action" claims;
- cross-course optimiser;
- microservices/event bus/vector database requirement;
- automated high-stakes grading;
- broad instructor causal insights;
- raw behaviour/attention surveillance;
- full conversational AI shell as the default product.

## Required QA basis
Stuart's 76-scenario matrix becomes the reusable specification QA contract. Its 20-case MUST-PASS subset is the minimum integrity gate for beta implementation. Kevin's 38 cross-domain scenarios remain concrete behaviour fixtures and must stay represented in later tests. These specification fixtures do not prove learning efficacy.

## Remaining engineering decisions
Still require engineering review before backend implementation:
- exact physical database/schema layout;
- transaction boundaries and SQL constraints;
- score-revision precedence/adjudication implementation;
- source semantic-impact review workflow;
- retention/deletion periods;
- supported response/scoring types for beta;
- decision trace size bound and TTL;
- offline-sync support level;
- exact estimator/read-model implementation;
- API/auth/RLS boundaries;
- how the existing frontend adapter moves from local fixture state to the real engine without becoming authority itself.

## General gate
Engine v1 Draft 2 design basis: READY FOR ENGINEERING REVIEW AND WEBSITE-PROTOTYPE CONTRACTING.

Not released for production/backend implementation yet. The next phases may proceed in parallel where they do not depend on the unresolved physical engineering choices:
1. engineering-integrity review of this reconciled Draft 2;
2. exact website-revision build contract using the October 1 owner review and these engine-facing behaviour boundaries;
3. prototype acceptance plan mapping website actions to engine contracts without putting durable learner truth in the UI.
