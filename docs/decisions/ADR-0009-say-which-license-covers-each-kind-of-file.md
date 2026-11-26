---
id: ADR-0009
title: Say which license covers each kind of file
status: accepted
date: 2026-11-26
problems: [P-0001, P-0026]
topics: [licensing, governance, contributions]
supersedes: []
superseded_by: null
---

# ADR-0009: Say which license covers each kind of file

## Context

[ADR-0002](ADR-0002-license-code-apache-docs-cc-by.md) licenses code under Apache-2.0 and documents under CC BY 4.0, but it doesn't say which files count as which. Several kinds of file sit in between: guides and agent instructions written in Markdown, configuration, schema files, and code samples printed inside documents. Our rules also promise that test files are released under CC0 ([AGENTS.md](../../AGENTS.md), rule 1), but the repository doesn't include the CC0 text.

The gap matters for sign-offs. Under the [Developer Certificate of Origin](https://developercertificate.org/), contributors certify their right to submit under "the open source license indicated in the file", and our files don't indicate one.

Two more facts shape the choice. Creative Commons recommends against using its licenses for software ([CC FAQ](https://creativecommons.org/faq/)), yet game developers will copy schemas and code samples from our documents into their code. And Khronos, whose glTF format we build on, uses a similar split in its glTF repository: CC BY 4.0 for specification text and informative files, and Apache-2.0 for everything else ([glTF contributing guide](https://github.com/KhronosGroup/glTF/blob/main/CONTRIBUTING.adoc)).

This decision aims to make the license of every file obvious, to contributors and to the studios that reuse our work, before outside contributions arrive.

## Options

1. **Leave it to judgment.** No work now, but every unclear file becomes a question later, when changing its license would need the agreement of everyone who contributed to it.
2. **A license header in every file.** Precise, but it clutters documents, and it's easy to forget.
3. **One license for each kind of file, listed in one place,** with short headers only in program source files.

## Decision

We will license each kind of file as follows, and list these rules in the [README](../../README.md#licenses) and [CONTRIBUTING.md](../../CONTRIBUTING.md#licenses):

| Files | License |
|---|---|
| Documents: every Markdown file, including future specification text | CC BY 4.0 ([LICENSE-DOCS](../../LICENSE-DOCS)) |
| Code and every other file, such as tools, the Makefile, workflows, configuration and schema files | Apache-2.0 ([LICENSE](../../LICENSE)) |
| Code samples and schemas inside documents | CC BY 4.0 or Apache-2.0, at the reader's choice |
| Test files and sample assets, such as made-up player data, avatars and credentials | CC0 1.0 ([LICENSE-CC0](../../LICENSE-CC0)) |

Program source files, such as the scripts in `tools/` and the Makefile, start with a copyright line and an [SPDX license identifier](../glossary.md), so their license travels with them when they're copied. The license texts themselves keep their own terms.

## Consequences

- Contributors know which license their sign-off covers, for every file.
- Developers can copy code samples and schemas from our documents into open or closed code under Apache-2.0, which includes a patent license from contributors.
- Test files can be used anywhere without attribution, which conformance testing needs ([P-0026](../../problems/P-0026-conformance-and-interop-testing.md)).
- CC BY 4.0 (section 2(b)(2)) and CC0 (section 4(a)) don't license patents, and this decision doesn't change that. The patent policy for specification text is still open as [P-0001-Q1](../../problems/P-0001-neutral-governance-and-ip.md). If that decision puts specification text, and the schemas that belong to it, under a specification license, a new ADR will supersede this one for those files.

## Universality and safety

Clear, permissive terms for every file keep adoption cheap for every kind of game, from closed-source commercial titles to one-person projects ([P-0030](../../problems/P-0030-built-for-every-game.md)). Unclear terms would favor studios with legal teams over small ones. This decision doesn't change any threat in the [threat model](../threat-model.md).
