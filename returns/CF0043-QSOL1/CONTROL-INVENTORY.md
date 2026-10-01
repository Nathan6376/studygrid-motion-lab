# Meaningful controls and stateful surfaces

All rows refer to the verified QB15 HTML. A row groups repeated/template controls with the same semantics. `control-ledger.json` enumerates every opening declaration; `handler-ledger.json` enumerates every listener, including keyboard-only and global listeners, and stores complete callback code. Dynamic labels in the ledger remain source template expressions rather than invented rendered text. Read the effective override table first.

## Effective renderer chain

| Current symbol | Effective entry and retained implementation |
|---|---|
| render | 3045 wrapper → saved base 2025 dispatcher; demo decoration 3036 |
| renderWelcome | 3396 replaces 1737 entirely |
| renderCourses | 3400 decorates saved base 2119; changes Add label/heading |
| renderAddClass | 3405 replaces 1993 entirely; old animated placeholder setup is not the current form |
| renderCourseRoute | 3411 → base 2128; moves/clones Back, changes label to All courses |
| courseHead | 3409 replaces earlier 2135 |
| renderTree / renderTreeTopicDetail | 3052 / 3060 replace earlier tree layouts |
| renderStudy | 3065 → base 2255, maps topic route into Learn plus topic intent |
| renderStudyStart | 3135 → base 2272, adds topic-target/review preference controls |
| startSession / assessment / question / commit / finish | 3084 / 3091 / 3103 / 3116 / 3122 replace earlier versions; use multi-answer and reveal policy |
| renderSessionSummary / renderProfile | 3127 / 3146 → saved bases 2507 / 2641 |
| renderInstructorWorkspace | 3393 → 3216 → base 2864; adds integrated shell/study sets then R6 surfaces |
| sgR6PaintSources | 3390 preserves existing bound source controls and prepends new workbench; 3389 superseded |
| renderWorkspace | 3429 selects Professor Home vs exact class route, delegates owner/other to saved base 2829 |

## Landing, access, school and class entry

| Current label/control | DOM/code, state/route | Actual destination or mutation; feedback implication |
|---|---|---|
| StudyGrid wordmark; Courses / Study / Profile | global shell 1115–1129; `setGlobalNav` 2026 | Hash anchors to welcome/courses/plan/profile; mobile Study may point to active course Study. Shared learner shell remains on instructor paths (F01). |
| Feedback + count; Help | `#openSiteReports`, `#vtHelp`, static header | Feedback opens modal; Help toggles help UI (3481 script). No remote send. Hover geometry remains owner-review requirement. |
| Try StudyGrid / Take a quick tour / Sign in / Instructor demo | final welcome 3396, `[data-welcome-route]` / href controls | `/start`, `/tour`, `/access/login`, `/tour/instructor`. Three static explanatory `.r6-welcome-path` blocks are not separate working actions. Current sign-in hierarchy remains below first actions. |
| Back; Add a class; Explore a demo; instructor path | `renderFirstStart` 2013–2018, `#startBack`, `[data-start-route]` | Back→welcome; Add→courses list, not form; demo→pfp207 overview; instructor destination as encoded in data-start-route. Click suppression uses detail>1. No school/program/join-code stage. |
| Tour Back / Next / finish / Skip / step dots | 1895–1935, `sgMountStepTour` | Step-controller changes index; final learner destination `/start`, instructor `/workspace/instructor`; completion/skip flags persist. Busy/queued transitions; outgoing step inert. |
| Selected phrase / Explain / Highlight / Ask teacher | 1750–1768, `#tourDemoPhrase`, `#tourDemo*` | Opens tool group, displays explanation, adds visual highlight, shows unsent example. Enter/Space supported; same action does not toggle off (F08). |
| Tour answer / confidence / Skip / Try again / confidence why | 1770–1789, `[data-tour-answer]`, `[data-tour-confidence]` | In-place example answer→confidence→feedback; reset recreates controls. Does not mutate learning record. |
| Paper / Dusk in tour | 1750 `.tour-theme-samples span` | Decorative samples, not buttons. Do not conflate with Settings theme handler. |
| Access email; Preview new/returning user; switch access mode | 2628–2632, `#accessEmail`, `#previewSignIn` | Local email validation/school preview; Continue to demo→courses. No real sign-in/account. Back→welcome. |
| Are you an instructor? request Name/Email/Course; Create local request preview | access disclosure and `#previewInstructorRequest` | Adds local pending instructor request, persists. No verification/email/permissions. Normal vs owner capability requires later architecture/backend contract. |
| + Add class; Open; Demo examples / Open demo; Back | effective courses 3400→2119–2122 | Add→courses/add; Open sets active course/onboarding and goes local overview; demo sets fixture course; Back→start. |
| Class title/code/institution/term; optional instructor/section/schedule | final Add Class 3405, `#localClassName`, `#localClassCode`, `#localClassInstitution`, `#localClassTerm` | Datalist-assisted free text. Alias normalization; title/code assist only fills the other if blank. Institution/seasonal term repeated per class; autocomplete off does not disprove OS autofill report. |
| Create class; Back / Cancel | `#addClassForm`, `#addClassBack`, `#cancelAddClass` 3405 | Local class strings +timestamps saved through persist; then local overview. Both return courses, independent of prior entry. No join code/catalogue identity/profile context. |
| Bring in notes/material / Edit material / Skip for now | 2010 local overview | material route; Skip mutates onboarding phase and toast, stays on overview. Native details expose optional class info. |
| Save material / Cancel | 2011, textarea/form `#localMaterialForm` | Typed text saved locally to class, returns overview; Cancel→overview. No OCR/upload. |
| Start studying / Edit material / Back to overview | 2012 local Study | Displays saved typed text; marks local first-study loop. Practice generation is explicitly unavailable. |

