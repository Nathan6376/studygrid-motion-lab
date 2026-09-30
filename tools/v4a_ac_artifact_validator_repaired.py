#!/usr/bin/env python3
"""Q-S4 repaired entrypoint for the frozen V4A A/C artifact validator.

This preserves the original frozen acceptance logic and replaces only its SHA-256
receipt target resolver with the strict path-normalization module added by Q-S4.
The historical validator file and prior Q-S1 raw result are intentionally left
unchanged.
"""
from __future__ import annotations

import v4a_ac_artifact_validator as base
import v4a_ac_receipt_paths as receipt_paths


def _patched_verify_hash_receipts(files, root):
    return receipt_paths.verify_hash_receipts(files, root, base.Check)


base.verify_hash_receipts = _patched_verify_hash_receipts
validate = base.validate
main = base.main


if __name__ == "__main__":
    raise SystemExit(main())
