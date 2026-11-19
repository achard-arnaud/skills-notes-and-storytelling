"""Keep the industry migration contract independently discoverable."""
import unittest
from method_relocation_support import METHODS, ROOT, RelocationChecks, canonical

METHOD_KEY = 'business.industry-and-operations'
SPEC = METHODS[METHOD_KEY]
OLD = ROOT / SPEC['old']
NEW = ROOT / SPEC['new']
MANIFEST = ROOT / 'skills/business-analysis/manifest.json'
SOURCE_BLOB = SPEC['blob']


class IndustryRelocationTests(RelocationChecks, unittest.TestCase):
    method_key = METHOD_KEY
