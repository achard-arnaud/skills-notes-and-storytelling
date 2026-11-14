"""Independent arithmetic checks for period-end cash flows and a product cohort."""
import math
from collections import Counter


def _finite(values):
    if any(not math.isfinite(x) for x in values):
        raise ValueError("finite values required")


def tco(upfront, periodic, exit_cost, residual):
    """Nominal lifecycle cost, all values in the same currency and horizon."""
    values = [upfront, *periodic, exit_cost, residual]
    _finite(values)
    if min(values) < 0:
        raise ValueError("enter costs and residual value as positive magnitudes")
    return math.fsum(values[:-1]) - residual


def roi(gross_benefits, total_cost):
    _finite([gross_benefits, total_cost])
    if total_cost <= 0:
        raise ValueError("positive investment required")
    return (gross_benefits - total_cost) / total_cost


def npv(rate, cashflows):
    _finite([rate, *cashflows])
    if rate <= -1 or not cashflows:
        raise ValueError("rate must exceed -100% and include t0")
    return math.fsum(flow / (1 + rate)**i for i, flow in enumerate(cashflows))


def irr(cashflows):
    """Unique IRR for conventional investments, via monotonic NPV bisection."""
    if len(cashflows) < 2 or cashflows[0] >= 0 or min(cashflows[1:]) < 0 or max(cashflows[1:]) <= 0:
        raise ValueError("conventional flows required for a unique IRR")
    lo, hi = -0.5, 1.0
    while npv(lo, cashflows) < 0:
        lo = (lo - 1.0) / 2
        if lo == -1:
            raise ValueError("rate below numerical resolution")
    while npv(hi, cashflows) > 0:
        hi = 2 * hi + 1
    for _ in range(128):
        mid = (lo + hi) / 2
        if npv(mid, cashflows) > 0:
            lo = mid
        else:
            hi = mid
    return (hi + lo) / 2


def multiple(numerator, denominator):
    _finite([numerator, denominator])
    if denominator <= 0:
        raise ValueError("positive denominator required for meaningful multiple")
    return numerator / denominator


def payback(cashflows):
    """First liquidity recovery; assume uniform intra-period inflow."""
    _finite(cashflows)
    if not cashflows or cashflows[0] >= 0:
        raise ValueError("initial outflow required")
    balance = cashflows[0]
    for period, flow in enumerate(cashflows[1:], start=1):
        if balance + flow >= 0:
            return period - 1 + (-balance / flow)
        balance += flow
    return None


def break_even(fixed_cost, price, variable_cost):
    _finite([fixed_cost, price, variable_cost])
    if min(fixed_cost, price, variable_cost) < 0 or price <= variable_cost:
        raise ValueError("nonnegative costs and positive unit contribution required")
    return math.ceil(fixed_cost / (price-variable_cost))


def rice(reach, impact, confidence, effort):
    _finite([reach, impact, confidence, effort])
    if min(reach, impact) < 0 or not 0 <= confidence <= 1 or effort <= 0:
        raise ValueError("use confidence fraction and positive person-months")
    return reach * impact * confidence / effort


def adoption(eligible_ids, active_ids):
    eligible, active = set(eligible_ids), set(active_ids)
    if not eligible or not active <= eligible:
        raise ValueError("active users must belong to eligible users in same window")
    return len(active) / len(eligible)


def median_ttv(observations):
    """Kaplan-Meier median, one (age_days, event_observed) per cohort member."""
    if not observations:
        raise ValueError("at least one cohort member required")
    events, censored = Counter(), Counter()
    for age, reached in observations:
        _finite([age])
        if age < 0 or type(reached) is not bool:
            raise ValueError("age and explicit event indicator required")
        (events if reached else censored)[age] += 1
    risk = len(observations)
    survival = 1.0
    for age in sorted(events.keys() | censored.keys()):
        survival *= 1 - events[age] / risk
        if survival <= 0.5:
            return age
        risk -= events[age] + censored[age]
    return None
