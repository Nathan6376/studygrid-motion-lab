# StudyGrid website prototype — compact cross-domain acceptance fixtures

From: StudyGrid Worker Kevin  
To: ChatGPT General CF-0047  
Date: 2026-10-01  
Status: WEBSITE-FACING ACCEPTANCE DESIGN ONLY — NO IMPLEMENTATION

## Basis
This set is a compact projection of Kevin's completed 38-scenario cross-domain behaviour attack, reconciled against General's Engine v1 Draft 2 design basis and the next website-prototype build-contract preparation.

Authority consumed:
- route: `routes/GENERAL_20261001_2049_KEVIN_WEBSITE_CROSS_DOMAIN_ACCEPTANCE.txt` @ `c0612110bbc268dca261e9f4eb3b2fd62cfec349`
- Kevin cross-domain return @ `7f5926287f17310b6b3e54b87cc69f9ef1d807bc`
- Draft 2 General reconciliation @ `b6ac02d321293a46002636f6e6286e1f067e9ea8`
- website build-contract prep @ `6be928678f784e968f3ecca3017d6da39fca9c84`

These are mock website states. They do not prescribe storage, APIs, scoring engines or backend implementation.

## Smallest high-value set: 10 fixtures

| Fixture | Domain / source scenario | Primary website risk proved |
|---|---|---|
| W01 | Law/policy · K01 | cold start is not weakness |
| W02 | Law/policy · K02 | recognition and application stay distinct |
| W03 | Biology/health science · K30 + K05 | protected assessment blocks coaching but preserves accommodation |
| W04 | Engineering · K11 | multi-claim task does not smear one error across every skill |
| W05 | Mathematics · K03/K22 | answer-exposed repeats are practice, not fresh proof |
| W06 | Mathematics · K19 | explicit help works in low-stakes practice without shame |
| W07 | Mathematics + General Study · K20 + K08/K35 | reject recommendation + self-directed escape without trait inference |
| W08 | Mathematics · K18 | no valid action renders honestly; no bogus fallback |
| W09 | Biology/health science · K29 | stale recommendation refreshes before delivery |
| W10 | Reading/writing/humanities · K32 | constructed response allows defensible alternate interpretations |

---

## W01 — Law/policy cold start
**Learner/course context:** New learner opens a policy-law unit. Current course source and first approved lesson are known; there is no learner evidence yet.

**Mock engine output/state needed:** `UNMEASURED`; recommended operation = approved introduction. Optional bounded diagnostic may exist as a secondary route if the package allows it.

**Primary visible action:** **Start the unit**.

**Learner-facing reason:** “I don't have learning evidence for this topic yet, so we'll start with the approved introduction.”

**Allowed alternate / escape:** “Quick check” when explicitly supported; “Choose another topic.”

**Must not appear:** “You're weak here,” “Behind,” “0% mastered,” “Needs remediation,” invented retention/urgency.

**Interaction type:** lesson/instruction; optional `single_select` diagnostic.

---

## W02 — Law/policy recognition succeeds, application fails
**Learner/course context:** Learner correctly identifies a rule in fresh recognition questions, then struggles to apply it to a new fact pattern.

**Mock engine output/state needed:** recognition = valid demonstrated evidence under recognition conditions; application = `OBSERVED_INSUFFICIENT`; reason flag = channel divergence/non-comparability, not one averaged score.

**Primary visible action:** **Work through an application example**.

**Learner-facing reason:** “You're recognising the rule correctly. Let's practise applying it to a new scenario.”

**Allowed alternate / escape:** “Try a fresh scenario”; “Keep going.”

**Must not appear:** “50% mastered,” “You both know and don't know this,” “You forgot the rule,” a single red/green mastery meter collapsing both channels.

**Interaction type:** scenario application; `short_text/constructed_response` or course-approved scenario interaction.

---

## W03 — Protected biology assessment with accommodation and help request
**Learner/course context:** Learner is inside a protected anatomy/health-science quiz, has approved keyboard/text-size/extended-time support, and asks for a hint.

