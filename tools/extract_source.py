#!/usr/bin/env python3
"""Extract the source whitepaper text from the preserved DOCX file."""

from pathlib import Path
from typing import Optional

from docx import Document


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DOCX = ROOT / "source" / "good-tomorrow-whitepaper.zh-cn.docx"
OUTPUT_MD = ROOT / "source" / "good-tomorrow-whitepaper.zh-cn.md"


def heading_level(text: str) -> Optional[int]:
    if text in {"摘要", "参考文献:"}:
        return 1
    if text and text[0].isdigit() and ". " in text[:5]:
        return 1
    if len(text) > 3 and text[0].isdigit() and text[1] == "." and text[2].isdigit():
        return 2
    if text.startswith("第") and "阶段" in text:
        return 2
    return None


def main() -> None:
    doc = Document(SOURCE_DOCX)
    lines: list[str] = [
        "# Good Tomorrow 白皮书",
        "",
        "> Source extracted from `source/good-tomorrow-whitepaper.zh-cn.docx`.",
        "> This file preserves the original Chinese whitepaper text for translation QA.",
        "",
    ]

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        if text == "Good Tomorrow 白皮书":
            continue
        level = heading_level(text)
        if level == 1:
            lines.extend([f"## {text}", ""])
        elif level == 2:
            lines.extend([f"### {text}", ""])
        else:
            if text == "900,00012=75,000\\frac{900,000}{12}=75,000":
                text = "$\\frac{900,000}{12}=75,000$"
            lines.extend([text.replace("DeFI", "DeFi"), ""])

    OUTPUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
