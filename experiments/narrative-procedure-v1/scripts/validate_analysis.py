"""Validate structure, source bindings and affected blocks; no truth certification."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator,FormatChecker
SCHEMA=Path(__file__).resolve().parents[1]/"contracts"/"analysis-result.schema.json"
def validate(payload, known_claims, known_blocks):
 errors=[e.message for e in Draft202012Validator(json.loads(SCHEMA.read_text()),format_checker=FormatChecker()).iter_errors(payload)]
 inputs=set(payload.get("input_claim_refs",[]))
 for ref in inputs-set(known_claims):errors.append("Unresolved claim: "+ref)
 for item in payload.get("findings",[]):
  for ref in set(item.get("claim_refs",[]))-inputs:errors.append("Finding outside inputs: "+ref)
 for ref in set(payload.get("affects_blocks",[]))-set(known_blocks):errors.append("Unresolved block: "+ref)
 return errors
def impacted_blocks(analyses,changed_ids):
 return sorted({b for a in analyses if a["id"] in changed_ids for b in a["affects_blocks"]})
if __name__=="__main__":
 import argparse
 p=argparse.ArgumentParser();p.add_argument("payload");p.add_argument("--claims",nargs="+",required=True);p.add_argument("--blocks",nargs="+",required=True);a=p.parse_args()
 errors=validate(json.loads(Path(a.payload).read_text()),a.claims,a.blocks)
 print(json.dumps({"valid":not errors,"errors":errors,"scope":"schema and bindings only"},ensure_ascii=False))
 raise SystemExit(bool(errors))
