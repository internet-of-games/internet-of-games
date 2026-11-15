---
id: ADR-0007
title: Keep everything in one repository until there is code
status: accepted
date: 2026-11-15
problems: ["*"]
topics: [process, repository]
supersedes: []
superseded_by: null
---

# ADR-0007: Keep everything in one repository until there is code

## Context

The organization could host separate repositories for specifications, SDKs, demo games and research. In Phase 0 the documents reference each other heavily, and splitting them would break links, divide contributors' attention and multiply the checks to maintain.

This decision aims to keep the project easy to contribute to while it's mostly documents.

## Decision

We will keep the documents, problems, decisions, specifications and early prototypes in this one repository until Phase 1 code makes a split clearly useful, and record any split in a new ADR.

## Consequences

- There's one place to search, contribute and run `make check`.
- SDKs may eventually need their own repositories for release cycles, packaging or different licenses. That will be a new decision.
- An organization-level `.github` repository for the public profile and default community files is a separate question, not covered here.

## Universality and safety

Not applicable: process decision.
