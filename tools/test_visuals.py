# Copyright 2026 The Internet of Games contributors
# SPDX-License-Identifier: Apache-2.0
"""Unit tests for tools/visuals.py. Run with: make test

They don't start a browser or use the network."""
from __future__ import annotations

import datetime as dt
import os
import unittest
from pathlib import Path
from unittest import mock

import visuals

FENCE = "`" * 3

BRIEF = f"""---
kind: Pull request #7
title: Compare credential formats
status: Ready for review
---

## What
Compares two formats in [the spike](docs/spikes/x.md#findings).

## Why
Phase 1 needs one format, see `docs/not-a-link.md`.

## Ask
Review it, then [decide](https://example.com/decide).

## Facts
- 2 formats
- 1 spike

## Diagram
{FENCE}mermaid
flowchart LR
  A --> B
{FENCE}

## Details
## What this changes
Text with a [relative link](problems/P-0013-portable-claims.md).

{FENCE}text
## Not a heading
[not](a-link.md)
{FENCE}

## Footer
Made with an agent.
"""


class ParseTests(unittest.TestCase):
    def test_sections(self):
        brief = visuals.parse_brief(BRIEF)
        self.assertEqual(brief.title, "Compare credential formats")
        self.assertEqual([label for label, _ in brief.points], ["What", "Why", "Ask"])
        self.assertEqual(brief.facts, ["2 formats", "1 spike"])
        self.assertEqual(brief.diagram, "flowchart LR\n  A --> B")
        self.assertTrue(brief.details.startswith("## What this changes"))
        self.assertIn("## Not a heading", brief.details)
        self.assertEqual(brief.footer, "Made with an agent.")

    def test_needs_three_points(self):
        text = BRIEF.replace("## Ask\nReview it, then [decide](https://example.com/decide).\n", "")
        with self.assertRaisesRegex(visuals.BriefError, "three"):
            visuals.parse_brief(text)

    def test_needs_a_title(self):
        with self.assertRaises(visuals.BriefError):
            visuals.parse_brief("---\nkind: Issue\n---\n## What\nx\n")
        with self.assertRaises(visuals.BriefError):
            visuals.parse_brief("## What\nx\n")

    def test_diagram_must_be_mermaid(self):
        text = BRIEF.replace(f"{FENCE}mermaid", f"{FENCE}text")
        with self.assertRaises(visuals.BriefError):
            visuals.parse_brief(text)

    def test_text_before_the_first_heading(self):
        with self.assertRaises(visuals.BriefError):
            visuals.parse_brief("---\ntitle: T\n---\nstray text\n## What\nx\n")

    def test_lengths(self):
        brief = visuals.parse_brief(BRIEF)
        self.assertEqual(visuals.check_lengths(brief), [])
        brief.points[0] = ("A label that is too long", "x" * 200)
        brief.facts = ["a", "b", "c", "d", "e"]
        self.assertEqual(len(visuals.check_lengths(brief)), 3)


