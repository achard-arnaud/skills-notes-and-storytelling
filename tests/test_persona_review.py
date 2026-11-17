import json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class PersonaReviewTest(unittest.TestCase):
 def test_consumer_links(self):
  case=json.loads((ROOT/'tests/fixtures/persona-review-v1.json').read_text())
  for item in case['consumers']:
   p=ROOT/item['path'];links=re.findall(r'\]\(([^)]*persona-review\.md)\)',p.read_text())
   self.assertEqual(len(links),1,item['path'])
   self.assertEqual((p.parent/links[0]).resolve(),(ROOT/case['contract']).resolve())
 def test_all_requested_lenses_are_distinct_and_covered(self):
  case=json.loads((ROOT/'tests/fixtures/persona-review-v1.json').read_text());names={x['persona'] for x in case['synthetic_cases']}
  self.assertEqual(len(names),10)
  self.assertEqual(names,{n for x in case['consumers'] for n in x['lenses']})
  text=(ROOT/case['contract']).read_text()
  for x in case['synthetic_cases']:
   self.assertIn(x['input'],text);self.assertIn(x['expected_correction'],text)
 def test_sharp_cto_sources_and_attribution(self):
  text=(ROOT/'references/personas/sharp-cto.md').read_text()
  self.assertEqual(len(set(re.findall(r'https://jeremyjouvance.com/en/blog/[^)]+',text))),4)
  self.assertIn('synthétique',text);self.assertIn('aucune', (ROOT/'references/persona-review.md').read_text())
if __name__=='__main__':unittest.main()
