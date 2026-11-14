import copy
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from adoption import analyze_adoption
from analysis_impact import plan_analysis_revision
from planning import CATALOG, validate_planned_analysis
from runtime import validate_study
from writing import EVIDENCE_KEYS, study_hash


def sample():
    fixture=json.loads((ROOT/'fixtures/convergence-adoption.json').read_text())
    study,brief=fixture['study'],fixture['brief']
    plan=dict(schema_version='1.0',id='PLAN1',study_ref=study['id'],intent_ref=brief['id'],
              input_revision=study_hash({k:study[k] for k in EVIDENCE_KEYS if k in study}),
              intent_revision=study_hash(brief),catalog_revision=study_hash(CATALOG),
              questions=[fixture['question']],budget={'max_publications':70,'max_queries':20})
    return study,brief,plan,fixture['measurements'],fixture['expected']


def run_method(study,brief,plan,measurements):
    return analyze_adoption(study,brief,plan,'Q1',measurements,analysis_id='A1')


class AdoptionTests(unittest.TestCase):
    def test_actual_method_from_claims_validates_and_remains_inference(self):
        study,brief,plan,measurements,expected=sample()
        before=copy.deepcopy((study,brief,plan,measurements))
        result=run_method(study,brief,plan,measurements)
        self.assertEqual(expected['percentage'],result['method_output']['percentage'])
        row=result['envelope']['analyses'][0]
        self.assertEqual(expected['state'],row['state'])
        self.assertEqual(expected['status'],row['findings'][0]['status'])
        self.assertEqual(['C1','C2','C3'],row['findings'][0]['claim_refs'])
        self.assertTrue(validate_planned_analysis(result['envelope'],plan,brief,study)['valid'])
        self.assertFalse(result['human_approval'])
        self.assertEqual(before,(study,brief,plan,measurements))
        self.assertEqual([],validate_study(study)['errors'])
        impact=plan_analysis_revision(study,result['envelope'],['SRC1'],
                                     expected_study_hash=study_hash(study),expected_envelope_hash=study_hash(result['envelope']))
        self.assertEqual(['A1'],impact['invalidate_analysis_ids'])

    def test_zero_numerator_is_zero_but_zero_denominator_is_unknown(self):
        study,brief,plan,m,_=sample();m['active']['value']=0
        self.assertEqual('0.00',run_method(study,brief,plan,m)['method_output']['percentage'])
        m['eligible']['value']=0
        result=run_method(study,brief,plan,m)
        self.assertIsNone(result['method_output']['percentage'])
        self.assertEqual([],result['envelope']['analyses'][0]['findings'])
        self.assertEqual('partial',result['envelope']['analyses'][0]['state'])

    def test_missing_values_or_context_are_partial_without_invented_conclusion(self):
        for key in ('eligible','active','cohort','period','frequency'):
            study,brief,plan,m,_=sample()
            if key in ('eligible','active'): m[key]={'value':None,'claim_refs':[]}
            else: m[key]=None
            result=run_method(study,brief,plan,m)
            row=result['envelope']['analyses'][0]
            self.assertEqual('partial',row['state'],key)
            self.assertTrue(row['unknowns'])
            self.assertTrue(row['needs_research'])
            self.assertEqual([],row['findings'])

    def test_required_evidence_gap_prevents_complete_result(self):
        study,brief,plan,m,_=sample()
        plan['questions'][0]['evidence_map']=[e for e in plan['questions'][0]['evidence_map'] if e['requirement']!='period']
        result=run_method(study,brief,plan,m)
        self.assertEqual('partial',result['envelope']['analyses'][0]['state'])
        self.assertEqual([],result['envelope']['analyses'][0]['findings'])

    def test_invalid_counts_units_refs_or_shape_rejected(self):
        for value in (-1,True,1.5,'12'):
            study,brief,plan,m,_=sample();m['active']['value']=value
            with self.assertRaises(ValueError): run_method(study,brief,plan,m)
        for key,value in [('unit','euros'),('extra',True),('eligible',{'value':40,'claim_refs':[]}),
                          ('active',{'value':12,'claim_refs':['C1']}),
                          ('active',{'value':41,'claim_refs':['C2']})]:
            study,brief,plan,m,_=sample();m[key]=value
            with self.assertRaises(ValueError): run_method(study,brief,plan,m)

    def test_source_change_requires_new_plan(self):
        study,brief,plan,m,_=sample();study['fragments'][0]['text']='Changed source'
        with self.assertRaises(ValueError): run_method(study,brief,plan,m)

    def test_rounding_is_explicit(self):
        study,brief,plan,m,_=sample();m['eligible']['value']=3;m['active']['value']=1
        result=run_method(study,brief,plan,m)
        self.assertEqual('33.33',result['method_output']['percentage'])
        self.assertIn('HALF_UP',result['method_output']['rounding'])
        self.assertEqual(study_hash(m),result['method_output']['measurements_revision'])


if __name__=='__main__':unittest.main()
