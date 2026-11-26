#!/usr/bin/env python3
# Copyright 2026 The Internet of Games contributors
# SPDX-License-Identifier: Apache-2.0
"""Make the visual summary for a pull request, an issue or a long comment.

Turns a short brief into three files, written next to the brief:

    <name>-card.png    a summary card image to put at the top
    <name>-body.md     the description to post: card, three short lines with
                       links, a diagram GitHub draws, and the full text folded away
    <name>-digest.pdf  everything in one PDF, with working links

    python3 tools/visuals.py BRIEF.md [--out DIR] [--card-url URL] [--pdf URL]

The brief format and how to post are in skills/visual-summaries/SKILL.md.

Standard library only. Drawing needs Google Chrome or Chromium; set
IOG_BROWSER to the command to use a particular one. The PDF draws diagrams with
Mermaid, which is downloaded once into your cache and checked against a pinned
hash. Markdown in the PDF is rendered by GitHub's API through the gh CLI, so it
matches what readers see on GitHub; with --offline, or without gh, a simple
built-in renderer is used instead.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import posixpath
import re
import shlex
import shutil
import struct
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docs  # noqa: E402  (the docs checker, for front matter and the secrets scan)

ROOT = docs.ROOT
DEFAULT_REPO = "internet-of-games/internet-of-games"

CARD_WIDTH, CARD_HEIGHT, CARD_SCALE = 1200, 630, 2
MAX_IMAGE_BYTES = 10 * 1024 * 1024   # GitHub's limit for an attached image
MAX_FILE_BYTES = 25 * 1024 * 1024    # GitHub's limit for other attached files, such as PDFs
TITLE_LIMIT, POINT_LIMIT, LABEL_LIMIT, FACT_LIMIT, MAX_FACTS = 80, 140, 12, 24, 4
ROLES = {"facts", "diagram", "details", "footer"}

MERMAID_VERSION = "12.3.0"
MERMAID_URL = f"https://cdn.jsdelivr.net/npm/mermaid@{MERMAID_VERSION}/dist/mermaid.min.js"
# Checked against the npm registry's integrity hash for the package and jsDelivr's file hash.
MERMAID_SHA256 = "336df803d87a38b70a01e736e666c8f7601d2ce42f5e47c8fafe5d721074b9a3"

BROWSERS = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome",
            "microsoft-edge", "msedge"]
BROWSER_PATHS = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                 "/Applications/Chromium.app/Contents/MacOS/Chromium",
                 r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                 r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]
FLATPAKS = ["com.google.Chrome", "org.chromium.Chromium"]

FONTS = '"Inter", "Segoe UI", "Noto Sans", "Helvetica Neue", Arial, sans-serif'
MONO = 'ui-monospace, "SFMono-Regular", "Noto Sans Mono", "DejaVu Sans Mono", Menlo, Consolas, monospace'

# Status pill colors (background, text), chosen by the first matching word.
STATUS_STYLES = [
    (("block", "reject", "fail", "broken"), ("#fde2e1", "#9b1c1c")),
    (("done", "merged", "accepted", "complete", "promoted", "fixed", "closed"), ("#dcf5e3", "#17612f")),
    (("review", "ready"), ("#e3e6ff", "#3730a3")),
    (("decision", "decide", "needs", "waiting", "input", "question"), ("#fdf0c8", "#8a4b0b")),
    (("draft", "progress", "wip", "exploring"), ("#e5e9f0", "#3b4556")),
]
DEFAULT_STATUS_STYLE = ("#e3e6ff", "#3730a3")

FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})\s*([^`\s]*)")
MD_LINK = re.compile(r"(!?)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(\s*<?([^)\s>]+)>?((?:\s+\"[^\"]*\")?\s*)\)")
LINK_DEFINITION = re.compile(r"^( {0,3}\[[^\]]+\]:\s*)(\S+)")
CODE_SPAN = re.compile(r"(`+)(.+?)\1")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
PLACEHOLDER = "IOGMERMAIDBLOCK"


class BriefError(ValueError):
    """The brief can't be turned into a visual summary."""


@dataclass
class Brief:
    meta: dict
    points: list = field(default_factory=list)   # [(label, markdown)], exactly three
    facts: list = field(default_factory=list)
    diagram: str | None = None                    # Mermaid source, without the fence
    details: str = ""
    footer: str = ""

    @property
    def title(self) -> str:
        return self.meta["title"]


# ---------------------------------------------------------------- reading the brief

def fence_end(line: str, marker: str) -> bool:
    stripped = line.strip()
    return stripped.startswith(marker[0] * len(marker)) and set(stripped) == {marker[0]}


