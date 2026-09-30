"""Deterministic doorway cube-selection policy fixture.

Pure Python: no Blender dependency and no product integration.
"""
from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Hashable, Iterable, Optional, Sequence, Tuple

CubeId = Hashable


@dataclass(frozen=True)
class SelectionResult:
    selected: CubeId
    eligible: Tuple[CubeId, ...]
    previous: Optional[CubeId]
    candidate_pool: Tuple[CubeId, ...]
    seed: Optional[int]


def _normalise_eligible(eligible: Iterable[CubeId]) -> Tuple[CubeId, ...]:
    items = tuple(eligible)
    if not items:
        raise ValueError("eligible cube list must not be empty")
    if any(item is None for item in items):
        raise ValueError("eligible cube IDs must not be None")
    if len(set(items)) != len(items):
        raise ValueError("eligible cube IDs must be unique")
    return items


def choose_doorway_cube(
    eligible: Iterable[CubeId],
    *,
    history: Sequence[CubeId] = (),
    seed: Optional[int] = None,
    rng: Optional[random.Random] = None,
) -> SelectionResult:
    """Choose one eligible cube under the locked no-immediate-repeat policy."""
    items = _normalise_eligible(eligible)
    if seed is not None and rng is not None:
        raise ValueError("pass seed or rng, not both")

    previous = history[-1] if history else None
    if len(items) > 1 and previous in items:
        pool = tuple(item for item in items if item != previous)
    else:
        pool = items

    chooser = rng if rng is not None else random.Random(seed)
    selected = pool[chooser.randrange(len(pool))]
    return SelectionResult(selected, items, previous, pool, seed)
