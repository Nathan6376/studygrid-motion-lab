# StudyGrid — Next Website Prototype Build Contract (Preparation)

Prepared by: ChatGPT General CF-0047
Date: 2026-10-01
Status: BUILD-CONTRACT PREP COMPLETE — IMPLEMENTATION STILL HELD

## Purpose
Translate Nathan's October 1 owner review and the reconciled Engine v1 Draft 2 behaviour boundaries into one bounded website revision contract. This is preparation for the next clickable HTML prototype. It does not mutate the accepted frontend.

## Exact current frontend base
- `StudyGrid-CF0042-QB17R2-stuart-defect-repair.html`
- Drive `1k0d69ZOrgs4NRRLRORKBmIwOR1Q0mE46`
- SHA-256 `874e4a743050d308759a9dcaefa9cc3296f8841c37b12e3acf5df2225ea49aab`
- version `v7.20-cf0042-qb17r2-stuart-defect-repair`

## Governing owner inputs
- October 1 product-flow/study-mode review `9e44452c4687b03fe62a1bc6faee387cc2713c6d`
- exact candidate/routing correction `18c3f30159717dfe971fb0ae8c4cf63756ba0adb`
- domain-neutral interaction/ordered assessment delta `cfe1071cd15faab19fe4195b30201f51aae42afd`
- non-timer-centric adaptive UX/beta delta `014280c9ef7c52341144f086a85df1a81d407da9`
- General Engine v1 Draft 2 reconciliation `b6ac02d321293a46002636f6e6286e1f067e9ea8`

## Product method
Do not patch screens independently. The next prototype should be one coherent release candidate following: purpose → research → multiple concepts → comparison/selection → coherent implementation → independent QA.

## Prototype job
The learner should open StudyGrid and immediately understand:
- where they are;
- what matters now;
- what StudyGrid recommends next;
- why that recommendation exists in plain language;
- what alternatives they have;
- what they completed and what happens next.

The visible product stays simple even when the engine reasoning underneath is sophisticated.

## Bounded revision areas

### A. Signed-in root and orientation
1. Signed-in Home/current workspace is the product root; Back must not walk into onboarding/public flow.
2. `Professor Home` becomes `Home`.
3. Reconsider/merge the empty `Your Classes` destination into a useful Home/current-workspace model.
4. Keep class-centred study plus a clear general/self-directed study path.
5. Reduce duplicated global/course chrome while preserving easy class switching and orientation.

### B. One strong next step
1. Make `Continue` / `Up next` the primary learner action.
2. It is a recommendation, not a mastery verdict.
3. Show a short human reason tied to course/evidence context, e.g. source sequence, unfinished work, evidence gap, scheduled review, learner-selected goal or approved prerequisite repair.
4. Always offer an escape/secondary route when appropriate.
5. Do not make time-available the primary entry question. Time/effort may optionally narrow choices.

### C. Stable study workspace
1. Preserve shell/layout anchors across Learn/Test/Support or equivalent same-level modes.
2. Remove large unnecessary persistent panels that steal study space.
3. Avoid schedule/filter/button shifts that move the user's target around.
4. Preserve easy class switching without repeating course identity everywhere.
5. Keep keyboard focus visible but redesign sharp green/white square focus artifacts into one consistent on-brand focus system.

### D. Learn must actually teach
1. Lesson surfaces cannot be thin shells followed immediately by quizzes.
2. Use approved instruction/explanation, worked examples, guided practice and retrieval/performance practice as distinct jobs.
3. `Mark as reviewed` must either have a real semantic job or be removed/replaced; a tiny border cannot stand in for learning progress.
4. `Quick / Focus / Deep` labels stay only if each corresponds to a genuinely different job. Do not keep timer-centric pseudo-modes.
5. One recommended next step should dominate; browse/notes/questions remain secondary exploration, not five equal starting points.

### E. Practice / question interaction system
Interaction type is first-class and domain-neutral. Prototype must support or cleanly scaffold at least:
- `single_select`
- `multi_select_unordered`
- `sequence_order`
- `match/pair`
- `categorize`
- `short_text/constructed_response`
- `numeric/formula` where applicable
- `hotspot/diagram` where applicable

For `sequence_order`, the expected operation must be obvious. Visible numbered order is required. Drag may be optional, never the only practical input; keyboard/single-pointer alternatives such as Move up/down or Choose position are required.

The current owner-observed multi-select defect must be source-reproduced and repaired in the next prototype. If the underlying construct is ordered, do not repair it as ordinary checkbox multi-select; redesign it as sequence order after source verification.

