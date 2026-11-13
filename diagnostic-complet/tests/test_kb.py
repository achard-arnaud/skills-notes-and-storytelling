import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("diagnostic_kb", ROOT / "kb.py")
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)


class KBTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.out = self.root / "private-kb"

    def tearDown(self):
        self.temp.cleanup()

    def source(self, name, text):
        path = self.root / name
        path.write_bytes(text.encode("utf-8"))
        return path

    def index(self):
        return json.loads((self.out / "kb.json").read_text())

    def test_exact_unicode_crlf_offsets_and_source_copy(self):
        text = "# Énergie\r\n\r\nGreenYellow mesure les données. Le PV reste une hypothèse.\r\n"
        source = self.source("source.md", text)
        result = kb.ingest_files([source], self.out)
        self.assertEqual(result["source_count"], 1)
        index = self.index()
        self.assertEqual((self.out / index["sources"][0]["copy_path"]).read_bytes(), source.read_bytes())
        for atom in index["atoms"]:
            for occurrence in atom["occurrences"]:
                self.assertEqual(text[occurrence["char_start"]:occurrence["char_end"]], occurrence["text"])
                self.assertEqual(text.encode()[occurrence["byte_start"]:occurrence["byte_end"]].decode(), occurrence["text"])
                self.assertGreaterEqual(occurrence["line_start"], 1)
        self.assertEqual(kb.validate_kb(index, self.out), [])
        self.assertEqual({a["status"] for a in index["atoms"]}, {"supplied_unverified"})
        self.assertEqual(result["coverage"]["input_characters"], len(text))
        self.assertEqual(result["coverage"]["unexplained_non_whitespace_characters"], 0)

    def test_structural_tables_code_not_falsely_atomic(self):
        source = self.source("blocks.md", "# Intro\n\n| A | B |\n| --- | --- |\n| 1 | 2 |\n\n```mermaid\nA-->B\n# not heading\n```\n")
        kb.ingest_files([source], self.out)
        atoms = self.index()["atoms"]
        self.assertEqual({a["kind"] for a in atoms}, {"heading", "table", "code"})
        self.assertTrue(all(not a["semantic_atomization"] for a in atoms))
        self.assertIn("# not heading", next(a for a in atoms if a["kind"] == "code")["text"])

    def test_question_directive_assertion_and_list_item_split(self):
        source = self.source("types.txt", "- Analysez les données.\n- Quel est le ROI ?\n- Le site est fictif; le résultat est inconnu.\n")
        kb.ingest_files([source], self.out)
        kinds = [a["kind"] for a in self.index()["atoms"]]
        self.assertIn("directive", kinds)
        self.assertIn("question", kinds)
        self.assertEqual(kinds.count("assertion"), 2)

    def test_numbered_list_marker_not_a_standalone_assertion(self):
        source = self.source("numbered.md", "1. Analysez les données.\n2. Quel est le ROI ?\n")
        kb.ingest_files([source], self.out)
        atoms = self.index()["atoms"]
        self.assertEqual(len(atoms), 2)
        self.assertEqual({a["kind"] for a in atoms}, {"directive", "question"})

    def test_normalized_dedup_preserves_all_exact_occurrences(self):
        first = self.source("first.md", "Les données sont fournies.\n")
        second = self.source("second.md", "LES  DONNÉES sont fournies.\n")
        kb.ingest_files([first, second], self.out)
        index = self.index()
        self.assertEqual(len(index["sources"]), 2)
        self.assertEqual(len(index["atoms"]), 1)
        self.assertEqual(len(index["atoms"][0]["occurrences"]), 2)
        self.assertNotEqual(index["atoms"][0]["occurrences"][0]["text"], index["atoms"][0]["occurrences"][1]["text"])
        self.assertEqual(kb.validate_kb(index, self.out), [])

    def test_idempotent_repeat_byte_identical_outputs(self):
        first = self.source("first.md", "# Sujet\n\nUne hypothèse. Une question ?\n")
        kb.ingest_files([first], self.out)
        before = {p.name: p.read_bytes() for p in self.out.glob("*.json")}
        result = kb.ingest_files([first], self.out)
        self.assertEqual(result["added_sources"], 0)
        self.assertEqual(result["added_atoms"], 0)
        self.assertEqual(result["added_occurrences"], 0)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.out.glob("*.json")})

    def test_incremental_new_source_retains_old_and_adds_version(self):
        first = self.source("first.md", "Version initiale.\n")
        kb.ingest_files([first], self.out)
        old_source = self.index()["sources"][0]
        old_atom = self.index()["atoms"][0]["id"]
        first.write_text("Version modifiée.\n", encoding="utf-8")
        kb.ingest_files([first], self.out)
        index = self.index()
        self.assertEqual(len(index["sources"]), 2)
        self.assertIn(old_atom, {a["id"] for a in index["atoms"]})
        self.assertEqual(len(index["versions"]), 1)
        self.assertEqual(index["versions"][0]["supersedes"], old_source["id"])
        self.assertEqual((self.out / old_source["copy_path"]).read_text(), "Version initiale.\n")

    def test_identical_source_alias_preserves_locations(self):
        first = self.source("first.md", "Une occurrence.\n")
        second = self.source("copy.md", "Une occurrence.\n")
        kb.ingest_files([first], self.out)
        kb.ingest_files([second], self.out)
        index = self.index()
        self.assertEqual(len(index["sources"]), 1)
        self.assertEqual(len(index["atoms"]), 1)
        self.assertEqual(len(index["atoms"][0]["occurrences"]), 1)
        self.assertEqual(len(index["atoms"][0]["occurrences"][0]["locators"]), 2)

    def test_reverting_source_creates_explicit_sequence_not_silent_overwrite(self):
        source = self.source("version.md", "Version one.\n")
        kb.ingest_files([source], self.out)
        source.write_text("Version two.\n", encoding="utf-8")
        kb.ingest_files([source], self.out)
        source.write_text("Version one.\n", encoding="utf-8")
        kb.ingest_files([source], self.out)
        index = self.index()
        self.assertEqual(len(index["sources"]), 2)
        self.assertEqual([v["sequence"] for v in index["versions"]], [1, 2])
        before = (self.out / "kb.json").read_bytes()
        kb.ingest_files([source], self.out)
        self.assertEqual(before, (self.out / "kb.json").read_bytes())

    def test_keywords_candidate_only_explicit_entities_no_name_guess(self):
        gy = kb.load_profile(Path(__file__).resolve().parents[1] / "profiles" / "greenyellow.profile.json")
        pillars, entities = kb.classify("GreenYellow compare un PV avec une étude de VisioSense. Alice dirige demain.", gy)
        self.assertTrue(any(p["id"] == "industry" for p in pillars))
        self.assertEqual({p["status"] for p in pillars}, {"candidate_keyword"})
        self.assertEqual({e["id"] for e in entities}, {"ENTITY-greenyellow", "ENTITY-photovoltaic", "ENTITY-visiosense"})
        self.assertEqual(kb.classify("privation et diversion", gy)[0], [])
        # Build default is the neutral profile: no run vocabulary at all.
        self.assertEqual(kb.classify("GreenYellow compare un PV avec VisioSense"), ([], []))

    def test_graph_integrity_and_no_causal_assertion(self):
        source = self.source("data.md", "GreenYellow utilise des données PV.\n")
        kb.ingest_files([source], self.out)
        graph = json.loads((self.out / "graph.json").read_text())
        ids = {n["id"] for n in graph["nodes"]}
        self.assertTrue(all(e["from"] in ids and e["to"] in ids for e in graph["edges"]))
        self.assertEqual(len({e["id"] for e in graph["edges"]}), len(graph["edges"]))
        self.assertNotIn("causes", {e["kind"] for e in graph["edges"]})
        self.assertIn("derived_from", {e["kind"] for e in graph["edges"]})

    def test_no_private_corpus_in_git_repository(self):
        source = self.source("data.md", "Private material.\n")
        repo = self.root / "repo"
        repo.mkdir()
        (repo / ".git").mkdir()
        with self.assertRaisesRegex(ValueError, "outside every Git"):
            kb.ingest_files([source], repo / "private-kb")

    def test_private_git_destination_requires_explicit_caller_opt_in(self):
        source = self.source("data.md", "Private material.\n")
        repo = self.root / "private-repo"
        repo.mkdir()
        (repo / ".git").mkdir()
        result = kb.ingest_files([source], repo / "kb", allow_private_git=True)
        self.assertEqual(result["source_count"], 1)
        self.assertTrue(result["destination_policy"]["under_git"])
        self.assertIn("not verified", result["destination_policy"]["visibility_verification"])

    def test_public_method_repository_always_refused_even_with_opt_in(self):
        source = self.source("data.md", "Private material.\n")
        target = ROOT / "must-not-be-created-private-kb"
        with self.assertRaisesRegex(ValueError, "public business method repository"):
            kb.ingest_files([source], target, allow_private_git=True)
        self.assertFalse(target.exists())

    def test_corrupted_preserved_source_stops_incremental(self):
        source = self.source("data.md", "Source initiale.\n")
        kb.ingest_files([source], self.out)
        copy_path = self.out / self.index()["sources"][0]["copy_path"]
        copy_path.write_text("Tampered")
        with self.assertRaisesRegex(ValueError, "corrupt"):
            kb.ingest_files([source], self.out)

    def test_zip_must_be_extracted_before_intake(self):
        source = self.source("untrusted.zip", "Not a Markdown file")
        with self.assertRaisesRegex(ValueError, "extracted Markdown"):
            kb.ingest_files([source], self.out)

    def test_concurrent_writer_refused_and_lock_cleared_on_failure(self):
        source = self.source("data.md", "Source.\n")
        self.out.mkdir()
        (self.out / ".ingest.lock").write_text("other")
        with self.assertRaisesRegex(ValueError, "writer already active"):
            kb.ingest_files([source], self.out)
        (self.out / ".ingest.lock").unlink()
        source.write_bytes(b"\xff")
        with self.assertRaises(UnicodeError):
            kb.ingest_files([source], self.out)
        self.assertFalse((self.out / ".ingest.lock").exists())

    def test_version_mismatch_requires_explicit_migration(self):
        source = self.source("data.md", "Source.\n")
        kb.ingest_files([source], self.out)
        index = self.index()
        index["lexicon_version"] = "future"
        (self.out / "kb.json").write_text(json.dumps(index))
        with self.assertRaisesRegex(ValueError, "migration"):
            kb.ingest_files([source], self.out)

    def test_tampered_offsets_rejected(self):
        source = self.source("data.md", "Source.\n")
        kb.ingest_files([source], self.out)
        index = self.index()
        index["atoms"][0]["occurrences"][0]["char_start"] = 2
        self.assertTrue(any("offset mismatch" in e for e in kb.validate_kb(index, self.out)))

    def test_tampered_identity_and_line_rejected(self):
        source = self.source("data.md", "Source.\n")
        kb.ingest_files([source], self.out)
        index = self.index()
        index["atoms"][0]["id"] = "ATOM-forged"
        index["atoms"][0]["occurrences"][0]["line_start"] = 999
        errors = kb.validate_kb(index, self.out)
        self.assertTrue(any("atom identity" in e for e in errors))
        self.assertTrue(any("line mismatch" in e for e in errors))

    def test_cli_receipt_and_atom_markdown_frontmatter(self):
        source = self.source("data.md", "# Test\n\nUne phrase.\n")
        result = subprocess.run([sys.executable, str(ROOT / "kb.py"), str(source), "--out", str(self.out)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        receipt = json.loads(result.stdout)
        self.assertEqual(receipt["atom_count"], 2)
        atom_files = list((self.out / "atoms").glob("*.md"))
        self.assertEqual(len(atom_files), 2)
        self.assertTrue(all(p.read_text().startswith("---\n") for p in atom_files))


if __name__ == "__main__":
    unittest.main()
