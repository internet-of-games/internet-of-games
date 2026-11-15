---
id: P-0027
title: "Discovery: finding participating games"
layer: presence
phase: 3
status: open
difficulty: medium
champion: unassigned
related: [P-0017, P-0019, P-0029]
last_reviewed: 2026-11-15
---

# P-0027: Discovery: finding participating games

**In one sentence:** a network of games is only useful if players can find the games that will recognize them, without a central store deciding who's in.

## Why it matters

The web works because anyone can publish and anyone can link. If discovery runs through one directory, that directory becomes the new gatekeeper.

## What exists today

- **Stores and platforms** run discovery for their own catalogs, using their own curation and algorithms.
- **OMA3's portaling draft** describes moving between worlds, but not finding them ([specification](https://github.com/oma3dao/iwps-specification)).
- **The web** discovers sites through links, search and well-known URLs.

## A sketch

- **A game manifest** published at a well-known URL on the game's own website, reachable from the game's world addresses ([P-0029](P-0029-world-addressing-and-links.md)). It lists which passport features the game accepts and issues, and any reward offers ([P-0019](P-0019-cross-game-entitlements.md)).
- **Open directories:** any number of them, run by anyone, all built from the same manifests.
- **"Where can I use this?"**: a player's passport app can ask directories which games honor a particular credential.
- **In-game portals** ([P-0017](P-0017-world-handoff.md)).

## Constraints

- **No single required directory.**
- **Privacy:** asking "where can I use this credential?" shouldn't reveal the player to the directory.
- **Spam resistance** for manifests and directories.

## What "solved enough" looks like (Phase 3)

- [ ] A manifest format, published by the demo games
- [ ] At least one open directory that can be built from manifests
- [ ] "Where can I use this?" demonstrated without sending the player's identity to the directory

## Open questions

- **P-0027-Q1:** What should the manifest contain?
- **P-0027-Q2:** How should directories curate and fight spam without becoming gatekeepers?
- **P-0027-Q3:** How can directory queries stay private?
- **P-0027-Q4:** Should conformance results ([P-0026](P-0026-conformance-and-interop-testing.md)) appear in manifests or directories?

## How to help

- Draft a manifest format.
- Prototype a static directory built from manifests.

## References

- [OMA3 Inter-World Portaling System](https://github.com/oma3dao/iwps-specification)
