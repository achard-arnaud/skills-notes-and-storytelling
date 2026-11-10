#!/usr/bin/env python3
"""Run-side check: every atom identifier of an example registry resolves in a private KB root.

The build side never reads the corpus (D25, D26). This tool takes the KB root as an argument, so
the check is run by whoever holds the private copy; tests exercise it on a synthetic tree only.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ATOM = re.compile(r"^ATOM-[0-9a-f]{64}$")


def check(registry: dict, kb_root: Path) -> dict:
    atoms_dir = Path(kb_root) / "kb" / "atoms"
    checked, missing, malformed = 0, [], []
    for example in registry.get("examples", []):
        for atom in example.get("atoms", []):
            checked += 1
            if not ATOM.match(atom):
                malformed.append({"example": example["id"], "atom": atom})
            elif not (atoms_dir / atom[5:7] / f"{atom}.md").is_file():
                missing.append({"example": example["id"], "atom": atom})
    return {"checked": checked, "missing": missing, "malformed": malformed, "ok": not missing and not malformed}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("registry", type=Path)
    parser.add_argument("--kb-root", type=Path, required=True, help="namespace root of the private KB (the folder holding kb/atoms)")
    args = parser.parse_args(argv)
    report = check(json.loads(args.registry.read_text(encoding="utf-8")), args.kb_root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
