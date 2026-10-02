# Kevin Engine v1 cross-domain scenario attack — scenarios K01–K20

Independent behaviour/design QA for General CF-0047. No implementation. Each scenario states only synthetic facts supplied by the fixture; no scenario is evidence about a real learner.

## K01 — Law/policy — cold start, no learner evidence
1. **Facts known:** Current course package/source and first required claim are known. No learner attempts, support events or declared prior knowledge exist.
2. **Tempting unjustified inference:** “The learner is weak” or “needs remediation.”
3. **Candidate actions:** Approved introduction; bounded cold-start probe if package policy explicitly permits probe-first; eligible learner-selected topic; pause.
4. **Allowed:** Introduce the unit, or use one bounded diagnostic only under an explicit author-time probe-first rule.
5. **Must not:** Mark weakness, create a misconception, estimate retention, or force remediation from absence.
6. **Learner-facing reason:** “I don’t have enough evidence about this yet, so we’ll start with the unit introduction.”
7. **Internal reason:** `UNMEASURED`; no negative evidence exists.
8. **What changes it:** A valid attempt, explicit learner goal, approved imported evidence or package-policy change.

## K02 — Law/policy — recognition succeeds, application fails
1. **Facts known:** Three fresh recognition items are correct; one valid novel fact-pattern application is weak under an application rubric.
2. **Tempting unjustified inference:** “The learner simultaneously knows and does not know the same thing,” or average to one medium score.
3. **Candidate actions:** Application worked example; fresh application probe; recognition review; advance.
4. **Allowed:** Keep recognition and application as separate channels and prefer application-focused work if the course requires application.
5. **Must not:** Collapse channels to one scalar, erase recognition success, or call channel divergence a logical contradiction by default.
6. **Learner-facing reason:** “You’re recognising the rule correctly. Let’s practise applying it to a new scenario.”
7. **Internal reason:** `CHANNEL_DIVERGENCE`; each contract has different conditions.
8. **What changes it:** Independent application evidence, rubric correction or invalidation of the novel prompt.

## K03 — Law/policy — repeated correct answers after answer exposure
1. **Facts known:** The governing test was revealed in feedback; four near-identical variants are then answered correctly in the same episode.
2. **Tempting unjustified inference:** Four independent demonstrations and durable retention.
3. **Candidate actions:** Fresh materially different application; normal progression; immediate fifth variant; retention review.
4. **Allowed:** Credit supported practice and move to a genuinely fresh task or normal progression under package policy.
5. **Must not:** Count variants as independent sufficiency units, relabel them unaided, or infer retention.
6. **Learner-facing reason:** “Those were good practice after the explanation. A fresh problem will tell us more.”
7. **Internal reason:** `ANSWER_EXPOSED` plus correlated task family; support lineage matters across attempts.
8. **What changes it:** Delayed unaided performance on an independently authored family.

## K04 — Law/policy — authority supersession without global learner regression
1. **Facts known:** The learner performed well under Policy Version A. Version B changes one rule while unrelated material remains unchanged.
2. **Tempting unjustified inference:** Old success is now “wrong,” so the learner became weak across the topic.
3. **Candidate actions:** Teach changed rule; review only affected tasks/mappings; preserve unaffected evidence; wipe topic state.
4. **Allowed:** Quarantine/reinterpret only dependencies affected by the changed proposition and present the new rule as current content.
5. **Must not:** Rewrite old attempts, globally lower competence, or keep Version-A content as current authority.
6. **Learner-facing reason:** “This rule changed in the current course material, so we’ll update just that part.”
7. **Internal reason:** `SOURCE_SUPERSESSION` with bounded semantic impact; old history remains historical.
8. **What changes it:** A semantic-impact review showing the revision was cosmetic, or new Version-B performance.

## K05 — Law/policy — protected exam plus explicit help request
1. **Facts known:** A protected graded quiz is active. The learner requests an explanation. Answer-bearing coaching is forbidden; authorised accessibility support remains permitted.
2. **Tempting unjustified inference:** A help request always deserves tutoring, or every kind of support must be disabled.
3. **Candidate actions:** Tutor explanation; approved non-answer-bearing instructions; authorised accessibility; exit/submit under exam rules.
4. **Allowed:** Follow the protected blueprint while preserving authorised accessibility.
5. **Must not:** Reveal answer guidance, infer weakness from the request, or disable accommodations as if they were tutoring.
6. **Learner-facing reason:** “I can’t give answer guidance during this assessment, but the approved assessment support is still available.”
7. **Internal reason:** Assessment-integrity constraint dominates tutoring; accessibility is an independent policy dimension.
8. **What changes it:** Leaving protected assessment, moving to practice, or an authorised policy change.

