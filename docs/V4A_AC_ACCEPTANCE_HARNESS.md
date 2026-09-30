# StudyGrid V4A — Candidate A/C post-render acceptance harness

Scope: independent acceptance preparation only. This file freezes the checks before Kevin's render is reviewed. It does not accept, reject or select Candidate A or Candidate C.

## Evidence bind

- Stuart prior independent acceptance: `routes/STUART_V4A_INDEPENDENT_ACCEPTANCE_DONE.txt` @ blob `53927e8b1f0cdf5c4b17c353f70693daea76fb9d`.
- Bob fixed comparison mechanics: commit `b1a7843fcc05a825c1043d1fa060004a29e730b8`.
- Bob comparison source: `blender/scene_v4a_2c_compare.py` @ blob `db9813aed09fc815b94d1693ea270db21ab0642c`.
- Bob geometry report: `blender/v4a_hidden_geometry_report.json` @ blob `19414f061e815e256a89eeb2f5d3e9af95056b00`.
- Bob verifier: `blender/verify_v4a_hidden_mechanics.py` @ blob `65b39e13b051dbff9c1012fdb9df9447325cf25a`.
- Kevin visual proof route: `routes/KEVIN_V4A_AC_RENDER_PROOF.txt` @ blob `27378d6e4f75b250608fe5676d29d8dd6858f67b`.
- Bob reversible integration route: `routes/BOB_V4A_AC_INTEGRATION_VARIANTS.txt` @ blob `a2a696adf5d349df8d32f16dafea41eda270d80d`.

The exact A/C geometry is already fixed by Bob's comparison source for this harness. A render-only compatibility change is acceptable only when Kevin explicitly records it and proves that it does not reinterpret the mechanics.

## Status vocabulary

- **PASS** — required evidence is present and satisfies the frozen condition.
- **FAIL** — evidence shows a frozen reject condition was violated.
- **HOLD** — evidence is missing, ambiguous, unbound to the expected source, or not inspectable enough to decide.

A PASS/FAIL/HOLD result is an acceptance result, not an owner preference. Stuart never turns acceptance into a hinge selection. Owner hinge choice remains a separate decision.

## Frozen source/analytic baseline — not post-render acceptance

Bob's existing analytic report says both fixed prototypes have zero sampled cube collisions and a `0.10L` final resting gap. It also reports positive floor clearance for A and both C stages, `visibility_toggle: none` for C, and `front_camera_start_fully_occluded: true` for C. Those are source/analytic prerequisites only; they do not substitute for Kevin's future visual proof.

Candidate A fixed geometry:
- one face-plane hinge;
- world Y axis through the parent edge plane `x=+0.50L, z=+0.50L`;
- child start centre relative to parent approximately `(1.00, 0, 1.10)`;
- child final centre relative to parent `(1.10, 0, 0)`;
- `-90° -> 0°` hinge sweep.

Candidate C fixed geometry:
- child starts physically rear-stowed at parent-relative `(0, +1.10, 0)`;
- no visibility toggle, opacity cheat or scale animation;
- stage 1: world Z hinge on the parent back-right edge, `0° -> -90°`;
- stage 2: local Y hinge which becomes world X after stage 1, `0° -> -90°`;
- stage-1 end centre approximately `(+1.10, +1.00, 0)`;
- final centre approximately `(+1.10, 0, 0)`.

Shared comparison source:
- cube edge `L=1.0`;
- resting gap `0.10L`;
- bevel `0.055L`;
- same green material and roughness contract;
- exact-front fixed 50 mm camera at `(0,-15,0)` looking at the origin;
- fixed 50 mm oblique diagnostic camera at `(7,-10,6)`;
- floor at `z=-1.25L`.

## Acceptance matrix

