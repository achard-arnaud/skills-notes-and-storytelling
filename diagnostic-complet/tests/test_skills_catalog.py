import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import skills_catalog as sc  # noqa: E402


class CatalogDataTests(unittest.TestCase):
    def test_twelve_unique_atomic_operations(self):
        names = [s["name"] for s in sc.SKILLS]
        self.assertEqual(len(names), 12)
        self.assertEqual(len(set(names)), 12)

    def test_every_module_exists_and_answers_help(self):
        for module in sorted({s["module"] for s in sc.SKILLS}):
            with self.subTest(module=module):
                self.assertTrue((ROOT / module).exists())
                rc = subprocess.run([sys.executable, "-B", str(ROOT / module), "--help"], capture_output=True).returncode
                self.assertEqual(rc, 0)

    def test_every_operation_has_exclusion_forbid_and_negative(self):
        for s in sc.SKILLS:
            with self.subTest(skill=s["name"]):
                self.assertTrue(s["exclude"] and s["forbid"] and s["negative"] and s["steps"])

    def test_published_catalog_equals_generated_catalog(self):
        published = (ROOT / "docs" / "SKILLS-CATALOG.md").read_text(encoding="utf-8")
        self.assertEqual(published, sc.catalog_markdown())


class DraftTests(unittest.TestCase):
    def test_drafts_lint_clean_outside_the_repo(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(sc.main(["drafts", "--out", tmp]), 0)
            self.assertEqual(sc.lint(Path(tmp)), [])

    def test_drafts_refuse_the_public_repository(self):
        self.assertEqual(sc.main(["drafts", "--out", str(sc.REPO / "diagnostic-complet" / "skills-out")]), 2)

    def test_lint_flags_missing_exclusion_and_unknown_module(self):
        with tempfile.TemporaryDirectory() as tmp:
            sc.main(["drafts", "--out", tmp])
            bad = Path(tmp) / "kb-ingest" / "SKILL.md"
            bad.write_text(bad.read_text(encoding="utf-8").replace("Exclure", "Sauf").replace("kb.py", "ghost.py"), encoding="utf-8")
            errors = sc.lint(Path(tmp))
        self.assertTrue(any("exclusion" in e for e in errors))
        self.assertTrue(any("existing module" in e for e in errors))

    def test_lint_flags_missing_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            sc.main(["drafts", "--out", tmp])
            import shutil
            shutil.rmtree(Path(tmp) / "reader-render")
            self.assertIn("reader-render: missing", sc.lint(Path(tmp)))


if __name__ == "__main__":
    unittest.main()
