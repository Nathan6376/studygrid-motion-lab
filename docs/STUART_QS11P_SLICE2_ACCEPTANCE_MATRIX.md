# Stuart Q-S11P — Slice 2 Acceptance Harness / Adversarial Prep

Lifecycle: PREP ONLY. This packet is **not Q-S11 acceptance evidence** and makes no claim about Bob Q-B15 bytes. It is implementation-independent and is bound only to General’s accepted Slice 1 pointer plus the published Q-B15 contract.

## Frozen preparation basis

- Accepted Slice 1: `StudyGrid-CF0042-QB14-local-product-gateway.html` / Drive `1S4eIU6VT2pnNQ4h5SHEGhJ3sWb7BLU6W` / SHA-256 `fcf89e5a31063746272a10bbfba72d605f745d01f797c75fa33697923dde6bb1` / 965519 bytes / `v7.17-cf0042-qb14-local-product-gateway`.
- Current accepted registry anchor: rev 11 / 237 entries / 237 unique component IDs.
- Q-B15 target: Professor Home / multi-course scale only. No Slice 3/4, backend/network/provider/deploy, motion/A-C, or canonical promotion.
- Direct physical-device, hosted-origin and full-accessibility evidence remains a later HOLD unless actually obtained during Q-S11.

## Acceptance matrix

| Gate | Category | Required observation | Evidence | Terminal |
|---|---|---|---|---|
| `ID-01` | identity | Exact provider filename/ID/SHA/bytes/version matches General-confirmed Q-B15 identity. | provider metadata + local rehash | PASS/FAIL |
| `ID-02` | derivation | Candidate derives from exact accepted Slice 1 bytes, not R6/Q-B13/another branch. | exact baseline rehash + bounded diff | PASS/FAIL |
| `ID-03` | boundary | Candidate remains non-canonical/not deployed. | General pointer + changed-text boundary | PASS/FAIL |
| `HOME-01` | scale | Current-term Professor Home represents approximately six courses and hundreds of students. | normalized course fixture + totals | PASS/FAIL |
| `HOME-02` | scale | Professor Home is bounded summary/navigation, not a full-roster long-scroll dashboard. | DOM summary probe | PASS/FAIL |
| `HOME-03` | today | Today / Now & next is derived only from confirmed schedule fixture. | read-model fixture probe | PASS/FAIL |
| `HOME-04` | today | Today never auto-opens, auto-navigates or steals selected-class context. | before/after route+selection oracle | PASS/FAIL |
| `ATTN-01` | attention | Live attention contains unresolved actionable items only. | normalized live attention oracle | PASS/FAIL |
| `ATTN-02` | attention | Resolving an item removes it from live attention. | before/after transition | PASS/FAIL |
| `ATTN-03` | attention | Resolved item remains in local history/audit fixture state. | history oracle | PASS/FAIL |
| `ATTN-04` | attention | All-resolved state shows no live attention without erasing history. | adversarial all-resolved fixture | PASS/FAIL |
| `CLASS-01` | identity | Each class exposes explicit name, code and section. | course fixture + DOM text | PASS/FAIL |
| `CLASS-02` | identity | Each class exposes useful student and open-question context. | course fixture + DOM text | PASS/FAIL |
| `CLASS-03` | identity | Duplicate colours/labels do not make classes ambiguous. | duplicate colour/label adversarial fixture | PASS/FAIL |
| `ORG-01` | organization | Pin/favourite/colour/label controls are optional and transparent. | before/after course-set equality | PASS/FAIL |
| `ORG-02` | organization | Alternate sort is explicit and deterministic. | name/code sort oracle | PASS/FAIL |
| `ORG-03` | organization | No opaque risk/readiness/priority ranking is introduced. | source/read-model key scan + UI copy | PASS/FAIL |
| `ORG-04` | organization | Sort/pin toggles preserve the same course population. | toggle adversarial fixture | PASS/FAIL |
| `DRILL-01` | drill-in | Professor Home drill-in selects the intended class. | runtime route/selection | PASS/FAIL |
| `DRILL-02` | drill-in | Existing selected-class R6 workspace remains the destination. | workspace tab oracle | PASS/FAIL |
| `DRILL-03` | drill-in | Professor Home does not replace accepted Overview/Assessments/Questions/Students/Sources architecture. | DOM/workspace oracle | PASS/FAIL |
| `GW-01` | gateway | Authoritative state remains behind StudyGridProductGateway/read-model/command boundary. | static + runtime gateway probe | PASS/FAIL |
| `GW-02` | gateway | section/source revision/block/display locator identity remains explicit. | source inventory oracle | PASS/FAIL |
| `GW-03` | gateway | One assessment revision remains shared across four accepted views. | shared revision oracle | PASS/FAIL |
| `GW-04` | gateway | Stale cross-course update fails closed without mutation. | stale command adversarial case | PASS/FAIL |
| `GW-05` | gateway | Unauthorized update fails closed without mutation. | unauthorized command adversarial case | PASS/FAIL |
| `GW-06` | gateway | ready/loading/empty/error/stale_revision/unauthorized remain deterministic. | state replay | PASS/FAIL |
| `REG-01` | regression | Q-B13 sort focus returns to r6StudentSort. | runtime focus probe | PASS/FAIL |
| `REG-02` | regression | Q-B13 filter focus returns to r6StudentFilter. | runtime focus probe | PASS/FAIL |
| `REG-03` | regression | Assessment confirmation focus returns to r6TaskCanvas without scroll jump. | settled runtime focus+scroll | PASS/FAIL |
| `REG-04` | regression | Roving instructor tabs still work. | keyboard ArrowRight/ArrowLeft | PASS/FAIL |
| `REG-05` | regression | Policy dialog focus/Escape returns to r6InspectPolicy. | dialog runtime probe | PASS/FAIL |
| `REG-06` | regression | Accepted Slice 1 gateway command/state/source identity checks remain clean. | compact Q-S10 regression replay | PASS/FAIL |
| `REG-07` | registry | Registry rev does not regress and IDs remain unique; accepted IDs survive. | registry JSON parse | PASS/FAIL |
| `RESP-01` | responsive | Professor Home passes desktop/tablet/phone no-overflow/duplicate-ID smoke. | Paper+Dusk matrix | PASS/FAIL |
| `RESP-02` | responsive | Large counts/duplicate labels do not overflow mobile class cards/controls. | adversarial mobile fixture | PASS/FAIL |
| `EDGE-01` | adversarial | No-current-day schedule produces a bounded empty Today state without navigation. | empty/current-day fixture | PASS/FAIL |
| `EDGE-02` | adversarial | Hundreds-student counts remain summarized and readable. | large roster fixture | PASS/FAIL |
| `EDGE-03` | adversarial | Focus restores after Professor Home organization actions. | action→focus probe | PASS/FAIL |
| `EDGE-04` | adversarial | Duplicate course labels/colours remain distinguishable by name/code/section. | duplicate fixture | PASS/FAIL |
| `SCOPE-01` | scope | No Slice 3 setup/autofill/human-timing surface. | candidate-added-text scan | PASS/FAIL |
| `SCOPE-02` | scope | No Slice 4 enrolment surface. | candidate-added-text scan | PASS/FAIL |
| `SCOPE-03` | scope | No backend/auth/Supabase/network/provider dependency. | candidate-added-text + request log | PASS/FAIL |
| `SCOPE-04` | scope | No Blender/motion/A-C work. | candidate-added-text scan | PASS/FAIL |
| `SCOPE-05` | scope | No canonical promotion/deployment. | changed-text/provider-state check | PASS/FAIL |
| `HOLD-01` | hold | Physical devices, hosted-origin, VoiceOver/Pencil/physical keyboard/true 200% zoom/full WCAG remain HOLD absent direct evidence. | explicit evidence boundary | HOLD unless direct evidence |

