#!/usr/bin/env python3
"""Synthetic positive/negative verification for motion_invariant_scanner.py."""

import copy
import json
from motion_invariant_scanner import build_report


def make_manifest():
    cubes = []
    for r in range(3):
        for c in range(3):
            cubes.append({
                "id": f"c{r}{c}",
                "centre": [c * 1.1, 0.0, r * 1.1],
                "dimensions": [1.0, 1.0, 1.0],
            })
    adjacency = []
    for r in range(3):
        for c in range(3):
            if c < 2:
                adjacency.append([f"c{r}{c}", f"c{r}{c+1}"])
            if r < 2:
                adjacency.append([f"c{r}{c}", f"c{r+1}{c}"])
    return {"final_cubes": cubes, "adjacency_pairs": adjacency}


CONFIG = {
    "fps": 30,
    "governed_object_vars": ["parent_c", "child_c"],
    "fixed_lens_camera_vars": ["cam"],
    "hidden_mechanics_object_vars": ["parent_c", "child_c"],
    "allowed_visibility_windows": {
        "parent_c": [[8.8, 12.0]],
        "child_c": [[8.8, 12.0]],
    },
    "expected_final_cube_count": 9,
    "minimum_air_gap": 0.1,
}

CLEAN_SOURCE = '''
class Obj:
    pass
cam = Obj()
cam.data = Obj()
cam.data.lens = 50
parent_c = Obj()
child_c = Obj()
set_linear_visibility(parent_c, F(8.8), F(12.0))
set_linear_visibility(child_c, F(8.8), F(12.0))
'''


def codes(report):
    return {f["code"] for f in report["findings"]}


def main():
    manifest = make_manifest()
    results = {}

    clean = build_report(CLEAN_SOURCE, CONFIG, manifest)
    assert clean["status"] == "PASS", clean
    results["clean_positive"] = "PASS"

    scale = build_report(
        CLEAN_SOURCE + '\nparent_c.scale = (1,1,1)\nparent_c.keyframe_insert("scale", frame=F(9.5))\n',
        CONFIG,
        manifest,
    )
    assert scale["status"] == "FAIL" and "ANIMATED_OBJECT_SCALE" in codes(scale), scale
    results["animated_scale_negative"] = "PASS"

    lens = build_report(
        CLEAN_SOURCE + '\ncam.data.keyframe_insert("lens", frame=F(9.0))\n',
        CONFIG,
        manifest,
    )
    assert lens["status"] == "FAIL" and "ANIMATED_CAMERA_FOV" in codes(lens), lens
    results["animated_lens_negative"] = "PASS"

    bad_visibility_source = CLEAN_SOURCE.replace(
        'set_linear_visibility(child_c, F(8.8), F(12.0))',
        'set_linear_visibility(child_c, F(9.1), F(12.0))',
    )
    visibility = build_report(bad_visibility_source, CONFIG, manifest)
    assert visibility["status"] == "FAIL" and "UNAPPROVED_HIDDEN_VISIBILITY_WINDOW" in codes(visibility), visibility
    results["hidden_visibility_negative"] = "PASS"

    bad_dimensions = copy.deepcopy(manifest)
    bad_dimensions["final_cubes"][1]["dimensions"] = [1.02, 1.0, 1.0]
    dimensions = build_report(CLEAN_SOURCE, CONFIG, bad_dimensions)
    assert dimensions["status"] == "FAIL" and "CUBE_DIMENSION_DRIFT" in codes(dimensions), dimensions
    results["dimension_drift_negative"] = "PASS"

    bad_gap = copy.deepcopy(manifest)
    bad_gap["final_cubes"][1]["centre"] = [1.02, 0.0, 0.0]
    gap = build_report(CLEAN_SOURCE, CONFIG, bad_gap)
    assert gap["status"] == "FAIL" and "GAP_COLLAPSE" in codes(gap), gap
    results["gap_collapse_negative"] = "PASS"

    hold = build_report(CLEAN_SOURCE, CONFIG, None)
    assert hold["status"] == "HOLD" and "FINAL_STATE_MANIFEST_MISSING" in codes(hold), hold
    results["missing_state_hold"] = "PASS"

    print(json.dumps({"status": "PASS", "cases": results}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
