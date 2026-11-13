"""Replay the four vertical fixtures and verify their registry bindings."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--repo", type=Path)
    source.add_argument("--snapshot", type=Path)
    args = parser.parse_args()
    catalog = json.loads((ROOT / "registry.json").read_text())
    results = {}
    for route, profile in catalog["routes"].items():
        for key in ["profile", "manifest"]:
            if not (ROOT / profile[key]).is_file():
                raise FileNotFoundError(profile[key])
        for path in profile["fixtures"].values():
            json.loads((ROOT / path).read_text())
        command = [sys.executable, str(ROOT / profile["replay"])]
        if route == "pedagogie":
            command.extend(["--repo", str(args.repo.resolve())] if args.repo else ["--snapshot", str(args.snapshot.resolve())])
        run = subprocess.run(command, capture_output=True, text=True, check=True)
        results[route] = json.loads(run.stdout)
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
