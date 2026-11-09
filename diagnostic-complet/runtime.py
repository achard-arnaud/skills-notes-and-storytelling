#!/usr/bin/env python3
"""Local evidence import and structural validation; no epistemic promotion."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sidestories  # noqa: E402

TERMINOLOGY = json.loads((Path(__file__).resolve().parent / "ontology" / "terminology.json").read_text(encoding="utf-8"))
STATUSES = set(TERMINOLOGY["claim_statuses"])
RELATIONS = {"supports", "contradicts", "depends_on", "illustrates", "compares", "contextualizes", "causal_hypothesis"}
# Derived from workflows/side-stories.workflow.json (single source of truth, D22). Legacy kinds stay
# accepted for existing studies and only produce a gap naming their canonical replacement.
SIDE_KINDS = set(sidestories.CANONICAL_KINDS) | set(sidestories.LEGACY_MAP)
STATES = {"candidate", "validated", "promoted", "retired"}
SOURCE_TIERS = TERMINOLOGY["source_tiers"]
LEGACY_KIND_TO_TIER = TERMINOLOGY["legacy_source_kind_to_tier"]


def source_tier(source: dict) -> str:
    """Explicit `tier` first, then the legacy `kind` mapping; anything else is `unassessed` (safe default)."""
    tier = source.get("tier") if "tier" in source else LEGACY_KIND_TO_TIER.get(source.get("kind"), "unassessed")
    return tier if tier in SOURCE_TIERS else "unassessed"


def verified_eligible(source: dict) -> bool:
    return bool(SOURCE_TIERS[source_tier(source)]["verified_fact_eligible"])
CONSULTED = {"read", "consulted", "full", "full_text"}


def text_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def import_markdown(path, study_id):
    """Preserve source bytes/hash and exact line slices; import all assertions as supplied."""
    path = Path(path)
    raw = path.read_bytes()
    original = raw.decode("utf-8")
    lines = original.splitlines(keepends=True)
    digest = hashlib.sha256(raw).hexdigest()
    sid = "SRC-" + digest[:16]
    study = {
        "id": study_id,
        "mandate": {"question": "À cadrer", "scope": "Import fourni, qualification à effectuer", "audience": "À préciser"},
        "pillars": [],
        "sources": [{"id": sid, "kind": "supplied_context", "access": "read", "title": path.name,
                     "locator": path.name, "sha256": digest, "size_bytes": len(raw), "text": original}],
        "fragments": [], "claims": [], "relations": [], "sections": [], "side_stories": [],
    }
    current = None
    ordinal = 0

    def consume(start, end, heading=False):
        nonlocal current, ordinal
        ordinal += 1
        block = "".join(lines[start:end])
        fid = f"FR-{digest[:10]}-{start + 1}-{end}"
        cid = f"CL-{digest[:10]}-{start + 1}-{end}"
        loc = f"{path.name}:L{start + 1}-L{end}"
        study["fragments"].append({"id": fid, "source_id": sid, "locator": loc,
                                   "line_start": start + 1, "line_end": end, "text": block})
        study["claims"].append({"id": cid, "text": block, "status": "supplied_claim", "fragment_ids": [fid], "pillar_ids": []})
        if heading or current is None:
            title = re.sub(r"^#{1,6}\s+", "", block.strip()) if heading else "Texte importé"
            current = {"id": f"SEC-{len(study['sections']) + 1:03d}", "title": title, "claim_ids": [], "pillar_ids": [], "paragraphs": []}
            study["sections"].append(current)
        current["claim_ids"].append(cid)
        if not heading:
            current["paragraphs"].append({"id": f"PAR-{ordinal:04d}", "text": block, "claim_ids": [cid], "pillar_ids": [],
                                          "review": {"evidence": False, "editorial": False, "text_sha256": text_hash(block)}})

    start = None
    fence = None
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        fm = re.match(r"^(`{3,}|~{3,})", stripped)
        if fence:
            if fm and fm.group(1)[0] == fence[0] and len(fm.group(1)) >= len(fence):
                fence = None
            continue
        if fm:
            if start is None:
                start = i
            fence = fm.group(1)
            continue
        if re.match(r"^#{1,6}\s+", line):
            if start is not None:
                consume(start, i)
                start = None
            consume(i, i + 1, heading=True)
        elif not line.strip():
            if start is not None:
                consume(start, i)
                start = None
        elif start is None:
            start = i
    if start is not None:
        consume(start, len(lines))
    return study


def validate_study(study):
    """Return structural errors separately from editorial gaps; never mutate input."""
    errors, gaps = [], []
    if not isinstance(study, dict):
        return {"valid": False, "errors": ["study must be an object"], "gaps": []}
    if not isinstance(study.get("id"), str) or not study["id"].strip():
        errors.append("study.id must be nonempty")
    mandate = study.get("mandate")
    if not isinstance(mandate, dict):
        errors.append("mandate must be an object")
        mandate = {}
    for name in ("question", "scope", "audience"):
        if not isinstance(mandate.get(name), str) or not mandate[name].strip():
            errors.append(f"mandate.{name} must be nonempty")
        elif mandate[name].startswith("À "):
            gaps.append(f"mandate.{name}: framing pending")
    indexes, all_ids = {}, set()

    def register(items, name):
        if not isinstance(items, list):
            errors.append(f"{name} must be a list")
            return {}
        result = {}
        for item in items:
            if not isinstance(item, dict):
                errors.append(f"{name} record must be an object")
                continue
            ident = item.get("id")
            if not isinstance(ident, str) or not ident.strip():
                errors.append(f"{name} record missing id")
                continue
            if ident in all_ids:
                errors.append(f"duplicate id: {ident}")
            all_ids.add(ident)
            result[ident] = item
        return result

    for key in ("pillars", "sources", "fragments", "claims", "relations", "sections", "side_stories"):
        indexes[key] = register(study.get(key, []), key)
    paragraphs = []
    for section in indexes["sections"].values():
        ps = section.get("paragraphs", [])
        if not isinstance(ps, list):
            errors.append(f"{section['id']}.paragraphs must be a list")
        else:
            paragraphs.extend(ps)
    indexes["paragraphs"] = register(paragraphs, "paragraphs")

    def refs(record, field, target, required=False):
        values = record.get(field, [])
        if not isinstance(values, list) or any(not isinstance(v, str) for v in values):
            errors.append(f"{record['id']}.{field} must be a string list")
            return []
        if required and not values:
            errors.append(f"{record['id']}.{field} must not be empty")
        for value in values:
            if value not in indexes[target]:
                errors.append(f"{record['id']}.{field} unknown reference: {value}")
        return values

    for group in ("pillars", "sections"):
        for record in indexes[group].values():
            if not isinstance(record.get("title"), str) or not record["title"].strip():
                errors.append(f"{record['id']}: {group} title must be nonempty")

    for source in indexes["sources"].values():
        for field in ("kind", "access", "title", "locator"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                errors.append(f"{source['id']}.{field} must be nonempty")
        if "text" in source:
            if not isinstance(source["text"], str):
                errors.append(f"{source['id']}.text must be a string")
            elif source.get("sha256") and text_hash(source["text"]) != source["sha256"]:
                errors.append(f"{source['id']}: source sha256 mismatch")
    for fragment in indexes["fragments"].values():
        sid = fragment.get("source_id")
        if not isinstance(sid, str) or sid not in indexes["sources"]:
            errors.append(f"{fragment['id']}: unknown source_id")
            continue
        if not isinstance(fragment.get("text"), str) or not fragment["text"].strip():
            errors.append(f"{fragment['id']}: text must be nonempty")
        if not isinstance(fragment.get("locator"), str) or not fragment["locator"].strip():
            errors.append(f"{fragment['id']}: locator must be nonempty")
        if "line_start" in fragment or "line_end" in fragment:
            lo, hi = fragment.get("line_start"), fragment.get("line_end")
            source = indexes["sources"][sid]
            if not isinstance(lo, int) or isinstance(lo, bool) or not isinstance(hi, int) or isinstance(hi, bool) or lo < 1 or hi < lo:
                errors.append(f"{fragment['id']}: invalid line range")
            elif isinstance(source.get("text"), str):
                lines = source["text"].splitlines(keepends=True)
                if hi > len(lines) or "".join(lines[lo - 1:hi]) != fragment.get("text"):
                    errors.append(f"{fragment['id']}: line slice differs from source")
    for claim in indexes["claims"].values():
        status = claim.get("status")
        if not isinstance(status, str) or status not in STATUSES:
            errors.append(f"{claim['id']}: invalid status")
            status = "unknown"
        if not isinstance(claim.get("text"), str) or not claim["text"].strip():
            errors.append(f"{claim['id']}: text must be nonempty")
        fragment_ids = refs(claim, "fragment_ids", "fragments", required=status in {"supplied_claim", "attributed_claim", "verified_fact"})
        refs(claim, "pillar_ids", "pillars")
        if status == "verified_fact":
            verification = claim.get("verification", {})
            if not isinstance(verification, dict):
                verification = {}
            vids = verification.get("source_ids", [])
            if verification.get("reviewed") is not True or not isinstance(verification.get("note"), str) or not verification["note"].strip() or not isinstance(vids, list) or not vids or any(not isinstance(s, str) for s in vids):
                errors.append(f"{claim['id']}: verified_fact requires reviewed verification, note and source_ids")
                continue
            supporting = {indexes['fragments'][f].get('source_id') for f in fragment_ids if f in indexes['fragments']}
            qualified_primary = False
            for sid in vids:
                source = indexes["sources"].get(sid)
                if source is None or sid not in supporting or source.get("access") not in CONSULTED:
                    errors.append(f"{claim['id']}: verification source {sid} must be consulted and linked by fragment")
                    continue
                if verified_eligible(source) and source.get("qualified") is True:
                    qualified_primary = True
            if not qualified_primary:
                errors.append(f"{claim['id']}: verified_fact requires qualified primary evidence")
    relation_keys = set()
    for relation in indexes["relations"].values():
        for field in ("from", "to"):
            ident = relation.get(field)
            if not isinstance(ident, str) or ident not in indexes["claims"]:
                errors.append(f"{relation['id']}: {field} must reference a claim")
        if not isinstance(relation.get("kind"), str) or relation["kind"] not in RELATIONS:
            errors.append(f"{relation['id']}: invalid relation kind")
        if not isinstance(relation.get("rationale"), str) or not relation["rationale"].strip():
            errors.append(f"{relation['id']}: rationale required")
        key = (relation.get("from"), relation.get("kind"), relation.get("to"))
        if all(isinstance(value, str) for value in key):
            if key in relation_keys:
                errors.append(f"{relation['id']}: duplicate relation {key}")
            relation_keys.add(key)
    for group in ("sections", "paragraphs"):
        for record in indexes[group].values():
            claim_ids = refs(record, "claim_ids", "claims")
            pillar_ids = refs(record, "pillar_ids", "pillars")
            if group == "paragraphs":
                claim_pillars = set()
                for cid in claim_ids:
                    claim = indexes["claims"].get(cid, {})
                    declared = claim.get("pillar_ids", [])
                    if isinstance(declared, list):
                        claim_pillars.update(value for value in declared if isinstance(value, str))
                for pid in pillar_ids:
                    if pid not in claim_pillars:
                        errors.append(f"{record['id']}: pillar {pid} is not declared by referenced claims")
                text = record.get("text")
                if not isinstance(text, str) or not text.strip():
                    errors.append(f"{record['id']}: paragraph text required")
                    continue
                review = record.get("review", {})
                if not isinstance(review, dict):
                    review = {}
                if any(review.get(k) is True for k in ("evidence", "editorial")) and review.get("text_sha256") != text_hash(text):
                    errors.append(f"{record['id']}: review text hash missing or stale")
                for key in ("evidence", "editorial"):
                    if review.get(key) is not True:
                        gaps.append(f"{record['id']}: {key} review pending")
                if not record.get("claim_ids"):
                    gaps.append(f"{record['id']}: no claim coverage")
    anchors = set(indexes["sections"]) | set(indexes["paragraphs"])
    for side in indexes["side_stories"].values():
        state = side.get("state")
        active = isinstance(state, str) and state in {"validated", "promoted"}
        refs(side, "claim_ids", "claims", required=active)
        refs(side, "pillar_ids", "pillars")
        if not isinstance(state, str) or state not in STATES:
            errors.append(f"{side['id']}: invalid lifecycle state")
        if not isinstance(side.get("kind"), str) or side["kind"] not in SIDE_KINDS:
            errors.append(f"{side['id']}: invalid side-story kind")
        if not isinstance(side.get("parent_section_id"), str) or side["parent_section_id"] not in indexes["sections"]:
            errors.append(f"{side['id']}: unresolved parent_section_id")
        if not isinstance(side.get("return_to"), str) or side["return_to"] not in anchors:
            errors.append(f"{side['id']}: unresolved return_to")
        for key in ("reason_outside", "payoff"):
            if not isinstance(side.get(key), str) or not side[key].strip():
                (errors if active else gaps).append(f"{side['id']}: {key} required")
        blocking, pending = sidestories.side_story_findings(side)
        errors.extend(f"{side['id']}: {item}" for item in blocking)
        gaps.extend(f"{side['id']}: {item}" for item in pending)
        if side.get("kind") == "dezoom":
            for key in ("scale_from", "scale_to", "mechanism"):
                if not isinstance(side.get(key), str) or not side[key].strip():
                    errors.append(f"{side['id']}: dezoom {key} required")
            if side.get("scale_from") == side.get("scale_to"):
                errors.append(f"{side['id']}: dezoom must change scale")
    for key in ("pillars", "sources", "claims", "sections"):
        if not indexes[key]:
            gaps.append(f"{key}: empty during inquiry")
    return {"valid": not errors, "errors": errors, "gaps": gaps}


def build_graph(study):
    """Build a proof projection, independently of research links and reader order."""
    result = validate_study(study)
    if result["errors"]:
        raise ValueError("Invalid study: " + "; ".join(result["errors"]))
    nodes, edges = [], []
    for group, kind in (("sources", "source"), ("fragments", "fragment"), ("claims", "claim")):
        for record in study.get(group, []):
            nodes.append({"id": record["id"], "kind": kind, "label": record.get("title", record.get("text", record["id"])), **({"status": record["status"]} if "status" in record else {})})
    for fragment in study.get("fragments", []):
        edges.append({"id": "origin:" + fragment["id"], "from": fragment["source_id"], "to": fragment["id"], "kind": "source_of"})
    for claim in study.get("claims", []):
        for fid in claim.get("fragment_ids", []):
            edges.append({"id": f"evidence:{fid}:{claim['id']}", "from": fid, "to": claim["id"], "kind": "evidence_for"})
    edges.extend(dict(r) for r in study.get("relations", []))
    return {"study_id": study["id"], "projection": "evidence", "nodes": nodes, "edges": edges}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    imp = sub.add_parser("import")
    imp.add_argument("path", type=Path)
    imp.add_argument("--study-id", required=True)
    imp.add_argument("--out", type=Path)
    for name in ("validate", "graph"):
        command = sub.add_parser(name)
        command.add_argument("path", type=Path)
        command.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == "import":
            result = import_markdown(args.path, args.study_id)
        else:
            study = json.loads(args.path.read_text(encoding="utf-8"))
            result = validate_study(study) if args.command == "validate" else build_graph(study)
        output = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.out:
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(output, encoding="utf-8")
        else:
            print(output, end="")
        return 1 if args.command == "validate" and not result["valid"] else 0
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
