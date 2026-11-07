import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import reinforce  # noqa: E402

FIX = Path(__file__).resolve().parents[1] / "fixtures" / "onto"


def load(name):
    return json.loads((FIX / name).read_text(encoding="utf-8"))


class ReinforceReceiptTests(unittest.TestCase):
    def test_receipt_never_claims_mutation_promotion_or_approval(self):
        receipt = reinforce.reinforce(load("graph-positive.json"), recent_ids=["F1"])
        self.assertIs(receipt["automatic_mutations"], False)
        self.assertIs(receipt["automatic_promotion"], False)
        self.assertIs(receipt["candidate_approval"], False)

    def test_actions_are_capped_at_three(self):
        receipt = reinforce.reinforce(load("graph-negative-structure.json"), recent_ids=["D2"])
        self.assertLessEqual(len(receipt["actions"]), reinforce.ACTION_LIMIT)

    def test_clean_graph_without_recent_material_is_no_change(self):
        receipt = reinforce.reinforce(load("graph-relations-all.json"))
        self.assertEqual(receipt["decision"], "no_change")
        self.assertEqual(receipt["findings"]["violations"], 0)

    def test_violations_and_directive_trigger_request_review(self):
        receipt = reinforce.reinforce(load("graph-negative-structure.json"), recent_ids=["D2"])
        self.assertEqual(receipt["decision"], "review_required")
        self.assertEqual(receipt["findings"]["violations"], 4)
        self.assertIn("directive_in_material", receipt["triggers_fired"])
        self.assertIn("cadence_semantic", receipt["triggers_measured_only"])

    def test_semantic_density_is_reported_not_scored(self):
        receipt = reinforce.reinforce(load("graph-relations-all.json"))
        self.assertIs(receipt["measurements"]["semantic_density"]["is_quality_score"], False)

    def test_inputs_are_not_mutated(self):
        graph = load("graph-negative-structure.json")
        before = copy.deepcopy(graph)
        reinforce.reinforce(graph, recent_ids=["D2"])
        self.assertEqual(graph, before)

    def test_cli_writes_receipt_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "receipt.json"
            rc = reinforce.main([str(FIX / "graph-positive.json"), "--recent-id", "F1", "--output", str(out)])
            self.assertEqual(rc, 0)
            written = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(written["tool"], "reinforce.py")
            self.assertNotIn("approved", json.dumps(written).lower().replace("candidate_approval", ""))


if __name__ == "__main__":
    unittest.main()
