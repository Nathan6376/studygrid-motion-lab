# Route and button transition map

Source route dispatcher: 2025, wrapped at3045. `nav(route, replace=false)` 1588 remembers same-context scroll, then hash or replaceState. `parseRoute` 1589 defaults to welcome. Unknown course replaces to courses; unknown course view displays error +Course overview; unknown top route shows not-found. Anchors remain in `control-ledger.json`; all explicit nav/history calls are in `routes.json`.

## Deterministic route families

| Route | Renderer / entry state | Exit / continuation semantics |
|---|---|---|
| `/welcome` | final3396 | Try→start; tour→tour; Sign in→access/login; instructor demo→tour/instructor |
| `/tour`, `/tour/instructor` | 1915/1927 +step controller | internal index; learner final→start; instructor final→workspace/instructor; skip/finish record local flags |
| `/start` | 2013 | Back→welcome; Add→courses; demo→course/pfp207/overview; instructor action uses its data route |
| `/access/login`, `/access/signup` | 2628 | mode switch; local preview then Continue→courses; Back→welcome |
| `/courses` | 3400→2119 | Back→start; Add→courses/add; local/demo open→course/id/overview |
| `/courses/add` | final3405 | Create→course/local-id/overview after local save; both Back/Cancel→courses |
| `/course/local-id/overview` | 2008/2010 | material, study; local Back→courses; Skip stays here |
| `/course/local-id/material` | 2011 | save/cancel→same overview |
| `/course/local-id/study` | 2012 | displays typed material; Edit→material; Back→overview; no generated quiz |
| `/course/id/overview` | 2128→2136 | duration choice; start plan→study/test; tree/class/context routes |
| `/course/id/study/{learn,test,support}` | 3065→2255→3135→2272 | purpose tabs pushState/direct render; note route; local sessions/games/scenario inside mount |
| `/course/id/study/topic-id` | 3065 /3069 | validated topic intent→Learn; wrapper inserts topic-practice action; does not treat arbitrary topic as purpose tab |
| `/course/id/notes/note-id` | 2238 | review/read/view state in place; Back→study/learn; Practise→study/test then RAF drill; Notes/questions→profile/notes |
| `/course/id/sources/{adaptive,chapters,all}` | 2549 | mode anchors; lesson detailed expansion and chapter details local; annotation state local |
| `/course/id/tree[/topic-id]` | final3052/3060 | topics hash; same selected-topic button closes to tree; Study this topic→study/topic-id; Learn→sources |
| `/course/id/class`, `/contribute`, `/scenario` | 2520/2530/2701 | local chat, contribution metadata, scenario state. Course rail remains available |
| `/plan` | 2577 | active fixture course Continue→Learn; Open→overview; Continue quiz→Test; calendar/test same course |
| `/profile`, `/profile/settings`, `/profile/notes`, `/profile/inventory` | 3146→2641,2660,2648,2678 | Back to profile fixed; saved quiz explicit resume; annotation-context links return to stored source route |
| `/workspace/instructor` | final3429→3427 | Professor Home library, attention/history, Today; Open/Review→exact class overview |
| `/workspace/instructor/class/id/tab` | final3429→3393 chain | exact initial class/tab; tabs/class switch subsequently rerender directly; ←Professor Home works via hash |
| `/workspace/owner` | 3429→2829 | local owner tabs/decisions/analytics, no auth claim |

## In-place state machine

