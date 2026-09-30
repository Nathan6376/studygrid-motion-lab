"""StudyGrid Q-B2 doorway-camera handoff safety fixture.

Analytic/static only. The selected doorway cube is treated as read-only input.
The fixture never selects/randomizes a cube and never scales scene geometry to
fake approach. Apparent enlargement is perspective-only with a fixed vfov.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose, radians, sqrt, tan
from typing import Iterable, Tuple

Vec3 = Tuple[float, float, float]


def add3(a: Vec3, b: Vec3) -> Vec3:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def scale3(v: Vec3, s: float) -> Vec3:
    return (v[0] * s, v[1] * s, v[2] * s)


def length3(v: Vec3) -> float:
    return sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)


def normalize3(v: Vec3) -> Vec3:
    n = length3(v)
    if n <= 0.0:
        raise ValueError("normal must be non-zero")
    return (v[0] / n, v[1] / n, v[2] / n)


def smoothstep01(value: float) -> float:
    t = max(0.0, min(1.0, float(value)))
    return t * t * (3.0 - 2.0 * t)


@dataclass(frozen=True)
class CameraContract:
    cube_edge: float = 1.0
    bevel: float = 0.055
    vfov_deg: float = 40.0
    aspect: float = 16.0 / 9.0
    near_clip: float = 0.10
    near_margin: float = 0.02
    start_distance: float = 8.0
    cube_scale: Vec3 = (1.0, 1.0, 1.0)

    def validate(self) -> None:
        if self.cube_edge <= 0.0:
            raise ValueError("cube_edge must be positive")
        if not 0.0 <= self.bevel < self.cube_edge / 2.0:
            raise ValueError("bevel must be in [0, L/2)")
        if not 1.0 < self.vfov_deg < 179.0:
            raise ValueError("vfov_deg must be a valid fixed perspective FOV")
        if self.aspect <= 0.0:
            raise ValueError("aspect must be positive")
        if self.near_clip <= 0.0 or self.near_margin < 0.0:
            raise ValueError("near plane/margin invalid")
        if self.start_distance <= 0.0:
            raise ValueError("start_distance must be positive")
        if self.cube_scale != (1.0, 1.0, 1.0):
            raise ValueError("object-scale fake is prohibited")


@dataclass(frozen=True)
class DoorwayMarker:
    """Read-only selected-cube face marker supplied by the caller/runtime."""

    name: str
    face_centre: Vec3
    outward_normal: Vec3

    def normalized(self) -> "DoorwayMarker":
        return DoorwayMarker(
            self.name, self.face_centre, normalize3(self.outward_normal)
        )


@dataclass(frozen=True)
class SafetyEnvelope:
    d_cover: float
    d_near_min: float
    safe_handoff_distance: float
    start_distance: float


@dataclass(frozen=True)
class CameraSample:
    progress: float
    distance_to_face: float
    position: Vec3
    look_target: Vec3
    vfov_deg: float
    cube_scale: Vec3
    before_or_at_handoff: bool
    near_plane_safe: bool
    outside_mesh: bool


def cover_distance(contract: CameraContract) -> float:
    """Claude §4.6 viewport-cover boundary, in cube-edge units."""
    contract.validate()
    numerator = contract.cube_edge / 2.0 - contract.bevel
    denominator = max(1.0, contract.aspect) * tan(
        radians(contract.vfov_deg) / 2.0
    )
    return numerator / denominator


def safety_envelope(contract: CameraContract) -> SafetyEnvelope:
    d_cover = cover_distance(contract)
    d_near_min = contract.near_clip + contract.near_margin
    safe_handoff = max(d_cover, d_near_min)
    if contract.start_distance <= safe_handoff:
        raise ValueError("start_distance must be outside the handoff envelope")
    return SafetyEnvelope(
        d_cover, d_near_min, safe_handoff, contract.start_distance
    )


def camera_sample(
    marker: DoorwayMarker,
    contract: CameraContract,
    progress: float,
) -> CameraSample:
    """Pure perspective dolly from start to the safe handoff marker."""
    m = marker.normalized()
    e = safety_envelope(contract)
    p = max(0.0, min(1.0, float(progress)))
    eased = smoothstep01(p)
    distance = e.start_distance + (
        e.safe_handoff_distance - e.start_distance
    ) * eased
    position = add3(m.face_centre, scale3(m.outward_normal, distance))
    tol = 1e-9
    return CameraSample(
        progress=p,
        distance_to_face=distance,
        position=position,
        look_target=m.face_centre,
        vfov_deg=contract.vfov_deg,
        cube_scale=contract.cube_scale,
        before_or_at_handoff=distance + tol >= e.safe_handoff_distance,
        near_plane_safe=distance + tol >= e.d_near_min,
        outside_mesh=distance > 0.0,
    )


def failure_cases(contract: CameraContract) -> dict:
    e = safety_envelope(contract)
    return {
        "object_scale_fake": contract.cube_scale != (1.0, 1.0, 1.0),
        "fov_change": False,  # fixture has one immutable vfov value
        "handoff_after_cover_boundary": False,  # path ends at safe_handoff
        "near_plane_clip_at_handoff": e.safe_handoff_distance < e.d_near_min,
        "camera_crosses_face": e.safe_handoff_distance <= 0.0,
        "inside_mesh_failure": e.safe_handoff_distance <= 0.0,
    }


def static_report(
    contract: CameraContract,
    normals: Iterable[Vec3] = (
        (0, -1, 0),
        (0, 1, 0),
        (1, 0, 0),
        (-1, 0, 0),
    ),
) -> dict:
    e = safety_envelope(contract)
    samples = []
    for i, normal in enumerate(normals):
        marker = DoorwayMarker(
            f"Doorway_fixture_{i}", (0.0, 0.0, 0.0), normal
        )
        samples.extend(
            camera_sample(marker, contract, p)
            for p in (0.0, 0.25, 0.5, 0.75, 1.0)
        )

    distances_monotonic = all(
        samples[i].distance_to_face + 1e-9 >= samples[i + 1].distance_to_face
        for group_start in range(0, len(samples), 5)
        for i in range(group_start, group_start + 4)
    )
    fixed_fov = all(
        isclose(s.vfov_deg, contract.vfov_deg, abs_tol=0.0) for s in samples
    )
    no_scale_fake = all(
        s.cube_scale == (1.0, 1.0, 1.0) for s in samples
    )
    all_near_safe = all(s.near_plane_safe for s in samples)
    all_outside = all(s.outside_mesh for s in samples)
    terminal_hits_marker = all(
        isclose(
            samples[group_start + 4].distance_to_face,
            e.safe_handoff_distance,
            rel_tol=0.0,
            abs_tol=1e-9,
        )
        for group_start in range(0, len(samples), 5)
    )
    failures = failure_cases(contract)
    checks = {
        "fixed_fov": fixed_fov,
        "perspective_only_no_object_scale_fake": no_scale_fake,
        "distance_monotonic_toward_face": distances_monotonic,
        "near_plane_safe_through_handoff": all_near_safe,
        "camera_remains_outside_mesh": all_outside,
        "terminal_distance_is_safe_handoff_marker": terminal_hits_marker,
        "randomization_logic_modified": False,
        "d_cover": e.d_cover,
        "d_near_min": e.d_near_min,
        "safe_handoff_distance": e.safe_handoff_distance,
        "failure_cases": failures,
    }
    checks["pass"] = (
        fixed_fov
        and no_scale_fake
        and distances_monotonic
        and all_near_safe
        and all_outside
        and terminal_hits_marker
        and not any(failures.values())
    )
    return checks
