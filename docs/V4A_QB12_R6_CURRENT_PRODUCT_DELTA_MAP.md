# StudyGrid V4A — Q-B12 R6 → Current Product Delta Map / Next-Candidate Decomposition

**Worker:** Bob / CF-0042  
**Coordinator:** ChatGPT General CF-0040  
**Status:** DONE — analysis/decomposition only; no product candidate mutation  
**Source baseline:** exact R6, read-only  

## Exact baseline verified

- File: `StudyGrid-CF0032-integrated-batch4-8-cf0039-r6.html`
- Drive: `1pxKsdqM6dhKE6ihN5k4UgO-0usgNBmjD`
- SHA-256: `875a81262d80cf33ceb32545ff20c1cbc03ae91db34c66a3a8a679f93f0314ef`
- Bytes: `954208`
- APP_VERSION: `v7.16-cf0032-integrated-batch4-8-cf0039-r6`
- R6 remains a verified non-canonical candidate. R5 remains preserved. Stuart Q-S8 is the independent R6 product-acceptance gate; Q-B12 does not promote either candidate.

## Authority / source set consumed

1. Current product direction: `1FQqt2rx2IF1uF-0cU6Qblyu83ESB5ywnVu1nq1_fx5E` — Instructor-First Product / Validation Direction — CURRENT, including owner deltas through Brand Portal Motion V2.
2. R6 implementation authority chain: `1aXh8z0yicgBVTjhsvvv7U_HzsIyUN95ogFcrrRYOGhk` — Instructor Validation Prototype → Implementation Spec, including the 15:22 owner release and later professor-scale re-hold.
3. Professor-scale research: `1-sNPmqHfRZcMGqaRY-X68OnXf8EqPxXvQGo9Sd1Dk4w`.
4. Professor-scale owner-QA design: `1pueJ2OhQoiS0UJY4CgcxgEd6nVQe-n8d` / `StudyGrid-Professor-Scale-Design-V3.html`, exact SHA-256 `860d3ec9b23d0c0d36fe92798d8ffe7c4d22364e21ff9ec097c1d1e3c50e7433`. Current product direction records Nathan’s 17:40 positive acceptance of V3 overall, with the brand-motion correction separated from the product workflow.
5. Accepted backend/architecture direction: `1KITiujdYWa3Ku1wT8ss0X10tx2z4wc0QDlU9nS-jDSI` — B-prime relational/modular-monolith direction, accepted in principle by Nathan at 18:36; material backend implementation remains held.
6. Exact R6 frontend↔backend seam audit: `14DjcMYUKtFZws49hM9xS78UZ-3MFBE5YAygA69QqpJE`.
7. Evidence/efficacy owner-QA packet: `1t_UCQaH5waVPlAKauJWG0Di5O1GQpJ75Ns6Cj3r4upc` — still owner-QA HOLD for its public evidence-system design.
8. Privacy/product-intelligence/upload/AI research: `1_tkZcGIcFc-wkQfLfPIkiuZtuoDP5oNTKKuxUJoK6b0` — research/design input, not a backend release.
9. General product-track resume lifecycle: `RT-20260930-1410-CF0040-STUDYGRID-PRODUCT-TRACK-RESUME`.

## What R6 already establishes and should be preserved

R6 already implements the owner-released instructor-first validation slice with local/example state: selected-class Instructor Overview; live unresolved `Needs your attention`; source proof and exact source-policy inspection; Assessment Desk; distinct assessment/open/close/practice/reminder/announcement concepts; repeated-question grouping/review/shared-answer flow; student preview; explicit `answered` / `still need help`; transparent Students sorting/filtering; local history/caught-up treatment; and no claim that backend/live AI/deployment is connected.

These are baseline behaviours, not post-R6 deltas. The next product candidate should preserve them unless Q-S8 identifies a concrete R6 defect.

---

# Delta classification

## A — owner-approved/released and safe for bounded next-candidate implementation

### A1. Professor-scale Instructor Home / multi-course organization
**Authority:** owner 15:53 delta + V3 accepted overall at 17:40.  
**R6 gap:** R6 remains selected-class oriented; it does not provide the accepted cross-course professor home.