| Surface/action | Actual next state | URL/history/focus contract |
|---|---|---|
| Study duration | persisted plan duration | no URL; button aria-pressed changes |
| Start review/assessment/chapter/topic | currentSession with fixed question/presentation identity | same Study route; existing saved-session guard |
| Answer | pending single/set → confidence | same mount; focus shifted to confidence; assessment remains neutral until summary |
| Commit confidence/Skip | append attempt →feedback/neutral submitted | committed ID guard; no premature assessment correctness |
| Next / N | advance or finish | same route; source handlers gate editable targets/modifiers |
| Pause/Resume | session status/timer | rerender; preserve pending/committed state |
| Options Restart/Quit | replace/clear session after explicit command | Restart→Test; Quit paints Study start; do not claim route back to previous arbitrary location |
| Summary→missed review→retry/back | prep /new target/summary | same mount; profile link separately changes route |
| Note review/detail | saved set/view mode | same route, full DOM replacement with missing explicit focus restoration |
| Professor resolve | revision command→resolved history | same home, focused source button removed; section focus target inadequate |
| Instructor class/tab switch | chosen renderer argument | **no URL update**, old class/tab URL remains; history cannot replay internal sequence |
| Instructor task/back | sgR6.view home/assessment/questions/etc | same class route; `sgR6RefreshOverview` focus ID |
| Dialog open/close | native showModal/close or open fallback | stable invoker ID focus; verify keyboard Escape/cancel |
| Feedback open→mark→Done/Cancel→form→thanks | overlay mode +pending selection/report | no route; modal focus/trap. Route close hides report overlays but misses gesture/annotation reset |
| Tour index | WAAPI busy/queue, outgoing inert→committed target | same route; buttons reflect first/final step; source detachment guard |

## Semantic findings, without choosing new design

| ID | Exact trigger and result | Required later acceptance |
|---|---|---|
| R01 | `All classes` switch item3213 opens fixed Police Powers section overview. | Label must match exact released class-index destination; preserve explicit instructor entry. |
| R02 | Instructor class/tab buttons2939–2940/3213 mutate renderer arguments without hash. | Address and reload/history must remain consistent with shown class/tab; General decides released routing contract. |
| R03 | `View learning progress`3127 retains `#seeTree`2511 →profile. | Decide expected progress destination in complete owner contract; don't blindly point every Profile link at Classes. Record Nathan's reported case as unlocated. |
| R04 | Add Back/Cancel→courses; notes Back→Learn; settings/inventory/notes Back→profile; start Back→welcome. | These are fixed hierarchy returns, not browser Back. Verify entry from all contexts/deep links and label accordingly; don't invoke history.back when no safe predecessor. |
| R05 | Instructor route shares Courses/Study/Profile/mobile active-course learner shell. | Role-specific IA and deliberate exit route; preserve global feedback/help and keyboard access as released. Local persona is not real permission enforcement. |
| R06 | Course rail includes All courses plus r6 cloned All courses, original hidden Back. | Reconcile duplicate exits while retaining one discoverable context return; source registry/test selectors must follow final node. |
| R07 | Welcome and start both contain demo/tour/start entry paths; Professor attention Review lands overview without task ID. | Treat as context/duplication audit input, not automatic deletion. Acceptance should verify labelled context and intended follow-up task. |
| R08 | Same-route context1582 groups workspace by role only, ignores class ID. | Cross-class navigation may preserve scroll/focus as same context; test class→class with different layout and task anchors. |
| R09 | Study tab pushState2285 paints directly without global render/cleanup/focus entry. | Prevent stale modal/annotation state; refresh global marker/remembered route consistently if contract requires. Preserve existing keyboard refocus/scroll. |
| R10 | hash+popstate2116 coalesced RAF→stop game→close overlays→render→route focus when context changes→settle scroll. | Any new animation must preserve this order/one commit; no delayed stale focus/scroll after a newer route. |

## Animation-sensitive seams

`focusRouteEntry`2024 chooses h1/h2 tabindex-1; `settleRouteScroll`2115 restores anchor/context via RAF; `sgCreateStepController`1837 handles inert outgoing content and queued steps; `sgTourSettleFocus`1881 restores connected control or heading; direct study/tab/note/attention handlers have separate focus obligations. A transition must not cover the fact that note review/resolve lacks a sound focused successor. Reduced motion uses `motionAllowed`1477 and `sgMotionOn`1823; preserve both OS and preference handling. General/Research owns which transitions, duration/easing and contextual chrome pattern. This map supplies seams, not a motion specification.
