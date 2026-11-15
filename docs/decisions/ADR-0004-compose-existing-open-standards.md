---
id: ADR-0004
title: Compose existing open standards instead of inventing new formats
status: accepted
date: 2026-11-15
problems: [P-0003, P-0008, P-0013]
topics: [standards, architecture]
supersedes: []
superseded_by: null
---

# ADR-0004: Compose existing open standards instead of inventing new formats

## Context

Each layer of a portable player identity already has a mature or maturing open standard. These include decentralized identifiers, Verifiable Credentials 2.0, OpenID for credential issuance and presentation, selective disclosure, Open Badges 3.0, and glTF with VRM ([standards-map.md](../standards-map.md)). What's missing is a profile for games that combines them, plus implementations that game engines can use. New formats take years to mature, fragment the ecosystem, and miss out on the security review the existing standards have already had.

This decision aims to get to a working, trustworthy standard faster by building on proven pieces.

## Options

1. **Invent a game-specific format.** Full control, but slow, unproven and isolated.
2. **Adopt one vendor's format.** Fast, but it hands control to that vendor.
3. **Compose open standards and write gaming profiles** that constrain them.

## Decision

We will build on existing open standards and write profiles that constrain them for games. We'll create a new format only when there's a documented gap that neither a profile nor an extension contributed upstream can fill.

## Consequences

- We inherit existing tooling, test suites and security review.
- We depend on other groups' timelines, such as the Khronos avatar extensions, and our profiles have to track their changes.
- Game-engine libraries for identifiers and credentials are thin today, so we'll need to build them ([P-0025](../../problems/P-0025-developer-adoption-cost.md)).

## Universality and safety

Open standards work across engines, platforms and companies, which serves universality ([P-0030](../../problems/P-0030-built-for-every-game.md)). Mature, reviewed cryptography lowers the risk of forged claims and of attacks on our own tools (T4 and T8 in the [threat model](../threat-model.md)).
