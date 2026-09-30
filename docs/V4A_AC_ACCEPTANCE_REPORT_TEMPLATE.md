# StudyGrid V4A — Candidate A/C independent acceptance report template

Use this only after Kevin's actual render artifact exists and has been bound to the expected source. Do not infer owner preference from the acceptance result.

## Artifact identity

- Review timestamp:
- Kevin branch:
- Render run ID:
- Render run head:
- Artifact name / ID:
- Artifact SHA-256/digest:
- Executed source file:
- Executed source SHA-256:
- Bob fixed comparison base: `b1a7843fcc05a825c1043d1fa060004a29e730b8`
- Bob comparison source blob: `db9813aed09fc815b94d1693ea270db21ab0642c`
- Render-only source difference, if any:
- Validator command/result:

Artifact identity disposition: PASS / FAIL / HOLD

## Machine / source checks

| Check | Result | Evidence |
|---|---|---|
| ZIP/folder inventory | PASS / FAIL / HOLD | |
| Required still inventory | PASS / FAIL / HOLD | |
| MP4/equivalent sequence decode | PASS / FAIL / HOLD | |
| Hash/source receipts | PASS / FAIL / HOLD | |
| Geometry report bound to fixed mechanics | PASS / FAIL / HOLD | |
| A collision/floor/gap analytic contract | PASS / FAIL / HOLD | |
| C collision/floor/gap/occlusion/no-toggle analytic contract | PASS / FAIL / HOLD | |
| Same comparison material/cube/camera source contract | PASS / FAIL / HOLD | |

## Candidate A — visual acceptance

| Check | Result | Evidence |
|---|---|---|
| Exact-front start state matches fixed A source | PASS / FAIL / HOLD | |
| Single world-Y face-plane hinge reads correctly | PASS / FAIL / HOLD | |
| No orbit/slide/teleport/wrong pivot | PASS / FAIL / HOLD | |
| No visible parent/child penetration | PASS / FAIL / HOLD | |
| No floor/environment intersection | PASS / FAIL / HOLD | |
| Fixed cube dimensions / no scale change | PASS / FAIL / HOLD | |
| Motion is slow enough to inspect | PASS / FAIL / HOLD | |
| Easing does not alter mechanic | PASS / FAIL / HOLD | |
| Final rest is correct east-side adjacent state | PASS / FAIL / HOLD | |
| Final 0.10L gap is source-verified and visually non-contacting | PASS / FAIL / HOLD | |

Candidate A acceptance: PASS / FAIL / HOLD
Reason in one sentence:

## Candidate C — visual acceptance

| Check | Result | Evidence |
|---|---|---|
| Exact-front rear-stowed child is genuinely occluded | PASS / FAIL / HOLD | |
| Oblique same-state view proves child physically exists behind parent | PASS / FAIL / HOLD | |
| No visibility/opacity/scale cheat | PASS / FAIL / HOLD | |
| Stage 1 reads as fixed world-Z back-right hinge | PASS / FAIL / HOLD | |
| Stage 2 reads as fixed local-Y/world-X back-top hinge | PASS / FAIL / HOLD | |
| Causal order is stage 1 then stage 2, not same-axis/simultaneous substitute | PASS / FAIL / HOLD | |
| No visible parent/child penetration in either stage | PASS / FAIL / HOLD | |
| No floor/environment intersection | PASS / FAIL / HOLD | |
| Fixed cube dimensions / no scale change | PASS / FAIL / HOLD | |
| Motion is slow enough to inspect | PASS / FAIL / HOLD | |
| Easing does not alter mechanic | PASS / FAIL / HOLD | |
| Final rest is correct east-side adjacent state | PASS / FAIL / HOLD | |
| Final 0.10L gap is source-verified and visually non-contacting | PASS / FAIL / HOLD | |

Candidate C acceptance: PASS / FAIL / HOLD
Reason in one sentence:

## Comparison validity

- Same material/cube size/camera conditions: PASS / FAIL / HOLD
- Required front/oblique states are directly comparable: PASS / FAIL / HOLD
- No debug clutter is needed for owner review: PASS / FAIL / HOLD

Comparison validity: PASS / FAIL / HOLD

## Independent result to General

Candidate A: PASS / FAIL / HOLD
Candidate C: PASS / FAIL / HOLD
Owner hinge choice: HOLD — not selected by independent acceptance

If both candidates pass: General may prepare the clean owner A-vs-C visual choice.
If either candidate fails: report the fixed reject condition and evidence; do not auto-select the other candidate on Nathan's behalf.
If either candidate is held: state the smallest missing evidence or re-render needed.
