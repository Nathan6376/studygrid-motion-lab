# Current versus requested owner-review matrix

Authority: full 21:13, 21:23 and 21:47 owner packets, Architecture 21:29 and General AMEND 22:09. No design verdict or build authorization is added. Every row is held for owner-batch closure and General's reconciled release. “Local” means technically feasible in the HTML prototype **after release**, not permission now. I=interaction; C=cosmetic; IA=information architecture; S=state model; A=accessibility; D=source data; B=backend dependent.

## 21:13 refinement and preservation

| Requirement | Current source / seam | Class; local feasibility / hold | Stuart downstream acceptance |
|---|---|---|---|
| Preserve liked Professor Home, classes, students/active-class presentation | 3420–3427 and gateway3320–3343 | C/IA/S; local, preserve | Compare released candidate to exact baseline; counts, search/sort, pin/favourite, Today, attention/history stay truthful. |
| Preserve liked returning-user continue concept without instructor leakage | renderPlan2577; global shell2026 | IA/S; role separation local; retirement HOLD Research | Learner continue works; instructor shell has intentional role nav; no accidental learner route. |
| Preserve Paper/Dusk concept | prefs1491; settings2660 | C/I/A; local, device defect unresolved | Both themes readable, usable by pointer/keyboard and persisted. |
| Feedback pill hover/focus geometry | `.report-launch` CSS +tactile3460 | C/A; local once direction released | Rounded compact hover/focus, no rectangular green box; keyboard focus remains visible on both themes. |
| Dusk cannot be pressed | settings2665; tour1750 static spans; modal/report CSS | I/A/S; reproduction prerequisite, local potential fix | Reproduce exact route/input/environment; inspect element hit target/overlay; Paper↔Dusk and reload. Handler presence is not PASS. |
| Edit-only label/colour controls; omit Label: None | course grid3422/binder3425 | I/IA/A; local | Default cards omit selects/redundant empty label; explicit Edit has accessible entry/exit, save/cancel focus and current meaning. |
| Richer restrained course accent/shine/lift | Professor course CSS/card3422 | C/A; local after direction | Readability/contrast; hover and focus parity; reduced motion; colour never sole identifier. |
| Mark resolved undo lower-right/bottom +history | resolve3312/gateway3337;3420/3426 | I/S/A; local fixture command feasible | Exact identity restored once, history not duplicated/mutated; repeated Undo/no-op; stale revision and focus; no backend durability claim. |
| Instructor-only nav/surfaces, intentional exit | global1115–1129;2026;workspace3429;persona3036 | IA/S/A; local UI/demo separation; real roles HOLD B | Instructor never gets learner Study/Your classes/continue by reused shell; role switch explicit; direct URL fallback as contract. |
| Disciplined information density | library3422;source/instructor details | C/IA; local contract only | Useful current data retained; editors disclosed; accepted counts/classes not lost. |
| Preserve gateway/commands and Q-B13 focus fixes; no Slice3 expansion | 3260–3343 and focused wrappers | S/A; local guardrail | Revision/role/error semantics unchanged, keyboard focus repairs retained; no provider/deploy/canonical change. |

## 21:23 school context and contextual Add Class

