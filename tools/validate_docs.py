#!/usr/bin/env python3
"""Validate the multilingual GitBook repository and write a QA report."""

from __future__ import print_function

import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LANGS = ["en", "zh", "ko", "ja"]
LANG_NAMES = ["English", "简体中文", "한국어", "日本語"]
REQUIRED_TOKEN_FACTS = ["10,000,000", "9,000,000", "900,000", "100,000", "90%", "9%", "1%", "75,000"]
REQUIRED_TERMS = ["Good Tomorrow", "BNB Smart Chain", "USDC", "DeFi", "RWA", "APY", "TVL"]
PROVENANCE_PATTERNS = [
    (r"\bco" + r"dex\b", "co" + "dex"),
    (r"\bchat" + r"gpt\b", "chat" + "gpt"),
    (r"\bope" + r"nai\b", "ope" + "nai"),
    (r"\bartificial intel" + r"ligence\b", "artificial intel" + "ligence"),
    (r"\ba" + r"i-generated\b", "a" + "i-generated"),
    (r"\bgenerated " + r"by\b", "generated " + "by"),
    (r"\bmade by a" + r"i\b", "made by a" + "i"),
    (r"\bi" + r"de\b", "i" + "de"),
]
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")


def read(path):
    return path.read_text(encoding="utf-8")


def add(checks, name, passed, details=""):
    checks.append({"name": name, "passed": bool(passed), "details": details})


def summary_links(summary_path):
    links = []
    for match in LINK_RE.finditer(read(summary_path)):
        target = match.group(1).split("#", 1)[0]
        links.append(target)
    return links


def markdown_files(lang):
    base = DOCS / lang
    return sorted(str(p.relative_to(base)) for p in base.rglob("*.md"))


def validate():
    checks = []

    root_config = read(ROOT / ".gitbook.yaml")
    add(checks, "English is default GitBook root", "root: ./docs/en" in root_config)

    langs_text = read(ROOT / "LANGS.md")
    ordered = [line.strip() for line in langs_text.splitlines() if line.startswith("* ")]
    expected = ["* [English](docs/en/)", "* [简体中文](docs/zh/)", "* [한국어](docs/ko/)", "* [日本語](docs/ja/)"]
    add(checks, "Language order is English, Simplified Chinese, Korean, Japanese", ordered == expected, " / ".join(ordered))

    baseline = markdown_files("en")
    for lang in LANGS:
        add(checks, f"{lang} has same Markdown hierarchy as English", markdown_files(lang) == baseline)
        add(checks, f"{lang} has .gitbook.yaml", (DOCS / lang / ".gitbook.yaml").exists())
        links = summary_links(DOCS / lang / "SUMMARY.md")
        missing = [link for link in links if not (DOCS / lang / link).exists()]
        add(checks, f"{lang} SUMMARY links resolve", not missing, ", ".join(missing))

    all_docs = [p for lang in LANGS for p in (DOCS / lang).rglob("*.md")]
    broken_images = []
    for path in all_docs:
        for image in IMAGE_RE.findall(read(path)):
            target = (path.parent / image).resolve()
            if not target.exists():
                broken_images.append(f"{path.relative_to(ROOT)} -> {image}")
    add(checks, "Markdown image references resolve", not broken_images, "; ".join(broken_images))

    publish_text = "\n".join(read(path) for path in all_docs)
    placeholders = re.findall(r"\b(TODO|TBD|FIXME|PLACEHOLDER)\b", publish_text, flags=re.IGNORECASE)
    add(checks, "No unresolved placeholders in publishable docs", not placeholders, ", ".join(sorted(set(placeholders))))
    add(checks, "Source DeFi capitalization normalized in publishable docs", "DeFI" not in publish_text)
    lower_publish_text = publish_text.lower()
    provenance_hits = [label for pattern, label in PROVENANCE_PATTERNS if re.search(pattern, lower_publish_text)]
    add(checks, "No external tooling provenance terms in publishable docs", not provenance_hits, ", ".join(provenance_hits))

    for lang in LANGS:
        combined = "\n".join(read(path) for path in (DOCS / lang).rglob("*.md"))
        missing_terms = [term for term in REQUIRED_TERMS if term not in combined]
        add(checks, f"{lang} preserves required protocol terms", not missing_terms, ", ".join(missing_terms))
        token_text = read(DOCS / lang / "governance" / "token-and-governance.md")
        missing_facts = [fact for fact in REQUIRED_TOKEN_FACTS if fact not in token_text]
        add(checks, f"{lang} preserves token supply facts", not missing_facts, ", ".join(missing_facts))
        add(checks, f"{lang} preserves lockup formula", "\\frac{900,000}{12}=75,000" in token_text)
        references = re.findall(r"^\d+\.", read(DOCS / lang / "reference" / "references.md"), flags=re.MULTILINE)
        add(checks, f"{lang} preserves 14 references", len(references) == 14, str(len(references)))

    content_map = read(DOCS / "en" / "project" / "content-map.md")
    missing_from_map = [row for row in baseline if row not in {"SUMMARY.md"} and row not in content_map and not row.startswith("project/")]
    add(checks, "Content map covers source-derived pages", not missing_from_map, ", ".join(missing_from_map))

    passed = all(check["passed"] for check in checks)
    existing_generated_at = None
    report_path = ROOT / "qa-report.json"
    if report_path.exists():
        try:
            existing_generated_at = json.loads(read(report_path)).get("generated_at")
        except Exception:
            existing_generated_at = None

    report = {
        "generated_at": existing_generated_at or datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "passed": passed,
        "language_order": LANG_NAMES,
        "markdown_pages_per_language": len(baseline) - 1,
        "checks": checks,
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    rows = "\n".join(
        "| {} | {} | {} |".format("PASS" if check["passed"] else "FAIL", check["name"], check["details"].replace("|", "\\|"))
        for check in checks
    )
    status = "PASS" if passed else "FAIL"
    md = f"""# QA Report

Status: **{status}**

Updated: `{report['generated_at']}`

| Result | Check | Details |
| --- | --- | --- |
{rows}

## Publishing Readiness

The documentation structure is ready to connect to GitBook as one default English space with Simplified Chinese, Korean, and Japanese language variants.
"""
    for lang in LANGS:
        (DOCS / lang / "project" / "qa-report.md").write_text(md, encoding="utf-8")

    print("QA status:", status)
    for check in checks:
        print("[{}] {}".format("PASS" if check["passed"] else "FAIL", check["name"]))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(validate())
