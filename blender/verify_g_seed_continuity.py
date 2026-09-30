"""Static verifier for the Q-B1 G -> seed continuity scaffold.

The geometry below is deliberately a NON-BRAND FIXTURE. It tests interface and
continuity invariants only; it is not a StudyGrid G and must never be promoted
as canonical geometry.
"""

from g_seed_continuity_scaffold import (
    CanonicalGInterface,
    GSeedContinuityScaffold,
    ParameterContract,
    TopologyMap,
    static_invariant_report,
)


def build_non_brand_fixture() -> TopologyMap:
    basis = (
        (-1.0, -0.2, 0.0),
        (-0.4, 0.8, 0.0),
        (0.4, 0.8, 0.0),
        (1.0, -0.2, 0.0),
        (0.4, -0.8, 0.0),
        (-0.4, -0.8, 0.0),
    )
    depth = tuple(
        (x * 0.98, y * 0.98, 0.18 if i % 2 else -0.18)
        for i, (x, y, _) in enumerate(basis)
    )
    fold = tuple((x * 0.72, y * 0.72, z * 1.8) for x, y, z in depth)
    close = (
        (-0.5, -0.5, -0.5),
        (-0.5, 0.5, -0.5),
        (0.5, 0.5, -0.5),
        (0.5, -0.5, 0.5),
        (0.5, -0.5, -0.5),
        (-0.5, -0.5, 0.5),
    )
    return TopologyMap(basis, depth, fold, close)


def main() -> None:
    canonical = CanonicalGInterface(
        asset_id="STUDYGRID-G-CANONICAL-TBD",
        asset_hash=None,
        source_vertex_count=None,
        source_is_frozen=False,
    )
    canonical.assert_not_claiming_canonical()

    scaffold = GSeedContinuityScaffold(
        build_non_brand_fixture(),
        contract=ParameterContract(),
    )
    report = static_invariant_report(scaffold)

    assert report["pass"], report
    assert report["canonical_geometry_embedded_by_scaffold"] is False
    assert scaffold.sample(0.0).stroke_radius == 1.0
    assert abs(
        scaffold.sample(scaffold.timing.half_stroke_end).stroke_radius - 0.5
    ) < 1e-9
    assert scaffold.sample(1.0).object_name == scaffold.sample(0.0).object_name
    assert scaffold.sample(1.0).parent_chain == ("SG_Root", "SG_G")

    print("PASS")
    for key, value in report.items():
        print(f"{key}={str(value).lower()}")


if __name__ == "__main__":
    main()
