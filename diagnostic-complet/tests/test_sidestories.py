import copy
import importlib.util
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location("diag_" + name, ROOT / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


runtime = load("runtime")
render = load("render")
sidestories = load("sidestories")
WORKFLOW = json.loads((ROOT / "workflows/side-stories.workflow.json").read_text(encoding="utf-8"))
REGISTRY = json.loads((ROOT / "workflows/kb-examples.json").read_text(encoding="utf-8"))
CANDIDATES = json.loads((ROOT / "workflows/side-stories.candidates.json").read_text(encoding="utf-8"))


def base_study(side):
    return {
        "id": "T", "mandate": {"question": "Pourquoi ?", "scope": "Synthétique", "audience": "COO"},
        "pillars": [{"id": "P-DATA", "title": "Data", "scope": "Mesures"}],
        "sources": [{"id": "S1", "kind": "primary_research", "access": "read", "qualified": True, "title": "F", "locator": "synthetic:1"}],
        "fragments": [{"id": "F1", "source_id": "S1", "locator": "synthetic:1", "text": "Signal"}],
        "claims": [{"id": "C1", "text": "Signal à examiner", "status": "supplied_claim", "fragment_ids": ["F1"], "pillar_ids": ["P-DATA"]}],
        "relations": [],
        "sections": [{"id": "SEC1", "title": "Constat", "claim_ids": ["C1"], "pillar_ids": ["P-DATA"],
                      "paragraphs": [{"id": "PAR1", "text": "Un signal appelle une enquête.", "claim_ids": ["C1"], "pillar_ids": ["P-DATA"], "review": {"evidence": False, "editorial": False}}]}],
        "side_stories": [side],
    }


def common(kind, state="promoted"):
    return {"id": "SS1", "kind": kind, "title": "Encart", "claim_ids": ["C1"], "pillar_ids": ["P-DATA"],
            "parent_section_id": "SEC1", "return_to": "PAR1", "state": state, "reason_outside": "Hors tronc",
            "payoff": "Mieux comprendre", "problematique": "Que change ce mécanisme ?",
            "bridge": {"in": "Le tronc établit un signal.", "out": "On revient au signal."}}


def lines():
    roles = ["headline", "offer", "model", "client_problem", "fact", "fact", "fact", "differentiation", "limit", "personal_reading", "implication", "sources"]
    out = []
    for i, role in enumerate(roles):
        line = {"role": role, "text": f"Ligne {i + 1} du pitch synthétique."}
        if role == "fact":
            line.update(date="2026-01-01", source="https://example.org/page")
        out.append(line)
    return out


def item(n):
    return {"term": f"Notion {n}",
            "definition": {"text": "Définition synthétique.", "source": {"author": "A. Auteur", "year": "2024", "venue_or_url": "Revue synthétique"}, "evidence_level": "peer_reviewed"},
            "example": "Exemple général.", "in_practice": "Dans le passage SEC1, la notion cadre le signal.",
            "contrast": "Anti-thèse rapide.", "perspective": {"mode": "synthesis", "content": "Première phrase. Seconde phrase."}}


VALID = {
    "veille_corporate_perso": lambda: {"payload": {"lines": lines()}},
    "veille_academique": lambda: {"payload": {"items": [item(n) for n in range(5)]}},
    "dezoom": lambda: {"scale_from": "site", "scale_to": "portefeuille", "mechanism": "Agrégation",
                       "payload": {"steps": [{"scale": "site", "statement": "Constat local."}, {"scale": "portefeuille", "statement": "Canal de transmission."}, {"scale": "site", "statement": "Gain local."}]}},
    "comparator": lambda: {"criterion": "Contrôle des données", "confounders": ["taille"], "takeaway": "Les conditions diffèrent.",
                           "payload": {"table": {"columns": ["Acteur", "Critère"], "rows": [["A", "x"], ["B", "y"], ["C", "z"]]}}},
    "illustration": lambda: {"payload": {"form": "use_case", "text": "Un cas d'usage synthétique."}},
    "analytical_focus": lambda: {"payload": {"analysis": {
        "core_question": "Pourquoi ?", "thesis": "Parce que.", "takeaway": "Donc.",
        "positions": [{"position": "A", "caveat": "limite A"}, {"position": "B", "caveat": "limite B"}],
        "mechanisms": [{"mechanism": "Canal", "evidence_status": "inference"}]}}},
}


def study_for(kind, state="promoted", **patch):
    side = {**common(kind, state), **VALID[kind]()}
    side.update(patch)
    return base_study(side)


class WorkflowTests(unittest.TestCase):
    def test_workflow_file_is_consistent(self):
        self.assertEqual([], sidestories.workflow_errors(WORKFLOW))

    def test_six_types_with_unique_visible_tags(self):
        self.assertEqual(6, len(WORKFLOW["types"]))
        self.assertEqual(len(WORKFLOW["types"]), len({t["tag"] for t in WORKFLOW["types"]}))
        self.assertEqual({"VCP", "VAC"}, {t["tag"] for t in WORKFLOW["types"]} & {"VCP", "VAC"})

    def test_type_colors_avoid_evidence_status_hues(self):
        # green/orange/red are reserved for verified/inference/unknown (color_policy)
        for t in WORKFLOW["types"]:
            for token in t["color"].values():
                r, g, b = (int(token[i:i + 2], 16) for i in (1, 3, 5))
                self.assertFalse(g > r + 25 and g > b + 25, f"{t['id']} reads green")
                self.assertFalse(r > g + 60 and r > b + 60, f"{t['id']} reads red or orange")

    def test_workflow_errors_detect_broken_references(self):
        broken = copy.deepcopy(WORKFLOW)
        broken["legacy_kind_map"]["x"] = "unknown_type"
        broken["pillar_routing"]["P-DATA"]["types"].append("nope")
        broken["types"][1]["tag"] = broken["types"][0]["tag"]
        errors = sidestories.workflow_errors(broken)
        self.assertEqual(3, len(errors), errors)

    def test_every_pillar_is_routed_with_problematiques_and_bridges(self):
        pillars = re.findall(r"\| (P-[A-Z]+) \|", (ROOT / "docs/PILLARS.md").read_text(encoding="utf-8"))
        self.assertEqual(8, len(pillars))
        self.assertEqual(set(pillars), set(WORKFLOW["pillar_routing"]))

    def test_runtime_vocabulary_is_derived_from_workflow(self):
        self.assertEqual(set(WORKFLOW["legacy_kind_map"]) | {t["id"] for t in WORKFLOW["types"]}, runtime.SIDE_KINDS)


class FormatTests(unittest.TestCase):
    def test_valid_side_story_of_each_type_passes_when_promoted(self):
        for kind in VALID:
            with self.subTest(kind=kind):
                result = runtime.validate_study(study_for(kind))
                self.assertEqual([], result["errors"])

    def test_candidate_without_payload_is_a_gap_not_an_error(self):
        for kind in VALID:
            with self.subTest(kind=kind):
                study = study_for(kind, "candidate")
                study["side_stories"][0].pop("payload")
                result = runtime.validate_study(study)
                self.assertTrue(result["valid"], result["errors"])
                self.assertTrue(any("payload" in g for g in result["gaps"]))

    def test_promoted_without_problematique_or_bridge_is_refused(self):
        for key in ("problematique", "bridge"):
            with self.subTest(key=key):
                study = study_for("illustration")
                study["side_stories"][0].pop(key)
                result = runtime.validate_study(study)
                self.assertFalse(result["valid"])

    def test_vcp_line_count_roles_and_fact_provenance(self):
        cases = {
            "nine lines": lambda p: p.update(lines=[l for l in p["lines"] if l["role"] not in ("model", "client_problem", "differentiation")]),
            "sixteen lines": lambda p: p["lines"].extend({"role": "fact", "text": "x", "date": "d", "source": "s"} for _ in range(4)),
            "two headlines": lambda p: p["lines"].__setitem__(1, {"role": "headline", "text": "Autre accroche."}),
            "headline not first": lambda p: p["lines"].insert(0, p["lines"].pop(1)),
            "no limit": lambda p: [l.update(role="offer") for l in p["lines"] if l["role"] == "limit"],
            "fact without source": lambda p: [l.pop("source") for l in p["lines"] if l["role"] == "fact"][:1],
            "line too long": lambda p: p["lines"][1].update(text="mot " * 40),
        }
        for name, mutate in cases.items():
            with self.subTest(name=name):
                study = study_for("veille_corporate_perso")
                mutate(study["side_stories"][0]["payload"])
                self.assertFalse(runtime.validate_study(study)["valid"], name)

    def test_vcp_count_rule_alone_rejects_nine_and_sixteen_lines(self):
        for n, message in ((9, "at least 10"), (16, "at most 15")):
            with self.subTest(n=n):
                study = study_for("veille_corporate_perso")
                keep = [l for l in study["side_stories"][0]["payload"]["lines"] if l["role"] not in ("model", "client_problem", "differentiation")]
                filler = {"role": "offer", "text": "Ligne de remplissage."}
                study["side_stories"][0]["payload"]["lines"] = keep + [dict(filler) for _ in range(n - len(keep))] if n > len(keep) else keep
                result = runtime.validate_study(study)
                self.assertTrue(any(message in e for e in result["errors"]), result["errors"])

    def test_vac_lexicon_size_structure_and_sources(self):
        cases = {
            "four items": lambda p: p["items"].pop(),
            "eight items": lambda p: p["items"].extend(item(n) for n in range(3)),
            "missing contrast": lambda p: p["items"][0].pop("contrast"),
            "definition without source": lambda p: p["items"][0]["definition"].pop("source"),
            "bad evidence level": lambda p: p["items"][0]["definition"].update(evidence_level="trust_me"),
            "synthesis of three sentences": lambda p: p["items"][0]["perspective"].update(content="Un. Deux. Trois."),
            "unknown perspective mode": lambda p: p["items"][0]["perspective"].update(mode="essay"),
        }
        for name, mutate in cases.items():
            with self.subTest(name=name):
                study = study_for("veille_academique")
                mutate(study["side_stories"][0]["payload"])
                self.assertFalse(runtime.validate_study(study)["valid"], name)

    def test_vac_table_perspective_is_not_word_limited(self):
        study = study_for("veille_academique")
        study["side_stories"][0]["payload"]["items"][0]["perspective"] = {"mode": "table", "content": "| a | b |\n" * 80}
        self.assertTrue(runtime.validate_study(study)["valid"])

    def test_other_types_reject_incomplete_payloads(self):
        cases = {
            "dezoom": lambda s: s["payload"]["steps"].pop(),
            "comparator": lambda s: s["payload"]["table"]["columns"].extend(["c3", "c4", "c5", "c6"]),
            "illustration": lambda s: s["payload"].update(form="quote", text="Une citation sans attribution."),
            "analytical_focus": lambda s: s["payload"]["analysis"]["positions"].pop(),
        }
        for kind, mutate in cases.items():
            with self.subTest(kind=kind):
                study = study_for(kind)
                mutate(study["side_stories"][0])
                self.assertFalse(runtime.validate_study(study)["valid"], kind)

    def test_comparator_row_width_must_match_columns(self):
        study = study_for("comparator")
        study["side_stories"][0]["payload"]["table"]["rows"][0] = ["seule cellule"]
        self.assertFalse(runtime.validate_study(study)["valid"])


class LegacyAndRenderTests(unittest.TestCase):
    def test_legacy_kinds_remain_valid_with_a_gap_naming_the_replacement(self):
        for old, new in WORKFLOW["legacy_kind_map"].items():
            with self.subTest(old=old):
                study = base_study({**common("illustration", "candidate"), "kind": old})
                result = runtime.validate_study(study)
                self.assertTrue(result["valid"], result["errors"])
                self.assertTrue(any(f"use {new}" in g for g in result["gaps"]))

    def test_legacy_kind_is_not_held_to_the_new_payload_format_when_promoted(self):
        study = base_study({**common("illustration", "promoted"), "kind": "portrait"})
        self.assertTrue(runtime.validate_study(study)["valid"])

    def test_unknown_kind_is_still_refused(self):
        study = base_study({**common("illustration", "candidate"), "kind": "essay"})
        self.assertFalse(runtime.validate_study(study)["valid"])

    def test_render_shows_the_visible_tag_and_its_css(self):
        html = render.render_study(study_for("veille_academique", "candidate"))
        self.assertIn('class="tag tag-VAC"', html)
        self.assertIn("[VAC]", html)
        self.assertIn(".tag-VCP{", html)
        self.assertNotIn("http://", html.replace("http://www.w3.org", ""))


class KbExamplesTests(unittest.TestCase):
    ATOM = re.compile(r"^ATOM-[0-9a-f]{64}$")

    def test_every_workflow_example_exists_in_the_registry(self):
        known = {e["id"] for e in REGISTRY["examples"]}
        for t in WORKFLOW["types"]:
            self.assertTrue(set(t["examples"]) <= known, t["id"])
            self.assertTrue(1 <= len(t["examples"]) <= 3, f"{t['id']}: one to three examples")

    def test_registry_holds_only_opaque_pointers(self):
        for e in REGISTRY["examples"]:
            for atom in e["atoms"]:
                self.assertRegex(atom, self.ATOM)
            self.assertIn(e["status"], REGISTRY["privacy"]["statuses"])
            if not e["atoms"]:
                self.assertIn(e["status"], {"to_ingest", "to_collect", "research_required", "to_confirm"}, e["id"])
            else:
                self.assertIn(e["status"], {"supplied_unverified", "research_required"}, e["id"])
            self.assertLess(len(e["topic"]) + len(e["role"]) + len(e["note"]), 420, f"{e['id']} reads like copied corpus text")

    def test_public_files_do_not_leak_private_paths_or_corpus_fields(self):
        blob = (ROOT / "workflows/kb-examples.json").read_text(encoding="utf-8")
        for forbidden in ("/home/user/private", "greenyellow-corpus", "occurrence_ids", "sha256"):
            self.assertNotIn(forbidden, blob)


SKILLS = ROOT / "skills"
PILLAR_SKILLS = {
    "P-MARKET": "analyzing-market-and-competition", "P-INDUSTRY": "analyzing-industry-value-chain",
    "P-CORPORATE": "analyzing-corporate-functions", "P-DATA": "analyzing-data-foundations",
    "P-AI": "analyzing-ai-capabilities", "P-ECONOMICS": "analyzing-economics-and-financing",
    "P-GOVERNANCE": "analyzing-governance-and-control", "P-ADOPTION": "analyzing-adoption-and-change",
}


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert match, f"{path}: frontmatter required"
    fields = dict(re.findall(r"^(\w+): (.*)$", match.group(1), re.M))
    return fields, text[match.end():]


class SkillFamilyTests(unittest.TestCase):
    def test_ten_skills_exist_and_each_pillar_has_its_skill(self):
        names = {d.name for d in SKILLS.iterdir() if d.is_dir()}
        self.assertEqual(set(PILLAR_SKILLS.values()) | {"side-stories-business", "designing-main-story"}, names)
        self.assertEqual(set(PILLAR_SKILLS), set(WORKFLOW["pillar_routing"]))

    def test_frontmatter_name_matches_folder_and_body_is_bounded(self):
        for d in SKILLS.iterdir():
            fields, body = frontmatter(d / "SKILL.md")
            self.assertEqual(d.name, fields["name"])
            self.assertGreater(len(fields["description"]), 120, d.name)
            self.assertLess(len(body.splitlines()), 500, d.name)

    def test_pillar_skill_routes_exactly_the_workflow_types_with_existing_references(self):
        for pillar, name in PILLAR_SKILLS.items():
            _, body = frontmatter(SKILLS / name / "SKILL.md")
            routed = set(re.findall(r"`\[(?:[A-Z]{2,3})\]` `([a-z_]+)`", body))
            self.assertEqual(set(WORKFLOW["pillar_routing"][pillar]["types"]), routed, name)
            for t in routed:
                self.assertTrue((SKILLS / "side-stories-business/references/types" / f"{t}.md").exists(), f"{name}:{t}")
            for problem in WORKFLOW["pillar_routing"][pillar]["problematiques"]:
                self.assertIn(problem, body, name)
            for bridge in WORKFLOW["pillar_routing"][pillar]["bridges"]:
                self.assertIn(bridge, body, name)
            self.assertIn("renderer-packet.md", body)
            self.assertIn(f"({pillar})", body)

    def test_every_skill_has_kb_pointers_that_mirror_the_registry(self):
        registry = {e["id"]: e for e in REGISTRY["examples"]}
        for d in SKILLS.iterdir():
            data = json.loads((d / "examples/kb-pointers.json").read_text(encoding="utf-8"))
            self.assertEqual(d.name, data["skill"])
            self.assertTrue(data["examples"], d.name)
            if d.name in PILLAR_SKILLS.values():
                self.assertIn(len(data["examples"]), (1, 2), d.name)
            for entry in data["examples"]:
                self.assertEqual(registry[entry["id"]], entry, f"{d.name}:{entry['id']} drifted from the registry")

    def test_each_type_reference_lists_its_workflow_examples_and_a_valid_skeleton(self):
        for spec in WORKFLOW["types"]:
            path = SKILLS / "side-stories-business/references/types" / f"{spec['id']}.md"
            text = path.read_text(encoding="utf-8")
            self.assertIn(f"Tag `{spec['tag']}`", text)
            for ex in spec["examples"]:
                self.assertIn(ex, text, f"{spec['id']} reference must discuss {ex}")
            blocks = [json.loads(b) for b in re.findall(r"```json\n(.*?)\n```", text, re.S)]
            skeletons = [b for b in blocks if "payload" in b]
            self.assertTrue(skeletons, spec["id"])
            for skeleton in skeletons:
                with self.subTest(kind=spec["id"]):
                    study = base_study({**common(spec["id"]), **skeleton})
                    result = runtime.validate_study(study)
                    self.assertEqual([], result["errors"])

    def test_renderer_packet_example_carries_every_declared_field(self):
        text = (SKILLS / "side-stories-business/references/renderer-packet.md").read_text(encoding="utf-8")
        packet = json.loads(re.findall(r"```json\n(.*?)\n```", text, re.S)[0])
        self.assertEqual(set(WORKFLOW["renderer_packet"]["fields"]), set(packet))

    def test_every_skill_has_evals_in_skill_creator_layout(self):
        for d in SKILLS.iterdir():
            cases = [c for c in (d / "evals").iterdir() if c.is_dir()]
            self.assertTrue(cases, d.name)
            for c in cases:
                self.assertTrue((c / "prompt.md").exists() and (c / "case.yaml").exists(), c)
                self.assertTrue(list((c / "graders").glob("*.md")), c)
                self.assertIn(f"name: {c.name}", (c / "case.yaml").read_text(encoding="utf-8"))
                self.assertRegex(c.name, r"^[a-z][a-z0-9-]*$")

    def test_skills_never_contain_private_paths_or_corpus_markers(self):
        for path in SKILLS.rglob("*"):
            if path.is_file():
                blob = path.read_text(encoding="utf-8")
                for forbidden in ("/home/user/private", "greenyellow-corpus", "occurrence_ids", "OCC-"):
                    self.assertNotIn(forbidden, blob, f"{path}: {forbidden}")

    def test_single_source_of_truth_is_cited_by_the_orchestrating_skill(self):
        _, body = frontmatter(SKILLS / "side-stories-business/SKILL.md")
        self.assertIn("workflows/side-stories.workflow.json", body)
        for spec in WORKFLOW["types"]:
            self.assertIn(f"`{spec['id']}`", body)


class CandidateInventoryTests(unittest.TestCase):
    def setUp(self):
        self.items = CANDIDATES["candidates"]
        self.registry = {e["id"]: e for e in REGISTRY["examples"]}
        self.types = {t["id"] for t in WORKFLOW["types"]}

    def test_all_nine_original_candidates_are_rewritten_and_new_ones_added(self):
        origins = [c["origin"] for c in self.items]
        self.assertEqual(9, sum(o.startswith("inventaire initial") for o in origins))
        self.assertGreaterEqual(len(self.items), 15)
        self.assertEqual(len(self.items), len({c["id"] for c in self.items}))

    def test_each_candidate_can_help_a_choice(self):
        for c in self.items:
            with self.subTest(id=c["id"]):
                for key in ("title", "objective", "problematique", "choice_criterion", "gaps"):
                    self.assertTrue(c[key].strip(), key)
                self.assertTrue(c["bridge"]["in"].strip() and c["bridge"]["out"].strip())
                self.assertIn(c["type"], self.types)
                self.assertIn(c["alternative"]["type"], self.types)
                self.assertNotEqual(c["type"], c["alternative"]["type"])
                self.assertTrue(c["alternative"]["when"].strip())
                self.assertTrue(set(c["pillar_ids"]) <= set(WORKFLOW["pillar_routing"]))
                self.assertIn(c["readiness"], CANDIDATES["readiness_values"])

    def test_candidate_pillars_accept_the_chosen_type_or_state_why(self):
        for c in self.items:
            with self.subTest(id=c["id"]):
                routed = {t for p in c["pillar_ids"] for t in WORKFLOW["pillar_routing"][p]["types"]}
                self.assertIn(c["type"], routed, f"{c['id']}: no pillar of the candidate routes to {c['type']}")

    def test_examples_exist_and_readiness_matches_their_status(self):
        for c in self.items:
            with self.subTest(id=c["id"]):
                for ex in c["examples"]:
                    self.assertIn(ex, self.registry)
                if c["readiness"] in ("to_collect", "to_ingest", "research_required", "to_confirm") and c["examples"]:
                    statuses = {self.registry[e]["status"] for e in c["examples"]}
                    self.assertTrue(statuses & {"to_collect", "to_ingest", "research_required", "to_confirm"}, c["id"])
                if c["readiness"] == "supported":
                    self.assertTrue(c["examples"] == [] or all(self.registry[e]["atoms"] for e in c["examples"]), c["id"])

    def test_nothing_is_validated_by_an_agent(self):
        self.assertEqual("candidate", CANDIDATES["lifecycle"])
        self.assertIn("humain", CANDIDATES["human_gate"])
        first = CANDIDATES["suggested_first_wave"]
        self.assertIn("non validée", first["status"])
        by_id = {c["id"]: c for c in self.items}
        for ident in first["ids"]:
            self.assertIn(by_id[ident]["readiness"], ("supported", "partial"), ident)


if __name__ == "__main__":
    unittest.main()
