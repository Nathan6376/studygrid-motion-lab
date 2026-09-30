"""
StudyGrid Motion V4A — isolated hidden-mechanics comparison prototype.

Purpose
- Compare Candidate A: strict collision-free single ~90° face-plane hinge.
- Compare Candidate C: genuinely rear-stowed, two-stage hidden-behind mechanism
  using two distinct face-plane hinge axes.
- This file is a prototype only. It does NOT choose the owner's final hinge option.

Boundary
- No StudyGrid production integration.
- No canonical G or final 3x3 choreography.
- No scale or opacity cheats during visible motion.
- Candidate C has NO visibility toggle: the child exists from frame 1 and is
  geometrically occluded only by the parent in the exact-front comparison camera.
"""

import bpy
import math
import sys
from pathlib import Path
from mathutils import Vector


def argv_after_dashes():
    if "--" not in sys.argv:
        return []
    return sys.argv[sys.argv.index("--") + 1:]


def parse_args():
    args = argv_after_dashes()
    out = {"output_dir": str(Path.cwd() / "output-v4a-hidden"), "quality": "preview"}
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

FPS = 12 if ARGS["quality"] == "preview" else 30
L = 1.0
GAP = 0.10
BEVEL = 0.055
GREEN = (0.0, 0.50, 0.22, 1.0)
BG = (0.92, 0.91, 0.88, 1.0)
ROUGHNESS = 0.33
F = lambda sec: max(1, int(round(sec * FPS)))

# Shared timing for both candidates.
T_HOLD = 1.0
T_STAGE1_END = 3.0
T_STAGE2_START = 3.5
T_STAGE2_END = 5.5
T_END = 6.5

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE_NEXT"
scene.render.fps = FPS
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_mode = "RGB"
scene.render.resolution_x = 960 if ARGS["quality"] == "preview" else 1920
scene.render.resolution_y = 540 if ARGS["quality"] == "preview" else 1080
scene.render.resolution_percentage = 100
scene.render.film_transparent = False
scene.frame_start = 1
scene.frame_end = F(T_END)
if scene.world is None:
    scene.world = bpy.data.worlds.new("SG_Hidden_World")
scene.world.color = BG[:3]


def mat_principled(name, base, roughness=0.33, metallic=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = base
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic
    return m


GREEN_MAT = mat_principled("SG_Hidden_Green", GREEN, ROUGHNESS, 0.0)
FLOOR_MAT = mat_principled("SG_Hidden_Floor", BG, 0.68, 0.0)


def add_cube(name, loc=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=L, location=loc)
    o = bpy.context.object
    o.name = name
    bev = o.modifiers.new("Bevel", "BEVEL")
    bev.width = BEVEL
    bev.segments = 4
    o.data.materials.append(GREEN_MAT)
    return o


def add_empty(name, loc=(0, 0, 0), parent=None):
    o = bpy.data.objects.new(name, None)
    o.empty_display_type = "PLAIN_AXES"
    o.empty_display_size = 0.14
    o.location = loc
    if parent is not None:
        o.parent = parent
    scene.collection.objects.link(o)
    return o


def key_rot(obj, frame, angle_deg, axis):
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


# Stage, lighting and two fixed diagnostic cameras.
# Exact-front camera is deliberately on the -Y axis with no X/Z offset.
# This makes C's rear-stowed child genuinely fully occluded by equal geometry.
# The oblique camera is used only for diagnostic stills to expose the same child.
FLOOR_Z = -1.25
bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, FLOOR_Z))
floor = bpy.context.object
floor.name = "SG_Hidden_Floor"
floor.data.materials.append(FLOOR_MAT)

LIGHT_TARGET = (0.0, 0.25, 0.25)
for name, loc, energy, size in (
    ("SG_Hidden_Key", (-5.0, -6.0, 7.0), 850, 5.0),
    ("SG_Hidden_Fill", (5.0, -4.0, 3.5), 260, 4.0),
    ("SG_Hidden_Rim", (0.0, 6.0, 5.0), 320, 3.5),
):
    bpy.ops.object.light_add(type="AREA", location=loc)
    light = bpy.context.object
    light.name = name
    light.data.energy = energy
    light.data.size = size
    point_object(light, LIGHT_TARGET)

bpy.ops.object.camera_add(location=(0.0, -15.0, 0.0))
front_cam = bpy.context.object
front_cam.name = "SG_Compare_Front_Camera"
front_cam.data.lens = 50
front_cam.data.sensor_fit = "HORIZONTAL"
point_object(front_cam, (0.0, 0.0, 0.0))

bpy.ops.object.camera_add(location=(7.0, -10.0, 6.0))
diag_cam = bpy.context.object
diag_cam.name = "SG_Compare_Diagnostic_Camera"
diag_cam.data.lens = 50
diag_cam.data.sensor_fit = "HORIZONTAL"
point_object(diag_cam, (0.0, 0.25, 0.35))
scene.camera = front_cam

