"""Study visibility / diagnostic-cut isolation fixture.

Pure Python. Encodes current V4A study object groups and window boundaries as an
explicit QA contract; it does not change cameras, mechanics, easing, or source.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Mapping, Optional, Tuple

CURRENT_SOURCE_ASSUMPTION = "blender/scene_v4a.py @ main 933eb618f162e4e8370c275221fefd71a95ed8d1"


@dataclass(frozen=True)
class StudyWindow:
    name: str
    start_s: float
    end_s: float
    render_objects: frozenset[str]


STUDY_WINDOWS: Tuple[StudyWindow, ...] = (
    StudyWindow("study1_g_seed", 0.0, 5.6, frozenset({"SG_G_PROVISIONAL", "Seed"})),
    StudyWindow("study2a_single_hinge", 5.8, 8.6, frozenset({"A_Parent", "A_Child"})),
    StudyWindow("study2c_hidden_hybrid", 8.8, 12.0, frozenset({"C_Parent", "C_Child"})),
    StudyWindow("study3_causal_chain", 12.2, 16.6, frozenset({"Chain_C", "Chain_E", "Chain_SE"})),
    StudyWindow("study4_doorway", 16.8, 22.0, frozenset({"Doorway", "Door_L", "Door_R", "Door_U", "Door_D"})),
)

ALLOWED_GLOBAL_RENDER_OBJECTS = frozenset({"SG_Floor"})


def frame_at(seconds: float, fps: int) -> int:
    if fps <= 0:
        raise ValueError("fps must be positive")
    return max(1, int(round(seconds * fps)))


def compile_schedule(fps: int) -> Dict[str, Tuple[int, int]]:
    return {w.name: (frame_at(w.start_s, fps), frame_at(w.end_s, fps)) for w in STUDY_WINDOWS}


def window_for_frame(frame: int, fps: int) -> Optional[StudyWindow]:
    matches = []
    for w in STUDY_WINDOWS:
        start, end = frame_at(w.start_s, fps), frame_at(w.end_s, fps)
        if start <= frame <= end:
            matches.append(w)
    if len(matches) > 1:
        raise AssertionError(f"overlapping visibility windows at frame {frame}: {[w.name for w in matches]}")
    return matches[0] if matches else None


def validate_frame_visibility(
    frame: int,
    visible_render_objects: Iterable[str],
    *,
    fps: int,
    allow_missing_expected: bool = True,
) -> Tuple[bool, Tuple[str, ...]]:
    """Reject cross-study bleed at one frame."""
    visible = set(visible_render_objects)
    study = window_for_frame(frame, fps)
    all_study_objects = set().union(*(set(w.render_objects) for w in STUDY_WINDOWS))

    if study is None:
        foreign = visible & all_study_objects
        missing = set()
    else:
        foreign = (visible & all_study_objects) - set(study.render_objects)
        missing = set() if allow_missing_expected else set(study.render_objects) - visible

    errors = []
    if foreign:
        errors.append("foreign-study-visible:" + ",".join(sorted(foreign)))
    if missing:
        errors.append("expected-study-missing:" + ",".join(sorted(missing)))
    return (not errors, tuple(errors))


def boundary_frames(fps: int) -> Dict[str, Tuple[int, int, int]]:
    """Immediately-before / at / after frames for each study-start cut."""
    result = {}
    for w in STUDY_WINDOWS[1:]:
        cut = frame_at(w.start_s, fps)
        result[w.name] = (cut - 1, cut, cut + 1)
    return result


def validate_observation_map(
    observations: Mapping[int, Iterable[str]],
    *,
    fps: int,
) -> Tuple[bool, Dict[int, Tuple[str, ...]]]:
    failures: Dict[int, Tuple[str, ...]] = {}
    for frame, visible in sorted(observations.items()):
        ok, errors = validate_frame_visibility(frame, visible, fps=fps)
        if not ok:
            failures[frame] = errors
    return (not failures, failures)
