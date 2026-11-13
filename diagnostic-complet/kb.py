#!/usr/bin/env python3
"""Incremental, lossless local Markdown intake. No source is promoted to evidence."""
from __future__ import annotations

import argparse
import bisect
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import unicodedata

VERSION = "1.0.0"
ROOT = Path(__file__).resolve().parent
PROFILES_DIR = ROOT / "profiles"
DEFAULT_PROFILE = PROFILES_DIR / "neutral.profile.json"
TERMINOLOGY = json.loads((ROOT / "ontology" / "terminology.json").read_text(encoding="utf-8"))
DOCUMENTARY_STATUS = TERMINOLOGY["documentary_status"]
PROFILE_ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{1,63}$")
# D35: only unambiguous instruction markers. Bare infinitives and singular imperatives (analyser,
# utiliser, analyse, recherche) are also descriptive forms, so they never make a directive on their own.
DIRECTIVE_PATTERN = re.compile(
    r"(?i)^(?:tu\s+(?:dois|devras)\b|vous\s+devez\b|merci\s+de\b|please\b|must\b"
    r"|(?:ignore|oublie)\s+(?:les|toutes|tout|ces|ce|la|le)\b"
    r"|(?:lisez|ajoutez|créez|rédigez|utilisez|analysez|recherchez|ignorez|oubliez|répondez|vérifiez|citez|résumez)\b)")


class ProfileError(ValueError):
    pass


def load_profile(path=None):
    """Load a run profile. Run vocabulary (entities, pillars, namespace) lives ONLY in profiles/.
    The build code ships with the neutral profile; anything else is named explicitly by the caller."""
    path = Path(path) if path else DEFAULT_PROFILE
    profile = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(profile.get("profile_id"), str) or not PROFILE_ID_PATTERN.match(profile["profile_id"]):
        raise ProfileError("profile_id must be lowercase, 2 to 64 characters")
    if not isinstance(profile.get("lexicon_version"), str) or not profile["lexicon_version"]:
        raise ProfileError("lexicon_version is required")
    pillars = profile.get("pillar_lexicon")
    if not isinstance(pillars, dict) or any(not isinstance(v, list) or not all(isinstance(w, str) and w for w in v) for v in pillars.values()):
        raise ProfileError("pillar_lexicon must map pillar ids to lists of terms")
    entities = profile.get("entity_lexicon")
    if not isinstance(entities, dict) or any(not isinstance(r, dict) or not isinstance(r.get("title"), str)
                                             or not isinstance(r.get("aliases"), list) or not r["aliases"] for r in entities.values()):
        raise ProfileError("entity_lexicon must map entity ids to {title, aliases}")
    projection = profile.get("projection")
    if projection is not None:
        namespace = projection.get("namespace", "") if isinstance(projection, dict) else ""
        if not namespace.startswith("knowledge/business/") or ".." in Path(namespace).parts or Path(namespace).is_absolute():
            raise ProfileError("projection namespace must live under knowledge/business/")
    return profile


def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode("utf-8")).hexdigest()


def normalized(text):
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def _json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, path)


