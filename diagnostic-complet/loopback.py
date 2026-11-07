#!/usr/bin/env python3
"""Read-only graph observations and bounded review proposals, never graph repairs."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path


SOURCE_COMMIT = "1a33eeb3d7bee058a914a1d405c420c5d16d57cd"
NODE_TYPES = {"source", "fragment", "claim", "atom", "pillar", "hil", "entity"}
PILLAR_TYPES = {"pillar", "hil"}
EDGE_TYPES = {"source_of", "evidence_for", "supports", "contradicts", "depends_on",
              "illustrates", "compares", "contextualizes", "causal_hypothesis",
              "in_pillar", "belongs_to", "has_pillar", "classified_as", "addresses_pillar",
              "about", "grounded_in", "derived_from", "references", "related_to",
              "alias_of", "supersedes", "candidate_classification", "explicit_mention"}
PILLAR_EDGES = {"in_pillar", "belongs_to", "has_pillar", "classified_as", "addresses_pillar", "about", "candidate_classification"}
DETAIL_LIMIT = 20


def _kind(record, edge=False):
    # In documentary KB nodes, type=atom while kind=assertion/question/etc.
    # Structural type must not be confused with the atom's content category.
    value = (record.get("kind", record.get("type", record.get("edge_type"))) if edge else
             record.get("type", record.get("node_type", record.get("kind"))))
    return value if isinstance(value, str) and value else "unknown"


def _identifier(value):
    return isinstance(value, str) and bool(value.strip())


def _sample(values):
    values = list(values)
    return {"count": len(values), "items": values[:DETAIL_LIMIT], "truncated": len(values) > DETAIL_LIMIT}


def _candidate(kind, observed, hypothesis, proposal, test, corrective=False):
    return {"kind": kind, "status": "candidate_not_applied", "observation": observed,
            "hypothesis": {"status": "unverified", "text": hypothesis},
            "proposal": proposal, "test": test,
            "review": {"status": "pending", "human_approval": False},
            "corrective_candidate": corrective,
            "stop_condition": "One proposed change only; stop after two unsuccessful repairs or unavailable evidence."}


def analyze_graph(graph, recent_ids=None, previous=None):
    """Inspect source/fragment/claim and atom/source/pillar projections without mutation.

    Density uses unique valid non-self directed endpoint pairs, not edge records.
    recent_ids denotes explicitly supplied node or edge IDs; no recency is guessed.
    previous may be an earlier graph or this function's earlier report.
    """
    if not isinstance(graph, dict) or not isinstance(graph.get("nodes"), list) or not isinstance(graph.get("edges"), list):
        raise ValueError("graph must contain nodes and edges lists")
    recent_ids = [] if recent_ids is None else recent_ids
    if not isinstance(recent_ids, list) or any(not _identifier(item) for item in recent_ids):
        raise ValueError("recent_ids must be an explicit list of nonempty IDs")
    nodes, duplicate_nodes, malformed_nodes = {}, [], []
    labels = defaultdict(list)
    for index, node in enumerate(graph["nodes"]):
        if not isinstance(node, dict) or not _identifier(node.get("id")):
            malformed_nodes.append(index)
            continue
        nid = node["id"]
        if nid in nodes:
            duplicate_nodes.append(nid)
            continue
        nodes[nid] = node
        label = node.get("text", node.get("label", node.get("title", "")))
        if isinstance(label, str) and label.strip():
            labels[(_kind(node), " ".join(label.casefold().split()))].append(nid)
    label_groups = [ids for ids in labels.values() if len(ids) > 1]
    type_counts = Counter(_kind(node) for node in nodes.values())
    subtype_counts = Counter(f"{_kind(node)}:{node['kind']}" for node in nodes.values()
                             if isinstance(node.get("kind"), str) and node["kind"] != _kind(node))
    pillars = {nid for nid, node in nodes.items() if _kind(node) in PILLAR_TYPES}
    declared_pillars = graph.get("pillars", [])
    if isinstance(declared_pillars, list):
        pillars.update(item["id"] if isinstance(item, dict) else item for item in declared_pillars
                       if _identifier(item.get("id") if isinstance(item, dict) else item))
    membership = {pid: set() for pid in pillars}
    candidate_membership = {pid: set() for pid in pillars}
    invalid_pillars = []
    for nid, node in nodes.items():
        ids = node.get("pillar_ids", node.get("hil_ids", []))
        if not isinstance(ids, list):
            invalid_pillars.append({"node": nid, "reason": "pillar_ids must be a list"})
            continue
        for pid in ids:
            if not isinstance(pid, str) or pid not in pillars:
                invalid_pillars.append({"node": nid, "pillar": pid, "reason": "unknown pillar"})
            elif nid not in pillars:
                membership[pid].add(nid)
    edge_counts = Counter()
    edge_ids, duplicate_edge_ids, invalid_edges, duplicate_edges = set(), [], [], []
    edge_endpoints = {}
    signatures, pairs, connected, self_loops = set(), set(), set(), []
    type_mismatches = []
    valid_edge_records = 0
    for index, edge in enumerate(graph["edges"]):
        if not isinstance(edge, dict):
            invalid_edges.append({"index": index, "reason": "edge must be an object"})
            continue
        kind = _kind(edge, edge=True)
        edge_counts[kind] += 1
        eid = edge.get("id")
        if _identifier(eid):
            if eid in edge_ids:
                duplicate_edge_ids.append(eid)
            edge_ids.add(eid)
        source = edge.get("from", edge.get("source"))
        target = edge.get("to", edge.get("target"))
        if not _identifier(source) or not _identifier(target) or source not in nodes or target not in nodes:
            invalid_edges.append({"index": index, "id": eid, "from": source, "to": target,
                                  "reason": "missing or unknown endpoint"})
            continue
        valid_edge_records += 1
        if _identifier(eid):
            edge_endpoints[eid] = {source, target}
        signature = (source, target, kind)
        if signature in signatures:
            duplicate_edges.append({"from": source, "to": target, "kind": kind, "id": eid})
        signatures.add(signature)
        connected.update((source, target))
        if source == target:
            self_loops.append(eid or str(index))
        else:
            pairs.add((source, target))
        if kind in PILLAR_EDGES:
            if target in pillars and source not in pillars:
                membership[target].add(source)
                if kind == "candidate_classification" or str(edge.get("status", "")).startswith("candidate"):
                    candidate_membership[target].add(source)
            elif source in pillars and target not in pillars:
                membership[source].add(target)
                if kind == "candidate_classification" or str(edge.get("status", "")).startswith("candidate"):
                    candidate_membership[source].add(target)
        left, right = _kind(nodes[source]), _kind(nodes[target])
        if ((kind == "source_of" and (left != "source" or right not in {"fragment", "atom"}))
                or (kind == "evidence_for" and (left not in {"fragment", "atom"} or right != "claim"))):
            type_mismatches.append({"id": eid, "kind": kind, "from_type": left, "to_type": right})
    n = len(nodes)
    denominator = n * (n - 1)
    density = len(pairs) / denominator if denominator else 0.0
    recent = set(recent_ids)
    unknown_recent = sorted(recent - nodes.keys() - edge_ids)
    recent_nodes = recent.intersection(nodes)
    for eid in recent.intersection(edge_endpoints):
        recent_nodes.update(edge_endpoints[eid])
    touched_pillars = sorted(pid for pid, members in membership.items()
                             if members.intersection(recent_nodes) or pid in recent_nodes)
    uncategorized_recent = sorted(nid for nid in recent_nodes if nid not in pillars
                                 and not any(nid in members for members in membership.values()))
    metrics = {"node_records": len(graph["nodes"]), "nodes": n,
               "edge_records": len(graph["edges"]), "valid_edge_records": valid_edge_records,
               "node_types": dict(sorted(type_counts.items())), "edge_types": dict(sorted(edge_counts.items())),
               "node_subtypes": dict(sorted(subtype_counts.items())),
               "directed_density": density, "density_numerator": len(pairs),
               "density_denominator": denominator,
               "density_definition": "unique valid non-self directed endpoint pairs / n(n-1); zero when n < 2",
               "density_is_quality_score": False}
    coverage = {"status": "available" if pillars else "not_projected",
                "pillars": [{"id": pid, "members": len(membership[pid]),
                             "candidate_members": len(candidate_membership[pid]),
                             "recent_members": len(membership[pid].intersection(recent_nodes))} for pid in sorted(pillars)],
                "empty_pillars": sorted(pid for pid in pillars if not membership[pid]),
                "touched_by_recent_material": touched_pillars,
                "uncategorized_recent": _sample(uncategorized_recent),
                "meaning": "Declared/candidate membership only; keyword candidates remain candidates. Counts prove neither relevance nor approval."}
    findings = {"isolated_nodes": _sample(sorted(set(nodes) - connected)),
                "duplicate_node_ids": _sample(duplicate_nodes), "malformed_nodes": _sample(malformed_nodes),
                "duplicate_edge_ids": _sample(duplicate_edge_ids), "duplicate_edges": _sample(duplicate_edges),
                "matching_text_groups": _sample(label_groups), "invalid_references": _sample(invalid_edges),
                "invalid_pillar_references": _sample(invalid_pillars), "self_loops": _sample(self_loops),
                "endpoint_type_mismatches": _sample(type_mismatches),
                "unknown_node_types": sorted(set(type_counts) - NODE_TYPES),
                "unknown_edge_types": sorted(set(edge_counts) - EDGE_TYPES),
                "unknown_recent_ids": _sample(unknown_recent)}
    alerts, candidates = [], []
    structural = bool(invalid_edges or invalid_pillars or duplicate_nodes or duplicate_edge_ids or malformed_nodes)
    if structural:
        alerts.append({"kind": "structural_review", "severity": "attention",
                       "observation": "Malformed identities or unresolved references exist; cause remains unverified."})
        candidates.append(_candidate("structural_review", "See structural findings and graph fingerprint.",
            "An import or identity mapping may require correction; source evidence must decide.",
            "Inspect the smallest implicated source/record; propose one corrective delta with original IDs retained.",
            "Reproduce the defect, test valid input and rejection cases, then review lineage and downstream dependencies.", True))
    if label_groups or duplicate_edges:
        alerts.append({"kind": "compaction_review", "severity": "attention",
                       "observation": "Matching text or repeated typed edges are candidates, not proof of entity identity."})
        candidates.append(_candidate("compaction_review", "See matching_text_groups and duplicate_edges.",
            "Some records may represent aliases or repetition; identical words alone cannot establish this.",
            "Propose merge/alias/tombstone only after source comparison; preserve all original IDs, locators, lineage, redirects and reversibility. Never delete evidence.",
            "Verify every original ID still resolves and every evidence/claim/reader dependency retains provenance; include a homonym counterexample.", not structural))
    if recent_nodes:
        alerts.append({"kind": "pillar_review", "severity": "review",
                       "observation": "Explicitly recent material triggers review of affected or missing analytical memberships."})
        candidates.append(_candidate("pillar_review", {"recent_nodes": _sample(sorted(recent_nodes)),
            "touched_pillars": touched_pillars, "uncategorized": _sample(uncategorized_recent)},
            "New material may change an analytical axis or expose an unrepresented angle; no threshold establishes this.",
            "Review relevance against the mandate and source excerpts; retain, reassign or propose a candidate pillar/alias with reason. Industry/corporate and data/AI distinctions remain explicit.",
            "Compare the new source with current pillar scope and a counterexample; record human retain/change/defer decision without auto-promotion."))
    if type_mismatches or findings["unknown_node_types"] or findings["unknown_edge_types"]:
        alerts.append({"kind": "type_review", "severity": "review",
                       "observation": "Undeclared or endpoint-incompatible types require contract review, not automatic relabelling."})
        candidates.append(_candidate("type_review", "See type counts, unknown types and endpoint mismatches.",
            "The projection may need a domain type or may contain a typing error; frequency does not decide.",
            "Compare the affected records and new material with node/edge semantics; propose one versioned type change only if useful to a concrete query.",
            "Test compatible endpoints, an incompatible relation and source/fragment/claim versus atom/source/pillar projections."))
    if unknown_recent:
        alerts.append({"kind": "unknown_recent_ids", "severity": "attention",
                       "observation": "Some declared recent IDs do not resolve; no recency or content is inferred for them."})
    if not alerts and findings["isolated_nodes"]["count"]:
        alerts.append({"kind": "isolates", "severity": "info",
                       "observation": "Isolated records can be legitimate open notes; do not invent edges to increase density."})
    delta = None
    if previous is not None:
        if not isinstance(previous, dict):
            raise ValueError("previous must be a graph or earlier report")
        old = previous.get("metrics") if "metrics" in previous else analyze_graph(previous)["metrics"]
        if not isinstance(old, dict):
            raise ValueError("previous report requires metrics")
        delta = {key: metrics[key] - old[key] for key in ("nodes", "edge_records", "directed_density")
                 if isinstance(old.get(key), (int, float))}
        delta["meaning"] = "Observed metric changes only; no quality, causality or savings claim."
    return {"version": 1, "graph_sha256": hashlib.sha256(json.dumps(graph, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
            "source_pattern": {"repository": "achard-arnaud/Candidatures-nice", "commit": SOURCE_COMMIT,
                               "path": "workflow/LOOPBACK.md"},
            "metrics": metrics, "findings": findings, "pillar_coverage": coverage, "delta": delta,
            "alerts": alerts, "review_candidates": candidates[:3], "deferred_candidates": max(0, len(candidates) - 3),
            "budgets": {"actions_max": 3, "corrective_candidates_max": 1, "repairs_per_blocker_max": 2,
                        "detail_items_max": DETAIL_LIMIT, "token_usage": None, "cost": None},
            "decision": "review_required" if candidates else ("unknown" if unknown_recent else "no_change"),
            "automatic_mutations": False, "automatic_promotion": False,
            "limits": ["The analyzer observes structure; hypotheses and semantic relevance require source review.",
                       "Density, frequency and lexical overlap are not quality, causality or identity proofs.",
                       "A candidate test is a proposal, not an executed test or human approval.",
                       "No compaction deletes nodes, IDs, evidence or lineage; no scheduler or graph writer is installed."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph", type=Path)
    parser.add_argument("--recent-id", action="append", default=[])
    parser.add_argument("--previous", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        previous = json.loads(args.previous.read_text(encoding="utf-8")) if args.previous else None
        report = analyze_graph(json.loads(args.graph.read_text(encoding="utf-8")), args.recent_id, previous)
        text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(text, encoding="utf-8")
        else:
            print(text, end="")
        return 0
    except (ValueError, OSError, TypeError) as exc:
        parser.exit(2, str(exc) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