**Mock engine output/state needed:** protected assessment active; answer-bearing coaching unavailable; authorised accessibility/accommodation remains active.

**Primary visible action:** **Continue assessment**.

**Learner-facing reason:** “Answer guidance isn't available during this assessment. Your approved access settings are still available.”

**Allowed alternate / escape:** approved assessment instructions; submit/exit according to assessment rules.

**Must not appear:** worked example, hint revealing the answer, cached coaching from practice, “All support is disabled,” “You needed help so this topic is weak,” latency-based judgement.

**Interaction type:** any protected question; use `multi_select_unordered` here if that control is part of the candidate so the protected-state behaviour is tested on a non-single-select interaction.

---

## W04 — Engineering multi-claim problem
**Learner/course context:** One circuit problem uses algebra, units and circuit-model selection. Rubric evidence shows algebra and units are correct; circuit-model choice is the isolated error.

**Mock engine output/state needed:** algebra = valid current evidence; units = valid current evidence; circuit-model claim = `OBSERVED_INSUFFICIENT` / targeted gap. No whole-problem learner diagnosis.

**Primary visible action:** **Review a circuit-model example**.

**Learner-facing reason:** “Your algebra and units were fine. The part to revisit is choosing the circuit model.”

**Allowed alternate / escape:** “Try another circuit problem”; “Keep going.”

**Must not appear:** “Three weak skills,” “You failed algebra,” “Whole topic not learned,” a single wrong final-answer state that paints every mapped skill red.

**Interaction type:** `numeric/formula` plus criterion-level feedback.

---

## W05 — Mathematics answer-exposed repeat success
**Learner/course context:** Learner sees a worked solution, then answers several near-identical equations correctly in the same episode.

**Mock engine output/state needed:** supported practice success; reason flag = dependent repeat / answer exposed; transfer evidence still insufficient.

**Primary visible action:** **Try a fresh problem**.

**Learner-facing reason:** “Those were good practice after the example. A fresh problem will tell us more.”

**Allowed alternate / escape:** “Keep practising this pattern”; “Review the example again.”

**Must not appear:** “Mastered,” “Retained,” “100% learned,” “4 correct = proven,” confetti/progress language implying independent fresh evidence.

**Interaction type:** `numeric/formula`.

---

## W06 — Mathematics explicit help request in low-stakes practice
**Learner/course context:** During ordinary practice, learner asks for help before committing an answer.

**Mock engine output/state needed:** explicit help request; help permitted; next response will be supported/coached practice rather than unaided evidence.

**Primary visible action:** **Show a worked example**.

**Learner-facing reason:** “You asked for help, so here's an example. Your next answer will count as supported practice.”

**Allowed alternate / escape:** “Break it down”; “Keep going without the example.”

**Must not appear:** “You're struggling,” “Low confidence,” “Needs remediation,” motivation/ability labels, or later UI copy calling the supported response “unaided.”

**Interaction type:** whatever practice item was open; test that the help surface does not move/replace the primary input unexpectedly.

---

## W07 — Reject recommendation and switch to General Study
**Learner/course context:** Course Home recommends fraction review. Learner selects “Not now” and chooses a self-directed algebra topic in General Study.

**Mock engine output/state needed:** recommendation dismissed/overridden; new selected context = General Study / algebra; override affects next action only, not competence/motivation state.

**Primary visible action:** **Start algebra practice**.

**Learner-facing reason:** “You chose algebra, so we'll work on that now.”

**Allowed alternate / escape:** “Return to course recommendation”; “Browse General Study topics”; pause.

**Must not appear:** “Disengaged,” “Avoiding fractions,” lower fraction mastery because of the dismissal, an immediate fraction nudge on the next screen, or General Study work silently presented as course-approved graded evidence.

**Interaction type:** context/topic selection followed by a normal supported practice interaction.

---

## W08 — Mathematics no valid next action
**Learner/course context:** Current target requires an approved interaction the prototype cannot presently render accessibly, and no equivalent approved activity exists.

