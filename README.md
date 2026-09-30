# StudyGrid Motion Lab

Private owner-QA lab for the StudyGrid entry/tutorial motion.

## Current gate: V4A

This repository exists to prove the motion in real 3D before StudyGrid browser integration.

The first workflow renders five mechanics studies:

1. Provisional G stroke-thickness reduction and seed handoff
2. Strict single ~90° face-plane hinge
3. Hidden-behind 90° + 90° hinge
4. Three-cube parent/child chain
5. Fixed-FOV physical camera approach into a doorway cube

## Run

GitHub → Actions → **Render StudyGrid V4A** → Run workflow → `preview`.

When complete, download the `studygrid-v4a-owner-qa` artifact.

Review the MP4 and stills on iPad. The `.blend` source is included in the artifact.

## Important

- The G in the first render is explicitly **provisional** until the canonical StudyGrid G vector is frozen.
- Do not treat this repository as StudyGrid production code.
- Do not merge this motion into R5/R6 or main StudyGrid based on this lab alone.
- Final 3×3 choreography remains unresolved until owner visual QA.