def split_sections(body: str) -> list[tuple[str, str]]:
    """Split the brief at its level-2 headings, ignoring headings inside code
    blocks. Everything after `## Details`, up to `## Footer`, is one section, so
    the details can use level-2 headings of their own."""
    sections: list[tuple[str, list[str]]] = []
    before: list[str] = []
    marker = None
    for line in body.splitlines():
        current = sections[-1][1] if sections else before
        if marker:
            current.append(line)
            if fence_end(line, marker):
                marker = None
            continue
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            current.append(line)
            continue
        heading = re.match(r"^##\s+(.+?)\s*#*\s*$", line)
        in_details = bool(sections) and sections[-1][0].lower() == "details"
        if heading and not (in_details and heading.group(1).strip().lower() != "footer"):
            sections.append((heading.group(1).strip(), []))
            continue
        current.append(line)
    if "".join(before).strip():
        raise BriefError("put everything after the front matter under a '## ' heading")
    return [(name, "\n".join(lines).strip("\n")) for name, lines in sections]


def list_items(text: str, section: str) -> list[str]:
    items = []
    for line in text.splitlines():
        if not line.strip():
            continue
        match = re.match(r"^\s*[-*+]\s+(.*\S)", line)
        if not match:
            raise BriefError(f"'## {section}' should be a bulleted list")
        items.append(match.group(1))
    return items


def mermaid_source(text: str) -> str:
    """Return the one Mermaid block in the diagram section, without its fence."""
    blocks, outside, marker, current = [], [], None, None
    for line in text.splitlines():
        if marker:
            if fence_end(line, marker):
                blocks.append("\n".join(current))
                marker = None
            else:
                current.append(line)
            continue
        fence = FENCE.match(line)
        if fence:
            if fence.group(2).lower() != "mermaid":
                raise BriefError("'## Diagram' must hold a ```mermaid code block")
            marker, current = fence.group(1), []
        elif line.strip():
            outside.append(line)
    if marker:
        raise BriefError("the Mermaid block in '## Diagram' isn't closed")
    if len(blocks) != 1 or outside:
        raise BriefError("'## Diagram' must hold exactly one ```mermaid code block and nothing else")
    if not blocks[0].strip():
        raise BriefError("the Mermaid block in '## Diagram' is empty")
    return blocks[0]


def parse_meta(block: str) -> dict:
    """`key: value` lines. Unlike problem docs, a `#` here is text, as in "Pull request #3"."""
    meta = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, colon, value = line.partition(":")
        if not colon:
            raise BriefError(f"can't read the front matter line {line!r}")
        meta[key.strip().lower()] = docs.parse_scalar(value)
    return meta


def parse_brief(text: str) -> Brief:
    block, body = docs.split_front_matter(text)
    if block is None:
        raise BriefError("the brief needs front matter between '---' lines, with at least a title")
    meta = parse_meta(block)
    if not meta.get("title"):
        raise BriefError("the front matter needs a title")
    brief = Brief(meta=meta)
    for name, content in split_sections(body):
        role = name.lower()
        if role == "facts":
            brief.facts = list_items(content, name)
        elif role == "diagram":
            brief.diagram = mermaid_source(content)
        elif role == "details":
            brief.details = content.strip()
        elif role == "footer":
            brief.footer = content.strip()
        else:
            point = " ".join(content.split())
            if not point:
                raise BriefError(f"'## {name}' is empty")
            brief.points.append((name.rstrip(":").strip(), point))
    if len(brief.points) != 3:
        raise BriefError(f"write exactly three short points (such as What, Why and Ask); found {len(brief.points)}")
    return brief


def plain(markdown: str) -> str:
    """Markdown inline text as plain text, for the card."""
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", markdown)
    text = MD_LINK.sub(lambda m: m.group(2), text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"(\*\*|__)(.+?)\1", r"\2", text)
    text = re.sub(r"(?<![\w*])([*_])(?!\s)(.+?)(?<!\s)\1(?![\w*])", r"\2", text)
    text = re.sub(r"~~(.+?)~~", r"\1", text)
    text = CODE_SPAN.sub(lambda m: m.group(2).strip(), text)
    return " ".join(html.unescape(text).split())


def check_lengths(brief: Brief) -> list[str]:
    problems = []
    if len(plain(brief.title)) > TITLE_LIMIT:
        problems.append(f"the title is longer than {TITLE_LIMIT} characters")
    for label, point in brief.points:
        if len(label) > LABEL_LIMIT:
            problems.append(f"the label '{label}' is longer than {LABEL_LIMIT} characters")
        if len(plain(point)) > POINT_LIMIT:
            problems.append(f"the '{label}' point is longer than {POINT_LIMIT} characters without its links")
    if len(brief.facts) > MAX_FACTS:
        problems.append(f"the card shows at most {MAX_FACTS} facts")
    for fact in brief.facts:
        if len(plain(fact)) > FACT_LIMIT:
            problems.append(f"the fact '{plain(fact)}' is longer than {FACT_LIMIT} characters")
    return problems


