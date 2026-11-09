from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from loopback import analyze_graph, main


def proof_graph():
    return {"nodes": [{"id": "s", "kind": "source"}, {"id": "f", "kind": "fragment"},
                      {"id": "c", "kind": "claim", "pillar_ids": ["data"]}],
            "pillars": [{"id": "data", "title": "Data"}],
            "edges": [{"id": "e1", "from": "s", "to": "f", "kind": "source_of"},
                      {"id": "e2", "from": "f", "to": "c", "kind": "evidence_for"}]}


class LoopbackTests(unittest.TestCase):
    def test_density_uses_unique_directed_nonself_pairs(self):
        graph = proof_graph()
        graph["edges"] += [dict(graph["edges"][0], id="duplicate"),
                           {"id": "parallel", "from": "s", "to": "f", "kind": "references"},
                           {"id": "loop", "from": "c", "to": "c", "kind": "references"}]
        report = analyze_graph(graph)
        self.assertAlmostEqual(report["metrics"]["directed_density"], 2 / 6)
        self.assertEqual(report["metrics"]["density_numerator"], 2)
        self.assertEqual(report["findings"]["duplicate_edges"]["count"], 1)
        self.assertEqual(report["findings"]["self_loops"]["count"], 1)
        self.assertFalse(report["metrics"]["density_is_quality_score"])

    def test_empty_and_single_graph_no_division_by_zero(self):
        for nodes in ([], [{"id": "a", "kind": "atom"}]):
            report = analyze_graph({"nodes": nodes, "edges": []})
            self.assertEqual(report["metrics"]["directed_density"], 0)
            self.assertEqual(report["decision"], "no_change")

    def test_analyzer_never_mutates_graph_or_recent_list(self):
        graph = proof_graph()
        recent = ["c"]
        original = deepcopy(graph)
        analyze_graph(graph, recent_ids=recent)
        self.assertEqual(graph, original)
        self.assertEqual(recent, ["c"])

    def test_source_fragment_claim_counts_and_pillar_projection(self):
        report = analyze_graph(proof_graph())
        self.assertEqual(report["metrics"]["node_types"], {"source": 1, "fragment": 1, "claim": 1})
        self.assertEqual(report["pillar_coverage"]["pillars"][0]["members"], 1)
        self.assertFalse(any(c["kind"] == "pillar_review" for c in report["review_candidates"]))

    def test_atom_source_pillar_alias_shape_and_recent_edge(self):
        graph = {"nodes": [{"id": "s", "type": "source"}, {"id": "a", "type": "atom"},
                           {"id": "p", "type": "pillar"}],
                 "edges": [{"id": "e", "source": "a", "target": "s", "type": "derived_from"},
                           {"id": "m", "source": "a", "target": "p", "type": "in_pillar"}]}
        report = analyze_graph(graph, ["e"])
        self.assertEqual(report["pillar_coverage"]["touched_by_recent_material"], ["p"])
        self.assertEqual(report["pillar_coverage"]["pillars"][0]["members"], 1)
        self.assertTrue(any(c["kind"] == "pillar_review" for c in report["review_candidates"]))

    def test_new_material_triggers_review_without_density_threshold(self):
        graph = proof_graph()
        old = analyze_graph(graph)
        recent = analyze_graph(graph, ["c"], old)
        self.assertEqual(recent["delta"]["directed_density"], 0)
        candidate = next(c for c in recent["review_candidates"] if c["kind"] == "pillar_review")
        self.assertEqual(candidate["hypothesis"]["status"], "unverified")
        self.assertFalse(candidate["review"]["human_approval"])

    def test_documentary_kb_content_kind_is_not_structural_node_type(self):
        graph = {"nodes": [{"id": "s", "type": "source", "kind": "source"},
                           {"id": "a", "type": "atom", "kind": "assertion"},
                           {"id": "p", "type": "pillar", "kind": "candidate_pillar"},
                           {"id": "e", "type": "entity", "kind": "entity"}],
                 "edges": [{"id": "provenance", "from": "s", "to": "a", "kind": "derived_from"},
                           {"id": "classification", "from": "a", "to": "p", "kind": "candidate_classification", "status": "candidate_keyword"},
                           {"id": "mention", "from": "a", "to": "e", "kind": "explicit_mention"}]}
        report = analyze_graph(graph, ["a"])
        self.assertEqual(report["metrics"]["node_types"]["atom"], 1)
        self.assertEqual(report["metrics"]["node_subtypes"]["atom:assertion"], 1)
        self.assertEqual(report["findings"]["unknown_node_types"], [])
        self.assertEqual(report["findings"]["unknown_edge_types"], [])
        self.assertEqual(report["pillar_coverage"]["pillars"][0]["candidate_members"], 1)
        self.assertEqual(report["pillar_coverage"]["touched_by_recent_material"], ["p"])

    def test_unprojected_pillars_are_unknown_not_zero_quality(self):
        graph = proof_graph()
        graph.pop("pillars")
        graph["nodes"][2].pop("pillar_ids")
        report = analyze_graph(graph, ["f"])
        self.assertEqual(report["pillar_coverage"]["status"], "not_projected")
        self.assertEqual(report["pillar_coverage"]["uncategorized_recent"]["items"], ["f"])

    def test_invalid_references_duplicates_and_bad_records(self):
        graph = proof_graph()
        graph["nodes"] += [{"id": "c", "kind": "claim"}, {}, None]
        graph["nodes"][2]["pillar_ids"] = ["missing"]
        graph["edges"] += [{"id": "e1", "from": "ghost", "to": "c", "kind": "supports"}, None]
        report = analyze_graph(graph)
        self.assertEqual(report["findings"]["duplicate_node_ids"]["count"], 1)
        self.assertEqual(report["findings"]["duplicate_edge_ids"]["count"], 1)
        self.assertEqual(report["findings"]["invalid_references"]["count"], 2)
        self.assertEqual(report["findings"]["malformed_nodes"]["count"], 2)
        self.assertEqual(report["findings"]["invalid_pillar_references"]["count"], 1)
        self.assertEqual(report["metrics"]["density_numerator"], 2)

    def test_compaction_preserves_identity_and_lineage_as_proposal(self):
        graph = {"nodes": [{"id": "one", "kind": "atom", "label": "  SAME words "},
                           {"id": "two", "kind": "atom", "text": "same WORDS"}], "edges": []}
        report = analyze_graph(graph)
        self.assertEqual(report["findings"]["matching_text_groups"]["count"], 1)
        candidate = report["review_candidates"][0]
        self.assertIn("preserve all original IDs", candidate["proposal"])
        self.assertIn("homonym counterexample", candidate["test"])
        self.assertFalse(report["automatic_mutations"])
        self.assertFalse(report["automatic_promotion"])

    def test_type_mismatch_and_unknown_type_require_review(self):
        graph = proof_graph()
        graph["nodes"].append({"id": "x", "kind": "unregistered"})
        graph["edges"] += [{"id": "wrong", "from": "c", "to": "s", "kind": "source_of"},
                           {"id": "newtype", "from": "x", "to": "c", "kind": "magic_cause"}]
        report = analyze_graph(graph, ["x"])
        self.assertEqual(report["findings"]["endpoint_type_mismatches"]["count"], 1)
        self.assertEqual(report["findings"]["unknown_node_types"], ["unregistered"])
        self.assertEqual(report["findings"]["unknown_edge_types"], ["magic_cause"])

    def test_at_most_three_candidates_one_corrective(self):
        graph = proof_graph()
        graph["nodes"] += [{"id": "extra", "kind": "new_type", "label": "same"},
                           {"id": "extra2", "kind": "new_type", "label": "same"}]
        graph["edges"].append({"from": "missing", "to": "extra", "kind": "unknown"})
        report = analyze_graph(graph, ["extra"])
        self.assertEqual(len(report["review_candidates"]), 3)
        self.assertEqual(report["deferred_candidates"], 1)
        self.assertLessEqual(sum(c["corrective_candidate"] for c in report["review_candidates"]), 1)
        self.assertEqual(report["budgets"]["repairs_per_blocker_max"], 2)

    def test_details_are_bounded_but_counts_complete(self):
        graph = {"nodes": [{"id": f"a-{i}", "kind": "atom"} for i in range(25)], "edges": []}
        report = analyze_graph(graph)
        self.assertEqual(report["findings"]["isolated_nodes"]["count"], 25)
        self.assertEqual(len(report["findings"]["isolated_nodes"]["items"]), 20)
        self.assertTrue(report["findings"]["isolated_nodes"]["truncated"])

    def test_previous_graph_reports_numeric_delta_without_quality_inference(self):
        old = {"nodes": [{"id": "s", "kind": "source"}], "edges": []}
        report = analyze_graph(proof_graph(), previous=old)
        self.assertEqual(report["delta"]["nodes"], 2)
        self.assertIn("no quality", report["delta"]["meaning"])

    def test_unknown_recent_does_not_invent_pillar_review(self):
        report = analyze_graph(proof_graph(), ["not-present"])
        self.assertEqual(report["findings"]["unknown_recent_ids"]["count"], 1)
        self.assertFalse(any(c["kind"] == "pillar_review" for c in report["review_candidates"]))

    def test_cli_writes_report_without_touching_input(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "graph.json"
            out = Path(directory) / "report.json"
            raw = json.dumps(proof_graph())
            path.write_text(raw)
            self.assertEqual(main([str(path), "--recent-id", "c", "--output", str(out)]), 0)
            self.assertEqual(path.read_text(), raw)
            self.assertFalse(json.loads(out.read_text())["automatic_mutations"])

    def test_invalid_shape_rejected(self):
        for graph in ([], {}, {"nodes": {}, "edges": []}):
            with self.assertRaises(ValueError):
                analyze_graph(graph)
        with self.assertRaises(ValueError):
            analyze_graph(proof_graph(), "c")


if __name__ == "__main__":
    unittest.main()
