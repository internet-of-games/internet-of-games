#!/usr/bin/env python3
"""Checks and helpers for the Internet of Games documentation.

Standard library only. Run from anywhere inside the repository:

    python3 tools/docs.py check        validate the docs (CI runs this)
    python3 tools/docs.py next         next free problem and decision IDs
    python3 tools/docs.py work         unclaimed problems, in roadmap order
    python3 tools/docs.py questions    every open question, with its ID
    python3 tools/docs.py index        JSON map of problems and decisions
    python3 tools/docs.py external     check external links (needs network)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEM_DIR = ROOT / "problems"
DECISION_DIR = ROOT / "docs" / "decisions"
SPIKE_DIR = ROOT / "docs" / "spikes"
DOCS_DIR = ROOT / "docs"

SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"
PROBLEM_FILE = re.compile(rf"^(P-\d{{4}})-{SLUG}\.md$")
DECISION_FILE = re.compile(rf"^(ADR-\d{{4}})-{SLUG}\.md$")
SPIKE_FILE = re.compile(rf"^\d{{4}}-\d{{2}}-\d{{2}}-{SLUG}\.md$")
QUESTION_LINE = re.compile(r"^\s*[-*]\s+(?:~~)?\*\*(P-\d{4})-Q(\d+):\*\*(.*)$")
OPEN_QUESTION_LINE = re.compile(r"^\*\*OQ-(\d+):")
LAST_REVIEWED = re.compile(r"\*Last reviewed: (\d{4}-\d{2}-\d{2})")
LINK = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")

LAYERS = {"governance", "identity", "appearance", "history", "presence",
          "ownership", "world", "cross-cutting"}
PHASE_ORDER = ["0", "1", "2", "3", "4", "5", "research"]
PROBLEM_STATUSES = {"open", "exploring", "proposal", "solved-enough", "parked"}
DIFFICULTY_ORDER = ["low", "medium", "high", "research"]
DECISION_STATUSES = {"accepted", "superseded", "deprecated"}
PROBLEM_KEYS = ["id", "title", "layer", "phase", "status", "difficulty",
                "champion", "related", "last_reviewed"]
DECISION_KEYS = ["id", "title", "status", "date", "problems", "topics"]
DECISION_SECTIONS = ["## Context", "## Decision", "## Consequences",
                     "## Universality and safety"]
DOCS_WITHOUT_REVIEW_DATE = {"README.md", "glossary.md"}
STALE_AFTER_DAYS = 180
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv"}
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".py", ".txt", ".json", ".toml"}
TEXT_NAMES = {"Makefile", "CODEOWNERS", ".gitignore", "NOTICE"}

SECRET_PATTERNS = [
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}")),
    ("API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}")),
    ("email address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("home-directory path", re.compile(r"(?:/home/[a-z_][a-z0-9_-]*/|/Users/[A-Za-z0-9._-]+/|[A-Za-z]:\\Users\\)")),
]
ALLOWED_EMAIL_DOMAINS = ("example.com", "example.org", "example.net")


class Finding:
    """A problem found by a check. Errors fail the build; warnings don't."""

    def __init__(self, level: str, path: Path | None, line: int, message: str):
        self.level, self.path, self.line, self.message = level, path, line, message

    def __str__(self) -> str:
        where = rel(self.path) if self.path else "repo"
        if self.line:
            where += f":{self.line}"
        return f"{self.level.upper():7} {where}: {self.message}"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


# ---------------------------------------------------------------- parsing

def split_front_matter(text: str) -> tuple[str | None, str]:
    """Return (front matter block, body). The block is None if absent."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5:]


def strip_comment(value: str) -> str:
    """Drop a trailing ' # comment' that isn't inside quotes."""
    out, quote = [], None
    for i, ch in enumerate(value):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "'\"":
            quote = ch
        elif ch == "#" and (i == 0 or value[i - 1].isspace()):
            break
        out.append(ch)
    return "".join(out).rstrip()


def parse_scalar(value: str):
    value = value.strip()
    if value in ("", "null", "~"):
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1]
    return value


def parse_front_matter(block: str) -> dict:
    """Parse the small YAML subset our docs use: scalars and inline lists."""
    data: dict = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"cannot parse front matter line {line!r}")
        key, _, raw = line.partition(":")
        raw = strip_comment(raw).strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            data[key.strip()] = [parse_scalar(x) for x in inner.split(",")] if inner else []
        else:
            data[key.strip()] = parse_scalar(raw)
    return data