| Check | Applies | Source/analytic evidence | Future visual/artifact evidence | Frozen outcome rule |
|---|---|---|---|---|
| Exact-front start truth | A + C | Fixed start transforms from Bob source/report | Front start still and start of motion sequence | PASS only if the render matches the authored start state. Ambiguous framing = HOLD. |
| C geometric occlusion | C | Rear-stow `(0,+1.10,0)` and analytic exact-front occlusion | Exact-front C start | Child visibly exposed at the exact-front stowed start = FAIL C. |
| C rear-child existence | C | Child exists continuously in source | Oblique diagnostic at the same stowed state | Missing/unclear oblique proof = HOLD. Oblique proof showing no genuine rear child or a different state = FAIL C. |
| No visibility/opacity/scale cheat | C | Source says no visibility toggle and no scale animation | Source identity + frame sequence | Any hide/show, opacity or scale trick used to manufacture the hidden start = FAIL C. |
| A hinge axis/plane | A | World-Y face-plane edge hinge | Inspectable motion sequence | Orbit, slide, teleport, wrong pivot/plane or other transform inconsistent with the fixed A source = FAIL A. |
| C hinge axes/sequencing | C | H1 world Z, then H2 local Y/world X after H1 | Stage-1 and stage-2 motion evidence | Colocated/same-axis substitute, wrong order, unexplained simultaneous actuation or different mechanics = FAIL C. If timing is too fast to tell = HOLD. |
| Cube interpenetration | A + C | Bob report: zero sampled collisions | Motion frames/stills for obvious visual contradiction | Any confirmed parent/child penetration = FAIL affected candidate. |
| Floor/environment intersection | A + C | Bob report: positive minimum floor clearance | Motion frames/stills | Any confirmed cube/floor intersection = FAIL affected candidate. |
| Resting gap | A + C | Exact contract `0.10L`; report final gaps `0.10L` | Final still must visibly preserve separation | Numeric source/report deviation from `0.10L` = FAIL. Obvious touching/closed gap in render = FAIL. Pixel-only uncertainty = HOLD, not guessed measurement. |
| Fixed cube dimensions | A + C | Shared `L=1.0`; no candidate scale animation | Source identity + motion sequence | Candidate cube scale/shape change during visible mechanics = FAIL affected candidate. |
| Same comparison conditions | A + C | Same material/cube size/front-camera contract in Bob source | Same run/artifact; matching resolution/framing/material treatment | If A and C are rendered under materially different size/material/camera conditions, the comparison is invalid: HOLD both for owner comparison until re-rendered consistently. |
| Motion readability/easing | A + C | AUTO_CLAMPED easing in comparison source | Slow/inspectable MP4 or equivalent frame sequence | Overshoot/reversal/temporal overlap that changes mechanics = FAIL affected candidate. Merely too fast/blurred to inspect = HOLD and re-render slower. |
| Final rest correctness | A + C | Both fixed final centres are parent-relative `(+1.10,0,0)` | Final still + final motion hold | Wrong final side/orientation/position or visible contact = FAIL affected candidate. |
| Artifact/source identity | Both | Bob head/source/blob identities frozen above | GitHub run head, executed-source identity/hash receipt, artifact digest | Unbound or undocumented mechanics-changing source = HOLD entire render evidence; do not judge either candidate from it. |
| Decode/inventory integrity | Both | N/A | Required stills + MP4/equivalent sequence; file/hash/decode checks | Missing required proof or corrupt/undecodable media = HOLD/FAIL artifact readiness; candidate mechanics remain undecided until valid evidence exists. |

## Required post-render evidence

Minimum visual inventory, using Bob's existing checkpoint names where possible:

1. `front_00_start_stowed.png` — exact-front start, both candidates under the same camera/material/cube contract.
2. `front_01_stage1_mid.png` — representative first-stage motion.
3. `front_02_stage1_landed.png` — C stage 1 landed / A settled-or-held state.
4. `front_03_stage2_mid.png` — C stage 2 motion with A unchanged.
5. `front_04_final.png` — final rest.
6. `diag_00_start_stowed.png` — oblique start proving C physically exists behind its parent while the exact-front start hides it.
7. One slow, inspectable A-vs-C MP4 or equivalent image sequence.
8. Run/artifact identity: workflow run ID, run head, artifact ID/digest where GitHub exposes them, executed source identity, and source/hash receipt when available.
9. Bob analytic geometry report or an exact bound reference to it.

