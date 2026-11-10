#!/usr/bin/env python3
"""One read-only receipt: loopback observations plus ontology checks for a KB graph.

Never writes the graph, never merges, promotes or approves. No cap on the number of proposals.
Contract: doc/architecture/ADR-0005-contrat-skill-reinforce.md.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import loopback  # noqa: E402
import ontology  # noqa: E402



def reinforce(graph: dict, recent_ids=None, previous=None) -> dict:
    loop = loopback.analyze_graph(graph, recent_ids=recent_ids, previous=previous)
    onto = loop["ontology"]
    # No cap: a run can produce proposals in several places at once. Each one stays a candidate, never applied.
    actions = [{key: candidate.get(key) for key in ("kind", "status", "observation", "hypothesis", "proposal", "test")}
               for candidate in loop["review_candidates"]]
    by_kind = {}
    for action in actions:
        by_kind[action["kind"]] = by_kind.get(action["kind"], 0) + 1
    return {
        "tool": "reinforce.py",
        "contract": "diagnostic-complet/doc/architecture/ADR-0005-contrat-skill-reinforce.md",
        "ontology": {"id": onto["ontology_id"], "version": onto["version"], "status": onto["status"]},
        "graph_sha256": loop["graph_sha256"],
        "decision": loop["decision"],
        "actions": actions,
        "actions_by_kind": dict(sorted(by_kind.items())),
        "deferred_actions": loop["deferred_candidates"],
        "measurements": {
            "directed_density": loop["metrics"]["directed_density"],
            "semantic_density": onto["semantic_density"],
            "semantic_nodes": onto["semantic_nodes"],
            "class_counts": onto["class_counts"],
        },
        "findings": {
            "violations": onto["violations"]["count"],
            "out_of_ontology": onto["out_of_ontology"]["count"],
            "unclassified": onto["unclassified"]["count"],
            "alias_candidates": onto["alias_candidates"]["count"],
        },
        "triggers_fired": [trigger["id"] for trigger in onto["review_triggers"] if trigger["fired"]],
        "triggers_measured_only": [trigger["id"] for trigger in onto["review_triggers"] if trigger["fired"] is None],
        "automatic_mutations": False,
        "automatic_promotion": False,
        "candidate_approval": False,
        "limits": ontology.LIMITS,
    }


def reinforce_batch(graphs: dict) -> dict:
    """Aggregate receipts over named graphs. Counts only; no threshold, no ranking, no approval."""
    per_graph = {name: reinforce(graph) for name, graph in sorted(graphs.items())}
    decisions = {}
    for receipt in per_graph.values():
        decisions[receipt["decision"]] = decisions.get(receipt["decision"], 0) + 1
    return {
        "tool": "reinforce.py", "mode": "batch", "graphs": len(per_graph),
        "decisions": dict(sorted(decisions.items())),
        "violations_total": sum(r["findings"]["violations"] for r in per_graph.values()),
        "unclassified_total": sum(r["findings"]["unclassified"] for r in per_graph.values()),
        "alias_candidates_total": sum(r["findings"]["alias_candidates"] for r in per_graph.values()),
        "per_graph": {name: {"decision": r["decision"], "violations": r["findings"]["violations"],
                             "triggers_fired": r["triggers_fired"], "graph_sha256": r["graph_sha256"]}
                      for name, r in per_graph.items()},
        "automatic_mutations": False, "automatic_promotion": False, "candidate_approval": False,
        "limits": ontology.LIMITS,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("graph", type=Path, nargs="?")
    parser.add_argument("--batch", type=Path, help="directory of graph-*.json to aggregate")
    parser.add_argument("--recent-id", action="append", default=[])
    parser.add_argument("--previous", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    if args.batch:
        graphs = {path.name: json.loads(path.read_text(encoding="utf-8")) for path in sorted(args.batch.glob("graph-*.json"))}
        receipt = reinforce_batch(graphs)
    else:
        if args.graph is None:
            parser.error("graph or --batch required")
        graph = json.loads(args.graph.read_text(encoding="utf-8"))
        previous = json.loads(args.previous.read_text(encoding="utf-8")) if args.previous else None
        receipt = reinforce(graph, recent_ids=args.recent_id, previous=previous)
    text = json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
