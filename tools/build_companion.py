#!/usr/bin/env python3
"""Build the single-file LLM companion: companion/blockcourse-companion.md.

Refreshes schedule/schedule.md from the Gantt workbook first, then concatenates
every Markdown document of the repository in reading order with a table of
contents and a short machine-readable header. Code files are included verbatim
in fenced blocks. Binary files, example data and generated outputs are skipped.

Usage: python3 tools/build_companion.py [--max-tokens N]
Exit code 1 if the estimated token count exceeds --max-tokens (default 150000),
so the CI fails before the bundle outgrows common context windows.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "companion" / "blockcourse-companion.md"

# Reading order. Globs are sorted. A tuple (path, title) names a section.
ORDER = [
    ("llms.txt", "Index (llms.txt)"),
    ("README.md", "Course script"),
    ("schedule/schedule.md", "Schedule"),
    ("protocols/README.md", "Protocol index"),
    ("protocols/P*.md", "Core protocols"),
    ("protocols/X*.md", "Extension protocols"),
    ("background/macrophage_biology.md", "Background reading"),
    ("background/reading_list.md", "Reading list"),
    ("slides/README.md", "Slides index"),
    ("slides/*.pdf", "Slides: extracted text"),
    ("code/README.md", "Code overview"),
    ("code/**/*.R", "Code: R scripts"),
    ("code/**/*.py", "Code: Python scripts"),
    ("code/**/README.md", "Code: folder notes"),
]
SKIP_PARTS = {"example_data", "output", "renv", "__pycache__"}
FENCE = {".R": "r", ".py": "python"}
PDF_MAX_CHARS = 60_000  # per deck, keeps the bundle inside common context windows


def git_rev():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                                       text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "uncommitted"


def files_for(pattern):
    paths = sorted(ROOT.glob(pattern))
    return [p for p in paths if p.is_file() and not (SKIP_PARTS & set(p.parts))
            and "00_TEMPLATE" not in p.name and p.resolve() != OUT.resolve()]


def demote(md: str, levels: int = 1) -> str:
    """Push every ATX heading down so the bundle has one H1."""
    return re.sub(r"^(#{1,5})(\s)", lambda m: "#" * min(6, len(m.group(1)) + levels) + m.group(2), md, flags=re.M)


def pdf_text(p: Path) -> str:
    """Slide text via pdftotext (poppler); empty string if unavailable."""
    try:
        out = subprocess.check_output(["pdftotext", "-layout", str(p), "-"], text=True,
                                      stderr=subprocess.DEVNULL)
    except Exception:
        return ""
    out = re.sub(r"\n{3,}", "\n\n", out).strip()
    if len(out) > PDF_MAX_CHARS:
        out = out[:PDF_MAX_CHARS] + "\n[... truncated for the companion; open the PDF for the rest]"
    return out


def est_tokens(text: str) -> int:
    return int(len(text) / 3.8)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-tokens", type=int, default=150_000)
    args = ap.parse_args()

    sys.path.insert(0, str(ROOT / "tools"))
    import xlsx2md  # noqa: E402
    xlsx2md.main()

    sections, seen = [], set()
    for pattern, title in ORDER:
        group = []
        for p in files_for(pattern):
            if p in seen:
                continue
            seen.add(p)
            rel = p.relative_to(ROOT).as_posix()
            if p.suffix == ".pdf":
                body = pdf_text(p)
                if not body:
                    continue
            else:
                body = p.read_text(encoding="utf-8")
            if p.suffix == ".pdf":
                body = f"```text\n{body}\n```\n"
            elif p.suffix in FENCE:
                body = f"```{FENCE[p.suffix]}\n{body.rstrip()}\n```\n"
            else:
                body = demote(body)
            group.append((rel, body))
        if group:
            sections.append((title, group))

    today = dt.date.today().isoformat()
    head = [
        "# Blockrophage course: companion file",
        "",
        f"Built {today} from commit {git_rev()} of the course repository. This single file",
        "contains the complete course material for the ETH Zürich block course",
        "\"Macrophage Biology: in vitro, in vivo, in silico\" (Spring Semester 2027).",
        "Repository: https://github.com/TizzuLab/blockrophage-course. It is meant to be given to a language model",
        "together with COMPANION_PROMPT.md.",
        "",
        "UNDER CONSTRUCTION: first run spring 2027, built in the open; protocol values are",
        "unverified and the protocols must not be used in the lab yet.",
        "",
        "Reading order and conventions are in the first section (llms.txt). Each document",
        "starts with a line `<!-- file: path -->` naming its path in the repository, so",
        "an answer can cite the file. Values marked [TODO] are unconfirmed.",
        "",
        "## Table of contents",
        "",
    ]
    for title, group in sections:
        head.append(f"- {title}")
        for rel, _ in group:
            head.append(f"  - `{rel}`")
    head.append("")

    body = []
    for title, group in sections:
        body += [f"# {title}", ""]
        for rel, text in group:
            body += [f"<!-- file: {rel} -->", "", text.rstrip(), "", "---", ""]

    text = "\n".join(head + body)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    n = est_tokens(text)
    print(f"wrote {OUT} ({len(text):,} chars, ~{n:,} tokens, {len(seen)} files)")
    if n > args.max_tokens:
        print(f"ERROR: bundle exceeds {args.max_tokens:,} tokens", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
