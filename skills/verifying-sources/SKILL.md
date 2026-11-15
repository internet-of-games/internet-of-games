---
name: verifying-sources
description: Use when adding a factual claim, statistic, date or standards status to any Internet of Games doc, or when re-checking existing facts. Covers choosing sources, labeling secondary reporting, review dates and link checks.
---

# Verifying sources

Every factual claim in this repository links to a source. People and agents make decisions based on these docs, so a wrong number causes real damage.

## Choosing a source

Prefer sources in this order:

1. **Primary sources:** a specification's own status page, a company's filing or press release, an official repository, a court record or a government page. For repository facts such as stars, last push and archived status, use the GitHub API.
2. **Reputable secondary sources,** when no primary source exists: established news outlets, and law-firm analyses for legal questions.
3. **Avoid** anonymous blogs, AI-generated pages, aggregator sites that don't cite sources, and anything behind a paywall or an NDA.

## Writing the claim

- Put the link on the claim itself, not only in a list at the end.
- If the source is secondary, say so: "reported", "according to".
- Give exact dates and versions ("W3C Recommendation, 15 May 2025"), never "recently".
- For numbers that change, such as users, revenue or stars, say when they were measured.
- Quote rarely and briefly, with attribution. Paraphrase wherever you can.
- Add important new sources to [docs/references.md](../../docs/references.md).
- Set the doc's `Last reviewed` line or `last_reviewed` field to today's date.

## Checking

1. `make check` validates internal links and anchors.
2. `make external` checks external links. Many sites block automated requests. For any link marked "check by hand", open it in a browser or confirm it through a search; never assume a blocked link is fine.
3. If a source disappears, find a replacement or an archived copy, or remove the claim.

## Red flags

- A statistic with no date.
- A status such as "final" or "ratified" that you didn't read on the official page.
- A claim about what a company *intends*, rather than what it has said or done.
- A source that only you can access.
