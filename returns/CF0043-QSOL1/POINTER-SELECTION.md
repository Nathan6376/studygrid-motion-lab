# Cursor, selection, capture and teardown

`cursorCSS.json` contains every extracted rule involving cursor, user-select, pointer-events, or touch-action; `selectionCalls.json` contains actual member calls to native selection/capture operations; `handler-ledger.json` includes all input listeners and callback bodies. The extraction excludes a whole-IIFE false positive by matching member method names exactly. No device reproduction is claimed.

## Source mechanisms

| Area | Selector/function/event | Source truth and bounds |
|---|---|---|
| Annotatable text | `.annotatable-text`584–605; notes2242, quiz explanations2385, lessons2560 | Explicit `cursor:text`, user-select text, WebKit selection/callout, `touch-action:pan-y`. Substantial portions of study text use this class. No corresponding body-wide cursor:text rule found. |
| Annotation marks | `.annotation-highlight`, `.annotation-circle`607–608 | Pointer cursor on saved clickable marks, separate from text selection. |
| Tour phrase | `.tour-demo-phrase`, role button1750 | Pointer-like interactive phrase and Enter/Space. Learn demo uses one-way open/highlight, not real saved native annotation. |
| Selection caching | `annotatableFromNode`2469, `currentAnnotationRange`2470, `cacheAnnotationRange`2471 | Restricts usable range to annotatable surface; cloned native range and surface ID cached, connected-node guard. |
| Deferred selection tools | `captureAnnotationSelection`2473; mouseup/keyup80ms, touchend520ms, contextmenu cache2475; selectionchange2476 | Debounced callback falls back to cached/still-connected range. Native range removal alone does not invalidate cached clone. |
| Tools fallback | `[data-selection-tools]`/`.selection-tools-fallback`2477 | pointerdown preventDefault preserves selection; keyboard click opens and focuses Explain. Intentional narrow interception, not forced page-wide cursor assignment. |
| Palette hold | #annotationHighlight2031–2036 | Mouse hover260ms, touch/pen hold430ms; leave/up/cancel clears hold timer. Route teardown has no explicit cancellation. |
| Annotation outside/Escape close | document pointerdown2045/keydown2046; `closeAnnotationPopover`2439 | Hides popover/palette/edit row, clears pending selection and native ranges; not timer/cache. Route cleanup2112 omits annotation close. |
| Annotation undo | 2448–2454 | 8-second local undo/snapshot for main highlight/circle/delete path; list deletion2478/profile2656 does not offer this undo. Unrelated to professor resolved history. |
| Report overlay | #reportMarkShell, #reportMarkCanvas report CSS near302–341 | Fixed full viewport shell pointer-events none; canvas pointer-events none/touch-action none; circle mode canvas pointer-events auto/crosshair; item mode shell crosshair. Hidden close removes visible interception via `.hidden`; no JS body cursor override. |
| Report item mode | document click2084 | Active unhidden item mode prevents default/propagation for underlying page click, toggles selected element. Browse mode permits page interaction/navigation. |
| Report circle | canvas pointerdown2076/move2077/up+cancel2079; finish2078 | capture single pointer; coalesced coordinates; draw/finish. `reportCirclePointer` must be null to accept a new down. No canvas lostpointercapture listener. |
| Two-finger reporting scroll | touchstart2080/move2081/end2082/cancel2083 | Releases active capture, clears drawing/pointer on second finger; manually scrolls while circle canvas has touch-action none. Last centroid resets on fewer than2/end/cancel. |
| Report close/route close | 1666/2112 →1668/1693 | Clears visual target/items/points/bounds/areas; does **not** clear drawing/pointer/centroid or explicitly release capture/reset mode. Open1665 sets Browse, clears items/areas but also does not reset pointer ID. |
| Branchline reorder |2350 pointerdown capture,2347/2348 move/end,2351 cleanup | Scoped drag; keyboard ArrowUp/Down and Move buttons are alternatives; use actual cleanup body when adding transitions. Distinct from report capture. |
| Tactile script |3460–3479 `.sg-contact` | Passive visual contact listeners; no capture/preventDefault. Cleans on up/cancel/lostcapture/scroll/blur/pagehide/hash. Cannot explain blanket native selection by itself. |
| Disabled/transition surfaces | tour outgoing `inert`, pointer-events1837; answer exit confidence and CSS rules | Interaction intentionally suppressed while outgoing content leaves. Test rapid press/route detach; avoid frozen inert subtree. |

