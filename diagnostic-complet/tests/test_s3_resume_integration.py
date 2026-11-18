"""End-to-end synthetic S3 resume coverage; no private RUN artifact is used."""
import copy
from html import escape
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT),str(ROOT/'tests')]
import context
from business_brief_content import freeze_business_brief_handoff
from planning import resolve_question
from render import anchor,render_study
from writing import study_hash
import test_contract_performance_convergence as contract_fixture
from test_convergence_replay import cold,phase2,save

FIXTURE=contract_fixture.FIXTURE


def scope(inputs):
    return {'id':'synthetic-contract-performance','subject':'Synthetic S3 resume integration',
            'input_revision':'a'*64,'scope':'Only the declared synthetic fixture',
            'authorized_inputs':inputs,'methods':['business.contracts-and-performance']}


class S3ResumeIntegrationTests(unittest.TestCase):
    def test_fresh_process_resumes_saved_artifacts_and_refuses_missing_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);payload=phase2(partial=True);save(folder,payload)
            result=cold(folder)
            self.assertEqual(0,result.returncode,result.stderr+result.stdout)
            restored=json.loads(result.stdout)
            self.assertEqual(payload['study']['id'],restored['study']['id'])
            self.assertEqual(payload['study']['claims'],restored['study']['claims'])
            self.assertTrue(restored['gaps'])
            expected=copy.deepcopy(restored)

            (folder/'phase2.json').unlink()
            refused=cold(folder)
            self.assertNotEqual(0,refused.returncode)
            self.assertNotIn('result_hash',refused.stdout)
            self.assertEqual(expected,restored)

    def test_stale_checkpoint_reopens_only_descendants_and_preserves_witness(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);source=folder/'amendment.json'
            source.write_text(json.dumps({'text':FIXTURE['amendment']}),encoding='utf-8')
            study_scope=scope(['amendment.json'])
            execution={'id':'s3-resume','base_sha':'synthetic-base-v1','tasks':[
                {'id':'analysis','status':'ready','depends_on':[],'study_scope':study_scope,
                 'outputs':['analysis.json'],'acceptance':['threshold qualified']},
            ]}
            packet=context.build_packet(folder,execution,'analysis',['amendment.json'],for_execution=True)
            checkpoint=context.checkpoint(folder,packet,next_task='brief')
            self.assertTrue(context.validate_checkpoint(folder,checkpoint,base_sha='synthetic-base-v1')['ok'])

            source.write_text(json.dumps({'text':FIXTURE['corrected_amendment']}),encoding='utf-8')
            stale=context.validate_checkpoint(folder,checkpoint,base_sha='synthetic-base-v1')
            self.assertFalse(stale['ok'])
            self.assertIn('stale input: amendment.json',stale['errors'])

            witness={'sha':'f'*64,'study_hash':'e'*64,'status':'verified'}
            board={'id':'s3-resume','base_sha':'synthetic-base-v1','tasks':[
                {'id':'analysis','status':'completed','depends_on':[],'study_scope':study_scope,
                 'receipt':{'sha':'a'*64}},
                {'id':'brief','status':'completed','depends_on':['analysis'],'study_scope':study_scope,
                 'receipt':{'sha':'b'*64}},
                {'id':'report','status':'completed','depends_on':['analysis'],'study_scope':study_scope,
                 'receipt':{'sha':'c'*64}},
                {'id':'witness','status':'completed','depends_on':[],'study_scope':study_scope,
                 'receipt':copy.deepcopy(witness)},
            ]}
            before=copy.deepcopy(board)
            invalidated=context.invalidate_descendants(board,['analysis'],study_id=study_scope['id'])
            by_id={task['id']:task for task in invalidated['tasks']}
            self.assertEqual({'analysis','brief','report'},
                             {key for key,item in by_id.items() if item['status']=='planned'})
            self.assertEqual(witness,by_id['witness']['receipt'])
            self.assertEqual(before,board)

    def test_corrected_brief_and_report_preserve_proof_unknown_and_navigation(self):
        helper=contract_fixture.ContractPerformanceConvergenceTests()
        helper.setUp()
        plan,envelope=helper.analysis(helper.study,FIXTURE['finding'])
        original=helper.project(helper.study,plan,envelope,'Report before correction')
        original_hash=study_hash(original['study'])

        corrected=copy.deepcopy(helper.study)
        corrected['fragments'][1]['text']=FIXTURE['corrected_amendment']
        corrected['claims'][1]['text']=FIXTURE['corrected_amendment']
        with self.assertRaisesRegex(ValueError,'stale or foreign revision'):
            resolve_question(plan,helper.brief,corrected,'Q1')

        corrected_plan,corrected_envelope=helper.analysis(corrected,FIXTURE['corrected_finding'])
        brief=helper.project(corrected,corrected_plan,corrected_envelope,'Brief after correction')
        report=helper.project(corrected,corrected_plan,corrected_envelope,'Report after correction')
        resolved=report['analysis_context']['resolved_findings'][0]
        self.assertEqual(resolved,brief['analysis_context']['resolved_findings'][0])

        content=json.loads((ROOT/'fixtures/business-brief-content.json').read_text(encoding='utf-8'))
        content['subject']={'id':corrected['id'],'name':corrected['title'],'scope':helper.brief['scope']}
        content['question']=helper.brief['question'];content['audience']=helper.brief['audience']
        content['cutoff']=helper.brief['as_of']
        claim=content['claims'][0]
        claim.update(id='A1',statement=resolved['statement'],status=resolved['status'],
                     unknowns=report['analysis_context']['unknowns']['A1'])
        claim['source']={'id':corrected['id'],'kind':'supplied_context',
                         'locator':', '.join(resolved['claim_refs']),'published_at':content['cutoff']}
        witness=copy.deepcopy(claim);witness.update(id='C-independent',statement=FIXTURE['independent'],
                                                   status='supplied_claim',unknowns=[])
        witness['source']={'id':'SRC-independent','kind':'supplied_context',
                           'locator':'C-independent','published_at':content['cutoff']}
        content['claims'].append(witness)
        handoff=freeze_business_brief_handoff(content)
        self.assertTrue(handoff['handoff_ready'],handoff['errors'])
        spec=handoff['handoff']['content_spec']

        markdown='\n'.join(['# Brief after correction','',spec['claims'][0]['statement'],
                           f"References: {spec['claims'][0]['source']['locator']}",
                           f"Unknown: {spec['claims'][0]['unknowns'][0]}",'',
                           '## Independent control',spec['claims'][1]['statement']])+'\n'
        self.assertIn(FIXTURE['corrected_finding'],markdown)
        self.assertIn('C-amendment',markdown)
        self.assertIn(FIXTURE['unknown'],markdown)
        self.assertIn(FIXTURE['independent'],markdown)
        self.assertNotIn(FIXTURE['finding'],markdown)

        for index,section in enumerate(report['study']['sections']):
            text=(f"{resolved['statement']}\nUnknown: {FIXTURE['unknown']}"
                  if index==0 else FIXTURE['independent'])
            section['paragraphs']=[{'id':f'P{index+1}','text':text,
                                    'claim_ids':section['claim_ids'],'pillar_ids':[],'review':{}}]
        report['study']['side_stories']=[{
            'id':'SS1','kind':'illustration','state':'candidate','title':'Orme on 2 October',
            'text':resolved['statement'],'claim_ids':resolved['claim_refs'],'pillar_ids':[],
            'parent_section_id':'B1','return_to':'P1',
            'reason_outside':'A concrete threshold example.',
            'payoff':'Keep the corrected contractual threshold visible.',
        }]
        html=render_study(report['study'])
        self.assertIn(FIXTURE['corrected_finding'],html)
        self.assertIn(FIXTURE['unknown'],html)
        self.assertIn(escape(FIXTURE['independent']),html)
        self.assertNotIn(FIXTURE['finding'],html)
        self.assertIn(f'id="{anchor("SS1")}"',html)
        self.assertIn(f'href="#{anchor("P1")}">Retour au récit</a>',html)
        self.assertEqual(original_hash,study_hash(original['study']))


if __name__=='__main__':unittest.main()