## Learner study, progress and practice

| Control | Source/state | Actual result / notes |
|---|---|---|
| Overview / Study / Your tree / Class / Scenario lab; All courses | course rail 2128–2133 +3411 | Hash route per course; Sources/Notes map active nav to Study, Contribute to Class. Two visible All courses paths plus hidden original Back are duplicate escape routes. |
| Quick / Focused / Deep; Start this plan; See the change | 2136–2142 overview | Duration changes persisted `state.plan.duration`; Start→study/test (selection surface, not automatic quiz); See change→class. |
| Learning-tree topics / All topics / Study this topic / Learn | final 3048–3077 | Topic routes tree/topic; selected topic Study route retains topic intent; Learn source route; topic close/back stays course tree. Tree is local evidence record, not live 3D tree. |
| Continue learning / Open class / Continue quiz / Open test prep / calendar | `renderPlan` 2577 | Fixed active fixture course routes Learn/overview/Test; introductory copy has no retirement heuristic. Continue quiz opens Test surface with saved session, not implicit account resume. |
| Learn / Test / Support | base study start 2285 +wrapper3135 | `pushState` plus in-place paint; scroll preserved, keyboard tab refocused; bypasses route dispatcher/overlay cleanup for this action. |
| Continue notes / Review notes / note cards / calendar items | 2272–2293 | Exact note route; assessment calendar→Test. `#classScheduleFilter` filters row visibility only. |
| Browse lessons / Adaptive / Chapters / All topics / chapter disclosure / Show detailed lesson | 2549–2560 | Sources hash views `adaptive`, `chapters`, `all`; details open inline, summary/detail toggles expansion class. Large annotatable text areas. |
| Summary / Detailed notes; Mark reviewed / Mark unread | 2238–2245 | Persists mode or per-note reviewed-section set then replaces DOM; no explicit focus restoration or dedicated reward effect (F11). |
| Practise this class / Jump to next section / Back to Learn / Notes & questions | 2242–2247 | Test hash then RAF chapter drill; scroll to next section if current note; fixed Learn route; profile/notes route. Check last two against user context. |
| My note text / Save note / Attach files | 2248–2249 | Local text and up to six file metadata records; no binary upload. |
| Student recording/transcript file/type/share/people; Save source | 2250–2251 | Saves local submission metadata/share status; selected-people field conditional. No delivery/transcription. |
| Add instructor material | 2286 `[data-accept-teacher-source]` | Acknowledges source update locally, rerenders Learn. |
| Post type/text / class-board submit | 2293 | Adds local class-board record; Support rerender. |
| Duration / Start review / assessment prep / chapter drill | 2291;2265–2266;3084/3091 | Session creation persists question order/presentations; existing session blocks accidental replacement. Assessment reveal policy differs from practice. |
| Practice immediate-review preference / topic-target practice | wrapper3135 /sgDecorateStudyTopicIntent3069 | Changes local preference/starts bounded target; no per-question assessment correctness until end. |
| Saved quiz Resume/Continue / Options / pause icon | 2290;2357–2363;3103 | Pause/resume state; options modal Resume/Restart/Quit; Restart explicit destructive replacement; Quit returns Study start. |
| Single/multiple answer choice; Submit answers; confidence choices / Skip | 3103–3119;2380 | Multi toggles selected set; single pending answer; confidence commit idempotent by session committed ID. Saved pending choices restored; source policy applied. |
| Next question / N keyboard; open lesson; Report / dislike question | 2383–2388;2493–2494 | Advances within mount; N excluded for text-entry/modifier contexts. Lesson opens related Sources; question report opens local form. |
| Report category/details; Submit/Cancel | 2483–2489 | Appends local report/history; no server. |
| Collect Seeds / Review missed / View learning progress | base2507–2511 +3127 | Idempotent milestone reward; missed-prep local mount; progress→profile (F10). |
| Start missed retry / Back to summary | 2513–2518 | New explicit missed-ID practice / in-place summary. |
| Games & scenario / start game / Back to activities | 2295–2352 | In-place activity mount. Canopy arrows/WASD +question gates/Continue; Signal Drop directional keys/movement +theme handler; Branchline drag capture and ArrowUp/Down/Move up/down/Check order. `stopActiveMiniGame` clears cleanup callbacks. |
| Scenario story / notes / choices / Reset / Continue / Explain / Retry | 2701–2763 | Local active scenario path, notes saved on blur/progress, in-place consequences/debrief. Reset/retry uses PFP207 fixture, not arbitrary class generation. |
| Class chat draft/Send; Contribute material form | 2520–2534 | Local example conversation display/contribution metadata; source provenance shown, no live messaging/processing. |

