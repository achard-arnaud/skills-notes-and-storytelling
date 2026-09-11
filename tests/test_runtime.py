import copy,json,unittest
from pathlib import Path
from src.runtime import plan,validate,packet,search_plan,revise

def fixture():
 intake={'environment':'chat','documents':['manual.pdf'],'entities':['A','B']}
 return {'intake':intake,'profile':plan(intake),'sources':[{'id':'S1','origin':'manual','family':'vendor','coverage_status':'read'}],
 'fragments':[{'id':'F1','source_id':'S1','source_locator':'physical page 2','content':'Vendor says value rises','evidence_status':'vendor_claim'}],
 'claims':[{'id':'C1','statement':'Vendor claims value rises','claim_type':'attributed_claim','fragment_ids':['F1'],'decision_relevance':5},
 {'id':'C2','statement':'Value may not rise','claim_type':'hypothesis','fragment_ids':[]},
 {'id':'C3','statement':'Unrelated question','claim_type':'unknown','fragment_ids':[]}],
 'edges':[{'from':'C2','to':'C1','type':'contradicts'}],
 'sections':[{'id':'SEC1','action_title':'Value remains to be tested','claim_ids':['C1','C2']}],
 'side_stories':[{'id':'SS1','kind':'method','claim_ids':['C1'],'section_anchor':'SEC1','return_to':None}],
 'gaps':[{'id':'G1','status':'open','reason':'independence','query':'independent value','target_claim_ids':['C1']}]}

class RuntimeTests(unittest.TestCase):
 def test_documents_force_heavy_in_chat(self):
  p=plan({'environment':'chat','execution':'light','documents':['a']});self.assertEqual(p['execution'],'heavy');self.assertEqual(p['packet_words'],2000)
 def test_cowork_alias(self):self.assertEqual(plan({'environment':'cowork'})['environment'],'work')
 def test_debug_orthogonal(self):
  p=plan({'environment':'chat','debug':True});self.assertTrue(p['debug']);self.assertEqual(p['execution'],'light')
 def test_reasoning_not_claimed_applied(self):self.assertFalse(plan({'entities':['a','b']})['reasoning_applied'])
 def test_bad_mode_rejected(self):
  with self.assertRaises(ValueError):plan({'generation':'retro-engineering'})
 def test_iterative_baseline_required(self):
  with self.assertRaises(ValueError):plan({'generation':'iterative'})
 def test_valid(self):self.assertEqual(validate(fixture()),[])
 def test_vendor_cannot_be_fact(self):
  r=fixture();r['claims'][0]['claim_type']='fact';self.assertTrue(validate(r))
 def test_unknown_without_fake_evidence(self):self.assertEqual(validate(fixture()),[])
 def test_broken_source(self):
  r=fixture();r['fragments'][0]['source_id']='absent';self.assertTrue(validate(r))
 def test_broken_fragment(self):
  r=fixture();r['claims'][0]['fragment_ids']=['absent'];self.assertTrue(validate(r))
 def test_duplicate(self):
  r=fixture();r['claims'].append(r['claims'][0]);self.assertTrue(validate(r))
 def test_contradiction_preserved(self):
  p=packet(fixture(),['C1']);self.assertEqual({c['id'] for c in p['claims']},{'C1','C2'});self.assertEqual(p['preserved_claim_ids'],['C3'])
 def test_fragment_zoom(self):self.assertEqual(len(packet(fixture(),['F1'])['claims']),2)
 def test_section_zoom(self):self.assertEqual(len(packet(fixture(),['SEC1'])['claims']),2)
 def test_missing_target(self):
  with self.assertRaises(ValueError):packet(fixture(),['absent'])
 def test_overflow_no_loss(self):
  p=packet(fixture(),['C1'],budget=1);self.assertTrue(p['budget']['overflow']);self.assertEqual(len(p['claims']),2)
 def test_causal_mechanism(self):
  r=fixture();r['edges'][0]['type']='causes';self.assertTrue(validate(r))
 def test_narrative_return_required(self):
  r=fixture();r['side_stories'][0]['kind']='callback';self.assertTrue(validate(r))
 def test_manual_first(self):
  r=fixture();r['sources'][0]['coverage_status']='unread';self.assertFalse(search_plan(r)['queries'])
 def test_dedup_queries(self):
  r=fixture();r['gaps'].append(dict(r['gaps'][0],id='G2'));self.assertEqual(len(search_plan(r)['queries']),1)
 def test_search_reason(self):
  r=fixture();r['gaps'][0]['reason']='decoration'
  with self.assertRaises(ValueError):search_plan(r)
 def test_packet_does_not_mutate(self):
  r=fixture();before=copy.deepcopy(r);packet(r,['C1']);self.assertEqual(r,before)
 def test_revision_preserves_unrelated(self):
  r=fixture();r['run_id']='v1';old=copy.deepcopy(r)
  row=dict(r['claims'][0],statement='Revised attributed proposition')
  new=revise(r,[{'family':'claims','record':row}],['C1'],'v1','deepen')
  self.assertEqual(new['claims'][2],r['claims'][2]);self.assertEqual(r,old)
 def test_revision_rejects_unrelated(self):
  r=fixture();r['run_id']='v1'
  with self.assertRaises(ValueError):revise(r,[{'family':'claims','record':r['claims'][2]}],['C1'],'v1','deepen')
 def test_scoped_coverage_requires_details(self):
  r=fixture();r['sources'][0]['coverage_status']='scoped';self.assertTrue(validate(r))
 def test_legacy_claim_schema_unknown(self):
  from jsonschema import Draft202012Validator
  schema=json.loads((Path(__file__).resolve().parents[1]/'contracts/claim.schema.json').read_text())
  c=dict(id='C',statement='unknown',claim_type='unknown',fragment_ids=[],decision_relevance=0)
  self.assertEqual(list(Draft202012Validator(schema).iter_errors(c)),[])
  c['claim_type']='fact';self.assertTrue(list(Draft202012Validator(schema).iter_errors(c)))
 def test_legacy_configuration_aliases(self):
  p=plan({'execution_mode':'chat','runtime_mode':'debug','documents':['d']})
  self.assertEqual(p['execution'],'heavy');self.assertTrue(p['debug'])
 def test_effort_from_configuration(self):
  p=plan({});self.assertEqual(next(x['effort'] for x in p['stage_efforts'] if x['stage']=='claims_arbitration'),'high')
 def test_all_templates_have_layers(self):
  root=Path(__file__).resolve().parents[1];profiles=json.loads((root/'templates/profiles.json').read_text())['profiles']
  manifest=json.loads((root/'templates/manifest.json').read_text())
  self.assertEqual(set(profiles),{t['type'] for t in manifest['templates']})
  for p in profiles.values():self.assertEqual(set(p),{'template','narrative','scaffold','writing'})

if __name__=='__main__':unittest.main()