| Requirement | Current source / seam | Class; local feasibility / hold | Stuart downstream acceptance |
|---|---|---|---|
| Feedback screenshot geometry | same report-launch surface | C/A; local | Same hover/focus check; no separate duplicate fix batch. |
| Course name personal-name autofill | #localClassName name=className autocomplete off3405 | I/A; local semantic/picker repair; device QA needed | Owner-relevant Safari/iPad autofill no name suggestions; keyboard/AT course selection remains usable. |
| Institution+Term too wide/repeated | form3405;local class payload | C/IA/S; profile context local shell | Tablet width/touch targets; established context reused rather than repeated every class. |
| Term1/2/3/4 +Other compact selector | refreshTermSeedOptions1981 currently seasonal strings | IA/S/A; local enum/manual fallback | Four values +Other label; seasonal academic_session separate, optional; edit/re-entry stable. |
| Curated/searchable institutions; manual fallback when unavailable | STATIC_INSTITUTION_SEEDS +alias1974;datalist3403 | IA/D/A; picker shell local; catalogue/source truth HOLD Research | Selection by stable ID; no guessed institutions/programme claims; explicit missing-school fallback. |
| Police Foundations prefix contextual; display207, store PFP207 when official | independent title/code3404/3405 | IA/S/D; display/model shell local; official mapping HOLD | Title+number linked; canonical full code preserved; no implicit prefix for unknown program/course. |
| Official institution/program/term searchable course picker, All courses +manual underneath | HUMBER_COURSE_SEEDS +rank1977;datalists | D/IA/S/A; local fixture shell only after approved source snapshot | Search title/code; term-first without hiding outside-term; verified provenance; unavailable/ambiguous/manual path; selected pair cannot drift. |
| Institution/program/term established once at onboarding/school-year setup; settings editing | firststart2013;state defaults1328;settings2660 | IA/S; local with versioned state shape; sync HOLD B | First-run/context-edit/returning user migration; existing local classes retained; explicit class override only when intended. |
| Join-code shortcut | no current join-code branch or separate field | IA/S/B; local labelled preview shell possible; real resolution HOLD | Code-first path distinct from catalogue identity; invalid/not-found/expired/authorization states must not fabricate enrolment. |
| Official source verification and refresh/versioning/provenance | embedded seeds reference prior supplied catalogue metadata | D/B; HOLD Research+backend ingestion | Do not claim live/current catalogue from existing fixture. Accepted snapshot source/version/last_verified needed; no critical-path scrape. |
| Profile/canonical IDs separate from display labels | localClasses string name/code/institution/term3405 | S/D; local model requires explicit migration contract | institution_id/program_id/course_id separate; raw/manual labels retained; no destructive guesses from aliases. |
| class_section/join_code separate from catalogue course identity | optional section string; no join identity | S/B; architecture-local fixture fields; actual joins HOLD | Same catalogue course can have multiple sections; join targets section; no conflation. |
| Program term vs academic session | current class term seasonal free text | S/IA; local model per Architecture | program_term1–4/OTHER +label; academic_session separately nullable; seasonal text not converted blindly to programme term. |
| Minimal permanent fields, touch/native feel, progressive manual fallback, keyboard accessibility | form/datlist/optional details3405 | C/I/IA/A; shell local after contract; external pattern HOLD Research | Tablet/narrow layout, touch picker, keyboard/AT, no long questionnaire, manual route always available. |

Architecture identifies institution_id, program_id/program_prefix, program_term +other label, optional academic_session, catalogue_course_id +canonical code/display number/source snapshot/version/last_verified and class-section/join distinction. Treat existing strings as legacy/manual data. Its local-shell recommendation does not override current owner hold or source-verification requirement.

## 21:47 welcome, guidance, study, motion, routing and feedback

