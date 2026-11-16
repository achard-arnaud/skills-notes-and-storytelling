#!/usr/bin/env python3
"""Bounded local task packets and verifiable resumption; no model-window control."""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys


STATUSES = {"planned", "ready", "running", "verified", "blocked", "awaiting_human", "completed", "done"}
SATISFIED = {"verified", "completed", "done"}
TASK_FIELDS = ("id", "title", "objective", "epic", "sprint", "issue", "status", "acceptance", "outputs", "owner", "stop_condition")
STUDY_SCOPE_FIELDS = ("id", "subject", "input_revision", "scope", "authorized_inputs", "methods")
SHARED_REFERENCE_FIELDS = ("source_study_id", "source_id", "source_revision", "path",
                           "source_status", "status", "purpose", "authorization_ref")
SHARED_REFERENCE_PURPOSES = {"comparison", "contextualization"}


def validate_board(board: dict) -> dict:
    """Return structural errors and a topological order, without changing the board."""
    if not isinstance(board, dict):
        return {"ok": False, "errors": ["board must be an object"], "order": []}
    errors = []
    tasks = board.get("tasks")
    if not isinstance(tasks, list):
        return {"ok": False, "errors": ["tasks must be a list"], "order": []}
    by_id = {}
    for task in tasks:
        if not isinstance(task, dict) or not isinstance(task.get("id"), str) or not task["id"]:
            errors.append("each task needs a nonempty string id")
            continue
        task_id = task["id"]
        if task_id in by_id:
            errors.append(f"duplicate task id: {task_id}")
        by_id[task_id] = task
        if not isinstance(task.get("status", "planned"), str) or task.get("status", "planned") not in STATUSES:
            errors.append(f"{task_id}: unknown status {task.get('status')!r}")
        deps = task.get("depends_on", [])
        if not isinstance(deps, list) or any(not isinstance(dep, str) for dep in deps):
            errors.append(f"{task_id}: depends_on must be a string list")
    if errors:
        return {"ok": False, "errors": errors, "order": []}
    for task_id, task in by_id.items():
        for dep in task.get("depends_on", []):
            if dep not in by_id:
                errors.append(f"{task_id}: missing dependency {dep}")
    if errors:
        return {"ok": False, "errors": errors, "order": []}
    visited, active, order = set(), set(), []

    def visit(task_id):
        if task_id in active:
            raise ValueError(f"dependency cycle at {task_id}")
        if task_id in visited:
            return
        active.add(task_id)
        for dep in by_id[task_id].get("depends_on", []):
            visit(dep)
        active.remove(task_id)
        visited.add(task_id)
        order.append(task_id)

    try:
        for task_id in by_id:
            visit(task_id)
    except ValueError as exc:
        errors.append(str(exc))
    return {"ok": not errors, "errors": errors, "order": order if not errors else []}


def _valid_tasks(board):
    result = validate_board(board)
    if not result["ok"]:
        raise ValueError("; ".join(result["errors"]))
    return {task["id"]: task for task in board["tasks"]}


def ready_tasks(board: dict) -> list[str]:
    """Select planned/ready tasks whose dependencies are mechanically satisfied."""
    tasks = _valid_tasks(board)
    return [task_id for task_id, task in tasks.items()
            if task.get("status", "planned") in {"planned", "ready"}
            and all(tasks[dep].get("status") in SATISFIED for dep in task.get("depends_on", []))]


def local_file(root: Path, raw: str) -> Path:
    """Resolve a declared relative file; reject traversals and symlink escapes."""
    if not isinstance(raw, str) or not raw:
        raise ValueError("file path must be a nonempty string")
    relative = Path(raw)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"path outside root: {raw}")
    root = Path(root).resolve()
    path = (root / relative).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"path outside root: {raw}") from exc
    if not path.is_file():
        raise ValueError(f"missing local file: {raw}")
    return path


def _read_input(root, raw):
    path = local_file(root, raw)
    data = path.read_bytes()
    try:
        content = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"input is not UTF-8: {raw}") from exc
    return {"path": str(path.relative_to(Path(root).resolve())),
            "sha256": hashlib.sha256(data).hexdigest(),
            "bytes": len(data), "words": len(content.split()), "content": content}


