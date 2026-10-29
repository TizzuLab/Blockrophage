#!/usr/bin/env python3
"""Build the single-file LLM companion: companion/blockcourse-companion.md.

Concatenates every Markdown document of the repository in reading order (the
schedule is Section 4 of README.md) with a table of contents and a short
machine-readable header. Code files are included verbatim
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
    ("README.md", "Course script, including the schedule"),
    ("tools/schedule/schedule_text.md", "Schedule, text version of the drawings"),
    ("protocols/README.md", "Protocol index"),
    ("protocols/C*.md", "Core protocols"),
    ("protocols/X*.md", "Extension protocols"),
    ("protocols/S*.md", "Staff protocols"),
    ("notebooks/README.md", "Notebooks: the lab notebook rules"),
    ("background/README.md", "Background reading"),
    ("background/reading_list.md", "Reading list"),
    ("slides/README.md", "Slides index"),
    ("slides/*.pdf", "Slides: extracted text"),
    ("safety/README.md", "Safety sheet"),
    ("poster/README.md", "Poster guide"),
    ("code/README.md", "Code overview"),
    ("code/**/*.R", "Code: R scripts"),
    ("code/**/*.py", "Code: Python scripts"),
    ("code/**/README.md", "Code: folder notes"),
]
SKIP_PARTS = {"example_data", "output", "renv", "__pycache__"}
# The core companion: what a session started from a link needs, a third of the size.
CORE_TITLES = {"Index (llms.txt)", "Course script, including the schedule",
               "Schedule, text version of the drawings", "Protocol index", "Core protocols",
               "Extension protocols", "Notebooks: the lab notebook rules", "Safety sheet",
               "Poster guide", "Code overview"}
CORE_OUT = ROOT / "companion" / "blockcourse-companion-core.md"
FENCE = {".R": "r", ".py": "python"}
PDF_MAX_CHARS = 60_000  # per deck, keeps the bundle inside common context windows


def git_rev():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                                       text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "uncommitted"


def companion_prompt():
    """The companion prompt, kept in companion/prompt.md inside its code fence."""
    text = (ROOT / "companion" / "prompt.md").read_text(encoding="utf-8")
    text = text.split("\n---\n", 1)[1] if "\n---\n" in text else text
    return "\n".join(ln for ln in text.strip().splitlines() if not ln.startswith("```")).strip()


BLOCK_BEGIN = "<!-- companion:begin -->"
BLOCK_END = "<!-- companion:end -->"
BLOCK_NOTE = "(On GitHub this spot holds the core companion itself, in a collapsible block with a copy button.)"


def strip_companion_block(text):
    """The README carries the core companion in a block; the companion must not contain itself."""
    a, b = text.find(BLOCK_BEGIN), text.find(BLOCK_END)
    if a < 0 or b < 0:
        return text
    return text[:a] + BLOCK_NOTE + text[b + len(BLOCK_END):]


def inject_companion_block(core_text):
    """Write the core companion into the README between the markers, as a copyable code block."""
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    a, b = text.find(BLOCK_BEGIN), text.find(BLOCK_END)
    if a < 0 or b < 0:
        return
    # The block sits inside a blockquote (a GitHub alert box), so every line is prefixed.
    quoted = "\n".join(("> " + ln) if ln else ">" for ln in core_text.rstrip().splitlines())
    block = BLOCK_BEGIN + "\n> ````text\n" + quoted + "\n> ````\n> " + BLOCK_END
    readme.write_text(text[:a] + block + text[b + len(BLOCK_END):], encoding="utf-8")


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
    ap.add_argument("--core", action="store_true", help="write the core companion (no background, slides, code)")
    args = ap.parse_args()

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
                if rel == "README.md":
                    body = strip_companion_block(body)
            if p.suffix == ".pdf":
                body = f"```text\n{body}\n```\n"
            elif p.suffix in FENCE:
                body = f"```{FENCE[p.suffix]}\n{body.rstrip()}\n```\n"
            else:
                body = demote(body)
            group.append((rel, body))
        if group and (not args.core or title in CORE_TITLES):
            sections.append((title, group))

    # No date and no commit hash in the header: the file is regenerated by CI and
    # compared on main, so its content must depend on the sources alone. The
    # version of this file is the git history of the file itself.
    head = [
        "# Blockrophage course: companion file",
        "",
        "Built from the course repository by tools/build_companion.py. This single file",
        "contains the complete course material for the ETH Zürich block course",
        "\"Macrophage Biology: in vitro, in vivo, in silico\" (Spring Semester 2027).",
        "Repository: https://github.com/TizzuLab/Blockrophage. It is meant to be given to a language model",
        "by pasting it into a new session; the instructions it then follows come next.",
        "",
        "UNDER CONSTRUCTION: first run spring 2027, built in the open; protocol values are",
        "unverified and the protocols must not be used in the lab yet.",
        "",
        "Reading order and conventions are in the first section (llms.txt). Each document",
        "starts with a line `<!-- file: path -->` naming its path in the repository, so",
        "an answer can cite the file. Values marked [TODO] are unconfirmed.",
        "",
        "## How to behave: the companion prompt",
        "",
        "The instructions below are companion/prompt.md. A student pasted this file to",
        "make you the course companion: follow them and open with the greeting.",
        "",
        companion_prompt(),
        "",
        *(["This is the core companion: the script, the schedule, the protocols, the notebook",
           "rules, the safety sheet and the poster guide. The full companion adds the",
           "background reading, the lecture text and the analysis code:",
           f"https://raw.githubusercontent.com/TizzuLab/Blockrophage/main/companion/blockcourse-companion.md . When a question needs that depth, tell the student to download the",
           "full file from the repository and attach it to the session."] if args.core else
          ["This is the full companion, including the background reading, the lecture text",
           "and the analysis code."]),
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
    out = CORE_OUT if args.core else OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    if args.core:
        inject_companion_block(text)
    n = est_tokens(text)
    print(f"wrote {out} ({len(text):,} chars, ~{n:,} tokens, {len(seen)} files)")
    if n > args.max_tokens:
        print(f"ERROR: bundle exceeds {args.max_tokens:,} tokens", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
