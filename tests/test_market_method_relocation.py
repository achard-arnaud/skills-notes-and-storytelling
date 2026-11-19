"""Relocation preserves the method and every repository-relative destination."""
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / 'diagnostic-complet/skills/analyzing-market-and-competition/SKILL.md'
NEW = ROOT / 'skills/business-analysis/references/market-and-competition.md'
MANIFEST = ROOT / 'skills/business-analysis/manifest.json'
SOURCE_BLOB = '66602978bc86c848e2f967893c7ec4831fda7987'
PATH = re.compile(r'(?<![\w/])(?:\.\./)+(?:[\w.-]+/)*[\w.-]+\.md')


def canonical(text, location):
    def resolve(match):
        path = (location.parent / match.group()).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise ValueError('unresolved reference: ' + match.group())
        return path.relative_to(ROOT).as_posix()
    return PATH.sub(resolve, text)


class MarketRelocationTests(unittest.TestCase):
    def test_manifest_selects_owned_method(self):
        data = json.loads(MANIFEST.read_text())
        self.assertEqual(data['methods']['business.market-and-competition'], NEW.relative_to(ROOT).as_posix())
        self.assertTrue(NEW.is_file())

    def test_preserves_original_blob_and_method_with_same_links(self):
        content = OLD.read_bytes()
        self.assertEqual(hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest(), SOURCE_BLOB)
        self.assertEqual(canonical(OLD.read_text(), OLD), canonical(NEW.read_text(), NEW))

    def test_detects_changed_instruction_and_bad_rebase(self):
        text = NEW.read_text()
        self.assertNotEqual(canonical(OLD.read_text(), OLD), canonical(text.replace('Aucun claim', 'Chaque claim'), NEW))
        with self.assertRaisesRegex(ValueError, 'unresolved reference'):
            canonical(text + '\n../missing-method-reference.md', NEW)

    def test_preserves_other_manifest_entries(self):
        snapshot = json.loads((ROOT / 'docs/planning/S3-RETIREMENT-INVENTORY.json').read_text())
        for item in snapshot['coverage']['manifests']:
            old = json.loads(snapshot['source_snapshots'][item['path']])
            current = json.loads((ROOT / item['path']).read_text())
            if item['path'] == MANIFEST.relative_to(ROOT).as_posix():
                old['methods'].pop('business.market-and-competition')
                current['methods'].pop('business.market-and-competition')
                old['methods'].pop('business.industry-and-operations')
                self.assertEqual(current['methods'].pop('business.industry-and-operations'), 'skills/business-analysis/references/industry-and-operations.md')
                old['methods'].pop('business.corporate-functions')
                self.assertEqual(current['methods'].pop('business.corporate-functions'), 'skills/business-analysis/references/corporate-functions.md')
                old.pop('version'); current.pop('version')
            self.assertEqual(old, current)
