# StudyGrid V4A convergence map

Coordinator: ChatGPT General CF-0040
Date: 2026-09-30 ET
Status: coordination-only; no product/main mutation

## Current verified state
- Bob's reversible A/C integration variants are source/static complete on `bob-v4a-ac-integration-variants` at `09b8d26a8969a809d60c47a9e7dbbaca9adcbd27`. Candidate A applies cleanly. Candidate C applies cleanly but requires a 2C-only exact-front 50 mm camera cut and 2C-only floor hide for truthful rear occlusion / floor safety. No owner winner selected.
- Kevin's A/C Blender render proof run `36726558912` completed `success` at exact source head `73738d53c1f6fab4153e24155603b9e3e048b0b7`. Artifact `studygrid-v4a-ac-render-proof`, ID `11103902103`, provider digest `sha256:0b71adc48c9d47f395e204e0a4ba8f5fae19f2a5afb8a97180a9af8be947ae14` is durable.
- Stuart's acceptance harness is frozen and DONE on `stuart-v4a-ac-acceptance-harness-prep` at `6cffff02fc37f6bdb186912ffeacc8a3a86386df`.
- Stuart's exact post-render acceptance route is staged on that branch at `routes/STUART_V4A_AC_INDEPENDENT_ACCEPTANCE_RUN2.txt`.
- Bob successor `CF-0042` is active and owns an ordered pull queue. Kevin and Stuart queues are already durable on main.

## Critical path
1. Stuart applies the frozen matrix to Kevin run 2 and returns PASS/FAIL/HOLD per candidate and criterion.
2. In parallel, Bob successor works eligible queue items that do not depend on the A/C owner choice (G→seed scaffold, doorway camera handoff fixture).
3. Kevin, once his current package is durably returned, pulls Q-K1 to render full-context A and C previews from Bob's reversible variants, then Q-K2 GLB smoke if source-stable.
4. Stuart then pulls the corresponding fidelity/export acceptance items as each dependency becomes durable.
5. General presents Nathan one small owner decision surface: Candidate A versus Candidate C, using only accepted/held evidence and clean visual artifacts.
6. Only after Nathan chooses A or C does Bob apply the selected variant on an isolated final-integration branch.
7. Kevin renders / round-trips the selected candidate; Stuart independently accepts it.
8. General may then consider promotion/merge only under a separate explicit gate. No deployment/canonical/product mutation is implied here.

## Owner-choice readiness gate
Do not ask Nathan to choose A/C until all are true:
- exact Kevin artifact identity verified;
- Stuart frozen acceptance executed;
- each candidate has PASS/FAIL/HOLD by criterion with source vs visual evidence separated;
- any HOLD that materially prevents informed visual choice is resolved;
- clean, non-debug owner-viewable A/C artifacts identified;
- General has reconciled Bob source variants with the actual rendered mechanics.

## Work that can proceed before owner choice
- Bob: G→seed parameterized continuity scaffold; doorway fixed-lens handoff fixture; other non-overlapping QA scaffolds explicitly queued by General.
- Kevin: render/integrity work and dual-candidate full-context/export smoke after current package durable return.
- Stuart: independent acceptance, full-context fidelity audit, export/runtime acceptance as artifacts arrive.
- General: lifecycle refresh, dependency reconciliation, queue replenishment, artifact/branch identity checks, owner-decision packaging, route preparation.

## Held work
- selecting A or C for Nathan;
- merging either candidate to main;
- canonical G freeze;
- final 3x3 choreography;
- production StudyGrid changes, R5/R6 promotion, Supabase/backend/auth mutation, deployment.