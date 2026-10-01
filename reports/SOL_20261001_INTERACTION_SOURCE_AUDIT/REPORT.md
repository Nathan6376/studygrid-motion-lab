# Sol exact-source interaction audit — General CF-0047

**Terminal: DONE — source audit and isolated JavaScript reproduction. Browser geometry remains unverified.**

From CHAT-CGPT-20260930-STUDYGRID-SOL-01 / CF-0043 to CHAT-CGPT-20261001-GENERAL-01 / CF-0047. Owner activated this exact task with “Check routing — Sol.” STARTED was provider-recorded in the StudyGrid worker surface, row 63, before interaction inspection. TX-0269 binds this work. No candidate changes, design selection, implementation, installation, deployment, canonical promotion, external UX research, backend/auth/Supabase work, or worker activation occurred.

## Exact inputs and evidence boundaries

| Input | Verified identity |
|---|---|
| General task | `routes/GENERAL_20261001_1700_SOL_EXACT-SOURCE-INTERACTION-AUDIT.txt` at `d17644b81fa64a968f844c58d3cf58004fcea3c7`; blob `61182372666a48e10a3596b0504e190590d17742`. Same bytes independently read at `893f05ff75a7891a86bea39e0d362e8ac7de4257`. |
| Controlling owner delta | `routes/OWNER_REVIEW_DELTA_20261001_1657_PRODUCT-FLOW-STUDY-MODE.txt` at `9e44452c4687b03fe62a1bc6faee387cc2713c6d`; blob `87f8f141cf0bdf482a70c314b916689ddac99cf6`. Implementation remains held. |
| Candidate | `StudyGrid-CF0042-QB17R2-stuart-defect-repair.html`, Drive `1k0d69ZOrgs4NRRLRORKBmIwOR1Q0mE46`, 1,063,586 bytes, SHA-256 `874e4a743050d308759a9dcaefa9cc3296f8841c37b12e3acf5df2225ea49aab`, `v7.20-cf0042-qb17r2-stuart-defect-repair`. |
| Acceptance context | Stuart Q-S13R2 narrow PASS read at `893f05ff75a7891a86bea39e0d362e8ac7de4257`; two repaired tour/rotor defects only. This audit neither revokes nor expands that bounded acceptance. |
| Startup authority | Current Base `CGPTBASE-R0004-N8V6`; current Active Corrections; registry row46 CF-0043 ACTIVE and row50 successor General CF-0047 ACTIVE. AC-0017 is retired. `SOL_QUEUE.txt` still records the earlier Q-SOL1 DONE; the newly owner-activated exact General route is the task consumed here. |

**Pointer discrepancy for General:** the controlling owner-delta file prints `1k0d69ZOrgs4NRRORKBmIwOR1Q0mE46`, which lacks the `L` in the task's `...NRRLRORK...` ID. The delta's ID returned provider 404. The task's ID returned the correctly named HTML and exact expected hash/size/version. Smallest repair: correct that one pointer in a successor delta, preserving the frozen original. This did not block consumption.

All line references below are **physical lines of that exact 3,748-line HTML**, including long single-line definitions. Four executable scripts parse. Static extraction found 603 function definitions, 414 listener declarations, 638 native-control occurrences and 237 registry entries. These are syntactic counts, including conditional templates and superseded definitions, not counts of simultaneously visible controls.

`isolated-results.json` contains **12/12 passing detector scenarios** executing exact extracted functions/callbacks in Node VM with explicit DOM, time, storage and selected dependency stubs enumerated in the harness. PASS means the scenario's stated observation was reproduced; it does not mean the product has no defects. Browser-history events in the history scenario are simulated. No installed Chromium/browser engine was found. No CSS paint, actual button coordinates, browser hit-testing, real storage failure, native focus behavior, physical iPad/Safari/VoiceOver, hosted-origin behavior or network functionality is claimed. No external requests were made by the isolation harness.

Premise lineage: PRIMARY-DIRECT candidate bytes; USER-DIRECT activation; owner observations inherited through General's exact route/delta. Sol independently inspected the bytes and ran the stated mechanical checks, but shares General's observation framing and prior StudyGrid context. This is not a less-correlated cross-model review.

## 1. Route, control and state inventory