def _match(text, phrase):
    return re.search(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", text, re.IGNORECASE)


def classify(text, profile=None):
    """Candidate pillars and explicit lexicon matches with exact evidence, under one run profile."""
    profile = profile if isinstance(profile, dict) else load_profile(profile)
    version = profile["lexicon_version"]
    pillars = []
    for pid, words in profile["pillar_lexicon"].items():
        hits = sorted({m.group(0) for w in words if (m := _match(text, w))})
        if hits:
            pillars.append({"id": pid, "matched_terms": hits, "status": "candidate_keyword", "lexicon_version": version})
    entities = []
    for eid, record in profile["entity_lexicon"].items():
        hits = []
        for alias in record["aliases"]:
            for match in re.finditer(r"(?<!\w)" + re.escape(alias) + r"(?!\w)", text, re.IGNORECASE):
                hits.append({"text": match.group(0), "start": match.start(), "end": match.end()})
        if hits:
            entities.append({"id": "ENTITY-" + eid, "title": record["title"], "matches": hits, "status": "explicit_lexicon_match", "lexicon_version": version})
    return pillars, entities


def _sentences(text, start, end):
    """Conservative boundaries: terminal punctuation and semicolon, outside brackets."""
    lo, depth = start, 0
    for i in range(start, end):
        char = text[i]
        if char in "([{" or char in "«":
            depth += 1
        elif char in ")]}" or char in "»":
            depth = max(depth - 1, 0)
        if depth or char not in ".!?;":
            continue
        # Keep decimal numbers, URLs and common abbreviations intact.
        if char == ".":
            prefix = text[max(lo, i - 8):i + 1]
            if re.fullmatch(r"\s*\d+\.", text[lo:i + 1]):
                continue
            if re.search(r"\b(?:M|Mme|Dr|Mr|etc|ex|e\.g|i\.e)\.$", prefix, re.I):
                continue
            if i > start and i + 1 < end and text[i - 1].isdigit() and text[i + 1].isdigit():
                continue
        if i + 1 == end or text[i + 1].isspace():
            yield lo, i + 1
            lo = i + 1
    if lo < end:
        yield lo, end


def split_units(text):
    """Yield exact character ranges; tables/code are deliberately nonsemantic units."""
    lines = text.splitlines(keepends=True)
    starts, cursor = [], 0
    for line in lines:
        starts.append(cursor)
        cursor += len(line)
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        fence = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence:
            j = i + 1
            while j < len(lines):
                closing = re.match(r"^\s*(`{3,}|~{3,})\s*$", lines[j])
                if closing and closing.group(1)[0] == fence.group(1)[0] and len(closing.group(1)) >= len(fence.group(1)):
                    j += 1
                    break
                j += 1
            yield "code", starts[i], starts[j] if j < len(lines) else len(text), False
            i = j
            continue
        # Leading or internal pipes identify candidate table; require delimiter row.
        if i + 1 < len(lines) and "|" in line and re.match(r"^\s*\|?\s*:?-{3,}:?\s*\|", lines[i + 1]):
            j = i + 2
            while j < len(lines) and "|" in lines[j] and lines[j].strip():
                j += 1
            yield "table", starts[i], starts[j] if j < len(lines) else len(text), False
            i = j
            continue
        if re.match(r"^\s{0,3}#{1,6}\s+", line):
            yield "heading", starts[i], starts[i] + len(line.rstrip("\r\n")), False
            i += 1
            continue
        if i + 1 < len(lines) and re.match(r"^\s*(?:={3,}|-{3,})\s*$", lines[i + 1]):
            yield "heading", starts[i], starts[i + 1] + len(lines[i + 1].rstrip("\r\n")), False
            i += 2
            continue
        lo = starts[i]
        j = i + 1
        # Each list item starts its own proposition block; continuation stays attached.
        while j < len(lines) and lines[j].strip() and not re.match(r"^\s*(?:#{1,6}\s|[-*+]\s|\d+[.)]\s|`{3,}|~{3,})", lines[j]):
            if j + 1 < len(lines) and "|" in lines[j] and re.match(r"^\s*\|?\s*:?-{3,}:?\s*\|", lines[j + 1]):
                break
            j += 1
        hi = starts[j] if j < len(lines) else len(text)
        for begin, end in _sentences(text, lo, hi):
            while begin < end and text[begin].isspace():
                begin += 1
            while end > begin and text[end - 1].isspace():
                end -= 1
            if begin == end:
                continue
            value = text[begin:end]
            content = re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+|>\s*)", "", value)
            if content.rstrip().endswith("?"):
                kind = "question"
            elif DIRECTIVE_PATTERN.match(content):
                kind = "directive"
            else:
                kind = "assertion"
            yield kind, begin, end, True
        i = j