Nathan should see only the clean owner comparison later, not debug geometry or acceptance plumbing, unless he asks.

## Fixed reject conditions

These conditions are frozen before reviewing Kevin's future artifact.

### Candidate A

Reject A if the evidence confirms any of the following:
- the child orbits, slides, teleports, or rotates about a different pivot/plane instead of the fixed world-Y face-plane hinge;
- parent/child interpenetration occurs;
- a cube intersects the floor/environment;
- the final resting gap is not `0.10L` or the cubes visibly touch;
- cube dimensions/scale change during the visible hinge mechanic;
- final rest is not the fixed adjacent east-side state;
- easing introduces a real transform overshoot/reversal that changes the intended mechanic.

### Candidate C

Reject C if the evidence confirms any of the following:
- the rear child is visible in the exact-front stowed start;
- the hidden start is manufactured using visibility, opacity or scale animation;
- the oblique same-state diagnostic proves the child is not genuinely rear-stowed;
- H1/H2 are not the fixed distinct world-Z then local-Y/world-X sequence, or the render substitutes colocated/same-axis mechanics;
- parent/child interpenetration occurs in either stage;
- a cube intersects the floor/environment;
- the final resting gap is not `0.10L` or the cubes visibly touch;
- cube dimensions/scale change during visible motion;
- final rest is not the fixed adjacent east-side state;
- easing introduces a real transform overshoot/reversal or stage overlap that changes the intended mechanism.

### Comparison / artifact

Do not reject either mechanic merely because evidence is missing. Use HOLD instead when:
- the run/artifact cannot be bound to Bob's fixed mechanics or a documented render-only derivative;
- required stills or motion evidence are missing;
- MP4/equivalent motion cannot be decoded or inspected;
- the front/oblique views do not show the relevant state clearly enough;
- A and C were not rendered under the same material/cube-size/camera comparison contract;
- pacing is too fast to inspect but no mechanical violation is actually proven.

## Validator behaviour

`tools/v4a_ac_artifact_validator.py` accepts a ZIP or extracted folder and does not modify the input. It:
- validates ZIP CRC/path safety and computes the ZIP SHA-256;
- inventories files;
- checks the six required still roles and validates PNG headers/dimensions;
- uses `ffprobe` when available for MP4 metadata and `ffmpeg` when available for a full decode;
- parses Bob-compatible geometry reports and checks collision/floor/gap/occlusion/visibility fields;
- looks for Bob head/source provenance in manifests/receipts;
- verifies filename-bound SHA-256 receipts when present;
- reports PASS/FAIL/HOLD/INFO;
- always leaves Candidate A, Candidate C and owner hinge selection on HOLD until the independent visual review is actually performed.

Exit code `0` means no machine-level FAIL was found; HOLDs may still remain. Exit code `1` means at least one machine-level FAIL. Exit code `2` means the input artifact/ZIP itself could not be processed.

## What can be done now vs what waits

Completed in prep:
- fixed acceptance matrix;
- fixed reject conditions;
- exact evidence inventory;
- source-vs-visual separation;
- reusable artifact validator;
- report template.

Still dependent on Kevin's future render:
- run/artifact/source identity binding for the actual render;
- actual still/MP4 inventory and decode result;
- visual exact-front C occlusion proof;
- visual oblique rear-stow proof;
- visual A hinge readability;
- visual C two-stage causal readability;
- visual confirmation of no contradictory clipping/floor contact;
- visual final-rest and gap legibility;
- final independent PASS/FAIL/HOLD by candidate.

Even after those are complete, owner preference remains a separate decision and is not chosen by this harness.
