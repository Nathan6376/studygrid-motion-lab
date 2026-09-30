"""
StudyGrid Motion V4A — Blender mechanics gate
Purpose: slow owner-QA proof. No StudyGrid integration.

Important:
- This script intentionally uses a PROVISIONAL geometric G proxy until the canonical
  StudyGrid G vector is frozen and supplied. Hinge, cube, lighting, camera and timing
  are the primary mechanics under review in this pass.
- Whole-G scale is not used to create the ~50% stroke-thickness effect.
- Final grid production choreography is NOT built here.
"""

import bpy
import math
import sys
from pathlib import Path
from mathutils import Vector

# -----------------------
# CLI
# -----------------------
def argv_after_dashes():
    if "--" not in sys.argv:
        return []
    return sys.argv[sys.argv.index("--") + 1:]


def parse_args():
    args = argv_after_dashes()
    out = {"output_dir": str(Path.cwd() / "output"), "quality": "preview"}
    i = 0
    while i < len(args):
        if args[i] == "--output-dir" and i + 1 < len(args):
            out["output_dir"] = args[i + 1]
            i += 2
        elif args[i] == "--quality" and i + 1 < len(args):
            out["quality"] = args[i + 1]
            i += 2
        else:
            i += 1
    return out


ARGS = parse_args()
OUT = Path(ARGS["output_dir"])
(OUT / "frames").mkdir(parents=True, exist_ok=True)
(OUT / "stills").mkdir(parents=True, exist_ok=True)

# -----------------------
# Constants / locked intent
# -----------------------
# Preview is intentionally lightweight for rapid owner QA. Review mode is 30fps/1080p.
FPS = 12 if ARGS["quality"] == "preview" else 30
L = 1.0
GAP = 0.10
BEVEL = 0.055
GREEN = (0.0, 0.50, 0.22, 1.0)  # provisional viewport approximation
BG = (0.92, 0.91, 0.88, 1.0)
ROUGHNESS = 0.33

F = lambda sec: max(1, int(round(sec * FPS)))

# -----------------------
# Scene reset / render
# -----------------------
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE_NEXT"
scene.render.fps = FPS
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_mode = "RGB"
scene.render.resolution_x = 800 if ARGS["quality"] == "preview" else 1920
scene.render.resolution_y = 450 if ARGS["quality"] == "preview" else 1080
scene.render.resolution_percentage = 100
scene.render.film_transparent = False
if scene.world is None:
    scene.world = bpy.data.worlds.new("SG_World")
scene.world.color = BG[:3]
scene.frame_start = 1
scene.frame_end = F(22.0)