@contextmanager
def _writer_lock(out):
    lock = out / ".ingest.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise ValueError("Intake writer already active; inspect .ingest.lock before retry") from exc
    try:
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        yield
    finally:
        lock.unlink(missing_ok=True)


def build_graph(index):
    nodes, edges = [], []
    for source in index["sources"]:
        nodes.append({"id": source["id"], "type": "source", "kind": "source", "label": source["title"], "sha256": source["sha256"]})
    used_pillars, used_entities = {}, {}
    for atom in index["atoms"]:
        nodes.append({"id": atom["id"], "type": "atom", "kind": atom["kind"], "label": atom["text"][:180], "status": atom["status"], "structural": not atom["semantic_atomization"]})
        for occurrence in atom["occurrences"]:
            edges.append({"id": "EDGE-" + occurrence["id"][4:], "from": occurrence["source_id"], "to": atom["id"], "kind": "derived_from", "occurrence_id": occurrence["id"], "locator": occurrence["locators"], "meaning": "documentary provenance, not truth"})
        for pillar in atom["candidate_pillars"]:
            pid = "PILLAR-" + pillar["id"]
            used_pillars[pid] = {"id": pid, "type": "pillar", "kind": "candidate_pillar", "label": pillar["id"]}
            edges.append({"id": "EDGE-" + digest(atom["id"] + pid)[:24], "from": atom["id"], "to": pid, "kind": "candidate_classification", "matched_terms": pillar["matched_terms"], "lexicon_version": index["lexicon_version"], "status": "candidate_keyword"})
        for entity in atom["entities"]:
            used_entities[entity["id"]] = {"id": entity["id"], "type": "entity", "kind": "entity", "label": entity["title"], "lexicon_version": index["lexicon_version"]}
            edges.append({"id": "EDGE-" + digest(atom["id"] + entity["id"])[:24], "from": atom["id"], "to": entity["id"], "kind": "explicit_mention", "matches": entity["matches"], "lexicon_version": index["lexicon_version"]})
    nodes.extend(used_pillars[k] for k in sorted(used_pillars))
    nodes.extend(used_entities[k] for k in sorted(used_entities))
    return {"schema_version": VERSION, "projection": "documentary_kb", "nodes": nodes, "edges": edges,
            "limits": "No causal edges; keyword classifications are candidates. Documents remain supplied_unverified."}


def _write_atom(path, atom):
    # JSON values are valid YAML scalars; exact text is preserved in atom JSON + offsets.
    keys = ("id", "kind", "status", "semantic_atomization", "normalization_version")
    front = ["---"] + [f"{key}: {json.dumps(atom[key], ensure_ascii=False)}" for key in keys]
    front += ["candidate_pillars: " + json.dumps([p["id"] for p in atom["candidate_pillars"]]),
              "occurrence_ids: " + json.dumps([o["id"] for o in atom["occurrences"]]), "---", ""]
    temp = path.with_name(path.name + ".tmp")
    temp.write_text("\n".join(front) + atom["text"] + "\n", encoding="utf-8")
    os.replace(temp, path)


