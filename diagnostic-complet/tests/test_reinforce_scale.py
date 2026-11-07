import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import reinforce  # noqa: E402
import synth  # noqa: E402
import ontology  # noqa: E402

SCHEMA = json.loads((ROOT / "schemas" / "reinforce-receipt.schema.json").read_text(encoding="utf-8"))


def check_receipt(receipt, schema=SCHEMA):
    """Minimal stdlib subset: required keys, const, enum, maxItems. Not a full JSON Schema validator."""
    errors = []
    for key in schema["required"]:
        if key not in receipt:
            errors.append(f"missing {key}")
    for key, rule in schema["properties"].items():
        if key not in receipt:
            continue
        value = receipt[key]
        if "const" in rule and value != rule["const"]:
            errors.append(f"{key} must be {rule['const']!r}")
        if "enum" in rule and value not in rule["enum"]:
            errors.append(f"{key} not in enum")
        if "maxItems" in rule and (not isinstance(value, list) or len(value) > rule["maxItems"]):
            errors.append(f"{key} exceeds maxItems")
    return errors


class SyntheticGeneratorTests(unittest.TestCase):
    def test_same_seed_gives_identical_graph(self):
        self.assertEqual(synth.build(5, 8, 7), synth.build(5, 8, 7))

    def test_different_seed_changes_graph(self):
        self.assertNotEqual(synth.build(5, 8, 7), synth.build(5, 8, 8))

    def test_generated_graph_respects_the_referential(self):
        report = ontology.analyze(synth.build(6, 12, 3))
        self.assertEqual(report["violations"]["count"], 0)
        self.assertEqual(report["unclassified"]["count"], 0)


class ReceiptContractTests(unittest.TestCase):
    def test_reinforce_is_idempotent_on_same_input(self):
        graph = synth.build(8, 10, 11)
        self.assertEqual(reinforce.reinforce(graph, recent_ids=["A0000-000"]),
                         reinforce.reinforce(graph, recent_ids=["A0000-000"]))

    def test_every_fixture_receipt_meets_the_schema_subset(self):
        fixtures = sorted((ROOT / "fixtures" / "onto").glob("graph-*.json"))
        for path in fixtures:
            receipt = reinforce.reinforce(json.loads(path.read_text(encoding="utf-8")), recent_ids=[])
            with self.subTest(fixture=path.name):
                self.assertEqual(check_receipt(receipt), [])

    def test_tampered_receipt_is_refused(self):
        receipt = reinforce.reinforce(synth.build(2, 4, 1))
        receipt["automatic_mutations"] = True
        self.assertIn("automatic_mutations must be False", check_receipt(receipt))

    def test_more_than_three_actions_is_refused(self):
        receipt = reinforce.reinforce(synth.build(2, 4, 1))
        receipt["actions"] = [{}] * 4
        self.assertIn("actions exceeds maxItems", check_receipt(receipt))


if __name__ == "__main__":
    unittest.main()