# -----------------------
# Helpers
# -----------------------
def mat_principled(name, base, roughness=0.33, metallic=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = base
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    return m


GREEN_MAT = mat_principled("SG_Green", GREEN, ROUGHNESS, 0.0)
FLOOR_MAT = mat_principled("SG_Floor", BG, 0.65, 0.0)


def set_linear_visibility(obj, start, end=None):
    obj.hide_render = True
    obj.hide_viewport = True
    obj.keyframe_insert("hide_render", frame=max(1, start - 1))
    obj.keyframe_insert("hide_viewport", frame=max(1, start - 1))
    obj.hide_render = False
    obj.hide_viewport = False
    obj.keyframe_insert("hide_render", frame=start)
    obj.keyframe_insert("hide_viewport", frame=start)
    if end is not None:
        obj.hide_render = False
        obj.hide_viewport = False
        obj.keyframe_insert("hide_render", frame=end)
        obj.keyframe_insert("hide_viewport", frame=end)
        obj.hide_render = True
        obj.hide_viewport = True
        obj.keyframe_insert("hide_render", frame=end + 1)
        obj.keyframe_insert("hide_viewport", frame=end + 1)


def add_cube(name, loc=(0, 0, 0), scale=1.0, material=GREEN_MAT):
    bpy.ops.mesh.primitive_cube_add(size=L, location=loc)
    o = bpy.context.object
    o.name = name
    o.scale = (scale, scale, scale)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bev = o.modifiers.new("Bevel", "BEVEL")
    bev.width = BEVEL
    bev.segments = 4
    o.data.materials.append(material)
    return o


def add_empty(name, loc):
    o = bpy.data.objects.new(name, None)
    o.empty_display_type = "PLAIN_AXES"
    o.empty_display_size = 0.2
    o.location = loc
    scene.collection.objects.link(o)
    return o


def key_rot(obj, frame, angle_deg, axis="Y"):
    idx = {"X": 0, "Y": 1, "Z": 2}[axis]
    obj.rotation_mode = "XYZ"
    obj.rotation_euler[idx] = math.radians(angle_deg)
    obj.keyframe_insert("rotation_euler", index=idx, frame=frame)


def damped_interp(obj):
    if not obj.animation_data or not obj.animation_data.action:
        return
    for fc in obj.animation_data.action.fcurves:
        for kp in fc.keyframe_points:
            kp.interpolation = "BEZIER"
            kp.easing = "AUTO"
            kp.handle_left_type = "AUTO_CLAMPED"
            kp.handle_right_type = "AUTO_CLAMPED"


def point_object(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def point_camera(cam, target):
    point_object(cam, target)


def set_camera_diagnostic_interpolation(obj, motion_start_frame):
    """Hold diagnostic framings between cuts; only the doorway approach is eased."""
    if not obj.animation_data or not obj.animation_data.action:
        return
    for fc in obj.animation_data.action.fcurves:
        for kp in fc.keyframe_points:
            if kp.co.x < motion_start_frame - 0.5:
                kp.interpolation = "CONSTANT"
            else:
                kp.interpolation = "BEZIER"
                kp.easing = "AUTO"
                kp.handle_left_type = "AUTO_CLAMPED"
                kp.handle_right_type = "AUTO_CLAMPED"

# -----------------------
# Stage / camera / lights
# -----------------------
bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 0, -0.75))
floor = bpy.context.object
floor.name = "SG_Floor"
floor.data.materials.append(FLOOR_MAT)
# The doorway cross extends below the floor plane; hide the diagnostic floor at
# that cut rather than render mesh penetration as if it were valid mechanics.
floor.hide_render = False
floor.hide_viewport = False
floor.keyframe_insert("hide_render", frame=F(16.6))
floor.keyframe_insert("hide_viewport", frame=F(16.6))
floor.hide_render = True
floor.hide_viewport = True
floor.keyframe_insert("hide_render", frame=F(16.7))
floor.keyframe_insert("hide_viewport", frame=F(16.7))

LIGHT_TARGET = (0.6, 0.0, 0.0)

bpy.ops.object.light_add(type="AREA", location=(-4, -4, 6))
key = bpy.context.object
key.name = "SG_Key"
key.data.energy = 900
key.data.shape = "DISK"
key.data.size = 5.0
point_object(key, LIGHT_TARGET)

bpy.ops.object.light_add(type="AREA", location=(4, -2, 3))
fill = bpy.context.object
fill.name = "SG_Fill"
fill.data.energy = 250
fill.data.size = 4.0
point_object(fill, LIGHT_TARGET)

bpy.ops.object.light_add(type="AREA", location=(0, 5, 4))
rim = bpy.context.object
rim.name = "SG_Rim"
rim.data.energy = 350
rim.data.size = 3.0
point_object(rim, LIGHT_TARGET)

bpy.ops.object.camera_add(location=(5.2, -8.8, 5.4))
cam = bpy.context.object
cam.name = "SG_Camera"
cam.data.lens = 50
cam.data.sensor_fit = "VERTICAL"
point_camera(cam, (0, 0, 0))
scene.camera = cam

# -----------------------
# Study 1 — provisional G -> seed
# -----------------------
curve_data = bpy.data.curves.new("G_Curve", type="CURVE")
curve_data.dimensions = "3D"
curve_data.resolution_u = 24
curve_data.bevel_resolution = 4
curve_data.bevel_depth = 0.22

spline = curve_data.splines.new("POLY")
pts = []
for i in range(33):
    a = math.radians(45 + (315 - 45) * i / 32)
    pts.append((1.15 * math.cos(a), 1.15 * math.sin(a), 0.0))
pts += [(0.15, -0.10, 0.0), (1.10, -0.10, 0.0)]
spline.points.add(len(pts) - 1)
for p, co in zip(spline.points, pts):
    p.co = (*co, 1.0)

g = bpy.data.objects.new("SG_G_PROVISIONAL", curve_data)
scene.collection.objects.link(g)
g.data.materials.append(GREEN_MAT)
g.rotation_euler = (math.radians(90), 0, 0)
g.location = (0, 0, 0.4)
set_linear_visibility(g, F(0.0), F(5.5))

