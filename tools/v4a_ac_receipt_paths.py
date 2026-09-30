from __future__ import annotations

import hashlib
import re
from pathlib import Path, PurePosixPath
from typing import Iterable

HASH_LINE_RE = re.compile(r"\b([0-9a-fA-F]{64})\b(?:\s+[* ]?(.+))?")
SAFE_FLATTENABLE_PREFIXES = frozenset({"output-v4a-hidden"})


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _safe_receipt_parts(raw_name: str) -> tuple[str, ...]:
    name = raw_name.strip().lstrip("*")
    if not name or "\\" in name:
        raise ValueError("empty or backslash-containing receipt path")
    p = PurePosixPath(name)
    if p.is_absolute() or any(part in {"", ".", ".."} for part in p.parts):
        raise ValueError("unsafe receipt path")
    return p.parts


def resolve_receipt_target(raw_name: str, receipt: Path, root: Path) -> tuple[Path, str]:
    parts = _safe_receipt_parts(raw_name)
    root_resolved = root.resolve()
    candidates: list[tuple[Path, str]] = []
    seen: set[Path] = set()

    def add_candidate(path: Path, mode: str) -> None:
        resolved = path.resolve()
        try:
            resolved.relative_to(root_resolved)
        except ValueError as exc:
            raise ValueError("receipt target escapes artifact root") from exc
        if resolved.is_file() and resolved not in seen:
            seen.add(resolved)
            candidates.append((resolved, mode))

    add_candidate(receipt.parent.joinpath(*parts), "receipt-relative")
    add_candidate(root.joinpath(*parts), "root-relative")

    if len(parts) >= 2 and parts[0] in SAFE_FLATTENABLE_PREFIXES:
        prefix_dir = root / parts[0]
        if not prefix_dir.exists():
            add_candidate(root.joinpath(*parts[1:]), f"flattened-known-prefix:{parts[0]}")

    if not candidates:
        raise FileNotFoundError(raw_name)
    if len(candidates) != 1:
        modes = ", ".join(mode for _p, mode in candidates)
        raise RuntimeError(f"ambiguous receipt target ({modes})")
    return candidates[0]


def verify_hash_receipts(files: Iterable[Path], root: Path, Check):
    checks = []
    files = list(files)
    receipts = [p for p in files if "sha256" in p.name.lower() or p.suffix.lower() == ".sha256"]
    if not receipts:
        return [Check("HOLD", "hash_receipts", "No SHA-256 receipt found in artifact; external run/artifact hash binding is still required.")]

    any_verified = False
    root_resolved = root.resolve()
    for receipt in receipts:
        try:
            text = receipt.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            checks.append(Check("FAIL", "hash_receipt_read", f"Cannot read {receipt.relative_to(root)}: {exc}"))
            continue

        mapped_targets: dict[str, str] = {}
        for line in text.splitlines():
            m = HASH_LINE_RE.search(line.strip())
            if not m or not m.group(2):
                continue
            expected = m.group(1).lower()
            raw_name = m.group(2).strip().lstrip("*")

            try:
                target, mode = resolve_receipt_target(raw_name, receipt, root)
            except ValueError as exc:
                checks.append(Check("FAIL", "hash_receipt_unsafe_path", f"{raw_name}: {exc}."))
                continue
            except RuntimeError as exc:
                checks.append(Check("FAIL", "hash_receipt_ambiguous", f"{raw_name}: {exc}."))
                continue
            except FileNotFoundError:
                checks.append(Check("FAIL", "hash_receipt_target", f"{receipt.relative_to(root)} references missing file {raw_name}."))
                continue

            canonical = target.resolve().relative_to(root_resolved).as_posix()
            previous = mapped_targets.get(canonical)
            if previous is not None:
                checks.append(Check("FAIL", "hash_receipt_duplicate_normalized_path", f"{raw_name} and {previous} both normalize to {canonical}."))
                continue
            mapped_targets[canonical] = raw_name

            actual = sha256_file(target)
            if actual != expected:
                checks.append(Check("FAIL", "hash_receipt_mismatch", f"{raw_name}: expected {expected}, got {actual}."))
            else:
                any_verified = True
                checks.append(Check("PASS", "hash_receipt_match", f"{raw_name} -> {canonical} ({mode}): SHA-256 receipt matches."))

    if not any_verified and not any(c.status == "FAIL" for c in checks):
        checks.append(Check("HOLD", "hash_receipts", "SHA-256 receipt files exist but no filename-bound hash line could be verified automatically."))
    return checks
