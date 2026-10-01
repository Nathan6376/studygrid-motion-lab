# StudyGrid — Stuart Q-S13RP Owner-Feedback Refinement Acceptance Harness

**Lifecycle:** PREP ONLY — no Q-B17R candidate is accepted or pre-approved by this artifact.

**Named downstream consumer:** future Stuart Q-S13R independent acceptance after Bob publishes an exact Q-B17R candidate and General explicitly releases that candidate to Stuart.

## Fixed source basis

- Accepted baseline: `StudyGrid-CF0042-QB15-professor-home-scale.html` / SHA-256 `48b16df1c05b1a62cf7af174d3a48b3609ae79c2b39edfbe8c6046cbe48c46cf` / 996820 bytes / `v7.18-cf0042-qb15-professor-home-scale`.
- General release: `routes/GENERAL_RELEASE_20261001_0030_OWNER_REVIEW_BUILD.txt`.
- Activated contract: `routes/HELD_IMPLEMENTATION_QA_RELEASE_20261001_OWNER_REVIEW.txt`.
- Sol exact-source audit commit: `4bd3a16e95aa344c730b5b2c18aa9b3614ff2462`, especially `DELTA-MATRIX.md`, `TRANSITIONS.md`, `POINTER-SELECTION.md`.
- Research Q-R3 terminal: `routes/RESEARCH_CF0044_20261001_0027_ADAPTIVE_CONFIDENCE_BEHAVIORAL_PRIVACY_DONE.txt`.
- Gemini motion is accepted only through General’s AMEND in `routes/GENERAL_ADJUDICATION_20260930_2209_GEMINI_SELECTRIC_MOTION.txt`.
- Screenshot regression evidence: `routes/OWNER_REVIEW_SCREENSHOT_EVIDENCE_20260930_2335.txt`.

## Execution contract

1. Before any candidate result is credited, recompute exact filename, bytes, SHA-256 and APP_VERSION and match General’s release.
2. Producer self-tests are corroboration only; Stuart must independently run the applicable gates.
3. Inherited Q-S11/QB15 evidence may be reused only for properties proven byte-unchanged; interaction-coupled or changed seams are rerun.
4. Static, visual, runtime and physical-device evidence are not interchangeable.
5. No backend/auth/Supabase/provider/deploy/canonical claim is permitted in this refinement acceptance.
6. Physical iPad/Safari, hardware-keyboard and VoiceOver items remain HOLD until actual device evidence exists.
7. No gate is PASS at prep time.

## Gate families

### G01 — Exact identity and lineage
- Match General-released candidate filename/SHA/bytes/APP_VERSION exactly.
- Verify derivation from exact accepted QB15 baseline, not a visually similar older HTML.
- Confirm edits hit Sol’s effective renderer/function chain rather than stale shadowed definitions.
- Reject unexpected backend/auth/network/deploy/canonical expansion.

### G02 — Instructor shell separation
- Instructor mode has intentional instructor navigation and does not inherit learner Study / Your Classes / learner continuation chrome.
- Feedback, Help and accessibility affordances remain reachable.
- Owner/admin capability is deliberate/context-switched, not ambient.

### G03 — Instructor routing/history
- All classes/current-class labels match their real destination.
- Class and tab switches update visible state, URL/history and reload/deep-link state coherently.
- Browser Back/Forward replays the displayed class/tab.
- Cross-class switches do not preserve stale focus/scroll just because workspace role is unchanged.
- Duplicate exits are reconciled to one clear hierarchy return.

### G04 — Professor Home preservation
- Preserve the accepted card hierarchy and truthful counts/search/sort/pin/favourite/Today/attention/history behaviour.
- No regression to generic/older card treatment.
- Paper and Dusk remain readable.

### G05 — Professor card editing
- Label and colour editing are behind explicit Edit.
- Default card omits redundant `Label: None`.
- Save/cancel preserves meaning and restores sensible focus.
- Accent/shine/lift remains restrained; colour is never sole meaning.

