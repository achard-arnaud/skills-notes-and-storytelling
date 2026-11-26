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

    def check_example_evidence(self, case_name, outputs):
        """Apply the fixture oracle to synthetic outputs, separately from receipt validation."""
        case = self.fixture["evidence_cases"][case_name]
        self.mandate["sources"] = [source["locator"] for source in case["sources"]]
        plan = self.plan()
        receipt = self.receipt(plan)
        self.assertEqual(
            {route["id"]: route["domain"] for route in plan["routes"]},
            self.fixture["oracle"]["question_owners"],
        )
        self.assertEqual(set(outputs), set(case["expectations"]))
        for part in receipt["interventions"]:
            question = part["question"]
            observed = outputs[question]
            part["sources"] = [observed["source"]]
            self.assertEqual(observed, case["expectations"][question], question)
        checked = self.routing.verify_receipt(ROOT, plan, receipt)
        self.assertEqual(checked["manual_declarations"], 2)
        self.assertEqual(checked["event_records_matched"], 0)

    def test_evidence_oracle_distinguishes_observed_results_from_announcements(self):
        self.check_example_evidence("observed", {
            "offer_and_adoption": {
                "status": "measured", "source": "synthetic:usage#2026-10",
                "cohort": "October pilot", "period": "2026-10", "frequency": "at least weekly",
                "event": "completed a search", "active_organizations": 18,
                "eligible_organizations": 30,
            },
            "organizational_funding": {
                "status": "received", "source": "synthetic:ledger#transfer-7",
                "beneficiary": "Horizon", "amount_eur": 25000, "received_on": "2026-10-16",
            },
        })
        self.check_example_evidence("announced", {
            "offer_and_adoption": {
                "status": "attributed_target", "source": "synthetic:roadmap#adoption",
                "target_organizations": 50, "measured_adoption": None,
            },
            "organizational_funding": {
                "status": "attributed_pledge", "source": "synthetic:announcement#funding",
                "received_amount": None,
            },
        })

    def test_evidence_oracle_rejects_unknown_even_with_positive_sources(self):
        observed = self.fixture["evidence_cases"]["observed"]["expectations"]
        for question in observed:
            with self.subTest(question=question), self.assertRaisesRegex(AssertionError, question):
                self.check_example_evidence("observed", {
                    **observed, question: {**observed[question], "status": "unknown"},
                })

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

    def test_registry_comes_from_the_mandate_revision_not_either_checkout(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)

            def git(*args):
                return subprocess.check_output(
                    ["git", "-C", str(repo), "-c", "user.name=Fixture",
                     "-c", "user.email=fixture@example.invalid", *args], text=True
                ).strip()

            git("init", "-q")
            paths = ("skills/product-analysis/manifest.json",
                     "diagnostic-complet/workflows/analysis-methods.v1.json",
                     "skills/business-analysis/manifest.json",
                     "skills/business-analysis/references/economics-and-financing.md")
            for name in paths:
                dest = repo / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes((ROOT / name).read_bytes())
            git("add", ".")
            git("commit", "-qm", "Methods only")
            no_registry = git("rev-parse", "HEAD")

            name = "contracts/s3-direct-routing.v1.json"
            registry = json.loads((ROOT / name).read_bytes())
            registry["version"] = "1.0.31"
            path = repo / name
            path.parent.mkdir()
            path.write_text(json.dumps(registry), encoding="utf-8")
            git("add", name)
            git("commit", "-qm", "Pinned registry")
            pinned = git("rev-parse", "HEAD")

            # Neither a newer checkout nor an uncommitted file is the mandate's authority.
            path.write_text(json.dumps({**registry, "version": "1.0.99"}), encoding="utf-8")
            git("add", name)
            git("commit", "-qm", "Different registry")
            path.write_text("{}", encoding="utf-8")
            self.mandate["revision"] = self.revision = pinned
            plan = self.routing.make_plan(repo, self.mandate)
            with self.subTest("pinned version and receipt"):
                self.assertEqual(plan["version"], "1.0.31")
                self.assertEqual(plan["registry_sha256"], self.routing.digest(registry))
                self.assertEqual(self.routing.verify_receipt(repo, plan, self.receipt(plan))["status"],
                                 "receipt_checked")
            with self.subTest("missing registry"):
                self.mandate["revision"] = no_registry
                with self.assertRaisesRegex(ValueError, "routing registry.*revision"):
                    self.routing.make_plan(repo, self.mandate)

            with self.subTest("duplicate registry keys"):
                path.write_text('{"version": "1.0.31", ' + json.dumps(registry)[1:], encoding="utf-8")
                git("add", name)
                git("commit", "-qm", "Duplicate registry key")
                self.mandate["revision"] = git("rev-parse", "HEAD")
                with self.assertRaisesRegex(ValueError, "duplicate JSON key: version"):
                    self.routing.make_plan(repo, self.mandate)

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
