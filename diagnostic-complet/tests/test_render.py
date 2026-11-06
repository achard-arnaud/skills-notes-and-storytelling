import copy
import json
from html.parser import HTMLParser
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from render import render_study


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.elements = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.study = json.loads((ROOT / "fixtures/synthetic.json").read_text(encoding="utf-8"))

    def test_synthetic_fixture_has_three_sections_and_distinct_pillars(self):
        self.assertEqual(3, len(self.study["sections"]))
        self.assertGreaterEqual(len(self.study["pillars"]), 4)
        self.assertTrue({"data", "ai", "industry", "corporate"}.issubset({p["id"] for p in self.study["pillars"]}))
        self.assertTrue(all(c["status"] in {"supplied_claim", "hypothesis"} for c in self.study["claims"]))
        self.assertTrue(all(s["state"] == "candidate" for s in self.study["side_stories"]))

    def test_all_internal_links_and_tab_controls_resolve(self):
        doc = Document(render_study(self.study))
        ids = [a["id"] for _, a in doc.elements if "id" in a]
        self.assertEqual(len(ids), len(set(ids)))
        for _, attrs in doc.elements:
            href = attrs.get("href", "")
            if href.startswith("#"):
                self.assertIn(href[1:], ids)
            if "aria-controls" in attrs:
                self.assertIn(attrs["aria-controls"], ids)
            if "aria-labelledby" in attrs:
                self.assertIn(attrs["aria-labelledby"], ids)

    def test_accessible_tabs_filter_and_cross_panel_navigation(self):
        output = render_study(self.study)
        doc = Document(output)
        tabs = [a for _, a in doc.elements if a.get("role") == "tab"]
        panels = [a for _, a in doc.elements if a.get("role") == "tabpanel"]
        self.assertEqual(4, len(tabs))
        self.assertEqual(4, len(panels))
        self.assertEqual(1, sum(t["aria-selected"] == "true" for t in tabs))
        self.assertEqual(1, sum(t["tabindex"] == "0" for t in tabs))
        for key in ["ArrowRight", "ArrowLeft", "Home", "End", "hashchange", "applyFilter"]:
            self.assertIn(key, output)
        self.assertIn('for="pillar-filter"', output)
        self.assertIn("Retour au récit", output)
        self.assertIn("Revue incomplète", output)

    def test_untrusted_content_cannot_inject_elements_or_active_urls(self):
        payload = '</script><script src="https://evil.example/x.js">alert(1)</script><img src=x onerror=alert(2)>'
        self.study["title"] = payload
        self.study["sections"][0]["paragraphs"][0]["text"] = payload
        self.study["side_stories"][0]["text"] = payload
        self.study["sources"][0]["locator"] = "javascript:alert(1)"
        output = render_study(self.study)
        doc = Document(output)
        self.assertEqual(1, sum(tag == "script" for tag, _ in doc.elements))
        self.assertFalse(any(tag == "img" for tag, _ in doc.elements))
        self.assertFalse(any("onerror" in attrs or "onclick" in attrs for _, attrs in doc.elements))
        self.assertFalse(any(attrs.get("href", "").startswith("javascript:") for _, attrs in doc.elements))
        self.assertIn("&lt;/script&gt;", output)
        self.assertFalse(any(tag == "script" and "src" in attrs for tag, attrs in doc.elements))

    def test_mermaid_is_exact_escaped_source_without_remote_runtime(self):
        import html
        diagram = 'flowchart TD\n A["<script>danger</script>"] --> B["R&D"]'
        self.study["mermaid"] = diagram
        output = render_study(self.study)
        self.assertIn(html.escape(diagram, quote=True), output)
        self.assertIn("source, sans moteur de rendu", output)
        doc = Document(output)
        self.assertFalse(any(tag in {"iframe", "link"} for tag, _ in doc.elements))
        self.assertFalse(any(tag == "script" and "src" in attrs for tag, attrs in doc.elements))

    def test_no_state_mutation_or_invented_verification(self):
        before = copy.deepcopy(self.study)
        output = render_study(self.study)
        self.assertEqual(before, self.study)
        self.assertNotIn("Fait déclaré vérifié", output)
        self.assertIn("Assertion fournie — à vérifier", output)
        self.assertIn("Hypothèse", output)
        self.assertIn("preuve à instruire", output)

    def test_unresolved_reference_is_explicit_and_not_a_broken_link(self):
        self.study["side_stories"][0]["return_to"] = "missing"
        output = render_study(self.study)
        self.assertIn("Référence non résolue", output)
        self.assertNotIn('href="#missing"', output)

    def test_duplicate_ids_rejected(self):
        self.study["claims"][1]["id"] = self.study["claims"][0]["id"]
        with self.assertRaisesRegex(ValueError, "Duplicate IDs"):
            render_study(self.study)

    def test_malformed_source_url_remains_inert(self):
        self.study["sources"][0]["locator"] = "https://[broken"
        output = render_study(self.study)
        self.assertIn("<code>https://[broken</code>", output)


if __name__ == "__main__":
    unittest.main()
