#!/usr/bin/env python3
"""One read-only receipt: loopback observations plus ontology checks for a KB graph.

Never writes the graph, never merges, promotes or approves. At most three actions.
Contract: docs/REINFORCE-KB-SKILL-CONTRACT.md.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import loopback  # noqa: E402
import ontology  # noqa: E402

ACTION_LIMIT = 3


def reinforce(graph: dict, recent_ids=None, previous=None) -> dict:
    loop = loopback.analyze_graph(graph, recent_ids=recent_ids, previous=previous)
    onto = loop["ontology"]
    actions = [{key: candidate.get(key) for key in ("kind", "status", "observation", "hypothesis", "proposal", "test")}
               for candidate in loop["review_candidates"][:ACTION_LIMIT]]
    return {
        "tool": "reinforce.py",
        "contract": "diagnostic-complet/docs/REINFORCE-KB-SKILL-CONTRACT.md",
        "ontology": {"id": onto["ontology_id"], "version": onto["version"], "status": onto["status"]},
        "graph_sha256": loop["graph_sha256"],
        "decision": loop["decision"],
        "actions": actions,
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


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("graph", type=Path)
    parser.add_argument("--recent-id", action="append", default=[])
    parser.add_argument("--previous", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
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