Buildable behaviour:
- `Today / Now & next` from confirmed teaching schedule, without auto-opening or stealing context.
- Cross-course `Needs your attention`, unresolved-only.
- Current-term class library with visible class name/code/section and student/open-question context.
- Optional favourite/pin/colour/label and transparent alternate sorting; colour is never the sole identifier.
- Preserve R6 selected-class workspace as the drill-in destination.

Acceptance:
- Six-course / hundreds-of-students fixture works without long-scroll dashboard clutter.
- `Today` never auto-navigates.
- Resolved items disappear from live attention and remain represented in history/audit fixture state.
- Class identity remains explicit without relying on colour.

### A2. Set-up-once term/course defaults + review-by-exception
**Authority:** owner 15:53 + V3 accepted overall.  
**R6 gap:** no persistent term-default/schedule workflow.

Buildable behaviour:
- Enter/confirm class meeting pattern once.
- Save course defaults for assessment timing/preparation/reminder/announcement behaviour.
- Apply confirmed defaults across the term.
- Summarize what is ready versus what requires instructor action instead of presenting one form per assessment.
- Stop on ambiguity/conflict and ask one targeted question.

Acceptance:
- Fixture can represent the V3 pattern: multiple detected assessments, most resolved automatically from confirmed inputs, exceptions isolated for review.
- Changing one assessment does not silently rewrite course defaults.
- No inferred fact is promoted as confirmed truth without its visible basis.

### A3. Human-readable timing + distinct timing semantics
**Authority:** owner 15:53 + V3 accepted overall.  
**R6 gap:** R6 preserves distinct timing concepts, but its primary editors are raw browser date/time/datetime-local controls and local strings rather than the accepted human-first presentation.

Buildable behaviour:
- Human-readable date/time is primary surface (`Wednesday, October 8 · 10:00 AM · during your scheduled class`-style language).
- Exact calendar/time controls remain available for editing.
- Assessment, opens, closes, practice release, reminder and announcement remain distinct.
- Relative rules are visible in plain language.
- Approval/confirmation remains separate from release/delivery.

Acceptance:
- No raw ISO/machine-like string is the primary professor-facing timing surface.
- One change propagates consistently to every fixture view consuming the same assessment revision.
- Confirmation never implies publish/send.

### A4. Source-aware assessment autofill + bounded automation explanation
**Authority:** owner 15:53 + V3 accepted overall.  
**R6 gap:** R6 has assessment fields and static provenance examples but not the accepted set-up-once evidence/default hierarchy.

Buildable order:
1. explicit syllabus fact;
2. confirmed class timetable;
3. approved course-material structure;
4. instructor-confirmed course defaults;
5. prior confirmed pattern offered for reuse, never silently applied as new truth.

Acceptance:
- Auto-filled/defaulted values expose why they were chosen.
- Missing/ambiguous/conflicting facts produce a bounded instructor question instead of a guess.
- Manual entry always remains available.

### A5. Large-roster professor workflow
**Authority:** owner 15:22 + 15:53 + V3 accepted overall.  
**R6 gap:** R6 proves transparent sorting/filtering against three hardcoded students; it does not yet prove hundreds-scale navigation.

Buildable behaviour:
- Search.
- Section/group filters.
- Sort/filter by name, open questions, needs reply and other concrete observable action states.
- Every attention ordering exposes its reason; no risk/readiness score.

Acceptance:
- Hundreds-row fixture remains usable by search/filter rather than manual scanning.
- No drag ordering and no opaque ranking.
- Existing R6 answered/still-needs-help semantics remain explicit workflow feedback, not mastery.

### A6. Instructor-managed enrolment UX as fixture behaviour
**Authority:** owner 15:53 + V3 accepted overall.  
**R6 gap:** no join-code/invite surface.

Buildable frontend-only behaviour:
- Short section join code.
- Invite link/email entry points.
- Reset/disable affordances.
- Student confirms course/section before the fixture marks the join complete.
- Section identity is visible.

Acceptance:
- Clearly labelled prototype/local behaviour; no claim of real authorization, email delivery or persistence.
- Code never implies instructor privilege.
- Reset/disable state can be exercised deterministically in fixture tests.

