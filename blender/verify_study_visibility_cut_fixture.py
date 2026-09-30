from study_visibility_cut_fixture import (
    ALLOWED_GLOBAL_RENDER_OBJECTS,
    STUDY_WINDOWS,
    boundary_frames,
    compile_schedule,
    frame_at,
    validate_frame_visibility,
    validate_observation_map,
    window_for_frame,
)

for fps in (8, 12, 30):
    schedule = compile_schedule(fps)
    assert len(schedule) == 5

    observations = {}
    for w in STUDY_WINDOWS:
        mid = (frame_at(w.start_s, fps) + frame_at(w.end_s, fps)) // 2
        observations[mid] = set(w.render_objects) | set(ALLOWED_GLOBAL_RENDER_OBJECTS)
        assert window_for_frame(mid, fps).name == w.name

    ok, failures = validate_observation_map(observations, fps=fps)
    assert ok, failures

    s2a_mid = sum(schedule["study2a_single_hinge"]) // 2
    ok, errors = validate_frame_visibility(
        s2a_mid,
        {"A_Parent", "A_Child", "C_Parent"},
        fps=fps,
    )
    assert not ok and any("C_Parent" in e for e in errors)

    for left, right in zip(STUDY_WINDOWS, STUDY_WINDOWS[1:]):
        gap_frame = frame_at((left.end_s + right.start_s) / 2.0, fps)
        if window_for_frame(gap_frame, fps) is None:
            ok, errors = validate_frame_visibility(gap_frame, {next(iter(left.render_objects))}, fps=fps)
            assert not ok and errors

    cuts = boundary_frames(fps)
    assert set(cuts) == {w.name for w in STUDY_WINDOWS[1:]}
    for name, triple in cuts.items():
        assert triple[1] - triple[0] == 1
        assert triple[2] - triple[1] == 1
        assert window_for_frame(triple[1], fps).name == name
        assert window_for_frame(triple[2], fps).name == name

print("Q-B6 PASS")
