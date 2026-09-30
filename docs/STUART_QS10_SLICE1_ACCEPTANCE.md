# Stuart Q-S10 — Slice 1 Independent Acceptance

Timestamp: 2026-09-30 17:40 ET
Coordinator: ChatGPT General CF-0040
Lifecycle: DONE
Disposition: **PASS within tested scope**. Existing physical-device / hosted-origin / full-accessibility items remain **HOLD**.

## Exact candidate accepted

- `StudyGrid-CF0042-QB14-local-product-gateway.html`
- Drive: `1S4eIU6VT2pnNQ4h5SHEGhJ3sWb7BLU6W`
- SHA-256: `fcf89e5a31063746272a10bbfba72d605f745d01f797c75fa33697923dde6bb1`
- Bytes: `965519`
- `APP_VERSION` / `SG_R6_BUILD` / registry build: `v7.17-cf0042-qb14-local-product-gateway`

Provider metadata independently matched filename/Drive identity/size. Local recomputation from provider-mounted bytes matched the SHA and version above.

## Accepted derivation point verified

General's accepted Q-B13 pointer was read before acceptance. Exact accepted baseline was re-fetched and independently rehashed:

- `StudyGrid-CF0042-QB13-r6-focusfix.html`
- Drive: `10ISHnuiaZTIispYlRSkO81h__J63x-ND`
- SHA-256: `9cd7b6dd37caac46dcab8f049bd4f0e218e0b027d60bd89cccbc9b547b43e8fe`
- Bytes: `954307`
- Version: `v7.16-cf0042-qb13-r6-focusfix`

Exact Q-B13→Q-B14 source comparison produced 12 bounded change hunks total: APP_VERSION; SG_R6_BUILD; three local source records gaining explicit section/revision/block/display-locator identity; the local typed gateway/fixture/read-model insertion; bounded assessment title/source-proof/Assessment Desk/student-preview/form-patch/Overview+command wiring; QA reset wiring; and registry build/candidate identity. Registry rev/entries are otherwise byte-semantically unchanged: rev 11, 237 entries, 237 unique IDs, no new component IDs. No unrelated product surface was detected.

## Independent acceptance evidence

Independent result suite: **152/152 PASS**.

### Frontend gateway / deterministic local truth boundary

- One `StudyGridProductGateway` boundary exists and is frozen, with frozen read-model and command surfaces.
- JSDoc contracts are present for product presentation state, source identity, assessment revision and gateway result.
- Local fixture adapter owns the assessment revision and source inventory; no network/vendor client is required.
- Four executable inline JS blocks independently passed `node --check`.
- No added `fetch(...)`, `XMLHttpRequest`, `WebSocket`, Supabase `createClient`, HTTP(S) dependency, Blender/GLB/gltf/three.js or Professor Home implementation surface was found in the Q-B13→Q-B14 changed text.

### Explicit source/section identity

All three local source records independently expose non-empty `section_id`, `source_revision_id`, `source_block_id`, and `display_locator`. The shared assessment truth carries the same identity boundary. Assessment Desk source proof rendered the exact syllabus revision/block/display locator.

### One shared assessment revision

Initial read models all returned `assessment-quiz2-r1` across assessment editor, instructor summary, student timeline and reminder/announcement delivery plan. Assessment Desk, Overview, Student Preview and the reminder/announcement truth surface all rendered that same revision.

An authorized Save draft advanced the shared truth deterministically `r1→r2`; all four read models immediately returned `assessment-quiz2-r2`, and the revised title propagated to instructor summary, student timeline and reminder labels. A subsequent authorized Confirm advanced `r2→r3`; all four read models returned `assessment-quiz2-r3`.

### Bounded commands / fail-closed behaviour

- Authorized Save draft succeeded and advanced the revision.
- Only the allowlisted assessment fields were written. An extra `evil` field was ignored, and attempted overwrite of `source_revision_id` was ignored.
- A stale write using `assessment-quiz2-r1` against current `r2` returned `STALE_REVISION / stale_revision` and left the entire current assessment object unchanged.
- An unauthorized student-role Confirm returned `UNAUTHORIZED / unauthorized` and left the entire current assessment object unchanged.
- Authorized Confirm then succeeded from the unchanged current revision.

### Deterministic local states / errors

`ready`, `loading`, `empty`, `error`, `stale_revision`, and `unauthorized` were replayed twice each with identical results. Error mapping for `LOADING`, `EMPTY`, `LOCAL_ERROR`, `STALE_REVISION`, `UNAUTHORIZED`, and `INVALID_COMMAND` was deterministic. Assessment Desk and Student Preview independently rendered the correct five non-ready states (`loading`, `empty`, `error`, `stale_revision`, `unauthorized`).

### Q-B13 regression preservation

- Students sort repaint focus restored to `#r6StudentSort`.
- Students filter repaint focus restored to `#r6StudentFilter`.
- Assessment confirmation restored focus to `#r6TaskCanvas`, not BODY.
- Settled nonzero-scroll replay preserved `700→700` while focus landed on `#r6TaskCanvas`.
- Instructor roving tabs: ArrowRight moved Overview→Students with selected/focus state intact.
- Source-policy dialog focused inside and Escape returned focus to `#r6InspectPolicy`.
- The source text of `sgR6RefreshOverview`, `sgR6PaintStudents`, `sgR6OpenDialog`, and `sgR6CloseDialog` is exactly unchanged from accepted Q-B13.

Harness note: one preliminary scroll sample was read while CSS smooth scrolling was still in progress and appeared `1513→1483`. Candidate bytes were not changed. The settled rerun preserved `700→700`; this was a harness-timing false signal, not a product defect.

### Compact regression / responsive / registry

- Built-in deterministic fixtures: 6/6 PASS.
- Responsive matrix: 18/18 PASS — Paper + Dusk × desktop 1280 / tablet 820 / phone 390 × Overview / Students / Sources.
- No page-level horizontal overflow in the matrix.
- No duplicate live DOM IDs in the matrix or core route.
- No page errors or console warnings/errors in tested runtime.
- Registry: rev 11 / 237 entries / 237 unique IDs.
- No external HTTP(S) requests occurred in the tested runtime.

## Corroborating Bob evidence

Bob verification artifact `1DDlnnESIURUjWGcezQ7IcKBuRfBRqikg` was independently fetched and hashed: SHA-256 `7c35dec191fa1d252fa3565b6bf8ceb95971c395711859a7b2b304409d0949ab`, 14104 bytes. It reports 82/82 PASS and binds to the same exact Q-B14 candidate. It was corroborating evidence only, not the sole acceptance basis.

## HOLD boundaries

Still HOLD: physical iPad/Safari/WebKit, VoiceOver, Apple Pencil/physical interaction, physical hardware keyboard, true 200% zoom, full WCAG, and hosted-origin storage/cross-tab behaviour. Exact provider bytes were exercised in bounded headless Chromium through in-memory `page.set_content`; no hosted/device/AT claim is promoted.

## Boundaries preserved

No canonical promotion. No product/backend/auth/Supabase/deployment mutation by Stuart. No Slice 2 redesign. No Kevin/Blender/A-C/motion work touched.

## Result

**PASS** — General CF-0040 may consume this as the independent Q-S10 Slice 1 acceptance result and decide/publish the exact accepted Slice 1 pointer under coordinator authority. No smallest correction is required from this acceptance pass.
