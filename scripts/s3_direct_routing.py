#!/usr/bin/env python3
"""Check S3 plans and direct receipts offline; never classify prose or dispatch work."""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "contracts/s3-direct-routing.v1.json"
CAPABILITIES = {"manual", "native", "unavailable"}
INACTIVE = {"planned", "unavailable", "not_executed"}


def digest(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")).hexdigest()


def shape(value, required, optional=(), *, label):
    if not isinstance(value, dict) or not set(required) <= value.keys():
        raise ValueError(f"{label}: object or required fields missing")
    if value.keys() - (set(required) | set(optional)):
        raise ValueError(f"{label}: unexpected fields")


def nonblank(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: expected nonblank text")
    return value


def unique_texts(values, label):
    if not isinstance(values, list):
        raise ValueError(f"{label}: expected list")
    result = {nonblank(item, label) for item in values}
    if len(result) != len(values):
        raise ValueError(f"{label}: duplicate value")
    return result


def git(repo, *args):
    result = subprocess.run(["git", "--no-replace-objects", "-C", str(repo), *args],
                            capture_output=True, check=False)
    if result.returncode:
        raise ValueError("commit or pinned file is unavailable")
    return result.stdout


def pinned_file(repo, revision, path):
    p = PurePosixPath(nonblank(path, "method path"))
    if p.is_absolute() or ".." in p.parts or p.as_posix() != path or ":" in path or "\\" in path:
        raise ValueError("method path must be a canonical repository path")
    entry = git(repo, "--literal-pathspecs", "ls-tree", "-z", revision, "--", path)
    if not entry.startswith((b"100644 blob ", b"100755 blob ")):
        raise ValueError("pinned reference must be a regular Git file")
    data = git(repo, "show", f"{revision}:{path}")
    return data, {"path": path, "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    def no_duplicates(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=no_duplicates)


def make_plan(repo, mandate):
    shape(mandate, ("revision", "subject", "mode", "objective", "audience", "questions",
                    "sources", "operator_context", "availability", "stop_condition"),
          ("clarification",), label="mandate")
    rev = nonblank(mandate["revision"], "revision")
    if not re.fullmatch(r"[0-9a-f]{40}", rev) or git(repo, "rev-parse", "--verify", f"{rev}^{{commit}}").decode().strip() != rev:
        raise ValueError("revision must be a full commit SHA")
    mode = nonblank(mandate["mode"], "mode")
    if mode not in {"direct", "complete"}:
        raise ValueError("mode must be direct or complete")
    for key in ("objective", "audience", "stop_condition"):
        nonblank(mandate[key], key)
    shape(mandate["subject"], (), ("product", "organization", "topic"), label="subject")
    if not mandate["subject"]:
        raise ValueError("subject is empty")
    for value in mandate["subject"].values():
        nonblank(value, "subject")
    sources = unique_texts(mandate["sources"], "sources")
    context = unique_texts(mandate["operator_context"], "operator context")
    if sources & context:
        raise ValueError("operator context cannot be an external source")
    registry = read_json(REGISTRY)
    if any(value.strip().casefold() == registry["method_repository"].casefold()
           for value in mandate["subject"].values()):
        raise ValueError("subject must be distinct from the method repository")
    manifests = registry["manifests"]
    avail = mandate["availability"]
    if not isinstance(avail, dict) or any(
        key not in manifests or nonblank(value, "availability") not in CAPABILITIES
        for key, value in avail.items()
    ):
        raise ValueError("invalid domain availability")
    clarification = mandate.get("clarification")
    if "clarification" in mandate:
        nonblank(clarification, "clarification")
    questions = mandate["questions"]
    if not isinstance(questions, list) or (not questions and not clarification):
        raise ValueError("ordered questions or a clarification are required")
    owners, domains, routes = set(), [], []
    for q in questions:
        shape(q, ("id", "domain", "method", "reason"), label="question")
        key, domain, method = (nonblank(q[k], k) for k in ("id", "domain", "method"))
        nonblank(q["reason"], "route reason")
        # Compare only identities here; keep the raw ID for plans and receipts.
        identity = key.strip()
        if identity in owners:
            raise ValueError("duplicate question: " + key)
        owners.add(identity)
        if domain not in manifests:
            raise ValueError("unknown domain: " + domain)
        if domain not in domains:
            domains.append(domain)
        blob, manifest_pin = pinned_file(repo, rev, manifests[domain])
        manifest = json.loads(blob)
        if manifest.get("domain") != domain or method not in manifest.get("methods", {}):
            raise ValueError("method does not belong to the pinned domain: " + method)
        _, method_pin = pinned_file(repo, rev, manifest["methods"][method])
        routes.append({**q, "manifest": {**manifest_pin, "version": manifest["version"]},
                       "method_pin": method_pin, "availability": avail.get(domain, "unavailable")})
    if clarification:
        status = "needs_clarification"
    elif any(r["availability"] == "unavailable" for r in routes):
        status = "route_unavailable"
    else:
        status = "handoff_complete" if mode == "complete" else "ready_direct"
    return {"version": registry["version"], "registry_sha256": digest(registry), "mandate": mandate,
            "status": status, "primary_domain": domains[0] if domains else None,
            "secondary_domains": domains[1:], "excluded_domains": sorted(set(manifests) - set(domains)),
            "routes": routes}


def plan_fingerprint(repo, plan):
    if not isinstance(plan, dict) or "mandate" not in plan or make_plan(repo, plan["mandate"]) != plan:
        raise ValueError("plan differs from the pinned mandate and registry")
    return digest(plan)


def verify_receipt(repo, plan, receipt, events=()):
    plan_pin = plan_fingerprint(repo, plan)
    mandate = plan["mandate"]
    if mandate["mode"] != "direct" or plan["status"] not in {"ready_direct", "route_unavailable"}:
        raise ValueError("receipt requires a resolved direct plan")
    shape(receipt, ("revision", "plan_sha256", "interventions"), label="receipt")
    if receipt["revision"] != mandate["revision"] or receipt["plan_sha256"] != plan_pin:
        raise ValueError("receipt does not match plan or revision")
    items = receipt["interventions"]
    if not isinstance(items, list) or len(items) != len(plan["routes"]):
        raise ValueError("receipt requires one ordered intervention per question")
    by_id = {}
    event_fields = ("event_id", "question", "actor", "method", "output", "revision", "plan_sha256")
    for event in events:
        shape(event, event_fields, label="event record")
        key = nonblank(event["event_id"], "event id")
        if key in by_id:
            raise ValueError("duplicate event id")
        by_id[key] = event
    allowed_sources = set(mandate["sources"])
    matched, manual = set(), 0
    for route, part in zip(plan["routes"], items):
        shape(part, ("question", "method", "status"), ("actor", "output", "sources", "event_id", "reason"),
              label="intervention")
        if part["question"] != route["id"] or part["method"] != route["method"]:
            raise ValueError("intervention differs from planned question or method")
        status = nonblank(part["status"], "intervention status")
        if status in INACTIVE:
            if set(part) & {"event_id", "output", "sources"}:
                raise ValueError("inactive intervention cannot claim output, events or sources")
            nonblank(part.get("reason"), "inactive reason")
            continue
        if route["availability"] == "unavailable":
            raise ValueError("unavailable domain cannot report execution")
        nonblank(part.get("actor"), "actor")
        nonblank(part.get("output"), "output")
        if not unique_texts(part.get("sources"), "sources") <= allowed_sources:
            raise ValueError("source outside the plan or operator context used as evidence")
        if status == "manual_declared":
            if "event_id" in part:
                raise ValueError("manual declaration cannot claim an invocation event")
            manual += 1
        elif status == "invocation_observed":
            key = nonblank(part.get("event_id"), "event id")
            expected = {**{k: part[k] for k in ("question", "actor", "method", "output", "event_id")},
                        "revision": mandate["revision"], "plan_sha256": plan_pin}
            if route["availability"] != "native" or by_id.get(key) != expected or key in matched:
                raise ValueError("invocation requires a matching event from an available native executor")
            matched.add(key)
        else:
            raise ValueError("unknown intervention status")
    return {"status": "receipt_checked", "plan_sha256": plan_pin, "manual_declarations": manual,
            "event_records_matched": len(matched), "interventions_checked": len(items)}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--repo", type=Path, default=ROOT, help="local Git checkout with the pinned objects")
    sub = cli.add_subparsers(dest="command", required=True)
    sub.add_parser("plan").add_argument("mandate", type=Path)
    sub.add_parser("fingerprint").add_argument("plan", type=Path)
    verify = sub.add_parser("verify")
    verify.add_argument("plan", type=Path)
    verify.add_argument("receipt", type=Path)
    verify.add_argument("--events", type=Path, help="separate JSON list from the executor's evidence boundary")
    args = cli.parse_args()
    try:
        if args.command == "plan":
            result = make_plan(args.repo, read_json(args.mandate))
        elif args.command == "fingerprint":
            result = {"plan_sha256": plan_fingerprint(args.repo, read_json(args.plan))}
        else:
            events = read_json(args.events) if args.events else []
            if not isinstance(events, list):
                raise ValueError("event records must be a list")
            result = verify_receipt(args.repo, read_json(args.plan), read_json(args.receipt), events)
    except (ValueError, OSError, KeyError, TypeError) as error:
        cli.exit(1, f"S3 routing: {error}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
