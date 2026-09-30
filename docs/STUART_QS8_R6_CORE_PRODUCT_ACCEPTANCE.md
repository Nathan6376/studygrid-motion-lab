# StudyGrid Q-S8 — Independent R6 Core Product Acceptance

**Worker:** Stuart  
**Coordinator:** ChatGPT General CF-0040  
**Date:** 2026-09-30  
**Disposition:** **DONE — FAIL (bounded keyboard/focus defect family); all other tested owner-release families PASS; real-device/hosted accessibility family HOLD**

## Acceptance basis

This acceptance is intentionally limited to the instructor-first slice Nathan approved for bounded implementation at 15:22 ET on September 29. Later professor-scale scheduling, multi-course organisation, class-code enrolment, broader architecture, teaching-mode and brand/motion work are not retroactive requirements and were not used to fail R6.

Authoritative release inputs:

- Exact accepted R5: Drive `1Zp8rAflaLBN-F-5_i8B9P1hF-XR-oJHC`, SHA-256 `0fee828511bdccd373fdc0625c0ea9f894485a57f6e6cbceff74e2652ec34d00`, 874986 bytes.
- R6 owner-release route: `1WgEnlzAJI4bf4USDdOSu5nqn_0kPUvTtCTUR4jdlfYQ`, specifically **OWNER QA RELEASE — 2026-09-29 15:22 ET**.
- Product/validation direction: `1FQqt2rx2IF1uF-0cU6Qblyu83ESB5ywnVu1nq1_fx5E`, specifically **OWNER QA — 2026-09-29 15:22 ET**.
- Implementation spec: `1aXh8z0yicgBVTjhsvvv7U_HzsIyUN95ogFcrrRYOGhk`, specifically **OWNER QA RELEASE / IMPLEMENTATION AMENDMENT — 2026-09-29 15:22 ET**.

## Exact R6 identity — PASS

Provider-downloaded bytes independently verified:

- `StudyGrid-CF0032-integrated-batch4-8-cf0039-r6.html`
- Drive `1pxKsdqM6dhKE6ihN5k4UgO-0usgNBmjD`
- 954208 bytes
- SHA-256 `875a81262d80cf33ceb32545ff20c1cbc03ae91db34c66a3a8a679f93f0314ef`
- APP_VERSION `v7.16-cf0032-integrated-batch4-8-cf0039-r6`

R5 was independently re-downloaded and rehashed to its accepted identity as the comparison baseline.

## Independent acceptance matrix

| Requirement family | Result | Independent evidence |
|---|---|---|
| Exact identity / static integrity | PASS | Exact size/hash/version; 104/104 static DOM IDs unique; all four executable inline scripts parse under `node --check`; registry JSON excluded from executable-JS parse; no external script dependency. |
| Registry integrity | PASS | Registry rev 11, 237 entries / 237 unique component IDs. R5 remains rev 10 / 218 unique. |
| Instructor shell / Clear Desk | PASS | Six compact selected-class destinations; initial unresolved queue is assessment + questions; confirming assessment removes its live item while preserving history; resolving question exception empties queue and produces calm caught-up state with history retained. |
| Assessment Desk / source proof / timing | PASS | Proposal-only review, manual fields, source proof to `syll-f26-r3` assessment schedule page 4, separate assessment/open/close/practice/reminder/announcement timing, confirmation clearly separate from publish/release/notify. |
| AI source policy / Sources safe rebase | PASS | Policy modal exposes exact approved revisions `syll-f26-r3`, `ch4-r7`, `notes-0917-r2`; official-authority mode explicitly not configured; no silent open-web claim; Sources shows Ready / Needs review / Conflict, review-before-apply and unsupported abstention while retaining prior source tools. |
| Repeated-question answer-once flow | PASS | Jordan/Aaliyah/Marcus originals preserved; shared draft marked NOT SENT; exact answer/source revision support; unsupported Marcus exception remains unresolved until separate instructor action. |
| Student preview / resolution / sorting | PASS | Timeline plus Fact / Recommendation / Unknown; answered/still-need-help feedback changes the instructor queue without grade/mastery/risk inference; Name/Open questions/Questions needing a reply sorts work and show transparent reasons. |
| Responsive / bounded runtime | PASS | 30/30 Paper+Dusk × 1280/1024/820/390/320 × Overview/Students/Sources cases with zero page-level horizontal overflow, zero bounded console/page errors and zero external HTTP(S) requests. 320px tabs remain a compact horizontal row. Reduced-motion and coarse-pointer contexts remain functional. |
| R5-preserved regression | PASS | Deterministic StudyGrid fixture suite 6/6; runtime duplicate-ID sweep 6/6 representative routes; previous Bob evidence artifacts independently rehashed to their recorded digests but not treated as sole acceptance evidence. |
| Keyboard / focus basics | **FAIL** | Two release-scope focus defects independently reproduced; details below. |
| Physical device / hosted-origin / full accessibility | HOLD | Physical iPad/Safari/WebKit, VoiceOver, Apple Pencil/physical feel, physical keyboard, true 200% zoom, full WCAG and hosted-origin cross-tab behaviour remain unverified. These are gaps, not demonstrated product defects. |

