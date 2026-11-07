import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from writing import EVIDENCE_KEYS, apply_iterative as apply_revision, plan_iterative, prepare_from_scratch, text_hash, study_hash


def apply_iterative(study, *args, **kwargs):
    # Every application in these fixtures uses an explicit, just-read baseline lease.
    return apply_revision(study, *args, expected_baseline_hash=study_hash(study), **kwargs)


def sample():
    study = json.loads((ROOT / "fixtures/synthetic.json").read_text(encoding="utf-8"))
    # Avoid linking the independent C-3 branch to C-2 in this delta fixture.
    study["relations"] = []
    for section in study["sections"]:
        for paragraph in section["paragraphs"]:
            paragraph["review"] = {"evidence": True, "editorial": True, "text_sha256": text_hash(paragraph["text"])}
    return study


class WritingTests(unittest.TestCase):
    def test_fresh_rejects_prior_prose_container_without_accessing_its_value(self):
        class NoRead(dict):
            def __getitem__(self, key):
                if key == "sections":
                    raise AssertionError("old prose value was read")
                return super().__getitem__(key)
        evidence = NoRead(sample())
        with self.assertRaisesRegex(ValueError, "evidence-only"):
            prepare_from_scratch(evidence)

    def test_fresh_has_no_previous_reader_prose_and_no_automatic_fact_generation(self):
        study = sample()
        evidence = {key: study[key] for key in EVIDENCE_KEYS if key in study}
        before = copy.deepcopy(evidence)
        result = prepare_from_scratch(evidence)
        self.assertFalse(result["packet"]["reader_prose_loaded"])
        self.assertEqual("scaffold_candidate_not_drafted", result["packet"]["state"])
        self.assertEqual([], result["study"]["sections"][0]["paragraphs"])
        self.assertEqual([], result["study"]["side_stories"])
        self.assertEqual(before, evidence)
        self.assertEqual(evidence["claims"], result["study"]["claims"])
        self.assertEqual(1, len(result["study"]["sections"]))
        self.assertEqual(["C-1", "C-2", "C-3"], result["study"]["sections"][0]["claim_ids"])

    def test_fresh_topology_keeps_explicit_editorial_order_and_does_not_create_prose(self):
        study = sample()
        evidence = {key: study[key] for key in EVIDENCE_KEYS if key in study}
        scaffold = {"sections": [{"id": "Z", "title": "Question", "claim_ids": ["C-3"], "pillar_ids": ["corporate"]},
                                 {"id": "A", "title": "Contre-épreuve", "claim_ids": ["C-1"], "pillar_ids": ["data"]}]}
        result = prepare_from_scratch(evidence, scaffold)
        self.assertEqual(["Z", "A"], [s["id"] for s in result["study"]["sections"]])
        self.assertTrue(all(s["paragraphs"] == [] for s in result["study"]["sections"]))
        scaffold["sections"][0]["paragraphs"] = [{"text": "OLD PROSE"}]
        with self.assertRaisesRegex(ValueError, "prose"):
            prepare_from_scratch(evidence, scaffold)

    def test_fresh_rejects_old_reader_disguised_as_declared_source_kind(self):
        study = sample()
        evidence = {key: study[key] for key in EVIDENCE_KEYS if key in study}
        evidence["sources"][0]["kind"] = "prior_reader"
        with self.assertRaisesRegex(ValueError, "prior reader"):
            prepare_from_scratch(evidence)

    def test_fresh_rejects_unknown_scaffold_claim(self):
        study = sample()
        evidence = {key: study[key] for key in EVIDENCE_KEYS if key in study}
        with self.assertRaisesRegex(ValueError, "unknown claim"):
            prepare_from_scratch(evidence, {"sections": [{"id": "S", "claim_ids": ["missing"]}]})

    def test_source_delta_closes_to_fragment_claim_and_only_their_paragraph(self):
        plan = plan_iterative(sample(), ["SRC-1"])
        self.assertEqual(["C-1"], plan["claim_ids"])
        self.assertEqual(["P-1"], plan["paragraph_ids"])
        self.assertEqual(["S-1"], plan["section_ids"])

    def test_relation_dependency_direction_and_contradiction_are_explicit(self):
        study = sample()
        study["relations"] = [
            {"id": "REL-1", "from": "C-2", "to": "C-1", "kind": "depends_on"},
            {"id": "REL-2", "from": "C-2", "to": "C-3", "kind": "contradicts"},
        ]
        self.assertEqual(["C-1", "C-2", "C-3"], plan_iterative(study, ["C-1"])["claim_ids"])
        self.assertEqual(["C-2", "C-3"], plan_iterative(study, ["C-3"])["claim_ids"])

    def test_delta_preserves_unaffected_text_ids_and_evidence_exactly(self):
        study = sample()
        before = copy.deepcopy(study)
        result = apply_iterative(study, ["P-1"], {"P-1": "Texte révisé fourni par le rédacteur."})
        self.assertEqual(before, study)
        updated = result["study"]
        self.assertEqual(study["sections"][1:], updated["sections"][1:])
        for key in ("sources", "fragments", "claims", "relations", "pillars"):
            self.assertEqual(study[key], updated[key])
        paragraph = updated["sections"][0]["paragraphs"][0]
        self.assertEqual("P-1", paragraph["id"])
        self.assertFalse(paragraph["review"]["evidence"])
        self.assertFalse(paragraph["review"]["editorial"])
        self.assertEqual(text_hash(paragraph["text"]), paragraph["review"]["text_sha256"])
        self.assertIn("prose_changed", result["ledger"][0]["reasons"])

    def test_outside_delta_replacement_and_unknown_ids_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            apply_iterative(sample(), ["P-1"], {"P-3": "Unexpected unrelated rewrite"})
        with self.assertRaisesRegex(ValueError, "unknown changed"):
            plan_iterative(sample(), ["UNKNOWN"])
        with self.assertRaisesRegex(ValueError, "nonempty"):
            apply_iterative(sample(), ["P-1"], {"P-1": " "})

    def test_evidence_delta_invalidates_evidence_but_preserves_exact_unchanged_prose(self):
        study = sample()
        result = apply_iterative(study, ["SRC-1"])
        paragraph = result["study"]["sections"][0]["paragraphs"][0]
        self.assertEqual(study["sections"][0]["paragraphs"][0]["text"], paragraph["text"])
        self.assertFalse(paragraph["review"]["evidence"])
        self.assertTrue(paragraph["review"]["editorial"])

    def test_form_global_expands_section_peers_and_only_invalidates_shape(self):
        study = sample()
        peer = {"id": "P-PEER", "text": "Un autre paragraphe de la même section.", "claim_ids": ["C-2"], "pillar_ids": ["ai"]}
        peer["review"] = {"evidence": True, "editorial": True, "text_sha256": text_hash(peer["text"])}
        study["sections"][0]["paragraphs"].append(peer)
        self.assertEqual(["P-1"], plan_iterative(study, ["P-1"])["paragraph_ids"])
        result = apply_iterative(study, ["P-1"], form_global=True)
        self.assertEqual(["P-1", "P-PEER"], result["plan"]["paragraph_ids"])
        for paragraph in result["study"]["sections"][0]["paragraphs"]:
            self.assertTrue(paragraph["review"]["evidence"])
            self.assertFalse(paragraph["review"]["editorial"])
        self.assertEqual(study["sections"][1:], result["study"]["sections"][1:])

    def test_stale_text_review_is_invalidated(self):
        study = sample()
        study["sections"][0]["paragraphs"][0]["review"]["text_sha256"] = "old-hash"
        result = apply_iterative(study, ["P-1"])
        self.assertIn("stale_text_review", result["ledger"][0]["reasons"])
        self.assertFalse(result["study"]["sections"][0]["paragraphs"][0]["review"]["evidence"])

    def test_host_change_reopens_side_story_and_journal_is_append_only(self):
        study = sample()
        study["writing_ledger"] = [{"sequence": 1, "id": "OLD", "human_approval": False}]
        study["side_stories"][0]["state"] = "promoted"
        result = apply_iterative(study, ["P-3"], {"P-3": "Révision locale fournie, hypothèse inchangée."})
        self.assertEqual("candidate", result["study"]["side_stories"][0]["state"])
        self.assertEqual(study["writing_ledger"][0], result["study"]["writing_ledger"][0])
        self.assertTrue(all(row["sequence"] > 1 for row in result["ledger"]))
        self.assertTrue(all(row["human_approval"] is False for row in result["ledger"]))

    def test_unresolved_dependency_is_not_silently_ignored(self):
        study = sample()
        study["fragments"][0]["source_id"] = "missing"
        with self.assertRaisesRegex(ValueError, "unresolved dependency"):
            plan_iterative(study, ["C-1"])

    def test_apply_requires_expected_baseline_hash_and_rejects_stale_snapshot(self):
        study = sample()
        with self.assertRaises(TypeError):
            apply_revision(study, ["P-1"])
        with self.assertRaisesRegex(ValueError, "baseline content hash mismatch"):
            apply_revision(study, ["P-1"], expected_baseline_hash="stale-hash")
        before_hash = study_hash(study)
        study["claims"][0]["text"] = "Changed after planning"
        with self.assertRaisesRegex(ValueError, "baseline content hash mismatch"):
            apply_revision(study, ["C-1"], expected_baseline_hash=before_hash)

    def test_plan_records_baseline_identity_version_content_and_separate_reviews(self):
        study = sample()
        study["version"] = "candidate-v2"
        study["approval_state"] = {"human": "pending"}
        baseline = plan_iterative(study, ["P-1"])["baseline"]
        self.assertEqual(study["id"], baseline["study_id"])
        self.assertEqual("candidate-v2", baseline["declared_version"])
        self.assertEqual(study_hash(study), baseline["content_sha256"])
        self.assertEqual({"human": "pending"}, baseline["approval_state"])
        self.assertEqual(3, baseline["factual_reviewed_paragraphs"])
        self.assertEqual(3, baseline["editorial_reviewed_paragraphs"])


if __name__ == "__main__":
    unittest.main()
