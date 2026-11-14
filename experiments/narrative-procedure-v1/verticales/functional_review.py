"""Check typed decision records attached to four existing template fixtures."""
import json
import math
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def product(record):
    errors = []
    if record["decision"] == "launch" and not set(record["required_buyer_capabilities"]) <= set(record["observed_buyer_capabilities"]):
        errors.append("buyer_prerequisite")
    if record["metric_window_days"] > record["decision_window_days"]:
        errors.append("metric_unavailable_at_decision")
    return errors


def business(record):
    errors = []
    if record["decision"] == "book_gain":
        if record["saving_basis"] != "measured" or record["eligible_volume"] is None:
            errors.append("benefit_unobserved")
        elif record["eligible_volume"] * record["unit_saving"] < record["fixed_cost"]:
            errors.append("below_break_even")
    if record["unit_saving"] <= 0 or record["break_even_cases"] != math.ceil(record["fixed_cost"] / record["unit_saving"]):
        errors.append("break_even")
    return errors


def technical(record):
    errors = []
    if record["architecture_kept"] and record["observed_lag_ms"] > record["reject_above_ms"]:
        errors.append("countertest_invalidates_choice")
    if record["posture"] == "production" and not record["exit_rehearsed"]:
        errors.append("production_without_exit")
    return errors


def pedagogical(record):
    errors = []
    expected = {"legible_match": "accept", "derived_only": "flag", "illegible": "suspend"}
    if not record["cards"] or set(record["cards"]) != set(record["answers"]):
        errors.append("materials_and_key")
    elif any(expected.get(card["condition"]) != record["answers"][key] for key, card in record["cards"].items()):
        errors.append("incorrect_key")
    retry = record["transfer"]
    if retry["id"] in record["cards"] or any(retry["material"] == card["material"] for card in record["cards"].values()):
        errors.append("repeated_material")
    if expected.get(retry["condition"]) != retry["answer"]:
        errors.append("incorrect_transfer")
    return errors


CHECKS = {"produit":product, "business":business, "technique":technical, "pedagogie":pedagogical}


def replay():
    registry = json.loads((ROOT / "registry.json").read_text())
    results = {}
    for route, check in CHECKS.items():
        manifest = json.loads((ROOT / registry["routes"][route]["manifest"]).read_text())
        fixture = json.loads((ROOT / route / manifest["functional_review"]["fixture"]).read_text())
        case = fixture["functional_case"]
        passing = check(case["corrected"])
        if passing:
            raise ValueError((route, passing))
        observations = []
        for mutation in case["holdouts"]:
            candidate = deepcopy(case["corrected"])
            candidate.update(mutation["replace"])
            errors = check(candidate)
            if errors != mutation["expected_errors"]:
                raise ValueError((route, errors, mutation["expected_errors"]))
            observations.append({"variant":mutation["id"],"v1_observed":errors,"v2_observed":passing})
        results[route] = observations
    return results


if __name__ == "__main__":
    print(json.dumps(replay(), ensure_ascii=False, indent=2))
