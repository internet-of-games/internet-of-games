"""Unit tests for tools/docs.py. Run with: make test"""
from __future__ import annotations

import datetime as dt
import tempfile
import unittest
from pathlib import Path

import docs


class FrontMatterTests(unittest.TestCase):
    def test_scalars_lists_and_comments(self):
        block = "\n".join([
            "id: P-0001",
            'title: "Discovery: finding games"',
            "related: [P-0002, P-0003]",
            "empty: []",
            "status: open  # open | exploring",
            "champion: null",
        ])
        meta = docs.parse_front_matter(block)
        self.assertEqual(meta["id"], "P-0001")
        self.assertEqual(meta["title"], "Discovery: finding games")
        self.assertEqual(meta["related"], ["P-0002", "P-0003"])
        self.assertEqual(meta["empty"], [])
        self.assertEqual(meta["status"], "open")
        self.assertIsNone(meta["champion"])

    def test_hash_inside_quotes_is_kept(self):
        self.assertEqual(docs.strip_comment(' "a # b"  # note'), ' "a # b"')

    def test_split_without_front_matter(self):
        block, body = docs.split_front_matter("# Title\n")
        self.assertIsNone(block)
        self.assertEqual(body, "# Title\n")

    def test_bad_line_raises(self):
        with self.assertRaises(ValueError):
            docs.parse_front_matter("no colon here")


class AnchorTests(unittest.TestCase):
    def test_github_style_slugs(self):
        self.assertEqual(docs.slugify("1. The licenses don't stretch"), "1-the-licenses-dont-stretch")
        self.assertEqual(docs.slugify("Pokémon HOME"), "pokémon-home")
        self.assertEqual(docs.slugify("Using `did:web` [here](x.md)"), "using-didweb-here")

    def test_links_inside_inline_code_are_ignored(self):
        line = "Strike it (`- ~~Q1~~ Decided in [ADR-0009](…).`) and see [real](x.md)."
        self.assertEqual(docs.LINK.findall(docs.strip_inline_code(line)), ["x.md"])

    def test_duplicates_and_code_fences(self):
        text = "# A\n\n```\n# Not a heading\n```\n\n## A\n"
        self.assertEqual(docs.anchors_for(text), {"a", "a-1"})


class QuestionTests(unittest.TestCase):
    def test_question_ids_answered_flag_and_line_numbers(self):
        content = "\n".join([
            "---", "id: P-0042", "---", "", "# P-0042: Example", "",
            "## Open questions", "",
            "- **P-0042-Q1:** First question?",
            "- ~~**P-0042-Q2:** Second question?~~ Decided in ADR-0001.",
            "",
        ])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "P-0042-example.md"
            path.write_text(content, encoding="utf-8")
            block, body = docs.split_front_matter(content)
            meta = docs.parse_front_matter(block)
            meta.update({"_path": path, "_body": body})
            found = docs.questions_in(meta)
        self.assertEqual([q[0] for q in found], ["P-0042-Q1", "P-0042-Q2"])
        self.assertEqual([q[3] for q in found], [False, True])
        self.assertEqual(found[0][1], 9)


class IdTests(unittest.TestCase):
    def test_next_id_never_reuses(self):
        self.assertEqual(docs.next_id("P", ["P-0001", "P-0030"]), "P-0031")
        self.assertEqual(docs.next_id("ADR", []), "ADR-0001")


class ReviewDateTests(unittest.TestCase):
    def test_stale_is_warning_future_is_error(self):
        today = dt.date(2026, 11, 15)
        findings = []
        docs.check_review_date(Path("x.md"), "2025-01-01", findings, today)
        docs.check_review_date(Path("y.md"), "2027-01-01", findings, today)
        docs.check_review_date(Path("z.md"), "not-a-date", findings, today)
        self.assertEqual([f.level for f in findings], ["warning", "error", "error"])


class SafetyPatternTests(unittest.TestCase):
    def matches(self, label, text):
        pattern = dict(docs.SECRET_PATTERNS)[label]
        return bool(pattern.search(text))

    def test_detects_tokens_and_paths(self):
        fake_token = "gh" + "p_" + "A1b2C3d4" * 4
        self.assertTrue(self.matches("GitHub token", f"token={fake_token}"))
        sample_path = "/" + "home" + "/someone/notes"  # built in pieces so this file passes the scan
        self.assertTrue(self.matches("home-directory path", f"see {sample_path}"))
        self.assertTrue(self.matches("private key", "-----BEGIN " + "OPENSSH PRIVATE KEY-----"))

    def test_ignores_ordinary_text(self):
        self.assertFalse(self.matches("GitHub token", "the github.com/omigroup repository"))
        self.assertFalse(self.matches("home-directory path", "news/home/2026 and ~/projects"))


class RepositoryTests(unittest.TestCase):
    def test_repository_passes_checks(self):
        errors = [str(f) for f in docs.run_checks() if f.level == "error"]
        self.assertEqual(errors, [], "run 'make check' for details")


if __name__ == "__main__":
    unittest.main()
