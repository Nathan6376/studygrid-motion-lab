"""Implementation-independent Q-S11 Slice 2 acceptance oracles.

PREP ONLY: this module does not import, inspect, or mutate StudyGrid runtime code.
Q-S11 supplies normalized observations collected from exact provider candidate bytes.
"""
from __future__ import annotations

import hashlib
import re
from typing import Any, Mapping, Sequence


class OracleFailure(AssertionError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise OracleFailure(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_exact_identity(data: bytes, *, sha256: str, byte_count: int) -> None:
    require(len(data) == byte_count, f"byte mismatch: {len(data)} != {byte_count}")
    require(sha256_bytes(data) == sha256, "SHA-256 mismatch")


def verify_version_triplet(text: str, expected: str) -> None:
    for token in ("APP_VERSION", "SG_R6_BUILD"):
        require(expected in text, f"{token} does not bind expected version")
    require(expected in text and "component" in text.lower() and "registry" in text.lower(),
            "registry build does not bind expected version")


def candidate_added_text(baseline: str, candidate: str) -> str:
    """Conservative changed-text helper; exact derivation still requires a byte-level diff at Q-S11."""
    base_lines = set(baseline.splitlines())
    return "\n".join(line for line in candidate.splitlines() if line not in base_lines)


def verify_scope_boundaries(added_text: str) -> None:
    low = added_text.lower()
    forbidden = (
        "fetch(", "xmlhttprequest", "websocket(", "createclient(", "supabase",
        "professor setup", "autofill", "human timing", "enrolment", "enrollment",
        "blender", ".glb", "gltf", "three.js", "canonical promotion", "deploy",
    )
    for term in forbidden:
        require(term not in low, f"out-of-scope surface detected: {term}")
    require(not re.search(r"https?://", added_text, flags=re.I), "new network/provider URL detected")


def verify_gateway_contract(text: str) -> None:
    for token in (
        "StudyGridProductGateway", "source_revision_id", "source_block_id",
        "display_locator", "stale_revision", "unauthorized",
    ):
        require(token in text, f"accepted Slice 1 gateway contract token missing: {token}")


def verify_registry(registry: Mapping[str, Any], baseline_ids: set[str] | None = None) -> None:
    rev = int(registry.get("revision", registry.get("rev", -1)))
    require(rev >= 11, f"registry revision regressed: {rev}")
    entries = registry.get("components", registry.get("entries", []))
    require(isinstance(entries, Sequence), "registry entries missing")
    ids = []
    for row in entries:
        require(isinstance(row, Mapping), "registry entry is not an object")
        cid = row.get("component_id", row.get("id"))
        require(bool(cid), "registry component id missing")
        ids.append(str(cid))
    require(len(ids) == len(set(ids)), "registry IDs are not unique")
    if baseline_ids is not None:
        require(baseline_ids.issubset(set(ids)), "accepted Slice 1 registry IDs were removed")


def verify_scale(courses: Sequence[Mapping[str, Any]]) -> None:
    require(5 <= len(courses) <= 7, f"expected approximately six courses, got {len(courses)}")
    total = sum(int(c.get("student_count", 0)) for c in courses)
    require(total >= 200, f"expected hundreds of students, got {total}")
    require(all(int(c.get("student_count", 0)) > 0 for c in courses), "course with zero/unknown student count")


def verify_explicit_class_identity(courses: Sequence[Mapping[str, Any]]) -> None:
    ids: set[str] = set()
    visible_keys: set[tuple[str, str, str]] = set()
    for c in courses:
        cid = str(c.get("id", "")).strip()
        require(cid and cid not in ids, f"missing/duplicate course id: {cid!r}")
        ids.add(cid)
        key = tuple(str(c.get(k, "")).strip() for k in ("name", "code", "section"))
        require(all(key), f"course {cid} missing name/code/section")
        require(key not in visible_keys, f"ambiguous visible class identity: {key}")
        visible_keys.add(key)
        require("student_count" in c, f"course {cid} missing student count context")
        require("open_question_count" in c, f"course {cid} missing open-question context")


def verify_colour_not_sole_identifier(courses: Sequence[Mapping[str, Any]]) -> None:
    verify_explicit_class_identity(courses)
    # Duplicate colour/label values are explicitly valid; visible name/code/section must still disambiguate.
    visible = [(c.get("name"), c.get("code"), c.get("section")) for c in courses]
    require(len(visible) == len(set(visible)), "class identity depends on colour/label")


def verify_today(today: Sequence[Mapping[str, Any]]) -> None:
    for item in today:
        require(item.get("confirmed") is True, f"unconfirmed Today item: {item.get('id')}")
        require(bool(str(item.get("course_id", "")).strip()), "Today item missing course identity")
        require(bool(str(item.get("starts_at", "")).strip()), "Today item missing scheduled time")


def verify_no_auto_navigation(before: Mapping[str, Any], after: Mapping[str, Any]) -> None:
    for key in ("location_hash", "selected_class_id", "workspace_view"):
        require(before.get(key) == after.get(key), f"Professor Home stole context via {key}")


def verify_attention_live(items: Sequence[Mapping[str, Any]]) -> None:
    ids: set[str] = set()
    for item in items:
        iid = str(item.get("id", "")).strip()
        require(iid and iid not in ids, f"missing/duplicate attention id: {iid!r}")
        ids.add(iid)
        require(item.get("actionable") is True, f"non-actionable live attention: {iid}")
        require(item.get("resolved") is False, f"resolved item remains live: {iid}")
        require(bool(str(item.get("reason", "")).strip()), f"attention item lacks reason: {iid}")


def verify_attention_resolution(before_live: Sequence[Mapping[str, Any]], after_live: Sequence[Mapping[str, Any]],
                                history: Sequence[Mapping[str, Any]], resolved_id: str) -> None:
    before = {str(x.get("id")) for x in before_live}
    after = {str(x.get("id")) for x in after_live}
    require(resolved_id in before, "resolved item was not initially live")
    require(resolved_id not in after, "resolved item remains in live attention")
    matches = [x for x in history if str(x.get("id")) == resolved_id]
    require(matches, "resolved item vanished from history/audit state")
    require(any(x.get("resolved") is True or str(x.get("status", "")).lower() == "resolved" for x in matches),
            "history does not record resolution")


def verify_all_resolved(live: Sequence[Mapping[str, Any]], history: Sequence[Mapping[str, Any]]) -> None:
    require(len(live) == 0, "all-resolved state still has live attention")
    require(len(history) > 0, "all-resolved state erased history")


def verify_transparent_organization(before: Sequence[Mapping[str, Any]], after: Sequence[Mapping[str, Any]]) -> None:
    require({str(x.get("id")) for x in before} == {str(x.get("id")) for x in after},
            "organization control hid or invented courses")
    for c in after:
        for forbidden in ("risk_score", "priority_score", "readiness_score", "rank_score"):
            require(forbidden not in c, f"opaque ranking field introduced: {forbidden}")
        for key in ("pinned", "favourite", "colour", "label"):
            if key in c:
                require(isinstance(c[key], (bool, str, type(None))), f"opaque organization value: {key}")


def verify_sort(courses: Sequence[Mapping[str, Any]], sort_key: str) -> None:
    require(sort_key in ("name", "code"), f"unsupported transparent sort: {sort_key}")
    actual = [str(c.get(sort_key, "")).casefold() for c in courses]
    require(actual == sorted(actual), f"{sort_key} sort is not deterministic")


def verify_selected_class_drill(after: Mapping[str, Any], target_course_id: str) -> None:
    require(after.get("selected_class_id") == target_course_id, "drill-in selected the wrong class")
    tabs = set(str(x) for x in after.get("workspace_tabs", []))
    expected = {"Overview", "Assessments", "Questions", "Students", "Sources"}
    require(expected.issubset(tabs), f"selected-class workspace tabs missing: {expected - tabs}")
    require(after.get("professor_home_replaced_workspace") is not True,
            "Professor Home replaced accepted selected-class workspace")


def verify_shared_assessment_revision(by_view: Mapping[str, Any]) -> None:
    keys = ("assessment_desk", "instructor_summary", "student_timeline", "delivery_plan")
    vals = [str(by_view.get(k, "")).strip() for k in keys]
    require(all(vals), "shared assessment revision missing from a view")
    require(len(set(vals)) == 1, f"assessment revision diverged across views: {vals}")


def verify_source_identity(sources: Sequence[Mapping[str, Any]]) -> None:
    require(bool(sources), "source inventory is empty")
    for src in sources:
        for key in ("section_id", "source_revision_id", "source_block_id", "display_locator"):
            require(bool(str(src.get(key, "")).strip()), f"source missing {key}")


def verify_stale_no_mutation(before: Mapping[str, Any], result: Mapping[str, Any], after: Mapping[str, Any]) -> None:
    require(result.get("ok") is False, "stale command unexpectedly succeeded")
    require(result.get("state") == "stale_revision", "stale command state mismatch")
    require((result.get("error") or {}).get("code") == "STALE_REVISION", "stale command code mismatch")
    require(before == after, "stale command mutated authoritative state")


def verify_unauthorized_no_mutation(before: Mapping[str, Any], result: Mapping[str, Any], after: Mapping[str, Any]) -> None:
    require(result.get("ok") is False, "unauthorized command unexpectedly succeeded")
    require(result.get("state") == "unauthorized", "unauthorized state mismatch")
    require((result.get("error") or {}).get("code") == "UNAUTHORIZED", "unauthorized code mismatch")
    require(before == after, "unauthorized command mutated authoritative state")


def verify_deterministic_states(first: Mapping[str, Any], second: Mapping[str, Any]) -> None:
    for state in ("ready", "loading", "empty", "error", "stale_revision", "unauthorized"):
        require(first.get(state) == second.get(state), f"state is not deterministic: {state}")


def verify_focus(expected_id: str, actual_id: str) -> None:
    require(actual_id == expected_id, f"focus mismatch: {actual_id!r} != {expected_id!r}")


def verify_responsive(obs: Mapping[str, Any]) -> None:
    require(int(obs.get("duplicate_ids", 0)) == 0, "duplicate live DOM IDs")
    require(int(obs.get("horizontal_overflow_px", 0)) <= 0, "page-level horizontal overflow")
    require(obs.get("professor_home_visible") is True, "Professor Home not visible")
    require(obs.get("class_library_visible") is True, "class library not visible")


def verify_home_bounded_summary(home: Mapping[str, Any]) -> None:
    require(home.get("full_roster_rows_rendered") in (0, None), "Professor Home rendered full rosters")
    require(home.get("organization_controls_visible") is True, "Professor Home lacks bounded organization controls")


GATE_IDS = (
    "ID-01","ID-02","ID-03","HOME-01","HOME-02","HOME-03","HOME-04",
    "ATTN-01","ATTN-02","ATTN-03","ATTN-04","CLASS-01","CLASS-02","CLASS-03",
    "ORG-01","ORG-02","ORG-03","ORG-04","DRILL-01","DRILL-02","DRILL-03",
    "GW-01","GW-02","GW-03","GW-04","GW-05","GW-06",
    "REG-01","REG-02","REG-03","REG-04","REG-05","REG-06","REG-07",
    "RESP-01","RESP-02","EDGE-01","EDGE-02","EDGE-03","EDGE-04",
    "SCOPE-01","SCOPE-02","SCOPE-03","SCOPE-04","SCOPE-05","HOLD-01",
)


def verify_gate_catalogue() -> None:
    require(len(GATE_IDS) == 46, f"gate count drift: {len(GATE_IDS)}")
    require(len(set(GATE_IDS)) == len(GATE_IDS), "duplicate gate IDs")
    require("HOLD-01" in GATE_IDS, "physical/hosted/accessibility HOLD gate missing")
