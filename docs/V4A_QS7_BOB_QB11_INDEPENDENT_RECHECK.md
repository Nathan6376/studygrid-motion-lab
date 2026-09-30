# StudyGrid V4A — Stuart Q-S7 Independent Recheck of Bob Q-B11

**Worker:** Stuart  
**Coordinator:** ChatGPT General CF-0040  
**Completed:** 2026-09-30 13:57 ET  
**Disposition:** **PASS**

## Authoritative input

Bob branch `bob-cf0042-qb11-align-integration-prep-state-contract` at commit `7433bafe25b7f0823854966607e0d17a6d4167fc`, exactly as named in `queues/STUART_QUEUE.txt`.

Provider-visible blobs checked:
- `integration/MOTION_HTML_ADAPTER_CONTRACT.txt` — `90b8d8d847d4f0ac9bf1a8a078949e7efc123a86`
- `integration/FALLBACK_STATE_MACHINE_CONTRACT.txt` — `bf8ed72e4358cf2c93159a28a09da7b54dec7a31`
- `integration/fallback_state_machine.json` — `55333fd8fee85245999b85aa2cc02d21bf36edde`
- `integration/motion_fallback_harness.py` — `baeff90567f388c9f5d81869d0ef4c1c3ab6178d`
- `integration/motion_html_seam_map.json` — `70b212376cf43a035ceedd42ec4a035a694c6d85`
- `integration/verify_motion_fallback_harness.py` — `5f78597218394db9bf517b9e2ef812e7e74ed77f`
- `integration/qb11_verification.json` — `e5d2d5bab5706316a777d1af6483159e012fff1d`

## Independent result

Q-B11 clears Stuart's Q-S6 hold. The amended adapter contract, fallback contract, canonical JSON and harness now agree on the same 13 states, 13 events and 33 allowed transitions.

The prior Q-S6 defects are resolved:
1. `SLOW_LOAD`, `FALLBACK_STATIC` and `SHELL_READY` are now in the shared canonical model.
2. `READY -> FAILED` and `RUNNING -> FAILED` are explicitly valid through the `FAILURE` event in contract, JSON and harness.
3. Invalid `NEW -> SKIPPED` and `NEW -> FAILED` calls now raise/reject rather than silently transitioning.
4. Transition enforcement is centralized through the canonical graph.

## Re-run evidence

Exact read-only HTML sources independently re-hashed:
- R5: `0fee828511bdccd373fdc0625c0ea9f894485a57f6e6cbceff74e2652ec34d00`, 874986 bytes — PASS.
- R6: `875a81262d80cf33ceb32545ff20c1cbc03ae91db34c66a3a8a679f93f0314ef`, 954208 bytes — PASS.

Common source anchors remain present in both: reduced-motion CSS, app less-motion CSS, entry root reservation, `.welcome-page`, `focusRouteEntry()` and `render()`.

Original Q-B10 acceptance re-run: **12/12 PASS**.
- reduced motion
- app less motion
- WebGL unavailable
- slow-load Continue
- asset failure
- hard timeout
- running Skip
- normal completion
- route dispose
- viewport fixed lens, 6/6
- Q-B2 doorway envelope, 6/6
- active-state escape, 4/4

Expanded Q-B11 regression re-run: **6/6 PASS**.
- canonical contract alignment: 33/33 allowed transitions represented
- allowed Skip paths: 4/4
- dispose from mounted/non-NEW states: 11/11
- READY/RUNNING failure recovery: 2/2
- invalid NEW Skip/failure: 2/2 rejected
- all canonical states × six representative viewports: 78/78 layout reservations preserved

Additional Stuart adversarial matrix: every one of 13 states × 13 events was checked against the canonical harness graph. **33 valid transitions accepted; 136 invalid transitions rejected; 0 mismatches.**

## Seam / role regression

The common HTML seam remains `#root > .welcome-page`; Q-B11 does not move the host into R5/R6 content geometry. R5 remains the accepted read-only baseline. R6 remains verified, unpromoted and read-only. General still owns the later HTML integration-baseline decision.

The Q-B10→Q-B11 compare is 8 commits ahead and changes exactly 8 preparation/docs files. It does not modify StudyGrid product HTML, R5, R6, main motion scene, backend, auth, Supabase or deployment.

## Runtime evidence boundary

PASS is for the preparation contract/harness only. It does **not** promote synthetic evidence into browser DOM/keyboard/assistive-technology focus proof, real GPU/WebGL failure or recovery proof, or rendered device acceptance. Those remain later runtime QA.

## Queue continuation

Q-S2 was refreshed after Q-S7 and remains **BLOCKED / NOT STARTED**. Current shared GitHub evidence still shows Kevin's only full-context workflow run `36734968949` as terminal failure and its artifact list is empty. No durable valid A+C full-context artifact is present on the checked shared surfaces. Q-S3 remains dependency-blocked.

## Boundaries preserved

No product/main/R5/R6/motion-scene/backend/auth/Supabase/deploy mutation. No A/C selection. No Kevin recovery overlap. No promotion.
