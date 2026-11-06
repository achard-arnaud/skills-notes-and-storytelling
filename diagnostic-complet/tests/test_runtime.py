import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("diagnostic_runtime", ROOT / "runtime.py")
runtime = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runtime)


def fixture():
    return {
        "id": "TEST", "mandate": {"question": "Pourquoi intervenir ?", "scope": "Site synthétique", "audience": "COO"},
        "pillars": [{"id": "P-DATA", "title": "Data", "scope": "Mesures"}],
        "sources": [{"id": "S1", "kind": "primary_research", "access": "read", "qualified": True, "title": "Fixture", "locator": "synthetic:1"}],
        "fragments": [{"id": "F1", "source_id": "S1", "locator": "synthetic:1", "text": "Signal observé"}],
        "claims": [{"id": "C1", "text": "Signal à examiner", "status": "supplied_claim", "fragment_ids": ["F1"], "pillar_ids": ["P-DATA"]}],
        "relations": [],
        "sections": [{"id": "SEC1", "title": "Constat", "claim_ids": ["C1"], "pillar_ids": ["P-DATA"],
                      "paragraphs": [{"id": "PAR1", "text": "Un signal appelle une enquête.", "claim_ids": ["C1"], "pillar_ids": ["P-DATA"], "review": {"evidence": False, "editorial": False}}]}],
        "side_stories": [{"id": "SS1", "kind": "analytical_focus", "title": "Mesurer", "claim_ids": ["C1"], "pillar_ids": ["P-DATA"], "parent_section_id": "SEC1", "return_to": "PAR1", "state": "candidate", "reason_outside": "Explication technique", "payoff": "Interpréter le signal", "text": "Complément."}],
    }