def slugify(heading: str) -> str:
    """GitHub-style heading anchor."""
    text = heading.replace("`", "")
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def prose_lines(text: str):
    """Yield (line number, line) for lines outside fenced code blocks."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if fence:
            if stripped.startswith(fence):
                fence = None
            continue
        if stripped.startswith("```") or stripped.startswith("~~~"):
            fence = stripped[:3]
            continue
        yield number, line


def strip_inline_code(line: str) -> str:
    """Remove `inline code` spans, so example links inside them aren't checked."""
    return re.sub(r"(`+)(?:(?!\1).)+\1", "", line)


def anchors_for(text: str) -> set[str]:
    seen: dict[str, int] = {}
    anchors = set()
    for _, line in prose_lines(text):
        match = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if match:
            slug = slugify(match.group(2))
            count = seen.get(slug, 0)
            seen[slug] = count + 1
            anchors.add(slug if count == 0 else f"{slug}-{count}")
    return anchors


def h1_of(body: str) -> str | None:
    for _, line in prose_lines(body):
        if line.startswith("# "):
            return line[2:].strip()
    return None


def walk_files(suffixes=None, names=None):
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS
                       and not os.path.islink(os.path.join(dirpath, d))]
        for name in sorted(filenames):
            path = Path(dirpath) / name
            if path.is_symlink():
                continue
            if (suffixes and path.suffix in suffixes) or (names and name in names):
                yield path


def markdown_files():
    return list(walk_files(suffixes={".md"}))


# ---------------------------------------------------------------- loading

def load_docs(directory: Path, pattern: re.Pattern, findings: list) -> dict:
    docs = {}
    if not directory.is_dir():
        return docs
    for path in sorted(directory.glob("*.md")):
        if path.name in ("README.md", "TEMPLATE.md"):
            continue
        match = pattern.match(path.name)
        if not match:
            findings.append(Finding("error", path, 0, "file name doesn't match the naming pattern"))
            continue
        text = path.read_text(encoding="utf-8")
        block, body = split_front_matter(text)
        if block is None:
            findings.append(Finding("error", path, 1, "missing front matter"))
            continue
        try:
            meta = parse_front_matter(block)
        except ValueError as exc:
            findings.append(Finding("error", path, 1, str(exc)))
            continue
        meta["_path"], meta["_body"], meta["_file_id"] = path, body, match.group(1)
        docs[match.group(1)] = meta
    return docs


def load_problems(findings: list) -> dict:
    return load_docs(PROBLEM_DIR, PROBLEM_FILE, findings)


def load_decisions(findings: list) -> dict:
    return load_docs(DECISION_DIR, DECISION_FILE, findings)


def questions_in(meta: dict) -> list[tuple[str, int, str, bool]]:
    """(question ID, line, text, answered) for each question in a problem doc."""
    found = []
    text = meta["_path"].read_text(encoding="utf-8")
    offset = text[: len(text) - len(meta["_body"])].count("\n")
    for number, line in prose_lines(meta["_body"]):
        match = QUESTION_LINE.match(line)
        if match:
            qid = f"{match.group(1)}-Q{match.group(2)}"
            answered = line.lstrip("-* ").startswith("~~")
            text = re.sub(r"\*\*|~~", "", match.group(3)).strip()
            found.append((qid, number + offset, text, answered))
    return found


# ---------------------------------------------------------------- checks

def check_links(findings: list) -> None:
    files = markdown_files()
    anchors = {path.resolve(): anchors_for(path.read_text(encoding="utf-8")) for path in files}
    for path in files:
        text = path.read_text(encoding="utf-8")
        for number, line in prose_lines(text):
            for target in LINK.findall(strip_inline_code(line)):
                if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                    continue  # http:, https:, mailto: and other schemes
                file_part, _, fragment = target.partition("#")
                resolved = (path.parent / file_part).resolve() if file_part else path.resolve()
                if not resolved.exists():
                    findings.append(Finding("error", path, number, f"broken link to {target}"))
                    continue
                if fragment and resolved.suffix == ".md" and fragment.lower() not in anchors.get(resolved, set()):
                    findings.append(Finding("error", path, number, f"missing heading anchor in {target}"))


