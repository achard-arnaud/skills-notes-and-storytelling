import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from analysis import SCHEMA, validate_analysis_envelope, validate_legacy_analysis_result


def sample(case_index=0):
    fixture = json.loads((ROOT / 'fixtures/analysis-contract-mapping.json').read_text())
    study = fixture['study']
    # Independent canonical-hash oracle, never computed by the function under test.
    evidence = {k: study[k] for k in ('id', 'title', 'mandate', 'pillars', 'sources', 'fragments', 'claims', 'relations') if k in study}
    revision = hashlib.sha256(json.dumps(evidence, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
    case = fixture['cases'][case_index]
    row = dict(id='A1', question_ref=case['question']['id'], question=case['question']['text'],
               method='evidence-review', method_version='synthetic-v1', scope='synthetic study',
               as_of='2026-11-14', input_claim_refs=case['input_claim_refs'],
               findings=case.get('analysis', {}).get('findings', []), counterevidence=[],
               unknowns=case.get('missing_evidence', []),
               state='complete' if case_index == 0 else 'partial', needs_research=case_index != 0)
    return study, dict(schema_version='1.0', study_ref=study['id'], input_revision=revision, analyses=[row])


class AnalysisTests(unittest.TestCase):
    def test_legacy_schema_is_exact_pinned_donor(self):
        raw = (json.dumps(SCHEMA['$defs']['legacyResult'], indent=2, ensure_ascii=False) + '\n').encode()
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        self.assertEqual('b2303d0bd50e23a7c7a2ad7eb71b896fcacdc446', blob)

    def test_schema_uses_only_supported_vocabulary(self):
        keywords = {'$schema', '$id', 'title', '$defs', '$ref', 'type', 'additionalProperties',
                    'required', 'properties', 'const', 'enum', 'minLength', 'pattern', 'format',
                    'minItems', 'uniqueItems', 'items', 'allOf', 'if', 'then'}
        def check(node):
            self.assertFalse(set(node) - keywords)
            for key, value in node.items():
                if key in ('properties', '$defs'):
                    for child in value.values():
                        check(child)
                elif key in ('items', 'if', 'then'):
                    check(value)
                elif key == 'allOf':
                    for child in value:
                        check(child)
        check(SCHEMA)

    def test_nominal_before_blocks_and_no_mutation(self):
        study, envelope = sample()
        before = copy.deepcopy((study, envelope))
        result = validate_analysis_envelope(envelope, study)
        self.assertEqual([], result['errors'])
        self.assertTrue(result['valid'])
        self.assertFalse(result['human_approval'])
        self.assertEqual(before, (study, envelope))
        self.assertEqual('recommendation', envelope['analyses'][0]['findings'][1]['status'])
        self.assertEqual('attributed_claim', study['claims'][0]['status'])

    def test_partial_matches_independent_oracle(self):
        study, envelope = sample(1)
        result = validate_analysis_envelope(envelope, study)
        self.assertTrue(result['valid'], result)
        self.assertTrue(result['gaps'])
        self.assertEqual([], envelope['analyses'][0]['findings'])
        self.assertNotIn('affects_blocks', envelope['analyses'][0])

    def test_partial_requires_gaps_and_research(self):
        for key, value in [('unknowns', []), ('needs_research', False)]:
            study, envelope = sample(1)
            envelope['analyses'][0][key] = value
            self.assertFalse(validate_analysis_envelope(envelope, study)['valid'])

    def test_complete_without_findings_or_inputs_rejected(self):
        for key in ('findings', 'input_claim_refs'):
            study, envelope = sample()
            envelope['analyses'][0][key] = []
            self.assertFalse(validate_analysis_envelope(envelope, study)['valid'])

    def test_refs_and_foreign_study(self):
        for location in ('input', 'finding', 'study'):
            study, envelope = sample()
            if location == 'study':
                envelope['study_ref'] = 'foreign-study'
            elif location == 'input':
                envelope['analyses'][0]['input_claim_refs'].append('foreign-C1')
            else:
                envelope['analyses'][0]['findings'][0]['claim_refs'] = ['foreign-C1']
            result = validate_analysis_envelope(envelope, study)
            self.assertTrue(result['reference_errors'])
            self.assertFalse(result['valid'])

    def test_duplicate_and_collision(self):
        for ident in ('A1', 'C1'):
            study, envelope = sample()
            extra = copy.deepcopy(envelope['analyses'][0])
            extra['id'] = ident
            envelope['analyses'].append(extra)
            self.assertFalse(validate_analysis_envelope(envelope, study)['valid'])

    def test_revision_and_study_identity_required(self):
        for key in ('input_revision', 'study_ref'):
            study, envelope = sample()
            del envelope[key]
            self.assertFalse(validate_analysis_envelope(envelope, study)['valid'])

    def test_evidence_change_stales_but_layout_does_not(self):
        study, envelope = sample()
        study['sections'] = [{'id': 'B1', 'paragraphs': [{'text': 'layout only'}]}]
        study['layout'] = {'font': 'sans'}
        self.assertTrue(validate_analysis_envelope(envelope, study)['valid'])
        study['claims'][0]['text'] = 'changed source assertion'
        result = validate_analysis_envelope(envelope, study)
        self.assertFalse(result['valid'])
        self.assertTrue(any('revision' in e for e in result['reference_errors']))

    def test_versions_types_dates_statuses_and_unknown_fields(self):
        cases = [('schema_version', 1), ('schema_version', '2.0'), ('analyses', {}), ('input_revision', 'x')]
        for key, value in cases:
            study, envelope = sample()
            envelope[key] = value
            self.assertFalse(validate_analysis_envelope(envelope, study)['valid'])
        for key, value in [('as_of', '2026-02-30'), ('as_of', '20261114'), ('needs_research', 1),
                           ('question_ref', ''), ('method_version', None), ('findings', None),
                           ('unknowns', [3]), ('unexpected', 'x')]:
            study, envelope = sample()
            envelope['analyses'][0][key] = value
            self.assertFalse(validate_analysis_envelope(envelope, study)['valid'], key)
        study, envelope = sample()
        envelope['analyses'][0]['findings'][0]['status'] = 'verified_fact'
        self.assertFalse(validate_analysis_envelope(envelope, study)['valid'])

    def test_malformed_inputs_return_errors_without_crash(self):
        study, envelope = sample()
        for bad in (None, [], 3, 'x', {'analyses': [None]}):
            self.assertFalse(validate_analysis_envelope(bad, study)['valid'])
        for bad in (None, [], {'id': 's', 'claims': None}, {'id': 's', 'claims': [None]},
                    {'id': 's', 'claims': [{'id': []}]}):
            self.assertFalse(validate_analysis_envelope(envelope, bad)['valid'])

    def test_legacy_explicit_and_unchanged(self):
        study, envelope = sample()
        row = envelope['analyses'][0]
        legacy = {k: copy.deepcopy(v) for k, v in row.items() if k not in ('question_ref', 'state', 'needs_research')}
        legacy['affects_blocks'] = ['B1']
        before = copy.deepcopy(legacy)
        result = validate_legacy_analysis_result(legacy, study)
        self.assertTrue(result['valid'], result)
        self.assertTrue(result['gaps'])  # no original study/revision asserted
        self.assertEqual(before, legacy)
        self.assertFalse(validate_analysis_envelope(legacy, study)['valid'])
        for key in ('findings', 'affects_blocks', 'input_claim_refs'):
            bad = copy.deepcopy(legacy)
            bad[key] = []
            self.assertFalse(validate_legacy_analysis_result(bad, study)['valid'])
        legacy['question_ref'] = 'Q1'
        self.assertFalse(validate_legacy_analysis_result(legacy, study)['valid'])

    def test_legacy_partial_oracle_rejected(self):
        study, envelope = sample(1)
        row = envelope['analyses'][0]
        legacy = {k: v for k, v in row.items() if k not in ('question_ref', 'state', 'needs_research')}
        legacy['affects_blocks'] = ['B1']
        self.assertFalse(validate_legacy_analysis_result(legacy, study)['valid'])


if __name__ == '__main__':
    unittest.main()