def _validate_shared_references(root: Path, study_id: str, raw: object,
                                authorized: list[str], requested: list[str]) -> list[dict]:
    """Validate explicit cross-study references before packet content hydration."""
    if not isinstance(raw, list):
        raise ValueError("study_scope.shared_references must be a list")
    references, seen = [], set()
    for index, item in enumerate(raw):
        prefix = f"study_scope.shared_references[{index}]"
        if not isinstance(item, dict):
            raise ValueError(f"{prefix} must be an object")
        missing = [field for field in SHARED_REFERENCE_FIELDS if field not in item]
        unknown = sorted(set(item) - set(SHARED_REFERENCE_FIELDS))
        if missing:
            raise ValueError(f"{prefix}.{missing[0]} is required")
        if unknown:
            raise ValueError(f"{prefix} has unknown field {unknown[0]}")
        for field in ("source_study_id", "source_id", "path", "source_status", "status",
                      "purpose", "authorization_ref"):
            if not isinstance(item[field], str) or not item[field].strip():
                raise ValueError(f"{prefix}.{field} must be nonempty")
        if item["source_study_id"] == study_id:
            raise ValueError(f"{prefix}.source_study_id must differ from study_scope.id")
        if not isinstance(item["source_revision"], str) or not re.fullmatch(r"[0-9a-f]{64}", item["source_revision"]):
            raise ValueError(f"{prefix}.source_revision must be a lowercase SHA-256")
        if item["purpose"] not in SHARED_REFERENCE_PURPOSES:
            raise ValueError(f"{prefix}.purpose must be comparison or contextualization")
        if item["status"] != item["source_status"]:
            raise ValueError(f"{prefix}: status promotion is forbidden")

        path = local_file(root, item["path"])
        normalized = str(path.relative_to(root))
        if normalized not in authorized:
            raise ValueError(f"shared reference {normalized} is not authorized for study {study_id}")
        if normalized not in requested:
            raise ValueError(f"shared reference {normalized} was not requested for this packet")
        identity = (item["source_study_id"], item["source_id"], normalized)
        if identity in seen:
            raise ValueError(f"duplicate shared reference: {item['source_id']}")

        current = _read_input(root, normalized)
        if current["sha256"] != item["source_revision"]:
            raise ValueError(f"stale source revision for shared reference {item['source_id']}")
        reference = {field: deepcopy(item[field]) for field in SHARED_REFERENCE_FIELDS}
        reference["path"] = normalized
        references.append(reference)
        seen.add(identity)
    return references


def validate_study_scope(root: Path, raw: dict, requested_paths: list[str]) -> dict:
    """Validate one explicit study boundary before hydrating packet contents."""
    if not isinstance(raw, dict):
        raise ValueError("study_scope must be an object")
    for field in ("id", "subject", "input_revision", "scope"):
        if not isinstance(raw.get(field), str) or not raw[field].strip():
            raise ValueError(f"study_scope.{field} must be nonempty")
    if not re.fullmatch(r"[0-9a-f]{64}", raw["input_revision"]):
        raise ValueError("study_scope.input_revision must be a lowercase SHA-256")
    for field in ("authorized_inputs", "methods"):
        values = raw.get(field)
        if (not isinstance(values, list) or not values
                or any(not isinstance(value, str) or not value.strip() for value in values)
                or len(values) != len(set(values))):
            raise ValueError(f"study_scope.{field} must be a nonempty unique string list")
    root = Path(root).resolve()
    authorized = []
    for item in raw["authorized_inputs"]:
        path = local_file(root, item)
        normalized = str(path.relative_to(root))
        if normalized not in authorized:
            authorized.append(normalized)
    requested = []
    for item in requested_paths:
        path = local_file(root, item)
        normalized = str(path.relative_to(root))
        if normalized not in requested:
            requested.append(normalized)
    unauthorized = [path for path in requested if path not in authorized]
    if unauthorized:
        raise ValueError(f"input {unauthorized[0]} is not authorized for study {raw['id']}")
    result = {field: deepcopy(raw[field]) for field in STUDY_SCOPE_FIELDS}
    result["authorized_inputs"] = authorized
    if "shared_references" in raw:
        result["shared_references"] = _validate_shared_references(
            root, raw["id"], raw["shared_references"], authorized, requested)
    return result


