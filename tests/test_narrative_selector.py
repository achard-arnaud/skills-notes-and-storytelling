"""CR #258: one evidence packet, two independent paths."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import narrative_selector as selector


def sample():
    return {
        'domain': 'business', 'decision_kind': 'diagnose',
        'conclusion': 'Condition the investment on a local pilot',
        'tension': 'Expected returns depend on data readiness',
        'objection': 'The business impact remains uncertain',
        'falsifier': 'A measured pilot clears the investment threshold',
        'sections': [{'id': 'value', 'action_title': 'Benchmark the local return',
                      'claim_ids': ['C-ROI', 'C-DATA']}],
        'classification': {
            'C-ROI': {'primary_pillar': 'P-ECONOMICS', 'secondary_pillars': ['P-TECH-DATA'],
                      'dimension': 'business'},
            'C-DATA': {'primary_pillar': 'P-TECH-DATA', 'scale': 'site'},
        },
        'required_pillars': ['P-ECONOMICS', 'P-TECH-DATA', 'P-RISK-CONTROL'],
        'coverage': {'loaded': ['S1:p.3', 'S2:p.4'], 'omitted': ['Group-level data'],
                     'stop_reason': 'Pilot scope reached'},
        'side_stories': [{'type': 'reality_check', 'section_id': 'value',
                          'anchor_claim_id': 'C-DATA', 'claim_ids': ['C-DATA'],
                          'objection': 'Can a site run a pilot?', 'limitation': 'One site is illustrative',
                          'return_hook': 'The local pilot measures readiness'}],
    }


def ledger():
    return {
        'C-ROI': {'statement': 'Vendor forecasts a 30% return', 'status': 'attributed_claim',
                  'evidence': [{'source_id': 'S1', 'locator': 'p.3', 'attribution': 'Vendor'}]},
        'C-DATA': {'statement': 'Dataset has a coverage gap', 'status': 'fact',
                   'evidence': [{'source_id': 'S2', 'locator': 'p.4'}]},
    }


class NarrativeSelectorTest(unittest.TestCase):
    def setUp(self):
        self.profile = selector.load_profile(ROOT)

    def test_selects_by_intent_and_withholds_on_ambiguity(self):
        for intent, scheme in self.profile['by_decision'].items():
            req = {**sample(), 'decision_kind': intent}
            with self.subTest(intent=intent):
                self.assertEqual(selector.build(req, ledger(), self.profile)['schema_id'], scheme)
        for intent in (None, 'unknown'):
            result = selector.build({**sample(), 'decision_kind': intent}, ledger(), self.profile)
            self.assertEqual(result['status'], 'needs_input')
            self.assertNotIn('conclusion', result)

    def test_all_domain_handoffs_route_to_their_actual_owner(self):
        for domain, decision in [('business', 'diagnose'), ('product', 'compare'),
                                 ('technical', 'deploy'), ('pedagogy', 'teach'), ('regulatory', 'verdict')]:
            with self.subTest(domain=domain):
                packet = selector.build({**sample(), 'domain': domain, 'decision_kind': decision},
                                        ledger(), self.profile)
                finding = {'kind': 'claim', 'observation': 'Scope unclear', 'ref': 'C-DATA',
                           'action': 'Check the denominator', 'exit_test': 'Population stated'}
                receipt = selector.review(packet, [finding], 'direct', self.profile)
                owner = receipt['findings'][0]['owner']
                self.assertTrue((ROOT / 'skills' / owner / 'SKILL.md').is_file())
                self.assertEqual(packet['schema_id'], self.profile['by_decision'][decision])

    def test_shared_packet_preserves_proof_and_separates_pillars(self):
        claims = ledger()
        packet = selector.build(sample(), claims, self.profile, ['C-ROI', 'C-DATA', 'C-OFF'])
        self.assertEqual(packet['sections'][0]['claim_ids'], ['C-ROI', 'C-DATA'])
        self.assertEqual(packet['claims']['C-ROI'], claims['C-ROI'])
        self.assertEqual(packet['classification']['C-ROI']['primary_pillar'], 'P-ECONOMICS')
        self.assertEqual(packet['pillar_coverage']['missing'], ['P-RISK-CONTROL'])
        self.assertEqual(packet['pillar_coverage']['unexamined'], ['C-OFF'])
        self.assertEqual(packet['side_stories'][0]['status'], 'candidate')
        self.assertEqual(packet['pillar_coverage']['unclassified'], [])
        self.assertFalse(packet['editorial_approved'])
        section = selector.section_packet(packet, 'value')
        self.assertEqual(section['claims']['C-DATA'], claims['C-DATA'])
        self.assertFalse(section['side_stories'][0]['render_eligible'])

    def test_classification_reasons_and_orthogonal_axes(self):
        req = sample()
        req['classification']['C-DATA'] = {'primary_pillar': None, 'unclassified_reason': 'Scope unclear',
                                           'scale': 'site', 'domain_layer': 'core'}
        result = selector.build(req, ledger(), self.profile)
        self.assertEqual(result['pillar_coverage']['unclassified'], ['C-DATA'])
        for bad in ({'primary_pillar': None}, {'primary_pillar': 'P-TECH-DATA', 'scale': 'business'},
                    {'primary_pillar': 'P-TECH-DATA', 'secondary_pillars': ['P-TECH-DATA']}):
            req['classification']['C-DATA'] = bad
            with self.assertRaises(ValueError):
                selector.build(req, ledger(), self.profile)

    def test_encart_cannot_introduce_foreign_or_other_section_proof(self):
        req = sample()
        req['sections'].append({'id': 'extra', 'action_title': 'Independent question', 'claim_ids': ['C-X']})
        claims = {**ledger(), 'C-X': {'statement': 'Context', 'status': 'unknown', 'evidence': []}}
        for ref in ('C-X', 'absent'):
            req['side_stories'][0]['claim_ids'] = ['C-DATA', ref]
            with self.assertRaisesRegex(ValueError, 'trunk'):
                selector.build(req, claims, self.profile)

    def test_review_routes_issues_without_approval(self):
        packet = selector.build(sample(), ledger(), self.profile)
        findings = [{'kind': 'missing_source', 'observation': 'Check actual return', 'ref': 'C-ROI',
                     'action': 'Locate audited numbers', 'exit_test': 'Record the scoped source'},
                    {'kind': 'prose', 'observation': 'Ambiguous transition', 'ref': 'value',
                     'action': 'Clarify the transition', 'exit_test': 'Reader identifies the next step'}]
        deep = selector.review(packet, findings, 'workflow', self.profile)
        self.assertEqual([x['owner'] for x in deep['findings']], ['A0', 'A3'])
        direct = selector.review(packet, findings, 'direct', self.profile)
        self.assertEqual([x['owner'] for x in direct['findings']], ['targeted_research', 'business-analysis'])
        self.assertFalse(deep['editorial_approved'])
        bad = copy.deepcopy(findings)
        bad[0]['ref'] = 'Other case'
        with self.assertRaises(ValueError):
            selector.review(packet, bad, 'workflow', self.profile)


if __name__ == '__main__':
    unittest.main()