def check_problems(problems: dict, findings: list, today: dt.date) -> None:
    for pid, meta in problems.items():
        path = meta["_path"]
        for key in PROBLEM_KEYS:
            if key not in meta:
                findings.append(Finding("error", path, 1, f"front matter is missing '{key}'"))
        if meta.get("id") != pid:
            findings.append(Finding("error", path, 1, f"id '{meta.get('id')}' doesn't match the file name ({pid})"))
        if meta.get("layer") not in LAYERS:
            findings.append(Finding("error", path, 1, f"unknown layer '{meta.get('layer')}'"))
        if str(meta.get("phase")) not in PHASE_ORDER:
            findings.append(Finding("error", path, 1, f"unknown phase '{meta.get('phase')}'"))
        if meta.get("status") not in PROBLEM_STATUSES:
            findings.append(Finding("error", path, 1, f"unknown status '{meta.get('status')}'"))
        if meta.get("difficulty") not in DIFFICULTY_ORDER:
            findings.append(Finding("error", path, 1, f"unknown difficulty '{meta.get('difficulty')}'"))
        expected_h1 = f"{pid}: {meta.get('title')}"
        if h1_of(meta["_body"]) != expected_h1:
            findings.append(Finding("error", path, 0, f"first heading should be '# {expected_h1}'"))
        check_review_date(path, meta.get("last_reviewed"), findings, today)
        related = meta.get("related") or []
        if not isinstance(related, list):
            findings.append(Finding("error", path, 1, "'related' must be a list like [P-0001, P-0002]"))
            continue
        for other in related:
            if other == pid:
                findings.append(Finding("error", path, 1, "a problem can't be related to itself"))
            elif other not in problems:
                findings.append(Finding("error", path, 1, f"related problem {other} doesn't exist"))
            elif pid not in (problems[other].get("related") or []):
                findings.append(Finding("error", path, 1,
                                        f"{other} is related here, but {other} doesn't list {pid} back"))
        seen = []
        for qid, number, _, _ in questions_in(meta):
            if not qid.startswith(pid + "-"):
                findings.append(Finding("error", path, number, f"question {qid} belongs to another problem"))
            if qid in seen:
                findings.append(Finding("error", path, number, f"duplicate question ID {qid}"))
            seen.append(qid)
        expected = [f"{pid}-Q{n}" for n in range(1, len(seen) + 1)]
        if seen and seen != expected:
            findings.append(Finding("error", path, 0, f"question IDs should run {expected[0]} to {expected[-1]} in order"))


def check_review_date(path: Path, value, findings: list, today: dt.date) -> None:
    try:
        reviewed = dt.date.fromisoformat(str(value))
    except ValueError:
        findings.append(Finding("error", path, 0, f"review date '{value}' isn't YYYY-MM-DD"))
        return
    if reviewed > today:
        findings.append(Finding("error", path, 0, f"review date {reviewed} is in the future"))
    elif (today - reviewed).days > STALE_AFTER_DAYS:
        findings.append(Finding("warning", path, 0,
                                f"last reviewed {reviewed}; facts older than {STALE_AFTER_DAYS} days need a recheck"))


def parse_index(path: Path, id_pattern: str, sectioned: bool) -> dict:
    """Read an index table: {id: {cells, target, phase, line}}."""
    rows: dict = {}
    if not path.exists():
        return rows
    phase = None
    row = re.compile(rf"^\|\s*\[({id_pattern})\]\(([^)]+)\)\s*\|(.*)\|\s*$")
    for number, line in prose_lines(path.read_text(encoding="utf-8")):
        heading = re.match(r"^##\s+(.*)", line)
        if heading:
            title = heading.group(1).strip().lower()
            match = re.match(r"phase (\d)", title)
            phase = match.group(1) if match else ("research" if title.startswith("research") else None)
            continue
        match = row.match(line)
        if match and (phase is not None or not sectioned):
            cells = [c.strip() for c in match.group(3).split("|")]
            rows.setdefault(match.group(1), []).append(
                {"target": match.group(2), "cells": cells, "phase": phase, "line": number})
    return rows