### A7. Preserve accepted R6 interaction architecture while applying professor-scale deltas
**Authority:** 15:22 owner release + 17:40 V3 acceptance.  
**Requirement:** next product work must extend—not replace—the accepted Instructor Overview, Assessment Desk, repeated-question flow, Students workflow, student preview/timeline, source-proof inspection and human-language task grammar.

### A8. Frontend typed gateway + local fixture adapter as reversible implementation foundation
**Authority status:** the owner accepted the B-prime architecture direction in principle at 18:36 and delegated reversible standards-aligned implementation details unless they cross the escalation boundary. The exact adapter shape is an implementation decision, not a claim that Nathan personally approved a particular interface name or backend API.  
**Seam-audit recommendation:** introduce the typed gateway and local fixture implementation before Supabase so the frontend proves its component/API seams without connecting a backend.

Buildable now, frontend/local only:
- One typed product gateway boundary with a deterministic local fixture implementation.
- Authoritative-domain fixture state (section/course/source/assessment/question/delivery) behind the gateway; theme/motion/tab/modal/demo state can remain local UI state.
- Read-model-shaped fixture outputs carrying explicit status/reason fields instead of UI recomputing authoritative truth from ad-hoc booleans.
- Explicit opaque section identity throughout relevant fixture objects.
- `source_revision_id` / `source_block_id` + display locator for proof identity.
- One assessment revision consumed by Assessment Desk, student timeline and reminder/announcement views.
- Central loading/empty/error/stale-revision/unauthorized presentation states and command-error mapping before network latency exists.

Acceptance:
- Zero Supabase/auth/network dependency.
- View/render code no longer owns authoritative-domain mutations directly for the migrated slice.
- Existing R6 user-visible behaviours remain reproducible from local fixtures.
- No vendor lock-in and no provider-specific API contract is introduced.

---

## B — owner requirements whose visual/interaction treatment still needs owner QA

### B1. Cross-section reusable-asset adoption UI
Owner requires approved sources/templates/study sets/answer assets to be reusable across same-course sections while rosters, schedules, student records, questions, grades and delivery history remain isolated. The product rule is approved; the actual browse/adopt/revision-conflict interaction has not received a finished owner-QA surface. Keep it out of the first candidate slice except for section-safe data/interface seams.

### B2. Polished upload/source-ingestion UX
Owner explicitly requires upload to feel seamless and designed—not like a raw browser file control—with drag/drop/select/progress/review and clear errors. The precise visual/interaction flow is not yet owner-QA approved. Real scanning/parsing is separately blocked under D.

### B3. Privacy/transparency product surface
Owner requires understandable data use, minimum collection, no hidden profiling and inspectable trust. Exact student/instructor privacy-control and disclosure surfaces are not yet an accepted product design. Do not invent them inside a build.

### B4. Teaching-style flexibility as a future product requirement
Owner wants StudyGrid to support materially different professor teaching styles through one shared Course Truth / Teaching Workflow system. The requirement is real, but the visible mode architecture has not passed design/owner QA. Do not bolt a mode selector onto the current product without that gate.

### B5. Short/non-blocking normal-login brand treatment
Owner has specified that normal login must be materially shorter than the full tutorial portal and must never delay a ready interface. Its exact final interaction belongs with the active brand/motion design lane, not this product build.

---

## C — research/architecture recommendations not yet approved as product implementation

### C1. Public evidence experience
The proposed `Mechanism Map → Evidence Ledger → Open Research Registry` system and `How StudyGrid Works` design remain owner-QA HOLD. The claim/evidence discipline is useful as a constraint; the public page/system itself is not released for Bob implementation.

### C2. Specific teaching-mode candidates
`Talk / Lecture`, `Present / Screen`, `Live Check` and `Student-paced` are explicitly research/design candidates only. No current MVP release.

### C3. Detailed product-intelligence / benchmark system
Purpose-tagged event plane, external aggregate benchmark products, cohort suppression, anti-differencing and possible differential privacy are research/architecture recommendations. The durable owner constraints—no selling identifiable learner data, no opaque learner profiling, minimum-purpose collection—still control, but the full analytics product is not current build scope.