### G06 — Resolve + Undo/history
- Resolve moves the exact item to history once.
- Undo restores the exact item once using stable identity/revision, not list index guessing.
- Repeat/no-op/stale-token and multiple-resolve cases are deterministic and do not duplicate history.
- No backend/reload durability is claimed for local fixture state.
- Focus lands on a connected meaningful successor after Resolve/Undo.

### G07 — Visual clutter defects
- No unexplained pale arcs/lines/circles cross instructor question/cluster cards.
- No random bright-blue rectangular outline appears around noninteractive heading/hero copy.
- Do not “fix” either issue by deleting legitimate keyboard focus from interactive controls.

### G08 — First-run route split
- Fresh start offers two clear routes: class code OR school setup.
- Both are keyboard/touch operable and avoid questionnaire sprawl.
- Join-code path remains distinct from catalogue course identity and cannot fabricate enrolment.

### G09 — School context model
- Institution → program → program term is established once and reused.
- Program term is Term 1/2/3/4 + Other; Other has an explicit label.
- Academic session is separate/optional and old seasonal text is not destructively guessed into program term.
- Existing local classes/manual legacy strings survive migration.

### G10 — Catalogue/course picker truth
- Catalogue uses an approved local snapshot with source/version/last_verified provenance; no live scrape/network dependency.
- Search by title/code resolves one stable course identity; title/code cannot drift apart.
- Context may display `207` while preserving canonical `PFP207`/equivalent identity only where source-backed.
- Unknown programs/courses never get guessed prefixes.
- Manual fallback remains explicit and complete.
- Class-section/join identity stays separate from catalogue course identity.

### G11 — Add Class responsive/input behaviour
- Institution/program/term and course picker do not become overly wide/squeezed at tablet/narrow widths.
- No page horizontal overflow; touch targets remain usable.
- Combobox/search semantics remain keyboard/AT usable.
- **HOLD:** physical Safari/iPad personal-name AutoFill reproduction; `autocomplete=off` alone is not proof.

### G12 — Welcome hierarchy
- Slightly larger StudyGrid mark remains subordinate to the centred `Learn the class. Be ready for the test.` goal.
- Sign in is promoted ahead of secondary tour/start choices in visual and keyboard order.
- Returning-user novice guidance retires from demonstrated use, not arbitrary cookie/sign-in counts.

### G13 — Selectric/typeball motion
- Replace the three static explainer bars/cards with one coherent implied Selectric-like rotor/object.
- No visible globe/wireframe/tech-demo treatment and no heavy renderer by default.
- Motion uses compound spatial continuity, not slot-machine/carousel behaviour.
- Active phrase ends front-facing/crisp; competing faces do not dominate.
- No springy bounce, gratuitous 360 flourish or blur-heavy smear.
- Prototype angles/easing are not acceptance values.

### G14 — Selectric semantics/reduced motion
- Stable semantic text/list remains available independent of decorative moving text.
- Interactive controls are not hidden with `aria-hidden`.
- Autoplay, if present, pauses on interaction/focus and does not cause repeated announcements.
- Reduced motion becomes static/instant/minimal and remains fully understandable.
- **HOLD:** physical Safari/iPad CSS3D crispness/compositing.

### G15 — Student tour Next/help layout
- `Next` has clean spacing and one intentional border treatment; no accidental double-edge/halo.
- Keyboard focus remains visible when focused.
- `How this works` is contained/anchored and does not make unrelated text jump.
- Tour cards remain readable at narrow/iPad-like widths.

### G16 — Student tour selection/tools
- Target wording reads like normal lesson text, not a permanent fake link/underline.
- Ghost cursor performs one finite selection demo, then disappears on real pointer/touch/keyboard input.
- Explain produces contextual content.
- Highlight toggles reversibly via click/tap/Enter/Space with correct state/focus.
- Ask Teacher opens a realistic in-context demo composer and never implies a real send.

