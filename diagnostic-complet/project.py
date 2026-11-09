#!/usr/bin/env python3
"""Project a private business KB into a Graph1 namespace, without touching the frozen formation graph.

Guards: the frozen graph hash must match before and after; writes only under knowledge/business/;
never under canonical/, build/, tmp_extract/, scripts/, tests/, docs/ or .github/; never deletes.
Raw HTML, when included, is gzip-compressed deterministically (lossless).
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

FROZEN_GRAPH = "build/graph.json"
# No default namespace: each run declares projection.namespace in its profile (profiles/<run>.profile.json).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb import load_profile  # noqa: E402
FORBIDDEN_TOP = {"canonical", "build", "tmp_extract", "scripts", "tests", "docs", ".github", ".git"}


class ProjectionError(ValueError):
    pass


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_namespace(root: Path, namespace: str) -> Path:
    parts = Path(namespace).parts
    if not namespace.startswith("knowledge/business/") or ".." in parts or Path(namespace).is_absolute():
        raise ProjectionError("namespace must be under knowledge/business/")
    if parts[0] in FORBIDDEN_TOP:
        raise ProjectionError(f"namespace may not live under {parts[0]}")
    target = (root / namespace).resolve()
    if root.resolve() not in target.parents:
        raise ProjectionError("namespace escapes the Graph1 root")
    return target


def _write(target: Path, data: bytes, written: list):
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.read_bytes() == data:
        return
    target.write_bytes(data)
    written.append(target)


def project(graph1_root: Path, frozen_sha: str, sources: dict[str, Path], namespace: str | None = None,
            include_raw: Path | None = None, dry_run: bool = False, shard_atoms: int = 0,
            compress_over: int = 0, only: set[str] | None = None, manifest: bool = True) -> dict:
    if namespace is None:
        raise ProjectionError("namespace required: declare projection.namespace in the run profile")
    root = Path(graph1_root)
    frozen = root / FROZEN_GRAPH
    if not frozen.exists() or sha256_file(frozen) != frozen_sha:
        raise ProjectionError("frozen formation graph hash does not match the declared baseline; refusing")
    target = check_namespace(root, namespace)
    written: list[Path] = []
    entries = []
    in_batch = 0
    for subdir, src in sorted(sources.items()):
        src = Path(src)
        files = [src] if src.is_file() else sorted(p for p in src.rglob("*") if p.is_file())
        for path in files:
            rel = Path(subdir) / (path.name if src.is_file() else path.relative_to(src))
            data = path.read_bytes()
            extra = {}
            if shard_atoms and rel.parent.name == "atoms":
                rel = rel.parent / path.stem.split("-", 1)[-1][:shard_atoms] / rel.name
            if compress_over and path.suffix == ".json" and len(data) > compress_over:
                extra = {"lossless": "gzip", "original_sha256": hashlib.sha256(data).hexdigest(), "original_bytes": len(data)}
                data = gzip.compress(data, mtime=0)
                rel = rel.with_name(rel.name + ".gz")
            entries.append({"path": str(rel), "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), **extra})
            selected = only is None or any(str(rel).startswith(prefix) for prefix in only)
            if selected and not dry_run:
                _write(target / rel, data, written)
            if selected:
                in_batch += 1
    if include_raw:
        for path in sorted(Path(include_raw).glob("*.html")):
            data = gzip.compress(path.read_bytes(), mtime=0)
            rel = Path("raw") / (path.name + ".gz")
            entries.append({"path": str(rel), "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "lossless": "gzip"})
            selected = only is None or any(str(rel).startswith(prefix) for prefix in only)
            if selected and not dry_run:
                _write(target / rel, data, written)
            if selected:
                in_batch += 1
    manifest_doc = {"namespace": namespace, "frozen_graph_sha256": frozen_sha, "files": len(entries),
                "total_bytes": sum(e["bytes"] for e in entries), "entries": entries,
                "rules": ["private corpus; not for the public repository", "imported sources are supplied, not verified",
                          "the frozen formation graph is separate and unchanged"]}
    if manifest and not dry_run:
        _write(target / "MANIFEST.json", (json.dumps(manifest_doc, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode(), written)
    after = sha256_file(frozen)
    if after != frozen_sha:
        raise ProjectionError("frozen graph changed during projection")
    outside = [p for p in written if target not in p.parents and p != target]
    if outside:
        raise ProjectionError(f"wrote outside the namespace: {outside}")
    return {"namespace": namespace, "dry_run": dry_run, "files": len(entries), "in_batch": in_batch, "total_bytes": manifest_doc["total_bytes"],
            "written": len(written), "frozen_graph_unchanged": after == frozen_sha}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--graph1", required=True, type=Path)
    parser.add_argument("--frozen-sha", required=True)
    parser.add_argument("--namespace")
    parser.add_argument("--profile", type=Path, help="run profile; its projection.namespace is used when --namespace is absent")
    parser.add_argument("--source", action="append", default=[], metavar="SUBDIR=PATH")
    parser.add_argument("--raw-html", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--shard-atoms", type=int, default=0, help="put atoms in subdirectories of N hex characters")
    parser.add_argument("--compress-over", type=int, default=0, help="gzip JSON files larger than N bytes, losslessly")
    parser.add_argument("--no-manifest", action="store_true", help="skip MANIFEST.json (intermediate batch)")
    parser.add_argument("--only", action="append", help="only entries whose relative path starts with this prefix (batch publication)")
    args = parser.parse_args(argv)
    namespace = args.namespace
    if namespace is None and args.profile:
        namespace = (load_profile(args.profile).get("projection") or {}).get("namespace")
    sources = {}
    for item in args.source:
        key, _, value = item.partition("=")
        sources[key] = Path(value)
    print(json.dumps(project(args.graph1, args.frozen_sha, sources, namespace, args.raw_html, args.dry_run,
                     args.shard_atoms, args.compress_over, set(args.only) if args.only else None, not args.no_manifest),
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
