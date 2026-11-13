import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_analysis import validate,impacted_blocks
class AnalysisTests(unittest.TestCase):
 def setUp(self):self.p=json.loads((ROOT/"fixtures/analysis-result.synthetic.json").read_text())
 def check(self):return validate(self.p,["SYN-S1","SYN-O1"],["B-OPTIONS","B-CONTEXT"])
 def test_valid_recommendation(self):self.assertEqual(self.check(),[])
 def test_unresolved_input(self):
  self.p["input_claim_refs"].append("MISSING");self.assertTrue(self.check())
 def test_finding_not_in_inputs(self):
  self.p["findings"][0]["claim_refs"]=["OUTSIDE"];self.assertTrue(self.check())
 def test_no_promotion_to_fact(self):
  self.p["findings"][0]["status"]="verified_fact";self.assertTrue(self.check())
 def test_unknown_block(self):
  self.p["affects_blocks"]=["ABSENT"];self.assertTrue(self.check())
 def test_invalid_date(self):
  self.p["as_of"]="2026-99-99";self.assertTrue(self.check())
 def test_reopen_only_affected(self):
  b=copy.deepcopy(self.p);b["id"]="AN-OTHER";b["affects_blocks"]=["B-CONTEXT"]
  self.assertEqual(impacted_blocks([self.p,b],{"AN-SYN-1"}),["B-OPTIONS"])
 def test_method_required(self):
  del self.p["method"];self.assertTrue(self.check())
 def test_non_object_is_reported(self):
  self.assertTrue(validate([],[],[]))
 def test_malformed_reference_is_reported(self):
  self.p["input_claim_refs"]=[{}];self.assertTrue(self.check())
 def test_empty_reference_is_reported(self):
  self.p["input_claim_refs"]=[""];self.assertTrue(self.check())
if __name__=="__main__":unittest.main()

