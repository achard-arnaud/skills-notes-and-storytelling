import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "templates" / "diagnostic-reco-sellside.md"
MANIFEST_PATH = ROOT / "templates" / "manifest.json"
FIXTURE_PATH = ROOT / "examples" / "diagnostic-reco-sellside-v1.md"


def _manifest_version(template_type: str) -> str:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return next(
        template["version"]
        for template in manifest["templates"]
        if template["type"] == template_type
    )


def _fixture_template_version() -> str:
    for line in FIXTURE_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("template_version:"):
            return line.partition(":")[2].strip()
    raise AssertionError("fixture template_version is missing")


class SellsideTemplateContractTest(unittest.TestCase):
    def test_sellside_template_distinguishes_body_and_catalogue_versions(self):
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
        catalogue_version = _manifest_version("diagnostic-reco-sellside")

        self.assertIn("Body revision: 1.1.0", template)
        self.assertIn(f"Catalogue usage version: {catalogue_version}", template)
        self.assertEqual(_fixture_template_version(), catalogue_version)

    def test_sellside_template_names_the_existing_editorial_bridges(self):
        template = TEMPLATE_PATH.read_text(encoding="utf-8")

        self.assertIn("partnership or co-distribution", template)
        self.assertIn("`integration-note`", template)
        self.assertIn("named-account hypothesis", template)
        self.assertIn("`opportunity-note-icp`", template)


if __name__ == "__main__":
    unittest.main()