## K06 — Law/policy — imminent assessment versus weak prerequisite
1. **Facts known:** Exam on B is tomorrow. Valid evidence shows a modest A prerequisite gap. Learner explicitly chooses B review; both B and A actions are available.
2. **Tempting unjustified inference:** Prerequisite weakness must always dominate, or deadline must always dominate.
3. **Candidate actions:** Targeted A repair; B review; bounded B probe; learner-selected B practice.
4. **Allowed:** Apply an explicit precedence rule; normally honour eligible B scope while surfacing A repair unless A is a real hard prerequisite.
5. **Must not:** Trap learner in A, claim A caused all B difficulty, or silently override learner solely because the exam is near.
6. **Learner-facing reason:** “You chose exam review. We can start there; there’s also one prerequisite skill worth repairing if you want it.”
7. **Internal reason:** Multiple valid factors require named branch precedence, not a hidden weighted score.
8. **What changes it:** A hard prerequisite policy, B evidence attributable specifically to A, or learner goal change.

## K07 — Law/policy — scorer disagreement and late regrade
1. **Facts known:** Same written response receives AI rubric 2/4, then authorised human regrade 4/4 with the AI result superseded.
2. **Tempting unjustified inference:** Average to 3/4, or keep first result forever because the attempt is immutable.
3. **Candidate actions:** Pending review; current human-reviewed score; remediation from AI score; advance from effective score.
4. **Allowed:** Keep response immutable, append score revisions and use one authorised effective score lineage.
5. **Must not:** Double-count scores, average them by default, or treat regrade as a second learner performance.
6. **Learner-facing reason:** “Your response was regraded. I’m using the current reviewed score.”
7. **Internal reason:** `SCORER_DISAGREEMENT` resolved by score-result authority/lineage, not by mutating the response.
8. **What changes it:** Another authorised appeal, rubric revision or scorer-precedence decision.

## K08 — Law/policy — self-directed topic outside course sequence
1. **Facts known:** Learner in Unit 3 selects an eligible Unit 6 doctrine early. No hard lock applies and sources are available.
2. **Tempting unjustified inference:** Out-of-sequence means “not ready” or “avoidance.”
3. **Candidate actions:** Unit 6 introduction; Unit 3 next task; relevant prerequisite probe; refuse access.
4. **Allowed:** Choose the learner-requested Unit 6 action if policy permits; sequence is fallback, not competence evidence.
5. **Must not:** Infer disengagement, fabricate prerequisite weakness, or block only because authored order differs.
6. **Learner-facing reason:** “You chose Unit 6, so we’ll start with an approved introduction there.”
7. **Internal reason:** Learner intent is context, not evidence.
8. **What changes it:** Real hard prerequisite, unavailable source, protected release rule or learner goal change.

## K09 — Engineering — one hard miss after strong history
1. **Facts known:** Six strong independent performances across varied circuit-analysis families, then one unusually hard novel miss.
2. **Tempting unjustified inference:** The learner “lost” the skill or needs broad remediation.
3. **Candidate actions:** Inspect miss; comparable novel probe; local help if attributable; broad remediation; continue.
4. **Allowed:** Preserve strong history and use a bounded probe/local repair only if the error can be isolated.
5. **Must not:** Reset the claim, infer forgetting from one miss, or launch an automatic broad remediation loop.
6. **Learner-facing reason:** “That was one difficult miss after several strong results. Let’s check whether it was a one-off or a specific gap.”
7. **Internal reason:** One result should not silently invalidate a stronger valid evidence history.
8. **What changes it:** Repeated comparable misses, component-level evidence, or discovery that earlier tasks were not independent.

## K10 — Engineering — repeated comparable unit-conversion errors
1. **Facts known:** Across three independent problems, equation setup is correct but the same unit-conversion error recurs; rubric isolates units from domain reasoning.
2. **Tempting unjustified inference:** The learner does not understand the whole engineering concept.
3. **Candidate actions:** Unit mini-example; full-topic reteach; isolated unit probe; advance.
4. **Allowed:** Offer one targeted unit-conversion action because the repeated error is comparable and component-attributable.
5. **Must not:** Lower unrelated claims, store a broad misconception as fact, or repeat the same repair indefinitely.
6. **Learner-facing reason:** “Your setup is consistent. The repeated issue is unit conversion, so we’ll focus just on that.”
7. **Internal reason:** `REPEATED_COMPONENT_ERROR`; bounded repair budget applies.
8. **What changes it:** Disconfirming unit probe, rubric correction or a shared item-format defect.

