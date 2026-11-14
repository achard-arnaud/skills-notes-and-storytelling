"""Replay annotated synthetic twins. Human review supplies the feature annotations."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def accepted(rule, f):
    if rule == "standalone_capability":
        return not f["requires_external_legend"] and f["input_capability"] == "to_verify"
    if rule == "buyer_qualification":
        return bool(f["alternative"]) and (f["budget_owner_verified"] or f["buyer_status"] == "hypothesis")
    if rule == "scope_revenue":
        return f["published_price_scope"] == f["revenue_scope"] or f["extension_revenue"] is None
    if rule == "activity_scope":
        return set(f["metrics"]) == {"fabrication", "maintenance"} and len(set(f["metrics"].values())) == 2
    if rule == "integration_boundary":
        return bool(f["countertest"]) and (f["consumer_check"] == "verified" or not f["guaranteed"])
    if rule == "observable_learning":
        return all(f[k] for k in ("observable", "trigger", "corrective_action", "retry"))
    raise ValueError(rule)

def main():
    cases = json.loads((ROOT / "inventory.json").read_text())["cases"]
    counts = Counter(case["target_template"] for case in cases)
    if max(counts.values()) > 5:
        raise ValueError("fixture budget exceeded")
    results = []
    for case in cases:
        fixture = json.loads((ROOT / case["fixture"]).read_text())
        results.append({"id":case["id"], **{v:accepted(fixture["oracle"],fixture[v]["features"]) for v in ("v1","v2")}})
    if any(row["v1"] or not row["v2"] for row in results):
        raise ValueError(results)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
