#!/usr/bin/env python3
"""Side-story workflow loader and typed-format checks (stdlib only).

`workflows/side-stories.workflow.json` is the single source of truth for types, tags, formats and
routing. This module reads it; runtime.py and render.py derive their vocabulary from it, so a type
cannot exist in the code and be absent from the workflow (same principle as D17 for relations).
Checks here are structural: they never judge editorial quality and never promote anything.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

WORKFLOW_PATH = Path(__file__).resolve().parent / "workflows" / "side-stories.workflow.json"
ACTIVE_STATES = {"validated", "promoted"}


def load_workflow(path: Path | None = None) -> dict:
    return json.loads((path or WORKFLOW_PATH).read_text(encoding="utf-8"))


WORKFLOW = load_workflow()
TYPES = {t["id"]: t for t in WORKFLOW["types"]}
CANONICAL_KINDS = set(TYPES)
LEGACY_MAP = dict(WORKFLOW["legacy_kind_map"])


def words(text) -> int:
    return len(re.findall(r"\w[\w'’-]*", text)) if isinstance(text, str) else 0


def sentences(text) -> int:
    return len([s for s in re.split(r"(?<=[.!?…])\s+", text.strip()) if s.strip()]) if isinstance(text, str) else 0


def filled(value) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return value is not None


def _count(label: str, items, spec: dict, out: list[str]) -> bool:
    if not isinstance(items, list):
        out.append(f"{label}: list required")
        return False
    if "min" in spec and len(items) < spec["min"]:
        out.append(f"{label}: at least {spec['min']} required, found {len(items)}")
    if "max" in spec and len(items) > spec["max"]:
        out.append(f"{label}: at most {spec['max']} allowed, found {len(items)}")
    return True


def _check_lines(payload: dict, fmt: dict, out: list[str]) -> None:
    lines = payload.get("lines")
    if not _count("payload.lines", lines, fmt["count"], out):
        return
    roles = []
    for i, line in enumerate(lines, 1):
        if not isinstance(line, dict):
            out.append(f"payload.lines[{i}]: object required")
            continue
        role = line.get("role")
        if role not in fmt["roles"]:
            out.append(f"payload.lines[{i}]: unknown role {role!r}")
        roles.append(role)
        if not filled(line.get("text")):
            out.append(f"payload.lines[{i}]: text required")
        elif words(line["text"]) > fmt["line"]["max_words"]:
            out.append(f"payload.lines[{i}]: more than {fmt['line']['max_words']} words")
        if role == "fact":
            for key in fmt["line"]["fact_requires"]:
                if not filled(line.get(key)):
                    out.append(f"payload.lines[{i}]: fact requires {key}")
    for role, rule in fmt["role_rules"].items():
        n = roles.count(role)
        if "exactly" in rule and n != rule["exactly"]:
            out.append(f"payload.lines: role {role} must appear exactly {rule['exactly']} time(s), found {n}")
        if "min" in rule and n < rule["min"]:
            out.append(f"payload.lines: role {role} requires at least {rule['min']}, found {n}")
        if "max" in rule and n > rule["max"]:
            out.append(f"payload.lines: role {role} allows at most {rule['max']}, found {n}")
        if rule.get("position") == "first" and roles and roles[0] != role:
            out.append(f"payload.lines: role {role} must come first")


def _check_items(payload: dict, fmt: dict, levels: list[str], out: list[str]) -> None:
    items = payload.get("items")
    if not _count("payload.items", items, fmt["count"], out):
        return
    for i, item in enumerate(items, 1):
        label = f"payload.items[{i}]"
        if not isinstance(item, dict):
            out.append(f"{label}: object required")
            continue
        for key in fmt["item_fields"]:
            if not filled(item.get(key)):
                out.append(f"{label}: {key} required")
        definition = item.get("definition")
        if isinstance(definition, dict):
            if not filled(definition.get("text")):
                out.append(f"{label}: definition.text required")
            source = definition.get("source")
            if not isinstance(source, dict) or any(not filled(source.get(k)) for k in fmt["source_fields"]):
                out.append(f"{label}: definition.source requires {', '.join(fmt['source_fields'])}")
            if definition.get("evidence_level") not in levels:
                out.append(f"{label}: definition.evidence_level must be one of {', '.join(levels)}")
        elif "definition" in item and filled(definition):
            out.append(f"{label}: definition must be an object with text, source, evidence_level")
        perspective = item.get("perspective")
        counted = [item.get(k) for k in ("term", "example", "in_practice", "contrast")]
        if isinstance(definition, dict):
            counted.append(definition.get("text"))
        if isinstance(perspective, dict):
            if perspective.get("mode") not in fmt["perspective_modes"]:
                out.append(f"{label}: perspective.mode must be one of {', '.join(fmt['perspective_modes'])}")
            elif perspective["mode"] == "synthesis":
                if sentences(perspective.get("content")) > fmt["synthesis_max_sentences"]:
                    out.append(f"{label}: synthesis limited to {fmt['synthesis_max_sentences']} sentences")
                counted.append(perspective.get("content"))
            if not filled(perspective.get("content")):
                out.append(f"{label}: perspective.content required")
        elif "perspective" in item and filled(perspective):
            out.append(f"{label}: perspective must be an object with mode and content")
        if sum(words(t) for t in counted) > fmt["item_max_words"]:
            out.append(f"{label}: more than {fmt['item_max_words']} words")


def _check_steps(payload: dict, fmt: dict, out: list[str]) -> None:
    steps = payload.get("steps")
    if not _count("payload.steps", steps, fmt["count"], out):
        return
    total = 0
    for i, step in enumerate(steps, 1):
        if not isinstance(step, dict) or not all(filled(step.get(k)) for k in fmt["step_fields"]):
            out.append(f"payload.steps[{i}]: requires {', '.join(fmt['step_fields'])}")
        else:
            total += words(step["statement"])
    if total > fmt["max_words"]:
        out.append(f"payload.steps: more than {fmt['max_words']} words")


def _check_table(payload: dict, fmt: dict, out: list[str]) -> None:
    table = payload.get("table")
    if not isinstance(table, dict):
        out.append("payload.table: object with columns and rows required")
        return
    columns, rows = table.get("columns"), table.get("rows")
    if not isinstance(columns, list) or not columns:
        out.append("payload.table.columns: list required")
        return
    if len(columns) > fmt["table"]["max_columns"]:
        out.append(f"payload.table.columns: at most {fmt['table']['max_columns']} columns")
    if _count("payload.table.rows", rows, {"min": fmt["table"]["min_rows"], "max": fmt["table"]["max_rows"]}, out):
        for i, row in enumerate(rows, 1):
            if not isinstance(row, list) or len(row) != len(columns) or not all(filled(c) for c in row):
                out.append(f"payload.table.rows[{i}]: one filled cell per column required")


def _check_illustration(payload: dict, fmt: dict, out: list[str]) -> None:
    form = payload.get("form")
    if form not in fmt["forms"]:
        out.append(f"payload.form must be one of {', '.join(fmt['forms'])}")
        return
    text = payload.get("text")
    if not filled(text):
        out.append("payload.text required")
        return
    limit = fmt["quote_max_words"] if form == "quote" else fmt["max_words"]
    if words(text) > limit:
        out.append(f"payload.text: more than {limit} words for form {form}")
    if form == "quote":
        for key in fmt["quote_requires"]:
            if not filled(payload.get(key)):
                out.append(f"payload: quote requires {key}")


def _check_analysis(payload: dict, fmt: dict, levels: list[str], out: list[str]) -> None:
    analysis = payload.get("analysis")
    if not isinstance(analysis, dict):
        out.append("payload.analysis: object required")
        return
    for key in fmt["analysis_required"]:
        if not filled(analysis.get(key)):
            out.append(f"payload.analysis.{key} required")
    positions = analysis.get("positions")
    if isinstance(positions, list):
        _count("payload.analysis.positions", positions, {"min": fmt["positions"]["min"]}, out)
        for i, p in enumerate(positions, 1):
            if not isinstance(p, dict) or not all(filled(p.get(k)) for k in fmt["positions"]["fields"]):
                out.append(f"payload.analysis.positions[{i}]: requires {', '.join(fmt['positions']['fields'])}")
    mechanisms = analysis.get("mechanisms")
    if isinstance(mechanisms, list):
        _count("payload.analysis.mechanisms", mechanisms, {"min": fmt["mechanisms"]["min"]}, out)
        for i, m in enumerate(mechanisms, 1):
            if not isinstance(m, dict) or not all(filled(m.get(k)) for k in fmt["mechanisms"]["fields"]):
                out.append(f"payload.analysis.mechanisms[{i}]: requires {', '.join(fmt['mechanisms']['fields'])}")
            elif m["evidence_status"] not in levels:
                out.append(f"payload.analysis.mechanisms[{i}]: evidence_status must be one of {', '.join(levels)}")
    total = sum(words(analysis.get(k)) for k in ("core_question", "thesis", "takeaway"))
    total += sum(words(p.get("position", "")) + words(p.get("caveat", "")) for p in positions if isinstance(p, dict)) if isinstance(positions, list) else 0
    total += sum(words(m.get("mechanism", "")) for m in mechanisms if isinstance(m, dict)) if isinstance(mechanisms, list) else 0
    if total > fmt["max_words"]:
        out.append(f"payload.analysis: more than {fmt['max_words']} words")


def side_story_findings(side: dict) -> tuple[list[str], list[str]]:
    """Return (blocking, pending) findings for one side story.

    Findings are blocking when the story is validated or promoted, pending (gaps) otherwise. Legacy
    kinds only produce a pending finding naming their canonical replacement.
    """
    kind = side.get("kind")
    state = side.get("state")
    active = isinstance(state, str) and state in ACTIVE_STATES
    problems: list[str] = []
    if not isinstance(kind, str):  # malformed record: runtime.py already reports the invalid kind
        return [], []
    if kind in LEGACY_MAP:
        return [], [f"legacy kind {kind}: use {LEGACY_MAP[kind]}"]
    if kind not in TYPES:
        return [], []
    spec = TYPES[kind]
    fmt = spec["format"]
    if not filled(side.get("problematique")):
        problems.append("problematique required")
    bridge = side.get("bridge")
    if not isinstance(bridge, dict) or not filled(bridge.get("in")) or not filled(bridge.get("out")):
        problems.append("bridge.in and bridge.out required")
    for key in fmt.get("required_top_level", []):
        if kind != "dezoom" and not filled(side.get(key)):  # dezoom keys are enforced by runtime.py
            problems.append(f"{key} required")
    payload = side.get("payload")
    if not isinstance(payload, dict):
        problems.append(f"payload.{fmt['payload_key']} required by the {spec['tag']} format")
    else:
        levels = spec["evidence_levels"]
        if kind == "veille_corporate_perso":
            _check_lines(payload, fmt, problems)
        elif kind == "veille_academique":
            _check_items(payload, fmt, levels, problems)
        elif kind == "dezoom":
            _check_steps(payload, fmt, problems)
        elif kind == "comparator":
            _check_table(payload, fmt, problems)
            if isinstance(side.get("confounders"), list) and not side["confounders"]:
                problems.append("confounders required")
        elif kind == "illustration":
            _check_illustration(payload, fmt, problems)
        elif kind == "analytical_focus":
            _check_analysis(payload, fmt, levels, problems)
    return (problems, []) if active else ([], problems)


def tag_for(kind: str) -> dict | None:
    kind = LEGACY_MAP.get(kind, kind)
    spec = TYPES.get(kind)
    return None if spec is None else {"tag": spec["tag"], "label": spec["label"], **spec["color"]}


def tag_css() -> str:
    """CSS classes `.tag-XXX` for the HTML renderer, from the workflow color tokens."""
    return "".join(
        f".tag-{t['tag']}{{background:{t['color']['bg']};border:1px solid {t['color']['border']};color:#17313d}}"
        for t in WORKFLOW["types"]
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("types", help="list canonical types, tags and examples")
    chk = sub.add_parser("check", help="check the workflow file itself")
    chk.add_argument("--workflow", type=Path)
    args = parser.parse_args(argv)
    if args.command == "types":
        for t in WORKFLOW["types"]:
            print(f"[{t['tag']}] {t['id']} — {t['label']} — exemples {', '.join(t['examples'])}")
        return 0
    wf = load_workflow(args.workflow)
    errors = workflow_errors(wf)
    print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


def workflow_errors(wf: dict) -> list[str]:
    errors: list[str] = []
    ids = [t["id"] for t in wf.get("types", [])]
    tags = [t["tag"] for t in wf.get("types", [])]
    if len(ids) != len(set(ids)):
        errors.append("duplicate type id")
    if len(tags) != len(set(tags)):
        errors.append("duplicate tag")
    for old, new in wf.get("legacy_kind_map", {}).items():
        if new not in ids:
            errors.append(f"legacy kind {old} maps to unknown type {new}")
        if old in ids:
            errors.append(f"legacy kind {old} is also canonical")
    for pillar, route in wf.get("pillar_routing", {}).items():
        for t in route.get("types", []):
            if t not in ids:
                errors.append(f"{pillar} routes to unknown type {t}")
        if not route.get("problematiques") or not route.get("bridges"):
            errors.append(f"{pillar} needs problematiques and bridges")
    for node in wf.get("choice_tree", []):
        target = node.get("yes")
        if target and target not in ids:
            errors.append(f"choice tree targets unknown type {target}")
    return errors


if __name__ == "__main__":
    sys.exit(main())
