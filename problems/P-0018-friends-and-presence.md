---
id: P-0018
title: Portable friends, blocks and presence
layer: presence
phase: 3
status: open
difficulty: high
champion: unassigned
related: [P-0006, P-0016, P-0017]
last_reviewed: 2026-11-15
---

# P-0018: Portable friends, blocks and presence

**In one sentence:** players want to find their friends in whatever game they're playing, and keep away the people they've blocked, but today friends lists and block lists live inside each platform.

## Why it matters

Social connection is a big part of why people play together, and safety tools only work if they follow the player. A block that doesn't travel stops protecting you the moment you change games.

## What exists today

- **Platform friends lists** (console networks, Steam, Epic and others). Epic Online Services can merge a player's Steam and Epic Games Store friends into a single list ([Epic news](https://onlineservices.epicgames.com/news/epic-online-services-release-free-pc-crossplay-tools)).
- **Federated social protocols:** [ActivityPub](https://www.w3.org/TR/activitypub/) (W3C Recommendation, 2018), [Matrix](https://spec.matrix.org/latest/) and the [AT Protocol](https://atproto.com/).
- **Third Room** tried using Matrix as the social layer for worlds. Its repository has been dormant since 2023 ([GitHub](https://github.com/matrix-org/thirdroom)).

## Constraints

- **Presence reveals location and activity**, so it's off by default and shared per friend.
- **Children** need extra protection and guardian controls.
- **Blocks should be enforceable** without revealing the block list to the blocked person.

## Idea: blocks before friends

A **portable block list** is low-risk and high-value. The player carries their own list, games enforce it locally, and nobody else is judged publicly. It could ship before friends and presence.

## What "solved enough" looks like (Phase 3)

- [ ] A portable block list format, honored by both demo games
- [ ] An opt-in friend connection that both players confirm
- [ ] A privacy review of presence sharing

## Candidate directions

1. **Use an existing federated protocol** (Matrix, ActivityPub or the AT Protocol) for friends and invites, keyed to passport identifiers.
2. **Player-held connection credentials**, where a friendship is a pair of signed statements held by the two players.
3. **Leave friends to platforms** and only do portable blocks.

## Open questions

- **P-0018-Q1:** Which protocol, if any, should we build on?
- **P-0018-Q2:** How can games enforce portable blocks without learning more than they need?
- **P-0018-Q3:** What should presence defaults be for minors?
- **P-0018-Q4:** How does this relate to per-game private identifiers ([P-0006](P-0006-privacy-unlinkability.md))?

## How to help

- Compare the three protocols for gaming use cases.
- Design the block list format and its privacy properties.

## References

- [ActivityPub](https://www.w3.org/TR/activitypub/) · [Matrix](https://spec.matrix.org/latest/) · [AT Protocol](https://atproto.com/)