def check_problem_index(problems: dict, findings: list) -> None:
    index_path = PROBLEM_DIR / "README.md"
    rows = parse_index(index_path, r"P-\d{4}", sectioned=True)
    for pid, entries in rows.items():
        if len(entries) > 1:
            findings.append(Finding("error", index_path, entries[1]["line"], f"{pid} is listed more than once"))
        if pid not in problems:
            findings.append(Finding("error", index_path, entries[0]["line"], f"{pid} is listed but has no doc"))
    for pid, meta in problems.items():
        if pid not in rows:
            findings.append(Finding("error", index_path, 0, f"{pid} is missing from the index"))
            continue
        entry = rows[pid][0]
        if entry["target"] != meta["_path"].name:
            findings.append(Finding("error", index_path, entry["line"], f"{pid} links to {entry['target']}"))
        expected = [str(meta.get("title")), str(meta.get("layer")), str(meta.get("difficulty")), str(meta.get("status"))]
        if entry["cells"] != expected:
            findings.append(Finding("error", index_path, entry["line"],
                                    f"{pid} row should read: {' | '.join(expected)}"))
        if entry["phase"] != str(meta.get("phase")):
            findings.append(Finding("error", index_path, entry["line"],
                                    f"{pid} is under phase '{entry['phase']}' but its doc says '{meta.get('phase')}'"))


def check_decisions(decisions: dict, problems: dict, findings: list, today: dt.date) -> None:
    for did, meta in decisions.items():
        path = meta["_path"]
        for key in DECISION_KEYS:
            if key not in meta:
                findings.append(Finding("error", path, 1, f"front matter is missing '{key}'"))
        if meta.get("id") != did:
            findings.append(Finding("error", path, 1, f"id '{meta.get('id')}' doesn't match the file name ({did})"))
        status = meta.get("status")
        if status not in DECISION_STATUSES:
            findings.append(Finding("error", path, 1, f"unknown status '{status}'"))
        try:
            if dt.date.fromisoformat(str(meta.get("date"))) > today:
                findings.append(Finding("error", path, 1, "decision date is in the future"))
        except ValueError:
            findings.append(Finding("error", path, 1, f"date '{meta.get('date')}' isn't YYYY-MM-DD"))
        for pid in meta.get("problems") or []:
            if pid != "*" and pid not in problems:
                findings.append(Finding("error", path, 1, f"related problem {pid} doesn't exist"))
        if status == "superseded":
            newer = meta.get("superseded_by")
            if newer not in decisions:
                findings.append(Finding("error", path, 1, "superseded decisions need 'superseded_by' set to an existing ADR"))
            elif did not in (decisions[newer].get("supersedes") or []):
                findings.append(Finding("error", path, 1, f"{newer} doesn't list {did} under 'supersedes'"))
        for older in meta.get("supersedes") or []:
            if older not in decisions:
                findings.append(Finding("error", path, 1, f"superseded decision {older} doesn't exist"))
            elif decisions[older].get("status") != "superseded":
                findings.append(Finding("error", decisions[older]["_path"], 1,
                                        f"{did} supersedes this decision, so its status should be 'superseded'"))
        expected_h1 = f"{did}: {meta.get('title')}"
        if h1_of(meta["_body"]) != expected_h1:
            findings.append(Finding("error", path, 0, f"first heading should be '# {expected_h1}'"))
        body_lines = [line.strip() for _, line in prose_lines(meta["_body"])]
        for section in DECISION_SECTIONS:
            if section not in body_lines:
                findings.append(Finding("error", path, 0, f"missing section '{section}'"))
        if "This decision aims to" not in meta["_body"]:
            findings.append(Finding("error", path, 0, "Context should end with a sentence starting 'This decision aims to'"))

    index_path = DECISION_DIR / "README.md"
    rows = parse_index(index_path, r"ADR-\d{4}", sectioned=False)
    for did, entries in rows.items():
        if did not in decisions:
            findings.append(Finding("error", index_path, entries[0]["line"], f"{did} is listed but has no file"))
    for did, meta in decisions.items():
        if did not in rows:
            findings.append(Finding("error", index_path, 0, f"{did} is missing from the decision index"))
            continue
        entry = rows[did][0]
        expected = [str(meta.get("title")), str(meta.get("status")).capitalize(), str(meta.get("date"))]
        if entry["target"] != meta["_path"].name or entry["cells"][:3] != expected:
            findings.append(Finding("error", index_path, entry["line"],
                                    f"{did} row should link {meta['_path'].name} and read: {' | '.join(expected)}"))


