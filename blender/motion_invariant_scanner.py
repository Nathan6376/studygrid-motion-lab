#!/usr/bin/env python3
"""Candidate-neutral StudyGrid motion-invariant scanner.

Static source scan:
- animated object scale on governed object variables
- fixed-lens camera focal-length/FOV animation or drift
- hidden-mechanics visibility-window drift
- obvious opacity animation patterns

State-manifest scan:
- final cube dimension drift
- pairwise gap collapse for axis-aligned final cube centres/dimensions

The scanner does not infer choreography, choose A/C, or execute Blender.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple


@dataclass
class Finding:
    code: str
    severity: str
    subject: str
    line: Optional[int]
    frame: Optional[float]
    time_seconds: Optional[float]
    detail: str


def _name_of(expr: ast.AST) -> Optional[str]:
    if isinstance(expr, ast.Name):
        return expr.id
    return None


def _attr_chain(expr: ast.AST) -> Optional[Tuple[str, ...]]:
    parts: List[str] = []
    cur = expr
    while isinstance(cur, ast.Attribute):
        parts.append(cur.attr)
        cur = cur.value
    if isinstance(cur, ast.Name):
        parts.append(cur.id)
        return tuple(reversed(parts))
    return None


def _literal_number(expr: ast.AST) -> Optional[float]:
    if isinstance(expr, ast.Constant) and isinstance(expr.value, (int, float)):
        return float(expr.value)
    if isinstance(expr, ast.UnaryOp) and isinstance(expr.op, ast.USub):
        n = _literal_number(expr.operand)
        return -n if n is not None else None
    return None


def _frame_time(expr: Optional[ast.AST], fps: float) -> Tuple[Optional[float], Optional[float]]:
    if expr is None:
        return None, None
    n = _literal_number(expr)
    if n is not None:
        return n, n / fps if fps else None
    if isinstance(expr, ast.Call) and isinstance(expr.func, ast.Name) and expr.func.id == "F" and expr.args:
        sec = _literal_number(expr.args[0])
        if sec is not None:
            return sec * fps, sec
    return None, None


def _keyword(call: ast.Call, name: str) -> Optional[ast.AST]:
    for kw in call.keywords:
        if kw.arg == name:
            return kw.value
    return None


def _call_string_arg(call: ast.Call, index: int = 0) -> Optional[str]:
    if len(call.args) <= index:
        return None
    arg = call.args[index]
    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
        return arg.value
    return None


def _allowed_time(config: Dict[str, Any], subject: str, prop: str, t: Optional[float]) -> bool:
    if t is None:
        return False
    allowed = config.get("allowed_visibility_times", {}).get(subject, {}).get(prop, [])
    tol = float(config.get("time_tolerance_seconds", 1e-6))
    return any(abs(float(x) - t) <= tol for x in allowed)


def scan_source(source: str, config: Dict[str, Any]) -> List[Finding]:
    tree = ast.parse(source)
    fps = float(config.get("fps", 30.0))
    governed = set(config.get("governed_object_vars", []))
    fixed_cameras = set(config.get("fixed_lens_camera_vars", []))
    hidden = set(config.get("hidden_mechanics_object_vars", []))
    findings: List[Finding] = []
    lens_assignments: Dict[str, List[Tuple[int, Optional[float]]]] = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                chain = _attr_chain(target)
                if not chain:
                    continue
                root = chain[0]
                if root in governed and chain[-1] == "scale":
                    if config.get("forbid_direct_scale_assignment", False):
                        findings.append(Finding(
                            "DIRECT_SCALE_ASSIGNMENT",
                            "ERROR",
                            root,
                            getattr(node, "lineno", None),
                            None,
                            None,
                            "Governed object receives a direct scale assignment.",
                        ))
                if root in fixed_cameras and chain[-1] in {"lens", "angle", "angle_x", "angle_y"}:
                    val = _literal_number(node.value)
                    lens_assignments.setdefault(root, []).append((getattr(node, "lineno", -1), val))
                if root in hidden and chain[-1] in {"alpha", "opacity"}:
                    findings.append(Finding(
                        "HIDDEN_PATH_OPACITY_ASSIGNMENT",
                        "ERROR",
                        root,
                        getattr(node, "lineno", None),
                        None,
                        None,
                        f"Hidden-mechanics object assigns {chain[-1]}.",
                    ))

        if isinstance(node, ast.Call):
            chain = _attr_chain(node.func)
            if chain and chain[-1] in {"keyframe_insert", "driver_add"}:
                owner_chain = chain[:-1]
                root = owner_chain[0] if owner_chain else None
                prop = _call_string_arg(node)
                frame_expr = _keyword(node, "frame")
                frame, t = _frame_time(frame_expr, fps)

                if root in governed and prop == "scale":
                    findings.append(Finding(
                        "ANIMATED_OBJECT_SCALE",
                        "ERROR",
                        root,
                        getattr(node, "lineno", None),
                        frame,
                        t,
                        "Governed object scale is keyframed or driven.",
                    ))

                if root in fixed_cameras and prop in {"lens", "angle", "angle_x", "angle_y"}:
                    findings.append(Finding(
                        "ANIMATED_CAMERA_FOV",
                        "ERROR",
                        root,
                        getattr(node, "lineno", None),
                        frame,
                        t,
                        f"Fixed-lens camera animates {prop}.",
                    ))

                if root in hidden and prop in {"hide_render", "hide_viewport", "alpha", "opacity"}:
                    if not _allowed_time(config, root, prop, t):
                        findings.append(Finding(
                            "UNAPPROVED_HIDDEN_VISIBILITY_ANIMATION",
                            "ERROR",
                            root,
                            getattr(node, "lineno", None),
                            frame,
                            t,
                            f"{prop} animation is outside the approved hidden-path visibility schedule.",
                        ))

            if isinstance(node.func, ast.Name) and node.func.id == "set_linear_visibility" and node.args:
                subject = _name_of(node.args[0])
                if subject in hidden:
                    start_frame, start_t = _frame_time(node.args[1] if len(node.args) > 1 else None, fps)
                    end_frame, end_t = _frame_time(node.args[2] if len(node.args) > 2 else None, fps)
                    allowed_windows = config.get("allowed_visibility_windows", {}).get(subject, [])
                    tol = float(config.get("time_tolerance_seconds", 1e-6))
                    ok = any(
                        len(win) == 2
                        and start_t is not None
                        and end_t is not None
                        and abs(float(win[0]) - start_t) <= tol
                        and abs(float(win[1]) - end_t) <= tol
                        for win in allowed_windows
                    )
                    if not ok:
                        findings.append(Finding(
                            "UNAPPROVED_HIDDEN_VISIBILITY_WINDOW",
                            "ERROR",
                            subject or "<unknown>",
                            getattr(node, "lineno", None),
                            start_frame,
                            start_t,
                            f"Visibility window ({start_t}, {end_t}) is not approved.",
                        ))

    for cam, assigns in lens_assignments.items():
        values = [v for _, v in assigns if v is not None]
        if len(assigns) > 1 and (len(set(values)) > 1 or len(values) != len(assigns)):
            lines = ",".join(str(line) for line, _ in assigns)
            findings.append(Finding(
                "CAMERA_LENS_DRIFT",
                "ERROR",
                cam,
                assigns[-1][0] if assigns else None,
                None,
                None,
                f"Fixed-lens camera has multiple/nonconstant focal assignments at lines {lines}.",
            ))

    for i, line in enumerate(source.splitlines(), start=1):
        stripped = line.strip()
        if "keyframe_insert" in stripped and any(tok in stripped for tok in ('"Alpha"', "'Alpha'", '"alpha"', "'alpha'")):
            findings.append(Finding(
                "MATERIAL_ALPHA_KEYFRAME",
                "ERROR",
                "<material>",
                i,
                None,
                None,
                "Material alpha keyframe detected in source.",
            ))

    return findings


def _as_vec3(value: Sequence[float], subject: str, field: str) -> Tuple[float, float, float]:
    if len(value) != 3:
        raise ValueError(f"{subject}.{field} must contain exactly 3 numbers")
    return tuple(float(x) for x in value)


def _axis_gap(
    ca: Tuple[float, float, float],
    da: Tuple[float, float, float],
    cb: Tuple[float, float, float],
    db: Tuple[float, float, float],
) -> Tuple[float, float, float]:
    return tuple(abs(cb[i] - ca[i]) - (da[i] + db[i]) / 2.0 for i in range(3))


def scan_state_manifest(manifest: Optional[Dict[str, Any]], config: Dict[str, Any]) -> List[Finding]:
    if manifest is None:
        return [Finding(
            "FINAL_STATE_MANIFEST_MISSING",
            "HOLD",
            "final_grid",
            None,
            None,
            None,
            "No final cube state manifest supplied; dimension/gap checks were not run.",
        )]

    cubes = manifest.get("final_cubes")
    if not isinstance(cubes, list) or not cubes:
        return [Finding(
            "FINAL_CUBES_MISSING",
            "HOLD",
            "final_grid",
            None,
            None,
            None,
            "Manifest does not provide final_cubes.",
        )]

    findings: List[Finding] = []
    expected_count = int(config.get("expected_final_cube_count", 9))
    if len(cubes) != expected_count:
        findings.append(Finding(
            "FINAL_CUBE_COUNT",
            "ERROR",
            "final_grid",
            None,
            None,
            None,
            f"Expected {expected_count} final cubes; found {len(cubes)}.",
        ))

    dim_tol = float(config.get("dimension_tolerance", 1e-6))
    min_gap = float(config.get("minimum_air_gap", 0.0))
    gap_tol = float(config.get("gap_tolerance", 1e-6))

    parsed = []
    for idx, cube in enumerate(cubes):
        name = str(cube.get("id", f"cube_{idx}"))
        dims = _as_vec3(cube["dimensions"], name, "dimensions")
        centre = _as_vec3(cube["centre"], name, "centre")
        parsed.append((name, centre, dims))

    ref_dims = parsed[0][2]
    for name, _, dims in parsed[1:]:
        if any(abs(dims[i] - ref_dims[i]) > dim_tol for i in range(3)):
            findings.append(Finding(
                "CUBE_DIMENSION_DRIFT",
                "ERROR",
                name,
                None,
                None,
                None,
                f"Dimensions {dims} differ from reference {ref_dims}.",
            ))

    adjacency = {
        tuple(sorted((str(a), str(b))))
        for a, b in manifest.get("adjacency_pairs", [])
    }
    by_name = {name: (centre, dims) for name, centre, dims in parsed}
    for a, b in sorted(adjacency):
        if a not in by_name or b not in by_name:
            findings.append(Finding(
                "INVALID_ADJACENCY_REFERENCE",
                "ERROR",
                f"{a}<->{b}",
                None,
                None,
                None,
                "Adjacency pair references an unknown cube.",
            ))
            continue
        ca, da = by_name[a]
        cb, db = by_name[b]
        gaps = _axis_gap(ca, da, cb, db)
        nonnegative = [g for g in gaps if g >= -gap_tol]
        if not nonnegative:
            findings.append(Finding(
                "CUBE_OVERLAP",
                "ERROR",
                f"{a}<->{b}",
                None,
                None,
                None,
                f"Axis separations {gaps} indicate overlap on all axes.",
            ))
            continue
        physical_gap = min(nonnegative)
        if physical_gap + gap_tol < min_gap:
            findings.append(Finding(
                "GAP_COLLAPSE",
                "ERROR",
                f"{a}<->{b}",
                None,
                None,
                None,
                f"Gap {physical_gap:.9f} is below minimum {min_gap:.9f}.",
            ))

    return findings


def build_report(source: str, config: Dict[str, Any], manifest: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    findings = scan_source(source, config) + scan_state_manifest(manifest, config)
    errors = [f for f in findings if f.severity == "ERROR"]
    holds = [f for f in findings if f.severity == "HOLD"]
    status = "FAIL" if errors else ("HOLD" if holds else "PASS")
    return {
        "schema": "studygrid.motion_invariant_scan.v1",
        "status": status,
        "candidate": config.get("candidate", "UNSPECIFIED"),
        "choreography": "UNSPECIFIED",
        "fps": float(config.get("fps", 30.0)),
        "summary": {
            "error_count": len(errors),
            "hold_count": len(holds),
            "finding_count": len(findings),
        },
        "findings": [asdict(f) for f in findings],
        "limitations": [
            "Static AST scan cannot prove rendered appearance, collision-free motion, or browser/WebGL parity.",
            "Dimension/gap validation requires an explicit final-state manifest.",
            "Dynamic exec/eval, custom handlers, drivers hidden behind helper abstractions, or generated code may require Blender-runtime instrumentation.",
            "Visibility exceptions must be declared explicitly in scanner config; undeclared hidden-path visibility animation is rejected.",
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, type=Path)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--state", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    source = args.source.read_text(encoding="utf-8")
    config = json.loads(args.config.read_text(encoding="utf-8"))
    manifest = json.loads(args.state.read_text(encoding="utf-8")) if args.state else None
    report = build_report(source, config, manifest)
    text = json.dumps(report, indent=2, sort_keys=True)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0 if report["status"] in {"PASS", "HOLD"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