Question/content review must also catch answer leakage (e.g. a prompt giving away the referenced case/rule) and must verify uncertain source wording instead of normalising speech guesses.

### F. Answer / feedback experience
1. Do not dump dense metadata after every answer.
2. Separate: what happened, what the learner can learn from it, and what to do next.
3. Confidence, when voluntarily collected before feedback, is a self-report; do not make the whole control visually scream success or treat confidence as mastery.
4. Repeated/answer-exposed success must not be presented as fresh proof of competence.
5. Broken scorer/content/interaction states must route to a neutral technical/content-review state, never `you got it wrong`.

### G. Gentle help and remediation
1. In low-stakes practice, StudyGrid may quietly offer another explanation/example or a bounded prerequisite repair when the evidence supports that move.
2. The wording must not shame the learner or declare a trait.
3. Explicit help remains available whenever policy permits.
4. Unsolicited help/remediation is episode-bounded to avoid loops.
5. If StudyGrid does not know enough, it may teach, offer a probe or say the evidence is not clear enough; it must not fake certainty.

### H. Protected assessment behaviour
1. Protected quiz/exam mode suppresses coaching/reveal according to the assessment policy.
2. Accessibility/accommodation support remains independently available.
3. The UI must make the different mode clear enough that cached coaching or explanations cannot leak into the protected attempt.
4. A recommendation issued in practice must be revalidated before delivery if the context becomes protected.

### I. Study Set review queue
1. Keep the 15-question review concept.
2. Keep `Approve and next` with a physically stable target position.
3. Last item must enter an explicit completion/finalisation state.
4. Draft / Ready / Published / Held / All must read as real state, not decorative badges.
5. Completion should show accomplishment, what changed and the next useful action.

### J. Completion and forward motion
1. End-of-session state should feel like progress, not retreat.
2. Show: what was completed; what changed in the learner's evidence/progress in appropriately bounded language; recommended next action; optional return/exploration.
3. Avoid unsupported `mastered`/`retained` claims. Prefer evidence-strength language whose exact vocabulary is separately owner-reviewed.
4. Rewards/seeds collect automatically when earned; reward state must not become the learning task and disconnected local failures cannot be shown as success.

### K. Instructor context
1. Instructor → Study transitions must preserve/declare role and context so the user knows whether they are previewing, studying personally or acting as instructor.
2. Instructor preview/demo must not create learner evidence, progress or rewards.
3. Instructor views in this prototype should show inspectable real evidence patterns and item/content issues, not behavioural surveillance or causal claims.
4. Professor-facing digests/automation remain hypotheses for real professor discovery, not assumed product truth.

### L. Welcome / brand
1. Preserve high-value copy: `Your class, easy to learn.` and `One common path from class material to useful practice.` where they serve distinct jobs.
2. Welcome 1→2→3 sequence continues automatically with polished purposeful motion and reduced-motion support.
3. Edge gloss may remain subtle; avoid full-surface wash.
4. Do not add slogans/animation simply to decorate the page.

## Engine/UI boundary for the prototype
The clickable prototype may simulate engine outputs, but it must keep the contract shape correct:
- UI renders a recommendation and reason; it does not own learner truth.
- UI submits committed responses/support/agency actions through an adapter boundary.
- current evidence profile and next action are read models/outputs, not mutable page state presented as authority.
- local fixtures may stand in for backend responses, but the fixture shape must be replaceable by the future API.
- instructor preview/synthetic fixtures use non-learner contexts.

## Prototype QA acceptance
Before Nathan receives the next HTML, independent QA must cover at minimum:
1. signed-in route/root continuity;
2. stable same-level study-mode layout;
3. keyboard/focus/escape/return-focus behaviour;
4. reduced motion;
5. multi-select and ordered-response correctness;
6. protected-assessment help suppression with accessibility preserved;
7. last-item/finalisation states;
8. no broken-item/scorer state recorded as learner failure;
9. learner override/help/dismiss behaviour without competence inference;
10. no duplicate response/recommendation from obvious UI retries;
11. desktop/tablet/phone layout smoke;
12. unchanged current accepted flows outside the bounded revision;
13. exact current source/candidate identity and a new exact candidate identity after build;
14. owner-visible HTML artifact delivery for review.

## Build gate
PREPARED FOR IMPLEMENTATION RELEASE AFTER THE ENGINEERING-INTEGRITY REVIEW AND OWNER/GENERAL RELEASE.

No HTML mutation is authorised by this preparation file alone.