### G17 — Student tour example motion/copy
- Example-question changes are finite or user-controlled, not endless forced autoplay.
- Student-facing copy remains concise everyday English and does not expose implementation/privacy jargon.
- Rapid Next/Back/Skip cannot leave old content inert/frozen or delayed focus from a stale step.

### G18 — Practice confidence ordering
- Exact order: answer commit → optional confidence → correctness/correct answer/explanation → adaptive update.
- No correctness cue leaks before confidence choose/Skip.
- Confidence choices are Guessing / Fairly sure / Very sure; Skip is a separate secondary action.

### G19 — Confidence semantics/privacy
- Skip is missing confidence, never low/Guessing.
- Disabling confidence removes the step without breaking study/adaptation.
- Confidence is real but non-authoritative; it cannot independently mark mastery or override correctness/history/spacing.
- No invented weighting/spacing formula.
- Timing/dwell/revision counts/pointer-directness are not production adaptation inputs.
- No fine-grained raw pointer/velocity/keystroke tracing is retained or transmitted for adaptation.
- Instructor-facing adaptation reasons are human-readable pedagogic facts, not surveillance traces.

### G20 — Practice reveal hierarchy
- Correctness is explicit text, not colour alone.
- Wrong answer clearly separates `Your answer` from `Correct answer` before explanation.
- Correct state is compact and unambiguous.
- Confidence/reveal controls wrap/stack cleanly on narrow widths with usable touch targets.

### G21 — Instructor demo truth
- Instructor demo runs in the real fake-data instructor shell with persistent Demo/Example-data context.
- Guided steps point at real controls/core loop; Skip stays discoverable; Replay is reachable from Help.
- Completion/Skip returns to the demo shell with a setup CTA and never silently converts fake data into live data.
- `Find current class` explains its known-context basis and permits correction.

### G22 — Adaptive response demonstration
- Student-question and instructor-response cards stay structurally stable while the question changes.
- Only materially changed response phrases animate/emphasize StudyGrid green, then settle.
- Unchanged response text does not rebuild/slide wholesale.
- Changed-state emphasis is not colour-only.
- Reduced-motion path still communicates the change without theatrical motion.

### G23 — Dusk/theme showcase
- Reproduce the exact owner-tour Dusk target; pointer and keyboard can operate it; handler presence alone is not PASS.
- Eligible first-run showcase performs Paper → Dusk → Paper once, then leaves Paper unless user explicitly chooses otherwise.
- Target zero flash/strobe events.
- Reduced-motion removes large spatial/3D/theatrical changes.
- Both themes remain readable on welcome/tour/practice/Professor Home/instructor demo/Help/Feedback.

### G24 — Interaction-state language
- Keyboard focus is visually distinct from hover, pressed, selected/active, tutorial target, adaptive-changed text and saved highlight.
- Noninteractive hero copy never looks like a focused form control.
- Tutorial target decoration does not replace keyboard focus.
- Adaptive changed-text emphasis and saved learner highlight remain distinguishable without colour alone.

### G25 — Report pointer-capture teardown
- Starting a report-circle gesture then closing/routing/Escape before pointerup cannot leave stale drawing/pointer/capture state.
- Reopen immediately and draw again successfully.
- pointercancel/lostpointercapture/blur/two-finger scroll/mode switch all converge on one safe reset.

### G26 — Deferred annotation teardown
- Close/outside/Escape/context switch before the 80/520ms deferred callback cannot resurrect annotation UI from cached range.
- Highlight hold timer cannot fire after route/cancel.
- Saved annotations remain intact while ephemeral timer/cache/pending state is invalidated.