def check_spikes(findings: list) -> None:
    if not SPIKE_DIR.is_dir():
        return
    for path in sorted(SPIKE_DIR.glob("*.md")):
        if path.name in ("README.md", "TEMPLATE.md"):
            continue
        if not SPIKE_FILE.match(path.name):
            findings.append(Finding("error", path, 0, "spike files are named YYYY-MM-DD-short-topic.md"))
        elif not (h1_of(path.read_text(encoding="utf-8")) or "").startswith("Spike: "):
            findings.append(Finding("error", path, 0, "spike title should start with 'Spike: '"))


def check_review_dates(findings: list, today: dt.date) -> None:
    for path in sorted(DOCS_DIR.glob("*.md")):
        if path.name in DOCS_WITHOUT_REVIEW_DATE:
            continue
        match = LAST_REVIEWED.search(path.read_text(encoding="utf-8"))
        if not match:
            findings.append(Finding("error", path, 0, "research docs need a '*Last reviewed: YYYY-MM-DD' line"))
        else:
            check_review_date(path, match.group(1), findings, today)


def check_open_questions(findings: list) -> None:
    path = DOCS_DIR / "open-questions.md"
    if not path.exists():
        return
    numbers = [(int(m.group(1)), n) for n, line in prose_lines(path.read_text(encoding="utf-8"))
               if (m := OPEN_QUESTION_LINE.match(line))]
    if [n for n, _ in numbers] != list(range(1, len(numbers) + 1)):
        findings.append(Finding("error", path, 0, "OQ numbers should run from OQ-1 upward with no gaps or repeats"))