## Conditional source-state defects

**P01 — report close during an active gesture.** Begin circle mode; pointerdown sets `drawing=true` and pointer ID. Escape/route close clears visual points but leaves both fields. If no later pointerup/pointercancel reaches the canvas, reopen and select Circle; pointerdown guard rejects a new gesture because pointer ID remains non-null. Conversely, a later matching up/cancel can finish/reset it, so this is a reachable stale-state path rather than proof that every close breaks reporting. The browser may implicitly release capture on hide/detach; there is no lostpointercapture handler to reset JS state. The isolated source check verifies the close/open fields, not delivery of native events.

**P02 — close followed by deferred annotation reopen.** Capture a selection, then outside-click close before timer fires while surface stays connected. Close removes native ranges/pending state; queued callback can use its captured cloned range and reopen the popover. Route replacement may disconnect the old range and reject it, but closeRouteOverlays does not hide an already-open annotation UI or cancel timer. A shared idempotent teardown seam should invalidate timer/cache/pending UI before painting new context, while preserving saved annotations.

**P03 — visible Dusk sample vs Settings control.** Tour appearance contains spans, hence no theme click handler there. Settings uses native button click and persists/applies/rerenders preserving focus. Owner route/device must be identified during later QA; no source-only claim that this distinction caused the reported symptom.

**P04 — focus replacement.** Note review replaces focused button; professor resolve removes focused control then tries focusing a section without tabindex. The selected/mutated state can be correct while keyboard focus is lost. Reward/route animations must not postpone or mask focus repair.

## Bounded Safari/iPad acceptance checklist (later, held)

Use exact released candidate hash, Safari version/iPadOS, viewport/orientation, mouse/trackpad vs touch vs Pencil, and whether HTML is opened as local attachment or hosted. Record one short before/action/after case per symptom. Do not report these as passed by this audit.

1. Tour Learn phrase: tap/Enter/Space twice; explicit toggle off per released contract; selection, no trapped highlight; tour step change/Skip/Back leaves no stale tools.
2. Tour appearance vs Settings: identify actual Dusk target. Settings Paper→Dusk→Paper via tap, pointer and keyboard; reload persistence; no overlay steals hit target; focus remains usable.
3. Lesson/note/quiz explanation: pointer over text, whitespace, control and rail; native long-press/drag/keyboard selection. Cursor:text limited to intended wording; selection still works; no blanket user-select:none workaround.
4. Select wording→outside click/Escape before80/520ms completes; tools stay closed. Repeat after route/tab switch, browser Back/Forward, scroll, rotation and app background/return.
5. Highlight hover/hold→route change/cancel; palette timer does not resurrect UI. Undo within/after8s; saved annotation context remains exact; orphan ranges handled.
6. Feedback Browse/Item/Circle: one-finger draw, Pencil, coalesced moves, two-finger scroll; switch modes midgesture; Escape/Cancel/Done/route change/blur/lost capture. Reopen and immediately draw; no stale pointer guard/crosshair/touch lock.
7. Feedback select/remove item/area, scroll and resize; stable source bounds; underlying click intercepted only in Item mode; Browse routes work and clean up.
8. Branchline drag pointer cancel/route change and keyboard alternatives; no capture/timer survives game cleanup.
9. Keyboard review/resolve/tabs/dialogs and rapid queued tour steps; stable focus successor, focus-visible and announcements. Test reduced motion both OS and app setting.
10. Add Class course field in Safari/iPad: OS personal-name autofill reproduction and released semantic fix; picker keyboard/AT/manual path. Setting autocomplete off alone is insufficient evidence.

Research owns external browser/UX evidence and final interaction recommendations. Source audit supplies bounded fault hypotheses and exact seams, not a device attribution or new product design.