### G27 — Native selection/input preservation
- Annotatable text remains natively selectable on desktop; no body-wide `user-select:none`/cursor workaround.
- Direct Study-tab paints also run required cleanup/focus logic.
- **HOLD:** physical iPad touch/Pencil selection, native handles and feedback gesture interaction.

### G28 — Feedback surface
- Feedback hover/focus geometry is compact and deliberate, not a rectangular green box.
- Progressive capture is privacy-bounded and cancel/reopen leaves no stale capture state.
- No false claim that local/demo feedback was remotely sent.

### G29 — Help/privacy/legal
- Help contains: How StudyGrid works; Replay tour; Accessibility & input help; Send feedback.
- Privacy & data and Legal are separate destinations.
- No claim of legal-completeness/compliance that the local prototype cannot support.

### G30 — Screenshot regression set
Recreate equivalent states for all six preserved screenshots:
1. IMG_1622: no large pale arc/circle over question cluster; stable base for adaptive response.
2. IMG_1623: practice card no longer compressed; answer/confidence/reveal hierarchy scans clearly.
3. IMG_1624: no Next double-outline in pointer-normal state; focus still visible on keyboard focus.
4. IMG_1621: no bright-blue rectangle around noninteractive instructor-tour heading.
5. IMG_1618: stable question/response two-card composition remains.
6. IMG_1617: normal lesson text + finite ghost selection + real mini Explain/Highlight/Ask Teacher behaviour.

### G31 — Inherited QB15 product regression
- Preserve accepted gateway/error/revision semantics unless the release explicitly changes them.
- Re-run selected-class workspace, Students action-first truth, neutral roster/detail, Tree→Study handoff, practice/assessment reveal, Profile truth, Study Sets revision/publication truth, feedback recovery and local/demo truth.
- Do not infer unchanged behaviour merely because a surface looks similar.

### G32 — Responsive regression
- Check at representative 320/390/820/1024 widths in Paper/Dusk.
- No document horizontal overflow on changed surfaces.
- No visible touch target below 44px where prior contract requires that floor.
- Instructor cards, Add Class, tour, confidence controls and Help/Feedback remain usable.

### G33 — Runtime cleanliness
- Zero unexpected page errors/console errors across changed owner-review flows.
- No unapproved external HTTP(S) dependency introduced.
- Local/demo truth remains honest; no backend/provider capability is implied by UI copy.

### G34 — Keyboard/accessibility regression
- Changed controls have semantic names/states and coherent tab order.
- Keyboard can execute every changed interactive action.
- DOM replacement restores focus to a connected meaningful successor.
- Reduced-motion path covers welcome rotor, tour, theme, adaptive response and mark-reviewed transitions.

### G35 — Physical iPad/Safari matrix — HOLD
Must be run later on the exact accepted candidate and record iPadOS/Safari, viewport/orientation and input mode. Required cases: Dusk hit target, Add Class AutoFill/combobox, native text selection, Pencil/touch report gestures, pointer capture/cancel/reopen, CSS3D text crispness, rotation/background-return and responsive overflow. Source or emulation evidence cannot convert this family to PASS.

### G36 — Physical hardware-keyboard / VoiceOver matrix — HOLD
Must be run later on the exact candidate. Verify instructor/student shell navigation, tour/tools, Add Class, practice confidence, dialogs/feedback, rotor semantic stability, focus-visible, announcements and no repeated moving-text chatter. Desktop/emulated accessibility checks may support but not replace this hold.

## Q-S13R terminal vocabulary

- **ACCEPT:** every applicable non-held release gate passes on the exact General-released bytes; any remaining physical-device holds are explicitly unclaimed.
- **AMEND-HOLD:** candidate is testable but one or more released requirements fail or lack sufficient evidence.
- **BLOCKED:** exact candidate/release identity or required evidence is unavailable before a meaningful result can be formed.
- **REJECT:** a release blocker is materially violated and the candidate needs refinement before another acceptance pass.

This harness does not mutate StudyGrid and does not itself release Q-S13R.