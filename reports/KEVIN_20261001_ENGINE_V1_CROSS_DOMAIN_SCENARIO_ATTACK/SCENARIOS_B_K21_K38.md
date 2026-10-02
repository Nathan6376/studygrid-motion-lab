# Kevin Engine v1 cross-domain scenario attack — scenarios K21–K38

Continuation of the independent learner-behaviour red-team. No implementation.

## K21 — Mathematics — learner wants to keep going despite struggle
1. **Facts known:** Three valid comparable misses occur in low-stakes practice. One quiet help offer appears; learner chooses “Keep going.”
2. **Tempting unjustified inference:** Refusing help proves low motivation, or remediation should now be forced.
3. **Candidate actions:** Fresh problem; repeat help offer; forced worked example; pause.
4. **Allowed:** Let learner continue with an eligible fresh problem; consume the unsolicited-help budget for this episode and preserve passive help access.
5. **Must not:** Repeat the same nudge every item, force remediation or infer motivation/personality.
6. **Learner-facing reason:** “Got it — we’ll keep going. Help is still available if you want it.”
7. **Internal reason:** Episode help budget has been consumed; an explicit future help request remains eligible.
8. **What changes it:** Explicit help request, scope change or an independent probe.

## K22 — Mathematics — surface variants masquerade as transfer
1. **Facts known:** Five equations differ only in numbers and follow the same visible template immediately after a worked solution.
2. **Tempting unjustified inference:** Five independent successes establish transfer.
3. **Candidate actions:** Fresh structurally different problem; advance; retention label; sixth variant.
4. **Allowed:** Count as practice within one correlated family and use another family if transfer evidence is needed.
5. **Must not:** Treat variants as independent sufficiency units or create durable learned/retained status.
6. **Learner-facing reason:** “You’ve practised this pattern. Let’s try a different version to see whether it transfers.”
7. **Internal reason:** `FAMILY_DEPENDENCE` plus recent answer exposure.
8. **What changes it:** Success on independently authored structurally distinct tasks under valid conditions.

## K23 — Mathematics — long gap since prior success
1. **Facts known:** Last demonstration was 90 days ago; no validated memory model is configured for this construct and there is no delayed retrieval since.
2. **Tempting unjustified inference:** Learner probably forgot it, or a numeric retention risk can be computed from elapsed time alone.
3. **Candidate actions:** Author-scheduled review; fresh probe; normal progression; remediation.
4. **Allowed:** Offer scheduled review only if the package declares one, otherwise treat current retention as unknown and use a fresh check if useful.
5. **Must not:** Invent forgetting probability, lower competence solely from time passage or claim retention.
6. **Learner-facing reason:** “It’s been a while since this was checked, so a fresh practice item can update the evidence.”
7. **Internal reason:** `RETENTION_UNKNOWN`; elapsed time is context, not proof.
8. **What changes it:** Valid delayed retrieval or a construct-valid approved memory model.

## K24 — Mathematics — incomplete/missing telemetry during submission
1. **Facts known:** Connection drops after an answer is selected but before the server confirms commitment; client logs are incomplete.
2. **Tempting unjustified inference:** No response means wrong/abandoned, or latency means weakness.
3. **Candidate actions:** Safe resume/retry; mark wrong; create nonresponse evidence; discard.
4. **Allowed:** Mark response state `PENDING/UNKNOWN`, resolve idempotent commit status and resume/retry without duplication.
5. **Must not:** Score transport uncertainty as failure, infer disengagement or create duplicate evidence.
6. **Learner-facing reason:** “I’m not sure your answer saved, so I’ll let you retry without counting it twice.”
7. **Internal reason:** Submission/software state is not learner evidence.
8. **What changes it:** Server confirmation, idempotency lookup or successful recommit.