def ingest_files(paths, out, source_kind="supplied_context", allow_private_git=False, profile=None):
    """Incremental ingestion; old versions and occurrences remain, no deletion or merging of meaning."""
    out = Path(out).resolve()
    # Public method repository is always excluded. Other Git destinations require
    # an explicit caller declaration; visibility is not discoverable offline.
    public_method_root = Path(__file__).resolve().parent.parent
    if out.is_relative_to(public_method_root):
        raise ValueError("KB corpus forbidden under the public business method repository, even with private Git opt-in")
    under_git = any((parent / ".git").exists() for parent in (out, *out.parents))
    if under_git and not allow_private_git:
        raise ValueError("KB corpus must be outside every Git repository unless caller explicitly declares a private Git destination")
    input_paths = sorted({Path(p).resolve() for p in paths}, key=str)
    if not input_paths:
        raise ValueError("At least one Markdown/text input required")
    for path in input_paths:
        if not path.is_file() or path.suffix.lower() not in {".md", ".markdown", ".txt"}:
            raise ValueError(f"Expected extracted Markdown/text file: {path.name}")
    profile = profile if isinstance(profile, dict) else load_profile(profile)
    out.mkdir(parents=True, exist_ok=True)
    with _writer_lock(out):
        index_path = out / "kb.json"
        if index_path.exists():
            index = json.loads(index_path.read_text(encoding="utf-8"))
            if index.get("schema_version") != VERSION or index.get("lexicon_version") != profile["lexicon_version"]:
                raise ValueError("Explicit migration required for changed KB/lexicon version")
            # One KB, one run profile: vocabularies are never mixed inside one index.
            if index.get("profile_id") != profile["profile_id"]:
                raise ValueError("KB index belongs to another run profile or predates profile_id: explicit migration required")
        else:
            index = {"schema_version": VERSION, "profile_id": profile["profile_id"], "lexicon_version": profile["lexicon_version"],
                     "sources": [], "atoms": [], "versions": [], "location_heads": {},
                     "normalization_version": "NFKC-casefold-whitespace-v1", "status": DOCUMENTARY_STATUS}
        sources = {s["id"]: s for s in index["sources"]}
        atoms = {a["id"]: a for a in index["atoms"]}
        # Source copies are authority. Any damage stops intake rather than hiding it.
        for source in sources.values():
            saved = out / source["copy_path"]
            if not saved.resolve().is_relative_to(out) or not saved.is_file() or digest(saved.read_bytes()) != source["sha256"]:
                raise ValueError(f"Preserved source missing or corrupt: {source['id']}")
        copies = out / "sources"
        atom_dir = out / "atoms"
        copies.mkdir(exist_ok=True)
        atom_dir.mkdir(exist_ok=True)
        added_sources = added_atoms = added_occurrences = 0
        for path in input_paths:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
            source_hash = digest(raw)
            sid = "SRC-" + source_hash
            location = str(path)
            prior_head = index.setdefault("location_heads", {}).get(location)
            previous = [prior_head] if prior_head and prior_head != sid else []
            if sid not in sources:
                copy_path = "sources/" + sid + ".source"
                source = {"id": sid, "sha256": source_hash, "size_bytes": len(raw), "title": path.name,
                          "kind": source_kind, "status": DOCUMENTARY_STATUS, "encoding": "utf-8", "copy_path": copy_path,
                          "locations": [], "supersedes": sorted(previous)}
                target = out / copy_path
                temp = target.with_suffix(".tmp")
                temp.write_bytes(raw)
                os.replace(temp, target)
                sources[sid] = source
                added_sources += 1
            source = sources[sid]
            if location not in source["locations"]:
                source["locations"].append(location)
                source["locations"].sort()
            for old_sid in previous:
                relation = {"sequence": len(index["versions"]) + 1, "source_id": sid, "supersedes": old_sid, "location": location, "meaning": "changed bytes at same path; no semantic reconciliation"}
                index["versions"].append(relation)
                if old_sid not in source["supersedes"]:
                    source["supersedes"].append(old_sid)
            index["location_heads"][location] = sid
            line_starts = [0] + [m.end() for m in re.finditer("\n", text)]
            byte_starts = [0]
            for char in text:
                byte_starts.append(byte_starts[-1] + len(char.encode("utf-8")))
            units = list(split_units(text))
            cursor = covered_chars = unexplained_chars = 0
            for _, lo, hi, _ in units:
                unexplained_chars += sum(not c.isspace() for c in text[cursor:lo])
                covered_chars += hi - lo
                cursor = hi
            unexplained_chars += sum(not c.isspace() for c in text[cursor:])
            source["coverage"] = {"input_characters": len(text), "input_bytes": len(raw), "input_lines": len(text.splitlines()),
                                  "units": len(units), "unit_characters": covered_chars,
                                  "uncovered_characters": len(text) - covered_chars, "unexplained_non_whitespace_characters": unexplained_chars,
                                  "meaning": "mechanical extraction coverage only; no claim of full semantic reading"}
            for kind, lo, hi, semantic in units:
                value = text[lo:hi]
                content_key = kind + "\0" + normalized(value)
                aid = "ATOM-" + digest(content_key)
                oid = "OCC-" + digest(sid + f":{lo}:{hi}:" + value)
                if aid not in atoms:
                    pillars, entities = classify(value, profile)
                    atoms[aid] = {"id": aid, "kind": kind, "status": DOCUMENTARY_STATUS, "text": value,
                                  "normalized_text": normalized(value), "normalization_version": index["normalization_version"],
                                  "semantic_atomization": semantic, "atomization_method": "heuristic_sentence_proposition" if semantic else "structural_block_not_semantically_atomized",
                                  "candidate_pillars": pillars, "entities": entities, "occurrences": []}
                    added_atoms += 1
                atom = atoms[aid]
                occurrence = next((o for o in atom["occurrences"] if o["id"] == oid), None)
                if occurrence is None:
                    occurrence = {"id": oid, "source_id": sid, "char_start": lo, "char_end": hi,
                                  "byte_start": byte_starts[lo], "byte_end": byte_starts[hi],
                                  "line_start": bisect.bisect_right(line_starts, lo),
                                  "line_end": bisect.bisect_right(line_starts, max(lo, hi - 1)),
                                  "text": value, "sha256": digest(value), "locators": []}
                    atom["occurrences"].append(occurrence)
                    added_occurrences += 1
                occurrence["locators"] = sorted(set(occurrence["locators"]) | set(source["locations"]))
        # New path aliases must be propagated to all occurrences of identical source bytes.
        for atom in atoms.values():
            for occurrence in atom["occurrences"]:
                occurrence["locators"] = sorted(set(occurrence["locators"]) | set(sources[occurrence["source_id"]]["locations"]))
            atom["occurrences"].sort(key=lambda x: x["id"])
        index["sources"] = sorted(sources.values(), key=lambda x: x["id"])
        index["atoms"] = sorted(atoms.values(), key=lambda x: x["id"])
        index["versions"].sort(key=lambda x: x["sequence"])
        errors = validate_kb(index, out)
        if errors:
            raise ValueError("Invalid KB: " + "; ".join(errors[:10]))
        for atom in index["atoms"]:
            _write_atom(atom_dir / (atom["id"] + ".md"), atom)
        graph = build_graph(index)
        _json(out / "graph.json", graph)
        _json(out / "sources-manifest.json", {"schema_version": VERSION, "sources": index["sources"], "versions": index["versions"], "location_heads": index["location_heads"]})
        _json(index_path, index)
        return {"schema_version": VERSION, "source_count": len(sources), "atom_count": len(atoms),
                "occurrence_count": sum(len(a["occurrences"]) for a in atoms.values()),
                "added_sources": added_sources, "added_atoms": added_atoms, "added_occurrences": added_occurrences,
                "nodes": len(graph["nodes"]), "edges": len(graph["edges"]), "errors": [], "out": str(out),
                "destination_policy": {"under_git": under_git, "allow_private_git": bool(allow_private_git),
                                       "visibility_verification": "caller responsibility; not verified by offline ingestion"},
                "coverage": {"input_characters": sum(s.get("coverage", {}).get("input_characters", 0) for s in sources.values()),
                             "input_bytes": sum(s["size_bytes"] for s in sources.values()),
                             "unexplained_non_whitespace_characters": sum(s.get("coverage", {}).get("unexplained_non_whitespace_characters", 0) for s in sources.values()),
                             "meaning": "extraction measured; semantic review remains pending"}}


