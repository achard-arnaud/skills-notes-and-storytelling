"""S3 retirement is an evidence gate, not a consequence of duplicate names."""
import hashlib
import copy
import json
import re
import unittest
from functools import lru_cache
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = 'docs/planning/S3-RETIREMENT-INVENTORY.json'
CATALOG = 'diagnostic-complet/docs/SKILLS-CATALOG.md'


def object_sha(kind, content):
    return hashlib.sha1(kind.encode() + b' ' + str(len(content)).encode() + b'\0' + content).hexdigest()


@lru_cache(maxsize=None)
def blob_sha(path):
    content = (ROOT / path).read_bytes()
    return hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()


def expected_units(data):
    units = {}
    for name, module in re.findall(r'^\| \d+ \| `([^`]+)` \| `([^`]+)`',
                                   data['source_snapshots'][CATALOG], re.M):
        units['operation:' + name] = ('diagnostic-complet/' + module, CATALOG)
    for manifest in data['coverage']['manifests']:
        for name, path in json.loads(data['source_snapshots'][manifest['path']])['methods'].items():
            units['method:' + name] = (path, manifest['path'])
    return units


@lru_cache(maxsize=None)
def text_lines(path):
    return (ROOT / path).read_text().splitlines()


def expected_references(row, base_files):
    """Re-scan bounded local text; missing callers cannot self-certify coverage."""
    found = {}
    excluded = {INVENTORY, 'tests/test_s3_retirement_inventory.py', row['path']}
    for path, metadata in base_files.items():
        if path in excluded or path.startswith(('.claude/', '.agents/')) or (ROOT / path).is_symlink():
            continue
        try:
            if blob_sha(path) != metadata['sha']:
                continue  # Historical inventory: drift is local STALE_FOR_SWITCH, not global CI failure.
            lines = text_lines(path)
        except (UnicodeError, OSError):
            continue
        matches = [i for i, line in enumerate(lines, 1) if any(n in line for n in row['reference_needles'])]
        if matches:
            found[path] = matches
    return found


def snapshot_tree_sha(files):
    tree = {}
    for path, metadata in files.items():
        directory = tree
        parts = path.split('/')
        for part in parts[:-1]:
            directory = directory.setdefault(part, {})
        directory[parts[-1]] = metadata
    def digest(directory):
        records = []
        for name, value in directory.items():
            is_dir = 'sha' not in value
            mode, sha = ('40000', digest(value)) if is_dir else (value['mode'], value['sha'])
            records.append((name + ('/' if is_dir else ''), mode.encode() + b' ' + name.encode() + b'\0' + bytes.fromhex(sha)))
        return object_sha('tree', b''.join(record for _, record in sorted(records)))
    return digest(tree)


def stale_for_switch(data, row):
    """Current drift blocks this switch only; the historical snapshot stays valid."""
    paths = {row['path'], row['source']['path'], row['destination']['path']}
    paths.update(c['path'] for c in row['local_references'])
    paths.update(pin['path'] for pin in row['known_pins'])
    stale = []
    for path in sorted(paths):
        try:
            if blob_sha(path) != data['base_files'][path]['sha']:
                stale.append(path)
        except OSError:
            stale.append(path)
    return stale


def pointer_value(document, pointer):
    """Resolve a JSON Pointer, including escaped keys and strict array indexes."""
    if not isinstance(pointer, str) or (pointer and not pointer.startswith('/')):
        raise ValueError('invalid JSON pointer')
    if pointer == '':
        return document
    for token in pointer[1:].split('/'):
        if re.search(r'~(?![01])', token):
            raise ValueError('invalid JSON pointer escape')
        token = token.replace('~1', '/').replace('~0', '~')
        if isinstance(document, list):
            if not re.fullmatch(r'0|[1-9][0-9]*', token):
                raise ValueError('invalid array index')
            document = document[int(token)]
        elif isinstance(document, dict):
            document = document[token]
        else:
            raise ValueError('pointer traverses scalar')
    return document


def pin_locator_valid(pin, base_files):
    """Check pinned source text when fresh; drift remains local to the switch."""
    path = pin.get('path')
    if path not in base_files or ('line' in pin) == ('json_pointer' in pin):
        return False
    if 'line' in pin and (type(pin['line']) is not int or pin['line'] < 1):
        return False
    try:
        if blob_sha(path) != base_files[path]['sha']:
            return True  # Historical witness; stale_for_switch forbids its reuse.
        lines = text_lines(path)
    except (OSError, UnicodeError):
        return True  # Missing source also blocks stale_for_switch, not unrelated CI.
    try:
        if 'line' in pin:
            return (pin['line'] <= len(lines)
                    and lines[pin['line'] - 1] == pin['witness']
                    and pin['value'] in pin['witness'])
        return pointer_value(json.loads('\n'.join(lines)), pin['json_pointer']) == pin['value'] == pin['witness']
    except (ValueError, KeyError, IndexError, TypeError):
        return False


