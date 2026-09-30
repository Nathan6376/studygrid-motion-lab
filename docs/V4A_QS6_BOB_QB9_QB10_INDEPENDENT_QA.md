# StudyGrid V4A — Stuart Q-S6 Independent QA

**Worker:** Stuart  
**Coordinator:** ChatGPT General CF-0040  
**Completed:** 2026-09-30 13:12 ET  
**Scope:** Bob Q-B9 Motion→HTML integration seam + Q-B10 reduced-motion/loading/failure fallback preparation only.

## Disposition

- **Q-B9: HOLD** — the core common seam is independently **PASS**, but its adapter state/event vocabulary is not aligned with Q-B10.
- **Q-B10: HOLD** — Bob's reported 12-group verifier independently re-runs **PASS**, and extended positive paths pass, but the harness does not enforce the formal state machine and the formal failure graph is incomplete relative to the Q-B9 runtime contract.
- These are preparation-contract findings, not StudyGrid product/runtime failures.

## Exact source identity

- Accepted R5: SHA-256 `0fee828511bdccd373fdc0625c0ea9f894485a57f6e6cbceff74e2652ec34d00`, 874986 bytes.
- Unpromoted R6: SHA-256 `875a81262d80cf33ceb32545ff20c1cbc03ae91db34c66a3a8a679f93f0314ef`, 954208 bytes.
- Q-B9 branch/head: `bob-cf0042-qb9-motion-html-seam-map` @ `ce9889635ce18e66d7548fe2b57b6e080b42fb86`.
- Q-B10 branch/head: `bob-cf0042-qb10-fallback-harness` @ `06ca7b6557b1cc2160873bd26ac42d51f457a01a`.
- Stuart used the exact Drive R5/R6 bytes and did not mutate them.

## Q-B9 independent checks

PASS:
- R5/R6 exact digests and byte sizes match Bob's evidence.
- `#root > .welcome-page` is genuinely common to both R5 and R6.
- `.welcome-shell` remains the common interactive content layer; R6's `.r6-welcome-grid` is an inner content difference and is not required by the proposed motion host.
- Common `render()`, route-change and `focusRouteEntry()` seams exist in both exact sources.
- R5 remains the accepted read-only baseline and R6 remains an unpromoted read-only candidate.
- Candidate A/C is opaque behind the adapter; no A/C winner, HTML integration baseline, canonical G or final 3x3 identity is selected.
- No auto-navigation, product-state ownership or candidate-specific content geometry is introduced.

HOLD finding:
- Q-B9's adapter state/event vocabulary contains `MOUNTED, LOADING, READY, RUNNING, HANDOFF_READY, SKIPPED, REDUCED_MOTION, FAILED, DISPOSED`.
- Q-B10's state machine adds `SLOW_LOAD, FALLBACK_STATIC, SHELL_READY` as canonical states.
- There is therefore no single shared adapter state/event enum for later integration.

## Q-B10 independent checks

Bob's exact published verifier was independently re-run against the exact R5/R6 bytes: **12 reported groups PASS / 0 FAIL**.

Stuart extended the positive coverage and confirmed:
- reduced motion and app less-motion reach shell-ready without WebGL/full motion;
- WebGL unavailable reaches static/shell-ready without an asset request;
- Skip/Continue succeeds from each documented active state: LOADING, SLOW_LOAD, READY and RUNNING;
- failure handling in the harness reaches shell-ready from LOADING, SLOW_LOAD, READY and RUNNING;
- disposal releases renderer/assets from each tested active state;
- layout reservation remains invariant across LOADING/SLOW_LOAD/READY/RUNNING × all six representative viewports (24/24 combinations);
- fixed lens is invariant and aspect follows the host viewport across all six viewports;
- Q-B2 doorway cover math independently reproduces the six Q-B10 viewport values and stays outside the 0.12L near boundary;
- synthetic non-user focus token continuity and active-state escape/no-dead-end checks pass.

Material HOLD findings:
1. The formal Q-B10 JSON defines failure to `FAILED` from MOUNTED (WebGL unavailable) and LOADING/SLOW_LOAD (asset failure/timeout), but not from READY or RUNNING. Q-B9 says load/runtime states may fail, and Q-B10's own harness accepts READY/RUNNING failure. Contract, state graph and harness are inconsistent.
2. The harness does not enforce the formal graph. `skip()` from NEW silently yields `SKIPPED -> SHELL_READY`; `asset_fail()` from NEW silently yields `FAILED -> FALLBACK_STATIC -> SHELL_READY`. Those transitions are not in the formal state machine and should be rejected/guarded rather than accepted.
3. Focus continuity here is a synthetic token check, not browser DOM, keyboard or assistive-technology focus proof. GPU/WebGL recovery and visual acceptance also remain unverified, as Bob's own limitation correctly states.

## Smallest corrective route for General

Route back to Bob for **integration-prep-only amendment**:
1. Define one canonical Q-B9/Q-B10 adapter state/event enum including `SLOW_LOAD`, `FALLBACK_STATIC` and `SHELL_READY`.
2. Align runtime failure semantics across contract/JSON/harness: explicitly support READY/RUNNING → FAILED, or narrow all three consistently.
3. Make `skip()` and failure methods enforce the canonical transition graph; invalid NEW → SKIPPED / NEW → FAILED must reject rather than silently succeed.
4. Extend the verifier to cover all allowed skip paths, dispose from every active state, READY/RUNNING failure, invalid-transition negative tests, and all-state × six-viewport layout reservation.
5. Preserve real browser/device/AT focus and GPU recovery as later integration QA; do not promote synthetic evidence into runtime acceptance.

## Boundaries preserved

No StudyGrid product/main/R5/R6/motion-scene/workflow/backend/auth/Supabase/deployment mutation. No Kevin Q-K1 recovery overlap. No A/C selection. No canonical-G or final-3x3 selection.