## Concrete defects

### QS8-F1 — Students sort/filter repaint loses keyboard focus

**Requirement:** in-place controls preserve focus/scroll and should not unexpectedly remove the user’s interaction context.

**Reproduction:** Instructor → Students → focus `#r6StudentSort` → change Name to Open questions. The change handler calls `sgR6PaintStudents(...)`, replacing the pane. After the repaint, `document.activeElement` is BODY/no meaningful element instead of the sort control.

**Impact:** a keyboard user loses interaction context after an ordinary in-place sort change.

### QS8-F2 — Assessment resolution focus target is not focusable

**Requirement:** resolution flow should preserve meaningful focus when the triggering control is removed.

**Reproduction:** Overview → Review quiz → focus/click `#r6ConfirmAssessment`. The page correctly keeps the same `scrollY`, but `sgR6RefreshOverview(chosen,'r6AttentionTitle')` attempts to focus `#r6AttentionTitle`, which is a plain non-focusable `<h4>`. Focus therefore falls to BODY/no meaningful id.

**Impact:** keyboard focus is lost after resolving the assessment attention item.

Positive keyboard evidence is otherwise good: selected-class tabs support ArrowRight roving focus/selection; the source-policy dialog moves focus into the dialog, Escape closes it, and focus returns to `#r6InspectPolicy`.

## Runtime method and limit

This environment blocks direct `file://` Chromium navigation with `ERR_BLOCKED_BY_ADMINISTRATOR`. I did not bypass that restriction. Independent browser checks therefore loaded the **exact provider-downloaded R6 HTML bytes** into Chromium with `page.set_content(...)` for a local/in-memory runtime. This proves the bounded DOM/JS/responsive behaviour reported above, but does **not** prove hosted-origin storage/cross-tab behaviour, real Safari/WebKit/device behaviour or full assistive-technology conformance.

## Evidence-integrity cross-check

Bob’s prior evidence was retrieved and independently rehashed:

- Static/registry QA SHA-256 `146bbee584f7211e7aa4e6d8401b7cb1816689c7e9df962485ad3f6e6dd73208` — match.
- Targeted QA SHA-256 `54b5af9296eeea8de3e8a30cc74b9681a35b3cfaf9901e5946ab1d08dec4a945` — match.
- Regression QA SHA-256 `f45c4631851fd90f2489a2dd4b1093f5673c6106e6515b36b628913d76dfbc31` — match.

Those files support Bob’s own test claims, but this Q-S8 disposition comes from Stuart’s independent checks above.

## Smallest corrective route

A bounded Bob R6 focus repair is sufficient; do not redesign product architecture:

1. After Students sort/filter repaint, restore focus to the initiating select/control with `preventScroll`.
2. After an attention item is resolved and its button disappears, move focus to a deliberately focusable persistent target (for example a heading given `tabindex="-1"` or the next live action/caught-up container) without changing scroll position.
3. Produce new exact non-canonical bytes, then Stuart reruns the two focus regressions plus compact static/runtime/responsive smoke.

No R5/R6 file was mutated by Stuart, no backend/auth/Supabase/deployment action occurred, no canonical promotion occurred, and the animation/A-C lane was untouched.