The complete syntactic navigation/surface-state inventory is `route-control-inventory.csv` (201 records). `control-ledger.json` retains every native control occurrence, raw attributes, owner, source line, exact href and selector-token handler candidates. `handler-ledger.json` retains exact callbacks, called functions and writes. Associations are candidate associations, not live DOM matches. `functions.json`, `bindings.json`, and `definition-chains.json` preserve exact implementations and aliases so a reader can resolve retained bases and replacements. The following table gives the operative hierarchy and important final bindings.

| Surface / visible control family | Destination or exact state/action | Classification / source |
|---|---|---|
| Global brand; Courses | `/courses`; instructor brand becomes `/workspace/instructor` | Global; static1125/1127, final role shell3523–3536 |
| Global Study | `/plan` | Global, learner study home;1128,2588. It is not the selected class's Study pane. |
| Global Profile | `/profile` | Global;1129 |
| Mobile Courses/Study/Profile | `/courses`; active course `/course/:id/study`, otherwise `/plan`; `/profile` | Global;1136–1140,2037. Mobile Study differs from desktop Study. |
| Feedback / Help | Static global feedback overlay; Help dialog | Command, not hash destinations;1130/1132,1648–1654,3545. Feedback save/export is local. Exact static ID is `#openSiteReports` at1130. |
| Welcome Sign in / Try StudyGrid / quick tour / Instructor demo | `/access/login`, `/start`, `/tour`, `/tour/instructor` | Entry / cross-role preview; final renderWelcome3598 |
| Welcome Show next step | Local rotor index; manual modulo3 | Local command;3598–3601; does not navigate |
| Access returning/new-user switch | `/access/login` ↔ `/access/signup` | Entry sibling;2639 |
| Access Back to StudyGrid | `/welcome` | Parent/up to public;2639 |
| Preview returning/new user | Validates example email, displays local receipt + Continue to demo `/courses` | Local command then entry transition;2639. No connected sign-in or account creation. |
| Instructor request preview | Pushes `state.instructorRequests`, local persist | Command / explicit placeholder for future verified access;2639 |
| First-start Back | `/welcome` | Parent/up;3610, unguarded by signed-in flag |
| I have a class code / Set up my school | Reveal code or school panel; focus code/institution input | Local command;3608–3610 |
| Class code Continue | `/course/pfp207/overview` | Explicit example preview; code is not validated;3610 |
| Save school setup | `sgQB17RSaveSchoolContext()` then `/courses/add` | Command→setup;3610 |
| First-start Your classes / Explore example | `/courses`, `/course/pfp207/overview` | Entry navigation;3608 |
| Your classes Back / Add a class | `/start`, `/courses/add` | Parent/up;2130–2133 retained by3411 wrapper |
| Saved class Open / Demo Open | Set active course, persist; `/course/:id/overview` | Local class selection;2133. Saved local classes and collapsed demo examples are separate collections. |
| Add-class Back / Cancel / Change school | `/courses`, `/courses`, clear school context then `/start` | Parent/up / setup command;3613–3618 |
| Add-class Save | Creates local class and opens its overview | Command→local class;3618. Catalogue options/manual entry are local. |
| Demo selected course rail | Overview `/overview`; Study `/study`; Your tree `/tree`; Class `/class`; Scenario lab `/scenario` on PFP207 | Local siblings;2141–2144 retained by3422. Hidden legacy Back is replaced by All courses→`/courses`. |
| Local created class | Overview `/overview`, Study `/study`, material `/material`; Courses→`/courses` | Local hierarchy;2019–2023. This is a different shell from populated demo study. |
| Local class Study | Read saved material; Edit material / Back to overview | Local command/navigation;2023. Practice generation is explicitly not connected. |
| `/plan` Continue learning/Open class/Continue quiz/test prep/calendar | Active known fixture course's `/study/learn`, `/overview`, `/study/test` | Cross-surface class entry;2588. Unknown local-course ID falls back to PFP207 fixture. |
| Course Overview Quick/Focused/Deep | Set plan.duration15/30/60, change copy/pressed state in place | Command;2147. Start this plan→`/study/test`, not immediately a session. |
| Study Learn/Test/Support | `/course/:id/study/learn|test|support`; custom pushState and `renderStudyStart` | Sibling/cross-mode;2283–2308, custom handler2296 retained via3146 wrapper. Outer course shell persists on this custom click. |
| Learn Continue notes / class date cards / calendar class event | `/course/:id/notes/:noteId` | Local child;2283–2308 |
| Learn Browse lessons | `/course/:id/sources` (default adaptive) | Local exploration;2283 |
| Lesson Adaptive/Chapters/All topics | `/sources/adaptive|chapters|all` | Sibling browse mode;2560. Chapter details native disclosure; detailed lesson toggles local content. |
| Related lesson question Practise in Quiz | `/study/test` | Cross-mode;2571. Does not directly run that specific question. |
| Notes class-date tabs / Back to Learn | `/notes/:noteId`, `/study/learn` | Local siblings / parent;2249–2264 |
| Mark reviewed / Mark unread | Toggle section ID in `classNoteProgress`, persist, rebuild notes, restore same control focus | Command;final3666. Changes Continue target and counts; not an attempt event. |
| Jump to next section | Scroll current note's first open section into view | Local command;2258. Does not mark it complete or go to another note. |
| Practise this class | `/study/test`, then `startChapterDrill` using note.topicId | Cross-mode;2257. Topic scope, not an exact note-only question collection. |
| Test Quick review/Focused session/Deep session | Set duration15/30/60; startSession uses common ordering and5/10/15 questions | Command;2283,2628,3095. Explicit assessments/question ID runs use their entire explicit list. |
| Practice review toggle / targeted chapter / assessment | Immediate review boolean; topic-filtered run; assessment mode with end-only reveal | Commands;3146,2276,3102. The toggled state is real local state. |
| Games & scenario practice | Scenario Lab / Canopy Chase / Signal Drop / Branchline | Local activity commands;2283–2365. Separate game/session renderers and state; not duration-specific implementations. |
| Support post / notes-and-question tools | Local class board / local notes/questions state | Commands;2283–2308. No real instructor/class delivery. |
| Single-answer practice | Final cloned answer handler→`sgQB17RShowConfidence`→commitAttempt | Command;3649,3655,3657. Confidence Off applies here. |
| Multi-answer practice | Toggle `pendingAnswers`, Continue→`sgConfidenceHost`→commitAttempt | Command;3114–3127, retained through3657. The single-answer clone override does not remove multi-select listeners. |
| Pause/Resume/Options / next question | Saved session status, restart/quit commands, advance index or finish | Commands;2368–2374,2504. Session-local, no parent route required. |
| Session Review missed / View learning progress / Back to course | Missed review prep/new attempt run; `/course/:id/tree`; `/course/:id/overview` | Command / sibling / parent;2518,2524, final3660. Final tree button overrides older `/profile` binding. |
| Collect Seeds | Manual local award attempt, persist, rollback on failure, dedupe by milestone | Command;2521. Not automatic collection. |
| Profile Notes/Settings/Inventory/learning Tree | `/profile/notes|settings|inventory`, current fixture `/course/:id/tree` | Global/local children;2652,3157,2671. Tree renderer remains a truthful placeholder. |
| Profile Instructor/Owner preview | `/workspace/instructor|owner` | Cross-role preview;2655. The role shell removes the owner persona button in the separate demo bar3525; that removal is not a source basis for declaring the profile's owner link removed. Neither preview is real authorization. |
| Instructor Professor Home | `/workspace/instructor` | Global instructor root;3438,3440,3534–3535. Label is literally Professor Home in several places. |
| Instructor Current class | Current `/workspace/instructor/class/:classId/:tab` | Local/contextual;3534. Root home defaults context to pfp207-a/overview. |
| Instructor Settings | `/profile/settings` | Cross-shell destination;3534. Role predicate3521 does not include profile/settings. |
| Class switching / All classes | Selected class overview route / `/workspace/instructor` | Sibling class / parent;final3630–3636. Final rebind replaces earlier in-place class-switch behavior. |
| Instructor Overview/Students/Study sets/Announcements/Sources/Achievements | `/workspace/instructor/class/:id/:tab`; Study sets tab key is `study` | Local siblings;2875,3227,3404,3633. Final render rebuilds selected workspace, not just active pane. |
| Study Set filter/search/open/question | `sgStudySetUI.filter/search/setId/questionId`; repaint entire study-set pane | Local state commands;3196–3212. No new hash per question/filter. |
| Approve & next / Edit / Request changes / Hold | Exact class/set/question revision-bound review; editor creates new local revision; approval selects next unapproved, then falls back to same q | Commands;3164–3170,3212 |
| Preview publication / Record local publication preview | Readiness check; pushes `ownerDecisions` with `local-preview-only` | Explicit local placeholder;3212. Does not transition a set into backend publication. |
| Instructor source/attention/student proof/demo actions | R6 local task state and anchored dialogs; exact bindings in handler ledger | Commands;3330–3404,3625–3641. Source association, approval and publication remain separate. |
| Instructor demo Complete / Skip | Final walkthrough retains workspace; setup `/start` or keep exploring `/workspace/instructor` | Cross-entry / local;3641. Earlier modal instructor tour1938 is replaced. |
| Help How works / Replay instructor tour / accessibility / feedback / Privacy / Legal | `/tour`, `/tour/instructor`, local disclosure, feedback command, `/info/privacy|legal` | Global commands/entry/info;3545 |
| Info Back / Welcome | `history.back()` if history.length>1 else `/welcome`; explicit `/welcome` | History command / public entry;3539–3542. No signed-in route guard. |

