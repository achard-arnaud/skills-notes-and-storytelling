#!/usr/bin/env python3
"""Ontology referential and read-only checks for the documentary KB graph.

Nothing here writes a graph, merges nodes, promotes a fact or approves a candidate.
Thresholds are not targets: a trigger without a calibrated threshold only reports a count.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
REFERENTIAL = ROOT / "ontology" / "ontology-v1.json"
CANONICAL_RELATIONS = ROOT.parent / "contracts" / "relation-types.json"
ONTOLOGY_ID = "business-kb-ontology"
DETAIL_LIMIT = 20
STRUCTURAL_RULES = {"derived_from", "candidate_classification", "explicit_mention", "addresses_pillar"}
LIMITS = [
    "Le référentiel nomme le vocabulaire ; il ne prouve ni la véracité d'une assertion ni la pertinence d'un lien.",
    "La densité sémantique n'est pas un score de qualité.",
    "Les déclencheurs de revue sont des signaux. Un seuil sans calibration n'est pas une cible.",
    "Les candidats d'alias ne sont jamais appliqués ; la décision est humaine.",
    "Le libellé des nœuds est tronqué à 180 caractères par kb.py ; deux textes différents peuvent partager un préfixe.",
]


class OntologyError(ValueError):
    """Raised when the referential itself is inconsistent."""


def load(path: Path = REFERENTIAL) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_referential(data)
    return data


def _all_types(onto: dict) -> set[str]:
    return {f"{cls}.{name}" for cls, spec in onto["classes"].items() for name in spec["types"]}


def validate_referential(onto: dict) -> None:
    if onto.get("ontology_id") != ONTOLOGY_ID:
        raise OntologyError("not a business-kb-ontology referential")
    known = _all_types(onto)
    for key, target in onto["node_map"].items():
        if target not in known:
            raise OntologyError(f"node_map {key!r} points to unknown type {target!r}")
    rules = onto["edge_rules"]
    ids = [rule["id"] for rule in rules]
    if len(ids) != len(set(ids)):
        raise OntologyError("duplicate edge rule id")
    for rule in rules:
        for side in ("domain", "range"):
            for target in rule[side]:
                if target not in known:
                    raise OntologyError(f"edge rule {rule['id']!r} {side} uses unknown type {target!r}")
    canonical = {item["id"] for item in json.loads(CANONICAL_RELATIONS.read_text(encoding="utf-8"))["relations"]}
    probatory = {rule["id"] for rule in rules if rule["id"] not in STRUCTURAL_RULES}
    if probatory != canonical:
        raise OntologyError(f"probatory rules differ from canonical catalogue: "
                            f"missing={sorted(canonical - probatory)} extra={sorted(probatory - canonical)}")
    for name in onto["density_scope"]["classes"]:
        if name not in known:
            raise OntologyError(f"density_scope names unknown type {name!r}")
    for trigger in onto["review_triggers"]:
        if trigger["threshold"] is not None and trigger["calibration"] != "not_required":
            raise OntologyError(f"trigger {trigger['id']!r} has a threshold without calibration: no target allowed")
    if onto["alias_policy"]["action"] != "none" or onto["alias_policy"]["candidate_approval"] is not False:
        raise OntologyError("alias policy must never apply a change nor approve a candidate")


def node_key(node: dict) -> str | None:
    value = node.get("type", node.get("node_type"))
    if value == "atom":
        kind = node.get("kind")
        return f"atom:{kind}" if isinstance(kind, str) else None
    return value if isinstance(value, str) else None


def classify_node(node: dict, onto: dict) -> str:
    key = node_key(node)
    return onto["node_map"].get(key, "unclassified") if key else "unclassified"


def _edge_kind(edge: dict) -> str | None:
    value = edge.get("kind", edge.get("type", edge.get("edge_type")))
    return value if isinstance(value, str) else None


def check_edge(edge: dict, src_class: str, tgt_class: str, rules: dict) -> tuple[str, str | None]:
    kind = _edge_kind(edge)
    rule = rules.get(kind)
    if rule is None:
        return "out_of_ontology", kind
    if "unclassified" in (src_class, tgt_class):
        return "unclassified_endpoint", kind
    if src_class not in rule["domain"] or tgt_class not in rule["range"]:
        return "domain_range", f"{kind}: {src_class} -> {tgt_class}"
    if rule.get("evidence_required") and not edge.get("evidence"):
        return "evidence_missing", kind
    prefix = rule.get("status_required_prefix")
    if prefix and not str(edge.get("status", "")).startswith(prefix):
        return "status_missing", kind
    return "ok", None


def analyze(graph: dict, recent_ids=None, previous=None, onto: dict | None = None) -> dict:
    """Read-only ontology report. Inputs are never mutated."""
    onto = onto or load()
    recent_ids = [] if recent_ids is None else list(recent_ids)
    nodes: dict[str, dict] = {}
    for node in graph.get("nodes", []):
        if isinstance(node, dict) and isinstance(node.get("id"), str):
            nodes.setdefault(node["id"], node)
    node_class = {nid: classify_node(node, onto) for nid, node in nodes.items()}
    class_counts = Counter(node_class.values())
    semantic_classes = set(onto["density_scope"]["classes"])
    semantic_ids = {nid for nid, cls in node_class.items() if cls in semantic_classes}
    rules = {rule["id"]: rule for rule in onto["edge_rules"]}

    violations, out_of, pairs = [], [], set()
    sources_of: dict[str, set] = defaultdict(set)
    hil_pillars: set[str] = set()
    classified: dict[str, set] = defaultdict(set)
    for index, edge in enumerate(graph.get("edges", [])):
        if not isinstance(edge, dict):
            continue
        source = edge.get("from", edge.get("source"))
        target = edge.get("to", edge.get("target"))
        if source not in nodes or target not in nodes:
            continue
        kind = _edge_kind(edge)
        status, reason = check_edge(edge, node_class[source], node_class[target], rules)
        if status == "out_of_ontology":
            out_of.append({"id": edge.get("id", index), "kind": reason})
        elif status != "ok":
            violations.append({"id": edge.get("id", index), "status": status, "reason": reason})
        if kind == "derived_from":
            sources_of[target].add(source)
        if kind == "addresses_pillar" and node_class[source] == "analysis.hil":
            hil_pillars.add(target)
        if kind == "candidate_classification":
            classified[source].add(target)
        if source in semantic_ids and target in semantic_ids and source != target:
            pairs.add((source, target))

    unclassified = sorted(nid for nid, cls in node_class.items() if cls == "unclassified")
    n = len(semantic_ids)
    denominator = n * (n - 1)
    recent_known = sorted(set(recent_ids) & nodes.keys())
    hit_hil = [nid for nid in recent_known if nid in semantic_ids and classified[nid] & hil_pillars]
    directive_recent = [nid for nid in recent_known if node_class[nid] == "instruction.directive"]
    previous_semantic = (previous or {}).get("ontology", {}).get("semantic_nodes") if isinstance(previous, dict) else None
    delta = n - previous_semantic if isinstance(previous_semantic, int) else None
    triggers = [
        {"id": "hil_touched", "fired": bool(hit_hil), "count": len(hit_hil), "sample": hit_hil[:DETAIL_LIMIT],
         "threshold": 1, "calibration": "not_required"},
        {"id": "directive_in_material", "fired": bool(directive_recent), "count": len(directive_recent),
         "sample": directive_recent[:DETAIL_LIMIT], "threshold": 1, "calibration": "not_required"},
        {"id": "cadence_semantic", "fired": None, "measured_delta": delta, "threshold": None,
         "calibration": "pending_real_corpus", "status": "measured_only"},
    ]

    groups: dict[str, list] = defaultdict(list)
    for nid in semantic_ids:
        if node_class[nid] == "assertion.fact":
            label = re.sub(r"\s+", " ", str(nodes[nid].get("label", "")).casefold()).strip()
            if label:
                groups[label].append(nid)
    aliases = []
    for text_key, members in groups.items():
        if len(members) < 2:
            continue
        sources = {src for member in members for src in sources_of[member]}
        if len(sources) >= 2:
            aliases.append({"text_key": text_key[:80], "members": sorted(members)[:DETAIL_LIMIT],
                            "source_count": len(sources), "action": "none", "candidate_approval": False,
                            "requires": onto["alias_policy"]["requires"]})

    return {
        "ontology_id": onto["ontology_id"],
        "version": onto["version"],
        "status": onto["status"],
        "class_counts": dict(sorted(class_counts.items())),
        "semantic_nodes": n,
        "semantic_density": {"value": (len(pairs) / denominator) if denominator else 0.0,
                             "numerator": len(pairs), "denominator": denominator, "is_quality_score": False},
        "unclassified": {"count": len(unclassified), "sample": unclassified[:DETAIL_LIMIT]},
        "violations": {"count": len(violations), "sample": violations[:DETAIL_LIMIT]},
        "out_of_ontology": {"count": len(out_of), "sample": out_of[:DETAIL_LIMIT]},
        "review_triggers": triggers,
        "alias_candidates": {"count": len(aliases), "sample": aliases[:DETAIL_LIMIT]},
        "limits": LIMITS,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="validate the referential")
    run = sub.add_parser("analyze", help="read-only ontology report for a graph.json")
    run.add_argument("graph", type=Path)
    run.add_argument("--recent-id", action="append", default=[])
    run.add_argument("--previous", type=Path)
    run.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    onto = load()
    if args.command == "check":
        print(json.dumps({"ok": True, "ontology_id": onto["ontology_id"], "version": onto["version"],
                          "types": len(_all_types(onto)), "edge_rules": len(onto["edge_rules"])}, ensure_ascii=False))
        return 0
    graph = json.loads(args.graph.read_text(encoding="utf-8"))
    previous = json.loads(args.previous.read_text(encoding="utf-8")) if args.previous else None
    report = analyze(graph, recent_ids=args.recent_id, previous=previous, onto=onto)
    text = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
