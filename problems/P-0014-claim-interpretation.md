---
id: P-0014
title: How a receiving game interprets foreign claims
layer: history
phase: 1
status: open
difficulty: medium
champion: unassigned
related: [P-0013, P-0015, P-0019, P-0022]
last_reviewed: 2026-11-15
---

# P-0014: How a receiving game interprets foreign claims

**In one sentence:** proving that a player did something in Game A is useless unless Game B has a simple, safe way to decide what that means locally.

## Why it matters

This is where "claims, not state" ([design principle 2](../docs/design-principles.md#2-claims-not-state)) turns into gameplay. Without interpretation, a verified claim is just a badge nobody looks at.

## What exists today

- **Amiibo.** Each game decides what a figure does: an outfit, an item, a character, or nothing at all ([Nintendo FAQ](https://en-americas-support.nintendo.com/app/answers/detail/a_id/13260/p/603/c/947)).
- **Skylanders.** Older games cap imported levels at their own limits ([Skylanders Wiki](https://skylanderswiki.com/wiki/Console_Stats)).
- **Pokémon HOME.** Creatures move only between compatible games, and only into games that support them ([Pokémon HOME](https://home.pokemon.com/en-us/); [VGC](https://www.videogameschronicle.com/guide/pokemon-home-scarlet-and-violet-compatibility-when-does-it-go-live)).

## A sketch: interpretation rules are local configuration

```text
when credential.issuer == did:web:game-a.example
 and credential.category == "completed-main-story"
then grant local title "Veteran of Game A"
     and unlock NPC greeting "veteran"
```

Optionally, issuers could publish hints such as difficulty or rarity ("3% of players"). Receiving games are free to ignore them.

A fuller sketch, comparing fixed-shape rules with a general expression language and including offers and examples, is in a [spike](../docs/spikes/2026-11-24-claim-interpretation-rules.md).

## Constraints

- **The receiving game always decides.** Nothing is obligatory.
- **By default, effects are cosmetic, social or narrative**, not gameplay power (to keep things fair; see [why-not-yet §5](../docs/why-not-yet.md#5-game-design-doesnt-transfer)).
- **The player chooses which claims to present** ([P-0006](P-0006-privacy-unlinkability.md)).

## What "solved enough" looks like (Phase 1)

- [ ] A simple, declarative rule format (JSON) plus an SDK helper
- [ ] Demo Game B maps a Game A credential to a local title
- [ ] A guide on fair interpretation: what to do and what to avoid

## Candidate directions

1. **Per-game rule files**, with matching by issuer and category.
2. **Shared categories** ([P-0013](P-0013-portable-claims.md)-Q2), so that "any final-boss clear from any trusted issuer" rules are possible.
3. **Narrative templates**, so characters can mention what you did elsewhere ("I heard you took down the Warden in Game A").

## Open questions

- **P-0014-Q1:** Should issuers publish rarity and difficulty metadata, and could it be gamed?
- **P-0014-Q2:** How could non-player characters reference foreign achievements naturally, and in many languages?
- **P-0014-Q3:** Should players be able to hide a claim *after* presenting it?
- **P-0014-Q4:** Do we need a shared category vocabulary in Phase 1, or only issuer-specific rules?

## Champion brief

- **First deliverable:** A small JSON rule format, with examples for games in different genres.
- **Decisions you'd drive:** whether Phase 1 needs a shared category vocabulary (P-0014-Q4) and whether issuers publish rarity (P-0014-Q1).
- **Helpful background:** game design, especially progression and rewards.
- **Commitment:** a few hours a week, until a proposal is ready for public review.

## How to help

- Propose rule-format examples for different genres.
- Collect interesting existing examples where one game recognizes progress from another.

## Decisions so far

- [ADR-0008](../docs/decisions/ADR-0008-continuity-as-signed-claims-not-state.md): continuity travels as signed claims, and each receiving game interprets them under its own rules.

## References

- [prior-art.md](../docs/prior-art.md) · [portability-matrix.md](../docs/portability-matrix.md)
