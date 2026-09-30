from pathlib import Path
import hashlib
import tempfile
from dataclasses import dataclass

from tools.v4a_ac_receipt_paths import verify_hash_receipts


@dataclass
class Check:
    status: str
    key: str
    detail: str


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run_case(setup, expect_fail_key=None, expect_pass_count=None):
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        setup(root)
        files = [p for p in root.rglob("*") if p.is_file()]
        checks = verify_hash_receipts(files, root, Check)
        fails = [c for c in checks if c.status == "FAIL"]
        passes = [c for c in checks if c.status == "PASS"]
        if expect_fail_key:
            assert any(c.key == expect_fail_key for c in fails), checks
        else:
            assert not fails, checks
        if expect_pass_count is not None:
            assert len(passes) == expect_pass_count, checks


def good_flat(root):
    data = b"abc"
    (root / "foo.txt").write_bytes(data)
    (root / "artifact_sha256.txt").write_text(f"{digest(data)}  output-v4a-hidden/foo.txt\n")


def exact_prefixed(root):
    data = b"abc"
    (root / "output-v4a-hidden").mkdir()
    (root / "output-v4a-hidden/foo.txt").write_bytes(data)
    (root / "artifact_sha256.txt").write_text(f"{digest(data)}  output-v4a-hidden/foo.txt\n")


def duplicate_normalized(root):
    data = b"abc"
    (root / "foo.txt").write_bytes(data)
    (root / "artifact_sha256.txt").write_text(
        f"{digest(data)}  output-v4a-hidden/foo.txt\n{digest(data)}  foo.txt\n"
    )


def traversal(root):
    (root / "artifact_sha256.txt").write_text(f"{'0' * 64}  ../foo.txt\n")


def unknown_prefix(root):
    data = b"abc"
    (root / "foo.txt").write_bytes(data)
    (root / "artifact_sha256.txt").write_text(f"{digest(data)}  other-prefix/foo.txt\n")


def mismatch(root):
    (root / "foo.txt").write_bytes(b"abc")
    (root / "artifact_sha256.txt").write_text(f"{'0' * 64}  output-v4a-hidden/foo.txt\n")


def missing(root):
    (root / "artifact_sha256.txt").write_text(f"{'0' * 64}  output-v4a-hidden/foo.txt\n")


def test_known_prefix_flattened_root():
    run_case(good_flat, expect_pass_count=1)


def test_exact_prefixed_root():
    run_case(exact_prefixed, expect_pass_count=1)


def test_duplicate_normalized_path_rejected():
    run_case(duplicate_normalized, expect_fail_key="hash_receipt_duplicate_normalized_path")


def test_traversal_rejected():
    run_case(traversal, expect_fail_key="hash_receipt_unsafe_path")


def test_unknown_prefix_not_stripped():
    run_case(unknown_prefix, expect_fail_key="hash_receipt_target")


def test_hash_mismatch_rejected():
    run_case(mismatch, expect_fail_key="hash_receipt_mismatch")


def test_missing_target_rejected():
    run_case(missing, expect_fail_key="hash_receipt_target")