def unsafe_text(text: str) -> list[str]:
    """What the docs checker's secrets and personal-data scan finds in text."""
    found = []
    for number, line in enumerate(text.splitlines(), 1):
        for label, pattern in docs.SECRET_PATTERNS:
            for match in pattern.finditer(line):
                if label == "email address" and match.group(0).lower().endswith(docs.ALLOWED_EMAIL_DOMAINS):
                    continue
                found.append(f"line {number}: possible {label}")
        if "file://" in line:
            found.append(f"line {number}: a link to a local file")
    return found


# ---------------------------------------------------------------- links

def absolute_target(target: str, base: str, image: bool) -> str:
    if target.startswith("#") or SCHEME.match(target) or target.startswith("//"):
        return target
    path, hash_mark, anchor = target.partition("#")
    clean = posixpath.normpath(path.lstrip("/")) if path else ""
    if clean.startswith(".."):
        raise BriefError(f"the link '{target}' points outside the repository")
    clean = "" if clean == "." else clean
    if image:
        base = base.replace("/blob/", "/raw/", 1)
    return base + clean + (hash_mark + anchor if hash_mark else "")


def absolutize(markdown: str, repo: str, ref: str) -> str:
    """Turn links to repository files into links to the exact commit, which keep
    working after the branch is deleted. Code blocks and code spans are left alone."""
    base = f"https://github.com/{repo}/blob/{ref}/"
    out, marker = [], None
    for line in markdown.splitlines(keepends=True):
        if marker:
            out.append(line)
            if fence_end(line, marker):
                marker = None
            continue
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            out.append(line)
            continue
        definition = LINK_DEFINITION.match(line)
        if definition:
            target = absolute_target(definition.group(2), base, image=False)
            out.append(definition.group(1) + target + line[definition.end():])
            continue
        spans = [m.span() for m in CODE_SPAN.finditer(line)]

        def rewrite(m):
            if any(start <= m.start() < end for start, end in spans):
                return m.group(0)   # a link inside a code span is just text
            target = absolute_target(m.group(3), base, image=bool(m.group(1)))
            return f"{m.group(1)}[{m.group(2)}]({target}{m.group(4)})"

        out.append(MD_LINK.sub(rewrite, line))
    return "".join(out)


# ---------------------------------------------------------------- the description

def alt_text(brief: Brief) -> str:
    text = brief.meta.get("alt")
    if not text:
        kind = plain(brief.meta.get("kind") or "")
        status = plain(brief.meta.get("status") or "")
        text = f"Summary card. {kind + ': ' if kind else ''}{plain(brief.title)}."
        if status:
            text += f" Status: {status}."
        if brief.facts:
            text += " " + ", ".join(plain(f) for f in brief.facts) + "."
        text += " The same points are written out below."
    return " ".join(text.replace("[", "(").replace("]", ")").split())


def body_markdown(brief: Brief, card_ref: str, pdf_url: str | None = None) -> str:
    lines = [f"![{alt_text(brief)}]({card_ref})", ""]
    for label, point in brief.points:
        lines += [f"**{label}:** {point}", ""]
    if pdf_url:
        lines += [f"📄 [Read everything as one PDF, with working links]({pdf_url})", ""]
    if brief.diagram:
        lines += ["```mermaid", brief.diagram.rstrip("\n"), "```", ""]
    if brief.details:
        lines += ["<details>", "<summary><b>Full details</b></summary>", "", brief.details, "", "</details>", ""]
    if brief.footer:
        lines += [brief.footer, ""]
    return "\n".join(lines).rstrip("\n") + "\n"


# ---------------------------------------------------------------- the card

def status_style(status: str) -> tuple[str, str]:
    words = status.lower()
    for keys, style in STATUS_STYLES:
        if any(key in words for key in keys):
            return style
    return DEFAULT_STATUS_STYLE


def long_date(day: dt.date) -> str:
    return f"{day.day} {day:%B %Y}"


KEEP_TOGETHER = re.compile(r"\b(?:Phase \d+|RFC \d+|[A-Z]{1,4}-\d{2,}(?:-Q\d+)?)\b|#\d+\b")


def card_text(text: str) -> str:
    """Escaped card text, with IDs such as P-0013 and phrases such as Phase 1 kept on one line."""
    return KEEP_TOGETHER.sub(lambda m: f'<span class="nb">{m.group(0)}</span>', html.escape(text))


def card_inline(markdown: str) -> str:
    """Card HTML for a line of Markdown: plain text, except that code keeps its code style."""
    codes: list[str] = []

    def keep(match):
        codes.append(match.group(2).strip())
        return f"\x00{len(codes) - 1}\x00"

    text = card_text(plain(CODE_SPAN.sub(keep, markdown)))
    return re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{html.escape(codes[int(m[1])])}</code>", text)


