import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from business_brief_content import SCHEMA, validate_business_brief_content


def sample():
    return json.loads((ROOT / "fixtures/business-brief-content.json").read_text(encoding="utf-8"))


def decision_sample():
    content = sample()
    content["decision_requested"] = True
    content["question"] = "Should the synthetic option proceed?"
    content["recommendations"] = [{
        "id": "R1",
        "option": "Run a bounded synthetic pilot.",
        "conditions": ["Independent evidence is collected."],
        "falsifier": "The independent evidence contradicts the core claim.",
        "action": "Review the evidence ledger.",
        "owner": {"status": "unassigned", "role": "decision owner"},
        "gate": "Human decision after evidence review."
    }]
    return content


class BusinessBriefContentTests(unittest.TestCase):
    def test_descriptive_fixture_is_valid_and_revision_is_independent(self):
        content = sample()
        before = copy.deepcopy(content)
        result = validate_business_brief_content(content)
        expected = hashlib.sha256(json.dumps(content, sort_keys=True, ensure_ascii=False,
                                             separators=(",", ":")).encode()).hexdigest()
        self.assertTrue(result["valid"], result)
        self.assertTrue(result["handoff_ready"])
        self.assertFalse(result["human_approval"])
        self.assertEqual(expected, result["content_revision"])
        self.assertEqual(before, content)

    def test_decision_requires_a_complete_option(self):
        content = decision_sample()
        self.assertTrue(validate_business_brief_content(content)["valid"])
        for key in ("option", "conditions", "falsifier", "action", "owner", "gate"):
            bad = decision_sample()
            del bad["recommendations"][0][key]
            self.assertFalse(validate_business_brief_content(bad)["valid"], key)

    def test_descriptive_does_not_invent_recommendations(self):
        content = sample()
        content["recommendations"] = decision_sample()["recommendations"]
        result = validate_business_brief_content(content)
        self.assertFalse(result["valid"])
        self.assertTrue(any("descriptive" in e for e in result["semantic_errors"]))

    def test_decision_without_option_is_blocked(self):
        content = sample()
        content["decision_requested"] = True
        result = validate_business_brief_content(content)
        self.assertFalse(result["handoff_ready"])
        self.assertTrue(any("decision" in e for e in result["semantic_errors"]))

    def test_ac1_fields_are_required_and_typed(self):
        for key in ("mode", "primary_dimension", "subject", "audience", "question",
                    "cutoff", "template"):
            content = sample()
            del content[key]
            self.assertFalse(validate_business_brief_content(content)["valid"], key)
        for key, value in (("mode", "candidate"), ("primary_dimension", "product"),
                           ("cutoff", "2026-02-30")):
            content = sample()
            content[key] = value
            self.assertFalse(validate_business_brief_content(content)["valid"], key)

    def test_ac2_fields_are_required(self):
        fields = ("id", "statement", "status", "grade", "source", "confidence",
                  "contradiction", "contradiction_detail", "unknowns")
        for key in fields:
            content = sample()
            del content["claims"][0][key]
            self.assertFalse(validate_business_brief_content(content)["valid"], key)
        for key in ("id", "kind", "locator", "published_at"):
            content = sample()
            del content["claims"][0]["source"][key]
            self.assertFalse(validate_business_brief_content(content)["valid"], key)

    def test_vendor_or_corporate_source_cannot_become_verified_fact(self):
        for kind in ("primary_vendor", "primary_corporate"):
            content = sample()
            content["claims"][0]["source"]["kind"] = kind
            content["claims"][0]["status"] = "verified_fact"
            result = validate_business_brief_content(content)
            self.assertFalse(result["valid"])
            self.assertTrue(any("supplier" in e for e in result["semantic_errors"]))

    def test_contradiction_and_unknown_are_explicit(self):
        content = sample()
        content["claims"][0]["contradiction"] = "present"
        content["claims"][0]["contradiction_detail"] = ""
        self.assertFalse(validate_business_brief_content(content)["valid"])
        content = sample()
        content["claims"][0]["contradiction"] = "unknown"
        content["claims"][0]["unknowns"] = []
        self.assertFalse(validate_business_brief_content(content)["valid"])

    def test_identifiers_are_unique(self):
        content = sample()
        content["claims"].append(copy.deepcopy(content["claims"][0]))
        self.assertFalse(validate_business_brief_content(content)["valid"])
        content = decision_sample()
        content["recommendations"][0]["id"] = "C1"
        self.assertFalse(validate_business_brief_content(content)["valid"])

    def test_unknown_fields_and_malformed_inputs_fail_without_crash(self):
        content = sample()
        content["unexpected"] = True
        self.assertFalse(validate_business_brief_content(content)["valid"])
        for bad in (None, [], "x", 3, {"claims": [None]}):
            self.assertFalse(validate_business_brief_content(bad)["valid"])

    def test_schema_uses_only_local_supported_vocabulary(self):
        keywords = {"$schema", "$id", "title", "$defs", "$ref", "type",
                    "additionalProperties", "required", "properties", "const", "enum",
                    "minLength", "pattern", "format", "minItems", "uniqueItems", "items"}
        def check(node):
            self.assertFalse(set(node) - keywords)
            for key, value in node.items():
                if key in ("properties", "$defs"):
                    for child in value.values():
                        check(child)
                elif key == "items":
                    check(value)
        check(SCHEMA)


if __name__ == "__main__":
    unittest.main()
