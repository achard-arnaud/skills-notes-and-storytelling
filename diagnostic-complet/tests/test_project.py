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



class ShardAndCompressTests(ProjectTests):
    def test_atoms_are_sharded_by_hex_prefix(self):
        (self.src / "atoms" / "ATOM-ab12.md").write_text("# x\n", encoding="utf-8")
        project.project(self.root, sha(self.frozen), {"kb": self.src}, shard_atoms=2)
        base = self.root / "knowledge/business/greenyellow/kb/atoms"
        self.assertTrue((base / "ab" / "ATOM-ab12.md").exists())

    def test_large_json_is_gzipped_with_original_hash_in_manifest(self):
        big = b'{"k": "' + b"x" * 3000 + b'"}'
        (self.src / "big.json").write_bytes(big)
        project.project(self.root, sha(self.frozen), {"kb": self.src}, compress_over=1000)
        base = self.root / "knowledge/business/greenyellow"
        self.assertEqual(gzip.decompress((base / "kb/big.json.gz").read_bytes()), big)
        manifest = json.loads((base / "MANIFEST.json").read_text(encoding="utf-8"))
        entry = next(e for e in manifest["entries"] if e["path"] == "kb/big.json.gz")
        self.assertEqual(entry["original_sha256"], sha(big))
        self.assertTrue((base / "kb/kb.json").exists())  # small JSON untouched

    def test_gzip_output_is_deterministic(self):
        (self.src / "big.json").write_bytes(b'{"k": "' + b"y" * 3000 + b'"}')
        a = project.project(self.root, sha(self.frozen), {"kb": self.src}, compress_over=1000)
        b = project.project(self.root, sha(self.frozen), {"kb": self.src}, compress_over=1000)
        self.assertEqual(b["written"], 0)
        self.assertEqual(a["files"], b["files"])


class OnlyPrefixTests(ProjectTests):
    def test_only_restricts_the_batch_by_path_prefix(self):
        (self.src / "atoms" / "ATOM-ab12.md").write_text("# x\n", encoding="utf-8")
        report = project.project(self.root, sha(self.frozen), {"kb": self.src}, shard_atoms=2, only={"kb/atoms/ab"})
        base = self.root / "knowledge/business/greenyellow/kb"
        self.assertEqual(report["in_batch"], 1)
        self.assertGreater(report["files"], 1)  # inventory stays complete
        self.assertTrue((base / "atoms/ab/ATOM-ab12.md").exists())
        self.assertFalse((base / "kb.json").exists())

    def test_manifest_lists_every_file_even_when_only_a_batch_is_written(self):
        (self.src / "atoms" / "ATOM-ab12.md").write_text("# x\n", encoding="utf-8")
        project.project(self.root, sha(self.frozen), {"kb": self.src}, shard_atoms=2, only={"kb/atoms/ab"})
        base = self.root / "knowledge/business/greenyellow"
        paths = {e["path"] for e in json.loads((base / "MANIFEST.json").read_text(encoding="utf-8"))["entries"]}
        self.assertIn("kb/kb.json", paths)

    def test_no_manifest_for_intermediate_batches(self):
        project.project(self.root, sha(self.frozen), {"kb": self.src}, only={"kb/kb"}, manifest=False)
        self.assertFalse((self.root / "knowledge/business/greenyellow/MANIFEST.json").exists())

if __name__ == "__main__":
    unittest.main()