## Adversarial cases that must be exercised

- No current-day schedule: Today renders a bounded empty state and does not alter route, selected class or workspace context.
- All attention resolved: live attention becomes empty while resolved records remain in local history/audit fixture state.
- Duplicate course colours and duplicate labels: classes remain distinguishable by explicit name + code + section.
- Hundreds-student scale: six-course fixture totals at least hundreds of students while Home stays summary/navigation rather than rendering full rosters.
- Sort/pin toggles: course population is invariant; ordering/organization is explicit and deterministic; no hidden rank/risk score.
- Stale cross-course update: stale revision maps to STALE_REVISION/stale_revision and authoritative fixture truth is byte/structure-equivalent before vs after.
- Unauthorized cross-course update: UNAUTHORIZED/unauthorized and no authoritative mutation.
- Mobile stress: large counts, duplicate labels/colours and organization controls do not cause duplicate IDs or page-level horizontal overflow.
- Focus restoration: after Professor Home organization actions, focus returns to a sensible initiating/replacement control; existing Q-B13 sort/filter/task-canvas and policy-dialog return targets remain intact.

## Reusable scaffolding

- `tests/stuart_qs11_professor_home_oracles.py` — pure acceptance oracles. It never imports or mutates StudyGrid runtime code.
- `tests/stuart_qs11p_scaffold_selftest.py` — synthetic positive/negative adversarial self-test for the oracles. Current result: 39/39 PASS.
- `tests/stuart_qs11_slice2_acceptance_spec.json` — machine-readable 46-gate catalogue and exact accepted Slice 1 anchor.
- `tests/stuart_qs11_runtime_observation_template.json` — normalized observation contract for Q-S11. Candidate-specific browser probing fills this from exact provider bytes; the oracle layer stays unchanged.
- `tests/stuart_qs11p_prep_results.json` — prep-only validation proving the exact Slice 1 anchor/version/gateway/registry and matrix shape; 7/7 PASS. It is not candidate evidence.

## Q-S11 execution rule

When Bob Q-B15 becomes durable, Q-S11 must first re-fetch the provider candidate and General-confirmed identity, independently recompute SHA/bytes/version, and prove exact derivation from the accepted Slice 1 bytes. Then bind runtime observations from those exact candidate bytes into the normalized observation contract and run the oracles. Candidate evidence supersedes all prep assumptions. Any selector/implementation detail needed for probing is discovered only from the provider-visible candidate at Q-S11 time; this prep does not constrain Bob’s implementation.

## Boundary

No StudyGrid product/runtime bytes were changed. No Bob private work-in-progress was inspected. No A/C choice was made. No backend/auth/Supabase/network/provider/deployment, Blender/motion, or canonical action was taken.