## Instructor, owner, settings and global secondary surfaces

| Control | Source/state | Actual result / notes |
|---|---|---|
| Persona learner/instructor/owner; Sign out | 3031–3045 `[data-demo-persona]` / demo bar | Local demo session +destination; not authentication/authorization. Decoration only when eligible root page/course-shell exists. |
| Professor course Open class; search/sort; Pin/Favourite; colour/label select | 3422–3425 | Open exact instructor class route; query rerenders library +restores search focus/caret; organisation through revision-guarded gateway; visible editors conflict with owner requirement. |
| Attention Review in class / Mark resolved; resolved-history disclosure | 3420–3426 | Review→class overview without explicit task intent; resolve gateway +history, rerender attention; no Undo. Section focus target lacks tabindex. |
| Today and all Professor Home links | 3421/3427 | Exact class/overview routes; preserve stats/library/accepted visual hierarchy; local fixture data and fixed clock. |
| Switch class / individual class / All classes / Professor Home | 3210–3216;3429 | Switch panel toggle; direct class/tab rerender leaves URL; All classes incorrectly fixed pfp207-a overview; separate ← Professor Home hash link works. |
| Instructor tabs +ArrowLeft/Right/Home/End; term filter | 2940–2941 | Direct class rerender and keyboard focus restore; term filter toast only. Role nav still global learner shell. |
| Study-set filter/search/open set/question; approve/revise/reject/save draft/next pending | 3185–3207 | Local review map keyed by section +set revision +question revision, bound content identity; preserve stale-review guards. Dynamic labels/callbacks fully listed in ledgers. |
| Overview task/Open questions/Back overview; source policy/proof/student preview | 3367–3382 | Changes `sgR6.view`, rerenders/focuses task heading; native/fallback dialog open/close remembers invoker. No real source fetch. |
| Assessment form Save draft / Confirm / student preview | 3374/3379/3382 | Revision-guarded commands; draft saved in session; confirm resolves exact local assessment task; no publication/notification. |
| Keep/Split/Reset group; Approve shared answer; Resolve separate exception | 3375–3382 | Local grouping/status/history; preserved original questions; no sending. Targeted drafting source support remains separated. |
| Demo Back / exit / advance trigger | 3364–3366 | `sgR6.demoStep` /demoActive rerender; no learner auth. Legacy modal tour launcher removed by final wrapper. |
| Sort/filter/View student | 3383–3388 | Observable local question-workflow sort/filter; focused selects restored; detail insertion scrolls but no explicit heading focus. No grade/risk prediction. |
| Inspect proof / policy / Review proposed assessment | final sources3390 | Dialog; switches class overview then deferred assessment task. Existing bound source controls preserved. |
| Setup fields/files/Save class setup; question draft/review; replies/Plan reply | 2937–2992 | Locally persisted setup/file metadata/question draft and legacy review records; replies/history local; no actual distribution. |
| Announcement form/section checkboxes; reward templates/draft form | 2972–2979 | Local announcement/reward drafts, no posting remotely. |
| Instructor notes/source forms / Publish / approve student source / keep private | 2984–2992 | Local records +class-source update; publish label is local preview status, not provider publication. |
| Owner report state/request decisions; tab keyboard; analytics export/clear | 2829–2848 | Local report histories/instructor request decisions; CSV local download; confirmed destructive local analytics clear. No permissions change. |
| Profile settings/notes/inventory; saved quiz resume/options | 2641–2648 +3146 | Hash subroutes; local evidence stats; profile notes select/scope/context anchors, deletion/cancel local teacher question. |
| Theme Paper/Dusk; motion/tips/timer/garden/review prompts/sound/example history | 2660–2676 | Persist preference then rerender preserving specific control focus. Theme emits studygrid-themechange. Actual Dusk symptom needs reproduction on owner route. |
| Highlight colour / Save colour; teacher material mode/notifications; Show tips again; Replay tour | 2660–2676 | Local preferences; resets onboarding hint flags; tour route. No provider subscription. |
| Inventory buy/equip/remove | 2640/2678–2689 | Local seeds +owned/equipped appearance state; insufficient balance guard and persisted changes. |
| Context tips / What’s this? / close / delayed help question save | 1461–1469;2093–2099 | Focus-bound explanation/popover; delayed context help only eligible routes; local help-question save, no live AI. |

