import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from analysis_impact import plan_analysis_revision
from writing import EVIDENCE_KEYS, study_hash


def sample():
    study = json.loads((ROOT / 'fixtures/synthetic.json').read_text())
    study['relations'] = []  # independent source branches in this oracle
    study['sources'].append(dict(id='SRC-2', kind='synthetic_fixture', access='synthetic', title='Independent branch', locator='fixture:independent'))
    study['fragments'].append(dict(id='F-2', source_id='SRC-2', locator='line 1', text='Independent unknown baseline'))
    study['claims'][2]['fragment_ids'] = ['F-2']
    analyses = []
    for ordinal, claim in enumerate(('C-1', 'C-3'), 1):
        analyses.append(dict(id=f'A{ordinal}', question_ref=f'Q{ordinal}', question='What is documented?',
                             method='synthetic-review', method_version='v1', scope='synthetic', as_of='2026-11-14',
                             input_claim_refs=[claim], findings=[dict(statement='Attributed observation only',
                             status='attributed_claim', claim_refs=[claim])], counterevidence=[], unknowns=[],
                             state='complete', needs_research=False))
    env = dict(schema_version='1.0', study_ref=study['id'], analyses=analyses,
               input_revision=study_hash({k: study[k] for k in EVIDENCE_KEYS if k in study}))
    return study, env


def impact(study, env, ids):
    return plan_analysis_revision(study, env, ids, expected_study_hash=study_hash(study),
                                  expected_envelope_hash=study_hash(env))


class ImpactTests(unittest.TestCase):
    def test_source_invalidates_only_descendant_analysis_and_preserves_inputs(self):
        study, env = sample(); before = copy.deepcopy((study, env))
        receipt = impact(study, env, ['SRC-1'])
        self.assertEqual(['C-1'], receipt['claim_ids'])
        self.assertEqual(['A1'], receipt['invalidate_analysis_ids'])
        self.assertEqual(['Q1'], receipt['question_refs'])
        self.assertEqual(['A2'], receipt['untouched_analysis_ids'])
        self.assertFalse(receipt['human_approval'])
        self.assertFalse(receipt['envelope_refreshed'])
        self.assertEqual(before, (study, env))
        self.assertIn('P-1', receipt['writing']['paragraph_ids'])
        self.assertEqual(['A2'], impact(study, env, ['SRC-2'])['invalidate_analysis_ids'])

    def test_claim_delta_and_relations_reuse_existing_closure(self):
        study, env = sample()
        self.assertEqual(['A1'], impact(study, env, ['C-1'])['invalidate_analysis_ids'])
        study['relations'] = [dict(id='R1', **{'from':'C-3','to':'C-1'}, kind='depends_on', rationale='synthetic'),
                              dict(id='R2', **{'from':'C-1','to':'C-3'}, kind='depends_on', rationale='synthetic')]
        env['input_revision'] = study_hash({k: study[k] for k in EVIDENCE_KEYS if k in study})
        receipt = impact(study, env, ['SRC-1'])
        self.assertEqual(['A1', 'A2'], receipt['invalidate_analysis_ids'])
        self.assertEqual([], receipt['untouched_analysis_ids'])

    def test_layout_does_not_invalidate_analysis(self):
        study, env = sample()
        section = study['sections'][0]['id']
        paragraph = study['sections'][0]['paragraphs'][0]['id']
        for ident in (section, paragraph):
            receipt = impact(study, env, [ident])
            self.assertEqual([], receipt['invalidate_analysis_ids'])
            self.assertEqual(['A1', 'A2'], receipt['untouched_analysis_ids'])

    def test_analysis_output_delta_and_empty_change(self):
        study, env = sample()
        receipt = impact(study, env, ['A2'])
        self.assertEqual(['A2'], receipt['invalidate_analysis_ids'])
        self.assertEqual([], receipt['claim_ids'])
        self.assertEqual([], receipt['writing']['paragraph_ids'])
        self.assertEqual([], impact(study, env, [])['invalidate_analysis_ids'])

    def test_stale_leases_and_unknown_ids_refused(self):
        study, env = sample()
        for key in ('expected_study_hash', 'expected_envelope_hash'):
            args = dict(expected_study_hash=study_hash(study), expected_envelope_hash=study_hash(env))
            args[key] = '0' * 64
            with self.assertRaises(ValueError): plan_analysis_revision(study, env, ['C-1'], **args)
        with self.assertRaises(ValueError): impact(study, env, ['UNKNOWN'])
        with self.assertRaises(TypeError): plan_analysis_revision(study, env, ['C-1'])

    def test_malformed_changes_and_envelope_rejected(self):
        study, env = sample()
        for ids in ('C-1', [None], [[]], ['C-1', 'C-1']):
            with self.assertRaises(ValueError): impact(study, env, ids)
        env['analyses'][0]['input_claim_refs'] = ['foreign']
        with self.assertRaises(ValueError): impact(study, env, ['SRC-1'])

    def test_analysis_id_cannot_collide_with_any_study_node(self):
        study, env = sample()
        env['analyses'][0]['id'] = 'SRC-1'
        with self.assertRaises(ValueError): impact(study, env, ['SRC-1'])


if __name__ == '__main__':
    unittest.main()
