#!/usr/bin/env python3
"""Read-only StudyGrid V4A Blender export preflight.

Run inside Blender, for example:
  blender studygrid-v4a.blend --background --python tools/v4a_export_preflight.py -- --json

This utility intentionally performs no scene mutation, export, frame changes, saves, or writes
inside the .blend. It only reads the currently opened Blender data and prints a report.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, asdict
from typing import Optional

try:
    import bpy  # type: ignore
except ModuleNotFoundError:
    print("BLOCKED: bpy is unavailable. Run this utility inside Blender.", file=sys.stderr)
    raise SystemExit(3)

EXPECTED_OBJECTS = {
    "SG_Floor": "MESH", "SG_Key": "LIGHT", "SG_Fill": "LIGHT", "SG_Rim": "LIGHT",
    "SG_Camera": "CAMERA", "SG_G_PROVISIONAL": "CURVE", "Seed": "MESH",
    "A_Parent": "MESH", "A_Child": "MESH", "A_Hinge": "EMPTY",
    "C_Parent": "MESH", "C_Child": "MESH", "C_Hinge_Rise": "EMPTY", "C_Hinge_Settle": "EMPTY",
    "Chain_C": "MESH", "Chain_E": "MESH", "Chain_SE": "MESH",
    "Chain_Hinge_E": "EMPTY", "Chain_Hinge_SE": "EMPTY",
    "Doorway": "MESH", "Door_L": "MESH", "Door_R": "MESH", "Door_U": "MESH", "Door_D": "MESH",
}
EXPECTED_PARENTAGE = {
    "A_Child": "A_Hinge", "C_Hinge_Settle": "C_Hinge_Rise", "C_Child": "C_Hinge_Settle",
    "Chain_E": "Chain_Hinge_E", "Chain_Hinge_SE": "Chain_E", "Chain_SE": "Chain_Hinge_SE",
}
CUBE_OBJECTS = [
    "Seed", "A_Parent", "A_Child", "C_Parent", "C_Child", "Chain_C", "Chain_E", "Chain_SE",
    "Doorway", "Door_L", "Door_R", "Door_U", "Door_D",
]
QA_ONLY_OBJECTS = {
    "SG_Floor", "SG_Key", "SG_Fill", "SG_Rim", "SG_G_PROVISIONAL", "Seed",
    "C_Parent", "C_Child", "C_Hinge_Rise", "C_Hinge_Settle",
}
VISIBILITY_PATHS = {"hide_render", "hide_viewport"}
EPS = 1e-5

@dataclass
class Finding:
    status: str
    key: str
    detail: str

def add(findings: list[Finding], status: str, key: str, detail: str) -> None:
    findings.append(Finding(status, key, detail))

def close(a: float, b: float, eps: float = EPS) -> bool:
    return abs(float(a) - float(b)) <= eps

def unit_scale(obj) -> bool:
    return all(close(v, 1.0) for v in obj.scale)

def fcurves(owner) -> list:
    ad = getattr(owner, "animation_data", None)
    action = getattr(ad, "action", None) if ad else None
    if action is None:
        return []
    curves = getattr(action, "fcurves", None)
    if curves is None:
        return []
    try:
        return list(curves)
    except Exception:
        return []

def paths(owner) -> set[str]:
    return {getattr(fc, "data_path", "") for fc in fcurves(owner)}

def key_values(owner, path: str) -> list[float]:
    vals: list[float] = []
    for fc in fcurves(owner):
        if getattr(fc, "data_path", "") == path:
            for kp in getattr(fc, "keyframe_points", []):
                try:
                    vals.append(float(kp.co.y))
                except Exception:
                    pass
    return vals

def mesh_identity(obj) -> Optional[int]:
    data = getattr(obj, "data", None)
    if data is None:
        return None
    ptr = getattr(data, "as_pointer", None)
    if callable(ptr):
        try:
            return int(ptr())
        except Exception:
            pass
    return id(data)

def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only StudyGrid V4A export readiness preflight")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    findings: list[Finding] = []
    scene = bpy.context.scene

    missing, wrong_type = [], []
    for name, typ in EXPECTED_OBJECTS.items():
        obj = bpy.data.objects.get(name)
        if obj is None:
            missing.append(name)
        elif obj.type != typ:
            wrong_type.append(f"{name}:{obj.type}!={typ}")
    if missing:
        add(findings, "FAIL", "expected_objects", "Missing: " + ", ".join(sorted(missing)))
    elif wrong_type:
        add(findings, "FAIL", "expected_objects", "Wrong types: " + ", ".join(sorted(wrong_type)))
    else:
        add(findings, "PASS", "expected_objects", f"All {len(EXPECTED_OBJECTS)} expected V4A QA objects are present with expected types.")

    parent_errors = []
    for child_name, parent_name in EXPECTED_PARENTAGE.items():
        child = bpy.data.objects.get(child_name)
        actual = getattr(getattr(child, "parent", None), "name", None) if child else None
        if actual != parent_name:
            parent_errors.append(f"{child_name}->{actual or 'NONE'} expected {parent_name}")
    if parent_errors:
        add(findings, "FAIL", "parentage", "; ".join(parent_errors))
    else:
        add(findings, "PASS", "parentage", "Expected 2A, 2C and C→E→SE parent relationships are present.")

    scaled = []
    for obj in bpy.data.objects:
        if obj.type in {"MESH", "CURVE", "EMPTY", "CAMERA"} and not unit_scale(obj):
            scaled.append(f"{obj.name}={tuple(round(float(v), 6) for v in obj.scale)}")
    if scaled:
        add(findings, "FAIL", "object_scales", "Non-unit current object scales: " + ", ".join(scaled))
    else:
        add(findings, "PASS", "object_scales", "Current export-relevant object scales are unit scale.")

    scale_animated = [obj.name for obj in bpy.data.objects if "scale" in paths(obj)]
    if scale_animated:
        add(findings, "WARN", "scale_animation", "Scale animation exists on: " + ", ".join(sorted(scale_animated)) + ". Current Seed use is diagnostic-only; production export must not inherit it silently.")
    else:
        add(findings, "PASS", "scale_animation", "No object scale animation detected.")

    mesh_objs = [bpy.data.objects.get(n) for n in CUBE_OBJECTS]
    mesh_objs = [o for o in mesh_objs if o is not None and o.type == "MESH"]
    identities = [mesh_identity(o) for o in mesh_objs]
    unique_meshes = len(set(identities)) if identities else 0
    if mesh_objs and unique_meshes == 1:
        add(findings, "PASS", "cube_mesh_reuse", f"{len(mesh_objs)} cube objects share one mesh datablock.")
    else:
        add(findings, "WARN", "cube_mesh_reuse", f"{len(mesh_objs)} cube objects use {unique_meshes} mesh datablocks; current QA scene is not instancing-ready as authored.")

    modifier_rows, shape_modifier_conflicts = [], []
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        mods = [m.type for m in obj.modifiers]
        if mods:
            modifier_rows.append(f"{obj.name}:{'/'.join(mods)}")
        shape_keys = getattr(getattr(obj, "data", None), "shape_keys", None)
        if shape_keys is not None and mods:
            shape_modifier_conflicts.append(obj.name)
    if modifier_rows:
        add(findings, "WARN", "mesh_modifiers", "Export-sensitive meshes retain modifiers: " + ", ".join(sorted(modifier_rows)) + ". Lock evaluated/baked export behaviour later; do not apply them to the QA scene here.")
    else:
        add(findings, "PASS", "mesh_modifiers", "No mesh modifiers detected.")
    if shape_modifier_conflicts:
        add(findings, "FAIL", "shape_key_modifier_conflict", "Shape keys coexist with modifiers on: " + ", ".join(sorted(shape_modifier_conflicts)))
    else:
        add(findings, "PASS", "shape_key_modifier_conflict", "No current mesh has both shape keys and modifiers.")

    g = bpy.data.objects.get("SG_G_PROVISIONAL")
    if g and g.type == "CURVE":
        if "bevel_depth" in paths(g.data):
            add(findings, "WARN", "provisional_g_animation", "SG_G_PROVISIONAL animates Curve.bevel_depth. Treat this as QA-only; do not assume a GLB/Three.js round-trip preserves this Blender data animation.")
        else:
            add(findings, "WARN", "provisional_g_animation", "SG_G_PROVISIONAL is a CURVE and remains non-canonical; future canonical-G export topology is still held.")

    cam_obj = bpy.data.objects.get("SG_Camera")
    if cam_obj is None or cam_obj.type != "CAMERA":
        add(findings, "FAIL", "camera", "SG_Camera is missing or not a camera.")
    else:
        cam = cam_obj.data
        if cam.sensor_fit == "VERTICAL" and close(cam.lens, 50.0, 1e-4):
            angle_y_deg = math.degrees(float(cam.angle_y))
            add(findings, "PASS", "camera", f"SG_Camera uses 50 mm and VERTICAL sensor fit; Blender-reported angle_y={angle_y_deg:.6f}° (exported glTF yfov must still be round-trip verified).")
        else:
            add(findings, "FAIL", "camera", f"Expected 50 mm + VERTICAL; found lens={cam.lens}, sensor_fit={cam.sensor_fit}.")
        lens_vals = key_values(cam, "lens")
        if lens_vals and all(close(v, 50.0, 1e-4) for v in lens_vals):
            add(findings, "PASS", "camera_lens_animation", f"All {len(lens_vals)} keyed lens values are 50 mm; no animated FOV zoom detected.")
        elif lens_vals:
            add(findings, "FAIL", "camera_lens_animation", "Camera lens animation changes focal length: " + ", ".join(f"{v:.4f}" for v in lens_vals))
        else:
            add(findings, "WARN", "camera_lens_animation", "No lens F-curve found; verify fixed-FOV export from the actual approved asset.")

    vis_users = []
    for obj in bpy.data.objects:
        used = sorted(paths(obj) & VISIBILITY_PATHS)
        if used:
            vis_users.append(f"{obj.name}({','.join(used)})")
    if vis_users:
        add(findings, "WARN", "visibility_animation", f"Blender visibility keyframes exist on {len(vis_users)} objects. Move study visibility to the Three.js/runtime schedule; do not rely on GLB carrying hide_render/hide_viewport. " + "; ".join(vis_users))
    else:
        add(findings, "PASS", "visibility_animation", "No Blender visibility keyframes detected.")

    area_lights = [o.name for o in bpy.data.objects if o.type == "LIGHT" and getattr(o.data, "type", None) == "AREA"]
    if area_lights:
        add(findings, "WARN", "area_lights", "AREA lights present: " + ", ".join(sorted(area_lights)) + ". Rebuild/override web lighting; do not treat these as portable GLB lighting.")
    else:
        add(findings, "PASS", "area_lights", "No AREA lights detected.")

    mat_names = {m.name for m in bpy.data.materials}
    if "SG_Green" in mat_names:
        add(findings, "WARN", "materials", "SG_Green exists as a QA placeholder. Runtime material/colour/lighting remain an explicit web override boundary.")
    else:
        add(findings, "WARN", "materials", "Expected QA material SG_Green is absent; verify material mapping before any export test.")

    marker_empties = [o.name for o in bpy.data.objects if o.type == "EMPTY" and any(tok in o.name.lower() for tok in ("door", "handoff", "export"))]
    if marker_empties:
        add(findings, "PASS", "doorway_markers", "Dedicated doorway/export marker empties detected: " + ", ".join(sorted(marker_empties)))
    else:
        add(findings, "WARN", "doorway_markers", "No dedicated doorway/export marker empty is present. Current handoff is encoded only in camera/object animation; add explicit runtime markers/metadata later, after mechanics approval.")

    qa_present = sorted(name for name in QA_ONLY_OBJECTS if bpy.data.objects.get(name) is not None)
    if qa_present:
        add(findings, "WARN", "production_subset", "Diagnostic/provisional objects are present and must not ship wholesale as production runtime state: " + ", ".join(qa_present))
    if bpy.data.objects.get("C_Parent") or bpy.data.objects.get("C_Child"):
        add(findings, "WARN", "study_2c_hold", "Study 2C objects are present, but Study 2C remains unresolved and excluded from production acceptance.")

    counts = {s: sum(1 for f in findings if f.status == s) for s in ("PASS", "WARN", "FAIL")}
    payload = {
        "tool": "StudyGrid V4A export preflight",
        "blender_version": getattr(bpy.app, "version_string", "unknown"),
        "blend_file": getattr(bpy.data, "filepath", ""),
        "scene": getattr(scene, "name", ""),
        "summary": counts,
        "findings": [asdict(f) for f in findings],
        "mutated_scene": False,
    }
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False))
    else:
        print(f"StudyGrid V4A export preflight — PASS {counts['PASS']} / WARN {counts['WARN']} / FAIL {counts['FAIL']}")
        for f in findings:
            print(f"[{f.status}] {f.key}: {f.detail}")
        print("Scene mutation: NONE")
    return 2 if counts["FAIL"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
