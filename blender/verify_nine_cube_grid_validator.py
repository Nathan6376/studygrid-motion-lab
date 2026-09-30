from dataclasses import replace
from nine_cube_grid_validator import CubeSpec, GridConfig, target_slots, validate_nine_cube_grid

cfg = GridConfig(cube_size=1.0, gap=0.10)
slots = list(target_slots(cfg))
cubes = []
for i, sid in enumerate(slots):
    parent = None if i == 0 else f"C{i-1}"
    cubes.append(CubeSpec(cube_id=f"C{i}", slot_id=sid, parent_id=parent))

report = validate_nine_cube_grid(cubes, cfg)
assert report.ok, report.errors
assert len(report.slot_positions) == 9
assert len(report.adjacency["r1c1"]) == 4


def must_fail(items, needle):
    r = validate_nine_cube_grid(items, cfg)
    assert not r.ok
    assert any(needle in e for e in r.errors), r.errors

must_fail(cubes[:-1], "exactly 9")
must_fail([replace(c, slot_id="r0c0") if c.cube_id == "C8" else c for c in cubes], "duplicate slot occupancy")
must_fail([replace(c, dimensions=(1.0, 1.01, 1.0)) if c.cube_id == "C2" else c for c in cubes], "dimension drift")
must_fail([replace(c, independent_mesh=False) if c.cube_id == "C3" else c for c in cubes], "fused/non-cube")
must_fail([replace(c, scale_samples=((1,1,1),(0.95,0.95,0.95))) if c.cube_id == "C4" else c for c in cubes], "object scale")
must_fail([replace(c, parent_id="MISSING") if c.cube_id == "C5" else c for c in cubes], "invalid parent reference")

cyc = list(cubes)
cyc[0] = replace(cyc[0], parent_id="C1")
cyc[1] = replace(cyc[1], parent_id="C0")
must_fail(cyc, "parent cycle")

try:
    target_slots(GridConfig(cube_size=1.0, gap=0.0))
    raise AssertionError("zero gap must fail")
except ValueError:
    pass

print("Q-B5 PASS")