# Stroke thickness changes; whole object scale does not.
curve_data.bevel_depth = 0.22
curve_data.keyframe_insert("bevel_depth", frame=F(0.7))
curve_data.bevel_depth = 0.11
curve_data.keyframe_insert("bevel_depth", frame=F(2.2))
g.rotation_euler = (math.radians(90), 0, 0)
g.keyframe_insert("rotation_euler", frame=F(2.2))
g.rotation_euler = (math.radians(76), math.radians(10), 0)
g.keyframe_insert("rotation_euler", frame=F(3.2))
damped_interp(curve_data)
damped_interp(g)

seed = add_cube("Seed", loc=(0, 0, 0))
set_linear_visibility(seed, F(3.1), F(5.6))
seed.scale = (0.08, 0.08, 0.08)
seed.keyframe_insert("scale", frame=F(3.1))
seed.scale = (1, 1, 1)
seed.keyframe_insert("scale", frame=F(4.4))
damped_interp(seed)

# -----------------------
# Study 2A — strict single ~90° face-plane hinge
# -----------------------
parent_a = add_cube("A_Parent", loc=(-2.8, 0, 0))
child_a = add_cube("A_Child", loc=(0, 0, 0))
hinge_a = add_empty("A_Hinge", (-2.8 + (L + GAP) / 2, 0, +L / 2))
child_a.parent = hinge_a
# Local centre is defined from the hinge itself. Do not use a parent-inverse that
# cancels the hinge translation and turns the intended fold into a large orbit.
child_a.location = ((L + GAP) / 2, 0, -L / 2)
set_linear_visibility(parent_a, F(5.8), F(8.6))
set_linear_visibility(child_a, F(5.8), F(8.6))
key_rot(hinge_a, F(6.2), -90, "Y")
key_rot(hinge_a, F(8.0), 0, "Y")
damped_interp(hinge_a)

# -----------------------
# Study 2C — hidden-behind 90 + 90 hybrid
# -----------------------
parent_c = add_cube("C_Parent", loc=(0.4, 0, 0))
child_c = add_cube("C_Child", loc=(0, 0, 0))
hinge_c1 = add_empty("C_Hinge_Rise", (0.4 + (L + GAP) / 2, 0, -L / 2))
hinge_c2 = add_empty("C_Hinge_Settle", (0, 0, 0))
hinge_c2.parent = hinge_c1
child_c.parent = hinge_c2
child_c.location = (-0.55, 0, -0.5)
set_linear_visibility(parent_c, F(8.8), F(12.0))
set_linear_visibility(child_c, F(9.1), F(12.0))
key_rot(hinge_c1, F(9.2), -90, "Y")
key_rot(hinge_c1, F(10.5), 0, "Y")
key_rot(hinge_c2, F(10.5), -90, "Y")
key_rot(hinge_c2, F(11.8), 0, "Y")
damped_interp(hinge_c1)
damped_interp(hinge_c2)

# -----------------------
# Study 3 — three-cube causal chain
# -----------------------
chain_seed = add_cube("Chain_C", loc=(2.9, 0, 0))
chain_e = add_cube("Chain_E", loc=(0, 0, 0))
chain_se = add_cube("Chain_SE", loc=(0, 0, 0))

# C -> E: edge/depth-aware Y hinge. E -> SE: nested X hinge attached to E,
# so SE is physically carried by E before its own quarter-turn begins.
hinge_e = add_empty("Chain_Hinge_E", (2.9 + (L + GAP) / 2, 0, +L / 2))
chain_e.parent = hinge_e
chain_e.location = ((L + GAP) / 2, 0, -L / 2)

hinge_se = add_empty("Chain_Hinge_SE", (0, -(L + GAP) / 2, +L / 2))
hinge_se.parent = chain_e
chain_se.parent = hinge_se
chain_se.location = (0, -(L + GAP) / 2, -L / 2)

set_linear_visibility(chain_seed, F(12.2), F(16.6))
set_linear_visibility(chain_e, F(12.2), F(16.6))
set_linear_visibility(chain_se, F(12.2), F(16.6))
key_rot(hinge_e, F(12.7), -90, "Y")
key_rot(hinge_e, F(14.0), 0, "Y")
key_rot(hinge_se, F(14.1), -90, "X")
key_rot(hinge_se, F(15.5), 0, "X")
damped_interp(hinge_e)
damped_interp(hinge_se)

