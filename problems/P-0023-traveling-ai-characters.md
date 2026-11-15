---
id: P-0023
title: AI characters that travel between games
layer: world
phase: research
status: open
difficulty: research
champion: unassigned
related: [P-0006, P-0011, P-0022]
last_reviewed: 2026-11-15
---

# P-0023: AI characters that travel between games

**In one sentence:** could an AI companion, one that remembers your adventures, follow you from game to game, and if so, who would own it, run it and keep it safe?

## Why it matters

The [vision](../VISION.md) imagines worlds that remember what players do. A companion character with shared memory is one of the most compelling ways continuity could *feel* real.

## The hard parts

| Issue | Why it's hard |
|---|---|
| **Memory** | What does the companion remember, in what format, and who holds it? Memories are personal data ([P-0006](P-0006-privacy-unlinkability.md)). |
| **Consistency** | Different games use different AI models. Can a personality description produce a recognizably similar character in each? |
| **Safety** | Behavior that's fine in a game for adults isn't fine in one rated for everyone ([P-0007](P-0007-age-and-eligibility.md)). |
| **Cost** | Someone pays for running the model. Is it the player, the game or a subscription? |
| **Rights** | Voices, likenesses and personas may belong to someone ([P-0011](P-0011-rights-licensing-likeness.md)). |
| **Consent and deletion** | Players must be able to see, edit and delete what a companion "knows". |

## A starting idea

- A **companion profile** held by the player: a persona description, appearance (as for player avatars) and **memory summaries** stored as player-held claims. Never raw chat logs by default.
- Each game runs the companion with **its own** model and **its own** content rules, using the profile as guidance. That's the same "the receiving game decides" principle used everywhere else.

## Research questions

- **P-0023-Q1:** What should a portable memory format look like?
- **P-0023-Q2:** How do consent, review and deletion work for companion memories?
- **P-0023-Q3:** How should behavior adapt to each game's age rating?
- **P-0023-Q4:** Who pays for running the model, and how do players avoid being locked into one provider?

## How to help

- Write short research notes on any of the questions above.
- Prototype a companion profile and test it across two different AI models.

## References

- [VISION.md §4](../VISION.md#4-why-ai-matters)