No unbound candidate is automatically called “dead.” Dynamic selectors, inline templates, conditional controls and final clone/rebind operations can defeat a token association. Explicit non-connected functionality is labelled a placeholder above; exact unavailable content paths are notices, not fabricated routes.

**Back escape paths:** demo course All courses→Your classes Back→`/start` Back→`/welcome`; local class Courses→same chain; add-class Back/Cancel→same chain; add-class Change school→`/start`→`/welcome`; local Study Back to overview→Courses→same chain. Access Back and info fallback also reach `/welcome` without checking `demoSignedIn`. Help's learner tour completes/skips to `/start`. The instructor demo offers setup→`/start`. These are source route paths, not proof of authenticated-account escape: the candidate is a local access preview and lacks connected authentication. Explicit preview sign-out does set `demoSignedIn=false` before welcome; pseudo-Back paths do not.

## 2. Owner-observation reproduction and defect disposition

“RUNTIME-REPRODUCED” below explicitly means **isolated exact JavaScript**, unless marked otherwise. It never means rendered browser reproduction in this return.

| Observation | Required classification | Exact finding / smallest later seam |
|---|---|---|
| Feedback square/count/highlight | CONFIRMED IN SOURCE for count/treatment; AMBIGUOUS for exact visual square | Static zero badge1130; count pill CSS223; final launch44px/min-width82 CSS1111. Border radius9px is specified, not a zero-radius square. Owner's precise painted artifact cannot be identified without rendered evidence. Later seam: launcher/badge CSS and count updater, preserve focus and feedback command. |
| Professor Home label | CONFIRMED IN SOURCE | Header/banner3438; return3440; global role nav3534; final replacement3636. Smallest copy repair spans these bindings rather than a single first match. Owner directs Home; no edit made. |
| Full-surface gloss | CONFIRMED IN SOURCE; NOT REPRODUCED visually | Course-card `:after` CSS1111 uses inset `-35% -65%`, a gradient sweep translated across the clipped card; hover moves card−2px. It is not confined to coloured top edge. Later seam: pseudo-element mask/extent, preserve reduced-motion rules1114. No judgment selecting an animation. |
| Class-code sharp green square/focus | AMBIGUOUS / NOT REPRODUCED visually | First-start choice reveals/focuses `#qb17rClassCode`3610; global final focus-visible outline3px + offset3px CSS1111. The owner could mean choice button or code input; source alone cannot prove which painted green square. Audit family includes generic focus, primary-button focus1032, review border363, pressed states and confidence contrast/legacy overrides. Preserve keyboard focus. |
| Your Classes empty / Back to onboarding | RUNTIME-REPRODUCED route callbacks; CONFIRMED IN SOURCE for population | Lists `state.localClasses` only, with example courses in a separate disclosure2130; empty local list has an explicit first-class notice. Back handlers with `demoSignedIn=true` still return `/start` then `/welcome`. Smallest seam: signed-in root/Back destination contract, after design selection. Do not equate local empty list with missing remote roster. |
| Learn/Test/Support jumps / moving controls | CONFIRMED IN SOURCE seam; NOT REPRODUCED geometry | Every switch replaces studyMount children. Test wrapper3146 **prepends** `.study-mode-truth` before existing purpose tabs; Learn/Support do not. CSS1057 adds variable-height flex content and margins. This changes DOM vertical ordering before the same nav target. Custom handler preserves outer shell and tries to restore/clamp scroll, so “whole shell always remounts” would be false. Later seam: common persistent mode header and shared content anchor; measure actual rectangles before fixing. |
| Schedule/filter shifts | CONFIRMED IN SOURCE mechanism; NOT REPRODUCED geometry | `classScheduleFilter` toggles `.filtered-out` event rows2299; mode calendar/grid content and disclosures have different height. Instructor sort/search repaint library3623; search restores focus/selection. Target position changes not measured. |
| Quick/Focus/Deep purpose | RUNTIME-REPRODUCED duration/count; CONFIRMED IN SOURCE copy | Exact title is **Focused session**. Common question priority/order; duration15/30/60 yields5/10/15 ordinary questions3095. No timer-enforced finish or distinct pedagogy in startSession. Explicit assessment/topic question lists bypass count cap. Later seam: purpose/plan model + ordering, not names alone. General/design team decides whether to retain. |
| Mark as reviewed only tiny border | RUNTIME-REPRODUCED state, CONFIRMED IN SOURCE visual seam | Exact label is **Mark reviewed**. Toggle advances next open section and changes reviewed count; toggling back restores it. Sources also show Reviewed/Not reviewed yet, Mark unread, note-card counts, caught-up state2249/2283. It creates no attempt or later-memory evidence. CSS363 adds a subtle read border. Owner's lack of meaningful progression is a design issue; “only border/no state effect” is contradicted by source. |
| Approve & next moving target / final no-op | RUNTIME-REPRODUCED final selection; NOT REPRODUCED geometry | 15 approvals advance q1…q15, then q15 remains; repeated approval retains q15 and rerenders. Review status can become Ready, but action stays Approve & next. Action row follows variable stem/options/rationale/source in normal flow3208/CSS1073; no fixed target anchor. Final state seam3212 and stable action layout seam3208. |
| Draft/Ready/Published/Held/All | RUNTIME-REPRODUCED status function; CONFIRMED IN SOURCE filters | Quiz1 state derives from effective exact-revision reviews; all approved→Ready; any held→Held; needs changes maps to Needs review. Seminar draft, quiz0 published, source-review held are fixed fixture seeds3185, overriding review state. All is a filter, not a persisted status. Publication is local preview only; recording it does not change sgSetStatus into Published. Later seam: unified status/read-model contract, retaining revision binding and approval/publication separation. |
| Practice confidence whole green | CONFIRMED IN SOURCE; NOT REPRODUCED visually | Dark-green gradient applies to `.confidence-host` CSS1054; older `.confidence-choices button` important backgrounds/borders799 also survive. Final single-answer wrapper changes layout/copy, not host gradient1111/3649. This is a cascade family, not just selected-state styling. |
| “Choose all three…” cannot multi-select | NOT REPRODUCED failure; RUNTIME-REPRODUCED successful isolated selection | q4m has correctAnswers[0,1,2], selectionMode multi, requiredChoices3 at3088. Exact multi listeners retain three aria-pressed selections, submit array, and commit correct result. Final single-answer clone selector only matches `[data-answer]`, not `[data-answer-multi]`. No rendered/native reproduction; retain owner issue open for browser/target reconciliation rather than inventing a handler defect. |
| Multi-select confidence setting | RUNTIME-REPRODUCED additional defect SOL-F04 | Setting Off is respected by final single-answer handler3649 but ignored by multi-submit's sgConfidenceHost3103. With `qb17rConfidenceEnabled=false`, confidence UI still appears. Smallest repair: apply same optional-confidence contract to multi host, preserving selected array and null semantics. |
| Multi-select answer receipt | RUNTIME-REPRODUCED additional defect SOL-F05 | Final renderFeedback3653 indexes choices with an answer array: correct [0,1,2] prints **0,1,2**. On incorrect multi selection its Correct answer uses scalar q.answer0 and omits other correct answers. Smallest repair: format selections using questionSelectionMode/questionCorrectSet consistently, including final fallback3657. |
| “McCue” / case clue answer leak | CONFIRMED IN SOURCE for q14 leak; AMBIGUOUS speech term | q14 at1289 has pre-answer example **“Macooh fled a traffic stop. The course point is that a suspect cannot escape an active arrest pursuit simply by crossing the threshold into a home.”** Correct choice is **“R. v. Macooh”**. Base session3114 renders q.example before question/answers, including assessment. This mechanically supplies the name clue. Literal McCue is absent. Smallest seam: question example/reveal contract, not assumed legal correction. q3/q3s also expose Macooh contextual text but ask concepts/situations. |
| “Canascape” term | AMBIGUOUS | Literal Canascape absent in candidate; do not map it to a legal term or alter course content. Source spellings Macooh, Mann, Feeney and other case names are preserved exactly. Owner/primary course source must reconcile the speech term. |
| Seeds manual/automatic/failure | RUNTIME-REPRODUCED isolated storage-failure rollback; CONFIRMED IN SOURCE manual action | finishSession records reward with coinsCollected=false; collectCoins click awards. Forced persist=false removes award, restores balance and coinsCollected, and emits **“Could not save Seeds yet. Nothing was collected.”** Success adds once and repeated click dedupes. This branch is local persistence failure, not proof of a backend/network disconnection; actual owner's storage cause remains unknown. Later seam: idempotent award timing/receipt; preserve rollback and duplicate protection. |
| Completion directionality | CONFIRMED IN SOURCE | Review missed starts preparation/new attempts; View learning progress final binding→course tree; Back to course→overview. No dedicated recommended-next-learning action is encoded in summary2518/3138/3660. Owner's forward-flow request goes to design; preserve original attempts/missed set and truthful learning-change distinction. |
| Welcome1→2→3 continuous loop | RUNTIME-REPRODUCED bounded autoplay; CONFIRMED IN SOURCE WAAPI | Starts1, auto advances2 then3, stops on third timer callback (`++runs>2`). Manual next wraps3→1. Focus/pointer/touch/key/manual interaction stops autoplay; reduced motion remains static until manual advance. These are the earlier accepted accessibility properties. Continuous loop is a newer owner requirement, not evidence Stuart's prior bounded test was false. Later seam3598: reconcile continuous default with explicit engagement/reduced-motion behavior. |
| Study purpose browser Back | CONFIRMED IN SOURCE / RUNTIME-REPRODUCED with simulated history events, SOL-F06 | Purpose handler2296 pushStates test and paints it without updating lastSettledRoute. Starting Learn→Test→first Back to Learn, route callback2127 sees previous==current Learn and skips render; Test markup can remain under Learn hash. Exact callbacks reproduced that mismatch in VM. Browser event/native reproduction pending. Smallest seam: reconcile route bookkeeping on custom pushState or one common route transition path. |