class ImportTests(unittest.TestCase):
    def test_deterministic_source_hash_exact_line_slices(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source.md"
            raw = b"# Title\r\n\r\nFirst paragraph.\r\nSecond line.\r\n\r\n## Next\r\n\r\nFinal."
            path.write_bytes(raw)
            first = runtime.import_markdown(path, "X")
            self.assertEqual(first, runtime.import_markdown(path, "X"))
            self.assertEqual(first["sources"][0]["text"].encode(), raw)
            self.assertEqual(first["sources"][0]["sha256"], runtime.hashlib.sha256(raw).hexdigest())
            for fragment in first["fragments"]:
                lines = first["sources"][0]["text"].splitlines(keepends=True)
                self.assertEqual(fragment["text"], "".join(lines[fragment["line_start"] - 1:fragment["line_end"]]))
            self.assertTrue(runtime.validate_study(first)["valid"])
            self.assertTrue(all(c["status"] == "supplied_claim" for c in first["claims"]))
            self.assertEqual(len(first["sections"]), 2)

    def test_fence_heading_not_interpreted_as_section(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source.md"
            path.write_text("# Header\n\n```mermaid\n# not a heading\n\nA-->B\n```\n", encoding="utf-8")
            study = runtime.import_markdown(path, "X")
            self.assertEqual(len(study["sections"]), 1)
            self.assertEqual(len(study["sections"][0]["paragraphs"]), 1)
            self.assertIn("# not a heading", study["fragments"][-1]["text"])

    def test_source_tampering_and_fragment_locator_tampering_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source.md"
            path.write_text("One.\n", encoding="utf-8")
            study = runtime.import_markdown(path, "X")
            study["sources"][0]["text"] = "Two.\n"
            errors = runtime.validate_study(study)["errors"]
            self.assertTrue(any("sha256" in x for x in errors))
            self.assertTrue(any("line slice" in x for x in errors))


class ValidationTests(unittest.TestCase):
    def test_structural_validity_separate_from_editorial_gaps(self):
        result = runtime.validate_study(fixture())
        self.assertTrue(result["valid"])
        self.assertTrue(any("editorial review pending" in x for x in result["gaps"]))

    def test_unique_ids_across_entity_types(self):
        study = fixture()
        study["pillars"][0]["id"] = "C1"
        self.assertTrue(any("duplicate id: C1" in x for x in runtime.validate_study(study)["errors"]))

    def test_unknown_references_and_missing_mandate(self):
        study = fixture()
        del study["mandate"]["question"]
        study["claims"][0]["fragment_ids"] = ["unknown"]
        result = runtime.validate_study(study)
        self.assertFalse(result["valid"])
        self.assertTrue(any("mandate.question" in x for x in result["errors"]))
        self.assertTrue(any("unknown reference" in x for x in result["errors"]))

    def test_verified_fact_rejects_supplied_or_unread_evidence(self):
        study = fixture()
        claim = study["claims"][0]
        claim.update(status="verified_fact", verification={"reviewed": True, "source_ids": ["S1"], "note": "Synthetic review"})
        study["sources"][0]["kind"] = "supplied_context"
        self.assertFalse(runtime.validate_study(study)["valid"])
        study["sources"][0]["kind"] = "primary_research"
        study["sources"][0]["access"] = "snippet"
        self.assertFalse(runtime.validate_study(study)["valid"])
        study["sources"][0]["access"] = "read"
        self.assertTrue(runtime.validate_study(study)["valid"])
        study["sources"][0]["qualified"] = False
        self.assertFalse(runtime.validate_study(study)["valid"])

    def test_verified_fact_requires_linked_fragment_and_review_note(self):
        study = fixture()
        study["claims"][0].update(status="verified_fact", verification={"reviewed": True, "source_ids": ["S1"], "note": "Reviewed"})
        study["claims"][0]["fragment_ids"] = []
        self.assertFalse(runtime.validate_study(study)["valid"])
        study["claims"][0]["fragment_ids"] = ["F1"]
        study["claims"][0]["verification"]["note"] = ""
        self.assertFalse(runtime.validate_study(study)["valid"])

    def test_hypothesis_can_have_no_fragments(self):
        study = fixture()
        study["claims"][0].update(status="hypothesis", fragment_ids=[])
        self.assertTrue(runtime.validate_study(study)["valid"])

    def test_side_return_lifecycle_payoff_dezoom(self):
        for update in ({"return_to": None}, {"state": "approved"}, {"state": "promoted", "payoff": ""}, {"kind": "dezoom"}):
            with self.subTest(update=update):
                study = fixture()
                study["side_stories"][0].update(update)
                self.assertFalse(runtime.validate_study(study)["valid"])
        study = fixture()
        study["side_stories"][0].update(kind="dezoom", scale_from="site", scale_to="portfolio", mechanism="Aggregation changes prioritization")
        self.assertTrue(runtime.validate_study(study)["valid"])
        study["side_stories"][0]["scale_to"] = "site"
        self.assertFalse(runtime.validate_study(study)["valid"])

    def test_paragraph_review_bound_to_current_text(self):
        study = fixture()
        paragraph = study["sections"][0]["paragraphs"][0]
        paragraph["review"] = {"evidence": True, "editorial": True, "text_sha256": runtime.text_hash(paragraph["text"])}
        self.assertTrue(runtime.validate_study(study)["valid"])
        paragraph["text"] += " Changed."
        self.assertTrue(any("stale" in x for x in runtime.validate_study(study)["errors"]))

    def test_relation_cannot_point_to_navigation_or_claim_causality(self):
        study = fixture()
        study["relations"] = [{"id": "R1", "from": "C1", "to": "SEC1", "kind": "causes", "rationale": "Unsupported"}]
        result = runtime.validate_study(study)
        self.assertFalse(result["valid"])
        self.assertTrue(any("reference a claim" in x for x in result["errors"]))
        self.assertTrue(any("relation kind" in x for x in result["errors"]))

    def test_duplicate_relation_tuple_rejected_even_with_distinct_ids(self):
        study = fixture()
        study["relations"] = [
            {"id": "R1", "from": "C1", "to": "C1", "kind": "contextualizes", "rationale": "First"},
            {"id": "R2", "from": "C1", "to": "C1", "kind": "contextualizes", "rationale": "Repeated"},
        ]
        self.assertTrue(any("duplicate relation" in x for x in runtime.validate_study(study)["errors"]))
        study["relations"][1]["kind"] = "compares"
        self.assertTrue(runtime.validate_study(study)["valid"])

    def test_paragraph_pillars_require_referenced_claim_relevance_without_quota(self):
        study = fixture()
        study["pillars"].append({"id": "P-INDUSTRY", "title": "Industrie", "scope": "Opérations"})
        paragraph = study["sections"][0]["paragraphs"][0]
        paragraph["pillar_ids"].append("P-INDUSTRY")
        self.assertTrue(any("not declared by referenced claims" in x for x in runtime.validate_study(study)["errors"]))
        study["claims"][0]["pillar_ids"].append("P-INDUSTRY")
        self.assertTrue(runtime.validate_study(study)["valid"])
        paragraph["pillar_ids"] = []
        self.assertTrue(runtime.validate_study(study)["valid"])

    def test_pillar_and_section_titles_nonempty(self):
        for target in ("pillars", "sections"):
            with self.subTest(target=target):
                study = fixture()
                study[target][0]["title"] = "  "
                self.assertTrue(any("title must be nonempty" in x for x in runtime.validate_study(study)["errors"]))

    def test_repository_synthetic_fixture_is_structurally_valid(self):
        study = json.loads((ROOT / "fixtures/synthetic.json").read_text(encoding="utf-8"))
        result = runtime.validate_study(study)
        self.assertTrue(result["valid"], result["errors"])

    def test_validation_does_not_mutate_or_promote(self):
        study = fixture()
        before = copy.deepcopy(study)
        runtime.validate_study(study)
        runtime.build_graph(study)
        self.assertEqual(study, before)

    def test_malformed_records_report_errors_instead_of_crashing(self):
        study = fixture()
        study["claims"][0]["status"] = []
        study["side_stories"][0].update(state={}, kind=[], parent_section_id={})
        study["relations"] = [{"id": "R1", "kind": {}, "from": [], "to": {}}]
        self.assertFalse(runtime.validate_study(study)["valid"])
        self.assertFalse(runtime.validate_study([])["valid"])

    def test_graph_has_only_evidence_nodes_and_relations(self):
        graph = runtime.build_graph(fixture())
        self.assertEqual({n["kind"] for n in graph["nodes"]}, {"source", "fragment", "claim"})
        self.assertEqual(len(graph["edges"]), 2)
        invalid = fixture()
        invalid["fragments"][0]["source_id"] = "MISSING"
        with self.assertRaises(ValueError):
            runtime.build_graph(invalid)

    def test_cli_import_validate_graph_and_invalid_exit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            md, out = root / "input.md", root / "study.json"
            md.write_text("# Test\n\nA supplied assertion.\n", encoding="utf-8")
            base = [sys.executable, str(ROOT / "runtime.py")]
            run = subprocess.run(base + ["import", str(md), "--study-id", "X", "--out", str(out)], capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(subprocess.run(base + ["validate", str(out)], capture_output=True).returncode, 0)
            self.assertEqual(subprocess.run(base + ["graph", str(out)], capture_output=True).returncode, 0)
            study = json.loads(out.read_text())
            study["claims"][0]["status"] = "verified_fact"
            out.write_text(json.dumps(study))
            self.assertEqual(subprocess.run(base + ["validate", str(out)], capture_output=True).returncode, 1)


if __name__ == "__main__":
    unittest.main()
