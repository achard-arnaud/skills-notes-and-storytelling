"""Replay two exercise revisions against the pinned canonical teaching sheet."""
import argparse
import copy
import json
import subprocess
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
def read(name):
    return json.loads((ROOT / name).read_text())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--snapshot", type=Path)
    args = parser.parse_args()
    manifest, fixture = read("manifest.json"), read("fixture.json")
    def source(path):
        if args.snapshot:
            return json.loads((args.snapshot / path).read_text())
        data = subprocess.check_output(["git", "-C", str(args.repo or "."), "show", manifest["ref"] + ":" + path])
        return json.loads(data)
    canonical = source(manifest["canonical_input"])
    validator = Draft202012Validator(source(manifest["contract"]))
    receipts = {}
    for revision in ("v1", "v2"):
        sheet = copy.deepcopy(canonical)
        page = next(p for p in sheet["pages"] if p["kind"] == "transmit")
        exercise = read(revision + ".json")
        page["content"]["exercise"] = exercise
        all_steps = " ".join(exercise["steps"])
        errors = []
        if not all(value in all_steps for value in ("24 €", "30 €", "42 €")):
            errors.append("Tâches A/B/C indisponibles dans le support")
        if not all(row["id"] + " → " + row["expected"] in exercise["check"] for row in fixture["inputs"]):
            errors.append("Corrigé inaccessible")
        if "réessai" not in exercise["check"] or fixture["transfer"]["expected"] not in exercise["check"].split("réessai")[-1]:
            errors.append("Réessai absent")
        validator.validate(sheet)
        changed = [new["kind"] for old,new in zip(canonical["pages"],sheet["pages"]) if old != new]
        assert changed == [fixture["only_changed_page"]]
        assert [p["kind"] for p in sheet["pages"]] == [b[0] for b in manifest["blocks"]]
        receipts[revision] = {"schema":"PASS","changed_pages":changed,"defects":errors,"exercise_gate":"FAIL" if errors else "PASS"}
    assert receipts["v1"]["defects"] == fixture["expected_defects"]
    assert receipts["v2"]["defects"] == []
    print(json.dumps(receipts,ensure_ascii=False,indent=2))
if __name__ == "__main__":
    main()

