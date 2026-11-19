"""Keep the corporate migration contract independently discoverable."""
import unittest
from method_relocation_support import METHODS, ROOT, RelocationChecks, canonical

METHOD_KEY = 'business.corporate-functions'
SPEC = METHODS[METHOD_KEY]
OLD = ROOT / SPEC['old']
NEW = ROOT / SPEC['new']
MANIFEST = ROOT / 'skills/business-analysis/manifest.json'
SOURCE_BLOB = SPEC['blob']


class CorporateRelocationTests(RelocationChecks, unittest.TestCase):
    method_key = METHOD_KEY
