from doorway_cube_selection_policy import choose_doorway_cube
import random

r = choose_doorway_cube(["NW", "N", "NE"], seed=7)
assert r.selected in {"NW", "N", "NE"}
assert r.previous is None and len(r.candidate_pool) == 3

r = choose_doorway_cube(["C"], history=["C"], seed=1)
assert r.selected == "C" and r.candidate_pool == ("C",)

for seed in range(100):
    r = choose_doorway_cube(["A", "B", "C"], history=["A"], seed=seed)
    assert r.selected != "A"
    assert r.candidate_pool == ("B", "C")

r = choose_doorway_cube(["A", "B"], history=["OLD"], seed=3)
assert set(r.candidate_pool) == {"A", "B"}

for seed in (0, 1, 2, 99, 123456):
    a = choose_doorway_cube(["A", "B", "C", "D"], history=["C"], seed=seed)
    b = choose_doorway_cube(["A", "B", "C", "D"], history=["C"], seed=seed)
    assert a == b

rng1 = random.Random(55)
rng2 = random.Random(55)
seq1 = [choose_doorway_cube(["A", "B", "C"], history=["B"], rng=rng1).selected for _ in range(20)]
seq2 = [choose_doorway_cube(["A", "B", "C"], history=["B"], rng=rng2).selected for _ in range(20)]
assert seq1 == seq2 and all(x != "B" for x in seq1)

for bad in ([], ["A", "A"]):
    try:
        choose_doorway_cube(bad, seed=1)
        raise AssertionError("invalid eligible list should fail")
    except ValueError:
        pass

try:
    choose_doorway_cube(["A", "B"], seed=1, rng=random.Random(1))
    raise AssertionError("seed + rng should fail")
except ValueError:
    pass

print("Q-B4 PASS")