SOL-F01 is the signed-in Back contract, SOL-F02 the terminal review state, SOL-F03 q14 name leakage, SOL-F04 multi confidence, SOL-F05 multi receipt, SOL-F06 custom history bookkeeping. These audit-local identifiers persist the defect/disposition without inventing canonical project bug IDs. Geometry concerns remain owner observations with source seams, not measured failures. No repair has been implemented.

**Additional pool divergence:** ordinary buildQuestionOrder1568 considers all 17 QUESTIONS entries, including original q3/q4 and replacement q3s/q4m. Chapter and first assessment map old IDs to replacements3089–3090; Quiz1 review is15 questions3176. Thus default practice and instructor review do not use one identical pool. Do not silently retire or alter questions during this audit. Smallest future seam: explicit source question-pool/read-model membership, preserving IDs/revisions/attempt provenance. This is source-confirmed, not a legal-content judgment.

## 3. State, shell and stability mechanisms

| Transition / target | Persistence, rebuild and scroll/focus behavior | Geometry evidence |
|---|---|---|
| Major hash/history route | Static topbar/mobile/feedback overlays persist outside root. Course/workspace/page renderers replace root.innerHTML. handleRouteHistoryChange stops game/closes overlays/renders; major context focuses heading and scrolls0. | Source-confirmed; actual size/CLS not measured. |
| Same course view deeper route | Context key is course/id/view; noteID/topicID changes preserve same context. Source anchor/scroll capture resolves replacement element and adjusts delta/focus. | Source-confirmed conditional restoration; native focus not verified. |
| Learn/Test/Support direct click | Custom pushState; replaces studyMount only; pointer blurs old link, keyboard explicitly focuses replacement link; attempts old scrollY clamped to new document height via double RAF +80ms timeout. Outer shell remains. Test truth preamble shifts inner nav order. | No browser rectangles. Shorter content can clamp scroll; preserved document Y does not guarantee stable visual anchor. |
| Instructor class/tab | Context key only workspace/instructor, ignoring class/tab. Final wrappers navigate hashes and rebuild entire workspace. Same-context route handler normally avoids heading focus; no captured replacement anchor means focus can be lost with old node. | Source risk, not native reproduction. Class change does not automatically count as major route context. |
| Study Set approval/filter/search | Replaces whole study pane innerHTML; summary/list/queue/canvas/action targets replaced. Approval row follows variable content. No explicit approval focus restoration in sgBindStudySetDetail. | Source reflow seam; no pixel displacement measured. Search input replaced every input event without this function restoring focus. |
| Notes reviewed | Whole notes content rerenders; final wrapper restores the same reviewed control focus with preventScroll. Section state/progression recomputed. Jump uses scrollIntoView. | Focus call evidenced; scroll/paint unknown. |
| Instructor course-card organisation | Library repaint on sort/pin/favourite/edit/save; selected selector focus restored and search selection reconciled. Edit disclosure changes card content/height. | Source mechanism; grid movement unmeasured. |
| Confidence / question reveal | Single answer replaces chosen button with confidence host; other answers receive answer-exit; multi host replaces stage. Commit rerenders question/feedback stage; changing stem/context/feedback height relocates normal-flow controls. | Source mechanism; no coordinate claim. |
| Welcome | Rotor faces hidden/unhidden + WAAPI opacity/rotateX/translateY; container minimum heights. Timer local to render function. | Exact timer tested; animation paint and orientation not judged. |
| Tour How this works | Existing accepted fixed anchored dialog and focus handling remain in source; prior Stuart reported0px Next shift. | Stuart's inherited browser measurements are not newly reproduced by Sol. |