def validate_inventory(data):
    errors = []
    expected = expected_units(data)
    rows = data['entries']
    base_files = data['base_files']
    if len({r['id'] for r in rows}) != len(rows):
        errors.append('duplicate unit')
    if {r['id'] for r in rows} != set(expected):
        errors.append('unit coverage')
    for row in rows:
        if row['id'] not in expected:
            continue
        path, source = expected[row['id']]
        if row['path'] != path or row['blob_sha'] != base_files[path]['sha']:
            errors.append('path/blob: ' + row['id'])
        if row['source'] != {'path': source, 'blob_sha': base_files[source]['sha']}:
            errors.append('source: ' + row['id'])
        expected_needles = sorted(set([path, row['id'].split(':', 1)[1]]
                                      + ([Path(path).name] if Path(path).name != 'SKILL.md' else [])
                                      + (['from ' + Path(path).stem + ' import', 'import ' + Path(path).stem]
                                         if row['role'] == 'engine' else [])))
        if '/skills/' in path:
            expected_needles.append(path.split('/skills/')[1].split('/')[0])
        if row['reference_needles'] != expected_needles:
            errors.append('reference vocabulary: ' + row['id'])
        fresh_refs = expected_references(row, base_files)
        recorded_fresh = {c['path']: c['lines'] for c in row['local_references'] if c['path'] in fresh_refs}
        if recorded_fresh != fresh_refs:
            errors.append('caller coverage: ' + row['id'])
        if row['destination']['path'] not in base_files:
            errors.append('destination: ' + row['id'])
        if row['restore'] != {'commit': data['base_commit'], 'path': path, 'blob_sha': row['blob_sha']}:
            errors.append('restore: ' + row['id'])
        if row['retirement_eligible'] or row['decision'] == 'proposed-remove':
            if (row['external_callers'] != 'VERIFIED_NONE'
                    or row['equivalence']['status'] != 'VERIFIED'
                    or not row['equivalence']['evidence']
                    or not row['switch_condition']
                    or stale_for_switch(data, row)
                    or any(c['disposition'] != 'SWITCH_VERIFIED' for c in row['local_references'])):
                errors.append('retirement gate: ' + row['id'])
        for caller in row['local_references']:
            if caller['blob_sha'] != base_files[caller['path']]['sha'] or not caller['disposition']:
                errors.append('caller: ' + row['id'])
            if len(caller['lines']) != len(caller['matched_text']):
                errors.append('caller locator: ' + row['id'])
            for line, witness in zip(caller['lines'], caller['matched_text']):
                if line < 1 or not any(n in witness for n in row['reference_needles']):
                    errors.append('caller locator: ' + row['id'])
                if caller['path'] in fresh_refs and (line > len(text_lines(caller['path'])) or text_lines(caller['path'])[line-1] != witness):
                    errors.append('caller locator: ' + row['id'])
        for pin in row['known_pins']:
            if not pin_locator_valid(pin, base_files):
                errors.append('pin locator: ' + row['id'])
            if 'line' in pin:
                if pin['value'] not in pin['witness']:
                    errors.append('pin locator: ' + row['id'])
            else:
                if pin['witness'] != pin['value']:
                    errors.append('pin locator: ' + row['id'])
        # A manifest is an active dependency even if its target looks like legacy code.
        if row['id'].startswith('method:') and not any(
                c['path'] == source and c['disposition'] == 'KEEP_ACTIVE_DEPENDENCY'
                for c in row['local_references']):
            errors.append('manifest dependency: ' + row['id'])
    return errors


class RetirementInventoryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / INVENTORY).read_text())

    def test_catalogue_and_all_five_manifests_are_covered(self):
        self.assertEqual(len(list(ROOT.glob('skills/*/manifest.json'))), 5)
        self.assertEqual({m['path'] for m in self.data['coverage']['manifests']},
                         {p for p in self.data['base_files'] if re.fullmatch(r'skills/[^/]+/manifest.json', p)})
        self.assertEqual(len([x for x in expected_units(self.data) if x.startswith('operation:')]), 12)
        self.assertEqual(validate_inventory(self.data), [])

    def test_snapshot_is_bound_to_actual_git_tree_and_commit(self):
        self.assertEqual(snapshot_tree_sha(self.data['base_files']), self.data['base_tree'])
        commit = self.data['base_commit_object']
        self.assertEqual(object_sha('commit', commit.encode()), self.data['base_commit'])
        self.assertTrue(commit.startswith('tree ' + self.data['base_tree'] + '\n'))
        for path, text in self.data['source_snapshots'].items():
            self.assertEqual(object_sha('blob', text.encode()), self.data['base_files'][path]['sha'])

    def test_later_caller_drift_blocks_switch_without_freezing_unrelated_build(self):
        row = self.data['entries'][0]
        changed = row['local_references'][0]['path']
        original = blob_sha
        with patch(__name__ + '.blob_sha', side_effect=lambda p: '0' * 40 if p == changed else original(p)):
            self.assertIn(changed, stale_for_switch(self.data, row))
            self.assertEqual(validate_inventory(self.data), [])

    def test_omitted_unit_is_rejected(self):
        self.data['entries'].pop()
        self.assertIn('unit coverage', validate_inventory(self.data))

    def test_corrupt_blob_and_caller_locator_are_rejected(self):
        row = self.data['entries'][0]
        row['blob_sha'] = '0' * 40
        row['local_references'][0]['lines'] = [999999]
        errors = validate_inventory(self.data)
        self.assertTrue(any(e.startswith('path/blob:') for e in errors))
        self.assertTrue(any(e.startswith('caller locator:') for e in errors))

    def test_active_manifest_reference_cannot_disappear(self):
        row = next(r for r in self.data['entries'] if r['id'].startswith('method:'))
        row['local_references'] = [c for c in row['local_references'] if c['path'] != row['source']['path']]
        self.assertIn('manifest dependency: ' + row['id'], validate_inventory(self.data))

    def test_omitted_non_manifest_caller_is_rejected(self):
        row = self.data['entries'][0]
        row['local_references'].pop()
        self.assertIn('caller coverage: ' + row['id'], validate_inventory(self.data))

    def test_changed_registry_pin_is_rejected(self):
        row = next(r for r in self.data['entries'] if any('json_pointer' in p for p in r['known_pins']))
        pin = next(p for p in row['known_pins'] if 'json_pointer' in p)
        pin['value'] = '0' * 40
        self.assertIn('pin locator: ' + row['id'], validate_inventory(self.data))

    def test_coordinated_pin_and_witness_forgery_is_rejected(self):
        row = next(r for r in self.data['entries'] if any('json_pointer' in p for p in r['known_pins']))
        pin = next(p for p in row['known_pins'] if 'json_pointer' in p)
        pin['value'] = pin['witness'] = '0' * 40
        self.assertIn('pin locator: ' + row['id'], validate_inventory(self.data))

    def test_pin_locators_are_checked_against_source(self):
        original = copy.deepcopy(self.data)
        for kind, value in [('line', 999999), ('line', 0), ('line', True),
                            ('json_pointer', '/missing'), ('json_pointer', '/source/~2bad')]:
            with self.subTest(kind=kind, value=value):
                self.data = copy.deepcopy(original)
                row = next(r for r in self.data['entries'] if any(kind in p for p in r['known_pins']))
                pin = next(p for p in row['known_pins'] if kind in p)
                pin[kind] = value
                self.assertIn('pin locator: ' + row['id'], validate_inventory(self.data))

    def test_pin_source_drift_blocks_switch_without_global_freeze(self):
        row = next(r for r in self.data['entries'] if any('json_pointer' in p for p in r['known_pins']))
        changed = next(p['path'] for p in row['known_pins'] if 'json_pointer' in p)
        original = blob_sha
        with patch(__name__ + '.blob_sha', side_effect=lambda p: '0' * 40 if p == changed else original(p)):
            self.assertIn(changed, stale_for_switch(self.data, row))
            self.assertEqual(validate_inventory(self.data), [])

    def test_json_pointer_escaping_and_array_bounds(self):
        source = {'a/b': {'~key': ['actual-pin']}}
        self.assertEqual(pointer_value(source, '/a~1b/~0key/0'), 'actual-pin')
        self.assertEqual(pointer_value(source, ''), source)
        for pointer in ['a/b', '/a~1b/~0key/-1', '/a~1b/~0key/01',
                        '/a~1b/~0key/1', '/a~1b/~2key', '/missing']:
            with self.subTest(pointer=pointer), self.assertRaises((ValueError, KeyError, IndexError)):
                pointer_value(source, pointer)

    def test_unknown_or_missing_equivalence_blocks_only_that_candidate(self):
        first, second = self.data['entries'][:2]
        for row in (first, second):
            row.update(decision='proposed-remove', retirement_eligible=True, external_callers='VERIFIED_NONE')
            row['equivalence'] = {'status': 'VERIFIED', 'evidence': ['synthetic gate witness, not a delivered equivalence']}
            row['local_references'] = []
            row['switch_condition'] = 'all verified callers switched'
        first['external_callers'] = 'UNKNOWN'
        errors = validate_inventory(self.data)
        self.assertEqual([e for e in errors if e.startswith('retirement gate:')], ['retirement gate: ' + first['id']])
        first['external_callers'] = 'VERIFIED_NONE'
        first['equivalence']['status'] = 'MISSING'
        self.assertIn('retirement gate: ' + first['id'], validate_inventory(self.data))

    def test_inventory_preserves_all_units_and_does_not_authorize_removal(self):
        self.assertTrue(all(r['decision'] == 'keep' and not r['retirement_eligible'] for r in self.data['entries']))
        self.assertEqual(self.data['authorized_mutations'], [])
        self.assertRegex(self.data['base_commit'], r'^[0-9a-f]{40}$')
        self.assertTrue(self.data['coverage']['exclusions'])


if __name__ == '__main__':
    unittest.main()
