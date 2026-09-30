"""Generic nine-cube 3x3 invariant validator.

Pure Python; intentionally independent from final reveal order/choreography.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from math import isclose
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

Vec3 = Tuple[float, float, float]
UNIT_SCALE: Vec3 = (1.0, 1.0, 1.0)


@dataclass(frozen=True)
class CubeSpec:
    cube_id: str
    slot_id: str
    dimensions: Vec3 = (1.0, 1.0, 1.0)
    parent_id: Optional[str] = None
    independent_mesh: bool = True
    representation: str = "cube"
    scale_samples: Tuple[Vec3, ...] = (UNIT_SCALE,)


@dataclass(frozen=True)
class GridConfig:
    cube_size: float = 1.0
    gap: float = 0.10
    tolerance: float = 1e-6


@dataclass
class ValidationReport:
    ok: bool
    errors: List[str] = field(default_factory=list)
    slot_positions: Dict[str, Vec3] = field(default_factory=dict)
    adjacency: Dict[str, Tuple[str, ...]] = field(default_factory=dict)


def target_slots(config: GridConfig = GridConfig()) -> Dict[str, Vec3]:
    if config.cube_size <= 0:
        raise ValueError("cube_size must be positive")
    if config.gap <= 0:
        raise ValueError("gap must be positive to preserve deliberate air gaps")
    pitch = config.cube_size + config.gap
    slots: Dict[str, Vec3] = {}
    for row in range(3):
        for col in range(3):
            sid = f"r{row}c{col}"
            x = (col - 1) * pitch
            z = (1 - row) * pitch
            slots[sid] = (x, 0.0, z)
    return slots


def slot_adjacency(slots: Mapping[str, Vec3]) -> Dict[str, Tuple[str, ...]]:
    out: Dict[str, Tuple[str, ...]] = {}
    for row in range(3):
        for col in range(3):
            sid = f"r{row}c{col}"
            if sid not in slots:
                continue
            neighbours = []
            for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                rr, cc = row + dr, col + dc
                nid = f"r{rr}c{cc}"
                if 0 <= rr < 3 and 0 <= cc < 3 and nid in slots:
                    neighbours.append(nid)
            out[sid] = tuple(neighbours)
    return out


def _is_unit_scale(scale: Sequence[float], tol: float) -> bool:
    return len(scale) == 3 and all(isclose(float(v), 1.0, abs_tol=tol) for v in scale)


def validate_nine_cube_grid(cubes: Iterable[CubeSpec], config: GridConfig = GridConfig()) -> ValidationReport:
    cubes = tuple(cubes)
    errors: List[str] = []
    slots = target_slots(config)
    adjacency = slot_adjacency(slots)

    if len(cubes) != 9:
        errors.append(f"expected exactly 9 cubes; got {len(cubes)}")

    ids = [c.cube_id for c in cubes]
    if len(set(ids)) != len(ids):
        errors.append("cube IDs must be unique")

    occupied = [c.slot_id for c in cubes]
    unknown = sorted(set(occupied) - set(slots))
    if unknown:
        errors.append(f"unknown target slots: {unknown}")
    duplicates = sorted({sid for sid in occupied if occupied.count(sid) > 1})
    if duplicates:
        errors.append(f"duplicate slot occupancy: {duplicates}")
    missing = sorted(set(slots) - set(occupied))
    if missing:
        errors.append(f"missing target slots: {missing}")

    expected_dims = (config.cube_size,) * 3
    for c in cubes:
        if not c.independent_mesh or c.representation != "cube":
            errors.append(f"{c.cube_id}: fused/non-cube representation is not allowed")
        if len(c.dimensions) != 3 or any(
            not isclose(float(v), config.cube_size, abs_tol=config.tolerance)
            for v in c.dimensions
        ):
            errors.append(f"{c.cube_id}: dimension drift {c.dimensions}, expected {expected_dims}")
        if not c.scale_samples:
            errors.append(f"{c.cube_id}: scale_samples must include at least one sample")
        elif any(not _is_unit_scale(s, config.tolerance) for s in c.scale_samples):
            errors.append(f"{c.cube_id}: animated/non-unit object scale is not allowed")

    id_set = set(ids)
    for c in cubes:
        if c.parent_id is not None:
            if c.parent_id not in id_set:
                errors.append(f"{c.cube_id}: invalid parent reference {c.parent_id!r}")
            elif c.parent_id == c.cube_id:
                errors.append(f"{c.cube_id}: self-parent reference is invalid")

    parent_map = {c.cube_id: c.parent_id for c in cubes if c.cube_id in id_set}
    for start in id_set:
        seen = set()
        cur = start
        while cur is not None and cur in parent_map:
            if cur in seen:
                errors.append(f"parent cycle detected from {start}")
                break
            seen.add(cur)
            cur = parent_map.get(cur)

    pitch = config.cube_size + config.gap
    if pitch - config.cube_size <= config.tolerance:
        errors.append("slot pitch does not preserve a positive air gap")
    for sid, neighbours in adjacency.items():
        x, y, z = slots[sid]
        for nid in neighbours:
            nx, ny, nz = slots[nid]
            centre_distance = abs(nx-x) + abs(ny-y) + abs(nz-z)
            if centre_distance + config.tolerance < pitch:
                errors.append(f"slot spacing too small between {sid} and {nid}")

    deduped = list(dict.fromkeys(errors))
    return ValidationReport(ok=not deduped, errors=deduped, slot_positions=slots, adjacency=adjacency)
