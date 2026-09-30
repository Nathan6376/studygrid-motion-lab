#!/usr/bin/env python3
"""Read-only validator for future StudyGrid V4A Candidate A/C render artifacts.

The validator checks artifact completeness, file integrity, source/hash receipts,
MP4 metadata/decode, expected still inventory, and Bob's analytic geometry report.
It deliberately does NOT visually accept/reject Candidate A or C and never chooses
an owner-preferred candidate. Candidate visual/mechanical disposition stays HOLD
until an independent reviewer inspects the future render against the frozen matrix.

Usage:
  python tools/v4a_ac_artifact_validator.py PATH [--json]

PATH may be an artifact directory or ZIP. ZIP input is extracted to a temporary
folder. The input artifact is never modified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Optional

EXPECTED_BOB_HEAD = "b1a7843fcc05a825c1043d1fa060004a29e730b8"
EXPECTED_COMPARE_BLOB = "db9813aed09fc815b94d1693ea270db21ab0642c"
EXPECTED_GEOMETRY_BLOB = "19414f061e815e256a89eeb2f5d3e9af95056b00"
EXPECTED_GAP = 0.10
FLOAT_EPS = 1e-9

# Frozen evidence roles from Bob's comparison source. These names already exist in
# the source and therefore avoid inventing a new post-render naming convention.
REQUIRED_STILLS = {
    "front_start": ("front_00_start_stowed.png", r"front.*start.*stow.*\.png$"),
    "front_stage1_mid": ("front_01_stage1_mid.png", r"front.*stage1.*mid.*\.png$"),
    "front_stage1_landed": ("front_02_stage1_landed.png", r"front.*stage1.*land.*\.png$"),
    "front_stage2_mid": ("front_03_stage2_mid.png", r"front.*stage2.*mid.*\.png$"),
    "front_final": ("front_04_final.png", r"front.*final.*\.png$"),
    "diag_start": ("diag_00_start_stowed.png", r"diag.*start.*stow.*\.png$"),
}

SOURCE_MANIFEST_HINTS = ("manifest", "source", "runtime", "sha256", "receipt", "provenance")
GEOMETRY_REPORT_NAMES = ("v4a_hidden_geometry_report.json", "geometry_report.json")
HASH_LINE_RE = re.compile(r"\b([0-9a-fA-F]{64})\b(?:\s+[* ]?(.+))?")


@dataclass
class Check:
    status: str  # PASS / FAIL / HOLD / INFO
    key: str
    detail: str


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_extract_zip(src: Path, dst: Path) -> None:
    with zipfile.ZipFile(src, "r") as zf:
        bad = zf.testzip()
        if bad:
            raise ValueError(f"ZIP CRC failure at {bad}")
        for info in zf.infolist():
            member = Path(info.filename)
            if member.is_absolute() or ".." in member.parts:
                raise ValueError(f"unsafe ZIP member: {info.filename}")
        zf.extractall(dst)


def all_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*") if p.is_file())


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def find_by_name_or_regex(files: Iterable[Path], exact: str, pattern: str) -> Optional[Path]:
    lowered = exact.lower()
    for p in files:
        if p.name.lower() == lowered:
            return p
    rx = re.compile(pattern, re.I)
    for p in files:
        if rx.search(p.name):
            return p
    return None


def png_dimensions(path: Path) -> Optional[tuple[int, int]]:
    try:
        with path.open("rb") as f:
            header = f.read(24)
        if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
            return None
        return struct.unpack(">II", header[16:24])
    except OSError:
        return None


def run_cmd(args: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def ffprobe_video(path: Path) -> tuple[str, dict]:
    if shutil.which("ffprobe") is None:
        return "HOLD", {"detail": "ffprobe unavailable; MP4 metadata not runtime-verified."}
    cmd = [
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=codec_name,width,height,r_frame_rate,pix_fmt:format=duration",
        "-of", "json", str(path),
    ]
    code, out, err = run_cmd(cmd)
    if code != 0:
        return "FAIL", {"detail": f"ffprobe failed: {err or out}"}
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return "FAIL", {"detail": "ffprobe returned invalid JSON"}
    return "PASS", data


def ffmpeg_decode(path: Path) -> tuple[str, str]:
    if shutil.which("ffmpeg") is None:
        return "HOLD", "ffmpeg unavailable; full MP4 decode not runtime-verified."
    code, _out, err = run_cmd(["ffmpeg", "-v", "error", "-i", str(path), "-f", "null", "-"])
    if code != 0:
        return "FAIL", f"ffmpeg decode failed: {err}"
    return "PASS", "Full MP4 decode completed without ffmpeg errors."


def load_geometry_report(files: list[Path]) -> Optional[tuple[Path, dict]]:
    by_name = {p.name.lower(): p for p in files}
    for name in GEOMETRY_REPORT_NAMES:
        p = by_name.get(name.lower())
        if p:
            try:
                return p, json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                return p, {"__parse_error__": True}
    for p in files:
        if p.suffix.lower() == ".json" and "geometry" in p.name.lower():
            try:
                return p, json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                return p, {"__parse_error__": True}
    return None


def verify_geometry_report(report: dict) -> list[Check]:
    checks: list[Check] = []
    if report.get("__parse_error__"):
        return [Check("FAIL", "geometry_report", "Geometry report exists but is not valid JSON.")]
    try:
        a = report["A"]
        c = report["C"]
        gap = float(report["rest_gap"])
        floor_z = float(report["floor_z"])
    except Exception as exc:
        return [Check("FAIL", "geometry_report", f"Geometry report is missing required fields: {exc}")]

    checks.append(Check(
        "PASS" if abs(gap - EXPECTED_GAP) <= FLOAT_EPS else "FAIL",
        "geometry_gap_contract",
        f"Reported resting-gap contract={gap:.12g}L; expected {EXPECTED_GAP:.2f}L.",
    ))

    a_ok = (
        int(a.get("colliding_samples", -1)) == 0
        and float(a.get("minimum_floor_clearance", -1)) > 0
        and abs(float(a.get("final_rest_gap", -999)) - EXPECTED_GAP) <= FLOAT_EPS
    )
    checks.append(Check(
        "PASS" if a_ok else "FAIL",
        "geometry_A",
        "A analytic report requires zero colliding samples, positive floor clearance and 0.10L final gap. "
        f"Observed colliding={a.get('colliding_samples')}, floor={a.get('minimum_floor_clearance')}, gap={a.get('final_rest_gap')}.",
    ))

    c_ok = (
        int(c.get("stage1_colliding_samples", -1)) == 0
        and int(c.get("stage2_colliding_samples", -1)) == 0
        and float(c.get("stage1_minimum_floor_clearance", -1)) > 0
        and float(c.get("stage2_minimum_floor_clearance", -1)) > 0
        and abs(float(c.get("final_rest_gap", -999)) - EXPECTED_GAP) <= FLOAT_EPS
        and str(c.get("visibility_toggle", "")).lower() == "none"
        and bool(c.get("front_camera_start_fully_occluded"))
    )
    checks.append(Check(
        "PASS" if c_ok else "FAIL",
        "geometry_C",
        "C analytic report requires zero collisions in both stages, positive floor clearance, 0.10L final gap, no visibility toggle, and true exact-front start occlusion. "
        f"Observed stage1_colliding={c.get('stage1_colliding_samples')}, stage2_colliding={c.get('stage2_colliding_samples')}, "
        f"floor1={c.get('stage1_minimum_floor_clearance')}, floor2={c.get('stage2_minimum_floor_clearance')}, "
        f"gap={c.get('final_rest_gap')}, visibility_toggle={c.get('visibility_toggle')}, occluded={c.get('front_camera_start_fully_occluded')}.",
    ))
    checks.append(Check("INFO", "geometry_floor", f"Report floor_z={floor_z:.12g}L."))
    return checks


def text_candidates(files: list[Path]) -> list[Path]:
    return [p for p in files if p.suffix.lower() in {".txt", ".md", ".json", ".yml", ".yaml", ".py", ".sha256"}]


def search_provenance(files: list[Path]) -> tuple[bool, bool, list[str]]:
    bob = False
    blob = False
    hits: list[str] = []
    for p in text_candidates(files):
        try:
            s = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        low_name = p.name.lower()
        if any(h in low_name for h in SOURCE_MANIFEST_HINTS) or p.suffix.lower() in {".json", ".py"}:
            if EXPECTED_BOB_HEAD in s:
                bob = True
                hits.append(f"{p.name}:bob-head")
            if EXPECTED_COMPARE_BLOB in s:
                blob = True
                hits.append(f"{p.name}:compare-blob")
    return bob, blob, sorted(set(hits))


def verify_hash_receipts(files: list[Path], root: Path) -> list[Check]:
    checks: list[Check] = []
    receipts = [p for p in files if "sha256" in p.name.lower() or p.suffix.lower() == ".sha256"]
    if not receipts:
        return [Check("HOLD", "hash_receipts", "No SHA-256 receipt found in artifact; external run/artifact hash binding is still required.")]
    any_verified = False
    for receipt in receipts:
        try:
            text = receipt.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            checks.append(Check("FAIL", "hash_receipt_read", f"Cannot read {rel(receipt, root)}: {exc}"))
            continue
        for line in text.splitlines():
            m = HASH_LINE_RE.search(line.strip())
            if not m or not m.group(2):
                continue
            expected, name = m.group(1).lower(), m.group(2).strip().lstrip("*")
            target = (receipt.parent / name).resolve()
            try:
                target.relative_to(root.resolve())
            except ValueError:
                continue
            if not target.is_file():
                alt = root / name
                if alt.is_file():
                    target = alt
                else:
                    checks.append(Check("FAIL", "hash_receipt_target", f"{rel(receipt, root)} references missing file {name}."))
                    continue
            actual = sha256_file(target)
            if actual != expected:
                checks.append(Check("FAIL", "hash_receipt_mismatch", f"{name}: expected {expected}, got {actual}."))
            else:
                any_verified = True
                checks.append(Check("PASS", "hash_receipt_match", f"{name}: SHA-256 receipt matches."))
    if not any_verified and not any(c.status == "FAIL" for c in checks):
        checks.append(Check("HOLD", "hash_receipts", "SHA-256 receipt files exist but no filename-bound hash line could be verified automatically."))
    return checks


def validate(path: Path) -> dict:
    checks: list[Check] = []
    temp: Optional[tempfile.TemporaryDirectory] = None
    artifact_zip_sha = None
    if not path.exists():
        return {"error": f"Artifact path does not exist: {path}", "exit_code": 2}
    try:
        if path.is_file():
            if path.suffix.lower() != ".zip":
                return {"error": "Artifact input must be a directory or ZIP file.", "exit_code": 2}
            artifact_zip_sha = sha256_file(path)
            temp = tempfile.TemporaryDirectory(prefix="studygrid-v4a-ac-")
            root = Path(temp.name)
            try:
                safe_extract_zip(path, root)
                checks.append(Check("PASS", "zip_integrity", f"ZIP CRC/path integrity passed; SHA-256={artifact_zip_sha}."))
            except Exception as exc:
                return {"error": f"ZIP integrity/extraction failed: {exc}", "exit_code": 2}
        else:
            root = path
            checks.append(Check("INFO", "artifact_input", "Directory input; no enclosing ZIP hash available."))

        files = all_files(root)
        checks.append(Check("PASS" if files else "FAIL", "artifact_inventory", f"Artifact contains {len(files)} files."))

        still_map = {}
        for role, (exact, pattern) in REQUIRED_STILLS.items():
            found = find_by_name_or_regex(files, exact, pattern)
            if found is None:
                checks.append(Check("FAIL", f"still_{role}", f"Missing required still role {role} (expected {exact} or equivalent name)."))
                continue
            dims = png_dimensions(found)
            if dims is None:
                checks.append(Check("FAIL", f"still_{role}", f"{rel(found, root)} is not a valid PNG header/IHDR."))
            else:
                still_map[role] = {"file": rel(found, root), "width": dims[0], "height": dims[1], "sha256": sha256_file(found)}
                checks.append(Check("PASS", f"still_{role}", f"{rel(found, root)} valid PNG {dims[0]}x{dims[1]}."))

        videos = [p for p in files if p.suffix.lower() == ".mp4"]
        video_meta = []
        if not videos:
            frame_files = [p for p in files if p.suffix.lower() == ".png" and "frame" in p.name.lower()]
            if frame_files:
                checks.append(Check("HOLD", "motion_evidence", f"No MP4 found; {len(frame_files)} frame PNGs may be an equivalent sequence, but inspectability must be reviewed manually."))
            else:
                checks.append(Check("FAIL", "motion_evidence", "No MP4 and no obvious frame sequence found."))
        else:
            any_decode_pass = False
            for video in videos:
                pstat, pmeta = ffprobe_video(video)
                dstat, ddetail = ffmpeg_decode(video)
                if pstat == "PASS" and dstat == "PASS":
                    any_decode_pass = True
                checks.append(Check(pstat, "mp4_metadata", f"{rel(video, root)}: {pmeta.get('detail', 'ffprobe metadata parsed.')}"))
                checks.append(Check(dstat, "mp4_decode", f"{rel(video, root)}: {ddetail}"))
                video_meta.append({"file": rel(video, root), "sha256": sha256_file(video), "ffprobe_status": pstat, "ffprobe": pmeta, "decode_status": dstat})
            if any_decode_pass:
                checks.append(Check("PASS", "motion_evidence", "At least one MP4 has valid metadata and full decode."))
            elif any(c.status == "FAIL" and c.key in {"mp4_metadata", "mp4_decode"} for c in checks):
                checks.append(Check("FAIL", "motion_evidence", "MP4 files exist but no video passed metadata+decode validation."))
            else:
                checks.append(Check("HOLD", "motion_evidence", "MP4 files exist, but local ffprobe/ffmpeg capability was insufficient to complete decode verification."))

        geo = load_geometry_report(files)
        geometry_file = None
        if geo is None:
            checks.append(Check("HOLD", "geometry_report", "No geometry report found in artifact; bind Bob's exact source/analytic report externally before candidate acceptance."))
        else:
            geometry_file, report = geo
            checks.append(Check("PASS", "geometry_report_present", f"Found {rel(geometry_file, root)}; SHA-256={sha256_file(geometry_file)}."))
            checks.extend(verify_geometry_report(report))

        bob_seen, blob_seen, provenance_hits = search_provenance(files)
        if bob_seen and blob_seen:
            checks.append(Check("PASS", "source_provenance", "Artifact text binds to Bob comparison head and comparison source blob: " + ", ".join(provenance_hits)))
        elif bob_seen:
            checks.append(Check("HOLD", "source_provenance", "Bob comparison head is recorded, but comparison source blob identity was not found. External executed-source hash/diff binding is still required."))
        else:
            checks.append(Check("HOLD", "source_provenance", "Artifact does not self-record Bob comparison head/source blob. Reviewer must bind the render run head and executed source to Bob's fixed mechanics or a documented render-only derivative before acceptance."))

        checks.extend(verify_hash_receipts(files, root))

        png_dims = {(v["width"], v["height"]) for v in still_map.values()}
        if len(png_dims) <= 1 and still_map:
            checks.append(Check("PASS", "still_resolution_uniformity", f"Required stills share one resolution: {next(iter(png_dims))}."))
        elif still_map:
            checks.append(Check("HOLD", "still_resolution_uniformity", f"Required stills use mixed resolutions {sorted(png_dims)}; confirm this did not change camera/comparison conditions."))

        checks.append(Check("HOLD", "candidate_A_visual_acceptance", "Not evaluated automatically. Independent reviewer must inspect A start/motion/final frames against the frozen acceptance matrix."))
        checks.append(Check("HOLD", "candidate_C_visual_acceptance", "Not evaluated automatically. Independent reviewer must inspect C exact-front occlusion, oblique rear-stow proof, stage sequence and final rest against the frozen acceptance matrix."))
        checks.append(Check("INFO", "owner_choice", "No owner hinge preference is inferred from validator results."))

        counts = {status: sum(1 for c in checks if c.status == status) for status in ("PASS", "FAIL", "HOLD", "INFO")}
        artifact_ready = counts["FAIL"] == 0 and all(
            any(c.key == key and c.status == "PASS" for c in checks)
            for key in ("motion_evidence", "still_front_start", "still_front_final", "still_diag_start")
        )
        return {
            "tool": "StudyGrid V4A A/C artifact validator",
            "contract": {
                "expected_bob_head": EXPECTED_BOB_HEAD,
                "expected_compare_source_blob": EXPECTED_COMPARE_BLOB,
                "expected_geometry_report_blob": EXPECTED_GEOMETRY_BLOB,
                "rest_gap_L": EXPECTED_GAP,
            },
            "input": str(path),
            "artifact_zip_sha256": artifact_zip_sha,
            "summary": counts,
            "artifact_ready_for_manual_acceptance": artifact_ready,
            "candidate_A_status": "HOLD_PENDING_MANUAL_VISUAL_ACCEPTANCE",
            "candidate_C_status": "HOLD_PENDING_MANUAL_VISUAL_ACCEPTANCE",
            "owner_hinge_choice": "HOLD",
            "stills": still_map,
            "videos": video_meta,
            "geometry_report_file": rel(geometry_file, root) if geometry_file else None,
            "checks": [asdict(c) for c in checks],
            "input_mutated": False,
        }
    finally:
        if temp is not None:
            temp.cleanup()


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate future V4A A/C render artifact without judging a winner")
    parser.add_argument("artifact", type=Path, help="Artifact ZIP or extracted directory")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()
    payload = validate(args.artifact)
    if "error" in payload:
        print(payload["error"], file=sys.stderr)
        return int(payload.get("exit_code", 2))
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        s = payload["summary"]
        print(f"StudyGrid V4A A/C artifact validator — PASS {s['PASS']} / FAIL {s['FAIL']} / HOLD {s['HOLD']} / INFO {s['INFO']}")
        for c in payload["checks"]:
            print(f"[{c['status']}] {c['key']}: {c['detail']}")
        print(f"Artifact ready for manual acceptance: {payload['artifact_ready_for_manual_acceptance']}")
        print("Candidate A: HOLD pending independent visual acceptance")
        print("Candidate C: HOLD pending independent visual acceptance")
        print("Owner hinge choice: HOLD")
        print("Input mutation: NONE")
    return 1 if payload["summary"]["FAIL"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
