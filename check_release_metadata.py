#!/usr/bin/env python3
"""Check v4 release metadata, assurance scope, core digests and anonymity."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
RELEASE_ID = "txgraffiti-c3-resolution/4.0.0-rc1"
V2_THEOREM = "106787526e7d356d7c0535ab01c43aa7d6a1223a95fe728bba76e287aadea589"
V3_REVIEWED = "94fe632a280d0ca8d6d06ec3cf2309d07973acdac0c43c53e21c3d4191903e8f"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_json(name: str) -> dict:
    return json.loads((BASE / name).read_text(encoding="utf-8"))


def main() -> int:
    result = load_json("RESULT.json")
    assurance = load_json("ASSURANCE.json")
    claims = load_json("CLAIMS.json")
    dependencies = load_json("EXTERNAL_DEPENDENCIES.json")

    if result.get("schema") != "evidence-press/mathematical-resolution/v4":
        raise AssertionError("RESULT.json does not declare the v4 schema")
    for document in (result, assurance, claims, dependencies):
        if document.get("release_id") != RELEASE_ID:
            raise AssertionError("release identifier mismatch")

    for filename, expected in result["core_artifact_hashes"].items():
        actual = sha256(BASE / filename)
        if actual != expected:
            raise AssertionError(f"{filename} digest mismatch: {actual} != {expected}")

    required = {
        "AI_INDEX.md", "STATUS.md", "ASSURANCE.md", "ASSURANCE.json",
        "PROVENANCE.md", "SOURCES.md", "CLAIMS.json", "LICENSE.md",
        "DOCUMENT_MAP.md", "PRIOR_ART_COMPARISON.md", "THEOREM_DEPENDENCY.md",
        "EXTERNAL_DEPENDENCIES.json", "ENVIRONMENT.md", "EVIDENCE_SUPPLEMENT.md",
        "MANUSCRIPT.md", "REVIEW_RESPONSE.md", "EXTERNAL_REVIEW_2026-08-06.md",
        "environment/Containerfile", "environment/requirements-milp.lock",
        "run_core_verification.sh", "run_optional_audits.sh"
    }
    missing = sorted(path for path in required if not (BASE / path).is_file())
    if missing:
        raise AssertionError(f"missing canonical interface files: {missing}")

    if assurance["status"] != "unrefereed-candidate":
        raise AssertionError("incorrect assurance status")
    false_fields = ("peerReviewed", "independentlyRerun", "independentlyReimplemented", "formallyVerified")
    if any(assurance[field] is not False for field in false_fields):
        raise AssertionError("assurance overclaim detected")
    if assurance["predecessorIndependentAnalysis"]["archive_sha256"] != V2_THEOREM:
        raise AssertionError("Fable predecessor hash mismatch")
    if assurance["predecessorTechnicalReview"]["archive_sha256"] != V3_REVIEWED:
        raise AssertionError("reviewed v3 hash mismatch")

    history = (BASE / "VERSION_HISTORY.md").read_text(encoding="utf-8")
    fable = (BASE / "INDEPENDENT_REPLAY_FABLE.md").read_text(encoding="utf-8")
    review_response = (BASE / "REVIEW_RESPONSE.md").read_text(encoding="utf-8")
    for digest in (V2_THEOREM, V3_REVIEWED):
        if digest not in history or digest not in review_response:
            raise AssertionError(f"lineage hash not consistently recorded: {digest}")
    if V2_THEOREM not in fable:
        raise AssertionError("Fable receipt scope banner missing")

    dependency_ids = {item["id"] for item in dependencies["dependencies"]}
    if "ZPS-2024-20-CLAUSE" not in dependency_ids:
        raise AssertionError("external theorem dependency missing")
    c9 = next(item for item in claims["claims"] if item["id"] == "C9")
    if c9["external_dependency"] != "ZPS-2024-20-CLAUSE":
        raise AssertionError("claim C9 dependency not mapped")

    canonical_text = "\n".join(
        (BASE / name).read_text(encoding="utf-8")
        for name in ("README.md", "STATUS.md", "ASSURANCE.md", "MANUSCRIPT.md", "EVIDENCE_SUPPLEMENT.md")
    )
    forbidden_phrases = (
        "exact v4 has been independently",
        "formally verified release",
        "peer-reviewed release",
        "globally minimal counterexample"
    )
    for phrase in forbidden_phrases:
        if phrase.lower() in canonical_text.lower():
            raise AssertionError(f"forbidden assurance phrase present: {phrase}")

    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    personal_markers = ("Ian" + " Pitchford",)
    binary_suffixes = {".pdf", ".zip", ".gz", ".g6", ".png"}
    for path in BASE.rglob("*"):
        if not path.is_file() or path.suffix.lower() in binary_suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if email_pattern.search(text):
            raise AssertionError(f"email address found in {path.relative_to(BASE)}")
        if any(marker in text for marker in personal_markers):
            raise AssertionError(f"personal identifier found in {path.relative_to(BASE)}")

    print("RELEASE_METADATA_PASSED schema=v4 assurance_scope=exact anonymity_scan=pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
