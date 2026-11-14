"""Synthetic cold-resume regression, not the real-company comparative trial."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT),str(ROOT/'tests')]
import context
from analysis_writing import prepare_analysis_writing
from test_adoption import sample,run_method
from writing import study_hash

ENGINE_PATHS=('analysis.py','planning.py','adoption.py','analysis_impact.py','analysis_writing.py',
              'writing.py','context.py','schemas/analysis-envelope.v1.schema.json',
              'schemas/analysis-planning.v1.schema.json','schemas/analysis-writing.v1.schema.json',
              'workflows/analysis-methods.v1.json','AGENTS.md','../AGENTS.md')

CHILD=r'''
import hashlib,json,sys
from pathlib import Path
root=Path(sys.argv[2]).resolve()
sys.path.insert(0,str(root))
import context
from analysis_writing import prepare_analysis_writing
from writing import study_hash
folder=Path(sys.argv[1])
snapshot=json.loads((folder/'checkpoint.json').read_text())
check=context.validate_checkpoint(folder,snapshot,base_sha='synthetic-base-v1')
if not check['ok']:
    print(json.dumps(check));raise SystemExit(2)
payload=json.loads((folder/'phase2.json').read_text())
if payload['runtime_version']!=list(sys.version_info[:3]):
    print('runtime version mismatch');raise SystemExit(3)
for path,expected in payload['engine_hashes'].items():
    if hashlib.sha256((root/path).read_bytes()).hexdigest()!=expected:
        print('engine version mismatch');raise SystemExit(3)
result=prepare_analysis_writing(payload['study'],payload['envelope'],payload['plan'],payload['brief'],
                               payload['next_stage_request']['synthesis'],payload['next_stage_request']['scaffold'],perspective='product')
print(json.dumps({'result_hash':study_hash(result),'study':result['study'],
                  'findings':result['analysis_context']['resolved_findings'],
                  'gaps':result['analysis_context']['gaps']}))
'''


def phase2(partial=False):
    study,brief,plan,measurements,_=sample()
    if partial:
        measurements['eligible']={'value':None,'claim_refs':[]}
    envelope=run_method(study,brief,plan,measurements)['envelope']
    refs=[] if partial else [{'analysis_ref':'A1','finding_index':0}]
    synthesis=dict(schema_version='1.0',study_ref=study['id'],envelope_revision=study_hash(envelope),
                   candidate_thesis={'text':'Open question' if partial else 'Declared weekly adoption is 30%', 'finding_refs':refs},
                   observations=refs,claim_disposition=[{'claim_ref':c['id'],'state':'included','reason':''} for c in study['claims']])
    scaffold={'sections':[dict(id='B1',title='What is documented?',analysis_refs=['A1'],
                              claim_ids=[c['id'] for c in study['claims']] if partial else [],pillar_ids=[])]}
    return dict(study=study,brief=brief,plan=plan,envelope=envelope,
                next_stage_request={'synthesis':synthesis,'scaffold':scaffold},
                runtime_version=list(sys.version_info[:3]),
                engine_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ENGINE_PATHS})


def save(folder,payload):
    (folder/'phase2.json').write_text(json.dumps(payload,ensure_ascii=False),encoding='utf-8')
    board={'id':'synthetic-convergence-board','base_sha':'synthetic-base-v1','tasks':[
        {'id':'phase2','title':'Analysis supplied','status':'done','depends_on':[]},
        {'id':'phase3','title':'Consume selected analysis','status':'ready','depends_on':['phase2'],'outputs':['prepared.json']}]}
    packet=context.build_packet(folder,board,'phase3',['phase2.json'],for_execution=True)
    checkpoint=context.checkpoint(folder,packet,next_task='phase3',note='Synthetic cold-resume test only')
    (folder/'checkpoint.json').write_text(json.dumps(checkpoint),encoding='utf-8')
    (folder/'RESUME.md').write_text(context.resume_markdown(checkpoint),encoding='utf-8')


def cold(folder):
    return subprocess.run([sys.executable,'-I','-c',CHILD,str(folder),str(ROOT)],text=True,capture_output=True,check=False)


class ConvergenceReplayTests(unittest.TestCase):
    def test_fresh_process_restores_nominal_and_partial_from_only_saved_artifacts(self):
        for partial in (False,True):
            with self.subTest(partial=partial),tempfile.TemporaryDirectory() as tmp:
                folder=Path(tmp);payload=phase2(partial);before=copy.deepcopy(payload)
                save(folder,payload)
                warm=prepare_analysis_writing(payload['study'],payload['envelope'],payload['plan'],payload['brief'],
                                              payload['next_stage_request']['synthesis'],payload['next_stage_request']['scaffold'],perspective='product')
                result=cold(folder)
                self.assertEqual(0,result.returncode,result.stderr+result.stdout)
                restored=json.loads(result.stdout)
                self.assertEqual(study_hash(warm),restored['result_hash'])
                self.assertEqual(payload['study']['claims'],restored['study']['claims'])
                self.assertEqual(before,payload)
                if partial:
                    self.assertEqual([],restored['findings'])
                    self.assertTrue(restored['gaps'])
                else:
                    self.assertIn('30.00%',restored['findings'][0]['statement'])

    def test_changed_or_missing_source_artifact_refuses_resume(self):
        for missing in (False,True):
            with tempfile.TemporaryDirectory() as tmp:
                folder=Path(tmp);save(folder,phase2())
                if missing:(folder/'phase2.json').unlink()
                else:
                    payload=json.loads((folder/'phase2.json').read_text())
                    payload['study']['claims'][0]['text']='Changed after checkpoint'
                    (folder/'phase2.json').write_text(json.dumps(payload))
                result=cold(folder)
                self.assertNotEqual(0,result.returncode)
                self.assertNotIn('result_hash',result.stdout)

    def test_changed_engine_pin_refuses_even_when_artifact_checkpoint_is_valid(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);payload=phase2();payload['engine_hashes']['planning.py']='0'*64
            save(folder,payload)
            result=cold(folder)
            self.assertEqual(3,result.returncode,result.stderr)
            self.assertIn('engine version mismatch',result.stdout)


if __name__=='__main__':unittest.main()
