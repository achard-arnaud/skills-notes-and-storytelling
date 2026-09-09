#!/usr/bin/env python3
import json
from pathlib import Path
from src.template_types import OutputTemplateType

ROOT = Path(__file__).resolve().parents[1]

def main():
    manifest = json.loads((ROOT / "templates" / "manifest.json").read_text())
    manifest_types = {x["type"] for x in manifest["templates"]}
    enum_types = {x.value for x in OutputTemplateType}
    missing = enum_types - manifest_types
    extra = manifest_types - enum_types
    if missing or extra:
        raise SystemExit(f"template enum/manifest mismatch missing={sorted(missing)} extra={sorted(extra)}")
    for item in manifest["templates"]:
        lo, hi = item["page_range"]
        if lo < 1 or hi < lo:
            raise SystemExit(f"invalid page range: {item}")
        if item["lifecycle"] not in {"candidate","validated","promoted","retired"}:
            raise SystemExit(f"invalid lifecycle: {item}")
    print("contracts: PASS")

if __name__ == "__main__":
    main()
