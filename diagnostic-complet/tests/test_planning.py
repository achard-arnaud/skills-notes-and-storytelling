import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from planning import CATALOG, resolve_question, validate_analysis_plan, validate_planned_analysis
from writing import EVIDENCE_KEYS, study_hash


def sample():
    study = {'id': 'S1', 'claims': [
        {'id': 'C1', 'text': '40 eligible; 12 performed the useful weekly task in cohort W1.', 'status': 'attributed_claim'},
        {'id': 'C2', 'text': 'Frequency, exclusions and dates need confirmation.', 'status': 'unknown'}]}
    brief = dict(schema_version='1.0', id='I1', study_ref='S1', question='What supports the adoption claim?',
                 scope='Synthetic product, cohort W1', audience='Product reader', intent='traction-commerciale',
                 decision_requested=False, as_of='2026-11-14')
    question = dict(id='Q1', question='What is the useful weekly adoption?', method='product.adoption',
                    method_version='514cac66e7fe571d85e2dd71e65142f481148b20', input_claim_refs=['C1', 'C2'],
                    evidence_map=[dict(requirement=r, claim_refs=['C1']) for r in
                                  ('eligible_population', 'useful_event', 'expected_frequency', 'cohort', 'period')],
                    unknowns=[], queries=['Find the dated cohort and exclusions'],
                    stop_condition='Dated cohort and denominator documented, otherwise retain the gap')
    plan = dict(schema_version='1.0', id='P1', intent_ref='I1', study_ref='S1',
                input_revision=study_hash({k: study[k] for k in EVIDENCE_KEYS if k in study}),
                intent_revision=study_hash(brief), catalog_revision=study_hash(CATALOG),
                questions=[question], budget={'max_publications': 70, 'max_queries': 20})
    return study, brief, plan


def envelope(study, brief, plan):
    q = plan['questions'][0]
    return dict(schema_version='1.0', study_ref=study['id'], input_revision=plan['input_revision'], analyses=[
        dict(id='A1', question_ref=q['id'], question=q['question'], method=q['method'],
             method_version=q['method_version'], scope=brief['scope'], as_of=brief['as_of'],
             input_claim_refs=q['input_claim_refs'][:], state='complete', needs_research=False,
             findings=[dict(statement='The declared cohort reports 30% weekly adoption; independent use is unverified.',
                            status='inference', claim_refs=['C1'])], counterevidence=[], unknowns=[])])


