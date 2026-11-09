#!/usr/bin/env python3
"""Bounded writing bootstraps and revision conservation; no factual generation."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from collections import deque
from pathlib import Path


EVIDENCE_KEYS = ("id", "title", "mandate", "pillars", "sources", "fragments", "claims", "relations")
FORBIDDEN_INPUT_KEYS = {"sections", "side_stories", "reader_prose", "manuscript", "canonical_text", "writing_ledger"}
PROSE_SOURCE_KINDS = {"reader_prose", "prior_reader", "canonical_manuscript", "reader_export"}


def text_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def study_hash(study):
    """Immutable baseline identity independent of a filename or JSON key order."""
    return text_hash(json.dumps(study, sort_keys=True, ensure_ascii=False, separators=(",", ":")))


def baseline_receipt(study):
    reviews = [{"id": p["id"], "review": p.get("review", {})}
               for s in study.get("sections", []) for p in s.get("paragraphs", [])]
    return {
        "study_id": study.get("id"), "declared_version": study.get("version"),
        "content_sha256": study_hash(study),
        "version_basis": "declared_version_and_content_hash" if study.get("version") else "content_hash; declared version unknown",
        "approval_state": copy.deepcopy(study.get("approval_state", study.get("approval", {"human": "not_recorded"}))),
        "paragraph_reviews_sha256": study_hash(reviews),
        "factual_reviewed_paragraphs": sum(r["review"].get("evidence") is True for r in reviews),
        "editorial_reviewed_paragraphs": sum(r["review"].get("editorial") is True for r in reviews),
    }


def _index(study):
    indexed = {}
    for kind in ("pillars", "sources", "fragments", "claims", "relations", "sections", "side_stories"):
        for record in study.get(kind, []):
            ident = record["id"]
            if ident in indexed:
                raise ValueError(f"duplicate ID: {ident}")
            indexed[ident] = (kind, record)
            if kind == "sections":
                for paragraph in record.get("paragraphs", []):
                    if paragraph["id"] in indexed:
                        raise ValueError(f"duplicate ID: {paragraph['id']}")
                    indexed[paragraph["id"]] = ("paragraphs", paragraph)
    return indexed


def prepare_from_scratch(evidence, reader_scaffold=None):
    """Accept evidence-only input and topology, rejecting all prior reader prose.

    The allowlist is deliberately narrower than a complete study. Rejecting prose
    containers makes a successful preparation independent of a previous draft.
    Reader headings may be reused explicitly; paragraphs and side-story prose may not.
    """
    if FORBIDDEN_INPUT_KEYS.intersection(evidence):
        raise ValueError("from-scratch requires evidence-only input; prior prose containers forbidden")
    unknown = set(evidence) - set(EVIDENCE_KEYS)
    if unknown:
        raise ValueError(f"unexpected evidence fields: {sorted(unknown)}")
    for source in evidence.get("sources", []):
        if source.get("kind") in PROSE_SOURCE_KINDS:
            raise ValueError("from-scratch cannot load a prior reader as an evidence source")
    # Only the explicitly allowed evidence fields are accessed/copied.
    result = {key: copy.deepcopy(evidence[key]) for key in EVIDENCE_KEYS if key in evidence}
    result.setdefault("relations", [])
    result.setdefault("pillars", [])
    result.setdefault("sources", [])
    result.setdefault("fragments", [])
    result.setdefault("claims", [])
    claim_ids = {record["id"] for record in result["claims"]}
    pillar_ids = {record["id"] for record in result["pillars"]}
    if reader_scaffold is None:
        topology = [{"id": "S-001", "title": result.get("mandate", {}).get("question", "Question à cadrer"),
                     "claim_ids": [c["id"] for c in result["claims"]], "pillar_ids": []}]
    else:
        topology = reader_scaffold.get("sections", [])
        if set(reader_scaffold) - {"sections", "id", "version", "approval"}:
            raise ValueError("reader scaffold must contain topology only")
        for section in topology:
            if set(section) - {"id", "title", "claim_ids", "pillar_ids"}:
                raise ValueError("reader scaffold contains prose or unsupported fields")
    result["sections"] = []
    for section in topology:
        if not set(section.get("claim_ids", [])).issubset(claim_ids):
            raise ValueError("scaffold contains unknown claim IDs")
        if not set(section.get("pillar_ids", [])).issubset(pillar_ids):
            raise ValueError("scaffold contains unknown pillar IDs")
        row = copy.deepcopy(section)
        row["paragraphs"] = []
        result["sections"].append(row)
    result["side_stories"] = []
    _index(result)
    packet = {
        "mode": "from-scratch", "reader_prose_loaded": False,
        "input_contract": "evidence-only + explicit prose-free reader topology",
        "evidence_ids": [c["id"] for c in result["claims"]],
        "section_ids": [s["id"] for s in result["sections"]],
        "writing_order": ["core_draft", "independent_core_review", "core_freeze", "side_story_qualification", "placement", "continuity_review"],
        "state": "scaffold_candidate_not_drafted", "human_approval": False,
        "limitations": ["Source semantic mislabelling is not mechanically detectable.", "No prose or facts generated by this preparation."],
    }
    return {"study": result, "packet": packet, "ledger": []}


def plan_iterative(study, changed_ids, form_global=False):
    """Resolve evidence dependency closure and a bounded editorial scope.

    depends_on points from dependent to dependency; supports/contextualizes and
    causal_hypothesis point from the supporting proposition toward its target.
    Symmetric comparisons and contradictions are conservatively reviewed both ways.
    Derived section membership alone never expands to unrelated peer paragraphs.
    """
    indexed = _index(study)
    changed = set(changed_ids)
    missing = changed - set(indexed)
    if missing:
        raise ValueError(f"unknown changed IDs: {sorted(missing)}")
    dependents = {key: set() for key in indexed}

    def edge(source, target):
        if source not in indexed or target not in indexed:
            raise ValueError(f"unresolved dependency: {source} -> {target}")
        dependents[source].add(target)

    for fragment in study.get("fragments", []):
        edge(fragment["source_id"], fragment["id"])
    for claim in study.get("claims", []):
        for fragment in claim.get("fragment_ids", []):
            edge(fragment, claim["id"])
        for pillar in claim.get("pillar_ids", []):
            edge(pillar, claim["id"])
    for relation in study.get("relations", []):
        left, right = relation["from"], relation["to"]
        if left not in indexed or right not in indexed:
            raise ValueError("unresolved relation endpoint")
        kind = relation["kind"]
        if kind == "depends_on":
            edge(right, left)
        elif kind in {"supports", "illustrates", "contextualizes", "causal_hypothesis"}:
            edge(left, right)
        elif kind in {"contradicts", "compares"}:
            edge(left, right)
            edge(right, left)
        else:
            raise ValueError(f"unsupported relation kind: {kind}")
        edge(relation["id"], left)
        edge(relation["id"], right)
    closure = set(changed)
    queue = deque(sorted(changed))
    while queue:
        for target in sorted(dependents[queue.popleft()]):
            if target not in closure:
                closure.add(target)
                queue.append(target)
    affected_claims = {ident for ident in closure if indexed[ident][0] == "claims"}
    explicit_sections = {ident for ident in changed if indexed[ident][0] == "sections"}
    paragraph_ids, section_ids, evidence_invalidated = set(), set(), set()
    for section in study.get("sections", []):
        section_hit = bool(set(section.get("claim_ids", [])) & affected_claims)
        for paragraph in section.get("paragraphs", []):
            evidence_hit = bool(set(paragraph.get("claim_ids", [])) & affected_claims)
            if evidence_hit:
                evidence_invalidated.add(paragraph["id"])
            if evidence_hit or paragraph["id"] in changed or section["id"] in explicit_sections:
                paragraph_ids.add(paragraph["id"])
                section_hit = True
        if section_hit or section["id"] in explicit_sections:
            section_ids.add(section["id"])
    if form_global:
        paragraph_ids.update(p["id"] for s in study.get("sections", []) if s["id"] in section_ids for p in s.get("paragraphs", []))
    side_ids = set()
    for story in study.get("side_stories", []):
        if (story["id"] in changed or set(story.get("claim_ids", [])) & affected_claims
                or story.get("return_to") in paragraph_ids
                or story.get("parent_section_id") in explicit_sections
                or (form_global and story.get("parent_section_id") in section_ids)):
            side_ids.add(story["id"])
    return {
        "mode": "iterative", "changed_ids": sorted(changed), "dependency_closure": sorted(closure),
        "claim_ids": sorted(affected_claims), "section_ids": sorted(section_ids),
        "paragraph_ids": sorted(paragraph_ids), "side_story_ids": sorted(side_ids),
        "evidence_invalidated_paragraph_ids": sorted(evidence_invalidated),
        "form_global": bool(form_global), "human_approval": False,
        "baseline": baseline_receipt(study),
    }


def apply_iterative(study, changed_ids, replacements=None, form_global=False, *, expected_baseline_hash):
    """Apply externally supplied prose only within the dependency-derived scope.

    Facts, sources, claim statuses and IDs remain unchanged. Every changed paragraph
    loses both review approvals. A form-global review invalidates editorial approval
    across its selected sections but preserves unaffected evidentiary approval.
    """
    if not isinstance(expected_baseline_hash, str) or expected_baseline_hash != study_hash(study):
        raise ValueError("baseline content hash mismatch; reread and replan before applying prose")
    replacements = replacements or {}
    plan = plan_iterative(study, changed_ids, form_global=form_global)
    writable = set(plan["paragraph_ids"]) | set(plan["side_story_ids"])
    if not set(replacements).issubset(writable):
        raise ValueError("replacement outside selected dependency closure")
    if any(not isinstance(text, str) or not text.strip() for text in replacements.values()):
        raise ValueError("replacement prose must be nonempty text")
    result = copy.deepcopy(study)
    indexed = _index(result)
    entries = []
    for ident in sorted(writable):
        kind, record = indexed[ident]
        before = record.get("text", "")
        after = replacements.get(ident, before)
        previous_review = copy.deepcopy(record.get("review", {}))
        review = copy.deepcopy(previous_review)
        reasons = []
        if after != before:
            record["text"] = after
            review = {"evidence": False, "editorial": False, "text_sha256": text_hash(after)}
            reasons.append("prose_changed")
            if kind == "side_stories":
                record["state"] = "candidate"
        else:
            expected_hash = previous_review.get("text_sha256") or previous_review.get("paragraph_sha256")
            if expected_hash and expected_hash != text_hash(before):
                review = {"evidence": False, "editorial": False, "text_sha256": text_hash(before)}
                reasons.append("stale_text_review")
            elif not expected_hash and (review.get("evidence") or review.get("editorial")):
                review = {"evidence": False, "editorial": False, "text_sha256": text_hash(before)}
                reasons.append("missing_text_review_hash")
            if ident in plan["evidence_invalidated_paragraph_ids"] or (kind == "side_stories" and set(record.get("claim_ids", [])) & set(plan["claim_ids"])):
                review["evidence"] = False
                reasons.append("evidence_dependency_changed")
                if kind == "side_stories":
                    record["state"] = "candidate"
            if form_global:
                review["editorial"] = False
                reasons.append("form_global_scope_review")
            if kind == "side_stories" and record.get("return_to") in plan["paragraph_ids"]:
                review["editorial"] = False
                record["state"] = "candidate"
                reasons.append("placement_dependency_changed")
        if review != previous_review:
            record["review"] = review
        if reasons:
            entries.append({
                "sequence": len(study.get("writing_ledger", [])) + len(entries) + 1,
                "id": ident, "kind": kind, "before_sha256": text_hash(before), "after_sha256": text_hash(after),
                "reasons": reasons, "previous_review": previous_review,
                "result_review": copy.deepcopy(record.get("review", {})), "human_approval": False,
            })
    result["writing_ledger"] = copy.deepcopy(study.get("writing_ledger", [])) + entries
    return {"study": result, "plan": plan, "ledger": entries}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    fresh = sub.add_parser("from-scratch")
    fresh.add_argument("evidence", type=Path)
    fresh.add_argument("output", type=Path)
    fresh.add_argument("--scaffold", type=Path)
    iterative = sub.add_parser("iterative")
    iterative.add_argument("study", type=Path)
    iterative.add_argument("output", type=Path)
    iterative.add_argument("--changed", nargs="+", required=True)
    iterative.add_argument("--replacements", type=Path)
    iterative.add_argument("--form-global", action="store_true")
    iterative.add_argument("--expected-baseline-hash", required=True)
    args = parser.parse_args()
    load = lambda path: json.loads(path.read_text(encoding="utf-8"))
    if args.command == "from-scratch":
        result = prepare_from_scratch(load(args.evidence), load(args.scaffold) if args.scaffold else None)
    else:
        result = apply_iterative(load(args.study), args.changed, load(args.replacements) if args.replacements else {}, args.form_global,
                                 expected_baseline_hash=args.expected_baseline_hash)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Writing workflow receipt: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
