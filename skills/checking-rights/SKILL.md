---
name: checking-rights
description: Use before committing or opening a pull request for any change that draws on outside material (news, research, specifications, other projects or AI-drafted text), and when reviewing someone else's change. A checklist for copied text, credit, licenses, confidential material, personal data, trademarks and fair description.
---

# Checking rights and originality

Run this review on every change that uses outside material. The rules and the reasons for them are in [docs/sourcing-and-originality.md](../../docs/sourcing-and-originality.md). This is a review, not legal advice: when a question needs a lawyer, say so and stop.

## Get ready

1. Look at the whole change: `git diff --stat main...HEAD` and `git diff main...HEAD` for a branch, or `git status` and `git diff` for uncommitted work.
2. List the outside material it draws on: every linked source, plus any notes, summaries or drafts it was written from.
3. For each source the change leans on, save a copy outside the repository (for example in a folder made with `mktemp -d`; turn PDFs into text with a tool such as `pdftotext`). Then run `make overlap SOURCE=<saved copy> FILES="<changed files>"` and look at every run it reports.

## Check

| Area | Passes when | Usual fix |
|---|---|---|
| Copied words | No passage follows a source's wording or structure. Every run `make overlap` reports is a quotation, a name or a title | Rewrite from the facts |
| Quotations | Each is 40 words or fewer, in quotation marks, attributed and linked, and quotations are a small part of what we say about the source | Shorten, paraphrase or cut |
| Credit for ideas | Every design, term or argument from someone else is credited where it's used, and listed in prior art or the standards map if it shapes our design | Add the credit |
| Facts | Every claim links to its source at the claim. Secondary sources say "reported". Dates and versions are exact | Fix the citation ([verifying-sources](../verifying-sources/SKILL.md)) |
| Licenses | Nothing is copied from specifications, share-alike content or all-rights-reserved content. Reused permissive content carries attribution and its license. Code is compatible with Apache-2.0 | Remove or replace it |
| Images and data | No copied images, logos, screenshots, figures or whole tables | Draw our own; cite the figures |
| Confidential material | Nothing from non-disclosure agreements, leaks, private repositories, internal documents or paywalled pages | Remove it and tell a maintainer |
| Personal data | No private individuals. People in public roles are named only when it matters | Refer to roles |
| Trademarks | Names only refer to things. No logos, and nothing implies endorsement | Reword |
| Fairness | Companies and people are described by what they said or did, with sources, and no motives are guessed | Reword around the evidence |
| AI involvement | The pull request says an agent helped, and no AI-generated page is cited as evidence | Find the primary source |

## Report

Give a verdict, **PASS** or **FIX FIRST**, then one line per problem: `file:line`, what's wrong, which row of the table it fails, and the fix. Finish with anything you couldn't check, such as a source that blocks automated access, so a person can check it by hand.

## Red flags

- A long, fluent passage on a technical topic that cites a single source. It's often a paraphrase of that source.
- A quotation with no link, or a link with no date.
- A figure or table laid out exactly like one in a source.
- A source you could only read through a login, a paywall or someone's private copy.
- Text pasted from a chat, a newsletter or an AI summary.
