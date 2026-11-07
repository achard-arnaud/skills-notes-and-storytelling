import copy
import json
import unittest
from pathlib import Path

import ontology
from ontology import OntologyError, analyze, check_edge, classify_node, load, validate_referential

ONTO = load()
RULES = {rule["id"]: rule for rule in ONTO["edge_rules"]}


def atom(nid, kind, label="texte"):
    return {"id": nid, "type": "atom", "kind": kind, "label": label}


def graph(nodes, edges=()):
    return {"nodes": list(nodes), "edges": list(edges)}


def derived(eid, source, target):
    return {"id": eid, "from": source, "to": target, "kind": "derived_from"}


class ReferentialTests(unittest.TestCase):
    def test_referential_loads_and_aligns_with_canonical_catalogue(self):
        self.assertEqual(ONTO["ontology_id"], "business-kb-ontology")
        probatory = {r["id"] for r in ONTO["edge_rules"] if r["id"] not in ontology.STRUCTURAL_RULES}
        self.assertEqual(len(probatory), 12)

    def test_unknown_type_in_edge_rule_is_rejected(self):
        broken = copy.deepcopy(ONTO)
        broken["edge_rules"][0]["domain"] = ["evidence.unknown"]
        with self.assertRaises(OntologyError):
            validate_referential(broken)

    def test_missing_canonical_relation_is_rejected(self):
        broken = copy.deepcopy(ONTO)
        broken["edge_rules"] = [r for r in broken["edge_rules"] if r["id"] != "enables"]
        with self.assertRaises(OntologyError):
            validate_referential(broken)

    def test_threshold_without_calibration_is_rejected(self):
        broken = copy.deepcopy(ONTO)
        broken["review_triggers"][2]["threshold"] = 50
        with self.assertRaises(OntologyError):
            validate_referential(broken)

    def test_alias_policy_cannot_apply_or_approve(self):
        broken = copy.deepcopy(ONTO)
        broken["alias_policy"]["action"] = "merge"
        with self.assertRaises(OntologyError):
            validate_referential(broken)


class ClassificationTests(unittest.TestCase):
    def test_every_observed_kb_kind_has_a_class(self):
        expected = {"assertion": "assertion.fact", "question": "assertion.question",
                    "directive": "instruction.directive", "heading": "structure.heading",
                    "code": "structure.code", "table": "structure.table"}
        for kind, cls in expected.items():
            self.assertEqual(classify_node(atom("A", kind), ONTO), cls)

    def test_unknown_kind_is_unclassified_not_guessed(self):
        self.assertEqual(classify_node(atom("A", "poem"), ONTO), "unclassified")

    def test_proof_projection_node_without_type_is_unclassified(self):
        self.assertEqual(classify_node({"id": "C1", "kind": "claim"}, ONTO), "unclassified")


class EdgeCheckTests(unittest.TestCase):
    def test_heading_cannot_support_a_fact(self):
        status, _ = check_edge({"kind": "supports"}, "structure.heading", "assertion.fact", RULES)
        self.assertEqual(status, "domain_range")

    def test_directive_cannot_be_classified_into_a_pillar(self):
        status, _ = check_edge({"kind": "candidate_classification", "status": "candidate_keyword"},
                               "instruction.directive", "analysis.pillar", RULES)
        self.assertEqual(status, "domain_range")

    def test_causes_requires_evidence(self):
        cause = {"kind": "causes"}
        self.assertEqual(check_edge(cause, "assertion.fact", "assertion.fact", RULES)[0], "evidence_missing")
        cited = {"kind": "causes", "evidence": ["EV-1"]}
        self.assertEqual(check_edge(cited, "assertion.fact", "assertion.fact", RULES)[0], "ok")

    def test_derived_from_from_source_to_directive_is_allowed(self):
        self.assertEqual(check_edge({"kind": "derived_from"}, "evidence.source", "instruction.directive", RULES)[0], "ok")

    def test_proof_projection_edge_is_out_of_ontology_not_violation(self):
        report = analyze(graph([atom("A1", "assertion"), {"id": "S1", "type": "source", "kind": "source"}],
                               [{"id": "E1", "from": "S1", "to": "A1", "kind": "source_of"}]))
        self.assertEqual(report["out_of_ontology"]["count"], 1)
        self.assertEqual(report["violations"]["count"], 0)


class AnalysisTests(unittest.TestCase):
    def test_structural_atoms_are_excluded_from_semantic_density(self):
        nodes = [atom("H1", "heading"), atom("H2", "heading"), atom("F1", "assertion"), atom("F2", "assertion")]
        report = analyze(graph(nodes, [{"id": "R1", "from": "F1", "to": "F2", "kind": "supports", "evidence": ["x"]}]))
        self.assertEqual(report["class_counts"]["structure.heading"], 2)
        self.assertEqual(report["semantic_nodes"], 2)
        self.assertEqual(report["semantic_density"]["numerator"], 1)
        self.assertFalse(report["semantic_density"]["is_quality_score"])

    def test_empty_and_single_graph_have_no_division_by_zero(self):
        for nodes in ([], [atom("F1", "assertion")]):
            self.assertEqual(analyze(graph(nodes))["semantic_density"]["value"], 0.0)

    def test_analysis_never_mutates_inputs(self):
        g = graph([atom("F1", "assertion"), atom("F2", "assertion")],
                  [{"id": "R1", "from": "F1", "to": "F2", "kind": "causes"}])
        before = copy.deepcopy(g)
        analyze(g, recent_ids=["F1"], previous={"ontology": {"semantic_nodes": 1}})
        self.assertEqual(g, before)