### C4. Source-revision re-review rule
Architecture recommends preserving approval only when cited support bytes/context remain unchanged and forcing re-review when support changes/removes. Exact context-window/rebase behaviour still needs design/testing; do not invent it in the next candidate.

### C5. Exact pilot upload allowlist/limits/security parameters
Research recommends a conservative initial allowlist and approximate limits, but the owner explicitly delegated final file-security decisions pending pilot/security review. Treat these as inputs, not fixed product constants.

### C6. AI provider/bakeoff and regional-processing choices
Provider adapter + StudyGrid-specific bakeoff is recommended. No provider/model/region/budget is approved for live product use.

### C7. Deferred live-session/presentation module path
Architecture may leave a clean future module seam, but no recording/transcription/Kahoot-like/live-classroom mode is released for current implementation.

---

## D — dependency-blocked / explicitly out of this build lane

### D0. Exact R6 independent acceptance / General baseline disposition
Stuart Q-S8 is the current independent product-acceptance gate for exact R6. Q-B12 can finish its map now, but an R6-derived product candidate should start only after General consumes Q-S8 and either accepts R6 as the working derivation point or routes a concrete R6 correction. This is independent of intro animation.

### D1. Real backend/auth/Supabase/RLS/command persistence
Architecture direction is accepted in principle, but material backend implementation remains held and this task explicitly forbids it. Real section membership, join-code authorization, server read models, command/RPC writes, RLS and persistence belong to the backend lane.

### D2. Real upload/scan/parser/OCR pipeline
Requires security/privacy/file-policy implementation and backend/storage/extraction work. Frontend UX may be designed separately, but it must not pretend files were safely ingested.

### D3. Live AI/provider execution
Blocked on provider/privacy/data terms/budget/quality validation plus backend orchestration. Frontend may show clearly labelled fixtures/candidates only.

### D4. Real Humber/student pilot data
Before real participant/student data: institutional sponsor/roles, PIA/privacy, research-vs-QA/REB determination, notice/consent as applicable, retention/deletion/access/export, subprocessors/processing locations and incident responsibilities must be resolved.

### D5. Intro / brand portal motion
Actual G → cube → 3×3 portal, A/C motion selection, canonical G/final 3×3 assets and Blender evidence remain in Kevin/Q-B3 motion lanes. Product slices below must not depend on them.

### D6. Public brand/domain/legal rollout
StudyGrid remains a working name. Formal trademark/domain/app-store clearance is required before meaningful public-brand spend/rollout.

### D7. Explicitly deferred integrations
Email/push, grade ingestion, SSO/LTI, institution-admin surface, analytics warehouse, recording/transcripts, live classroom mode, Scenario Lab/3D backend and similar expansions remain outside the next candidate.

---

# Smallest coherent next-product build slices — dependency order

## Gate 0 — consume Q-S8 exact-R6 acceptance
Not a build slice. General consumes Stuart Q-S8. If R6 PASSes, derive from exact R6. If Q-S8 finds a concrete defect that materially affects the planned areas, correct that first rather than layering new product work over an unaccepted baseline.

**Intro animation is not part of this gate.**

## Slice 1 — Local Product Gateway / fixture truth boundary
**Purpose:** stop extending R6’s local prototype state in a way that would later conflict with the accepted architecture.

Scope:
- A8 only, plus the minimum preservation adapters needed for current R6 screens.
- No visible redesign beyond ordinary loading/error/empty fixture states where required.
- No network, Supabase, auth or provider code.

Acceptance:
- typed gateway + local fixture adapter exercised by tests;
- section/revision/source-proof identity explicit;
- one assessment revision feeds all relevant fixture surfaces;
- authoritative-domain fixture writes go through bounded commands instead of view-layer field mutation;
- existing R6 instructor/student validation paths remain intact;
- exact candidate identity/hash/version recorded and sent to Stuart for independent acceptance when General releases the implementation.

**This is the first slice that can actually be implemented without waiting for the intro animation.** It also reduces rework before the visible professor-scale slices.