| # / owner requirement | Current behaviour / exact seam | Class; feasibility / hold | Stuart downstream acceptance |
|---|---|---|---|
| 1 Single Selectric/typeball full-loop control | three static .r6-welcome-path inside .r6-welcome-paths3396 | C/I/A; local CSS/native text shell; final motion HOLD Research/General | One coherent active face; all three meanings stable/available; no competing text, no WebGL dependency by default. |
| 2 Gemini credible motion +independent evidence | supplied Gemini and General AMEND inputs, no baseline rotor | advisory D/A; already received; independent Research HOLD | Do not treat proposed angles/easing/blur as specification; eventual candidate tested Safari/iPad. |
| 3 Centre “Learn the class. Be ready for the test.” | welcome3396 .r6-welcome composition | C; local after direction | Hero remains primary across widths/orientation. |
| 4 Slightly larger liked wordmark, subordinate | global brand/welcome CSS | C/A; local | Logo scale/hierarchy, no goal displacement or overflow. |
| 5 Sign in earlier than tour/start | current Try→tour→sign-in3396 | IA/C/A; local | Visual/DOM/keyboard order coherent; main user goal retained. |
| 6 School context before per-class creation | start2013→courses→form3405 | IA/S; local flow shell; source/joins HOLD | Institution→program→term→code branch→picker/manual, fast return/migration. |
| 7 Few clear routes: I have a class code vs guided setup | first-start choices lack code branch | IA/I/S; local preview, joins HOLD B | Code-first and guided routes unambiguous, no questionnaire sprawl. |
| 8 Normal everyday account with separable owner/admin capability | local persona bar3036;owner workspace2829 | S/IA/B; demo UI boundary local; real auth/capabilities HOLD | Normal learner surface unpolluted; privileged capability deliberate and separately authorized later. No second-account requirement invented. |
| 9 Tour/highlight second press toggles off | phrase/tools opens; highlight class.add1758–1768 | I/A; local | Click/tap/Enter/Space same control twice clears only intended coach/highlight; aria state/focus correct. |
| 10 Fast tour/onboarding, progressive guidance | 6-step learner tour,5 instructor;local coach1990 | IA/I/S; local shell; final heuristic HOLD Research | Useful state quickly; can skip/back/replay, no forced tutorial before value. |
| 11 Introductory continue copy decays, evidence-based trigger | fixed renderPlan2577 copy; no retirement state | S/IA/D; HOLD Research trigger | New/returning/eligible state cases; no arbitrary sign-in count presented as evidence. |
| 12 Compact Continue ·course·topic destination | plan2577 active course +next note;rememberLearnerRoute2022 | IA/S; local after trigger/contract | Accurate safe resume target; stale/deleted class fallback; no instructor leakage. |
| 13 Preserve liked Continue/Browse/notes | 2272/2238/2549 | C/IA; local guardrail | Retain improved hierarchy/content and exact context. |
| 14 Satisfying restrained Mark reviewed response |2245 persists set/rerenders;generic tactile only | C/I/A; local implementation; creative/evidence HOLD | Exact reviewed-state toggle, focus successor, no duplicate progress; reduced motion; no noisy rewards. |
| 15 Deliberate route/page/action transitions | route2116,step1837,direct paints | C/I/A; mechanics local; where/duration/easing HOLD Research | One state commit, no stale focus/scroll, old content inert only during transition, reduced-motion instant path. |
| 16 Calm focus/contextual header evaluate, no assumed redesign | shared nav/rail plus quiz-active class | IA/C/A; pattern HOLD Research/owner | Header only changes per released contract; controls remain reachable, no scroll jump/trapped focus. |
| 17 Intrusive/forced I-beam attribution | annotatable text CSS;native selection;report modes | I/A; source mechanism established, device attribution HOLD QA | Cross-input cursor/selection boundaries; preserved legitimate selection; no body-wide workaround. |
| 18 Annotatable text broad coverage inspection |2242/2385/2560;CSS584–605 | I/A; source audit complete, device checks later | Pointer over text vs gaps/control/rail, tablet native handles, selective styling. |
| 19 Report teardown/capture never stale |1666/1668/2112/2075–2083 | I/S/A; local shared teardown seam feasible | Close/route/Escape/blur/lostcapture/multitouch, immediate reopen/draw, no stale crosshair/touch capture. |
| 20 Full Back/Next/Opencontext/Continue/Profile audit | TRANSITIONS.md +full ledgers | I/IA/S/A; source audit complete; desired destinations General | End-to-end entry from courses/profile/context/deep link; browser history/reload matches displayed state; R01/R02 concrete defects. |
| 21 Feedback capture evidence-driven improvement | structured local form/selection/screenshot/export1591–1696 | IA/I/D/B; existing local mechanics; pattern/privacy HOLD Research, actual delivery HOLD B | Categorisation/context/optional text/confirmation/friction/privacy per approved contract; no false send claim. |
| 22 Beta feedback easy/useful | global entry,modal/mark sequence2048–2087 | I/IA; local refinement after evidence | Complete low-friction intended path and useful context; cancelled flow has no stale state; don't invent conversion results. |

Process items23–27 are satisfied as scope constraints: no Bob/Stuart/Kevin activation; Research/architecture remain distinct; no extra Gemini task; no Claude dependence/wake; technical preparation returned to General. No implementation or owner closure follows from this table.

## General's Gemini AMEND constraints (non-final)

The implied single-object/native-text/CSS3D direction is provisional. Final compound geometry, shortest path, damped settle, optional blur, dwell/autoplay/manual controls, Safari compositing, reduced-motion static/instant path and returning-user retirement remain gated. Do not hide interactive controls from AT; keep stable semantic text/list separate from decorative moving text; avoid repeated live-region announcements. Do not make the phrase a navigation target or accept Gemini's click-to-advance suggestion without product intent. Stuart must test the exact released mechanics and responsive legibility, not memorised prototype angles.
