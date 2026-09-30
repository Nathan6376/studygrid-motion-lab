# StudyGrid V4A — Export / Runtime Readiness

Scope: export-readiness audit only. This package does not alter V4A mechanics, choose a hinge, or make the current QA scene production-ready.

## Evidence bound

- Current main source audited: `blender/scene_v4a.py` at blob `cb87739e3f254222e9e336eb0db5b25164f59bb8` (main head observed `2daca92eef8e25b92e36e30f5f599ce67586ae66`).
- Post-Bob mechanics/render reference: commit `13200b8c6111b65608d755a576b170b55427a72e`, Actions run #10 `36715371870`.
- Run #10 artifact: `studygrid-v4a-owner-qa`, artifact `11096826897`, GitHub digest `sha256:61b50e5d7b16b94e4e5ba0acbe5010ab165c8e4a2d9ae736c8c31d6bb4087290`.
- Artifact runtime source rehash: `af7425d17a4b64fd62ecb961e0a4da8ef00ffd7405312686f04d90c101e6f144`, matching its receipt.
- Artifact `.blend` rehash in this lane: `f14d1dad42eeb1fadd0e6640a36503168904bb712723aec1c5a770cc631ad7d0`.
- Blender runtime is not installed in Stuart's current execution environment; `bpy` is also unavailable. Therefore the new preflight could not be executed against the `.blend` here. Source/static verification and artifact identity checks are complete; Blender-runtime findings remain to be run later.

## Audit matrix

| Area | Status | Current finding | Later handoff requirement |
|---|---|---|---|
| Object names / hierarchy | PASS (source) | Stable named diagnostic objects and explicit hinge parentage exist for 2A and the C→E→SE chain. 2C hierarchy exists but remains mechanically rejected by the prior acceptance lane. | Preserve stable approved node names/parents in the export subset; do not treat current 2C hierarchy as accepted. |
| Applied transforms / scale | PASS + WARN (source) | `add_cube()` applies creation scale. The temporary `Seed` deliberately animates scale 0.08→1.0. | Approved production cubes should export at unit scale; Seed scale animation must not silently become production behaviour. |
| Cube reuse / instancing | WARN | Each `add_cube()` call creates a fresh primitive; the QA scene is authored as separate mesh datablocks, not a shared instanced cube asset. | After mechanics approval, create an export/runtime cube asset strategy (shared geometry / runtime instancing) in an export copy, not by rewriting the QA scene. |
| Bevels / modifiers | WARN | All cubes receive a Blender Bevel modifier (`0.055L`, 4 segments). | Lock whether the GLB export uses evaluated/baked bevel geometry or an equivalent web geometry/material treatment; verify the result in the round-trip. |
| Canonical G / shape-key risk | HOLD | Current G is `SG_G_PROVISIONAL`, a Blender Curve with animated `bevel_depth`; canonical G is not frozen. | Do not build the production G export contract yet. When canonical G arrives, verify mesh/curve conversion, shape keys, modifiers and animation compatibility before export. |
| Camera projection | PASS (source) / runtime check pending | `SG_Camera` is 50 mm with `sensor_fit='VERTICAL'`; doorway enlargement is physical camera translation. | Exported glTF `yfov` must be read back from the GLB/Three.js camera and compared to Blender; do not infer web FOV from source alone. |
| Animation / sampling | PASS + WARN | Mechanics primarily use object/empty TRS animation, which is the right portable class. The QA scene also uses curve-data animation and Blender visibility keys. | Bake/sample only the approved transform tracks at an explicit rate; compare key poses and timing after GLB load. Non-TRS QA animation must be removed or replaced deliberately. |
| Visibility schedule | WARN | Studies are isolated with `hide_render` / `hide_viewport` keyframes. | Move study visibility/show-hide timing to the Three.js/runtime schedule or approved metadata; do not assume GLB preserves Blender visibility semantics. |
| AREA lights | WARN | Three Blender AREA lights create the QA look. | Web lighting must be rebuilt/overridden deliberately. Do not use their presence in the `.blend` as evidence that the GLB reproduces lighting. |
| Materials | WARN | `SG_Green` / `SG_Floor` are QA materials; the green is explicitly provisional. | Treat materials as placeholders. Runtime material, colour management and lighting are a separate web contract. |
| Doorway handoff | PASS + WARN | Fixed 50 mm physical approach is authored. No dedicated export/handoff marker empties are defined; timing is encoded in the camera animation. | After owner mechanics approval, add explicit export/runtime markers or metadata for approach start, stop/handoff and camera identity in the export package. |
| Diagnostic scene contamination | HOLD for production | Floor, QA lights, provisional G, Seed proxy, unresolved 2C and all comparison studies coexist in one diagnostic `.blend`. | Never ship the QA `.blend` wholesale as runtime state. Curate an approved export subset after the owner mechanics decision. |

## What V4A already gives the later web handoff

- Stable object names for the current diagnostic studies.
- Explicit parent/child transform chains for accepted 2A and the accepted C→E→SE diagnostic chain.
- Equal cube-size intent and a 0.10L resting-gap contract in the accepted studies.
- Fixed-lens doorway camera motion rather than FOV zoom cheating.
- A known Blender version from run #10 (`4.5.14 LTS`) and exact artifact/source identities for reproducibility.

## What stays deliberately blocked

1. Study 2C export acceptance: still rejected until Bob/General provide a genuinely hidden start, honest distinct mechanics, clearance and correct gap.
2. Canonical G topology/export method: current curve is only a proxy.
3. Final G→seed transition: current Seed scale-up is only a QA proxy.
4. Final 3×3 choreography and production node set.
5. Production material/lighting look.
6. Production export subset, runtime visibility schedule and doorway marker schema.

## Changes that should wait until after owner mechanics approval

- Do not apply/bake modifiers in the V4A QA scene.
- Do not replace separate cube meshes with instances inside the QA scene.
- Do not add production marker empties or export metadata to `scene_v4a.py` yet.
- Do not convert the provisional G into a production mesh or create shape keys yet.
- Do not rewrite visibility keys into a runtime schedule yet.
- Do not build the final GLB or Three.js integration from unresolved 2C/final choreography.

## Smallest later round-trip before web implementation

After the mechanics choice is approved, make a throwaway export copy containing only one approved hinge fixture (2A is currently mechanically valid), its parent/child hierarchy, one cube material placeholder and the fixed-lens doorway camera. Export that subset to GLB with locked exporter settings, then load it with Three.js `GLTFLoader` and compare:

1. node names and parentage;
2. unit scales and cube dimensions;
3. hinge start/mid/end world transforms and 0.10L resting gap;
4. animation duration and sampled key timing;
5. camera `yfov`, aspect handling and physical approach start/stop transforms;
6. absence of Blender-only visibility/light assumptions.

Only after that minimal round-trip matches should the larger approved choreography be exported. This technical fixture does not select the owner's final hinge option.
