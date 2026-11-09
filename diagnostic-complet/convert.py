#!/usr/bin/env python3
"""Convert source files to Markdown text for the KB, preserving source bytes and hashes.

Stdlib only, except PDF which needs the optional pypdf; without it the file is reported as
`converter_unavailable` and no text is invented. ZIP members are read with traversal and size
guards. A conversion measures extraction, never truth.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import crawl  # noqa: E402

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
MAX_ZIP_MEMBER = 50 * 1024 * 1024
MAX_ZIP_TOTAL = 200 * 1024 * 1024
SUPPORTED = {".md", ".txt", ".html", ".htm", ".docx", ".pdf", ".zip"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _docx_to_markdown(data: bytes) -> str:
    import io
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        info = archive.getinfo("word/document.xml")
        if info.file_size > MAX_ZIP_MEMBER:
            raise ValueError("document.xml too large")
        root = ET.fromstring(archive.read("word/document.xml"))
    lines = []
    for paragraph in root.iter(W + "p"):
        text = "".join(node.text or "" for node in paragraph.iter(W + "t")).strip()
        if not text:
            continue
        style = paragraph.find(f"{W}pPr/{W}pStyle")
        level = re.match(r"(?i)heading(\d)", style.get(W + "val", "")) if style is not None else None
        in_table = False
        for parent in root.iter(W + "tc"):
            if paragraph in list(parent.iter(W + "p")):
                in_table = True
                break
        lines.append(("#" * int(level.group(1)) + " " + text) if level else (f"| {text}" if in_table else text))
    return "\n\n".join(lines) + "\n"


def _pdf_to_markdown(data: bytes):
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        return None
    import io
    reader = PdfReader(io.BytesIO(data))
    pages = []
    for index, page in enumerate(reader.pages, 1):
        text = (page.extract_text() or "").strip()
        if text:
            pages.append(f"## Page {index}\n\n{text}")
    return "\n\n".join(pages) + "\n"


def convert_bytes(name: str, data: bytes) -> dict:
    """Return {status, converter, markdown?}. Never raises for a single bad file."""
    ext = Path(name).suffix.lower()
    try:
        if ext in {".md", ".txt"}:
            return {"status": "ok", "converter": "passthrough", "markdown": data.decode("utf-8", "replace").replace("\r\n", "\n")}
        if ext in {".html", ".htm"}:
            md, _, _ = crawl.html_to_markdown(data.decode("utf-8", "replace"), name)
            return {"status": "ok", "converter": "stdlib_html", "markdown": md}
        if ext == ".docx":
            return {"status": "ok", "converter": "stdlib_docx", "markdown": _docx_to_markdown(data)}
        if ext == ".pdf":
            md = _pdf_to_markdown(data)
            if md is None:
                return {"status": "converter_unavailable", "converter": "pypdf_missing"}
            return {"status": "ok" if md.strip() else "no_text_layer", "converter": "pypdf", "markdown": md}
    except Exception as error:  # a bad file is reported, never fabricated
        return {"status": "error", "converter": ext, "error": f"{type(error).__name__}: {error}"}
    return {"status": "unsupported", "converter": ext or "none"}


def safe_members(archive: zipfile.ZipFile):
    total = 0
    for info in archive.infolist():
        if info.is_dir():
            continue
        parts = PurePosixPath(info.filename).parts
        if info.filename.startswith(("/", "\\")) or ".." in parts or (parts and re.match(r"^[A-Za-z]:", parts[0])):
            yield info, "path_traversal_refused"
            continue
        total += info.file_size
        if info.file_size > MAX_ZIP_MEMBER or total > MAX_ZIP_TOTAL:
            yield info, "size_limit_refused"
            continue
        yield info, None


def convert_file(path: Path, out_dir: Path) -> list[dict]:
    data = path.read_bytes()
    records = []
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as archive:
            for info, refusal in safe_members(archive):
                rec = {"source": f"{path.name}!{info.filename}"}
                if refusal:
                    rec.update(status=refusal, converter="zip_guard")
                else:
                    member = archive.read(info)
                    rec.update(sha256=sha256(member), **_write(out_dir, info.filename, member))
                records.append(rec)
        return records
    return [{"source": path.name, "sha256": sha256(data), **_write(out_dir, path.name, data)}]


def _write(out_dir: Path, name: str, data: bytes) -> dict:
    result = convert_bytes(name, data)
    markdown = result.pop("markdown", None)
    if markdown:
        stem = re.sub(r"[^A-Za-z0-9._-]+", "-", Path(name).stem).strip("-") or "file"
        target = out_dir / f"{stem}-{sha256(data)[:8]}.md"
        out_dir.mkdir(parents=True, exist_ok=True)
        target.write_text(markdown, encoding="utf-8")
        result.update(markdown_path=str(target), characters=len(markdown))
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("inputs", nargs="+", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args(argv)
    report = []
    for path in args.inputs:
        report.extend(convert_file(path, args.out))
    summary = {}
    for rec in report:
        summary[rec["status"]] = summary.get(rec["status"], 0) + 1
    print(json.dumps({"files": len(report), "by_status": summary, "records": report}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
