import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
spec=importlib.util.spec_from_file_location('relation_contract_validator',ROOT/'scripts/validate_contracts.py')
validator=importlib.util.module_from_spec(spec);spec.loader.exec_module(validator)

class RelationCatalogTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
  for rel in ['contracts/relation-types.json','contracts/claims-graph-light.schema.json','references/workflow.md','tests/fixtures/relation-catalog-v1.json']:
   target=self.root/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/rel,target)
 def run_check(self):
  with patch.object(validator,'ROOT',self.root):validator.check_relation_catalog()
 def test_actual_catalog_covers_four_previously_missing_types(self):
  self.run_check();c=json.loads((self.root/'contracts/relation-types.json').read_text())
  self.assertTrue({'integrates_with','substitutes','complements','enables'}<={x['id'] for x in c['relations']})
 def test_schema_omission_refused(self):
  p=self.root/'contracts/claims-graph-light.schema.json';x=json.loads(p.read_text());x['properties']['edges']['items']['properties']['type']['enum'].pop();p.write_text(json.dumps(x))
  with self.assertRaisesRegex(SystemExit,'mismatch'):self.run_check()
 def test_unknown_fixture_type_refused(self):
  p=self.root/'tests/fixtures/relation-catalog-v1.json';x=json.loads(p.read_text());x['invalid_types'].append('causes');p.write_text(json.dumps(x))
  with self.assertRaisesRegex(SystemExit,'fixture mismatch'):self.run_check()
 def test_duplicate_catalog_refused(self):
  p=self.root/'contracts/relation-types.json';x=json.loads(p.read_text());x['relations'].append(x['relations'][0]);p.write_text(json.dumps(x))
  with self.assertRaisesRegex(SystemExit,'duplicate'):self.run_check()
