import asyncio,copy,importlib.util,json,os,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'renderers/pedagogical'))
import landscape as renderer
SOURCE=ROOT/'learning/enterprise-ai/perception.sheet.json'
MANIFEST=SOURCE.parent/'manifest.json'

def validate_manifest_content_inventory(manifest):
    modules=manifest['modules'];ids=[item['id'] for item in modules]
    if len(ids)!=len(set(ids)) or set(manifest['content_files'])!={f'{item}.md' for item in ids}:
        raise ValueError('module IDs and content files must match')
    for item in modules:
        if item.get('content_file')!=f"{item['id']}.md":
            raise ValueError('module content file must match its ID')
    active=[item for item in modules if item.get('content_status')=='active_canonical']
    if len(active)!=1 or active[0]['id']!='perception':
        raise ValueError('Perception must be the only active canonical module')
    canonical=active[0]
    if canonical.get('sheet_file')!=manifest['canonical_perception'] or not (SOURCE.parent/canonical['sheet_file']).is_file():
        raise ValueError('active canonical sheet is missing or inconsistent')
    if canonical.get('markdown_role')!='canonical_projection' or canonical.get('render_status')!='candidate_supported':
        raise ValueError('active canonical projection or render status is inconsistent')
    candidates=[item for item in modules if item['id']!='perception']
    if any(item.get('content_status')!='legacy_candidate' or item.get('sheet_file') is not None or item.get('render_status')!='not_certified' for item in candidates):
        raise ValueError('legacy candidates must not claim an active sheet or render')
    return {item['id']:item['content_status'] for item in modules}

class LandscapeTests(unittest.TestCase):
    def test_manifest_identifies_one_active_canonical_module(self):
        manifest=json.loads(MANIFEST.read_text())
        statuses=validate_manifest_content_inventory(manifest)
        self.assertEqual(statuses['perception'],'active_canonical')
        self.assertEqual(set(statuses.values()),{'active_canonical','legacy_candidate'})
        self.assertEqual(manifest['template_source_commit_role'],'historical_candidate_baseline')

    def test_manifest_rejects_ambiguous_or_missing_canonical_status(self):
        manifest=json.loads(MANIFEST.read_text())
        for kind in ('double_active','missing_sheet','divergent_id'):
            changed=copy.deepcopy(manifest)
            if kind=='double_active':changed['modules'][0]['content_status']='active_canonical'
            if kind=='missing_sheet':changed['modules'][1]['sheet_file']='missing.sheet.json'
            if kind=='divergent_id':changed['modules'][2]['content_file']='wrong-module.md'
            with self.assertRaises(ValueError):validate_manifest_content_inventory(changed)

    def test_content_separation_and_source_links(self):
        sheet=renderer.load_sheet(SOURCE);scaffold=renderer.scaffold(sheet)
        self.assertNotIn('<style',scaffold)
        self.assertEqual(scaffold.count('<section class="page '),6)
        self.assertIn('Cinq causes systémiques',scaffold)
        self.assertIn('932 millions',scaffold)
        self.assertIn('https://www.bmwgroup.com/',scaffold)
        self.assertEqual([x['id'] for x in sheet['pages'][5]['content']['use_cases']],['UC-021','UC-042','UC-041','UC-044'])

    def test_unknown_sources_and_invented_cases_fail(self):
        for kind in ('source','case','score','presentation'):
            sheet=json.loads(SOURCE.read_text())
            if kind=='source':sheet['pages'][0]['source_ids'].append('S999')
            if kind=='case':sheet['pages'][5]['content']['use_cases'][0]['id']='UC-999'
            if kind=='score':sheet['pages'][5]['content']['use_cases'][0]['scores'][0]=0
            if kind=='presentation':sheet['pages'][0]['content']['definition']='<div>hidden layout</div>'
            with self.assertRaises(ValueError):renderer.validate(sheet,SOURCE.parent)

    def test_do_not_collapse_autopilot_and_agent(self):
        sheet=renderer.load_sheet(SOURCE);levels=sheet['pages'][3]['content']['levels']
        self.assertEqual([(x['integration'],x['automation']) for x in levels],[('Faible','Faible'),('Forte','Faible'),('Faible','Forte'),('Forte','Forte')])
        levels[2]['name']='Agent'
        with self.assertRaises(ValueError):renderer.validate(sheet,SOURCE.parent)

    def test_catalog_preserves_70_distinct_situations_and_classical_options(self):
        c=json.loads((SOURCE.parent/'use-cases.catalog.json').read_text());items={x['id']:x for x in c['items']}
        self.assertEqual(set(items),{f'UC-{n:03d}' for n in range(1,71)})
        self.assertIsNone(items['UC-035']['primary_capability']);self.assertIsNone(items['UC-068']['primary_capability'])
        self.assertEqual(items['UC-042']['primary_capability'],'perception')
        self.assertIn('sans intervention humaine',items['UC-021']['situation_originale'])
        self.assertIn('règle fixe',items['UC-046']['explanation_originale'])

    def test_markdown_is_regenerated_from_canonical_sheet(self):
        sheet=renderer.load_sheet(SOURCE)
        self.assertEqual(renderer.as_markdown(sheet),(SOURCE.parent/'perception.md').read_text())
        self.assertEqual(renderer.as_markdown(sheet).count('## Page '),6)

    @unittest.skipUnless(os.environ.get('PEDAGOGICAL_BROWSER_TEST')=='1','real browser enabled by CI')
    def test_landscape_overflow_is_rejected(self):
        sheet=renderer.load_sheet(SOURCE)
        sheet['pages'][0]['content']['definition']='Débordement volontaire. '*3000
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);source=root/'perception.sheet.json';source.write_text(json.dumps(sheet,ensure_ascii=False))
            (root/sheet['catalog_ref']).write_text((SOURCE.parent/sheet['catalog_ref']).read_text())
            report=asyncio.run(renderer.render(source,root/'out'))
            self.assertFalse(report['pass'])
            with self.assertRaises(ValueError):renderer.verify(source,root/'out')

if __name__=='__main__':unittest.main()