History machinery: location.hash, history.replaceState, custom history.pushState, both hashchange and popstate handlers, and info history.back. `data-vt` identifies the visual/material layer; **no `startViewTransition` call occurs**. WAAPI `.animate` exists in rotor, tour and other UI controllers; CSS transitions/keyframes, reduced-motion media and lessMotion state are already present. Do not claim that a View Transition implementation exists from the attribute name.

Duplicate chrome source: learner global Courses/Study/Profile plus selected course rail and course head; nested Study-purpose tabs and lesson/note navigation; desktop and mobile nav variants; instructor Home/current-class/settings plus home-return link, selected-class header and tabs. Responsive visibility matters, so this is layered navigation, not proof that desktop and mobile controls are simultaneously visible. Instructor role shell depends on route prefix, not previewPersona: `/profile/settings` leaves instructor prefix and can restore learner global chrome while persona state remains unchanged. This is a concrete source context boundary for design reconciliation; no live authorization consequence is implied.

## 4. Exact copy and terminology

| Requested wording | Current exact source |
|---|---|
| Your class, easy to learn | **Your class, easier to learn** — final welcome3598. Earlier welcome3407 has **Your class. Ready for what comes next.** but is replaced. |
| One common path from class material to useful practice | **One calm path from class material to useful practice.** —3598. |
| Professor Home | **Professor Home**, **Professor Home · Example data**, **← Professor Home** —3438/3440/3534/3636. |
| Quick/Focus/Deep | **Quick review**, **Focused session**, **Deep session** —2628; overview shorthand **Quick**, **Focused**, **Deep** —2147. |
| Your Classes | **Your classes** —2130/3411,3608,3622. Final3411 replaces the older2130 heading **Add or open a class** with **Your classes** and changes Add a class to **+ Add class**. Case and final override preserved. |
| Mark as reviewed | **Mark reviewed**, **Mark unread**, **Reviewed**, **Not reviewed yet** —2249. No exact “Mark as reviewed” label located. |
| Seeds/failure | **Collect Seeds**, **Collected**, **No Seeds from this quiz.**, **Could not save Seeds yet. Nothing was collected.** —2518–2521. |
| Confidence | Single **How sure are you that your answer is correct?**, **Guessing**, **Fairly sure**, **Very sure**, **Skip confidence** —3649. Multi retains **How sure were you?**, **Skip** —3103. Setting **Confidence after answers** —3663. |
| Study Set states/filters | State labels **Needs review**, **Draft**, **Ready**, **Published**, **Held** —3185. Filter **Drafts** plural and **All** —3196. Review decision label **On hold** differs from set **Held** —3170. |
| Approval action | **Approve & next** —3208. |
| Session end | **Review missed question(s)**, **View learning progress**, **Back to course** —2518/3138/3660. |

