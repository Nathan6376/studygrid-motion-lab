"""
StudyGrid G -> seed continuity scaffold (Q-B1).

This is an isolated, source/static scaffold. It deliberately does NOT encode a
StudyGrid G outline. The final canonical vector is an input boundary.

Core invariants:
- one perceptual/object identity from G through seed-close;
- no opacity/visibility crossfade and no replacement-G handoff;
- object TRS scale is locked at (1, 1, 1);
- stroke radius targets 0.5x during the half-stroke phase;
- 3D formation is vertex/radius deformation, not whole-object scaling;
- final cube-close uses the same topology and an externally supplied,
  canonical-asset-derived target map.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose
from typing import Iterable, Tuple

Vec3 = Tuple[float, float, float]
ONE3: Vec3 = (1.0, 1.0, 1.0)


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


def smoothstep01(value: float) -> float:
    t = clamp01(value)
    return t * t * (3.0 - 2.0 * t)


def lerp(a: float, b: float, t: float) -> float:
    u = clamp01(t)
    return a + (b - a) * u


def lerp3(a: Vec3, b: Vec3, t: float) -> Vec3:
    u = clamp01(t)
    return tuple(lerp(x, y, u) for x, y in zip(a, b))  # type: ignore[return-value]


def window(progress: float, start: float, end: float) -> float:
    if not 0.0 <= start < end <= 1.0:
        raise ValueError("window must satisfy 0 <= start < end <= 1")
    return smoothstep01((clamp01(progress) - start) / (end - start))


@dataclass(frozen=True)
class CanonicalGInterface:
    """Asset boundary; values remain unresolved until the canonical G is frozen."""

    asset_id: str
    asset_hash: str | None
    source_vertex_count: int | None
    source_is_frozen: bool = False

    def assert_not_claiming_canonical(self) -> None:
        if not self.source_is_frozen:
            if self.asset_hash is not None or self.source_vertex_count is not None:
                raise ValueError(
                    "unfrozen canonical G must not carry final hash/vertex-count claims"
                )


@dataclass(frozen=True)
class Timing:
    half_stroke_start: float = 0.05
    half_stroke_end: float = 0.32
    soften_start: float = 0.12
    soften_end: float = 0.42
    depth_start: float = 0.18
    depth_end: float = 0.58
    fold_start: float = 0.40
    fold_end: float = 0.84
    cube_close_start: float = 0.72
    cube_close_end: float = 1.00

    def validate(self) -> None:
        spans = (
            ("half_stroke", self.half_stroke_start, self.half_stroke_end),
            ("soften", self.soften_start, self.soften_end),
            ("depth", self.depth_start, self.depth_end),
            ("fold", self.fold_start, self.fold_end),
            ("cube_close", self.cube_close_start, self.cube_close_end),
        )
        for name, start, end in spans:
            if not 0.0 <= start < end <= 1.0:
                raise ValueError(f"{name} timing is invalid: {start}, {end}")
        if self.cube_close_end != 1.0:
            raise ValueError("cube-close must end at normalized progress 1.0")


@dataclass(frozen=True)
class ParameterContract:
    object_name: str = "SG_G"
    seed_anchor_name: str = "Seed"
    root_name: str = "SG_Root"
    base_stroke_radius: float = 1.0
    half_stroke_ratio: float = 0.5
    min_depth_ratio: float = 0.12
    object_scale: Vec3 = ONE3
    opacity: float = 1.0
    visible: bool = True

    def validate(self) -> None:
        if self.object_name != "SG_G":
            raise ValueError("continuity object identity must remain SG_G")
        if self.object_scale != ONE3:
            raise ValueError("global/object scale must remain (1,1,1)")
        if not isclose(self.half_stroke_ratio, 0.5, abs_tol=0.05):
            raise ValueError("half-stroke target must remain approximately 0.5x")
        if self.opacity != 1.0 or not self.visible:
            raise ValueError("opacity/visibility handoff is prohibited")
        if self.base_stroke_radius <= 0.0:
            raise ValueError("base stroke radius must be positive")
        if self.min_depth_ratio <= 0.0:
            raise ValueError("3D depth target must be positive")


@dataclass(frozen=True)
class TopologyMap:
    """
    Topology-stable source -> cube-close mapping.

    basis_points:
        Frame-0 surface vertices generated from the future canonical G vector.
    depth_points:
        Same vertices after real-depth formation, still visibly the same G.
    fold_points:
        Same vertices after the fold/close preparation.
    cube_close_points:
        Same vertices projected onto the centre seed cube surface.

    The scaffold never fabricates these arrays. A future canonical-G adapter must
    provide all four arrays with identical vertex count and ordering.
    """

    basis_points: Tuple[Vec3, ...]
    depth_points: Tuple[Vec3, ...]
    fold_points: Tuple[Vec3, ...]
    cube_close_points: Tuple[Vec3, ...]

    def validate(self) -> None:
        n = len(self.basis_points)
        if n < 4:
            raise ValueError("topology fixture must have at least four vertices")
        if not all(
            len(points) == n
            for points in (
                self.depth_points,
                self.fold_points,
                self.cube_close_points,
            )
        ):
            raise ValueError("all deformation states must preserve vertex count/order")


@dataclass(frozen=True)
class ContinuitySample:
    progress: float
    object_name: str
    parent_chain: Tuple[str, ...]
    object_scale: Vec3
    opacity: float
    visible: bool
    stroke_radius: float
    terminal_softness: float
    depth_weight: float
    fold_weight: float
    cube_close_weight: float
    vertices: Tuple[Vec3, ...]


class GSeedContinuityScaffold:
    def __init__(
        self,
        topology: TopologyMap,
        contract: ParameterContract = ParameterContract(),
        timing: Timing = Timing(),
    ) -> None:
        topology.validate()
        contract.validate()
        timing.validate()
        self.topology = topology
        self.contract = contract
        self.timing = timing

    @property
    def parent_chain(self) -> Tuple[str, ...]:
        # SG_G keeps one identity under SG_Root. Seed is a target/anchor, not a
        # replacement object during the morph.
        return (self.contract.root_name, self.contract.object_name)

    def sample(self, progress: float) -> ContinuitySample:
        p = clamp01(progress)
        t = self.timing

        half = window(p, t.half_stroke_start, t.half_stroke_end)
        soften = window(p, t.soften_start, t.soften_end)
        depth = window(p, t.depth_start, t.depth_end)
        fold = window(p, t.fold_start, t.fold_end)
        close = window(p, t.cube_close_start, t.cube_close_end)

        stroke_radius = self.contract.base_stroke_radius * lerp(
            1.0, self.contract.half_stroke_ratio, half
        )

        # Vertex identity/order is preserved at every stage. First gain depth,
        # then fold, then close onto the seed surface. No object swap occurs.
        v_depth = tuple(
            lerp3(a, b, depth)
            for a, b in zip(self.topology.basis_points, self.topology.depth_points)
        )
        v_fold = tuple(
            lerp3(a, b, fold)
            for a, b in zip(v_depth, self.topology.fold_points)
        )
        vertices = tuple(
            lerp3(a, b, close)
            for a, b in zip(v_fold, self.topology.cube_close_points)
        )

        return ContinuitySample(
            progress=p,
            object_name=self.contract.object_name,
            parent_chain=self.parent_chain,
            object_scale=self.contract.object_scale,
            opacity=self.contract.opacity,
            visible=self.contract.visible,
            stroke_radius=stroke_radius,
            terminal_softness=soften,
            depth_weight=depth,
            fold_weight=fold,
            cube_close_weight=close,
            vertices=vertices,
        )


def static_invariant_report(
    scaffold: GSeedContinuityScaffold,
    checkpoints: Iterable[float] = (0.0, 0.1, 0.25, 0.5, 0.75, 1.0),
) -> dict:
    samples = tuple(scaffold.sample(p) for p in checkpoints)
    expected_n = len(scaffold.topology.basis_points)

    same_identity = all(s.object_name == "SG_G" for s in samples)
    no_global_scale = all(s.object_scale == ONE3 for s in samples)
    no_visibility_swap = all(s.visible and s.opacity == 1.0 for s in samples)
    stable_topology = all(len(s.vertices) == expected_n for s in samples)
    half_stroke_reached = isclose(
        scaffold.sample(scaffold.timing.half_stroke_end).stroke_radius,
        scaffold.contract.base_stroke_radius * scaffold.contract.half_stroke_ratio,
        rel_tol=0.0,
        abs_tol=1e-9,
    )
    depth_is_real = scaffold.sample(scaffold.timing.depth_end).depth_weight > 0.999
    final_matches_close_map = all(
        all(isclose(a, b, rel_tol=0.0, abs_tol=1e-9) for a, b in zip(actual, target))
        for actual, target in zip(
            scaffold.sample(1.0).vertices, scaffold.topology.cube_close_points
        )
    )

    checks = {
        "same_object_identity": same_identity,
        "no_global_scale": no_global_scale,
        "no_visibility_or_opacity_swap": no_visibility_swap,
        "stable_vertex_topology": stable_topology,
        "half_stroke_target_reached": half_stroke_reached,
        "depth_phase_reaches_3d_state": depth_is_real,
        "final_vertices_equal_supplied_cube_close_map": final_matches_close_map,
        "canonical_geometry_embedded_by_scaffold": False,
    }
    checks["pass"] = all(
        v for k, v in checks.items() if k != "canonical_geometry_embedded_by_scaffold"
    )
    return checks
