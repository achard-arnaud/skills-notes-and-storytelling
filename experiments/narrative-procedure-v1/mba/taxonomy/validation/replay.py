"""Compare independently calculated answers with explicit hand-computed oracles."""
import json
import math
from pathlib import Path
import recalculate as r


def check(name, function, args, expected):
    try:
        actual = function(*args)
    except ValueError:
        actual = "invalid"
    passed = math.isclose(actual, expected, rel_tol=1e-8, abs_tol=1e-8) if isinstance(expected,(int,float)) and isinstance(actual,(int,float)) else actual == expected
    return dict(case=name, inputs=args, expected=expected, actual=actual, status="PASS" if passed else "FAIL")


CASES = [
    ("tco_nominal_eur_2y",r.tco,[100,[30,40],10,20],160),
    ("tco_sign",r.tco,[100,[-30],10,20],"invalid"),
    ("roi_gross_200_cost_160",r.roi,[200,160],.25),
    ("roi_zero_cost",r.roi,[100,0],"invalid"),
    ("van_10pct_t0_and_2_year_ends",r.npv,[.1,[-100,55,60.5]],0),
    ("van_invalid_discount",r.npv,[-1,[-100,110]],"invalid"),
    ("tri_conventional",r.irr,[[-100,55,60.5]],.1),
    ("tri_negative_return",r.irr,[[-100,80]],-.2),
    ("tri_ambiguous_two_roots",r.irr,[[-100,230,-132]],"invalid"),
    ("multiple_moic_value_over_invested",r.multiple,[360,120],3),
    ("multiple_ev_ebitda_same_scope_period",r.multiple,[900,150],6),
    ("multiple_negative_ebitda",r.multiple,[900,-150],"invalid"),
    ("payback_undiscounted_years",r.payback,[[-100,40,80]],1.75),
    ("payback_not_recovered",r.payback,[[-100,20,40]],None),
    ("break_even_indivisible_cases",r.break_even,[121,13,5],16),
    ("break_even_negative_contribution",r.break_even,[121,4,5],"invalid"),
    ("rice_quarter_users_person_months",r.rice,[250,2,.8,4],100),
    ("rice_percent_misentered",r.rice,[250,2,80,4],"invalid"),
    ("ttv_with_right_censoring",r.median_ttv,[[(2,True),(3,False),(5,True),(7,False)]],5),
    ("ttv_censor_and_event_same_day",r.median_ttv,[[(2,True),(2,False),(5,True),(7,False)]],5),
    ("ttv_median_not_reached",r.median_ttv,[[(2,True),(4,False),(7,False)]],None),
    ("ttv_all_censored",r.median_ttv,[[(2,False),(4,False)]],None),
    ("adoption_distinct_users_same_window",r.adoption,[['a','b','c','d'],['a','a','b']],.5),
    ("adoption_mixed_cohort",r.adoption,[['a','b'],['a','x']],"invalid"),
    ("adoption_no_eligible_users",r.adoption,[[],[]],"invalid"),
]
if __name__ == '__main__':
    results = [check(*case) for case in CASES]
    receipt = {"source":"synthetic analytical fixtures", "checks":results,"passed":sum(x["status"]=="PASS" for x in results),"total":len(results)}
    Path(__file__).with_name("receipt.json").write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
    print(receipt["passed"],"/",receipt["total"])
    raise SystemExit(receipt["passed"]!=receipt["total"])
