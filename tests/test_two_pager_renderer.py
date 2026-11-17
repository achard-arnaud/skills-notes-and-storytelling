import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

from jsonschema import ValidationError


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests/fixtures/two-pager-render-content-v1.json"
RENDER = ROOT / "renderers/two_pager_nice/scripts/render.py"


def load_renderer():
    spec = importlib.util.spec_from_file_location("two_pager_render", RENDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TwoPagerRendererContractTests(unittest.TestCase):
    def setUp(self):
        self.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_valid_fixture_preserves_content_revision(self):
        renderer = load_renderer()
        validated = renderer.load_config(FIXTURE)
        self.assertEqual(validated["content_revision"], self.fixture["content_revision"])
        self.assertEqual(len(validated["pages"]), 2)

    def test_missing_outer_gate_fails_before_theme_or_jinja(self):
        renderer = load_renderer()
        invalid = copy.deepcopy(self.fixture)
        del invalid["pages"][0]["gate"]
        with tempfile.TemporaryDirectory() as folder:
            config = Path(folder) / "invalid.json"
            config.write_text(json.dumps(invalid), encoding="utf-8")
            with self.assertRaises(ValidationError) as raised:
                renderer.build_html(config, Path(folder) / "output.html")
        self.assertIn("gate", str(raised.exception))

    def test_exactly_two_pages_are_required(self):
        renderer = load_renderer()
        invalid = copy.deepcopy(self.fixture)
        invalid["pages"].pop()
        with self.assertRaises(ValidationError):
            renderer.validate_config(invalid)


if __name__ == "__main__":
    unittest.main()
