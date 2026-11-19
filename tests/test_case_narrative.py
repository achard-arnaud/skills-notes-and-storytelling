"""A #258 case uses its own A1, blocks stale proofs and keeps editorial approval separate."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_narrative_selector import ROOT, sample, selector
import case_runtime as engine


class CaseNarrativeTest(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        process = engine.process()
        self.intake = {'entity_id': 'fixture', 'objective': 'Review a pilot', 'constraints': ['Synthetic data'],
                       'cutoff': '2026-11-20', 'template_id': 'two-pager', 'render_requested': False,
                       'narrative_profile': 's3-narrative-v1'}
        release = engine.load(ROOT / 'workflow/engine-release.json')
        refs = {'workflow/engine-release.json', engine.PROCESS, engine.NARRATIVE_GUIDE,
                *release['files'], *engine.NARRATIVE_REFS, *process['stable_refs'],
                *(r for t in process['templates'].values() for r in t['refs'])}
        for ref in refs:
            path = self.root / ref
            path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / ref, path)
        engine.init('test-case', self.intake, self.root)
        self.case = engine.case_path('test-case', self.root)

    def begin(self, stage, case='test-case'):
        return engine.begin(case, stage, 'fixture', self.root)

    def complete(self, stage, case='test-case'):
        return engine.complete(case, stage, self.root)

    def submit(self, ctx, content):
        kind = ctx['output_schema'].split('/')[-1]
        case = engine.case_path(ctx['case_id'], self.root)
        engine.atomic(case / ctx['output_ref'], {'kind': kind, 'case_id': ctx['case_id'], **content})

    def through_a1(self, case='test-case', statement='Dataset has a coverage gap'):
        ctx = self.begin('A0', case)
        folder = Path(ctx['output_ref']).parent
        case_root = engine.case_path(case, self.root)
        sources = []
        for sid, page in [('S1', 'p.3'), ('S2', 'p.4')]:
            ref = folder / (sid + '.txt')
            (case_root / ref).write_text('Synthetic version: ' + statement)
            sources.append({'id': sid, 'url': 'https://example.org/' + sid, 'locator': page, 'coverage': 'read',
                            'capture_ref': ref.as_posix(), 'fetched_at': '2026-11-20T00:00:00Z'})
        self.submit(ctx, {'sources': sources, 'unknowns': ['Long-term ROI']})
        self.complete('A0', case)
        ctx = self.begin('A1', case)
        nodes = [{'id': 'C-RISK', 'type': 'claim', 'statement': 'A comparable pilot may measure a different return',
                  'status': 'hypothesis'}]
        edges = [{'from': 'C-RISK', 'to': 'C-ROI', 'type': 'contradicts'}]
        for i, (cid, text, status, evid) in enumerate([
            ('C-ROI', 'Vendor forecasts a 30% return', 'attributed_claim', 'attributed'),
            ('C-DATA', statement, 'fact', 'verified'),
        ], 1):
            nodes.extend([{'id': 'N' + str(i), 'type': 'source', 'source_id': sources[i-1]['id']},
                          {'id': 'F' + str(i), 'type': 'fragment', 'text': text,
                           'locator': sources[i-1]['locator'], 'evidence_status': evid},
                          {'id': cid, 'type': 'claim', 'statement': text, 'status': status}])
            edges.extend([{'from': 'F' + str(i), 'to': 'N' + str(i), 'type': 'extracted_from'},
                          {'from': 'F' + str(i), 'to': cid, 'type': 'supports'}])
        self.submit(ctx, {'nodes': nodes, 'edges': edges, 'unknowns': []})
        self.complete('A1', case)
        return case_root / folder / 'S2.txt'

    def prepare_a2(self, request, case='test-case'):
        ctx = self.begin('A2', case)
        ref = (Path(ctx['output_ref']).parent / 'narrative.json').as_posix()
        engine.atomic(engine.case_path(case, self.root) / ref, request)
        preview = engine.narrative(case, 'A2', request_ref=ref, root=self.root)
        return ctx, ref, preview

    def through_a4(self, request, case='test-case'):
        ctx, ref, preview = self.prepare_a2(request, case)
        packet = preview['packet']
        self.submit(ctx, {**preview['scaffold'], 'narrative_ref': ref, 'decision': 'Different verdict'})
        with self.assertRaisesRegex(ValueError, 'differs'):
            self.complete('A2', case)
        request_ref = ref
        self.submit(ctx, {**preview['scaffold'], 'narrative_ref': request_ref})
        self.complete('A2', case)
        ctx = self.begin('A3', case)
        section = engine.narrative(case, 'A3', section='value', root=self.root)
        self.assertEqual(section['claims'], packet['claims'])
        self.assertEqual(section['relations'][0]['outside_section'], ['C-RISK'])
        self.assertFalse(section['side_stories'][0]['render_eligible'])
        self.submit(ctx, {'sections': [{'id': 'value', 'claim_ids': section['section']['claim_ids'],
                                        'prose': 'Run the local pilot before investment.'}]})
        self.complete('A3', case)
        ctx = self.begin('A4', case)
        folder = Path(ctx['output_ref']).parent
        case_root = engine.case_path(case, self.root)
        ref = (folder / 'findings.json').as_posix()
        reviews = []
        for lens in ('evidence', 'counter-perspective', 'decision'):
            note = folder / (lens + '.txt')
            (case_root / note).write_text('Synthetic reviewer checks declared scope.')
            reviews.append({'lens': lens, 'reviewer': lens, 'verdict': 'pass', 'evidence_ref': note.as_posix()})
        self.submit(ctx, {'reviews': reviews, 'narrative_review_ref': ref})
        engine.atomic(case_root / ref, [{'kind': 'missing_source', 'ref': 'C-ROI',
                                        'observation': 'Reported only', 'action': 'Find local data',
                                        'exit_test': 'Record result and locator'}])
        receipt = engine.narrative(case, 'A4', findings_ref=ref, root=self.root)
        self.assertEqual(receipt['findings'][0]['owner'], 'A0')
        with self.assertRaisesRegex(ValueError, 'unresolved findings'):
            self.complete('A4', case)
        engine.atomic(case_root / ref, [])
        self.assertFalse(self.complete('A4', case)['business_approval'])
        pinned = engine.inspect(case, self.root)['stages']['A2']['output_pins']
        self.assertEqual(pinned[request_ref], engine.digest(case_root / request_ref))
        return packet

    def test_opt_in_reuses_direct_evidence_and_reopens_only_bound_case(self):
        src = self.through_a1()
        req = sample()
        original = self.through_a4(req)
        direct_tool = self.root / engine.NARRATIVE_REFS[0]
        direct_path = self.root / 'direct.json'
        graph = engine.current_artifact(engine.load(self.case / 'state.json'), self.case, 'A1')
        evidence = engine.current_artifact(engine.load(self.case / 'state.json'), self.case, 'A0')
        claims, _, relations = selector.graph_ledger(graph, evidence, selector.claim_ids(req))
        claims['C-RISK'] = {'statement': 'A comparable pilot may measure a different return',
                            'status': 'hypothesis', 'evidence': []}
        engine.atomic(direct_path, {'request': req, 'claims': claims, 'relations': relations})
        direct = json.loads(subprocess.check_output([sys.executable, direct_tool, 'select', '--input', direct_path]))
        self.assertEqual(original, direct)
        self.assertFalse((self.root / 'data/cases/direct').exists())

        technical = {**req, 'domain': 'technical', 'decision_kind': 'compare'}
        engine.init('separate', self.intake, self.root)
        self.through_a1('separate')
        case_technical = self.through_a4(technical, 'separate')
        engine.atomic(direct_path, {'request': technical, 'claims': claims, 'relations': relations})
        direct_technical = json.loads(subprocess.check_output(
            [sys.executable, direct_tool, 'select', '--input', direct_path]))
        self.assertEqual(case_technical, direct_technical)
        self.assertEqual(case_technical['schema_id'], 'option-comparison')
        independent = engine.inspect('separate', self.root)

        old_bytes = src.read_bytes()
        src.write_text('Changed evidence')
        with self.assertRaisesRegex(ValueError, 'Stale context'):
            engine.inspect('test-case', self.root)
        src.write_bytes(old_bytes)
        self.assertEqual(engine.invalidate('test-case', 'A0', 'New capture from source', self.root)['invalidated'],
                         ['A0', 'A1', 'A2', 'A3', 'A4'])
        self.through_a1(statement='Dataset now covers two sites')
        _, _, preview = self.prepare_a2(req)
        self.assertNotEqual(preview['packet']['packet_sha256'], original['packet_sha256'])
        self.assertEqual(preview['packet']['claims']['C-DATA']['statement'], 'Dataset now covers two sites')
        self.assertEqual(engine.inspect('separate', self.root), independent)

    def test_unknown_profile_and_foreign_attempt_ref(self):
        with self.assertRaisesRegex(ValueError, 'Unknown narrative profile'):
            engine.init('bad-case', {**self.intake, 'narrative_profile': 'typo'}, self.root)
        self.assertFalse(engine.case_path('bad-case', self.root).exists())
        self.through_a1()
        self.begin('A2')
        engine.atomic(self.case / 'outside.json', sample())
        with self.assertRaisesRegex(ValueError, 'active A2 attempt'):
            engine.narrative('test-case', 'A2', request_ref='outside.json', root=self.root)


if __name__ == '__main__':
    unittest.main()
