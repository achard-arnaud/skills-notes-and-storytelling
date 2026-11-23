import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "scripts/s3_direct_routing.py"
FIXTURE = ROOT / "tests/fixtures/s3-routing-mixed-v1.json"


class DirectRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("s3_direct_routing", ENTRY)
        cls.routing = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.routing)
        # A CI checkout and the local evidence snapshot both supply Git objects.
        cls.revision = subprocess.check_output(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True
        ).strip()
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def setUp(self):
        case = self.fixture["input"]
        self.mandate = {
            "revision": self.revision, "subject": dict(case["subject"]), "mode": "direct",
            "objective": case["objective"], "audience": case["audience"],
            "stop_condition": "Compare both scoped answers with the supplied evidence.",
            "questions": [
                {"id": "offer_and_adoption", "domain": "product", "method": "product.adoption",
                 "reason": "The question asks about adoption of the product."},
                {"id": "organizational_funding", "domain": "business",
                 "method": "business.economics-and-financing", "reason": "The organization owns the funding."},
            ],
            "sources": [x["locator"] for x in case["sources"]],
            "operator_context": [case["operator_context"]["locator"]],
            "availability": {"product": "native", "business": "manual"},
        }

    def plan(self):
        return self.routing.make_plan(ROOT, self.mandate)

    def receipt(self, plan):
        return {
            "revision": self.revision, "plan_sha256": self.routing.digest(plan),
            "interventions": [
                {"question": item["id"], "method": item["method"],
                 "status": "manual_declared", "actor": "synthetic:reviewer",
                 "output": f"synthetic:{item['id']}", "sources": [self.mandate["sources"][i]]}
                for i, item in enumerate(self.mandate["questions"])
            ],
        }

    def native(self, receipt):
        first = receipt["interventions"][0]
        first.update(status="invocation_observed", actor="synthetic:worker", event_id="e1")
        return dict(event_id="e1", question=first["question"], actor=first["actor"],
                    method=first["method"], output=first["output"],
                    revision=receipt["revision"], plan_sha256=receipt["plan_sha256"])

    def test_mixed_fixture_routes_both_orders_without_reclassifying_free_text(self):
        oracle = self.fixture["oracle"]
        plan = self.plan()
        self.assertEqual(plan["primary_domain"], oracle["primary_domain"])
        self.assertEqual(plan["secondary_domains"], oracle["secondary_domains"])
        self.assertEqual(set(plan["excluded_domains"]), set(oracle["excluded_domains"]))
        self.assertEqual({q["id"]: q["domain"] for q in plan["routes"]}, oracle["question_owners"])
        self.assertEqual(plan["routes"][0]["manifest"]["path"], "skills/product-analysis/manifest.json")
        self.assertEqual(len(plan["routes"][0]["method_pin"]["sha256"]), 64)
        self.mandate["questions"].reverse()
        self.mandate["objective"] = self.fixture["variants"][0]["objective"]
        self.assertEqual(self.plan()["primary_domain"], self.fixture["variants"][0]["expected_primary_domain"])

    def test_complete_ambiguity_and_unavailable_are_distinct(self):
        self.mandate["mode"] = self.fixture["variants"][1]["expected_mode"]
        self.assertEqual(self.plan()["status"], "handoff_complete")
        plan = self.plan()
        with self.assertRaisesRegex(ValueError, "direct"):
            self.routing.verify_receipt(ROOT, plan, self.receipt(plan))
        self.mandate["mode"] = "direct"
        self.mandate["availability"]["product"] = "unavailable"
        self.assertEqual(self.plan()["status"], "route_unavailable")
        self.mandate["clarification"] = "Which product should own the adoption question?"
        self.assertEqual(self.plan()["status"], "needs_clarification")

    def test_rejects_mobile_revision_and_duplicate_owner(self):
        self.mandate["revision"] = "HEAD"
        with self.assertRaisesRegex(ValueError, "commit SHA"):
            self.plan()
        self.mandate["revision"] = self.revision
        self.mandate["questions"][1]["id"] = self.mandate["questions"][0]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate question"):
            self.plan()

    def test_rejects_duplicate_question_owners_with_boundary_whitespace(self):
        owner_id = self.mandate["questions"][0]["id"]
        for padded in (f" {owner_id} ", owner_id + "\t"):
            with self.subTest(padded=padded):
                self.mandate["questions"][1]["id"] = padded
                with self.assertRaisesRegex(ValueError, "duplicate question"):
                    self.plan()

    def test_valid_question_ids_are_preserved_in_plan_and_receipt(self):
        ids = [" offer_and_adoption ", "Offer_and_adoption"]
        for question, raw_id in zip(self.mandate["questions"], ids):
            question["id"] = raw_id
        plan = self.plan()
        self.assertEqual([route["id"] for route in plan["routes"]], ids)
        receipt = self.receipt(plan)
        check = self.routing.verify_receipt(ROOT, plan, receipt)
        self.assertEqual(check["plan_sha256"], receipt["plan_sha256"])
        self.assertEqual(check["manual_declarations"], 2)

    def test_rejects_other_domain_method_and_context_as_external_evidence(self):
        self.mandate["questions"][0]["method"] = "business.economics-and-financing"
        with self.assertRaisesRegex(ValueError, "method"):
            self.plan()
        self.mandate["questions"][0]["method"] = "product.adoption"
        self.mandate["sources"].extend(self.mandate["operator_context"])
        with self.assertRaisesRegex(ValueError, "operator context"):
            self.plan()

    def test_manual_receipt_never_counts_as_native_and_stays_in_scope(self):
        plan = self.plan()
        receipt = self.receipt(plan)
        result = self.routing.verify_receipt(ROOT, plan, receipt)
        self.assertEqual(result["event_records_matched"], 0)
        self.assertEqual(result["manual_declarations"], 2)
        receipt["interventions"][0]["sources"] = self.mandate["operator_context"]
        with self.assertRaisesRegex(ValueError, "source"):
            self.routing.verify_receipt(ROOT, plan, receipt)

    def test_method_repository_is_not_the_subject(self):
        self.mandate["subject"]["product"] = self.fixture["input"]["method_repository"]
        with self.assertRaisesRegex(ValueError, "distinct from the method repository"):
            self.plan()

    def test_rejects_different_revision_digest_and_tampered_plan(self):
        plan = self.plan()
        for field, value in (("revision", "a" * 40), ("plan_sha256", "b" * 64)):
            with self.subTest(field=field):
                receipt = self.receipt(plan)
                receipt[field] = value
                with self.assertRaisesRegex(ValueError, "plan or revision"):
                    self.routing.verify_receipt(ROOT, plan, receipt)
        plan["routes"][0]["method_pin"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "plan differs"):
            self.routing.verify_receipt(ROOT, plan, self.receipt(plan))

    def test_rejects_out_of_plan_method_and_claimed_case_states(self):
        plan = self.plan()
        receipt = self.receipt(plan)
        receipt["interventions"][0]["method"] = "product.fit"
        with self.assertRaisesRegex(ValueError, "planned question or method"):
            self.routing.verify_receipt(ROOT, plan, receipt)
        receipt = self.receipt(plan)
        receipt["case_stages"] = {"A0": "passed"}
        with self.assertRaisesRegex(ValueError, "unexpected"):
            self.routing.verify_receipt(ROOT, plan, receipt)

    def test_native_status_needs_matching_external_event_record(self):
        plan = self.plan()
        receipt = self.receipt(plan)
        event = self.native(receipt)
        with self.assertRaisesRegex(ValueError, "matching event"):
            self.routing.verify_receipt(ROOT, plan, receipt)
        with self.assertRaisesRegex(ValueError, "matching event"):
            self.routing.verify_receipt(ROOT, plan, receipt, [dict(event, output="other")])
        result = self.routing.verify_receipt(ROOT, plan, receipt, [event])
        self.assertEqual(result["event_records_matched"], 1)
        self.assertEqual(result["manual_declarations"], 1)

    def test_cli_builds_plan_and_validates_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            mandate, plan, receipt = [folder / name for name in ("mandate.json", "plan.json", "receipt.json")]
            mandate.write_text(json.dumps(self.mandate), encoding="utf-8")
            cmd = [sys.executable, str(ENTRY), "--repo", str(ROOT)]
            p = subprocess.run(cmd + ["plan", str(mandate)], check=True, capture_output=True, text=True)
            plan.write_text(p.stdout, encoding="utf-8")
            actual = json.loads(p.stdout)
            self.assertEqual(actual, self.plan())
            pin = subprocess.run(cmd + ["fingerprint", str(plan)], check=True, capture_output=True, text=True)
            self.assertEqual(json.loads(pin.stdout)["plan_sha256"], self.routing.digest(actual))
            receipt.write_text(json.dumps(self.receipt(actual)), encoding="utf-8")
            r = subprocess.run(cmd + ["verify", str(plan), str(receipt)], check=True, capture_output=True,
                               text=True)
            self.assertEqual(json.loads(r.stdout)["status"], "receipt_checked")