# -----------------------
# Study 4 — doorway physical camera dolly
# -----------------------
door = add_cube("Doorway", loc=(0, 0, 0))
left = add_cube("Door_L", loc=(-(L + GAP), 0, 0))
right = add_cube("Door_R", loc=((L + GAP), 0, 0))
up = add_cube("Door_U", loc=(0, 0, (L + GAP)))
down = add_cube("Door_D", loc=(0, 0, -(L + GAP)))
for o in (door, left, right, up, down):
    set_linear_visibility(o, F(16.8), F(22.0))

# -----------------------
# Camera framing / diagnostics
# -----------------------
def cam_pose(frame, loc, target):
    cam.location = loc
    point_camera(cam, target)
    cam.keyframe_insert("location", frame=frame)
    cam.keyframe_insert("rotation_euler", frame=frame)


# Deliberate diagnostic cuts between studies.
cam_pose(F(0.0), (4.2, -8.2, 3.7), (0, 0, 0))
cam_pose(F(5.7), (3.2, -9.0, 4.0), (-1.2, 0, 0))
cam_pose(F(8.7), (3.0, -9.0, 4.0), (0.4, 0, 0))
cam_pose(F(12.1), (6.4, -10.5, 4.6), (3.4, -0.4, 0))
cam_pose(F(16.7), (3.8, -8.2, 3.2), (0, 0, 0))

# Doorway study: fixed 50mm lens, actual camera translation only.
cam.data.lens = 50
cam.data.keyframe_insert("lens", frame=F(16.7))
cam.location = (3.8, -8.2, 3.2)
point_camera(cam, (0, 0, 0))
cam.keyframe_insert("location", frame=F(17.0))
cam.keyframe_insert("rotation_euler", frame=F(17.0))
cam.location = (0.3, -2.0, 0.3)
point_camera(cam, (0, 0, 0))
cam.keyframe_insert("location", frame=F(21.0))
cam.keyframe_insert("rotation_euler", frame=F(21.0))
cam.data.lens = 50
cam.data.keyframe_insert("lens", frame=F(21.0))
damped_interp(cam)
set_camera_diagnostic_interpolation(cam, F(17.0))

# -----------------------
# Save, stills, render
# -----------------------
blend_path = OUT / "studygrid-v4a.blend"
bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

still_frames = {
    "01_g_full": F(0.8),
    "02_g_halfstroke": F(2.2),
    "03_seed": F(4.5),
    "04_hinge_a_mid": F(7.1),
    "05_hinge_c_rise": F(10.0),
    "06_hinge_c_settle": F(11.2),
    "07_chain": F(15.2),
    "08_doorway_start": F(17.2),
    "09_doorway_near": F(20.8),
}
for name, fr in still_frames.items():
    scene.frame_set(fr)
    scene.render.filepath = str(OUT / "stills" / f"{name}.png")
    bpy.ops.render.render(write_still=True)

scene.render.filepath = str(OUT / "frames" / "frame_")
scene.render.image_settings.file_format = "PNG"
bpy.ops.render.render(animation=True)

manifest = f"""StudyGrid Motion V4A owner-QA
Blender: {bpy.app.version_string}
Quality: {ARGS['quality']}
FPS: {FPS}
Resolution: {scene.render.resolution_x}x{scene.render.resolution_y}
Frames: {scene.frame_start}-{scene.frame_end}
Locked mechanics represented:
- G object scale remains constant during stroke-thickness reduction
- provisional G curve bevel thickness 0.22 -> 0.11
- independent equal cubes
- air gap target: {GAP}
- bevel target: {BEVEL}
- fixed 50mm lens for doorway study
- physical camera translation for doorway enlargement
- diagnostic camera framings hold between cuts; only doorway approach is eased
- Study 2A uses an edge/depth-aware local hinge transform rather than parent-inverse orbiting
- Study 3 uses a true nested C -> E -> SE parent/child hinge chain
Important limitation:
- G is PROVISIONAL geometric proxy. Canonical StudyGrid G vector is not frozen in this packet.
- Study 1 seed closure uses a temporary scale-up proxy and is NOT production-approved G->seed topology.
- Study 2C remains a provisional hidden-chain diagnostic; its exact hidden-behind arrangement still requires coordinator reconciliation and visual proof.
- Final 3x3 choreography intentionally not included.
"""
(OUT / "qa_manifest.txt").write_text(manifest, encoding="utf-8")
print(manifest)
