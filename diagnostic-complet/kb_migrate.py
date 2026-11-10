#!/usr/bin/env python3
"""Explicit, receipted migration of a KB index that predates `profile_id` (RF-06, D37).

Scope: declares the run profile on an index whose schema and lexicon versions already match that
profile. It never reclassifies an atom: a version mismatch is refused, because a new lexicon needs a
re-ingestion, not a label. The receipt holds identifiers and digests only, never corpus content.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

import kb


class MigrationError(ValueError):
    pass


def _sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def plan(kb_dir, profile_path):
    """Read-only decision: what the migration would do, or why it refuses."""
    kb_dir = Path(kb_dir)
    index_path = kb_dir / "kb.json"
    if not index_path.is_file():
        raise MigrationError("no kb.json in this directory")
    profile = kb.load_profile(profile_path)
    index = json.loads(index_path.read_text(encoding="utf-8"))
    declared = index.get("profile_id")
    if declared == profile["profile_id"]:
        return {"action": "none", "reason": "profile_id already declared", "profile_id": declared}
    if declared is not None:
        raise MigrationError(f"index belongs to profile '{declared}', not '{profile['profile_id']}': refused")
    if index.get("schema_version") != kb.VERSION:
        raise MigrationError(f"schema_version {index.get('schema_version')} differs from {kb.VERSION}: re-ingestion required")
    if index.get("lexicon_version") != profile["lexicon_version"]:
        raise MigrationError(f"lexicon_version {index.get('lexicon_version')} differs from profile {profile['lexicon_version']}: re-ingestion required")
    return {"action": "declare_profile_id", "profile_id": profile["profile_id"], "schema_version": index["schema_version"],
            "lexicon_version": index["lexicon_version"], "sources": len(index.get("sources", [])), "atoms": len(index.get("atoms", []))}


def migrate(kb_dir, profile_path, backup_dir=None, receipt_path=None, apply=False):
    decision = plan(kb_dir, profile_path)
    if decision["action"] == "none" or not apply:
        return {**decision, "applied": False}
    if backup_dir is None:
        raise MigrationError("a backup directory is required to apply")
    kb_dir, backup_dir = Path(kb_dir).resolve(), Path(backup_dir).resolve()
    if backup_dir == kb_dir or kb_dir in backup_dir.parents:
        raise MigrationError("the backup must live outside the KB directory")
    index_path = kb_dir / "kb.json"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup = backup_dir / "kb.json.before-profile-id"
    if backup.exists():
        raise MigrationError("a backup already exists there: refused to overwrite")
    shutil.copy2(index_path, backup)
    before = _sha(index_path)
    index = json.loads(index_path.read_text(encoding="utf-8"))
    index = {"schema_version": index["schema_version"], "profile_id": decision["profile_id"], **{k: v for k, v in index.items() if k != "schema_version"}}
    with kb._writer_lock(kb_dir):
        kb._json(index_path, index)
    result = {**decision, "applied": True, "index_sha256_before": before, "index_sha256_after": _sha(index_path), "backup": backup.name}
    if receipt_path:
        Path(receipt_path).write_text(json.dumps({"receipt": "kb-profile-migration", **result}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Declare the run profile on a KB index that predates profile_id. Dry run unless --apply.")
    parser.add_argument("--kb", required=True, type=Path)
    parser.add_argument("--profile", required=True, type=Path)
    parser.add_argument("--backup-dir", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(migrate(args.kb, args.profile, args.backup_dir, args.receipt, args.apply), ensure_ascii=False, indent=2))
    except (MigrationError, kb.ProfileError, ValueError) as error:
        print(f"refused: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