## Hidden/global input inventory

| Mechanism | Code | State/actual effect |
|---|---|---|
| Quiz exit link interception / Pause and leave / Stay / Escape | 2102–2111 | Captures last route trigger; active quiz route links open confirmation; Pause saves then sets href. Browser history changes separately handled. |
| Hash/popstate / storage event / visibility/activity clocks | 1701–1734;2116 | Coalesced route render/scroll/focus; cross-tab state read/rerender; auto-pause/timers. Storage event does not run full route overlay cleanup. |
| Text-selection tools / palette hover/hold / Explain/Highlight/Circle/Delete/Undo/Ask/Share | 2027–2046;2438–2478 | Mouse/keyboard/touch selection, native range caching; local annotations/teacher questions; undo expires after 8s. List deletion bypasses that undo path. |
| Feedback form/screenshot/export/clear/confirmation | static1120–1209;1591–1696;2048–2059 | Local structured feedback with route/viewport/selection, screenshot compression from file, CSV/JSON/MD downloads, confirmed local clear. No screen capture API or remote send. |
| Report Browse/Select items/Circle; Done/Cancel/Use selection; chip/review/remove selected item/area | 1658–1693;2060–2087 | Whole-page overlay selection workflow. Item mode intercepts page clicks; circle captures pointer; two-finger scroll custom handler; Escape closes. Gesture cleanup gap F05. |
| Tactile contact / Help dismiss / registry tagging | scripts3460/3481/3493 | Visual contact classes; passive cleanup on pointerup/cancel/lostcapture/scroll/blur/pagehide/hash. Help and data tagging do not introduce product auth/network. |

No runtime uniqueness/completeness count is claimed: template strings can generate additional instances, components can be hidden/disabled, and late wrappers replace earlier implementations. The declaration ledgers retain every candidate, exact callback and supersession classification so no legacy control is silently counted as current.