# Candidate A — strict single ~90° face-plane hinge.
# Parent centre A0 = (-2.2, 0, 0).
# Hinge axis: world Y through parent top-right edge plane:
#   x = A0.x + 0.50L, z = +0.50L.
# Child local centre from hinge = (+0.60L, 0, -0.50L).
# Start angle -90° => centre A0 + (1.00, 0, 1.10).
# End angle 0°   => centre A0 + (1.10, 0, 0.00).
# Parent/child closest clearance is 0.10L for the full analytic sweep.
A0 = Vector((-2.2, 0.0, 0.0))
a_parent = add_cube("A_Parent", A0)
a_hinge = add_empty("A_Hinge_FacePlane_Y", A0 + Vector((0.5, 0.0, 0.5)))
a_child = add_cube("A_Child", (0, 0, 0))
a_child.parent = a_hinge
a_child.location = (0.6, 0.0, -0.5)
key_rot(a_hinge, F(T_HOLD), -90, "Y")
key_rot(a_hinge, F(T_STAGE1_END), 0, "Y")
key_rot(a_hinge, F(T_END), 0, "Y")
damped_interp(a_hinge)

# Candidate C — genuine rear-stow + two mechanically distinct hinge events.
# Parent centre C0 = (+2.2, 0, 0).
# Start child centre = C0 + (0, +1.10, 0): 0.10L behind parent.
# No hide/opacity keyframes: the child is present continuously.
#
# Stage 1:
#   H1 world axis = Z through parent back-right vertical edge:
#       x = C0.x + 0.50L, y = +0.50L.
#   H2 local origin in H1 = (0, +0.60L, +0.50L).
#   Child local centre in H2 = (-0.50L, 0, -0.50L).
#   H1 0° -> -90° around Z.
#   Child centre: rear stow C0+(0,1.10,0) -> rear-right C0+(1.10,1.00,0).
#
# Stage 2:
#   H1 stays at -90°. H2's LOCAL Y axis is then WORLD +X.
#   Its world hinge line lies at y=+0.50L, z=+0.50L (parent back-top face edge).
#   H2 0° -> -90° around local Y / world X.
#   Child centre: C0+(1.10,1.00,0) -> east final C0+(1.10,0,0).
#   During stage 2 the child's world-X interval remains [C0.x+0.60, C0.x+1.60],
#   so the parent's max X at C0.x+0.50 retains an exact 0.10L clearance.
C0 = Vector((2.2, 0.0, 0.0))
c_parent = add_cube("C_Parent", C0)
c_h1 = add_empty("C_Hinge1_BackRight_Z", C0 + Vector((0.5, 0.5, 0.0)))
c_h2 = add_empty("C_Hinge2_BackTop_LocalY", (0.0, 0.6, 0.5), parent=c_h1)
c_child = add_cube("C_Child", (0, 0, 0))
c_child.parent = c_h2
c_child.location = (-0.5, 0.0, -0.5)

key_rot(c_h1, F(T_HOLD), 0, "Z")
key_rot(c_h1, F(T_STAGE1_END), -90, "Z")
key_rot(c_h1, F(T_END), -90, "Z")
damped_interp(c_h1)

key_rot(c_h2, F(T_HOLD), 0, "Y")
key_rot(c_h2, F(T_STAGE2_START), 0, "Y")
key_rot(c_h2, F(T_STAGE2_END), -90, "Y")
key_rot(c_h2, F(T_END), -90, "Y")
damped_interp(c_h2)

# Save prototype + evidence stills + front comparison animation.
blend_path = OUT / "studygrid-v4a-hidden-mechanics-compare.blend"
bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))

checkpoints = {
    "00_start_stowed": F(0.5),
    "01_stage1_mid": F(2.0),
    "02_stage1_landed": F(3.15),
    "03_stage2_mid": F(4.5),
    "04_final": F(5.75),
}

for camera_name, camera in (("front", front_cam), ("diag", diag_cam)):
    scene.camera = camera
    for label, frame in checkpoints.items():
        scene.frame_set(frame)
        scene.render.filepath = str(OUT / "stills" / f"{camera_name}_{label}.png")
        bpy.ops.render.render(write_still=True)

scene.camera = front_cam
scene.render.filepath = str(OUT / "frames" / "frame_")
bpy.ops.render.render(animation=True)

manifest = f"""StudyGrid V4A hidden-mechanics comparison prototype
Quality: {ARGS['quality']}
FPS: {FPS}
Resolution: {scene.render.resolution_x}x{scene.render.resolution_y}
Cube edge L: {L}
Resting air gap: {GAP}L
Bevel: {BEVEL}L
Material: metallic 0.0 / roughness {ROUGHNESS}
Floor Z: {FLOOR_Z}L (kept below all sampled cube sweeps)
Comparison camera: fixed 50mm, exact front axis (0,-15,0) -> origin
Diagnostic camera: fixed 50mm oblique (7,-10,6)

Candidate A
- one face-plane Y hinge through parent edge x=+0.50L, z=+0.50L
- child local centre (+0.60L, 0, -0.50L)
- -90° -> 0°
- source target rest gap 0.10L

Candidate C
- starts at rear centre offset (0,+1.10L,0), present from frame 1
- NO visibility/opacity toggle and NO scale animation
- H1: world Z on parent back-right edge, 0° -> -90°
- H2: local Y; after H1 it is world X on parent back-top edge, 0° -> -90°
- intermediate centre (+1.10L,+1.00L,0)
- final centre (+1.10L,0,0)
- source target rest gap 0.10L
- exact-front start is genuine geometric occlusion; oblique diagnostic exposes the rear child

This prototype does not choose the owner's final hinge option.
Run blender/verify_v4a_hidden_mechanics.py independently for sampled collision/clearance evidence.
"""
(OUT / "qa_manifest_hidden_mechanics.txt").write_text(manifest, encoding="utf-8")
print(manifest)
