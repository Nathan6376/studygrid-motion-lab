# Exact-source audit evidence

Read REPORT.md first. This is a report-only branch for General CF-0047, not a product patch or release.

The original HTML is not copied into this package. Obtain the exact hash-bound candidate from the Drive pointer in REPORT.md. No external requests, connected auth or live service tests are needed.

Files:

- REPORT.md: required six-part technical return and disposition table.
- route-control-inventory.csv: 201 exact navigation/surface-state source records.
- control-ledger.json / handler-ledger.json: all 638 native-control occurrences / 414 listener declarations, with scope, supersession and association limits.
- functions.json / bindings.json / definition-chains.json: exact extracted implementations, assignments and alias chains. Replaced definitions are not assumed active.
- fixture-data.json: exact course/question/class/note fixture data used in isolated checks.
- registry.json / routes.json / stateWrites.json / visual-seams.json: component metadata and source routing/state/style evidence.
- isolated-results.json: 12 detector scenarios; explicit isolated JavaScript evidence, not browser acceptance.
- manifest.json / input-provenance.json / package-manifest.json: frozen input and package identities.
- extract_source.cjs / source_inspection.cjs / build_inventory.py / isolate_behaviour.cjs: reproducible audit tooling. No product code modifications.

Reproduction in the supplied execution environment:

```sh
node extract_source.cjs /absolute/path/to/StudyGrid-CF0042-QB17R2-stuart-defect-repair.html /absolute/path/to/audit-output
node source_inspection.cjs /absolute/path/to/StudyGrid-CF0042-QB17R2-stuart-defect-repair.html
python build_inventory.py
node isolate_behaviour.cjs /absolute/path/to/StudyGrid-CF0042-QB17R2-stuart-defect-repair.html
```

The extractor and source inspector use the already-installed Playwright Babel parser at the absolute dependency path encoded in each script. **They do not launch a browser.** The other scripts operate on the extracted JSON beside them. Selected dependencies, DOM/storage/time and browser-history events are stubbed in the isolation harness. Real geometry, native input, focus heuristics and provider/browser storage failures need separate browser/device reproduction.

PASS in isolated-results.json means the observation asserted by that detector was produced. Several detectors deliberately confirm defects.
