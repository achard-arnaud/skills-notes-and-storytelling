"""Shared, explicitly pinned contracts for the four delivered migrations."""
import copy
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = 'skills/business-analysis/manifest.json'
PATH = re.compile(r'(?<![\w/])(?:\.\./)+(?:[\w.-]+/)*[\w.-]+\.md')

# Expectations come from the delivered migrations, never from the current routes.
METHODS = {
    'business.industry-and-operations': {
        'old': 'diagnostic-complet/skills/analyzing-industry-value-chain/SKILL.md',
        'new': 'skills/business-analysis/references/industry-and-operations.md',
        'blob': '5c2e852fab8ef7c16a3219d1a6bb7e7108733929',
    },
    'business.market-and-competition': {
        'old': 'diagnostic-complet/skills/analyzing-market-and-competition/SKILL.md',
        'new': 'skills/business-analysis/references/market-and-competition.md',
        'blob': '66602978bc86c848e2f967893c7ec4831fda7987',
    },
    'business.corporate-functions': {
        'old': 'diagnostic-complet/skills/analyzing-corporate-functions/SKILL.md',
        'new': 'skills/business-analysis/references/corporate-functions.md',
        'blob': '8bd3e43eef9882feaf2d4cd1e1de97b49f15e222',
    },
    'business.economics-and-financing': {
        'old': 'diagnostic-complet/skills/analyzing-economics-and-financing/SKILL.md',
        'new': 'skills/business-analysis/references/economics-and-financing.md',
        'blob': '400711e7684b06d1ceceaa0d922a94e88c33ca0f',
    },
}


def canonical(text, location):
    def resolve(match):
        path = (location.parent / match.group()).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise ValueError('unresolved reference: ' + match.group())
        return path.relative_to(ROOT).as_posix()
    return PATH.sub(resolve, text)


def current_manifests():
    snapshot = json.loads((ROOT / 'docs/planning/S3-RETIREMENT-INVENTORY.json').read_text())
    return {item['path']: json.loads((ROOT / item['path']).read_text())
            for item in snapshot['coverage']['manifests']}


def assert_manifest_snapshots(check, manifests):
    snapshot = json.loads((ROOT / 'docs/planning/S3-RETIREMENT-INVENTORY.json').read_text())
    check.assertEqual(set(manifests), {item['path'] for item in snapshot['coverage']['manifests']})
    for path, current in manifests.items():
        expected = json.loads(snapshot['source_snapshots'][path])
        actual = copy.deepcopy(current)
        if path == MANIFEST:
            expected['methods'].update({key: spec['new'] for key, spec in METHODS.items()})
            expected.pop('version')
            actual.pop('version')
        check.assertEqual(expected, actual, path)


class RelocationChecks:
    """Mixin only: unittest discovers the four existing concrete test classes."""

    @property
    def spec(self):
        return METHODS[self.method_key]

    def test_manifest_selects_owned_method(self):
        data = json.loads((ROOT / MANIFEST).read_text())
        self.assertEqual(data['methods'][self.method_key], self.spec['new'])
        self.assertTrue((ROOT / self.spec['new']).is_file())

    def test_preserves_original_blob_and_method_with_same_links(self):
        old, new = ROOT / self.spec['old'], ROOT / self.spec['new']
        content = old.read_bytes()
        self.assertEqual(hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest(),
                         self.spec['blob'])
        self.assertEqual(canonical(old.read_text(), old), canonical(new.read_text(), new))

    def test_detects_changed_instruction_and_bad_rebase(self):
        old, new = ROOT / self.spec['old'], ROOT / self.spec['new']
        text = new.read_text()
        self.assertIn('Aucun claim', text)
        self.assertNotEqual(canonical(old.read_text(), old),
                            canonical(text.replace('Aucun claim', 'Chaque claim', 1), new))
        with self.assertRaisesRegex(ValueError, 'unresolved reference'):
            canonical(text + '\n../missing-method-reference.md', new)
        # An existing file outside the repository must not pass as a valid link.
        with tempfile.NamedTemporaryFile(suffix='.md') as outside:
            self.assertTrue(Path(outside.name).is_file())
            with self.assertRaisesRegex(ValueError, 'unresolved reference'):
                canonical(text + '\n' + os.path.relpath(outside.name, new.parent), new)

    def test_preserves_other_manifest_entries(self):
        manifests = current_manifests()
        assert_manifest_snapshots(self, manifests)
        # Exercise the shared assertion against isolated mutations, including a
        # method outside the migrated set and each of the four other domains.
        non_migrated = sorted(set(manifests[MANIFEST]['methods']) - set(METHODS))
        self.assertTrue(non_migrated)
        for key in (self.method_key, non_migrated[0]):
            with self.subTest(changed_route=key):
                damaged = copy.deepcopy(manifests)
                damaged[MANIFEST]['methods'][key] = 'wrong-method.md'
                with self.assertRaises(AssertionError):
                    assert_manifest_snapshots(self, damaged)
        for path in sorted(set(manifests) - {MANIFEST}):
            with self.subTest(changed_manifest=path):
                damaged = copy.deepcopy(manifests)
                damaged[path]['unexpected_change'] = True
                with self.assertRaises(AssertionError):
                    assert_manifest_snapshots(self, damaged)
