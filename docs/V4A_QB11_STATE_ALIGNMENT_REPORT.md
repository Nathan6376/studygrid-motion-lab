# StudyGrid V4A — Bob Q-B11 Q-B9/Q-B10 State-Contract Alignment

**Worker:** Bob / CF-0042  
**Coordinator:** ChatGPT General CF-0040  
**Scope:** integration-prep-only amendment from Stuart Q-S6.  
**Authoritative QA input:** `stuart-qs6-qb9-qb10-independent-qa` @ `9dd9b22fe7b52cde1f8fa0650a8a11a7ed25bd6c`.

## Result

Q-B11 aligns the Q-B9 motion→HTML adapter vocabulary with the Q-B10 fallback state machine without touching StudyGrid product HTML, R5/R6, motion mechanics, backend/auth/Supabase, deployment, canonical G, final 3×3 choreography, or Candidate A/C selection.

### Before

Stuart Q-S6 identified three material preparation-contract drifts:

1. Q-B9 omitted `SLOW_LOAD`, `FALLBACK_STATIC`, and `SHELL_READY` from its adapter state/event vocabulary.
2. Q-B10 formal JSON omitted `READY -> FAILED` and `RUNNING -> FAILED`, while the prose/runtime intent and harness accepted those failures.
3. Q-B10 `skip()` and failure handling did not enforce the formal graph, so invalid `NEW -> SKIPPED` and `NEW -> FAILED` silently succeeded.

### After

- One canonical state enum now spans Q-B9/Q-B10: `NEW, MOUNTED, REDUCED_MOTION, LOADING, SLOW_LOAD, READY, RUNNING, FAILED, FALLBACK_STATIC, SKIPPED, HANDOFF_READY, SHELL_READY, DISPOSED`.
- One canonical event enum is shared by the adapter contract, seam map, JSON state graph, harness and verifier.
- `READY/RUNNING --FAILURE--> FAILED -> FALLBACK_STATIC -> SHELL_READY` is explicit and tested.
- `skip()` is graph-guarded and only valid from `LOADING/SLOW_LOAD/READY/RUNNING`.
- Failure is graph-guarded; `NEW -> FAILED` rejects.
- `DISPOSE` is accepted from every mounted/non-NEW canonical state.
- The original Q-B9 `#root > .welcome-page` seam and R5/R6 read-only roles are preserved.

## Verification

- Exact R5 SHA-256: `0fee828511bdccd373fdc0625c0ea9f894485a57f6e6cbceff74e2652ec34d00` — PASS.
- Exact R6 SHA-256: `875a81262d80cf33ceb32545ff20c1cbc03ae91db34c66a3a8a679f93f0314ef` — PASS.
- Original Q-B10 acceptance groups: **12/12 PASS**.
- Expanded Q-B11 regression groups: **6/6 PASS**.
- Canonical JSON/harness graph: 33/33 transition entries aligned.
- Allowed skip paths: 4/4 PASS.
- READY/RUNNING failure paths: 2/2 PASS.
- Invalid NEW skip/failure negatives: 2/2 rejected as required.
- Dispose: every mounted/non-NEW canonical state PASS.
- Layout reservation: 13 canonical states × 6 representative viewports = 78/78 PASS.
- Python compile + JSON parse: PASS.

## Remaining HOLD items

These remain later integration/runtime QA and were not promoted by synthetic evidence:
- real browser DOM/keyboard/assistive-technology focus behaviour;
- real GPU/WebGL failure and recovery;
- rendered visual/device acceptance;
- General's eventual authorized HTML baseline;
- approved motion profile/asset manifest;
- canonical G/final 3×3 asset identity.

No A/C candidate is selected by this package.
