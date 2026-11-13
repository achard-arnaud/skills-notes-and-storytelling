"""Run/build separation and one terminology. Regression guards for RF-01..RF-04 (docs/REFACTOR-BACKLOG.md)."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import kb  # noqa: E402
import ontology  # noqa: E402
import runtime  # noqa: E402

PROFILES = ROOT / "profiles"
GY = kb.load_profile(PROFILES / "greenyellow.profile.json")
SYNTH = kb.load_profile(PROFILES / "synthetic-logistics.profile.json")
NEUTRAL = kb.load_profile(PROFILES / "neutral.profile.json")
TERM = json.loads((ROOT / "ontology" / "terminology.json").read_text(encoding="utf-8"))
# Core code and referentials: everything except profiles/, tests/ and run records under runs/.
CORE_FILES = sorted(p for p in ROOT.glob("*.py")) + sorted((ROOT / "ontology").glob("*.json")) + [ROOT / "ontology" / "terminology.json"]


def run_terms(profile: dict) -> set[str]:
    """Distinctive run vocabulary: entity titles and aliases of 7+ characters, plus the namespace leaf."""
    terms = set()
    for record in profile["entity_lexicon"].values():
        terms.update(a.lower() for a in [record["title"], *record["aliases"]] if len(a) >= 7)
    if profile.get("projection"):
        terms.add(Path(profile["projection"]["namespace"]).name.lower())
    return terms


class ProfileSeparationTests(unittest.TestCase):
    def test_golden_greenyellow_classification_is_unchanged(self):
        """The GreenYellow profile must reproduce the lexicon 1.0.0 used for the published corpus."""
        golden = json.loads((ROOT / "fixtures" / "profiles" / "classify-golden-greenyellow.json").read_text(encoding="utf-8"))
        for case in golden:
            pillars, entities = kb.classify(case["text"], GY)
            self.assertEqual(pillars, case["pillars"], case["text"])
            self.assertEqual(entities, case["entities"], case["text"])

    def test_neutral_profile_carries_no_run_vocabulary(self):
        self.assertEqual(NEUTRAL["pillar_lexicon"], {})
        self.assertEqual(NEUTRAL["entity_lexicon"], {})
        self.assertIsNone(NEUTRAL["projection"])

    def test_core_code_contains_no_run_vocabulary(self):
        terms = run_terms(GY)
        offenders = []
        for path in CORE_FILES:
            text = path.read_text(encoding="utf-8").lower()
            offenders += [f"{path.relative_to(ROOT)}: {t}" for t in sorted(terms) if t in text]
        self.assertEqual(offenders, [], "run vocabulary leaked into build code or referentials")

    def test_synthetic_profile_is_isolated_from_greenyellow(self):
        _, entities = kb.classify("La Fictive Logistique SA gère un entrepôt et une flotte de livraison. GreenYellow est absent.", SYNTH)
        self.assertEqual([e["id"] for e in entities], ["ENTITY-fictive-logistics"])
        self.assertTrue(run_terms(SYNTH).isdisjoint(run_terms(GY)))

    def test_one_kb_one_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "note.md"
            src.write_text("Fictive Logistique SA gère un entrepôt.\n", encoding="utf-8")
            out = Path(tmp) / "kb"
            kb.ingest_files([src], out, profile=SYNTH)
            with self.assertRaises(ValueError):
                kb.ingest_files([src], out, profile=GY)
            self.assertEqual(json.loads((out / "kb.json").read_text(encoding="utf-8"))["profile_id"], "synthetic-logistics")

    def test_projection_requires_a_namespace(self):
        from project import ProjectionError  # noqa: WPS433
        import project
        with self.assertRaises(ProjectionError):
            project.project(ROOT, "0" * 64, {}, namespace=None)

    def test_profile_rejects_namespace_outside_business_area(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "p.json"
            bad.write_text(json.dumps({**NEUTRAL, "projection": {"namespace": "canonical/x"}}), encoding="utf-8")
            with self.assertRaises(kb.ProfileError):
                kb.load_profile(bad)


class AgentsMandatesTests(unittest.TestCase):
    """RF-21: the sub-project AGENTS.md must keep the mandates other sessions depend on (D34)."""

    def test_agents_keeps_its_mandates(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        for needle in ("Mandat courant R2", "Mandat éditorial", "Périmètre léger", "Dix skills éditoriaux", "Un agent ne marque jamais une side story `validated`"):
            self.assertIn(needle, text)


class TerminologyTests(unittest.TestCase):
    def test_runtime_statuses_come_from_terminology(self):
        self.assertEqual(runtime.STATUSES, set(TERM["claim_statuses"]))

    def test_ontology_facets_match_terminology(self):
        onto = ontology.load()
        self.assertEqual(onto["facets"]["knowledge_status"]["values"], TERM["knowledge_status"]["values"])
        self.assertEqual(onto["facets"]["validation"]["values"], TERM["validation_states"])
        self.assertNotIn("evidence_basis", onto["facets"])

    def test_kind_is_the_only_source_term(self):
        self.assertNotIn("source_tiers", TERM)
        self.assertNotIn("legacy_source_kind_to_tier", TERM)
        self.assertIn("tier", TERM["retired_terms"])  # recorded as retired, not as a term in use

    def test_eligibility_follows_claim_statuses(self):
        for kind, spec in TERM["source_kinds"].items():
            self.assertEqual(spec["verified_fact_eligible"], "verified_fact" in spec["may_back"], kind)
            self.assertTrue(set(spec["may_back"]) <= set(TERM["claim_statuses"]), kind)

    def test_vendor_and_corporate_kinds_never_eligible(self):
        self.assertFalse(TERM["source_kinds"]["primary_vendor"]["verified_fact_eligible"])
        self.assertFalse(TERM["source_kinds"]["primary_corporate"]["verified_fact_eligible"])

    def test_crosswalk_documentary_status_is_the_kb_status(self):
        self.assertEqual(TERM["documentary_status"], kb.DOCUMENTARY_STATUS)
        self.assertEqual(TERM["crosswalk"]["supplied"]["knowledge_status"], "SOURCE")


class VerifiedKindRegressionTests(unittest.TestCase):
    """RF-04 and RF-10, kind-only (#287): a vendor or corporate declaration never backs a verified fact."""

    def _study(self):
        from test_runtime import fixture  # same synthetic fixture as the runtime suite
        study = fixture()
        study["claims"][0].update(status="verified_fact", verification={"reviewed": True, "source_ids": ["S1"], "note": "Synthetic review"})
        study["sources"][0].update(access="read", qualified=True, kind="primary_research")
        return study

    def test_vendor_and_corporate_kinds_rejected_even_qualified(self):
        for kind in ("primary_vendor", "primary_corporate", "primary", "supplied_context"):
            study = self._study()
            study["sources"][0]["kind"] = kind
            self.assertFalse(runtime.validate_study(study)["valid"], kind)

    def test_eligible_kinds_accepted(self):
        for kind in ("primary_research", "primary_official", "measured_internal"):
            study = self._study()
            study["sources"][0]["kind"] = kind
            self.assertTrue(runtime.validate_study(study)["valid"], kind)

    def test_unqualified_eligible_kind_rejected(self):
        study = self._study()
        study["sources"][0]["qualified"] = False
        self.assertFalse(runtime.validate_study(study)["valid"])

    def test_attributed_claim_needs_an_attributable_kind(self):
        study = self._study()
        study["claims"][0]["status"] = "attributed_claim"
        study["claims"][0].pop("verification", None)
        study["sources"][0]["kind"] = "primary_corporate"
        self.assertTrue(runtime.validate_study(study)["valid"])
        study["sources"][0]["kind"] = "supplied_context"
        self.assertFalse(runtime.validate_study(study)["valid"])
