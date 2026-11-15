---
id: P-0017
title: World-to-world handoff
layer: presence
phase: 2
status: open
difficulty: medium
champion: unassigned
related: [P-0006, P-0021, P-0027, P-0029]
last_reviewed: 2026-11-15
---

# P-0017: World-to-world handoff

**In one sentence:** going from Game A to Game B should feel like stepping through a door, with Game B knowing who's arriving, from where, and what they chose to bring, even though the two games share no servers.

## Why it matters

"Travel between worlds" is central to the [vision](../VISION.md). Without a handoff, moving between games means quitting one, launching the other and logging in again as a stranger.

## What exists today

- **OMA3's Inter-World Portaling System** is a draft specification for moving users between virtual worlds, published for comment in 2024. Its repository was last updated in September 2025 ([specification](https://github.com/oma3dao/iwps-specification); [Metaverse Standards Forum liaison](https://metaverse-standards.org/news/blog/metaverse-standards-forum-enters-liaison-agreement-with-oma3/)).
- **Deep links and URL schemes** on the web and on mobile and desktop operating systems.
- **Platform invite systems**, each tied to its own platform.

## A sketch: a signed, short-lived "handoff ticket"

A ticket contains:

- a reference to the player's passport (possibly a per-game identifier)
- the credentials the player chose to bring
- the origin game, and an optional *intent*, such as "arrive at the stadium" or "continue the story"
- an expiry time and a one-time number to prevent replay
- the destination: a world address, and optionally a place inside that world ([P-0029](P-0029-world-addressing-and-links.md))

It's delivered as a link or deep link. Game B verifies it and greets the player. If Game B isn't installed, the link falls back to a store or web page.

## Constraints

- **No server-to-server dependency** between the games.
- **Replay protection** and short expiry.
- **Privacy:** only what the player chose is shared ([P-0006](P-0006-privacy-unlinkability.md)).
- **Works when the target isn't installed.**
- **Abuse prevention:** no spammy auto-portals.

## What "solved enough" looks like (Phase 2)

- [ ] A handoff ticket format, with test vectors
- [ ] In the demo, walking through a portal in Game A opens Game B with a personalized welcome
- [ ] An analysis of how this relates to OMA3's draft specification

## Candidate directions

1. **Align with OMA3's portaling draft**, contributing feedback upstream.
2. **A minimal ticket on top of OpenID4VP**, treating the handoff as a presentation.
3. **A plain signed JSON ticket** inside a deep link. Simplest for Phase 2.

## Open questions

- **P-0017-Q1:** Should we align with, extend or simply learn from OMA3's portaling draft?
- **P-0017-Q2:** What deep-linking options exist on consoles ([P-0021](P-0021-platform-holder-rules.md))?
- **P-0017-Q3:** What arrival context is useful without being invasive?
- **P-0017-Q4:** How do we stop handoffs being used for spam or phishing?

## How to help

- Read the OMA3 draft and summarize what's reusable.
- Prototype a deep-link handoff between two web games.

## References

- [OMA3 Inter-World Portaling System](https://github.com/oma3dao/iwps-specification)
- [OpenID4VP 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)
