import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pointers_check", ROOT / "pointers_check.py")
pointers_check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pointers_check)

GOOD = "ATOM-" + "ab" * 32
GONE = "ATOM-" + "cd" * 32


class PointerCheckTests(unittest.TestCase):
    def tree(self, tmp):
        d = Path(tmp) / "kb" / "atoms" / "ab"
        d.mkdir(parents=True)
        (d / f"{GOOD}.md").write_text("synthetic", encoding="utf-8")
        return Path(tmp)

    def test_present_missing_and_malformed_atoms_are_reported_separately(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.tree(tmp)
            report = pointers_check.check({"examples": [{"id": "E1", "atoms": [GOOD, GONE, "ATOM-xyz"]}, {"id": "E2", "atoms": []}]}, root)
        self.assertEqual(3, report["checked"])
        self.assertEqual([{"example": "E1", "atom": GONE}], report["missing"])
        self.assertEqual([{"example": "E1", "atom": "ATOM-xyz"}], report["malformed"])
        self.assertFalse(report["ok"])

    def test_cli_exit_code_follows_the_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.tree(tmp)
            reg = Path(tmp) / "registry.json"
            reg.write_text(json.dumps({"examples": [{"id": "E1", "atoms": [GOOD]}]}), encoding="utf-8")
            self.assertEqual(0, pointers_check.main([str(reg), "--kb-root", str(root)]))
            reg.write_text(json.dumps({"examples": [{"id": "E1", "atoms": [GONE]}]}), encoding="utf-8")
            self.assertEqual(1, pointers_check.main([str(reg), "--kb-root", str(root)]))

    def test_the_tool_itself_names_no_run(self):
        text = (ROOT / "pointers_check.py").read_text(encoding="utf-8").lower()
        for word in ("greenyellow", "framatome", "easyvision"):
            self.assertNotIn(word, text)


if __name__ == "__main__":
    unittest.main()
