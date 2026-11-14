"""Measure previous and strengthened controls on the same synthetic mutations."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from shutil import copytree

from functional_review import CHECKS, ROOT


def measure(snapshot):
    registry = json.loads((ROOT / "registry.json").read_text())["routes"]
    rows = []
    for route, entry in registry.items():
        with tempfile.TemporaryDirectory() as temp:
            work = Path(temp) / route
            copytree(ROOT / route, work)
            manifest = json.loads((work / "manifest.json").read_text())
            path = work / manifest["functional_review"]["fixture"]
            fixture = json.loads(path.read_text())
            case = fixture["functional_case"]
            command = [sys.executable, str(work / Path(entry["replay"]).name)]
            if route == "pedagogie":
                command.extend(["--snapshot", str(snapshot.resolve())])
            for mutation in case["holdouts"]:
                candidate = dict(case["corrected"], **mutation["replace"])
                fixture["functional_case"]["decision_under_review"] = candidate
                path.write_text(json.dumps(fixture, ensure_ascii=False))
                old = subprocess.run(command, capture_output=True, text=True)
                if old.returncode:
                    raise RuntimeError(old.stderr)
                new = CHECKS[route](candidate)
                if new != mutation["expected_errors"]:
                    raise ValueError((route, new))
                rows.append({"route":route,"mutation":mutation["id"],"previous_exit":old.returncode,"strengthened_errors":new})
    return rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot",type=Path,required=True)
    args = parser.parse_args()
    print(json.dumps(measure(args.snapshot),indent=2))