## K25 — Biology/health science — gentle help after repeated low-stakes struggle
1. **Facts known:** Two independently valid application misses share one isolated conceptual error; no help has yet been offered this episode.
2. **Tempting unjustified inference:** Two misses prove a durable misconception or require stopping practice.
3. **Candidate actions:** One quiet explanation/example offer; fresh task; forced remediation; advance.
4. **Allowed:** Offer one non-blocking support action with Keep going available.
5. **Must not:** Store a permanent diagnosis, force a modal interruption or keep resurfacing the offer after dismissal.
6. **Learner-facing reason:** “This concept is showing up twice. Want a quick example, or keep going?”
7. **Internal reason:** Repeated valid pattern supports bounded help, not a trait.
8. **What changes it:** Disconfirming response, item-quality issue or learner choice.

## K26 — Biology/health science — historical success with uncertain current applicability
1. **Facts known:** Learner performed well on anatomical identification last term. Current course reuses the claim, but no current-term evidence or validated retention model exists.
2. **Tempting unjustified inference:** Old success guarantees current mastery, or old success has expired into weakness.
3. **Candidate actions:** Fresh probe; current introduction; skip as mastered; remediate.
4. **Allowed:** Preserve old performance as historical evidence and use a fresh bounded check where appropriate.
5. **Must not:** Auto-certify mastery, auto-fail for age or generate precise retention probability.
6. **Learner-facing reason:** “You did well on this before. A quick fresh check can show how it carries over now.”
7. **Internal reason:** Historical evidence with current applicability uncertain.
8. **What changes it:** Current valid response or an approved equivalence rule between course versions.

## K27 — Biology/health science — conflicting course sources
1. **Facts known:** Textbook and new instructor handout disagree on a convention; instructor has approved the handout as current course authority.
2. **Tempting unjustified inference:** Average sources, textbook always wins, or source conflict means learner conflict.
3. **Candidate actions:** Teach approved handout rule; flag conflict; use textbook; pause for review.
4. **Allowed:** Use scoped approved current authority while retaining the conflict/provenance for review.
5. **Must not:** Mix rules, penalise a learner for the approved source or turn source disagreement into learner-state uncertainty.
6. **Learner-facing reason:** “Your course currently uses the instructor handout for this convention.”
7. **Internal reason:** `SOURCE_AUTHORITY_CONFLICT`; authority state and learner evidence are separate.
8. **What changes it:** Instructor approval change or source correction.

## K28 — Biology/health science — one complex miss after strong performance
1. **Facts known:** Strong varied physiology evidence is followed by one integrative miss with unusually high reading load.
2. **Tempting unjustified inference:** The learner lost the concept or has low ability.
3. **Candidate actions:** Inspect item validity/language load; comparable integrative task; broad review; continue.
4. **Allowed:** Keep strong history and use another valid measure before a strong state change if construct-irrelevant load is plausible.
5. **Must not:** Reset the claim or infer ability from an outlier.
6. **Learner-facing reason:** “That was one unusually complex question. I’ll check the same idea another way before changing the recommendation.”
7. **Internal reason:** Outlier plus possible construct-irrelevant variance.
8. **What changes it:** Repeated valid integrative misses or evidence the extra reading load is intentionally part of the construct.

## K29 — Biology/health science — stale recommendation after source change
1. **Facts known:** A task is recommended under Source V1; before opening, Source V2 changes the approved answer.
2. **Tempting unjustified inference:** A recommendation valid at issue time remains safe to deliver unchanged.
3. **Candidate actions:** Deliver cached V1; revalidate/replace; block; silently continue.
4. **Allowed:** Revalidate authority/mapping/policy at delivery and expire/recompute if materially stale.
5. **Must not:** Deliver obsolete answer-bearing content or score under superseded authority.
6. **Learner-facing reason:** “This activity changed since it was recommended, so I’ve refreshed it to the current version.”
7. **Internal reason:** Issue-time validity and delivery-time execution authority are distinct.
8. **What changes it:** Impact review showing the revision does not affect the action.

