---
id: ADR-0002
title: License code under Apache-2.0 and documents under CC BY 4.0
status: accepted
date: 2026-11-15
problems: [P-0001]
topics: [licensing, governance]
supersedes: []
superseded_by: null
---

# ADR-0002: License code under Apache-2.0 and documents under CC BY 4.0

## Context

A standard that every game can build on has to be free to use, copy and implement, including in commercial, closed-source games. Contributors need a simple way to take part, and implementers need confidence that contributors can't later assert patents against them ([P-0001](../../problems/P-0001-neutral-governance-and-ip.md)). Licensing is hard to change once outside contributions arrive, because changing it needs every contributor's agreement.

This decision aims to set licenses that let anyone adopt the work, while keeping contribution simple.

## Options

1. **MIT for code, CC BY 4.0 for documents.** Short and familiar, but with no explicit patent license from contributors.
2. **CC0 for everything.** Maximum reuse, but no attribution and no patent license.
3. **Apache-2.0 for code, CC BY 4.0 for documents, contributions under the DCO.** Includes a patent license for code, attribution for documents, and a lightweight contribution process.
4. **Either of the above with a contributor license agreement.** Stronger legal footing, but it puts off casual contributors.

## Decision

We will license code under Apache-2.0 and documentation and specifications under CC BY 4.0, and accept contributions under the Developer Certificate of Origin, with no contributor license agreement.

## Consequences

- Any game, studio or platform can implement and ship the work, commercially or otherwise.
- CC BY 4.0 doesn't license patents, so specification text needs its own patent policy before normative text is merged. That remains open as [P-0001-Q1](../../problems/P-0001-neutral-governance-and-ip.md).
- Changing these licenses later requires contributors' agreement.

## Universality and safety

Permissive licenses let every kind of game adopt the standard without fees, which serves universality ([P-0030](../../problems/P-0030-built-for-every-game.md)). Because anyone can fork the work, the risk of capture by a single party (T7 in the [threat model](../threat-model.md)) goes down.