**Mock engine output/state needed:** `NO_ELIGIBLE_ACTION` / `UNSUPPORTED`; capability/access gap belongs to the product/content state, not the learner.

**Primary visible action:** **Choose another activity**.

**Learner-facing reason:** “I don't have an approved accessible activity for this topic right now.”

**Allowed alternate / escape:** “Switch topic”; “Pause and come back later.”

**Must not appear:** silent substitution to ordinary MCQ, “Completed,” “Mastered,” “You got this wrong,” or a dead-end disabled page with no escape.

**Interaction type:** use a deliberately unsupported/withheld `hotspot/diagram` fixture or equivalent capability-gated task; do not fake support.

---

## W09 — Biology recommendation becomes stale after source change
**Learner/course context:** A biology task is recommended under Source V1; before learner opens it, Source V2 changes the approved answer/teaching point.

**Mock engine output/state needed:** previous recommendation = stale; current valid replacement/refreshed activity available.

**Primary visible action:** **Open refreshed activity**.

**Learner-facing reason:** “This activity changed since it was recommended, so I've refreshed it to the current version.”

**Allowed alternate / escape:** “Review what changed”; “Choose another topic.”

**Must not appear:** cached V1 answer/explanation, scoring against superseded content, a claim that the learner regressed because the source changed.

**Interaction type:** `categorize`, `single_select` or another biology-appropriate task; the acceptance target is stale-state replacement, not the specific control.

---

## W10 — Humanities constructed response with more than one defensible interpretation
**Learner/course context:** Literature response supports a defensible thesis different from the example answer. Rubric evaluates textual evidence and reasoning rather than one required thesis.

**Mock engine output/state needed:** response evaluated by rubric criteria; alternate interpretation accepted when criteria are met. If human review is required, show `REVIEW_REQUIRED` rather than wrong.

**Primary visible action:** **Review feedback** / **Continue** when criteria are satisfied.

**Learner-facing reason:** “Your interpretation can be valid when the evidence and reasoning support it. Here's how your response met the rubric.”

**Allowed alternate / escape:** “Revise response”; “See the rubric”; “Try another passage.”

**Must not appear:** “Different from the model answer = wrong,” “Misconception,” a single exact-answer comparison, or AI certainty presented as course truth.

**Interaction type:** `short_text/constructed_response`.

---

## Cross-fixture visible acceptance rules
A prototype passes this set only if the visible behaviour consistently does all of the following:

1. Shows one primary next action and a short reason without presenting the recommendation as a mastery verdict.
2. Provides a graceful alternate/escape whenever policy permits.
3. Keeps cold start, missing evidence, unsupported capability, invalid/stale content and learner error visually/semantically distinct.
4. Never turns help, dismissal, latency, accommodation or self-directed choice into motivation/ability/engagement evidence.
5. Keeps protected-assessment coaching suppression separate from accessibility support.
6. Does not present answer-exposed/correlated repeats as fresh transfer or retention proof.
7. Can display targeted component evidence without smearing a multi-claim task across unrelated skills.
8. Revalidates stale recommendations before showing answer-bearing content.
9. Makes General Study clearly distinct from course-approved consequential work.
10. Uses interaction types appropriate to the construct and refuses unsupported fallback rather than silently changing the task.

## Coverage check against General route
All routed minimums are covered by the ten fixtures:
- five required domains: W01/W02, W04, W05–W08, W03/W09, W10;
- cold start: W01;
- recognition success + application failure: W02;
- answer-exposed repeat success: W05;
- explicit help request: W06 (allowed) and W03 (correctly suppressed under protected policy);
- learner rejects recommendation: W07;
- protected assessment: W03;
- accessibility/accommodation: W03;
- no valid next action: W08;
- stale recommendation after source/context change: W09;
- multi-claim task: W04;
- self-directed/general-study path: W07.

No software PASS is claimed here. These are website-facing fixture expectations for Bob/Stuart to apply to the exact candidate they review/build.