class TextTests(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(visuals.plain("See **the** [spike](x.md), `make check` and _this_."),
                         "See the spike, make check and this.")

    def test_alt_text(self):
        brief = visuals.parse_brief(BRIEF)
        alt = visuals.alt_text(brief)
        self.assertIn("Pull request #7: Compare credential formats.", alt)
        self.assertIn("Status: Ready for review.", alt)
        self.assertIn("2 formats, 1 spike.", alt)
        brief.meta["alt"] = "A [bracketed]\nalt"
        self.assertEqual(visuals.alt_text(brief), "A (bracketed) alt")

    def test_unsafe_text(self):
        address = "player" + "@" + "mailbox.test"
        self.assertEqual(len(visuals.unsafe_text(f"Write to {address}")), 1)
        self.assertEqual(visuals.unsafe_text("Write to " + "someone" + "@" + "example.com"), [])
        self.assertEqual(len(visuals.unsafe_text("/ho" + "me/someone/notes.md")), 1)
        self.assertEqual(len(visuals.unsafe_text("[x](file:///etc/hosts)")), 1)


class LinkTests(unittest.TestCase):
    BASE = "https://github.com/o/r/blob/abc123/"

    def test_relative_links_point_at_the_commit(self):
        text = visuals.absolutize("[a](docs/x.md#y) [b](./problems/P-0001-a.md) [c](/README.md)", "o/r", "abc123")
        self.assertEqual(text, f"[a]({self.BASE}docs/x.md#y) [b]({self.BASE}problems/P-0001-a.md) "
                               f"[c]({self.BASE}README.md)")

    def test_code_in_link_text(self):
        self.assertEqual(visuals.absolutize("[`did:key` keys](docs/x.md)", "o/r", "abc123"),
                         f"[`did:key` keys]({self.BASE}docs/x.md)")

    def test_other_links_are_kept(self):
        text = "[a](https://example.com) [b](#anchor) [c](mailto:x) `[d](e.md)`"
        self.assertEqual(visuals.absolutize(text, "o/r", "abc123"), text)

    def test_images_use_raw_files(self):
        self.assertEqual(visuals.absolutize("![alt](docs/a.png)", "o/r", "abc123"),
                         "![alt](https://github.com/o/r/raw/abc123/docs/a.png)")

    def test_code_blocks_are_kept(self):
        text = f"{FENCE}\n[a](b.md)\n{FENCE}\n"
        self.assertEqual(visuals.absolutize(text, "o/r", "abc123"), text)

    def test_reference_definitions(self):
        self.assertEqual(visuals.absolutize("[ref]: docs/x.md\n", "o/r", "abc123"), f"[ref]: {self.BASE}docs/x.md\n")

    def test_links_outside_the_repository(self):
        with self.assertRaises(visuals.BriefError):
            visuals.absolutize("[a](../elsewhere.md)", "o/r", "abc123")


class OutputTests(unittest.TestCase):
    def test_body_layout(self):
        brief = visuals.parse_brief(BRIEF)
        body = visuals.body_markdown(brief, "./pr-card.png", "https://example.com/digest.pdf")
        lines = body.splitlines()
        self.assertTrue(lines[0].startswith("![Summary card."))
        self.assertTrue(lines[0].endswith("](./pr-card.png)"))
        self.assertIn("**What:** Compares two formats", body)
        self.assertIn("(https://example.com/digest.pdf)", body)
        self.assertIn(f"{FENCE}mermaid\nflowchart LR", body)
        self.assertLess(body.index(f"{FENCE}mermaid"), body.index("<details>"))
        self.assertLess(body.index("</details>"), body.index("Made with an agent."))

    def test_card_escapes_text(self):
        brief = visuals.parse_brief(BRIEF.replace("Compare credential formats", "Compare <b>formats</b> & more"))
        page = visuals.card_html(brief, "o/r", dt.date(2026, 11, 26))
        self.assertNotIn("<b>formats", page)
        self.assertIn("Compare formats &amp; more", page)
        self.assertIn("26 November 2026", page)
        self.assertIn("2 formats", page)

    def test_card_keeps_ids_together(self):
        self.assertEqual(visuals.card_text("Phase 1 & P-0013-Q2, ADR-0009, #3"),
                         '<span class="nb">Phase 1</span> &amp; <span class="nb">P-0013-Q2</span>, '
                         '<span class="nb">ADR-0009</span>, <span class="nb">#3</span>')

    def test_card_keeps_code_style(self):
        self.assertEqual(visuals.card_inline("Run `make <x>` on [`did:key`](a.md) & P-0001"),
                         'Run <code>make &lt;x&gt;</code> on <code>did:key</code> &amp; <span class="nb">P-0001</span>')

    def test_status_colors(self):
        self.assertEqual(visuals.status_style("Needs your decision"), visuals.status_style("waiting"))
        self.assertNotEqual(visuals.status_style("Ready for review"), visuals.status_style("Needs your decision"))
        self.assertEqual(visuals.status_style("Merged"), visuals.status_style("done"))


class MarkdownTests(unittest.TestCase):
    def test_simple_markdown(self):
        out = visuals.simple_markdown("\n".join([
            "# Title", "", "Some **bold**, `code` and a [link](https://example.com/a?b=1&c=2).", "",
            "| A | B |", "|---|---|", "| 1 | 2 |", "", "- [x] done", "- [ ] open", "",
            "<details>", "<summary><b>More</b></summary>", "", "<script>alert(1)</script>", "", "</details>"]))
        self.assertIn("<h1>Title</h1>", out)
        self.assertIn("<strong>bold</strong>", out)
        self.assertIn("<code>code</code>", out)
        self.assertIn('<a href="https://example.com/a?b=1&amp;c=2">link</a>', out)
        self.assertIn("<th>A</th>", out)
        self.assertIn("<td>2</td>", out)
        self.assertIn("☑ done", out)
        self.assertIn("☐ open", out)
        self.assertIn("<details open>", out)
        self.assertIn("<summary><strong>More</strong></summary>", out)
        self.assertNotIn("<script>", out)

    def test_bare_urls_become_links(self):
        self.assertEqual(visuals.inline_html("See https://example.com/x."),
                         'See <a href="https://example.com/x">https://example.com/x</a>.')

    def test_mermaid_blocks_are_drawn(self):
        text, blocks = visuals.take_mermaid(f"Before\n\n{FENCE}mermaid\nflowchart LR\n  A --> B\n{FENCE}\n\nAfter")
        self.assertEqual(blocks, ["flowchart LR\n  A --> B"])
        html = visuals.finish_html(visuals.simple_markdown(text), blocks)
        self.assertIn('<pre class="mermaid">flowchart LR\n  A --&gt; B</pre>', html)

    def test_finish_html(self):
        html = visuals.finish_html('<details><summary>x</summary></details><a href="/o/r/pull/3">#3</a>'
                                   '<img src="https://example.com/a.png" alt="A chart">', [])
        self.assertIn("<details open>", html)
        self.assertIn('href="https://github.com/o/r/pull/3"', html)
        self.assertIn('<a href="https://example.com/a.png">[image: A chart]</a>', html)
        self.assertNotIn("<img", html)


class FileTests(unittest.TestCase):
    def test_pdf_links_and_pages(self):
        data = (b"<< /Type /Pages /Count 2 >> << /Type /Page >> << /Type /Page >>"
                b"<< /A << /S /URI /URI (https://example.com/a) >> >> << /URI (file:///x) >>")
        self.assertEqual(visuals.pdf_links(data), ["https://example.com/a", "file:///x"])
        self.assertEqual(visuals.pdf_pages(data), 2)

    def test_png_size(self):
        import struct
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "a.png"
            path.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00\x00\x00\x0dIHDR" + struct.pack(">II", 2400, 1260))
            self.assertEqual(visuals.png_size(path), (2400, 1260))


class BrowserTests(unittest.TestCase):
    def test_override(self):
        with mock.patch.dict(os.environ, {"IOG_BROWSER": "flatpak run com.example.Browser"}):
            self.assertEqual(visuals.find_browser(), ["flatpak", "run", "com.example.Browser"])

    def test_flatpak_gets_the_folder_and_no_network(self):
        command = visuals.browser_command(["flatpak", "run", "com.example.Browser"], Path("/w"), ["--x"])
        self.assertEqual(command[:5], ["flatpak", "run", "--filesystem=/w", "--unshare=network", "com.example.Browser"])
        self.assertEqual(command[-1], "--x")
        self.assertIn("--host-resolver-rules=MAP * ~NOTFOUND", command)

    def test_other_browsers(self):
        command = visuals.browser_command(["/usr/bin/chromium"], Path("/w"), ["--x"])
        self.assertEqual(command[0], "/usr/bin/chromium")
        self.assertIn("--user-data-dir=/w/profile", command)


if __name__ == "__main__":
    unittest.main()