def card_html(brief: Brief, repo: str, today: dt.date) -> str:
    e = html.escape
    status = plain(brief.meta.get("status") or "")
    background, ink = status_style(status)
    status_html = f'<div class="status">{e(status)}</div>' if status else ""
    points = "".join(f'<div class="label">{e(label)}</div><div class="text">{card_inline(point)}</div>'
                     for label, point in brief.points)
    facts = "".join(f'<span class="fact">{e(plain(fact))}</span>' for fact in brief.facts)
    where = re.sub(r"^https?://", "", brief.meta.get("url") or f"github.com/{repo}")
    when = brief.meta.get("date") or long_date(today)
    brand = brief.meta.get("brand") or "Internet of Games"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'">
<title>Summary card</title>
<style>
html, body {{ margin: 0; background: transparent; }}
body {{ width: {CARD_WIDTH}px; height: {CARD_HEIGHT}px; }}
.card {{ box-sizing: border-box; position: relative; width: {CARD_WIDTH}px; height: {CARD_HEIGHT}px;
  overflow: hidden; display: flex; flex-direction: column; padding: 44px 64px 36px 78px;
  background: #ffffff; border: 2px solid #d5dbe5; border-radius: 28px; font-family: {FONTS}; color: #14161b; }}
.card::before {{ content: ""; position: absolute; top: 0; bottom: 0; left: 0; width: 14px;
  background: linear-gradient(180deg, #4f46e5, #0d9488); }}
.top {{ display: flex; align-items: center; justify-content: space-between; gap: 24px; min-height: 42px; }}
.kind {{ font-size: 19px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #545d6b;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.status {{ flex: none; font-size: 19px; font-weight: 700; padding: 8px 18px; border-radius: 999px;
  background: {background}; color: {ink}; }}
h1 {{ margin: 18px 0 24px; font-size: 50px; line-height: 1.12; font-weight: 800; letter-spacing: -0.01em;
  display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 2; overflow: hidden; }}
.points {{ display: grid; grid-template-columns: max-content 1fr; column-gap: 24px; row-gap: 14px; align-items: baseline; }}
.label {{ font-size: 17px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: #4338ca; }}
.text {{ font-size: 25px; line-height: 1.32; display: -webkit-box; -webkit-box-orient: vertical;
  -webkit-line-clamp: 2; overflow: hidden; }}
.spacer {{ flex: 1; }}
.facts {{ display: flex; flex-wrap: wrap; gap: 12px; padding-top: 16px; }}
.fact {{ font-size: 19px; font-weight: 600; padding: 7px 14px; border-radius: 10px; background: #f2f4f8;
  border: 1px solid #dde2ea; }}
.foot {{ display: flex; justify-content: space-between; gap: 24px; margin-top: 18px; padding-top: 14px;
  border-top: 1px solid #e3e7ee; font-size: 17px; color: #545d6b; white-space: nowrap; }}
.brand {{ font-weight: 700; color: #14161b; }}
.where {{ overflow: hidden; text-overflow: ellipsis; }}
.nb {{ white-space: nowrap; }}
code {{ font-family: {MONO}; font-size: 0.86em; padding: 0 0.25em; border-radius: 6px; background: #f2f4f8;
  border: 1px solid #dde2ea; white-space: nowrap; }}
</style></head>
<body><div class="card">
<div class="top"><div class="kind">{e(plain(brief.meta.get("kind") or ""))}</div>{status_html}</div>
<h1>{card_inline(brief.title)}</h1>
<div class="points">{points}</div>
<div class="spacer"></div>
{f'<div class="facts">{facts}</div>' if facts else ""}
<div class="foot"><span class="brand">{e(brand)}</span><span class="where">{e(where)} · {e(str(when))}</span></div>
</div></body></html>
"""


# ---------------------------------------------------------------- Markdown for the PDF

def take_mermaid(markdown: str) -> tuple[str, list[str]]:
    """Swap Mermaid blocks for placeholders, so they can be drawn in the PDF."""
    out, blocks, marker, current = [], [], None, None
    for line in markdown.splitlines():
        if marker:
            if fence_end(line, marker):
                out += ["", f"{PLACEHOLDER}{len(blocks)}", ""]
                blocks.append("\n".join(current))
                marker = None
            else:
                current.append(line)
            continue
        fence = FENCE.match(line)
        if fence and fence.group(2).lower() == "mermaid":
            marker, current = fence.group(1), []
            continue
        out.append(line)
    if marker:
        out.append("```")
        out += current
        out.append("```")
    return "\n".join(out), blocks


def github_markdown(markdown: str, repo: str) -> str | None:
    """Render Markdown with GitHub's own renderer, through the gh CLI."""
    if not shutil.which("gh"):
        return None
    payload = json.dumps({"text": markdown, "mode": "gfm", "context": repo})
    try:
        result = subprocess.run(["gh", "api", "markdown", "--input", "-"], input=payload,
                                capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return result.stdout if result.returncode == 0 else None


def inline_html(text: str) -> str:
    codes: list[str] = []

    def keep(match):
        codes.append(f"<code>{html.escape(match.group(2).strip())}</code>")
        return f"\x00{len(codes) - 1}\x00"

    def href(url: str) -> str:
        return url.replace('"', "%22")

    text = CODE_SPAN.sub(keep, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", lambda m: f'<a href="{href(m[2])}">[image: {m[1]}]</a>', text)
    text = MD_LINK.sub(lambda m: f'<a href="{href(m[3])}">{m[2]}</a>', text)
    text = re.sub(r'(?<!["=>])\b(https?://[^\s<]*[^\s<.,;:!?)\]])', r'<a href="\1">\1</a>', text)
    text = re.sub(r"(\*\*|__)(.+?)\1", r"<strong>\2</strong>", text)
    text = re.sub(r"(?<![\w*])([*_])(?!\s)(.+?)(?<!\s)\1(?![\w*])", r"<em>\2</em>", text)
    text = re.sub(r"~~(.+?)~~", r"<del>\1</del>", text)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m[1])], text)


def table_cells(row: str) -> list[str]:
    return [cell.strip() for cell in row.strip().strip("|").split("|")]


def simple_markdown(markdown: str) -> str:
    """A small Markdown renderer, used when GitHub's renderer isn't available."""
    out: list[str] = []
    paragraph: list[str] = []
    items: list[str] = []
    list_tag = None
    lines = markdown.splitlines()

    def flush():
        nonlocal list_tag
        if paragraph:
            out.append(f"<p>{inline_html(' '.join(paragraph))}</p>")
            paragraph.clear()
        if items:
            out.append(f"<{list_tag}>" + "".join(f"<li>{item}</li>" for item in items) + f"</{list_tag}>")
            items.clear()
            list_tag = None

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        fence = FENCE.match(line)
        if fence:
            flush()
            code = []
            i += 1
            while i < len(lines) and not fence_end(lines[i], fence.group(1)):
                code.append(lines[i])
                i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(code))}</code></pre>")
            i += 1
            continue
        if not stripped:
            flush()
        elif re.fullmatch(r"#{1,6}\s+.*", stripped):
            flush()
            level = len(stripped) - len(stripped.lstrip("#"))
            out.append(f"<h{level}>{inline_html(stripped[level:].strip().rstrip('#').strip())}</h{level}>")
        elif stripped.startswith("|") and i + 1 < len(lines) and re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?", lines[i + 1].strip()):
            flush()
            head = "".join(f"<th>{inline_html(cell)}</th>" for cell in table_cells(stripped))
            rows = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append("<tr>" + "".join(f"<td>{inline_html(c)}</td>" for c in table_cells(lines[i])) + "</tr>")
                i += 1
            out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{''.join(rows)}</tbody></table>")
            continue
        elif stripped in ("<details>", "<details open>"):
            flush()
            out.append("<details open>")
        elif stripped == "</details>":
            flush()
            out.append("</details>")
        elif re.fullmatch(r"<summary>(.*)</summary>", stripped):
            flush()
            summary = re.fullmatch(r"<summary>(.*)</summary>", stripped).group(1)
            out.append(f"<summary>{inline_html(re.sub(r'</?b>', '**', summary))}</summary>")
        elif re.match(r"^([-*+]|\d+[.)])\s+", stripped) and not paragraph:
            tag = "ol" if stripped[0].isdigit() else "ul"
            if list_tag and tag != list_tag:
                flush()
            list_tag = tag
            item = re.sub(r"^([-*+]|\d+[.)])\s+", "", stripped)
            task = re.match(r"^\[([ xX])\]\s+(.*)", item)
            if task:
                item = ("☑ " if task.group(1) != " " else "☐ ") + task.group(2)
            items.append(inline_html(item))
        elif items and line.startswith((" ", "\t")):
            items[-1] += " " + inline_html(stripped)
        elif stripped.startswith(">"):
            flush()
            out.append(f"<blockquote><p>{inline_html(stripped.lstrip('>').strip())}</p></blockquote>")
        else:
            if items:
                flush()
            paragraph.append(stripped)
        i += 1
    flush()
    return "\n".join(out)


def finish_html(fragment: str, blocks: list[str]) -> str:
    """Open folded sections, draw Mermaid blocks, and turn remote images into links,
    so the PDF shows everything and fetches nothing."""
    fragment = re.sub(r"<details(?![^>]*\bopen\b)", "<details open", fragment)
    for number, source in enumerate(blocks):
        block = f'<pre class="mermaid">{html.escape(source)}</pre>'
        fragment = re.sub(rf"<p[^>]*>\s*{PLACEHOLDER}{number}\s*</p>", lambda _m: block, fragment)

    def image_link(match):
        attributes = dict(re.findall(r'([\w-]+)="([^"]*)"', match.group(0)))
        source = attributes.get("data-canonical-src") or attributes.get("src", "")
        label = attributes.get("alt") or "image"
        return f'<a href="{source}">[image: {label}]</a>' if source.startswith("http") else ""

    fragment = re.sub(r"<img\b[^>]*>", image_link, fragment)
    return re.sub(r'href="/(?!/)', 'href="https://github.com/', fragment)


def render_markdown(markdown: str, repo: str, offline: bool) -> str:
    text, blocks = take_mermaid(markdown)
    rendered = None if offline else github_markdown(text, repo)
    return finish_html(rendered if rendered is not None else simple_markdown(text), blocks)


# ---------------------------------------------------------------- the PDF

DIGEST_CSS = f"""
@page {{ size: Letter; margin: 15mm 16mm 17mm;
  @bottom-right {{ content: "Page " counter(page) " of " counter(pages); font: 8pt {FONTS}; color: #6b7280; }} }}
:root {{ --ink: #1f2328; --muted: #59636e; --line: #d1d9e0; --wash: #f6f8fa; --link: #0b5cad; }}
html {{ background: #ffffff; }}
body {{ margin: 0; font: 10.5pt/1.55 {FONTS}; color: var(--ink); }}
img.card {{ display: block; width: 100%; margin: 0 0 12pt; }}
.points p {{ margin: 0 0 5pt; font-size: 11.5pt; }}
.points strong:first-child {{ color: #3730a3; }}
.online {{ margin: 8pt 0 0; color: var(--muted); font-size: 9pt; }}
h2.section {{ font-size: 13pt; margin: 18pt 0 8pt; padding-bottom: 3pt; border-bottom: 1px solid var(--line); break-after: avoid; }}
h1, h2, h3, h4 {{ line-height: 1.25; break-after: avoid; }}
.details h1 {{ font-size: 14pt; }} .details h2 {{ font-size: 12.5pt; }} .details h3 {{ font-size: 11pt; }}
a {{ color: var(--link); text-underline-offset: 2px; }}
table {{ border-collapse: collapse; margin: 8pt 0; font-size: 9.5pt; }}
th, td {{ border: 1px solid var(--line); padding: 4pt 6pt; vertical-align: top; text-align: left; }}
th {{ background: var(--wash); }}
tr {{ break-inside: avoid; }}
code {{ font: 9pt {MONO}; background: var(--wash); padding: 0.1em 0.3em; border-radius: 4px; }}
pre {{ background: var(--wash); padding: 8pt; border-radius: 6px; white-space: pre-wrap; overflow-wrap: anywhere; }}
pre code {{ background: none; padding: 0; }}
pre.mermaid {{ background: none; text-align: center; white-space: pre; }}
.diagram {{ break-inside: avoid; }}
svg {{ max-width: 100%; height: auto; }}
blockquote {{ margin: 0 0 8pt; padding: 0 10pt; color: var(--muted); border-left: 3pt solid var(--line); }}
details > summary {{ font-weight: 700; list-style: none; margin: 6pt 0; }}
details > summary::-webkit-details-marker {{ display: none; }}
ul.contains-task-list {{ list-style: none; padding-left: 1.1em; }}
footer {{ margin-top: 16pt; padding-top: 8pt; border-top: 1px solid var(--line); color: var(--muted); font-size: 9.5pt; }}
"""

MERMAID_INIT = ('mermaid.initialize({ startOnLoad: true, securityLevel: "strict", theme: "neutral", '
                f'fontFamily: {json.dumps(FONTS)} }});\n')


def digest_html(brief: Brief, parts: dict, card: Path, mermaid: Path | None, base: str) -> str:
    e = html.escape
    sections = [f'<img class="card" src="{card.as_uri()}" alt="{e(alt_text(brief))}">',
                f'<section class="points">{parts["points"]}</section>']
    if brief.meta.get("url"):
        url = brief.meta["url"]
        sections.append(f'<p class="online">Online: <a href="{e(url)}">{e(url)}</a></p>')
    if brief.diagram:
        drawing = (f'<pre class="mermaid">{e(brief.diagram)}</pre>' if mermaid else
                   f'<p class="online">Mermaid couldn\'t be loaded, so here is the diagram\'s source.</p>'
                   f'<pre>{e(brief.diagram)}</pre>')
        sections.append(f'<h2 class="section">Diagram</h2><div class="diagram">{drawing}</div>')
    if brief.details:
        sections.append(f'<h2 class="section">Details</h2><div class="details">{parts["details"]}</div>')
    if brief.footer:
        sections.append(f'<footer>{parts["footer"]}</footer>')
    scripts = ""
    if mermaid:
        scripts = (f'<script src="{mermaid.as_uri()}"></script>'
                   f'<script src="{mermaid.with_name("init.js").as_uri()}"></script>')
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; img-src file: data:; style-src 'unsafe-inline'; script-src file:; font-src file: data:">
<base href="{e(base)}">
<title>{e(plain(brief.title))}</title>
<style>{DIGEST_CSS}</style></head>
<body>
{chr(10).join(sections)}
{scripts}
</body></html>
"""


# ---------------------------------------------------------------- the browser

def find_browser() -> list[str] | None:
    override = os.environ.get("IOG_BROWSER")
    if override:
        return shlex.split(override)
    for name in BROWSERS:
        path = shutil.which(name)
        if path:
            return [path]
    for path in BROWSER_PATHS:
        if Path(path).exists():
            return [path]
    if shutil.which("flatpak"):
        for app in FLATPAKS:
            if subprocess.run(["flatpak", "info", app], capture_output=True).returncode == 0:
                return ["flatpak", "run", app]
    return None


def browser_command(browser: list[str], workdir: Path, args: list[str]) -> list[str]:
    """The full command. Flatpak browsers get the work folder and no network."""
    common = ["--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
              "--disable-extensions", "--disable-background-networking", "--disable-component-update",
              "--disable-sync", "--disable-default-apps", "--no-pings", "--mute-audio", "--hide-scrollbars",
              f"--user-data-dir={workdir / 'profile'}", "--host-resolver-rules=MAP * ~NOTFOUND"]
    if browser[:2] == ["flatpak", "run"]:
        return ["flatpak", "run", f"--filesystem={workdir}", "--unshare=network", *browser[2:], *common, *args]
    return [*browser, *common, *args]


def run_browser(browser: list[str], workdir: Path, args: list[str], output: Path) -> None:
    command = browser_command(browser, workdir, args)
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        raise SystemExit("error: the browser took longer than 3 minutes") from None
    if not output.exists():
        tail = "\n".join((result.stdout + result.stderr).splitlines()[-8:])
        raise SystemExit(f"error: the browser didn't write {output.name}:\n{tail}")


def cache_dir() -> Path:
    base = Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache")
    return base / "iog-visuals"


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def mermaid_script(cache: Path, offline: bool) -> Path | None:
    """The pinned Mermaid build, downloaded once and checked against its hash."""
    local = os.environ.get("IOG_MERMAID_JS")
    path = Path(local) if local else cache / f"mermaid-{MERMAID_VERSION}.min.js"
    if path.exists():
        if sha256_of(path) == MERMAID_SHA256:
            return path
        print(f"warning: {path} doesn't match the pinned Mermaid hash, so it isn't used", file=sys.stderr)
        if local:
            return None
    if offline or local:
        return None
    try:
        with urllib.request.urlopen(MERMAID_URL, timeout=60) as response:
            data = response.read()
    except (urllib.error.URLError, OSError) as error:
        print(f"warning: couldn't download Mermaid ({error}); the PDF shows the diagram's source", file=sys.stderr)
        return None
    if hashlib.sha256(data).hexdigest() != MERMAID_SHA256:
        print("warning: the downloaded Mermaid doesn't match the pinned hash, so it isn't used", file=sys.stderr)
        return None
    cache.mkdir(parents=True, exist_ok=True)
    partial = path.with_suffix(".part")
    partial.write_bytes(data)
    partial.replace(path)
    return path


def png_size(path: Path) -> tuple[int, int]:
    head = path.read_bytes()[:24]
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit(f"error: {path.name} isn't a PNG image")
    return struct.unpack(">II", head[16:24])


def pdf_links(data: bytes) -> list[str]:
    return [link.decode("latin-1") for link in re.findall(rb"/URI\s*\(((?:\\.|[^\\)])*)\)", data)]


def pdf_pages(data: bytes) -> int:
    return len(re.findall(rb"/Type\s*/Page(?![s\w])", data))


# ---------------------------------------------------------------- putting it together

def git_head() -> str | None:
    try:
        result = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True)
    except OSError:
        return None
    return result.stdout.strip() or None


def build(args) -> int:
    brief_path = Path(args.brief).resolve()
    try:
        text = brief_path.read_text(encoding="utf-8")
        brief = parse_brief(text)
    except (OSError, BriefError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    found = unsafe_text(text)
    if found:
        print("error: the brief may contain secrets or personal data, so nothing was made:\n  "
              + "\n  ".join(found), file=sys.stderr)
        return 1
    problems = check_lengths(brief)
    if problems:
        print("error: the card has room for less text:\n  " + "\n  ".join(problems), file=sys.stderr)
        return 1
    repo = brief.meta.get("repo") or DEFAULT_REPO
    ref = brief.meta.get("ref") or git_head() or "main"
    try:
        for i, (label, point) in enumerate(brief.points):
            brief.points[i] = (label, absolutize(point, repo, ref))
        brief.details = absolutize(brief.details, repo, ref)
        brief.footer = absolutize(brief.footer, repo, ref)
    except BriefError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    stem = brief_path.stem
    out = Path(args.out).resolve() if args.out else brief_path.parent
    out.mkdir(parents=True, exist_ok=True)
    card_name, body_name, pdf_name = f"{stem}-card.png", f"{stem}-body.md", f"{stem}-digest.pdf"
    body = body_markdown(brief, args.card_url or f"./{card_name}", args.pdf)
    found = unsafe_text(body)
    if found:
        print("error: the description may contain secrets or personal data, so nothing was written:\n  "
              + "\n  ".join(found), file=sys.stderr)
        return 1
    (out / body_name).write_text(body, encoding="utf-8")
    written = [("body", out / body_name, "")]

    browser = find_browser()
    if not browser:
        print("error: no Chrome or Chromium found; install one or set IOG_BROWSER", file=sys.stderr)
        return 1
    cache = cache_dir()
    (cache / "work").mkdir(parents=True, exist_ok=True)
    workdir = Path(tempfile.mkdtemp(prefix="run-", dir=cache / "work"))
    try:
        (workdir / "card.html").write_text(card_html(brief, repo, dt.date.today()), encoding="utf-8")
        run_browser(browser, workdir, [f"--screenshot={workdir / 'card.png'}",
                                       f"--window-size={CARD_WIDTH},{CARD_HEIGHT}",
                                       f"--force-device-scale-factor={CARD_SCALE}",
                                       "--default-background-color=00000000", "--virtual-time-budget=3000",
                                       (workdir / "card.html").as_uri()], workdir / "card.png")
        width, height = png_size(workdir / "card.png")
        size = (workdir / "card.png").stat().st_size
        if size > MAX_IMAGE_BYTES:
            print(f"error: the card is {size} bytes, over GitHub's image limit", file=sys.stderr)
            return 1
        shutil.copyfile(workdir / "card.png", out / card_name)
        written.append(("card", out / card_name, f"{width}×{height}, {size // 1024} KB"))

        if not args.no_pdf:
            mermaid = None
            if brief.diagram or "```mermaid" in brief.details:
                source = mermaid_script(cache, args.offline)
                if source:
                    mermaid = workdir / "mermaid.min.js"
                    shutil.copyfile(source, mermaid)
                    (workdir / "init.js").write_text(MERMAID_INIT, encoding="utf-8")
            points = "\n\n".join(f"**{label}:** {point}" for label, point in brief.points)
            parts = {"points": render_markdown(points, repo, args.offline),
                     "details": render_markdown(brief.details, repo, args.offline) if brief.details else "",
                     "footer": render_markdown(brief.footer, repo, args.offline) if brief.footer else ""}
            base = f"https://github.com/{repo}/blob/{ref}/"
            page = workdir / "digest.html"
            page.write_text(digest_html(brief, parts, workdir / "card.png", mermaid, base), encoding="utf-8")
            run_browser(browser, workdir, [f"--print-to-pdf={workdir / 'digest.pdf'}", "--no-pdf-header-footer",
                                           "--virtual-time-budget=20000", "--run-all-compositor-stages-before-draw",
                                           page.as_uri()], workdir / "digest.pdf")
            data = (workdir / "digest.pdf").read_bytes()
            links = pdf_links(data)
            bad = [link for link in links if not link.startswith(("https://", "http://", "mailto:"))]
            if bad or len(data) > MAX_FILE_BYTES:
                print(f"error: the PDF has {len(bad)} link(s) to local files or is too large; not written",
                      file=sys.stderr)
                return 1
            shutil.copyfile(workdir / "digest.pdf", out / pdf_name)
            note = "" if mermaid or not brief.diagram else ", diagram shown as source"
            written.append(("digest", out / pdf_name,
                            f"{pdf_pages(data)} pages, {len(data) // 1024} KB, {len(set(links))} links{note}"))
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    print("Wrote:")
    for label, path, detail in written:
        print(f"  {label:7}{path}" + (f"  ({detail})" if detail else ""))
    if ROOT in out.parents or out == ROOT:
        print("\nThese files are inside the repository. Don't commit them (AGENTS.md, rule 12).")
    attach = "" if args.card_url else f" --attach {shlex.quote(str(out / card_name))}"
    print(f"""
Look at the card{"" if args.no_pdf else " and the PDF"} first. Posting needs your human's go-ahead (AGENTS.md, rule 18):
  gh pr edit NUMBER --body-file {shlex.quote(str(out / body_name))}{attach}
  gh issue create --title TITLE --body-file {shlex.quote(str(out / body_name))}{attach}""")
    if not args.no_pdf and not args.pdf:
        print(f"""gh can't upload PDFs, so ask your human to drag {pdf_name} into a comment. Then rerun with
--card-url and --pdf set to the two uploaded links, and post the body again without --attach.""")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("brief", help="the brief: front matter, three short points, and optional facts, "
                                      "diagram, details and footer sections")
    parser.add_argument("--out", help="folder for the files (default: next to the brief)")
    parser.add_argument("--card-url", help="use a card already uploaded to GitHub instead of attaching a new one")
    parser.add_argument("--pdf", help="link to the PDF digest once it's uploaded")
    parser.add_argument("--no-pdf", action="store_true", help="skip the PDF")
    parser.add_argument("--offline", action="store_true",
                        help="don't use GitHub's renderer or download Mermaid (uses a cached copy if there is one)")
    return build(parser.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
