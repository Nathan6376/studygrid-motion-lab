"""Static/analytic verifier for Q-B2 doorway-camera handoff fixture."""

from doorway_camera_handoff_fixture import (
    CameraContract,
    cover_distance,
    static_report,
)


def main() -> None:
    aspects = {
        "16:9": 16 / 9,
        "4:3": 4 / 3,
        "3:4": 3 / 4,
        "9:16": 9 / 16,
    }
    reports = {}
    for label, aspect in aspects.items():
        contract = CameraContract(aspect=aspect)
        report = static_report(contract)
        assert report["pass"], (label, report)
        assert report["randomization_logic_modified"] is False
        reports[label] = report

    landscape = CameraContract(aspect=16 / 9)
    d = cover_distance(landscape)
    assert 0.68 < d < 0.70, d

    print("PASS")
    for label, report in reports.items():
        print(
            f"{label}: d_cover={report['d_cover']:.6f}L "
            f"d_near_min={report['d_near_min']:.6f}L "
            f"handoff={report['safe_handoff_distance']:.6f}L"
        )


if __name__ == "__main__":
    main()