def validate_kb(index, out):
    out = Path(out)
    errors, ids = [], set()
    sources = {s["id"]: s for s in index["sources"]}
    texts, source_bytes, source_lines = {}, {}, {}
    for source in sources.values():
        path = out / source["copy_path"]
        if not path.resolve().is_relative_to(out.resolve()):
            errors.append(f"source path escapes KB: {source['id']}")
            continue
        raw = path.read_bytes()
        if digest(raw) != source["sha256"]:
            errors.append(f"source hash mismatch: {source['id']}")
        texts[source["id"]] = raw.decode("utf-8")
        source_bytes[source["id"]] = raw
        source_lines[source["id"]] = [0] + [m.end() for m in re.finditer("\n", texts[source["id"]])]
    for atom in index["atoms"]:
        if atom["id"] != "ATOM-" + digest(atom["kind"] + "\0" + atom["normalized_text"]):
            errors.append("atom identity mismatch: " + atom["id"])
        if atom["id"] in ids:
            errors.append("duplicate atom id: " + atom["id"])
        ids.add(atom["id"])
        if atom["status"] != DOCUMENTARY_STATUS:
            errors.append("automatic status promotion forbidden: " + atom["id"])
        if atom["kind"] in {"table", "code"} and atom["semantic_atomization"]:
            errors.append("structural block falsely marked atomic: " + atom["id"])
        for occurrence in atom["occurrences"]:
            if occurrence["id"] in ids:
                errors.append("duplicate occurrence id: " + occurrence["id"])
            ids.add(occurrence["id"])
            if occurrence["source_id"] not in sources:
                errors.append("unknown occurrence source: " + occurrence["id"])
                continue
            text = texts.get(occurrence["source_id"], "")
            lo, hi = occurrence["char_start"], occurrence["char_end"]
            if not (isinstance(lo, int) and isinstance(hi, int) and 0 <= lo < hi <= len(text)):
                errors.append("occurrence range invalid: " + occurrence["id"])
                continue
            value = text[lo:hi]
            if value != occurrence["text"] or digest(value) != occurrence["sha256"] or normalized(value) != atom["normalized_text"]:
                errors.append("occurrence text/offset mismatch: " + occurrence["id"])
            if source_bytes[occurrence["source_id"]][occurrence["byte_start"]:occurrence["byte_end"]] != value.encode("utf-8"):
                errors.append("occurrence byte offset mismatch: " + occurrence["id"])
            starts = source_lines[occurrence["source_id"]]
            if occurrence["line_start"] != bisect.bisect_right(starts, lo) or occurrence["line_end"] != bisect.bisect_right(starts, hi - 1):
                errors.append("occurrence line mismatch: " + occurrence["id"])
            if occurrence["id"] != "OCC-" + digest(occurrence["source_id"] + f":{lo}:{hi}:" + value):
                errors.append("occurrence identity mismatch: " + occurrence["id"])
    graph = build_graph(index)
    node_ids = [n["id"] for n in graph["nodes"]]
    node_set = set(node_ids)
    if len(node_ids) != len(set(node_ids)):
        errors.append("duplicate graph node id")
    edge_ids = [e["id"] for e in graph["edges"]]
    if len(edge_ids) != len(set(edge_ids)):
        errors.append("duplicate graph edge id")
    for edge in graph["edges"]:
        if edge["from"] not in node_set or edge["to"] not in node_set:
            errors.append("unresolved graph edge: " + edge["id"])
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--source-kind", default="supplied_context")
    parser.add_argument("--profile", type=Path, default=None, help="run profile JSON; default is the neutral profile (no run vocabulary)")
    parser.add_argument("--allow-private-git", action="store_true", help="Caller declares Git destination private after checking visibility; public method repo remains forbidden")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(ingest_files(args.paths, args.out, args.source_kind, allow_private_git=args.allow_private_git, profile=args.profile), ensure_ascii=False, indent=2))
        return 0
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, KeyError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
