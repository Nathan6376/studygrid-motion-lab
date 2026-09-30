# StudyGrid V4A — Q-S5 Independent QA of Bob Q-B4/Q-B5/Q-B6

## Exact source identity
- Q-B4 branch head: `7c94bd8765d11398181d799a1fc9d9d53bb95ef5`
  - `doorway_cube_selection_policy.py` blob `9df4370b8be6be2917c1aeb12f236e0e2f4ea784`
- Q-B5 branch head: `8cddfeb71b1b70c7d62aec8ba663e257242deb0c`
  - `nine_cube_grid_validator.py` blob `0bf0dcfa8cd05397f0f2f0367c35431893235092`
- Q-B6 branch head: `fa4cbb1d95a396d2cd9dfdb6020bd574e1383b56`
  - `study_visibility_cut_fixture.py` blob `4c6cc02f014fd68ea9861f6ffe580d3d2a24890e`

Local QA copies were checked with `git hash-object` and matched those three provider blobs exactly before execution.

## Q-B4 — doorway cube-selection policy
**PASS.** Tested:
- first run with no history;
- one eligible cube with unavoidable repeat;
- 2, 3 and 9 eligible cubes across 250 seeds each: previous eligible cube never immediately repeats;
- invalid/non-eligible prior cube: full eligible pool remains available;
- deterministic replay across fixed seeds: exact result equality;
- duplicate and empty eligible sets remain rejected.

No corrective route required.

## Q-B5 — nine-cube grid invariant validator
**PASS.** Baseline valid 3×3 grid passes. Adversarial cases correctly fail:
- missing cube and missing slot;
- extra tenth cube;
- unequal cube dimension;
- effectively collapsed positive gap at/below tolerance;
- literal zero gap;
- duplicate slot occupancy;
- invalid parent reference;
- parent cycle.

No corrective route required.

## Q-B6 — study visibility / cut isolation fixture
**PASS.** Tested at 8, 12 and 30 fps:
- each study's own objects pass at representative mid-frames;
- one foreign object from another study is detected as cross-study bleed;
- every study-start cut is owned by the new study at the cut and immediately after;
- a previous-study object present at the cut is rejected;
- non-study diagnostic names representing camera-cut/easing metadata do not trigger visibility errors, confirming the checker does not conflate cut/easing diagnostics with study-object visibility.

No corrective route required.

## Aggregate
18 independent QA assertions/groups passed, 0 failed. Q-B4 PASS / Q-B5 PASS / Q-B6 PASS.

This is fixture QA only. It does not certify product integration, final choreography, Blender runtime behavior, or deployment.
