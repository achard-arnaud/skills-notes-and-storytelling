import json
import re
import unittest
from pathlib import Path

from src.template_types import OutputTemplateType


ROOT = Path(__file__).resolve().parents[1]


class TemplateRoutesTest(unittest.TestCase):
    def test_root_skill_routes_cover_catalogue_without_duplicates(self):
        manifest = json.loads(
            (ROOT / "templates/manifest.json").read_text(encoding="utf-8")
        )
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        _, heading, rest = skill.partition("\n## Template enum\n")
        self.assertTrue(heading, "SKILL.md: missing Template enum section")
        routes, _, _ = rest.partition("\n## ")
        symbols = re.findall(r"^- `([A-Z][A-Z0-9_]+)`", routes, re.MULTILINE)
        catalogue = [template["type"] for template in manifest["templates"]]
        expected = [OutputTemplateType(template).name for template in catalogue]

        self.assertCountEqual(
            symbols,
            expected,
            "Align the routes in SKILL.md with templates/manifest.json.",
        )
