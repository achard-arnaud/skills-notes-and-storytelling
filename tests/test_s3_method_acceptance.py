"""Synthetic method acceptance. Funding and capability rows are review oracles."""
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "diagnostic-complet"
FIXTURE = ROOT / "tests/fixtures/s3-method-acceptance-v1.json"


class S3MethodAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_owner_and_method_remain_resolvable(self):
        self.assertNotEqual(self.case["subject"]["offer"], self.case["subject"]["operator"])
        for domain, question in self.case["questions"].items():
            with self.subTest(domain=domain):
                manifest = ROOT / "skills" / f"{domain}-analysis" / "manifest.json"
                route = json.loads(manifest.read_text(encoding="utf-8"))["methods"][question["method"]]
                self.assertEqual(question["reference"], route)
                self.assertTrue((ROOT / route).is_file())

    def test_capability_evidence_levels_are_distinct(self):
        observations = self.case["capability_review"]
        self.assertEqual(
            {"announced", "documented", "tested", "used_in_organization", "measured"},
            {row["level"] for row in observations},
        )
        for row in observations:
            with self.subTest(level=row["level"]):
                source = self.case["sources"][row["source"]]
                self.assertEqual("product", source["domain"])
                self.assertEqual(row["status"], source["status"])
                self.assertEqual(self.case["subject"]["offer"], source["subject"])
        self.assertEqual("attributed_claim", self.case["sources"]["target"]["status"])
        self.assertEqual("unknown", self.case["adoption"]["target_only"]["measurement_status"])

    def test_adoption_target_stays_unknown_and_observation_yields_calculation(self):
        with patch.object(sys, "path", [str(LEGACY), *sys.path]):
            from adoption import analyze_adoption
            from planning import CATALOG
            from writing import EVIDENCE_KEYS, study_hash

        seed = json.loads((LEGACY / "fixtures/convergence-adoption.json").read_text(encoding="utf-8"))
        for label, example in self.case["adoption"].items():
            with self.subTest(example=label):
                study = seed["study"].copy()
                scope = self.case["subject"]["offer"]
                study.update(title=scope, mandate={**study["mandate"], "scope": scope})
                brief = {**seed["brief"], "scope": scope}
                question = {**seed["question"], "input_claim_refs": [], "evidence_map": []}
                source = self.case["sources"][example["source"]]
                self.assertEqual("product", source["domain"])
                study["sources"] = [{**study["sources"][0], "locator": example["source"]}]
                study["fragments"] = [{**study["fragments"][0], "text": source["excerpt"]}]
                study["claims"] = []
                for index, (requirement, statement) in enumerate(example["evidence"].items(), 1):
                    claim = f"E{index}"
                    study["claims"].append({
                        "id": claim, "text": statement, "status": source["status"],
                        "fragment_ids": ["F1"], "pillar_ids": [],
                    })
                    question["input_claim_refs"].append(claim)
                    if requirement in CATALOG["methods"][question["method"]]["required_evidence"]:
                        question["evidence_map"].append({"requirement": requirement, "claim_refs": [claim]})
                plan = {
                    "schema_version": "1.0", "id": "PLAN1", "study_ref": study["id"],
                    "intent_ref": brief["id"], "intent_revision": study_hash(brief),
                    "input_revision": study_hash({key: study[key] for key in EVIDENCE_KEYS}),
                    "catalog_revision": study_hash(CATALOG), "questions": [question],
                    "budget": {"max_publications": 1, "max_queries": 1},
                }
                measurements = {**example["context"], "unit": "users"}
                for field, requirement in (("active", "useful_event"), ("eligible", "eligible_population")):
                    refs = next((row["claim_refs"] for row in question["evidence_map"]
                                 if row["requirement"] == requirement), [])
                    measurements[field] = {"value": example[field], "claim_refs": refs}
                result = analyze_adoption(study, brief, plan, "Q1", measurements, analysis_id="A1")
                row = result["envelope"]["analyses"][0]
                self.assertEqual(example["expected_percentage"], result["method_output"]["percentage"])
                self.assertEqual(example["measurement_status"], row["findings"][0]["status"]
                                 if row["findings"] else "unknown")
                self.assertFalse(result["human_approval"])

    def test_funding_oracle_separates_channels_and_financial_stages(self):
        funding = self.case["funding_review"]
        sources = self.case["sources"]
        self.assertEqual({"direct", "indirect"}, {row["channel"] for row in funding})
        self.assertEqual(self.case["subject"]["operator"], funding[0]["holder"])
        self.assertNotEqual(funding[0]["holder"], funding[0]["deployer"])
        for row in funding:
            with self.subTest(channel=row["channel"]):
                self.assertTrue(row["restrictions"])
                self.assertTrue(row["continuity_condition"])
                self.assertEqual({"promised", "signed", "received", "spent"}, set(row["stages"]))
                for stage, mark in row["stages"].items():
                    if mark["source"] is None:
                        self.assertEqual({"amount_eur": None, "status": "unknown", "source": None}, mark)
                        continue
                    witness = sources[mark["source"]]
                    self.assertEqual(("business", stage, row["channel"]),
                                     (witness["domain"], witness["stage"], witness["channel"]))
                    self.assertEqual((witness["amount_eur"], witness["status"]),
                                     (mark["amount_eur"], mark["status"]))
        direct, indirect = funding
        self.assertEqual("attributed_claim", direct["stages"]["promised"]["status"])
        self.assertIsNone(indirect["stages"]["received"]["amount_eur"])
        self.assertTrue(direct["stages"]["received"]["amount_eur"] > direct["stages"]["spent"]["amount_eur"] > 0)
        self.assertTrue(all(source["subject"] != self.case["method_repository"]
                            for source in sources.values()))


if __name__ == "__main__":
    unittest.main()