## 5. Minimal implementation seams for later selected redesign

1. **Root/context contract:** render/parseRoute/nav wrappers, first-start/courses Back bindings, `routeContextFromParts`, role-shell predicate, and custom Study pushState. Define signed-in root and role/mode context before changing chrome. Preserve explicit sign-out semantics and local-preview truth.
2. **Stable common Study header:** renderStudyStart2283 + wrapper3146; keep persistent mode controls outside purpose-specific preambles and content replacements. Define expected scroll/focus anchors and browser Back/Forward contract. No chosen layout is supplied here.
3. **Review workbench completion/action anchor:** sgStudySetDetailMarkup3204, canvas3208, binder3212 and status3185. Add real terminal selection state after last approval; preserve revision/class isolation and require publication separately. Measure variable text at representative widths before prescribing fixed/sticky action geometry.
4. **Question/answer contract:** selection-mode helpers3091–3093, confidence host3103/final3649, final feedback3653/fallback3657 and example rendering3114. Align optional confidence and multi answer receipts; prevent case-name clue leakage; make default/assessment/chapter pool membership explicit. Preserve arrays, scoring, provenance and end-only assessment reveal.
5. **Progress/reward/completion:** reviewed-section model2195–2211, summary/finish3133/3138/3660, manual award2521. Decide reviewed meaning and forward progression first; any automatic award must retain dedupe, storage rollback and truthful result receipts.
6. **Shared visual family:** global focus1111, primary focus1032, confidence cascade799/1054/1111, badge223/1111, card sweep1111 and reduced-motion1114. Repair families coherently after design selection; do not remove keyboard focus or accessibility behavior to eliminate a green border.
7. **Welcome copy/timer:** final3598 only; exact owner copy differs from accepted candidate. Continuous cycle is a future owner requirement. Retain stable semantic summary, AT-hidden moving layer, reduced motion and interaction-stop properties while reconciling its new continuous-loop contract.