def build_packet(root: Path, board: dict, task_id: str, paths: list[str], max_words: int = 8000,
                 for_execution: bool = False) -> dict:
    """Hydrate only explicitly declared files, not all board task inputs or issue bodies."""
    if max_words < 0:
        raise ValueError("max_words must be nonnegative")
    tasks = _valid_tasks(board)
    if task_id not in tasks:
        raise ValueError(f"unknown task: {task_id}")
    if not isinstance(paths, list) or not paths:
        raise ValueError("declare at least one input path")
    task = tasks[task_id]
    dependencies = [{"id": dep, "status": tasks[dep].get("status", "planned")}
                    for dep in task.get("depends_on", [])]
    blockers = [f"dependency {dep['id']} is {dep['status']}" for dep in dependencies
                if dep["status"] not in SATISFIED]
    if task.get("status", "planned") not in {"ready", "running"}:
        blockers.append(f"task state is {task.get('status', 'planned')}; ready or running required")
    raw_study_scope = task.get("study_scope")
    study_scope = None
    if raw_study_scope is None:
        blockers.append("task.study_scope is required for execution")
    else:
        study_scope = validate_study_scope(root, raw_study_scope, paths)
    execution_ready = not blockers
    if for_execution and not execution_ready:
        raise ValueError("task is not execution-ready: " + "; ".join(blockers))
    inputs, seen = [], set()
    for raw in paths:
        item = _read_input(root, raw)
        if item["path"] not in seen:
            inputs.append(item)
            seen.add(item["path"])
    words = sum(item["words"] for item in inputs)
    if words > max_words:
        raise ValueError(f"context budget exceeded: {words} words > {max_words}")
    return {"version": 1, "task": {k: task[k] for k in TASK_FIELDS if k in task},
            "board_id": board.get("id"), "base_sha": board.get("base_sha"),
            "study_scope": study_scope,
            "dependencies": dependencies,
            "write_scope": deepcopy(task.get("outputs", [])),
            "outputs": deepcopy(task.get("outputs", [])),
            "acceptance": deepcopy(task.get("acceptance", [])),
            "stop_condition": task.get("stop_condition") or
                "Stop after the declared artifact and acceptance checks, or record a blocker after two unsuccessful repairs.",
            "execution_ready": execution_ready,
            "execution_blockers": blockers,
            "packet_mode": "execution" if for_execution else "planning",
            "inputs": inputs,
            "budget": {"input_words": words, "input_bytes": sum(i["bytes"] for i in inputs),
                       "max_words": max_words, "token_count": None,
                       "token_measurement": "unknown; words and UTF-8 bytes only",
                       "measurement_scope": "declared input file bodies only; excludes task envelope and runtime context"},
            "context_coverage": "explicit_study_and_declared_inputs_only; caller must declare root/routed instructions and mandatory companions explicitly",
            "limits": ["No model context erasure or technical compaction is performed.",
                       "Mechanical completion is not human editorial approval.",
                       "Markdown companions are not auto-expanded; undeclared files are neither read nor measured.",
                       "No task lease is acquired and no writer or board transition is performed.",
                       "Execution readiness is a board snapshot, not a lease or continuing authorization.",
                       "No previous study, KB or cross-study reference is selected implicitly."]}


def checkpoint(root: Path, packet: dict, next_task: str | None = None, note: str = "") -> dict:
    """Verify actual bytes before retaining a compact input snapshot."""
    entries = []
    for original in packet.get("inputs", []):
        current = _read_input(root, original["path"])
        if current["sha256"] != original.get("sha256"):
            raise ValueError(f"stale packet input: {original['path']}")
        entries.append({k: current[k] for k in ("path", "sha256", "bytes", "words")})
    if not entries:
        raise ValueError("checkpoint requires packet inputs")
    snapshot = {"version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
            "task": deepcopy(packet["task"]), "board_id": packet.get("board_id"),
            "base_sha": packet.get("base_sha"), "inputs": entries,
            "next_task": next_task, "note": note,
            "limits": deepcopy(packet.get("limits", []))}
    for field in ("write_scope", "outputs", "acceptance", "stop_condition", "execution_ready",
                  "execution_blockers", "packet_mode", "study_scope"):
        if field in packet:
            snapshot[field] = deepcopy(packet[field])
    return snapshot


def validate_checkpoint(root: Path, snapshot: dict, base_sha: str | None = None) -> dict:
    """A changed/missing input refuses a silent resume; caller chooses recovery."""
    errors = []
    entries = snapshot.get("inputs")
    if not isinstance(entries, list) or not entries:
        return {"ok": False, "errors": ["checkpoint requires input snapshots"]}
    if base_sha is not None and snapshot.get("base_sha") != base_sha:
        errors.append("base_sha changed")
    for entry in entries:
        if not isinstance(entry, dict) or not {"path", "sha256"} <= entry.keys():
            errors.append("invalid checkpoint input")
            continue
        try:
            current = _read_input(root, entry["path"])
            if current["sha256"] != entry["sha256"]:
                errors.append(f"stale input: {entry['path']}")
        except ValueError as exc:
            errors.append(str(exc))
    return {"ok": not errors, "errors": errors}


