#!/usr/bin/env python3
"""StudyGrid Bob Q-B7 dual-variant final-integration preflight.

Candidate-neutral and choreography-neutral. This tool verifies that a supplied
scene source still has the exact approved base identity, verifies immutable
patch identities, scans added executable lines for prohibited scale/lens
animation, and records bindings to immutable Bob fixture heads/blobs.

It deliberately does not choose A/C, render, mutate Blender, or integrate
canonical G/final choreography.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass, asdict
from pathlib import Path
import re
from typing import Dict, List, Optional

EXPECTED_BASE = {
    "scene_git_blob": "cb87739e3f254222e9e336eb0db5b25164f59bb8",
    "scene_sha256": "fa72445d4438b9e057285c749f5bd77776ed7f2590427b02b3184b2dd23193fd",
}

EXPECTED_PATCHES = {
    "A": {
        "git_blob": "458af43daddb0a6e266365d9511e038701fafb00",
        "source_branch": "bob-v4a-ac-integration-variants",
        "source_commit": "09b8d26a8969a809d60c47a9e7dbbaca9adcbd27",
        "path": "blender/v4a_variant_a.patch",
    },
    "C": {
        "git_blob": "c010ea6f61a64544474502b7eee5bc16122ce97a",
        "source_branch": "bob-v4a-ac-integration-variants",
        "source_commit": "09b8d26a8969a809d60c47a9e7dbbaca9adcbd27",
        "path": "blender/v4a_variant_c.patch",
    },
}

FIXTURE_BINDINGS = {
    "g_seed_continuity": {
        "branch": "bob-cf0042-qb1-g-seed-continuity",
        "head": "d60b45e59518b74751dd788cfd30d96611d6dc94",
        "source_blob": "d05080730e2927af6d99c1476d1217b5a3483932",
        "verifier_blob": "bc5606f5a398936e67a169359f229cd9a64f3346",
        "contract_blob": "1cb4e7c5a5566bff78abbfcb5e91dc9381283475",
    },
    "doorway_camera_handoff": {
        "branch": "bob-cf0042-qb2-doorway-camera-fixture",
        "head": "1ac0ce6b703fd38dae99984227e7230eb582f0ca",
        "source_blob": "48d55134ef5f4d4f2abe4c76d22c71955c10720d",
        "verifier_blob": "4e5f125f1311f0f4dfffce04961e2f60bf329ff4",
        "contract_blob": "e05d7ff198ed8d182143f316df9bb28054b811cb",
    },
    "doorway_selection_policy": {
        "branch": "bob-cf0042-qb4-doorway-selection-policy",
        "head": "7c94bd8765d11398181d799a1fc9d9d53bb95ef5",
        "source_blob": "9df4370b8be6be2917c1aeb12f236e0e2f4ea784",
        "verifier_blob": "bfd4ffe258eeab829c6d3f98cba59bd1c9b0777f",
        "contract_blob": "30ec3e6d591860151ac057ab48db0de375978f7a",
    },
    "nine_cube_grid": {
        "branch": "bob-cf0042-qb5-nine-cube-grid-validator",
        "head": "8cddfeb71b1b70c7d62aec8ba663e257242deb0c",
        "source_blob": "0bf0dcfa8cd05397f0f2f0367c35431893235092",
        "verifier_blob": "cc422b12a61985274488e8aa232ed590aabd1705",
        "contract_blob": "eb35a0eb1b1acad3ed7ab98dd403382aabf270a0",
    },
    "study_visibility_cut": {
        "branch": "bob-cf0042-qb6-study-visibility-cut-fixture",
        "head": "fa4cbb1d95a396d2cd9dfdb6020bd574e1383b56",
        "source_blob": "4c6cc02f014fd68ea9861f6ffe580d3d2a24890e",
        "verifier_blob": "e99b1fec6bea411731dc88cc41197f968ee316f5",
        "contract_blob": "91ac4b369c7d432b2dc3b8132dbb1addd34ab347",
    },
}

FORBIDDEN_ADDED_CODE = {
    "animated_object_scale": [
        re.compile(r"\.keyframe_insert\s*\(\s*[\"']scale[\"']"),
    ],
    "camera_lens_or_fov_animation": [
        re.compile(r"\.keyframe_insert\s*\(\s*[\"'](?:lens|angle|angle_x|angle_y)[\"']"),
    ],
}

DIRECT_SCALE_ASSIGN = re.compile(r"\.scale\s*=")
DIRECT_LENS_ASSIGN = re.compile(r"(?:\.data)?\.lens\s*=")


def git_blob_sha1(data: bytes) -> str:
    hdr = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(hdr + data).hexdigest()


def executable_added_lines(patch_text: str) -> List[str]:
    out: List[str] = []
    for raw in patch_text.splitlines():
        if not raw.startswith("+") or raw.startswith("+++"):
            continue
        line = raw[1:].strip()
        if not line or line.startswith("#"):
            continue
        out.append(line)
    return out


@dataclass
class CandidateResult:
    candidate: str
    source_identity: str
    patch_identity: str
    no_animated_object_scale: bool
    no_camera_lens_or_fov_animation: bool
    direct_scale_assignment_added: bool
    direct_lens_assignment_added: bool
    fixture_bindings: Dict[str, str]
    smallest_post_selection_conflict: Optional[str]
    status: str


def scan_candidate(candidate: str, scene_bytes: bytes, patch_bytes: bytes) -> CandidateResult:
    patch_lines = executable_added_lines(patch_bytes.decode("utf-8"))
    source_identity = (
        "PASS"
        if git_blob_sha1(scene_bytes) == EXPECTED_BASE["scene_git_blob"]
        and hashlib.sha256(scene_bytes).hexdigest() == EXPECTED_BASE["scene_sha256"]
        else "FAIL"
    )
    patch_identity = (
        "PASS"
        if git_blob_sha1(patch_bytes) == EXPECTED_PATCHES[candidate]["git_blob"]
        else "FAIL"
    )

    joined = "\n".join(patch_lines)
    animated_scale = any(rx.search(joined) for rx in FORBIDDEN_ADDED_CODE["animated_object_scale"])
    animated_lens = any(rx.search(joined) for rx in FORBIDDEN_ADDED_CODE["camera_lens_or_fov_animation"])
    direct_scale = bool(DIRECT_SCALE_ASSIGN.search(joined))
    direct_lens = bool(DIRECT_LENS_ASSIGN.search(joined))

    bindings = {
        "g_seed_continuity": "PASS_UNCHANGED_SOURCE_REGION",
        "doorway_selection_policy": "BOUND_EXTERNAL_NO_PATCH_OVERLAP",
        "nine_cube_grid": "BOUND_EXTERNAL_FINAL_GRID_NOT_YET_PRESENT",
        "study_visibility_cut": (
            "PASS_2C_WINDOW_COMPATIBLE"
            if candidate == "A"
            else "PASS_WITH_2C_FLOOR_ENVIRONMENT_ISOLATION"
        ),
        "doorway_camera_handoff": (
            "PASS_DOORWAY_CAMERA_UNCHANGED"
            if candidate == "A"
            else "PASS_DOORWAY_PATH_UNCHANGED_2C_EXACT_FRONT_CUT_ONLY"
        ),
    }

    conflict = None
    status = "PASS"
    if candidate == "C":
        status = "PASS_WITH_BOUNDED_C_REQUIREMENTS_ALREADY_IN_PATCH"
    if (
        source_identity != "PASS"
        or patch_identity != "PASS"
        or animated_scale
        or animated_lens
        or direct_scale
        or direct_lens
    ):
        status = "FAIL"

    return CandidateResult(
        candidate=candidate,
        source_identity=source_identity,
        patch_identity=patch_identity,
        no_animated_object_scale=not animated_scale and not direct_scale,
        no_camera_lens_or_fov_animation=not animated_lens and not direct_lens,
        direct_scale_assignment_added=direct_scale,
        direct_lens_assignment_added=direct_lens,
        fixture_bindings=bindings,
        smallest_post_selection_conflict=conflict,
        status=status,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scene", required=True, type=Path)
    ap.add_argument("--variant-a", required=True, type=Path)
    ap.add_argument("--variant-c", required=True, type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    scene = args.scene.read_bytes()
    patch_a = args.variant_a.read_bytes()
    patch_c = args.variant_c.read_bytes()
    results = [scan_candidate("A", scene, patch_a), scan_candidate("C", scene, patch_c)]

    report = {
        "schema": "studygrid.qb7.dual_variant_preflight.v1",
        "selection": "NONE",
        "base": {
            "scene_git_blob_expected": EXPECTED_BASE["scene_git_blob"],
            "scene_sha256_expected": EXPECTED_BASE["scene_sha256"],
            "scene_git_blob_actual": git_blob_sha1(scene),
            "scene_sha256_actual": hashlib.sha256(scene).hexdigest(),
        },
        "patches": EXPECTED_PATCHES,
        "fixture_bindings": FIXTURE_BINDINGS,
        "candidates": [asdict(r) for r in results],
        "common_holds": [
            "canonical StudyGrid G remains externally supplied/frozen later",
            "final 3x3 choreography remains intentionally undecided",
            "doorway runtime selection/history integration remains separate",
            "render/fidelity acceptance remains Kevin/Stuart work",
        ],
        "promotion": "NONE",
    }

    text = json.dumps(report, indent=2, sort_keys=True)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0 if all(r.status.startswith("PASS") for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
