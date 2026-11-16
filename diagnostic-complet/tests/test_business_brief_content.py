import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from business_brief_content import (
    HANDOFF_SCHEMA,
    SCHEMA,
    freeze_business_brief_handoff,
    validate_business_brief_content,
    verify_business_brief_handoff,
)


def sample():
    return json.loads((ROOT / "fixtures/business-brief-content.json").read_text(encoding="utf-8"))


def handoff_sample():
    return json.loads((ROOT / "fixtures/business-brief-handoff.json").read_text(encoding="utf-8"))


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

    def test_valid_content_can_be_frozen_and_verified_without_mutation(self):
        content = sample()
        before = copy.deepcopy(content)
        frozen = freeze_business_brief_handoff(content)
        self.assertTrue(frozen["valid"], frozen)
        self.assertTrue(frozen["handoff_ready"])
        self.assertFalse(frozen["human_approval"])
        self.assertEqual(before, content)

        handoff = frozen["handoff"]
        self.assertEqual("1.0", handoff["schema_version"])
        self.assertEqual("business-brief-content-handoff", handoff["kind"])
        self.assertEqual(frozen["content_revision"], handoff["content_revision"])
        self.assertEqual(content, handoff["content_spec"])
        self.assertFalse(handoff["human_approval"])

        handoff_before = copy.deepcopy(handoff)
        verified = verify_business_brief_handoff(
            handoff, expected_revision=frozen["content_revision"]
        )
        self.assertTrue(verified["valid"], verified)
        self.assertTrue(verified["handoff_ready"])
        self.assertEqual(frozen["content_revision"], verified["content_revision"])
        self.assertEqual(handoff_before, handoff)

    def test_synthetic_handoff_fixture_matches_the_canonical_content_fixture(self):
        handoff = handoff_sample()
        result = verify_business_brief_handoff(handoff)
        self.assertTrue(result["valid"], result)
        self.assertEqual(sample(), handoff["content_spec"])
        self.assertEqual(handoff["content_revision"], result["content_revision"])

    def test_invalid_content_is_not_frozen(self):
        content = sample()
        content["claims"][0]["status"] = "verified_fact"
        result = freeze_business_brief_handoff(content)
        self.assertFalse(result["valid"])
        self.assertFalse(result["handoff_ready"])
        self.assertIsNone(result["handoff"])

    def test_expected_revision_must_match_before_freeze_or_verification(self):
        content = sample()
        stale = "0" * 64
        frozen = freeze_business_brief_handoff(content, expected_revision=stale)
        self.assertFalse(frozen["valid"])
        self.assertIsNone(frozen["handoff"])
        self.assertTrue(any("expected_revision" in error for error in frozen["errors"]))

        current = freeze_business_brief_handoff(content)
        verified = verify_business_brief_handoff(
            current["handoff"], expected_revision=stale
        )
        self.assertFalse(verified["valid"])
        self.assertTrue(any("expected_revision" in error for error in verified["errors"]))

    def test_tampered_content_and_invalid_hash_are_rejected(self):
        handoff = freeze_business_brief_handoff(sample())["handoff"]
        tampered = copy.deepcopy(handoff)
        tampered["content_spec"]["claims"][0]["statement"] = "Changed after freeze."
        result = verify_business_brief_handoff(tampered)
        self.assertFalse(result["valid"])
        self.assertTrue(any("content_revision" in error for error in result["errors"]))

        malformed = copy.deepcopy(handoff)
        malformed["content_revision"] = "not-a-sha256"
        result = verify_business_brief_handoff(malformed)
        self.assertFalse(result["valid"])
        self.assertTrue(result["structural_errors"])

    def test_unknown_schema_and_invalid_entry_are_rejected_without_crash(self):
        handoff = freeze_business_brief_handoff(sample())["handoff"]
        unknown = copy.deepcopy(handoff)
        unknown["schema_version"] = "2.0"
        self.assertFalse(verify_business_brief_handoff(unknown)["valid"])
        for bad in (None, [], "x", 3, {"schema_version": "1.0"}):
            result = verify_business_brief_handoff(bad)
            self.assertFalse(result["valid"])

    def test_handoff_schema_uses_only_local_supported_vocabulary(self):
        keywords = {"$schema", "$id", "title", "type", "additionalProperties",
                    "required", "properties", "const", "pattern"}

        def check(node):
            self.assertFalse(set(node) - keywords)
            for child in node.get("properties", {}).values():
                check(child)

        check(HANDOFF_SCHEMA)


if __name__ == "__main__":
    unittest.main()