def resume_markdown(snapshot: dict) -> str:
    """A compact handoff carrying IDs and verification commands, not source bodies."""
    task = snapshot["task"]
    lines = ["# Reprise du diagnostic complet", "", f"Tâche : {task['id']} — {task.get('title', '')}",
             f"Objectif : {task.get('objective', '')}",
             f"Étude : {(snapshot.get('study_scope') or {}).get('id') or 'non déclarée'}",
             f"Base enregistrée : {snapshot.get('base_sha') or 'inconnue'}",
             f"Prochaine tâche proposée : {snapshot.get('next_task') or 'à sélectionner depuis le board'}", "",
             "Avant reprise : exécuter `context.py resume-check` avec ce checkpoint ; une entrée périmée exige revalidation.",
             "Charger seulement le paquet explicite de la tâche, sans relire tout le corpus.",
             "Le coordinateur reste seul intégrateur Git/board ; pas de CI ni de promotion main dans ce mandat.",
             "Les choix éditoriaux candidats attendent une décision humaine ; aucune compaction technique n’est effectuée."]
    if snapshot.get("note"):
        lines += ["", "Note de passage : " + snapshot["note"]]
    lines += ["", "Entrées vérifiables :"]
    lines += [f"- `{item['path']}` — SHA-256 `{item['sha256']}`" for item in snapshot["inputs"]]
    return "\n".join(lines) + "\n"


def _task_study_id(task: dict) -> str | None:
    scope = task.get("study_scope")
    return scope.get("id") if isinstance(scope, dict) else None


def invalidate_descendants(board: dict, changed_ids: list[str], study_id: str | None = None) -> dict:
    """Return a copied board with changed tasks and eligible descendants reopened."""
    tasks = _valid_tasks(board)
    if not set(changed_ids) <= tasks.keys():
        raise ValueError("unknown changed task")
    if study_id is not None:
        if not isinstance(study_id, str) or not study_id.strip():
            raise ValueError("study_id must be a nonempty string")
        mismatched = [task_id for task_id in changed_ids
                      if _task_study_id(tasks[task_id]) != study_id]
        if mismatched:
            raise ValueError(f"changed task {mismatched[0]} does not belong to study {study_id}")
    affected = set(changed_ids)
    while True:
        expanded = affected | {tid for tid, task in tasks.items()
                               if (study_id is None or _task_study_id(task) == study_id)
                               if affected.intersection(task.get("depends_on", []))}
        if expanded == affected:
            break
        affected = expanded
    result = deepcopy(board)
    for task in result["tasks"]:
        if task["id"] in affected:
            task["previous_status"] = task.get("status", "planned")
            task["status"] = "planned"
            task["invalidated_by"] = sorted(set(changed_ids))
            task["receipt"] = None
    return result


def _load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _emit(data, output):
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if output:
        Path(output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    board = sub.add_parser("board", help="validate board and show ready task IDs")
    board.add_argument("board")
    packet = sub.add_parser("packet", help="build only explicitly declared local inputs")
    packet.add_argument("board")
    packet.add_argument("task_id")
    packet.add_argument("--root", default=str(Path(__file__).resolve().parent))
    packet.add_argument("--input", action="append", required=True, dest="inputs")
    packet.add_argument("--max-words", type=int, default=8000)
    packet.add_argument("--for-execution", action="store_true",
                        help="require ready/running state and satisfied dependencies; does not acquire a lease")
    packet.add_argument("--output")
    check = sub.add_parser("checkpoint", help="verify packet and write compact checkpoint")
    check.add_argument("packet")
    check.add_argument("--root", default=str(Path(__file__).resolve().parent))
    check.add_argument("--next-task")
    check.add_argument("--note", default="")
    check.add_argument("--output")
    check.add_argument("--resume", help="optional Markdown resume path")
    resume = sub.add_parser("resume-check", help="refuse stale inputs before resumption")
    resume.add_argument("checkpoint")
    resume.add_argument("--root", default=str(Path(__file__).resolve().parent))
    resume.add_argument("--base-sha")
    args = parser.parse_args(argv)
    try:
        if args.command == "board":
            data = _load(args.board)
            result = validate_board(data)
            if result["ok"]:
                result["ready"] = ready_tasks(data)
            _emit(result, None)
            return 0 if result["ok"] else 1
        if args.command == "packet":
            result = build_packet(Path(args.root), _load(args.board), args.task_id, args.inputs,
                                  args.max_words, args.for_execution)
            _emit(result, args.output)
        elif args.command == "checkpoint":
            result = checkpoint(Path(args.root), _load(args.packet), args.next_task, args.note)
            _emit(result, args.output)
            if args.resume:
                Path(args.resume).write_text(resume_markdown(result), encoding="utf-8")
        elif args.command == "resume-check":
            result = validate_checkpoint(Path(args.root), _load(args.checkpoint), args.base_sha)
            _emit(result, None)
            return 0 if result["ok"] else 1
        return 0
    except (ValueError, OSError, KeyError) as exc:
        print(json.dumps({"ok": False, "errors": [str(exc)]}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
