import gzip
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import project  # noqa: E402


def sha(b):
    return hashlib.sha256(b).hexdigest()


class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "graph1"
        (self.root / "build").mkdir(parents=True)
        self.frozen = b'{"nodes": [], "edges": []}'
        (self.root / "build" / "graph.json").write_bytes(self.frozen)
        self.src = Path(self.tmp.name) / "kb"
        (self.src / "atoms").mkdir(parents=True)
        (self.src / "atoms" / "a.md").write_text("# a\n", encoding="utf-8")
        (self.src / "kb.json").write_text("{}", encoding="utf-8")

    def run_project(self, **kw):
        return project.project(self.root, sha(self.frozen), {"kb": self.src}, **kw)

    def test_writes_only_under_namespace_and_keeps_frozen_graph(self):
        report = self.run_project()
        self.assertTrue(report["frozen_graph_unchanged"])
        self.assertTrue((self.root / "knowledge/business/greenyellow/kb/atoms/a.md").exists())
        self.assertTrue((self.root / "knowledge/business/greenyellow/MANIFEST.json").exists())
        self.assertEqual((self.root / "build" / "graph.json").read_bytes(), self.frozen)

    def test_wrong_frozen_hash_refuses_before_any_write(self):
        with self.assertRaises(project.ProjectionError):
            project.project(self.root, "0" * 64, {"kb": self.src})
        self.assertFalse((self.root / "knowledge").exists())

    def test_formation_directories_and_traversal_are_refused(self):
        for bad in ("canonical/x", "build/x", "knowledge/business/../../build/x", "/abs", "knowledge/other/x"):
            with self.subTest(namespace=bad), self.assertRaises(project.ProjectionError):
                self.run_project(namespace=bad)

    def test_dry_run_writes_nothing(self):
        report = self.run_project(dry_run=True)
        self.assertEqual(report["written"], 0)
        self.assertFalse((self.root / "knowledge").exists())

    def test_idempotent_second_run_writes_nothing(self):
        self.run_project()
        self.assertEqual(self.run_project()["written"], 0)

    def test_raw_html_is_gzipped_losslessly(self):
        raw = Path(self.tmp.name) / "raw"
        raw.mkdir()
        (raw / "p.html").write_bytes(b"<html>x</html>")
        self.run_project(include_raw=raw)
        out = self.root / "knowledge/business/greenyellow/raw/p.html.gz"
        self.assertEqual(gzip.decompress(out.read_bytes()), b"<html>x</html>")

    def test_manifest_hashes_match_files(self):
        self.run_project()
        base = self.root / "knowledge/business/greenyellow"
        manifest = json.loads((base / "MANIFEST.json").read_text(encoding="utf-8"))
        for entry in manifest["entries"]:
            self.assertEqual(sha((base / entry["path"]).read_bytes()), entry["sha256"])


if __name__ == "__main__":
    unittest.main()