## K30 — Biology/health science — protected assessment with accommodation
1. **Facts known:** Summative exam disables tutoring; learner has approved keyboard/text-size/extended-time accommodation.
2. **Tempting unjustified inference:** Exam mode means disable every support feature.
3. **Candidate actions:** Authorised access supports; tutor explanation; normal exam progression; exit.
4. **Allowed:** Keep authorised accommodations while disabling prohibited answer-bearing coaching.
5. **Must not:** Conflate accessibility with tutoring, penalise extended time or expose an explanation.
6. **Learner-facing reason:** “Your approved access settings remain on. Answer guidance isn’t available during this assessment.”
7. **Internal reason:** Stakes/assistance/accessibility are independent policy dimensions.
8. **What changes it:** Authorised post-submission feedback phase or policy change.

## K31 — Biology/health science — imminent assessment with no evidence
1. **Facts known:** Exam is tomorrow; syllabus scope is known; learner has never used StudyGrid for this unit and no prerequisite evidence exists.
2. **Tempting unjustified inference:** Urgency means target the “weakest” prerequisite despite no weakness evidence.
3. **Candidate actions:** Exam-scope overview; bounded diagnostic; first lesson; ask learner priority.
4. **Allowed:** Use real deadline/scope to choose context, then a bounded approved review/diagnostic without inventing weakness.
5. **Must not:** Create retention risk, prerequisite weakness or personalised certainty from zero evidence.
6. **Learner-facing reason:** “The exam is tomorrow, but I don’t have learning evidence for this unit yet. Let’s start with a quick approved check of the exam topics.”
7. **Internal reason:** Real urgency may select scope; it cannot manufacture learner state.
8. **What changes it:** Diagnostic results or explicit learner priorities.

## K32 — Reading/writing/humanities — multiple defensible interpretations
1. **Facts known:** Literature response supports two defensible theses; rubric rewards textual evidence/reasoning rather than a single thesis. Learner chooses B.
2. **Tempting unjustified inference:** Different from model answer means wrong.
3. **Candidate actions:** Rubric/human review; accept B if supported; force A; remediation.
4. **Allowed:** Score against criteria and preserve legitimate alternate interpretations.
5. **Must not:** Treat noncanonical thesis as misconception or collapse open-ended work to one generated exemplar.
6. **Learner-facing reason:** “Your interpretation can be valid if the evidence and reasoning support it; I’m evaluating those criteria.”
7. **Internal reason:** Open construct; validity is criterion-based, not key-match.
8. **What changes it:** Rubric failure, unsupported evidence or instructor narrowing of acceptable interpretations.

## K33 — Reading/writing/humanities — language load confounds target construct
1. **Facts known:** Target is argument structure; prompt uses dense archaic language. Organisation is strong when prompt is paraphrased with approved support.
2. **Tempting unjustified inference:** Initial miss proves weak argument structure.
3. **Candidate actions:** Argument remediation; alternate valid prompt; language support; fresh argument task.
4. **Allowed:** Flag construct-irrelevant language load and use another task/modality before making a strong argument-structure claim.
5. **Must not:** Infer intelligence, disability, language trait or low argument competence from the confounded item.
6. **Learner-facing reason:** “That prompt added extra language difficulty, so I’ll check the argument skill with a clearer task.”
7. **Internal reason:** `VALIDITY_CONFOUND`; evidence is low-quality for the intended claim.
8. **What changes it:** Repeated failures on valid accessible prompts.

