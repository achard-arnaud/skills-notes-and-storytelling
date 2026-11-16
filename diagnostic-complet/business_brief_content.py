"""Validate an evidence-led business brief before any rendering hand-off."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from analysis import _shape


SCHEMA = json.loads(
    (Path(__file__).parent / "schemas/business-brief-content.v1.schema.json")
    .read_text(encoding="utf-8")
)


def _result(structural_errors, semantic_errors, content_revision=None):
    errors = structural_errors + semantic_errors
    return {
        "valid": not errors,
        "errors": errors,
        "structural_errors": structural_errors,
        "semantic_errors": semantic_errors,
        "content_revision": content_revision,
        "handoff_ready": not errors,
        "human_approval": False,
    }


def _semantic_errors(content):
    errors = []
    claims = content["claims"]
    recommendations = content["recommendations"]

    claim_ids = [claim["id"] for claim in claims]
    recommendation_ids = [item["id"] for item in recommendations]
    all_ids = claim_ids + recommendation_ids
    if len(all_ids) != len(set(all_ids)):
        errors.append("identifiers: claim and recommendation ids must be unique")

    for claim in claims:
        source_kind = claim["source"]["kind"]
        if claim["status"] == "verified_fact" and source_kind in {
            "primary_vendor", "primary_corporate"
        }:
            errors.append(
                f'claim {claim["id"]}: supplier or corporate source cannot become verified_fact'
            )
        if claim["contradiction"] == "present" and not claim["contradiction_detail"].strip():
            errors.append(f'claim {claim["id"]}: present contradiction requires detail')
        if claim["contradiction"] == "unknown" and not claim["unknowns"]:
            errors.append(f'claim {claim["id"]}: unknown contradiction requires an explicit unknown')

    if content["decision_requested"] and not recommendations:
        errors.append("decision brief: at least one explicit option is required")
    if not content["decision_requested"] and recommendations:
        errors.append("descriptive brief: recommendations must remain empty")

    for item in recommendations:
        owner = item["owner"]
        if owner["status"] == "assigned" and not owner.get("assignee"):
            errors.append(f'recommendation {item["id"]}: assigned owner requires an assignee')
        if owner["status"] == "unassigned" and owner.get("assignee"):
            errors.append(f'recommendation {item["id"]}: unassigned owner cannot name an assignee')
    return errors


def validate_business_brief_content(content):
    """Return a deterministic pre-render verdict without mutating the content.

    This validates AC1–AC3 only. It does not render, approve, research, or prove
    that a cited source semantically supports a claim.
    """
    structural = _shape(content, SCHEMA, root=SCHEMA)
    if structural:
        return _result(structural, [])
    semantic = _semantic_errors(content)
    revision = hashlib.sha256(
        json.dumps(content, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        .encode("utf-8")
    ).hexdigest()
    return _result([], semantic, revision)
