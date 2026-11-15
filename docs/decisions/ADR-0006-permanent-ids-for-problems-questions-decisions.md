---
id: ADR-0006
title: Give problems, questions and decisions permanent IDs
status: accepted
date: 2026-11-15
problems: ["*"]
topics: [process]
supersedes: []
superseded_by: null
---

# ADR-0006: Give problems, questions and decisions permanent IDs

## Context

People and AI agents need to point at a specific problem or question from issues, pull requests, commits and other docs. Titles change, files get renamed, and a link built from a title breaks when the title does. Precise references also let tools build an accurate map of the project.

This decision aims to make every problem, question and decision referenceable forever.

## Decision

We will identify problems as `P-NNNN`, their open questions as `P-NNNN-QN`, decisions as `ADR-NNNN` and cross-cutting questions as `OQ-N`. IDs are permanent and never reused.

- Problem and decision files start with their ID, for example `P-0003-player-identifier.md`.
- `make next` prints the next free ID, and `make check` enforces the formats and checks that question numbers run in order.
- An answered question is struck through and linked to its decision, never deleted.

## Consequences

- References stay stable even when titles change.
- Parked or merged problems keep their IDs, so old links still make sense.
- Pull requests opened in parallel can pick the same number, so authors check open pull requests before choosing one.

## Universality and safety

Not applicable: process decision.