## K34 — Reading/writing/humanities — late rubric/mapping correction
1. **Facts known:** Essay initially maps to Claims A+B. Review finds rubric only isolates A; B mapping is removed after submission.
2. **Tempting unjustified inference:** Keep B evidence because history is immutable, or move it automatically to some other claim.
3. **Candidate actions:** Preserve response; invalidate B interpretation; recompute profile; rewrite attempt.
4. **Allowed:** Preserve response history, revise mapping/effective interpretation and remove B from current evidence.
5. **Must not:** Double-count A+B, mutate response or silently move competence.
6. **Learner-facing reason:** “The grading map for that essay was corrected. Your response stays the same; only what it can support has changed.”
7. **Internal reason:** Mapping revision with explicit retrospective applicability.
8. **What changes it:** Human review establishing a valid B criterion could restore B evidence.

## K35 — Reading/writing/humanities — self-directed text outside sequence
1. **Facts known:** Learner selects a later approved novel for analysis; no hard curricular gate applies.
2. **Tempting unjustified inference:** Off-sequence choice means avoidance/disengagement.
3. **Candidate actions:** Selected text analysis; current-sequence reading; prerequisite background; refuse.
4. **Allowed:** Use learner-selected text as scope and recommend an eligible analysis action.
5. **Must not:** Penalise motivation/engagement, block on sequence alone or surface override as instructor risk.
6. **Learner-facing reason:** “You chose this text, so we’ll work with it now.”
7. **Internal reason:** Learner-declared scope is context, not a trait.
8. **What changes it:** Release restriction, missing approved source or explicit course requirement.

## K36 — Reading/writing/humanities — nudge fatigue after dismissal
1. **Facts known:** Learner dismisses “Want an example?” and succeeds on the next item; old error trigger still exists.
2. **Tempting unjustified inference:** Trigger still true, so repeat nudge until accepted.
3. **Candidate actions:** Repeat nudge; suppress for episode; normal next task; passive help link.
4. **Allowed:** Suppress unsolicited repeat while preserving help on request.
5. **Must not:** Nag, infer resistance/low motivation or count acceptance/dismissal as mastery evidence.
6. **Learner-facing reason:** “We’ll keep going. Help is available whenever you ask for it.”
7. **Internal reason:** Episode nudge budget/cooldown is part of policy.
8. **What changes it:** Explicit help request, new episode or materially different struggle pattern.

## K37 — Cross-domain — prior recommendation becomes self-confirming evidence
1. **Facts known:** A tentative prerequisite hypothesis causes the engine to serve only tasks targeting that prerequisite; learner misses two of those policy-selected tasks.
2. **Tempting unjustified inference:** Subsequent misses prove the original recommendation/hypothesis was correct.
3. **Candidate actions:** Strengthen hypothesis; disconfirming probe; inspect item quality; change scope.
4. **Allowed:** Record selection context, keep hypothesis separate from evidence and use an independent/disconfirming path before escalating confidence.
5. **Must not:** Treat prior recommendation as evidence, claim causal validation or lock into endless remediation.
6. **Learner-facing reason:** “I’ve been focusing on one possible gap. Let’s check it another way before deciding that’s the main issue.”
7. **Internal reason:** `POLICY_SELECTION_BIAS`; the observation process is endogenous.
8. **What changes it:** Independent evidence from another valid family or authorised instructor review.

## K38 — Cross-domain — personal provisional notes versus course-approved source
1. **Facts known:** Learner’s private notes conflict with course handout. Learner wants to study privately from the notes; notes are not approved course authority.
2. **Tempting unjustified inference:** Unapproved means unusable anywhere, or personal notes may silently replace course truth.
3. **Candidate actions:** Clearly labelled personal/provisional study; course-approved instruction; block notes; merge invisibly.
4. **Allowed:** Permit labelled provisional personal study where policy allows while preventing those notes from silently supporting consequential course claims/graded scoring.
5. **Must not:** Promote notes to canonical truth, erase them solely for lack of approval or invisibly mix authorities.
6. **Learner-facing reason:** “We can use your notes for personal study, but they aren’t the approved course source for graded claims.”
7. **Internal reason:** Authority scope separates personal provisional from course-approved; approval and validity are distinct.
8. **What changes it:** Instructor approval, source correction or switch back to course mode.
