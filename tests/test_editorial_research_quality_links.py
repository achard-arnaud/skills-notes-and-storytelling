import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/fixtures/editorial-research-quality-links-v1.json"
LINK_PATTERN = re.compile(r"\[[^]]+\]\(([^)#]*editorial-and-research-quality\.md)\)")


class EditorialResearchQualityLinkTest(unittest.TestCase):
    def test_links_resolve_to_canonical_file(self):
        case = json.loads(FIXTURE.read_text(encoding="utf-8"))
        contract = (ROOT / case["contract"]).resolve()

        for relative_path in case["consumers"]:
            with self.subTest(consumer=relative_path):
                consumer = ROOT / relative_path
                targets = LINK_PATTERN.findall(consumer.read_text(encoding="utf-8"))
                self.assertTrue(targets, f"{relative_path} must link the shared editorial contract")
                self.assertEqual(len(targets), 1, f"{relative_path} must have one canonical contract link")
                resolved = (consumer.parent / targets[0]).resolve()
                self.assertEqual(resolved, contract)
                self.assertTrue(resolved.is_file(), f"{relative_path} links a missing contract")


if __name__ == "__main__":
    unittest.main()
