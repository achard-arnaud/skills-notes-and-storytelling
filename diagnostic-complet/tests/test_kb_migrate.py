import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import kb  # noqa: E402
import kb_migrate  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "profiles" / "neutral.profile.json"


class KbMigrateTests(unittest.TestCase):
    """Synthetic KB only: no test reads a private corpus (D25)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)
        self.note = base / "note.md"
        self.note.write_text("# Note synthétique\n\nUne phrase de test.\n", encoding="utf-8")
        self.kb = base / "kb"
        kb.ingest_files([self.note], self.kb, profile=PROFILE)
        self.backup = base / "backup"
        index = json.loads((self.kb / "kb.json").read_text(encoding="utf-8"))
        del index["profile_id"]
        (self.kb / "kb.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def test_ingestion_refuses_then_accepts_after_migration(self):
        other = Path(self.tmp.name) / "other.md"
        other.write_text("# Autre\n\nAutre phrase.\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            kb.ingest_files([other], self.kb, profile=PROFILE)
        result = kb_migrate.migrate(self.kb, PROFILE, self.backup, Path(self.tmp.name) / "receipt.json", apply=True)
        self.assertTrue(result["applied"])
        out = kb.ingest_files([other], self.kb, profile=PROFILE)
        self.assertEqual(out["added_sources"], 1)

    def test_dry_run_changes_nothing(self):
        before = (self.kb / "kb.json").read_bytes()
        result = kb_migrate.migrate(self.kb, PROFILE)
        self.assertFalse(result["applied"])
        self.assertEqual(result["action"], "declare_profile_id")
        self.assertEqual((self.kb / "kb.json").read_bytes(), before)

    def test_apply_needs_a_backup_outside_the_kb(self):
        with self.assertRaises(kb_migrate.MigrationError):
            kb_migrate.migrate(self.kb, PROFILE, apply=True)
        with self.assertRaises(kb_migrate.MigrationError):
            kb_migrate.migrate(self.kb, PROFILE, self.kb / "backup", apply=True)

    def test_receipt_holds_digests_and_counts_only(self):
        receipt = Path(self.tmp.name) / "receipt.json"
        kb_migrate.migrate(self.kb, PROFILE, self.backup, receipt, apply=True)
        data = json.loads(receipt.read_text(encoding="utf-8"))
        self.assertNotEqual(data["index_sha256_before"], data["index_sha256_after"])
        self.assertNotIn("phrase de test", receipt.read_text(encoding="utf-8"))
        self.assertTrue((self.backup / "kb.json.before-profile-id").is_file())

    def test_atoms_are_untouched(self):
        before = json.loads((self.kb / "kb.json").read_text(encoding="utf-8"))
        kb_migrate.migrate(self.kb, PROFILE, self.backup, apply=True)
        after = json.loads((self.kb / "kb.json").read_text(encoding="utf-8"))
        self.assertEqual(before["atoms"], after["atoms"])
        self.assertEqual(before["sources"], after["sources"])
        self.assertEqual(after["profile_id"], "neutral")

    def test_idempotent_and_refuses_another_profile_or_version(self):
        kb_migrate.migrate(self.kb, PROFILE, self.backup, apply=True)
        self.assertEqual(kb_migrate.migrate(self.kb, PROFILE)["action"], "none")
        index = json.loads((self.kb / "kb.json").read_text(encoding="utf-8"))
        index["profile_id"] = "autre-profil"
        (self.kb / "kb.json").write_text(json.dumps(index), encoding="utf-8")
        with self.assertRaises(kb_migrate.MigrationError):
            kb_migrate.migrate(self.kb, PROFILE)
        del index["profile_id"]
        index["lexicon_version"] = "0.0.0-ancien"
        (self.kb / "kb.json").write_text(json.dumps(index), encoding="utf-8")
        with self.assertRaises(kb_migrate.MigrationError):
            kb_migrate.migrate(self.kb, PROFILE)


if __name__ == "__main__":
    unittest.main()
