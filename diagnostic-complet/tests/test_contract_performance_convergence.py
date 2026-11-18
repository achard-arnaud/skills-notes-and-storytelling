import copy
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from analysis_writing import apply_analysis_writing_revision, prepare_analysis_writing
from business_brief_content import freeze_business_brief_handoff
from planning import CATALOG, resolve_question
from render import anchor, render_study
from writing import EVIDENCE_KEYS, study_hash, text_hash


FIXTURE = json.loads((ROOT / 'fixtures' /
                      'convergence-contract-performance.json').read_text(encoding='utf-8'))
METHOD = 'business.contracts-and-performance'


class ContractPerformanceConvergenceTests(unittest.TestCase):
    def setUp(self):
        self.study = {
            'id': FIXTURE['id'], 'title': 'Synthetic contract performance',
            'sources': [], 'fragments': [], 'claims': [], 'relations': [],
            'pillars': [], 'sections': [], 'side_stories': [],
        }
        for field in ('contract', 'amendment', 'measurement', 'independent'):
            source, fragment, claim = (f'{kind}-{field}' for kind in ('SRC', 'F', 'C'))
            self.study['sources'].append({
                'id': source, 'kind': 'synthetic_fixture', 'access': 'synthetic',
                'title': field, 'locator': f'fixture:{field}',
            })
            self.study['fragments'].append({
                'id': fragment, 'source_id': source, 'locator': field, 'text': FIXTURE[field],
            })
            self.study['claims'].append({
                'id': claim, 'text': FIXTURE[field], 'status': 'supplied_claim',
                'fragment_ids': [fragment], 'pillar_ids': [],
            })
        self.brief = {
            'schema_version': '1.0', 'id': 'BRIEF', 'study_ref': self.study['id'],
            'question': 'Which displayed alerts are contractual?', 'scope': 'Orme and Pin',
            'audience': 'Operations', 'intent': 'contract-performance',
            'decision_requested': False, 'as_of': '2026-10-12',
        }

    def analysis(self, study, statement):
        inputs = ['C-contract', 'C-amendment', 'C-measurement']
        version = CATALOG['methods'][METHOD]['method_version']
        question = {
            'id': 'Q1', 'question': self.brief['question'], 'method': METHOD,
            'method_version': version, 'input_claim_refs': inputs,
            'evidence_map': [
                {'requirement': 'contract_rule', 'claim_refs': [inputs[0]]},
                {'requirement': 'effective_scope', 'claim_refs': [inputs[1]]},
                {'requirement': 'measurement', 'claim_refs': [inputs[2]]},
            ],
            'unknowns': [], 'queries': [], 'stop_condition': 'Use only the synthetic fixture.',
        }
        revision = study_hash({key: study[key] for key in EVIDENCE_KEYS if key in study})
        plan = {
            'schema_version': '1.0', 'id': 'PLAN', 'study_ref': study['id'],
            'intent_ref': self.brief['id'], 'intent_revision': study_hash(self.brief),
            'input_revision': revision, 'catalog_revision': study_hash(CATALOG),
            'questions': [question], 'budget': {'max_publications': 4, 'max_queries': 1},
        }
        envelope = {
            'schema_version': '1.0', 'study_ref': study['id'], 'input_revision': revision,
            'analyses': [{
                'id': 'A1', 'question_ref': 'Q1', 'question': question['question'],
                'method': METHOD, 'method_version': version, 'scope': self.brief['scope'],
                'as_of': self.brief['as_of'], 'input_claim_refs': inputs,
                'findings': [{'statement': statement, 'status': 'inference', 'claim_refs': inputs}],
                'counterevidence': [], 'unknowns': [FIXTURE['unknown']],
                'state': 'complete', 'needs_research': False,
            }],
        }
        return plan, envelope

    def project(self, study, plan, envelope, title):
        ref = {'analysis_ref': 'A1', 'finding_index': 0}
        statement = envelope['analyses'][0]['findings'][0]['statement']
        synthesis = {
            'schema_version': '1.0', 'study_ref': study['id'],
            'envelope_revision': study_hash(envelope), 'observations': [ref],
            'candidate_thesis': {'text': statement, 'finding_refs': [ref]},
            'claim_disposition': [{'claim_ref': claim['id'], 'state': 'included', 'reason': ''}
                                  for claim in study['claims']],
        }
        scaffold = {'sections': [
            {'id': 'B1', 'title': title, 'analysis_refs': ['A1'], 'claim_ids': [], 'pillar_ids': []},
            {'id': 'B2', 'title': 'Independent control', 'analysis_refs': [],
             'claim_ids': ['C-independent'], 'pillar_ids': []},
        ]}
        return prepare_analysis_writing(study, envelope, plan, self.brief, synthesis,
                                        scaffold, perspective='business')

    def test_one_business_method_feeds_two_views_and_reopens_a_changed_source(self):
        plan, envelope = self.analysis(self.study, FIXTURE['finding'])
        packet = resolve_question(plan, self.brief, self.study, 'Q1')
        self.assertEqual(METHOD, packet['method']['id'])
        self.assertFalse(packet['analysis_executed'])

        short = self.project(self.study, plan, envelope, 'Brief: alerts to review')
        long = self.project(self.study, plan, envelope, 'Report: how the amendment changes operations')
        self.assertEqual(short['analysis_context'], long['analysis_context'])
        self.assertNotEqual(short['study']['sections'][0]['title'], long['study']['sections'][0]['title'])
        self.assertEqual({'A1': [FIXTURE['unknown']]}, short['analysis_context']['unknowns'])
        self.assertEqual(['C-amendment', 'C-contract', 'C-measurement'],
                         long['study']['sections'][0]['claim_ids'])

        corrected = copy.deepcopy(self.study)
        corrected['fragments'][1]['text'] = FIXTURE['corrected_amendment']
        corrected['claims'][1]['text'] = FIXTURE['corrected_amendment']
        with self.assertRaisesRegex(ValueError, 'stale or foreign revision'):
            resolve_question(plan, self.brief, corrected, 'Q1')

        corrected_plan, corrected_envelope = self.analysis(corrected, FIXTURE['corrected_finding'])
        for view in (short, long):
            baseline = view['study']
            for index, section in enumerate(baseline['sections']):
                text = FIXTURE['finding'] if index == 0 else FIXTURE['independent']
                section['paragraphs'] = [{
                    'id': f'P{index + 1}', 'text': text, 'claim_ids': section['claim_ids'],
                    'pillar_ids': [], 'review': {
                        'evidence': True, 'editorial': True, 'text_sha256': text_hash(text),
                    },
                }]
            applied = apply_analysis_writing_revision(
                baseline, envelope, view['analysis_context'], ['SRC-amendment'],
                {'P1': FIXTURE['corrected_finding']},
                expected_study_hash=study_hash(baseline),
                expected_envelope_hash=study_hash(envelope),
            )
            self.assertEqual(['P1'], applied['analysis_review']['paragraph_ids'])
            self.assertFalse(applied['study']['sections'][0]['paragraphs'][0]['review']['evidence'])
            self.assertEqual(baseline['sections'][1], applied['study']['sections'][1])
            self.assertEqual(FIXTURE['finding'], baseline['sections'][0]['paragraphs'][0]['text'])

        final_short = self.project(corrected, corrected_plan, corrected_envelope, 'Brief after correction')
        final_long = self.project(corrected, corrected_plan, corrected_envelope, 'Report after correction')
        resolved = final_long['analysis_context']['resolved_findings'][0]
        self.assertEqual(resolved, final_short['analysis_context']['resolved_findings'][0])

        content = json.loads((ROOT / 'fixtures' / 'business-brief-content.json').read_text())
        context = final_short['analysis_context']
        content['subject'] = {'id': corrected['id'], 'name': corrected['title'], 'scope': self.brief['scope']}
        content['question'] = self.brief['question']
        content['audience'] = self.brief['audience']
        content['cutoff'] = self.brief['as_of']
        claim = content['claims'][0]
        claim.update(id=resolved['reference']['analysis_ref'], status=resolved['status'],
                     statement=resolved['statement'], unknowns=context['unknowns']['A1'])
        claim['source'] = {'id': corrected['id'], 'kind': 'supplied_context',
                           'locator': ', '.join(resolved['claim_refs']), 'published_at': content['cutoff']}
        handoff = freeze_business_brief_handoff(content)
        self.assertTrue(handoff['handoff_ready'], handoff['errors'])
        self.assertEqual(FIXTURE['corrected_finding'],
                         handoff['handoff']['content_spec']['claims'][0]['statement'])
        self.assertFalse(handoff['human_approval'])

        section = final_long['study']['sections'][0]
        section['paragraphs'] = [{'id': 'P1', 'text': resolved['statement'],
                                  'claim_ids': resolved['claim_refs'], 'pillar_ids': [], 'review': {}}]
        final_long['study']['side_stories'] = [{
            'id': 'SS1', 'kind': 'illustration', 'state': 'candidate', 'title': 'Orme on 2 October',
            'text': resolved['statement'], 'claim_ids': resolved['claim_refs'], 'pillar_ids': [],
            'parent_section_id': section['id'], 'return_to': 'P1',
            'reason_outside': 'A concrete contractual threshold example.',
            'payoff': 'Distinguish the dashboard signal from its contractual qualification.',
        }]
        rendered = render_study(final_long['study'])
        self.assertIn(f'id="{anchor("SS1")}"', rendered)
        self.assertIn(f'href="#{anchor("P1")}">Retour au récit</a>', rendered)
        self.assertIn(FIXTURE['corrected_finding'], rendered)
        amendment_anchor = anchor('C-amendment')
        self.assertIn(f'href="#{amendment_anchor}">C-amendment</a>', rendered)
        self.assertIn(f'id="{amendment_anchor}"', rendered)
        self.assertEqual({'A1': [FIXTURE['unknown']]}, final_long['analysis_context']['unknowns'])
