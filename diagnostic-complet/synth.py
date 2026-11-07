#!/usr/bin/env python3
"""Deterministic synthetic KB graph for scale and idempotence checks. Not a model of the real KB."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import sys

PILLARS = 4
KIND_WEIGHTS = (("assertion", 70), ("question", 10), ("heading", 15), ("directive", 5))


def build(sources: int, atoms_per_source: int, seed: int) -> dict:
    rng = random.Random(seed)
    nodes = [{"id": f"P{i}", "type": "pillar", "kind": "candidate_pillar", "label": f"pilier {i}"}
             for i in range(PILLARS)]
    nodes.append({"id": "Q0", "type": "hil", "kind": "hil", "label": "question de décision"})
    edges = [{"id": "AP0", "from": "Q0", "to": "P0", "kind": "addresses_pillar"}]
    kinds = [k for k, _ in KIND_WEIGHTS]
    weights = [w for _, w in KIND_WEIGHTS]
    facts: list[str] = []
    for s in range(sources):
        sid = f"S{s:04d}"
        nodes.append({"id": sid, "type": "source", "kind": "source", "label": sid})
        for a in range(atoms_per_source):
            aid = f"A{s:04d}-{a:03d}"
            kind = rng.choices(kinds, weights=weights)[0]
            nodes.append({"id": aid, "type": "atom", "kind": kind, "label": f"texte {s}-{a} variante {rng.randrange(1000)}"})
            edges.append({"id": f"D{s:04d}-{a:03d}", "from": sid, "to": aid, "kind": "derived_from"})
            if kind == "assertion":
                facts.append(aid)
                if rng.random() < 0.3:
                    pillar = f"P{rng.randrange(PILLARS)}"
                    edges.append({"id": f"C{s:04d}-{a:03d}", "from": aid, "to": pillar,
                                  "kind": "candidate_classification", "status": "candidate_keyword"})
                if len(facts) > 1 and rng.random() < 0.1:
                    earlier = facts[rng.randrange(len(facts) - 1)]
                    edges.append({"id": f"R{s:04d}-{a:03d}", "from": aid, "to": earlier, "kind": "supports"})
    return {"id": f"synthetic-{sources}x{atoms_per_source}-seed{seed}", "projection": "documentary_kb",
            "nodes": nodes, "edges": edges}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--sources", type=int, required=True)
    parser.add_argument("--atoms", type=int, required=True)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    graph = build(args.sources, args.atoms, args.seed)
    text = json.dumps(graph, ensure_ascii=False, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