## K11 — Engineering — multi-part problem covering several skills
1. **Facts known:** One design problem requires algebra, units and circuit reasoning. Final answer is wrong; rubric says algebra correct, units correct, circuit-model choice wrong.
2. **Tempting unjustified inference:** Wrong final answer means failure on all mapped claims.
3. **Candidate actions:** Circuit-model explanation; algebra review; unit review; another joint task.
4. **Allowed:** Use criterion-level evidence and target the isolated circuit-model component.
5. **Must not:** Penalise algebra/units or manufacture three independent failures from an undifferentiated outcome.
6. **Learner-facing reason:** “Your algebra and units were fine. The part to revisit is choosing the circuit model.”
7. **Internal reason:** `MULTI_CLAIM_COMPONENT`; per-claim updates require rubric isolation.
8. **What changes it:** If the rubric cannot isolate components, evidence must remain joint/diagnostic and the next action more cautious.

## K12 — Engineering — prerequisite unknown versus genuinely weak
1. **Facts known:** Prerequisite A has no logged evidence because prior study was offline. B has not yet been attempted.
2. **Tempting unjustified inference:** Unknown A means weak A, so block B.
3. **Candidate actions:** A probe; A review; B introduction; ask learner; block.
4. **Allowed:** Treat A as unknown; offer a bounded probe or proceed if policy and learner intent permit.
5. **Must not:** Create weakness, hard-block from missing telemetry, or equate offline absence with non-learning.
6. **Learner-facing reason:** “I don’t have evidence for that prerequisite yet. We can check it quickly or continue if the course allows.”
7. **Internal reason:** `UNMEASURED_PREREQUISITE`; missing is not failed.
8. **What changes it:** Valid A evidence or an explicit course hard prerequisite.

## K13 — Engineering — soft prerequisite cycle
1. **Facts known:** Two soft/hypothesised edges say A may support B and B may support A. Neither is an approved hard prerequisite.
2. **Tempting unjustified inference:** Neither topic can be studied until the other is mastered.
3. **Candidate actions:** Probe/introduce A; probe/introduce B; quarantine cycle; block both.
4. **Allowed:** Quarantine/ignore the soft cycle for blocking and use package order or learner choice.
5. **Must not:** Trap the learner or turn a graph defect into learner weakness.
6. **Learner-facing reason:** “The course map has an uncertain dependency here, so it won’t block you from continuing.”
7. **Internal reason:** `GRAPH_CYCLE` in non-authoritative readiness relations.
8. **What changes it:** Instructor-approved directed hard prerequisite or valid evidence that changes preference.

## K14 — Engineering — offline attempt syncs with wrong device clock
1. **Facts known:** Offline work has a device timestamp two days fast; it syncs after a later online task and receives trustworthy server receipt/sequence only then.
2. **Tempting unjustified inference:** Client timestamp proves the offline task was later and therefore delayed retention evidence.
3. **Candidate actions:** Use client time; use server order; mark chronology uncertain; ignore response.
4. **Allowed:** Preserve client metadata but restrict recency/delay claims when chronology is untrusted; retain usable response content where valid.
5. **Must not:** Infer forgetting/delayed recall from bad clock data or discard valid evidence solely because time is uncertain.
6. **Learner-facing reason:** “I saved this work, but its timing is uncertain, so I won’t use it as proof of delayed recall.”
7. **Internal reason:** `CLOCK_PROVENANCE_UNCERTAIN`; evidence content and chronology validity are separable.
8. **What changes it:** Trusted timing metadata or authorised confirmation of occurrence order.

## K15 — Engineering — accommodation/support present
1. **Facts known:** Approved extended time and keyboard navigation are used. Answers are accurate but slower than cohort; no answer-bearing hint is given.
2. **Tempting unjustified inference:** Slow means weak, accommodation means coached, or graded work should disable access support.
3. **Candidate actions:** Normal next action; remediation; speed drill; preserve accommodation.
4. **Allowed:** Interpret performance under construct-valid accommodation and continue according to evidence.
5. **Must not:** Penalise latency, infer disability/ability traits, or downgrade evidence solely because approved access support was used.
6. **Learner-facing reason:** “Your answer is evaluated under the approved support settings; response speed isn’t being treated as a knowledge score.”
7. **Internal reason:** Purpose-limited accommodation context; timing is confounded.
8. **What changes it:** Only a validated construct where timing itself matters under the authorised accommodation policy.