def check_safety(findings: list) -> None:
    for path in walk_files(suffixes=TEXT_SUFFIXES, names=TEXT_NAMES):
        if path.name.startswith("LICENSE"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(text.splitlines(), 1):
            for label, pattern in SECRET_PATTERNS:
                for match in pattern.finditer(line):
                    if label == "email address" and match.group(0).lower().endswith(ALLOWED_EMAIL_DOMAINS):
                        continue
                    findings.append(Finding("error", path, number,
                                            f"possible {label}; public files must not contain one"))


def run_checks(today: dt.date | None = None) -> list:
    today = today or dt.date.today()
    findings: list = []
    problems = load_problems(findings)
    decisions = load_decisions(findings)
    check_links(findings)
    check_problems(problems, findings, today)
    check_problem_index(problems, findings)
    check_decisions(decisions, problems, findings, today)
    check_spikes(findings)
    check_review_dates(findings, today)
    check_open_questions(findings)
    check_safety(findings)
    return findings


# ---------------------------------------------------------------- commands

def cmd_check(_args) -> int:
    findings = run_checks()
    for finding in findings:
        print(finding)
    errors = sum(1 for f in findings if f.level == "error")
    warnings = len(findings) - errors
    print(f"\n{errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


def next_id(prefix: str, ids) -> str:
    numbers = [int(i.split("-")[1]) for i in ids]
    return f"{prefix}-{(max(numbers) if numbers else 0) + 1:04d}"


def cmd_next(_args) -> int:
    problem_ids = [PROBLEM_FILE.match(p.name).group(1) for p in PROBLEM_DIR.glob("P-*.md") if PROBLEM_FILE.match(p.name)]
    decision_ids = [DECISION_FILE.match(p.name).group(1) for p in DECISION_DIR.glob("ADR-*.md") if DECISION_FILE.match(p.name)]
    print(f"next problem:  {next_id('P', problem_ids)}")
    print(f"next decision: {next_id('ADR', decision_ids)}")
    print("IDs are never reused. Check open pull requests for IDs that are already in flight.")
    return 0


def cmd_work(_args) -> int:
    findings: list = []
    problems = load_problems(findings)
    rows = [m for m in problems.values()
            if m.get("champion") in (None, "unassigned") and m.get("status") in ("open", "exploring")]
    rows.sort(key=lambda m: (PHASE_ORDER.index(str(m.get("phase"))) if str(m.get("phase")) in PHASE_ORDER else 99,
                             DIFFICULTY_ORDER.index(m.get("difficulty")) if m.get("difficulty") in DIFFICULTY_ORDER else 99,
                             m["id"]))
    print("Problems with no champion, in roadmap order (earliest phase, easiest first):\n")
    for m in rows:
        open_questions = sum(1 for q in questions_in(m) if not q[3])
        print(f"  {m['id']}  phase {str(m.get('phase')):<8} {str(m.get('difficulty')):<9} "
              f"{open_questions} open question(s)  {m.get('title')}")
    return 0


def cmd_questions(args) -> int:
    findings: list = []
    problems = load_problems(findings)
    for pid in sorted(problems):
        if args.problem and pid != args.problem:
            continue
        for qid, _, text, answered in questions_in(problems[pid]):
            if answered and not args.all:
                continue
            print(f"{qid}{' (answered)' if answered else ''}: {text}")
    return 0


def cmd_index(_args) -> int:
    findings: list = []
    problems = load_problems(findings)
    decisions = load_decisions(findings)
    out = {"problems": [], "decisions": []}
    for pid in sorted(problems):
        m = problems[pid]
        out["problems"].append({
            "id": pid, "title": m.get("title"), "path": rel(m["_path"]),
            "layer": m.get("layer"), "phase": m.get("phase"), "status": m.get("status"),
            "difficulty": m.get("difficulty"), "champion": m.get("champion"),
            "related": m.get("related") or [],
            "decisions": sorted(d for d, dm in decisions.items()
                                if pid in (dm.get("problems") or []) or "*" in (dm.get("problems") or [])),
            "open_questions": [{"id": q[0], "text": q[2]} for q in questions_in(m) if not q[3]],
        })
    for did in sorted(decisions):
        m = decisions[did]
        out["decisions"].append({
            "id": did, "title": m.get("title"), "path": rel(m["_path"]), "status": m.get("status"),
            "date": m.get("date"), "problems": m.get("problems") or [], "topics": m.get("topics") or [],
            "supersedes": m.get("supersedes") or [], "superseded_by": m.get("superseded_by"),
        })
    json.dump(out, sys.stdout, indent=2)
    print()
    return 0


def external_urls() -> list[str]:
    urls = set()
    for path in walk_files(suffixes={".md", ".yml", ".yaml"}):
        for _, line in prose_lines(path.read_text(encoding="utf-8")):
            for match in re.findall(r"https?://[^\s)>\"'`\]]+", line):
                urls.add(match.rstrip(".,;:"))
    return sorted(u for u in urls if "github.com/internet-of-games/" not in u)


def probe(url: str) -> tuple[str, int]:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; iog-docs-linkcheck/1.0)"}
    for method in ("HEAD", "GET"):
        try:
            request = urllib.request.Request(url, headers=headers, method=method)
            with urllib.request.urlopen(request, timeout=20) as response:  # noqa: S310 (https only)
                return url, response.status
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in (403, 405, 501):
                continue
            return url, exc.code
        except Exception:  # timeouts, TLS and DNS errors
            if method == "HEAD":
                continue
            return url, 0
    return url, 0


def cmd_external(_args) -> int:
    urls = external_urls()
    print(f"checking {len(urls)} external links…")
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(probe, urls))
    broken = [(u, c) for u, c in results if c in (404, 410)]
    unsure = [(u, c) for u, c in results if c not in (404, 410) and not 200 <= c < 400]
    for url, code in unsure:
        print(f"CHECK BY HAND ({code or 'no response'}): {url}")
    for url, code in broken:
        print(f"BROKEN ({code}): {url}")
    print(f"\n{len(results) - len(broken) - len(unsure)} ok, {len(unsure)} to check by hand, {len(broken)} broken")
    return 1 if broken else 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("check", help="validate the docs")
    sub.add_parser("next", help="show the next free IDs")
    sub.add_parser("work", help="list unclaimed problems in roadmap order")
    questions = sub.add_parser("questions", help="list open questions")
    questions.add_argument("--problem", help="only this problem, e.g. P-0003")
    questions.add_argument("--all", action="store_true", help="include answered questions")
    sub.add_parser("index", help="print a JSON map of problems and decisions")
    sub.add_parser("external", help="check external links (needs network)")
    args = parser.parse_args(argv)
    commands = {"check": cmd_check, "next": cmd_next, "work": cmd_work, "questions": cmd_questions,
                "index": cmd_index, "external": cmd_external, None: cmd_check}
    return commands[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