class PlanningTests(unittest.TestCase):
    def test_resolves_before_scaffold_without_executing_analysis(self):
        study, brief, plan = sample()
        before = copy.deepcopy((study, brief, plan, CATALOG))
        result = resolve_question(plan, brief, study, 'Q1')
        self.assertEqual('ready_for_analysis', result['state'])
        self.assertEqual('product.adoption', result['method']['id'])
        self.assertEqual('514cac66e7fe571d85e2dd71e65142f481148b20', result['method']['method_version'])
        self.assertFalse(result['analysis_executed'])
        self.assertFalse(result['human_approval'])
        self.assertNotIn('affects_blocks', result)
        self.assertNotIn('sections', result)
        self.assertEqual(before, (study, brief, plan, CATALOG))
        result['question']['unknowns'].append('caller edit')
        self.assertEqual([], plan['questions'][0]['unknowns'])

    def test_missing_evidence_is_research_gap_not_fake_conclusion(self):
        study, brief, plan = sample()
        plan['questions'][0]['evidence_map'] = []
        result = validate_analysis_plan(plan, brief, study)
        self.assertTrue(result['valid'], result)
        self.assertEqual(5, len(result['gaps'][0]['missing_requirements']))
        packet = resolve_question(plan, brief, study, 'Q1')
        self.assertEqual('needs_research', packet['state'])
        self.assertNotIn('findings', packet)
        self.assertEqual(2, len(study['claims']))

    def test_unknowns_remain_visible_even_with_complete_mapping(self):
        study, brief, plan = sample()
        plan['questions'][0]['unknowns'] = ['No independent cohort available']
        packet = resolve_question(plan, brief, study, 'Q1')
        self.assertEqual('needs_research', packet['state'])
        self.assertEqual(['No independent cohort available'], packet['gaps'][0]['unknowns'])

    def test_input_brief_and_catalog_revisions_must_match(self):
        for target in ('study', 'brief', 'catalog_revision'):
            study, brief, plan = sample()
            if target == 'study': study['claims'][0]['text'] = 'Changed'
            elif target == 'brief': brief['scope'] = 'Other population'
            else: plan['catalog_revision'] = '0' * 64
            result = validate_analysis_plan(plan, brief, study)
            self.assertFalse(result['valid'], target)
            self.assertTrue(result['reference_errors'])

    def test_layout_does_not_stale_plan(self):
        study, brief, plan = sample()
        study['sections'] = [{'id': 'B1', 'title': 'New layout'}]
        self.assertTrue(validate_analysis_plan(plan, brief, study)['valid'])

    def test_identity_and_reference_failures(self):
        for key, value in [('intent_ref', 'other'), ('study_ref', 'foreign')]:
            study, brief, plan = sample(); plan[key] = value
            self.assertFalse(validate_analysis_plan(plan, brief, study)['valid'])
        for key, value in [('id', 'C1'), ('method', 'porter'), ('method_version', 'unknown'),
                           ('input_claim_refs', ['foreign']),
                           ('evidence_map', [{'requirement': 'imagined', 'claim_refs': ['C1']}])]:
            study, brief, plan = sample(); plan['questions'][0][key] = value
            self.assertFalse(validate_analysis_plan(plan, brief, study)['valid'], key)
        study, brief, plan = sample()
        plan['questions'].append(copy.deepcopy(plan['questions'][0]))
        self.assertFalse(validate_analysis_plan(plan, brief, study)['valid'])
        with self.assertRaises(ValueError): resolve_question(sample()[2], sample()[1], sample()[0], 'missing')

    def test_evidence_refs_must_be_declared_inputs_and_requirements_unique(self):
        study, brief, plan = sample()
        plan['questions'][0]['input_claim_refs'] = ['C2']
        self.assertFalse(validate_analysis_plan(plan, brief, study)['valid'])
        study, brief, plan = sample()
        plan['questions'][0]['evidence_map'].append(copy.deepcopy(plan['questions'][0]['evidence_map'][0]))
        self.assertFalse(validate_analysis_plan(plan, brief, study)['valid'])

    def test_bad_shapes_and_versions_rejected(self):
        for key, value in [('schema_version', '2.0'), ('questions', []), ('budget', {'max_publications': True, 'max_queries': -1})]:
            study, brief, plan = sample(); plan[key] = value
            self.assertFalse(validate_analysis_plan(plan, brief, study)['valid'])
        for key, value in [('decision_requested', 'yes'), ('as_of', '2026-02-30'), ('intent', 'fiche-produit')]:
            study, brief, plan = sample(); brief[key] = value
            self.assertFalse(validate_analysis_plan(plan, brief, study)['valid'])
        for bad in (None, [], {'questions': [None]}):
            self.assertFalse(validate_analysis_plan(bad, sample()[1], sample()[0])['valid'])

    def test_result_matches_plan_but_does_not_gain_fact_status(self):
        study, brief, plan = sample()
        result = envelope(study, brief, plan)
        before = copy.deepcopy((study, brief, plan, result))
        self.assertTrue(validate_planned_analysis(result, plan, brief, study)['valid'])
        self.assertEqual(before, (study, brief, plan, result))
        self.assertEqual('attributed_claim', study['claims'][0]['status'])
        for key, value in [('method_version', 'foreign'), ('question_ref', 'Q404'), ('question', 'Other question'),
                           ('input_claim_refs', ['C1']), ('scope', 'All products')]:
            bad = copy.deepcopy(result); bad['analyses'][0][key] = value
            self.assertFalse(validate_planned_analysis(bad, plan, brief, study)['valid'], key)

    def test_recommendation_requires_explicit_decision_mandate(self):
        study, brief, plan = sample()
        result = envelope(study, brief, plan)
        result['analyses'][0]['findings'][0]['status'] = 'recommendation'
        self.assertFalse(validate_planned_analysis(result, plan, brief, study)['valid'])
        brief['decision_requested'] = True
        plan['intent_revision'] = study_hash(brief)
        self.assertTrue(validate_planned_analysis(result, plan, brief, study)['valid'])

    def test_declared_complete_cannot_hide_missing_requirements(self):
        study, brief, plan = sample()
        plan['questions'][0]['evidence_map'] = []
        result = envelope(study, brief, plan)
        self.assertFalse(validate_planned_analysis(result, plan, brief, study)['valid'])
        row = result['analyses'][0]
        row.update(state='partial', needs_research=True, findings=[], unknowns=['Missing denominator'])
        self.assertTrue(validate_planned_analysis(result, plan, brief, study)['valid'])


if __name__ == '__main__':
    unittest.main()
