---
id: ADR-0001
title: Record decisions as ADRs
status: accepted
date: 2026-11-15
problems: ["*"]
topics: [process]
supersedes: []
superseded_by: null
---

# ADR-0001: Record decisions as ADRs

## Context

Most of this repository is problem docs: open explorations full of options and questions. As the community settles questions, readers and AI agents need to tell "options under discussion" apart from "what we decided". They also need to find out *why* a decision was made long after the conversation ends. Decisions left inside problem docs or pull-request threads get lost, or quietly reversed.

This decision aims to give every lasting decision a stable, findable record.

## Decision

We will record each significant decision as an architecture decision record (ADR) in `docs/decisions/`, named `ADR-NNNN-short-title.md`, with one decision per record.

- Every record uses [TEMPLATE.md](TEMPLATE.md), whose front matter covers status, date, related problems and topics.
- A record is accepted when its pull request merges. The valid statuses are `accepted`, `superseded` and `deprecated`.
- Accepted records aren't rewritten. When a decision changes, a new record supersedes the old one, and the two link to each other.
- When a record is accepted, the documents it affects are updated in the same pull request, including striking through the open questions it answers.
- `make check` validates every record and the index.

## Consequences

- Problem docs stay exploratory, and every decision has one obvious home.
- The history of a decision, including what replaced it, can be followed through the `supersedes` links.
- Records take effort to write, so small, easily reversed choices don't need one. When in doubt, write one.

## Universality and safety

Not applicable: process decision.
