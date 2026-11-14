"""Validate method-specific properties and the result's source-to-block bindings."""
import json
from decimal import Decimal, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def method_error(method, detail):
    if method == "swot-tows":
        factors = {factor["id"]: factor["kind"] for factor in detail["factors"]}
        pair = "".join(factors.get(ref, "?") for ref in detail["pair"])
        if pair not in {"SO", "ST", "WO", "WT"} or pair != detail["quadrant"]:
            return "tows_pair"
    elif method == "pestel":
        if detail["event_status"] == "proposal" and detail["application"] != "conditional":
            return "pestel_status"
    elif method == "porter":
        if set(detail["forces"]) != {"buyers", "suppliers", "entrants", "substitutes", "rivalry"}:
            return "porter_coverage"
    elif method == "ishikawa":
        if detail["cause_status"] != "candidate":
            return "ishikawa_cause"
    elif method == "marketing-4p":
        if set(detail["mix"]) != {"product", "price", "place", "promotion"}:
            return "marketing_mix"
        if detail["price_basis"] == "proposed" and detail["demand_status"] == "verified":
            return "marketing_demand"
    elif method == "vrio":
        dimensions = detail["dimensions"]
        if set(dimensions) != {"value", "rarity", "inimitability", "organization"}:
            return "vrio_dimensions"
        if detail["conclusion"] == "sustained_advantage" and set(dimensions.values()) != {"supported"}:
            return "vrio_evidence"
    elif method == "unit-economics":
        margin = Decimal(str(detail["price"])) - Decimal(str(detail["variable"]))
        threshold = None if margin <= 0 else int(
            (Decimal(str(detail["fixed"])) / margin).to_integral_value(rounding=ROUND_CEILING)
        )
        if threshold != detail["break_even"]:
            return "unit_threshold"
    else:
        raise ValueError(f"Unknown method {method}")
    return None


def run():
    registry = json.loads((ROOT / "registry.json").read_text())
    observed = {}
    for key, entry in registry["methods"].items():
        card = json.loads((ROOT / entry["asset"]).read_text())
        fixture = json.loads((ROOT / entry["fixture"]).read_text())
        result = fixture["result"]
        if card["id"] != key or result["method"] != key:
            raise ValueError(f"Unbound method {key}")
        inputs = set(result["input_claim_refs"])
        if not inputs <= fixture["claims"].keys() or not set(result["affects_blocks"]) <= set(fixture["blocks"]):
            raise ValueError(f"Unresolved bindings for {key}")
        for finding in result["findings"]:
            if not set(finding["claim_refs"]) <= inputs:
                raise ValueError(f"Unbound finding for {key}")
        good = method_error(key, fixture["positive_details"])
        bad = method_error(key, fixture["negative_details"])
        if good or bad != fixture["expected_negative"]:
            raise ValueError(f"{key} returned {good}, {bad}")
        observed[key] = {"positive": "PASS", "negative_rejected_for": bad}
    return observed


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
