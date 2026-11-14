import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "mba/taxonomy/tools"))
from resolve_method import select


class PurposeDispatchTests(unittest.TestCase):
    def test_eight_intents_bind_methods_and_blocks(self):
        manifest = json.loads((ROOT / "verticales/produit/manifest.json").read_text())
        self.assertEqual(manifest["default_intent"], "fiche-produit")
        self.assertEqual(len(manifest["intents"]), 8)
        for intent, spec in manifest["intents"].items():
            self.assertTrue(spec["methods"])
            self.assertTrue(spec["block_ids"])
            for method in spec["methods"]:
                with self.subTest(intent=intent, method=method):
                    block = spec["block_ids"][0]
                    result = select("produit", intent, method, block)
                    self.assertEqual(result["affects_blocks"], [block])

    def test_page_count_does_not_invoke_analysis(self):
        for route in ("produit", "business"):
            with self.subTest(route=route), self.assertRaises(ValueError):
                select(route, "two-pager", "product.icp", "identite")

    def test_unrelated_method_or_unbound_block(self):
        for method, block in [("TECH-07", "identite"), ("product.icp", "missing")]:
            with self.subTest(method=method), self.assertRaises(ValueError):
                select("produit", "fiche-produit", method, block)