## K16 — Engineering — two valid next actions tied
1. **Facts known:** Two approved tasks target the same unmet contract with equal authored priority and equivalent policy fit.
2. **Tempting unjustified inference:** One must be objectively better, so create an opaque utility score.
3. **Candidate actions:** E17; E18; ask learner; stable deterministic tie-break.
4. **Allowed:** Use a declared stable tie-break and record that options were tied under current rules.
5. **Must not:** Invent causal superiority or explain the tie-break as stronger learning evidence.
6. **Learner-facing reason:** “Both are good fits. I’m starting with this one because it comes first in the course set.”
7. **Internal reason:** `TIE_WITHIN_BRANCH`; tie-breaking is policy mechanics, not pedagogy evidence.
8. **What changes it:** Learner preference, accessibility fit, recency or author priority.

## K17 — Mathematics — invalid/broken question
1. **Facts known:** A quadratic item has no correct option because of an authoring error and is later flagged invalid.
2. **Tempting unjustified inference:** Every wrong selection indicates learner weakness or class weakness.
3. **Candidate actions:** Remediate; exclude item; route to content review; valid replacement.
4. **Allowed:** Mark evidence invalid, remove it from current inference and use a valid replacement where appropriate.
5. **Must not:** Create negative learner evidence, trigger remediation or diagnose a cohort bottleneck.
6. **Learner-facing reason:** “That question had a problem, so it won’t count against your learning record.”
7. **Internal reason:** `INVALID_ITEM`; content-quality path, not learner path.
8. **What changes it:** Corrected validated item plus a fresh response.

## K18 — Mathematics — no valid next action exists
1. **Facts known:** Required construct needs an interaction the current client cannot render accessibly; no approved equivalent task/resource exists.
2. **Tempting unjustified inference:** Fall back to ordinary MCQ, choose least-bad unsupported content, or claim completion.
3. **Candidate actions:** Unsupported fallback; pause; switch eligible topic; honest unavailable state.
4. **Allowed:** Return `NO_ELIGIBLE_ACTION`/`UNSUPPORTED` with an escape such as switch topic or pause.
5. **Must not:** Silently substitute MCQ, claim completion/mastery or blame learner for a product capability gap.
6. **Learner-facing reason:** “I don’t have an approved accessible activity for this topic right now. You can switch topics or come back later.”
7. **Internal reason:** All candidates excluded by capability/accessibility contract.
8. **What changes it:** Approved accessible content or learner scope change.

## K19 — Mathematics — explicit help request in low-stakes practice
1. **Facts known:** Learner requests a worked example before committing an answer; practice policy permits help.
2. **Tempting unjustified inference:** Help request proves weakness, or help must always be withheld to preserve evidence.
3. **Candidate actions:** Worked example; hint; continue; diagnostic probe.
4. **Allowed:** Provide approved requested help and mark subsequent relevant performance as supported/coached.
5. **Must not:** Lower mastery because help was requested, call the next answer unaided or force a diagnostic first.
6. **Learner-facing reason:** “Here’s an example. Your next answer will count as supported practice, not an unaided check.”
7. **Internal reason:** `EXPLICIT_HELP_REQUEST` changes action and exposure lineage, not learner trait state.
8. **What changes it:** Protected assessment state or learner cancellation.

## K20 — Mathematics — learner rejects recommendation
1. **Facts known:** Engine recommends fraction review; learner selects “Not now” and chooses an eligible algebra topic.
2. **Tempting unjustified inference:** Disengagement, aversion or lower fraction mastery.
3. **Candidate actions:** Respect algebra; repeat fraction nudge immediately; record override as learner-state evidence.
4. **Allowed:** Respect eligible override, record decision history and suppress immediate regeneration of the same unsolicited recommendation.
5. **Must not:** Change mastery/motivation, label disengagement or nag on refresh.
6. **Learner-facing reason:** “Okay — we’ll work on algebra instead.”
7. **Internal reason:** Override affects agency/anti-repetition history only.
8. **What changes it:** Explicit learner reason, genuine hard obligation or later learner goal change.
