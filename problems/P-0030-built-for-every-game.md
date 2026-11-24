---
id: P-0030
title: Built for every game
layer: cross-cutting
phase: 1
status: open
difficulty: high
champion: unassigned
related: [P-0002, P-0021, P-0025, P-0026]
last_reviewed: 2026-11-15
---

# P-0030: Built for every game

**In one sentence:** to become the baseline of the gaming world, the standard has to work for *every* kind of game: one-person mobile games and live services with over a hundred million players, single-player offline adventures and social worlds, on every platform and at every age rating, between companies and *within* them.

## Why it matters

The mission is a standard that **every game builds on** ([problem statement](../docs/problem-statement.md#the-mission)). A standard that only suits small web games stays a niche. One that only suits big online games leaves out most of the medium. Decisions made early, in Phase 1, can quietly rule out whole categories of games later, so the requirements need to be written down now.

## The range a universal standard must cover

| Dimension | From | To | What it demands of the standard |
|---|---|---|---|
| **Scale** | A game with a handful of players | Platforms with over 100 million daily players. Roblox averaged 144M daily users in Q4 2025 ([GamesBeat](https://gamesbeat.com/roblox-stock-rises-20-after-earnings-daily-active-users-up-69-in-q4/)) | Local, cheap verification; no central service in the login path |
| **Connectivity** | Fully offline single-player games | Always-online live services | Works offline, syncs later, and is clear about what an offline claim can prove (see below) |
| **Platforms** | Web and PC | Consoles, mobile, VR and cloud streaming | No dependence on any one platform's features ([P-0021](P-0021-platform-holder-rules.md)) |
| **Age ratings** | Rated for everyone, like NBA 2K26 ([ESRB](https://www.esrb.org/ratings/40735/nba-2k26/)) | Rated mature, like Grand Theft Auto VI ([ESRB](https://www.esrb.org/ratings/41627/grand-theft-auto-vi/)) | Age signals and safety defaults that fit both ([P-0007](P-0007-age-and-eligibility.md)) |
| **Genres** | Puzzle, sports, racing | RPGs, shooters, sims, social worlds | Nothing in the core may assume a genre, for example a humanoid avatar or a level system |
| **Business models** | Premium, one-time purchase | Free-to-play, subscriptions, ad-supported | Nothing in the core may assume a store or a payment model |
| **Engines** | Godot, web | Unity, Unreal and in-house engines | Formats and SDKs that any engine can implement ([P-0025](P-0025-developer-adoption-cost.md)) |
| **Relationships between games** | Two unrelated studios | Many titles from one publisher | The standard should be the easiest way for a publisher to connect *its own* games, not only to connect with others |

## A subtle problem: claims from offline games

An online game signs claims on its servers, where its keys are safe. A fully offline game has to sign on the player's device, and anyone determined enough can pull keys out of a device. So a claim from an offline game proves less than a claim from an online one. The standard should **say so honestly**, for example with a "client-attested" trust level, so receiving games can decide how much weight to give it ([P-0015](P-0015-issuer-trust-revocation.md)).

## Constraints

- **Layers are optional.** A tiny game can implement only identity and appearance; a large one can implement everything ([P-0026](P-0026-conformance-and-interop-testing.md) conformance levels).
- **No required server or account** for the basic flow.
- **Nothing in the core assumes** a genre, platform, store, business model or always-online connection.

## What "solved enough" looks like (Phase 1)

- [ ] A written universality requirements document with target numbers, for example: verify a passport in under a set number of milliseconds on a mid-range phone, with zero network calls when keys are cached (first draft: [universality requirements](../docs/universality-requirements.md))
- [ ] Every Phase 1 design reviewed against the requirements, with any gaps written down
- [ ] Trust levels defined for claims from online and offline games (first draft in the [universality requirements](../docs/universality-requirements.md#6-honest-about-how-much-a-claim-proves))
- [ ] A load-test plan for verification at very large scale

## Open questions

- **P-0030-Q1:** What are the right performance targets for verification at login, on low-end devices and at very large scale?
- **P-0030-Q2:** How should offline single-player games sign claims, and how should receiving games treat them?
- **P-0030-Q3:** What does a publisher need in order to use the standard *inside* its own portfolio, for example a shared identity across all its titles?
- **P-0030-Q4:** What's the smallest useful profile for very small games and game jams?

## Champion brief

- **First deliverable:** A written set of universality requirements with target numbers, each with its basis.
- **Decisions you'd drive:** performance targets (P-0030-Q1), how offline games sign claims and how much they're trusted (P-0030-Q2), and what publishers need inside their own portfolios (P-0030-Q3).
- **Helpful background:** experience across several kinds of games, platforms or studio sizes, and performance testing.
- **Commitment:** a few hours a week, until a proposal is ready for public review.

## How to help

- Developers from different genres, platforms and studio sizes: describe what would stop *your* game from adopting this.
- Benchmark signature verification on low-end phones and older consoles (public specifications only).

## Decisions so far

- [ADR-0003](../docs/decisions/ADR-0003-universal-scope-built-in-risk-order.md): sets the universal scope that this problem turns into concrete requirements.

## References

- [Problem statement](../docs/problem-statement.md) · [Design principles](../docs/design-principles.md)
