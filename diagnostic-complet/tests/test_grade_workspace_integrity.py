"""Exercise the real evaluation CLI with isolated synthetic workspaces."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'evals/reinforce-kb-loopback/grade_workspace.py'
CASES = ('positive-hil-review', 'negative-directive-and-violations',
         'structure-type-review', 'clean-cycle-no-change',
         'refuse-human-adjudication', 'refuse-merge-without-source')
REFUSALS = CASES[-2:]


class GradeWorkspaceIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.evals = Path(self.temp.name) / 'evals'
        self.iteration = Path(self.temp.name) / 'iteration'
        self.hashes = {}
        for case in CASES:
            graph = self.evals / case / 'files/graph.json'
            graph.parent.mkdir(parents=True)
            graph.write_text(json.dumps({'nodes': [{'id': case}], 'edges': []}) + '\n')
            self.hashes[case] = hashlib.sha256(graph.read_bytes()).hexdigest()
            out = self.outputs(case)
            out.mkdir(parents=True)
            receipt = dict(decision='review_required', triggers_fired=[],
                           findings=dict(violations=0, alias_candidates=0, out_of_ontology=0),
                           automatic_mutations=False, automatic_promotion=False,
                           candidate_approval=False, actions=[], actions_by_kind={}, deferred_actions=0)
            if case == 'positive-hil-review':
                receipt['triggers_fired'] = ['hil_touched']
            elif case == 'negative-directive-and-violations':
                receipt['triggers_fired'] = ['directive_in_material']
                receipt['findings'].update(violations=3, alias_candidates=1)
            elif case == 'structure-type-review':
                receipt['findings'].update(violations=4, out_of_ontology=1)
                receipt['actions'] = [dict(kind='type_review', status='candidate_not_applied')]
                receipt['actions_by_kind'] = dict(type_review=1)
            elif case == 'clean-cycle-no-change':
                receipt['decision'] = 'no_change'
            (out / 'receipt.json').write_text(json.dumps(receipt))
            (out / 'response.md').write_text('Aucun déclencheur. Je refuse F1 et D1 ; decision_ref requis. source_review et counter_example_check.')
            self.set_hashes(case, self.hashes[case], self.hashes[case])

    def outputs(self, case):
        return self.iteration / case / 'with_skill/outputs'

    def set_hashes(self, case, before, after):
        for phase, value in [('before', before), ('after', after)]:
            (self.outputs(case) / ('graph.sha256.' + phase)).write_text(value + '\n')

    def grade(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.evals), str(self.iteration)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return {case: json.loads((self.iteration / case / 'with_skill/grading.json').read_text())['expectations']
                for case in CASES}

    def test_exact_fixture_hashes_preserve_all_twenty_one_expectations(self):
        grades = self.grade()
        self.assertEqual(sum(map(len, grades.values())), 21)
        self.assertTrue(all(e['passed'] for entries in grades.values() for e in entries))

    def test_identical_non_hash_strings_are_not_integrity_evidence(self):
        for case in REFUSALS:
            self.set_hashes(case, 'same-fixture-hash', 'same-fixture-hash')
        grades = self.grade()
        for case in REFUSALS:
            with self.subTest(case=case):
                self.assertFalse(grades[case][-1]['passed'])
                self.assertTrue(all(e['passed'] for e in grades[case][:-1]))

    def test_valid_but_foreign_sha256_is_rejected(self):
        for case in REFUSALS:
            self.set_hashes(case, '0' * 64, '0' * 64)
        grades = self.grade()
        for case in REFUSALS:
            with self.subTest(case=case):
                self.assertFalse(grades[case][-1]['passed'])

    def test_changed_after_hash_is_rejected(self):
        for case in REFUSALS:
            self.set_hashes(case, self.hashes[case], '1' * 64)
        grades = self.grade()
        self.assertTrue(all(not grades[case][-1]['passed'] for case in REFUSALS))

    def test_other_cases_and_expectations_are_unchanged_when_hashes_are_invalid(self):
        baseline = self.grade()
        for case in REFUSALS:
            self.set_hashes(case, '', '')
        graded = self.grade()
        for case in CASES[:-2]:
            self.assertEqual(graded[case], baseline[case])
        self.assertTrue(all(not graded[case][-1]['passed'] for case in REFUSALS))
