# Stuart Q-S11 — Slice 2 Professor Home / Multi-Course Independent Acceptance

**Lifecycle:** DONE  
**Timestamp:** 2026-09-30 19:05 ET  
**Disposition:** PASS within tested scope. Physical-device / hosted-origin / full-accessibility gates remain HOLD.

## Exact candidate
- `StudyGrid-CF0042-QB15-professor-home-scale.html`
- Drive `1CSN0jYJHnYbk2kpLAz8HNg4BSYELbe6U`
- SHA-256 `48b16df1c05b1a62cf7af174d3a48b3609ae79c2b39edfbe8c6046cbe48c46cf`
- 996820 bytes
- APP_VERSION / SG_R6_BUILD / registry build `v7.18-cf0042-qb15-professor-home-scale`

## Accepted parent derivation point
- General accepted Slice 1 pointer `routes/GENERAL_ACCEPTED_SLICE1_QB14.txt`
- Exact parent Drive `1S4eIU6VT2pnNQ4h5SHEGhJ3sWb7BLU6W`
- SHA-256 `fcf89e5a31063746272a10bbfba72d605f745d01f797c75fa33697923dde6bb1`
- 965519 bytes
- APP_VERSION `v7.17-cf0042-qb14-local-product-gateway`

Both provider files were freshly fetched and independently rehashed before acceptance testing.

## Independent result
**145 / 145 PASS.** The Q-S11P matrix/oracles were treated as preparation only; candidate behaviour was observed directly against the exact provider bytes.

### Professor Home / scale
- Exactly six deterministic course fixtures and 438 total students.
- Every course keeps explicit class name, code, section and term context.
- Class-section identity remains a separate `section` field; Slice 1 source/document identity remains `section_id` plus `source_revision_id`, `source_block_id` and `display_locator`. No class object was observed carrying source `section_id` semantics.
- Today returns four confirmed rows from the deterministic schedule; fixture current class is Police Powers and next is Provincial Statutes.
- Professor Home does not auto-navigate or steal class context. Search and sort remain on `#/workspace/instructor`; drill-in occurs only after explicit Open class activation.
- Unresolved attention initially contains four items only. Two resolved seed items remain in history. Resolving a local item removes it from live attention and preserves it in history.
- Course organisation controls persist pin/favourite/colour/label/sort through the gateway. An unowned extra field was rejected from persisted read-model truth.
- Colour is explicitly supplementary; class name/code/section remain visible identifiers.

### Date / weekday correctness
- Q-B15 changed text introduces no hard-coded weekday string pair.
- Slice 2 formatting uses `Intl.DateTimeFormat` / deterministic fixture timestamps.
- Fixture date `2026-09-30` independently resolves to Wednesday. Professor Home renders current-date schedule context as Today rather than a separately hard-coded weekday/date pair.

### Gateway / command / state preservation
- Existing Slice 1 gateway build remains `qb14-local-fixture-gateway-v1`; Slice 2 is exposed as `qb15-professor-home-v1` behind the same product boundary.
- Source inventory remains three records with complete section/source revision/block/display-locator identity.
- Assessment editor, instructor summary, student timeline and reminder/announcement delivery share one revision. Authorized save advanced all from `assessment-quiz2-r1` to `assessment-quiz2-r2`.
- Assessment command patching remained bounded; an extra field did not persist.
- Slice 1 stale and unauthorized assessment commands failed closed without mutation.
- Professor attention stale and unauthorized commands failed closed without mutation.
- Professor organisation stale and unauthorized commands failed closed without mutation.
- Deterministic assessment states `loading`, `empty`, `error`, `stale_revision`, `unauthorized` mapped to their expected command/read errors.

### R6 / Q-B13 regression preservation
- Component registry remains rev 11, 237 entries, 237 unique component IDs, with unchanged component-ID sequence; only build identity advanced.
- Student sort focus returns to `r6StudentSort`.
- Student filter focus returns to `r6StudentFilter`.
- Instructor roving tab ArrowRight moved Overview → Students.
- Source-policy dialog opened with focus inside and Escape returned focus to `r6InspectPolicy`.
- Assessment Confirm returned focus to `r6TaskCanvas` and preserved the settled nonzero scroll position after controlling for Playwright's own pre-click scroll-into-view behaviour.
- `sgR6PaintStudents`, `sgR6OpenDialog` and `sgR6CloseDialog` source remained byte-identical to Slice 1.

### Responsive / runtime
- Paper + Dusk × desktop 1440 + tablet 820 + phone 390 × Professor Home + selected-class drill-in all passed duplicate-ID and major-horizontal-overflow checks.
- Professor Home rendered all six course cards across all tested viewport/theme combinations.
- Runtime page errors: 0.
- Console warnings/errors: 0.
- External HTTP(S) requests: 0.

## Bounded diff conclusion
Exact Slice 1 → Slice 2 comparison produced **15 non-equal source-record hunks**. Changes were bounded to Slice 2 Professor Home/multi-course fixture/read-model/command/UI wiring, identity/build updates, component-registry build identity, and one extra settled-scroll restoration frame in the existing R6 overview refresh. Registry component IDs did not change.

No added `fetch(`, `XMLHttpRequest`, `WebSocket(`, `createClient(`, Supabase client, Blender, GLB, glTF or Three.js surface was found in the changed text. No Slice 3 setup/autofill implementation, Slice 4 enrolment implementation, deployment or canonical-promotion surface was accepted.

## Corroborating Bob evidence
Bob verification artifact Drive `1dD_bYpgUBk2wf46DDHKky_Hoy-EXwb1o` was independently hashed as SHA-256 `d8887d033296eb278450d74daed3377636c24576fdf2f8d93981741b3a917dcf`, 19250 bytes, and reports 133/133 PASS against the same exact Q-B15 candidate. It was corroboration only, not a substitute for Stuart's independent pass.

## Holds
Still HOLD without direct evidence: physical iPad/Safari/WebKit, VoiceOver, Apple Pencil / physical interaction, physical hardware keyboard, true 200% zoom, full WCAG, hosted-origin storage/cross-tab behaviour and real backend/provider/auth/Supabase truth.

## Result
**PASS — no correction required for Q-S11 within tested scope.** No product/runtime/backend/deployment/canonical mutation was performed by Stuart.
