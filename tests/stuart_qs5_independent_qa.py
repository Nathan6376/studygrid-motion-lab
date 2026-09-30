from dataclasses import replace

# This regression file is intended to be run with the three exact Bob fixture
# modules on PYTHONPATH. It does not modify those modules.
from doorway_cube_selection_policy import choose_doorway_cube
from nine_cube_grid_validator import CubeSpec, GridConfig, validate_nine_cube_grid
from study_visibility_cut_fixture import STUDY_WINDOWS, boundary_frames, frame_at, validate_frame_visibility, window_for_frame


def test_qb4():
    r = choose_doorway_cube(["A", "B", "C"], seed=17)
    assert r.selected in {"A", "B", "C"} and r.previous is None

    r = choose_doorway_cube(["A"], history=["A"], seed=1)
    assert r.selected == "A" and r.candidate_pool == ("A",)

    for n in (2, 3, 9):
        items = tuple(str(i) for i in range(n))
        for seed in range(250):
            r = choose_doorway_cube(items, history=[items[0]], seed=seed)
            assert r.selected != items[0]

    r = choose_doorway_cube(["A", "B", "C"], history=["OLD"], seed=5)
    assert r.candidate_pool == ("A", "B", "C")

    for seed in (0, 1, 2, 7, 99, 123456):
        assert choose_doorway_cube(["A", "B", "C", "D"], history=["C"], seed=seed) == choose_doorway_cube(["A", "B", "C", "D"], history=["C"], seed=seed)


def _base_cubes():
    slots = [f"r{r}c{c}" for r in range(3) for c in range(3)]
    return [CubeSpec(f"C{i}", slot) for i, slot in enumerate(slots)]


def test_qb5():
    base = _base_cubes()
    assert validate_nine_cube_grid(base).ok

    rep = validate_nine_cube_grid(base[:-1])
    assert not rep.ok and any("expected exactly 9" in e for e in rep.errors) and any("missing target slots" in e for e in rep.errors)

    rep = validate_nine_cube_grid(base + [CubeSpec("C9", "r0c0")])
    assert not rep.ok and any("expected exactly 9" in e for e in rep.errors)

    unequal = list(base)
    unequal[4] = replace(unequal[4], dimensions=(1.0, 1.01, 1.0))
    assert any("dimension drift" in e for e in validate_nine_cube_grid(unequal).errors)

    rep = validate_nine_cube_grid(base, GridConfig(gap=1e-7, tolerance=1e-6))
    assert not rep.ok and any("positive air gap" in e for e in rep.errors)

    dup = list(base)
    dup[8] = replace(dup[8], slot_id="r0c0")
    rep = validate_nine_cube_grid(dup)
    assert any("duplicate slot occupancy" in e for e in rep.errors)

    bad_parent = list(base)
    bad_parent[2] = replace(bad_parent[2], parent_id="MISSING")
    assert any("invalid parent reference" in e for e in validate_nine_cube_grid(bad_parent).errors)


def test_qb6():
    for fps in (8, 12, 30):
        for idx, w in enumerate(STUDY_WINDOWS):
            mid = frame_at((w.start_s + w.end_s) / 2, fps)
            good = set(w.render_objects)
            passed, _ = validate_frame_visibility(mid, good, fps=fps)
            assert passed
            foreign = next(iter(STUDY_WINDOWS[(idx + 1) % len(STUDY_WINDOWS)].render_objects))
            passed, errors = validate_frame_visibility(mid, good | {foreign}, fps=fps)
            assert not passed and any("foreign-study-visible" in e for e in errors)

        for idx, w in enumerate(STUDY_WINDOWS[1:], start=1):
            _before, cut, after = boundary_frames(fps)[w.name]
            assert window_for_frame(cut, fps).name == w.name
            assert window_for_frame(after, fps).name == w.name
            prev_obj = next(iter(STUDY_WINDOWS[idx - 1].render_objects))
            passed, _ = validate_frame_visibility(cut, set(w.render_objects) | {prev_obj}, fps=fps)
            assert not passed

        w = STUDY_WINDOWS[2]
        mid = frame_at((w.start_s + w.end_s) / 2, fps)
        passed, errors = validate_frame_visibility(mid, set(w.render_objects) | {"CAMERA_CUT_MARKER", "EASING_DIAGNOSTIC"}, fps=fps)
        assert passed and not errors


if __name__ == "__main__":
    test_qb4()
    test_qb5()
    test_qb6()
    print("STUART Q-S5 PASS")
