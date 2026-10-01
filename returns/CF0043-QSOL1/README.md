# CF-0043 / Q-SOL1 exact-source return to General CF-0040

Status: DONE — source inspection and preparation only. Implementation feeder HELD until Nathan closes the owner-review batch and General publishes the reconciled release contract. Publication is not General consumption, owner acceptance, or worker activation.

## Evidence boundary

Inspected byte-for-byte: `StudyGrid-CF0042-QB15-professor-home-scale.html`, Drive `1CSN0jYJHnYbk2kpLAz8HNg4BSYELbe6U`, SHA-256 `48b16df1c05b1a62cf7af174d3a48b3609ae79c2b39edfbe8c6046cbe48c46cf`, 996820 bytes, APP_VERSION `v7.18-cf0042-qb15-professor-home-scale`. All line references below are 1-based lines of this HTML, including embedded scripts. They are not lines of an extracted/minified JS file. The final line is empty (3511 newline characters; 3512 split lines).

Four executable inline scripts parse successfully. The embedded component registry is data, not a fifth executable script. The extraction finds 553 named function/method declarations, 553 control opening declarations, 355 event-listener declarations, 37 explicit `nav`/history calls, 84 CSS rules involving cursor/selection/pointer/touch, and 237 registry entries. One additional non-native role-button span is explicitly inventoried in role-controls.json and appended as C0554 in the control ledger. Counts include superseded functions and template declarations; **they are not counts of live unique DOM controls**. Anchor href navigation and direct in-place state changes are separately covered by the control and handler inventories.

No browser/device reproduction was performed. No browser binary was available locally; none was downloaded. Source statements are deterministic source findings; Safari/iPad symptoms and appearance remain later QA. No external research, product HTML change, backend/auth/network integration, deployment, canonical promotion, owner-review closure or Bob/Stuart/Kevin wake occurred. The only repository changes in this isolated branch are audit documents and extraction/verification tooling.

## Read order and complete coverage

1. `CONTROL-INVENTORY.md`: semantic surface inventory and effective override map.
2. `TRANSITIONS.md`: actual route/state map and destination/focus findings.
3. `POINTER-SELECTION.md`: exact cursor/selection/capture/teardown audit and bounded device checklist.
4. `DELTA-MATRIX.md`: every product requirement from the three feedback packets, preservation requirements, Research holds and Stuart implications.
5. `BOB-FEEDER.md`: compact, held mutation seams; no design adjudication.
6. `control-ledger.json` + `handler-ledger.json`: full declaration-level evidence with current label/template, code owner, line, href/form/state handler, binding scope and callback body. These are the drill-down for each instance in a grouped semantic row. Automatic associations are marked as candidates, never proof of runtime binding.
7. `manifest.json`, `functions.json`, `handlers.json`, `controls.json`, `routes.json`, `stateWrites.json`, `cursorCSS.json`, `selectionCalls.json`, `registry.json`: raw source extraction, including legacy definitions so replacement seams remain inspectable.
8. `verification.json`: source integrity, parser coverage and isolated source-state checks. These checks do not prove browser behaviour.

## Principal findings

| ID | Source conclusion | Evidence and limit |
|---|---|---|
| F01 | Instructor routes retain the global learner shell. | Static Courses/Study/Profile at 1115–1129; `setGlobalNav` 2026 changes active markers, not role IA. Explicit role/demo switching is a separate local decoration, not authorization. |
| F02 | Instructor **All classes** opens a single fixed class instead of Professor Home. | `sgEnhanceInstructorShell` 3213 calls `renderInstructorWorkspace('pfp207-a','overview')`. Class/tab switches similarly rerender without updating the URL. |
| F03 | Label/colour editors and `Label: None` are continuously displayed. | `sgQB15CourseGridMarkup` 3422. Course organisation commands already provide the local mutation boundary. |
| F04 | Professor resolution has history but no undo command/control. | Gateway 3304–3343; attention markup/binding 3420/3426. Annotation undo exists separately and cannot be mistaken for professor undo. |
| F05 | Report close/route-close do not reset the active pointer state. | 1666/2112 call `clearReportMarkCanvas` 1668, which clears points/bounds/areas, not `drawing`, `reportCirclePointer` or `reportTwoFingerLastY`. No canvas `lostpointercapture` listener. Later pointerup/cancel can clean it; stale state is conditional, not a reproduced universal fault. |
| F06 | Annotation close leaves deferred selection work and cached range alive. | `closeAnnotationPopover` 2439 vs `captureAnnotationSelection` 2473; a still-connected cached range can reopen tools after outside-click close. Route close does not explicitly close this popover. |
| F07 | Explicit text cursor is bounded to annotatable text, not a body-wide cursor rule. | `.annotatable-text` 584–605 used in note bullets, lesson paragraphs and explanations (2242/2560/2385). Broad text coverage may feel intrusive; native Safari selection remains a device question. |
| F08 | Tour selection/highlight actions are one-way; tour theme samples are noninteractive. | `bindTourDemo` 1758–1789 opens tools/adds highlight, without second-press toggle-off. `tourVisualMarkup` 1750 renders Paper/Dusk as spans. Settings 2665 has pointer/keyboard-native theme buttons plus persistence/focus restoration; source handler presence does not close the owner Dusk defect. |
| F09 | Add Class still conflates repeated school context and seasonal term strings. | Effective `renderAddClass` 3405; aliases/datalists 1972–1982 and local class save. No profile institution/program IDs, program-term enum, linked catalogue course identity or join-code flow. |
| F10 | Practice summary routes to Profile. | `#seeTree` callback 2511 goes `/profile`; wrapper 3127 relabels it `View learning progress`. This is an exact possible Profile path, not proof of which flow Nathan encountered. |
| F11 | Resolve and note-review rerenders need focused QA. | 3426 focuses a section without tabindex; 2245 replaces the note DOM without explicit restoring focus. Do not add transition animation that obscures missing focus. |
| F12 | Final overrides matter. | Legacy welcome/add-class/tree/question implementations remain in the file but are replaced. Patch final renderers/wrapper seams, not the first matching function name. |

## Input provenance

Startup queue verified at `c86e77840529cdef772871722c37e5054fc8a8de`; exact task consumed at `9f94b1cd3067d9330ae09a4a76c34c3e7c75d6a8`. Full inputs read: owner batch OPEN; feedback 21:13, 21:23 and 21:47; Architecture Add Class adjudication 21:29; Gemini Selectric return and General AMEND 22:09. Exact fetched blob identities are in `input-provenance.json`. These inputs do not release implementation. No subsequent owner-batch closure is asserted. The required current startup Base/Active Corrections and CF-0043 registry row46 were independently verified before the STARTED claim.

## Direct return contract

General should consume the frozen return, reconcile it with Astra/Architecture/Research and later feedback, and release only an exact complete candidate contract after batch closure. Stuart should validate the released candidate rather than treat this source audit as acceptance. Research holds are intentionally unresolved. No new Sol task is invented after terminal return; the queue receives one final refresh.
