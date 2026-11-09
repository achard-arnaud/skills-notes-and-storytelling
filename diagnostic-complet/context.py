#!/usr/bin/env python3
"""Bounded local task packets and verifiable resumption; no model-window control."""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys


STATUSES = {"planned", "ready", "running", "verified", "blocked", "awaiting_human", "completed", "done"}
SATISFIED = {"verified", "completed", "done"}
TASK_FIELDS = ("id", "title", "objective", "epic", "sprint", "issue", "status", "acceptance", "outputs", "owner", "stop_condition")


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
            "context_coverage": "declared_inputs_only; caller must declare root/routed instructions and mandatory companions explicitly",
            "limits": ["No model context erasure or technical compaction is performed.",
                       "Mechanical completion is not human editorial approval.",
                       "Markdown companions are not auto-expanded; undeclared files are neither read nor measured.",
                       "No task lease is acquired and no writer or board transition is performed.",
                       "Execution readiness is a board snapshot, not a lease or continuing authorization."]}


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
                  "execution_blockers", "packet_mode"):
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


def invalidate_descendants(board: dict, changed_ids: list[str]) -> dict:
    """Return a copied board with changed tasks and dependent results reopened."""
    tasks = _valid_tasks(board)
    if not set(changed_ids) <= tasks.keys():
        raise ValueError("unknown changed task")
    affected = set(changed_ids)
    while True:
        expanded = affected | {tid for tid, task in tasks.items()
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
