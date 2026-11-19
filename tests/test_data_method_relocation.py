"""Keep the technical data migration and its owner independently discoverable."""
import json
import unittest
from method_relocation_support import ROOT, TECHNICAL_MANIFEST, TECHNICAL_METHODS, RelocationChecks


class DataRelocationTests(RelocationChecks, unittest.TestCase):
    method_key = 'technical.data-foundations'
    manifest_path = TECHNICAL_MANIFEST
    method_specs = TECHNICAL_METHODS

    def test_manifest_selects_owned_method(self):
        super().test_manifest_selects_owned_method()
        data = json.loads((ROOT / self.manifest_path).read_text())
        self.assertEqual(data['domain'], 'technical')
        self.assertEqual(data['version'], '1.0.2')