These are source seams and small functional repair boundaries, not a product-design selection or build instruction. Bob's separately routed feasibility lane and Astra/Research lanes remain the proper consumers of architectural/design options under General.

## 6. Liked behavior and safeguards to preserve

- Owner's preferred copy is exactly “Your class, easy to learn.” and “One common path from class material to useful practice.” Preserve those owner requirements; current source uses the differing predecessor strings listed above.
- The15-question review and fast Approve & next workflow, with real class/revision-bound approval and publication separation.
- Coloured edge identity and hover gloss intent; easy class switching and readable class/code/section context.
- Course overview/course context and Scenario Lab orientation, with room reduction left to selected design.
- Continue learning / Continue notes, next-open-section logic, counts, reversibility of reviewed state and truthful completion.
- Source-context practice, selected answer retention, multi-select scoring, optional confidence/null semantics and delayed assessment reveal.
- Missed-question review creates new evidence instead of erasing original attempts; later-memory growth is not claimed from mere first practice/review flags.
- Reward award idempotence and failure rollback; Seeds stay separate from grades/access/learning evidence.
- Welcome stable semantic3-step list, AT-hidden non-live animation layer, engagement pause and reduced-motion static/manual behavior; tour fixed How-this-works disclosure and explicit focus restoration.
- Local/example/non-connected truth, supplied legal/course terminology, existing storage preservation and feedback privacy/export choices.

## General consumption / next step

Consume this package as the current exact-source feeder. Keep owner implementation hold active. Carry SOL-F01…F06, the default-vs-review question-pool divergence, the source-backed layout seams, and every NOT REPRODUCED/AMBIGUOUS item into synthesis. Reproduce moving-button/green-square/native multi-select claims in an installed browser against the same hash before implementation. Obtain the exact observed screen/state for ambiguous speech terms; do not silently rewrite legal terminology. No worker wake, release or owner courier action is issued by Sol.

The source hash is rechecked at terminal publication. Publication/readback proves availability, not General's adoption or background wake.
