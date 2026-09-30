# StudyGrid V4A — Q-S4 Acceptance Validator Path Repair

## Scope
Tooling repair only. The frozen A/C acceptance criteria and the historical Q-S1 raw result remain unchanged.

## Defect reproduced
Kevin run-2 artifact `11103902103` stores the payload at ZIP root, while `artifact_sha256.txt` records the producing directory prefix `output-v4a-hidden/`. The frozen validator treated every prefixed target as missing and emitted 19 false FAIL rows even though the payload hashes were correct.

## Repair
New entrypoint: `tools/v4a_ac_artifact_validator_repaired.py`.

It imports the frozen validator unchanged and replaces only `verify_hash_receipts` with `tools/v4a_ac_receipt_paths.py`.

The repair accepts only:
1. exact receipt-parent paths;
2. exact artifact-root paths; or
3. the explicit known `output-v4a-hidden/` producing-prefix when that directory is absent and stripping exactly that one prefix resolves to one existing file.

It still rejects unsafe traversal/backslash paths, unknown prefixes, missing targets, SHA mismatches, and duplicate normalized receipt targets. The historical validator file is preserved.

## Exact Kevin run-2 regression
Artifact ZIP SHA-256: `0b71adc48c9d47f395e204e0a4ba8f5fae19f2a5afb8a97180a9af8be947ae14` — matches provider digest.

Repaired receipt layer against the exact downloaded ZIP:
- 19 receipt entries
- 19 PASS
- 0 FAIL
- all 19 resolved only through the explicit `output-v4a-hidden/` flattened-root rule
- no artifact bytes mutated

## Synthetic regression set
Local syntax compile: PASS.

Cases exercised:
- known-prefix flattened root: PASS
- exact prefixed-root layout: PASS
- duplicate normalized receipt target: rejected
- traversal path: rejected
- unknown prefix: rejected / not stripped
- hash mismatch: rejected
- missing target: rejected

The repaired wrapper itself compiled successfully. The original frozen validator remains the source for every non-path acceptance check; Q-S4 does not alter visual/mechanics criteria or the prior Q-S1 A/C PASS verdict.
