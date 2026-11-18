#!/usr/bin/env python3
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.template_types import OutputTemplateType, GenerationMode, TemplateClass

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
        template_class = schema.get("properties", {}).get("template_class", {})
        classes = {item.value for item in TemplateClass}
        if "enum" in template_class and set(template_class["enum"]) != classes:
            raise SystemExit(f"template class/schema mismatch in {path.relative_to(ROOT)}")
        if "const" in template_class and template_class["const"] not in classes:
            raise SystemExit(f"unknown template class in {path.relative_to(ROOT)}")
        template_type = schema.get("properties", {}).get("template_type")
        if template_type is None:
            continue
        if "const" in template_type:
            # A template-specific contract may constrain the canonical enum to one registered type.
            value = template_type["const"]
            if value not in enum_types:
                raise SystemExit(
                    f"unknown template const in {path.relative_to(ROOT)}: {value}"
                )
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

def check_relation_catalog():
    catalog = load_json("contracts/relation-types.json")
    names = [r["id"] for r in catalog["relations"]]
    if len(names) != len(set(names)) or not names:
        raise SystemExit("duplicate or empty relation catalogue")
    schema = load_json("contracts/claims-graph-light.schema.json")
    allowed = schema["properties"]["edges"]["items"]["properties"]["type"]["enum"]
    workflow = (ROOT / "references/workflow.md").read_text()
    line = next(line for line in workflow.splitlines() if line.startswith("Edge types:"))
    documented = re.findall(r"[a-z_]+", line.split("`", 1)[1].split("`", 1)[0])
    fixture = load_json("tests/fixtures/relation-catalog-v1.json")
    if set(names) != set(allowed) or set(names) != set(documented):
        raise SystemExit("relation catalogue/schema/workflow mismatch")
    if set(fixture["valid_types"]) != set(names) or set(fixture["invalid_types"]) & set(names):
        raise SystemExit("relation catalogue fixture mismatch")


def check_domain_methods():
    domains = {
        "business": "business-analysis",
        "product": "product-analysis",
        "technical": "technical-analysis",
        "pedagogy": "pedagogical-ai-learning",
        "regulatory": "regulatory-bootstrap",
    }
    method_refs = {}
    for domain, skill in domains.items():
        directory = ROOT / "skills" / skill
        entry = directory / "SKILL.md"
        discovered = ROOT / ".agents" / "skills" / skill / "SKILL.md"
        frontmatter = parse_frontmatter(entry)
        if (frontmatter.get("name") != skill or not frontmatter.get("description")
                or discovered.resolve() != entry.resolve()):
            raise SystemExit(f"invalid domain skill entry: {skill}")

        manifest = load_json(directory / "manifest.json")
        if set(manifest) != {"domain", "version", "methods"} or manifest["domain"] != domain:
            raise SystemExit(f"invalid domain manifest: {skill}")
        check_semver(manifest["version"], skill)
        methods = manifest["methods"]
        if not isinstance(methods, dict) or not methods:
            raise SystemExit(f"missing domain methods: {skill}")
        for ident, reference in methods.items():
            if not isinstance(reference, str):
                raise SystemExit(f"invalid method reference: {ident}")
            if not re.fullmatch(re.escape(domain) + r"\.[a-z0-9]+(?:-[a-z0-9]+)*", ident):
                raise SystemExit(f"invalid method identity: {ident}")
            target = (ROOT / reference).resolve()
            if not target.is_relative_to(ROOT) or not target.is_file() or Path(reference).is_absolute():
                raise SystemExit(f"unresolved method reference: {ident}: {reference}")
            method_refs[ident] = reference

    catalog = load_json("diagnostic-complet/workflows/analysis-methods.v1.json")
    for ident, method in catalog["methods"].items():
        note = method["note"]
        if note.startswith("https://"):
            continue
        if method_refs.get(ident) != note:
            raise SystemExit(f"planner method differs from domain manifest: {ident}")
        if hashlib.sha256((ROOT / note).read_bytes()).hexdigest() != method["method_version"]:
            raise SystemExit(f"stale planner method version: {ident}")


def main():
    check_relation_catalog()
    check_domain_methods()
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
    valid_template_classes = {x.value for x in TemplateClass}
    mode_enum = {x.value for x in GenerationMode}

    for item in manifest["templates"]:
        t = item["type"]
        if item.get("template_class") not in valid_template_classes:
            raise SystemExit(f"missing or invalid template_class for {t}: {item.get('template_class')}")
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