## Slice 2 — Professor Home / multi-course scale
Depends on Slice 1 fixture/read-model seam.

Scope: A1 + the cross-course portion of A5.
- Today / Now & next.
- Cross-course unresolved attention.
- Current-term class library and transparent sort/pin/colour/label treatment.
- Preserve selected-class R6 drill-in.

Acceptance:
- six-course/hundreds-student fixture;
- no auto-navigation/context theft;
- attention lifecycle correct;
- class identity never colour-only;
- responsive and keyboard/focus basics preserved.

## Slice 3 — Set-up once + assessment autofill + human timing
Depends on Slice 1; can follow Slice 2 or run after the same gateway is stable.

Scope: A2 + A3 + A4.
- schedule/defaults once;
- deterministic evidence/default hierarchy;
- review-by-exception summary;
- human-readable timing with exact editing;
- explicit basis/`why these times?`;
- separate assessment/open/close/practice/reminder/announcement state.

Acceptance:
- fixture reproduces accepted V3 exception pattern;
- no silent ambiguity resolution;
- manual entry parity;
- instructor and student views consume the same assessment revision;
- confirm/approve never equals publish/send.

## Slice 4 — Large roster + local enrolment workflow
Depends on Slice 1 section identity. Does not require live auth.

Scope: A5 + A6.
- hundreds-scale search/filter/sort;
- concrete reason cues;
- fixture join code/link/email, reset/disable and confirm-section flow.

Acceptance:
- no opaque risk ranking;
- accessible controls at scale;
- no claim of real email/auth/persistence;
- section isolation explicit.

## Slice 5 — Section-safe reusable assets, only after owner-QA interaction design
Depends on B1 design gate plus Slice 1 section/revision seam.

Scope after release: browse/adopt revision-bound approved teaching assets while student/roster/question/schedule/delivery state remains section-local.

## Later design-gated slices
- polished upload UX (B2) after owner QA; real ingestion still D2;
- privacy/transparency surfaces (B3) after owner QA;
- teaching-mode surfaces (B4/C2) after research/design/owner QA;
- public evidence system (C1) only after owner QA;
- motion/brand portal (D5) integrated independently through the already-prepared motion seam after its own evidence/selection gates.

---

# Recommended first build slice

**Recommend Slice 1: Local Product Gateway / fixture truth boundary.**

Reason:
1. It is independent of Blender, A/C selection, canonical G and the intro portal.
2. It is reversible and provider-neutral, fitting Nathan’s accepted architecture/delegated-default rule without creating vendor lock-in.
3. It prevents the new professor-scale UI from multiplying R6’s current in-memory/localStorage truth semantics.
4. It lets Slices 2–4 be built entirely against deterministic local read models and later swapped to a real backend adapter without redesigning product surfaces.
5. It preserves the owner gate: Bob implements a bounded technical seam; Bob does not invent backend architecture or unresolved product UX.

**Immediate prerequisite:** Q-S8 terminal R6 acceptance + General release of the slice.  
**Not a prerequisite:** intro animation / Kevin / Blender / A-C / canonical G / final 3×3.

If General prefers the next candidate to include a user-visible improvement rather than a foundation-only delta, the smallest coherent combined release is **Slice 1 + Slice 2**, still with motion excluded.

# Small unresolved decision surface

No new Nathan decision is required for Slices 1–4 beyond the already recorded product/design direction. The immediate non-owner gate is Q-S8 exact-R6 acceptance and General’s bounded implementation release.

Later owner/design decisions remain:
- B1 reusable-asset adoption interaction;
- B2 upload UX;
- B3 privacy/transparency surface;
- B4/C2 teaching-mode experience;
- C1 public evidence experience;
- D5 A/C intro-motion selection when General declares that owner gate ready.

Provider/privacy/institutional/backend decisions are handled through their delegated architecture/security lanes and return to Nathan only when the owner-escalation rule is triggered.

# Boundary verification

Q-B12 changed documentation/route state only. It did **not** mutate R5, R6, product HTML, Blender/motion assets or mechanics, backend/auth/Supabase, deployment, canonical G, final 3×3, or A/C selection.