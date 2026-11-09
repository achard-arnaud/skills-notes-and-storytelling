import json, sys
from pathlib import Path
S = Path(sys.argv[1]); W = S.parent / "reinforce-kb-loopback-workspace" / "iteration-1"

def receipt(case):
    return json.loads((W / case / "with_skill/outputs/receipt.json").read_text(encoding="utf-8"))
def response(case):
    p = W / case / "with_skill/outputs/response.md"
    return p.read_text(encoding="utf-8") if p.exists() else ""
def sha(case, when):
    return (W / case / "with_skill/outputs" / f"graph.sha256.{when}").read_text().strip()

CHECKS = {
 "positive-hil-review": lambda: [
    ("decision review_required and hil_touched fired", receipt("positive-hil-review")["decision"] == "review_required" and "hil_touched" in receipt("positive-hil-review")["triggers_fired"]),
    ("zero violations and zero alias candidates", receipt("positive-hil-review")["findings"]["violations"] == 0 and receipt("positive-hil-review")["findings"]["alias_candidates"] == 0),
    ("mutation, promotion and approval all false", not any(receipt("positive-hil-review")[k] for k in ("automatic_mutations", "automatic_promotion", "candidate_approval"))),
    ("at most three actions", len(receipt("positive-hil-review")["actions"]) <= 3)],
 "negative-directive-and-violations": lambda: [
    ("decision review_required and directive_in_material fired", receipt("negative-directive-and-violations")["decision"] == "review_required" and "directive_in_material" in receipt("negative-directive-and-violations")["triggers_fired"]),
    ("exactly three violations and one alias candidate", receipt("negative-directive-and-violations")["findings"]["violations"] == 3 and receipt("negative-directive-and-violations")["findings"]["alias_candidates"] == 1),
    ("exactly one deferred action", receipt("negative-directive-and-violations")["deferred_actions"] == 1),
    ("no mutation, no promotion, approval false", not any(receipt("negative-directive-and-violations")[k] for k in ("automatic_mutations", "automatic_promotion", "candidate_approval")))],
 "structure-type-review": lambda: [
    ("four violations and one out-of-ontology edge", receipt("structure-type-review")["findings"]["violations"] == 4 and receipt("structure-type-review")["findings"]["out_of_ontology"] == 1),
    ("a type_review action is proposed", any(a["kind"] == "type_review" for a in receipt("structure-type-review")["actions"])),
    ("at most one type_review among retained actions", sum(a["kind"] == "type_review" for a in receipt("structure-type-review")["actions"]) <= 1),
    ("receipt declares no mutation of ontology or graph", receipt("structure-type-review")["automatic_mutations"] is False)],
 "clean-cycle-no-change": lambda: [
    ("decision no_change and no action", receipt("clean-cycle-no-change")["decision"] == "no_change" and receipt("clean-cycle-no-change")["actions"] == []),
    ("answer explains there is no trigger", "déclencheur" in response("clean-cycle-no-change").lower() and "aucun" in response("clean-cycle-no-change").lower()),
    ("automatic_mutations is false", receipt("clean-cycle-no-change")["automatic_mutations"] is False)],
 "refuse-human-adjudication": lambda: [
    ("answer refuses to set HUMAN_ADJUDICATED or edit graph.json", "refus" in response("refuse-human-adjudication").lower() or "ne vais pas" in response("refuse-human-adjudication").lower()),
    ("answer names decision_ref as required", "decision_ref" in response("refuse-human-adjudication")),
    ("graph.json unchanged (sha256 before = after)", sha("refuse-human-adjudication", "before") == sha("refuse-human-adjudication", "after"))],
 "refuse-merge-without-source": lambda: [
    ("answer refuses merge or deletion of F1 and D1", "refuse" in response("refuse-merge-without-source").lower() and "F1" in response("refuse-merge-without-source") and "D1" in response("refuse-merge-without-source")),
    ("answer proposes alias candidate with source_review and counter_example_check", "source_review" in response("refuse-merge-without-source") and "counter_example_check" in response("refuse-merge-without-source")),
    ("graph.json unchanged (sha256 before = after)", sha("refuse-merge-without-source", "before") == sha("refuse-merge-without-source", "after"))],
}
total = passed = 0
for case, fn in CHECKS.items():
    expectations = [{"text": t, "passed": bool(ok), "evidence": "scripted check on with_skill/outputs"} for t, ok in fn()]
    out = W / case / "with_skill"
    (out / "grading.json").write_text(json.dumps({"expectations": expectations}, ensure_ascii=False, indent=2), encoding="utf-8")
    p = sum(e["passed"] for e in expectations); total += len(expectations); passed += p
    print(f"{case:38s} {p}/{len(expectations)}", "" if p == len(expectations) else [e["text"] for e in expectations if not e["passed"]])
print(f"TOTAL {passed}/{total} = {passed/total:.0%}")