class TriggerTests(unittest.TestCase):
    def test_no_recent_material_means_no_fired_trigger(self):
        report = analyze(graph([atom("F1", "assertion")]))
        fired = [t["fired"] for t in report["review_triggers"] if t["id"] != "cadence_semantic"]
        self.assertEqual(fired, [False, False])

    def test_recent_directive_fires_its_trigger(self):
        report = analyze(graph([atom("D1", "directive")]), recent_ids=["D1"])
        trig = next(t for t in report["review_triggers"] if t["id"] == "directive_in_material")
        self.assertTrue(trig["fired"])

    def test_cadence_is_measured_only_without_target(self):
        report = analyze(graph([atom("F1", "assertion"), atom("F2", "assertion")]), previous={"ontology": {"semantic_nodes": 1}})
        cadence = next(t for t in report["review_triggers"] if t["id"] == "cadence_semantic")
        self.assertIsNone(cadence["threshold"])
        self.assertIsNone(cadence["fired"])
        self.assertEqual(cadence["measured_delta"], 1)

    def test_hil_touched_requires_hil_linked_to_pillar(self):
        nodes = [atom("F1", "assertion"), {"id": "P1", "type": "pillar", "kind": "candidate_pillar"},
                 {"id": "Q1", "type": "hil", "kind": "hil"}]
        edges = [{"id": "E1", "from": "F1", "to": "P1", "kind": "candidate_classification", "status": "candidate_keyword"},
                 {"id": "E2", "from": "Q1", "to": "P1", "kind": "addresses_pillar"}]
        report = analyze(graph(nodes, edges), recent_ids=["F1"])
        trig = next(t for t in report["review_triggers"] if t["id"] == "hil_touched")
        self.assertTrue(trig["fired"])


class AliasCandidateTests(unittest.TestCase):
    def _two_sources(self, same_source=False):
        nodes = [{"id": "S1", "type": "source", "kind": "source"},
                 {"id": "S2", "type": "source", "kind": "source"},
                 atom("F1", "assertion", "Le budget est validé."),
                 atom("F2", "assertion", "le  budget est VALIDÉ.")]
        second = "S1" if same_source else "S2"
        edges = [derived("D1", "S1", "F1"), derived("D2", second, "F2")]
        return graph(nodes, edges)

    def test_same_text_in_two_sources_is_a_candidate_never_applied(self):
        report = analyze(self._two_sources())
        self.assertEqual(report["alias_candidates"]["count"], 1)
        cand = report["alias_candidates"]["sample"][0]
        self.assertEqual(cand["action"], "none")
        self.assertIs(cand["candidate_approval"], False)

    def test_same_text_in_one_source_is_not_an_alias_candidate(self):
        self.assertEqual(analyze(self._two_sources(same_source=True))["alias_candidates"]["count"], 0)


class FixtureContractTests(unittest.TestCase):
    """Each fixture in fixtures/onto is a case with an expected outcome."""
    FIX = Path(__file__).resolve().parents[1] / "fixtures" / "onto"

    def test_positive_and_negative_fixtures_match_expected_outcomes(self):
        expected = json.loads((self.FIX / "expected.json").read_text(encoding="utf-8"))
        for case in expected["cases"]:
            g = json.loads((self.FIX / case["graph"]).read_text(encoding="utf-8"))
            report = analyze(g, recent_ids=case.get("recent_ids", []))
            with self.subTest(case=case["id"]):
                self.assertEqual(report["violations"]["count"], case["violations"])
                self.assertEqual(report["unclassified"]["count"], case["unclassified"])
                self.assertEqual(report["alias_candidates"]["count"], case["alias_candidates"])
                fired = sorted(t["id"] for t in report["review_triggers"] if t["fired"])
                self.assertEqual(fired, sorted(case["fired"]))


class ContractConsistencyTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_skill_contract_names_every_fixture_eval(self):
        expected = json.loads((self.ROOT / "fixtures" / "onto" / "expected.json").read_text(encoding="utf-8"))
        contract = (self.ROOT / "docs" / "REINFORCE-KB-SKILL-CONTRACT.md").read_text(encoding="utf-8")
        for case in expected["cases"]:
            with self.subTest(case=case["id"]):
                self.assertIn("`" + case["id"] + "`", contract)

    def test_ontology_doc_states_no_threshold_without_calibration(self):
        text = (self.ROOT / "docs" / "ONTOLOGY.md").read_text(encoding="utf-8")
        self.assertIn("cadence_semantic", text)
        self.assertIn("aucun", text.lower())


class LoopbackIntegrationTests(unittest.TestCase):
    def test_loopback_report_exposes_ontology_without_changing_existing_metrics(self):
        from loopback import analyze_graph
        g = graph([atom("H1", "heading"), atom("F1", "assertion"), atom("F2", "assertion")],
                  [{"id": "R1", "from": "F1", "to": "F2", "kind": "causes"}])
        report = analyze_graph(g)
        self.assertIn("ontology", report)
        self.assertEqual(report["metrics"]["nodes"], 3)
        self.assertEqual(report["ontology"]["violations"]["count"], 1)
        self.assertEqual(report["ontology"]["violations"]["sample"][0]["status"], "evidence_missing")
        self.assertFalse(report["automatic_mutations"])


if __name__ == "__main__":
    unittest.main()
