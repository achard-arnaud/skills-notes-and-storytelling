#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.template_types import OutputTemplateType, GenerationMode

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

def load_json(path):
    return json.loads((ROOT / path).read_text())

def parse_frontmatter(path):
    text = (ROOT / path).read_text()
    if not text.startswith("---\n"):
        raise SystemExit(f"missing front matter: {path}")
    _, block, _ = text.split("---", 2)
    data = {}
    for line in block.strip().splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip()
    return data

def major(v):
    return v.split(".", 1)[0]

def check_semver(v, label):
    if not SEMVER.match(v):
        raise SystemExit(f"invalid semver for {label}: {v}")

def check_template_enums(enum_types):
    """Require every schema that declares template_type to match the canonical enum."""
    for path in sorted((ROOT / "contracts").glob("*.schema.json")):
        schema = json.loads(path.read_text())
        template_type = schema.get("properties", {}).get("template_type")
        if template_type is None:
            continue
        schema_types = set(template_type.get("enum", []))
        if schema_types != enum_types:
            raise SystemExit(
                f"template enum/schema mismatch in {path.relative_to(ROOT)} "
                f"missing={sorted(enum_types - schema_types)} extra={sorted(schema_types - enum_types)}"
            )

def check_docx_runtime_interface():
    path = ROOT / "contracts/docx-runtime-interface.schema.json"
    if not path.exists():
        raise SystemExit("missing DOCX runtime interface contract")
    schema = json.loads(path.read_text())
    properties = schema.get("properties", {})
    if schema.get("required") != ["input", "output"]:
        raise SystemExit("DOCX runtime interface must require input and output")
    if properties.get("input", {}).get("$ref") != "output-spec.schema.json":
        raise SystemExit("DOCX runtime input must reference output-spec.schema.json")
    if properties.get("output", {}).get("$ref") != "qa-report.schema.json":
        raise SystemExit("DOCX runtime output must reference qa-report.schema.json")

def main():
    manifest = load_json("templates/manifest.json")
    workflow_version = manifest["workflow_version"]
    check_semver(workflow_version, "workflow_version")

    manifest_types = {x["type"] for x in manifest["templates"]}
    enum_types = {x.value for x in OutputTemplateType}
    missing = enum_types - manifest_types
    extra = manifest_types - enum_types
    if missing or extra:
        raise SystemExit(f"template enum/manifest mismatch missing={sorted(missing)} extra={sorted(extra)}")
    check_template_enums(enum_types)
    check_docx_runtime_interface()

    valid_template_lifecycle = {"candidate", "validated", "promoted", "retired"}
    mode_enum = {x.value for x in GenerationMode}

    for item in manifest["templates"]:
        t = item["type"]
        check_semver(item["version"], f"{t}.version")
        check_semver(item["qa_fixture_version"], f"{t}.qa_fixture_version")
        lo, hi = item["page_range"]
        if lo < 1 or hi < lo:
            raise SystemExit(f"invalid page range: {item}")
        if item["lifecycle"] not in valid_template_lifecycle:
            raise SystemExit(f"invalid template lifecycle: {item}")
        unknown_modes = set(item["supported_modes"]) - mode_enum
        if unknown_modes:
            raise SystemExit(f"unknown supported modes for {t}: {sorted(unknown_modes)}")
        template_file = ROOT / "templates" / f"{t}.md"
        if not template_file.exists():
            raise SystemExit(f"missing template file: {template_file.relative_to(ROOT)}")
        fixture_path = item["qa_fixture"]
        if not (ROOT / fixture_path).exists():
            raise SystemExit(f"missing QA fixture: {fixture_path}")
        fm = parse_frontmatter(fixture_path)
        if fm.get("template_type") != t:
            raise SystemExit(f"fixture/template type mismatch for {t}: {fm}")
        if major(fm.get("template_version", "")) != major(item["version"]):
            raise SystemExit(f"fixture/template major mismatch for {t}: {fm.get('template_version')} vs {item['version']}")
        if fm.get("fixture_version") != item["qa_fixture_version"]:
            raise SystemExit(f"fixture version mismatch for {t}: {fm.get('fixture_version')} vs {item['qa_fixture_version']}")
        if fm.get("workflow_version") != workflow_version:
            raise SystemExit(f"workflow version mismatch for {t}: {fm.get('workflow_version')} vs {workflow_version}")

    modes = load_json("modes/manifest.json")
    manifest_modes = {x["mode"] for x in modes["modes"]}
    if manifest_modes != mode_enum:
        raise SystemExit(f"mode enum/manifest mismatch enum={sorted(mode_enum)} manifest={sorted(manifest_modes)}")

    for item in modes["modes"]:
        m = item["mode"]
        check_semver(item["version"], f"{m}.version")
        check_semver(item["qa_fixture_version"], f"{m}.qa_fixture_version")
        if item["lifecycle"] not in {"candidate", "validated", "promoted", "retired", "todo"}:
            raise SystemExit(f"invalid mode lifecycle: {item}")
        fixture_path = item["qa_fixture"]
        if not (ROOT / fixture_path).exists():
            raise SystemExit(f"missing mode fixture: {fixture_path}")
        fm = parse_frontmatter(fixture_path)
        if fm.get("mode") != m:
            raise SystemExit(f"mode fixture mismatch for {m}: {fm}")
        if major(fm.get("mode_version", "")) != major(item["version"]):
            raise SystemExit(f"mode fixture major mismatch for {m}")
        if fm.get("fixture_version") != item["qa_fixture_version"]:
            raise SystemExit(f"mode fixture version mismatch for {m}")

    retro = next(x for x in modes["modes"] if x["mode"] == "retro-engineering")
    if retro["lifecycle"] != "todo":
        raise SystemExit("retro-engineering must remain TODO until implementation gates are explicitly changed")

    print(f"contracts: PASS | templates={len(manifest['templates'])} modes={len(modes['modes'])} workflow={workflow_version}")

if __name__ == "__main__":
    main()
