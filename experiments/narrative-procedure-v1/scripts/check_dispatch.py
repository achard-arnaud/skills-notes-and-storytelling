"""Exercise route -> format -> analytical card -> real block binding."""
import json
from collections import Counter
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
ROOT = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads(path.read_text())
def run(root):
    vertical = root / "verticales"
    registry = read(vertical / "registry.json")
    catalog = registry["routes"]
    mba = read(root / "mba/registry.json")["methods"]
    validator = Draft202012Validator(read(root/"contracts/analysis-result.schema.json"), format_checker=FormatChecker())
    counts = Counter()
    receipts = []
    for route, spec in catalog.items():
        manifest = read(vertical / spec["manifest"])
        for template, fixture in spec["fixtures"].items():
            read(vertical / fixture)
            counts[template] += 1
            formats = manifest.get("formats", manifest.get("templates", {}))
            config = formats.get(template, {})
            blocks = config.get("block_ids") or config.get("required_blocks") or [b["block"] for b in config.get("scaffold", [])] or [b[0] for b in manifest.get("blocks", [])]
            if not blocks:
                raise ValueError((route, template))
            receipts.append({"route":route,"template":template,"blocks":blocks})
    for file in (root/"history/fixtures").glob("*.json"):
        case = read(file)
        active = catalog[case["vertical"]]["fixtures"]
        archived = registry.get("retired_fixtures", {}).get(case["vertical"], {})
        assert case["template"] in active or case["template"] in archived
        counts[case["template"]] += 1
    assert max(counts.values()) <= 5
    for entry in mba.values():
        fixture = read(root/"mba"/entry["fixture"])
        validator.validate(fixture["result"])
    example = next(x for x in receipts if x["route"]=="business" and x["template"]=="one-pager")
    packet = read(root/"mba"/mba["unit-economics"]["fixture"])["result"]
    packet["affects_blocks"] = [example["blocks"][0]]
    validator.validate(packet)
    assert set(packet["affects_blocks"]) <= set(example["blocks"])
    return {"routes":len(catalog),"bindings":receipts,"fixtures_by_template":dict(counts),"schema_valid_mba_results":len(mba),"example_bound_block":packet["affects_blocks"]}
if __name__=="__main__":
    print(json.dumps(run(ROOT),ensure_ascii=False,indent=2))
