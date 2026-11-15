---
id: P-0019
title: Cross-game rewards as entitlements
layer: ownership
phase: 2
status: open
difficulty: medium
champion: unassigned
related: [P-0011, P-0014, P-0020, P-0021]
last_reviewed: 2026-11-15
---

# P-0019: Cross-game rewards as entitlements

**In one sentence:** "do X in Game A, get Y in Game B" is valuable and legally simple if Game B *grants* Y based on a claim, rather than anything being transferred.

## Why it matters

Cross-game rewards are the most visible, most fun payoff of interoperability, and the most plausible business reason for a game to join ([P-0002](P-0002-why-would-a-game-join.md)). Framing them as **entitlements granted by the receiving game** avoids almost all the legal and economic problems of moving value ([P-0020](P-0020-connected-economies.md)).

## What exists today

- **LEGO styles in Fortnite** were granted free to people who owned the original outfits, all within one company ([PC Gamer](https://www.pcgamer.com/fortnite-is-adding-a-lego-themed-survival-crafting-mode-that-includes-lego-versions-of-over-1200-pre-existing-skins)).
- **Amiibo unlocks:** tapping a figure unlocks content defined by each game ([Nintendo FAQ](https://en-americas-support.nintendo.com/app/answers/detail/a_id/13260/p/603/c/947)).
- **Cross-promotions between games** are common commercially, but each one is a one-off business deal.

## A sketch: an "offer"

Game B publishes a rule:

> Holders of a credential of category *completed-main-story* from issuer *Game A* may claim the cosmetic *"Wanderer's Cloak"* once.

Game B records that the offer was redeemed, under its own identifier for the player, to prevent double-claiming.

## Constraints

- **No currency and no resale.** The item is Game B's own, granted under Game B's terms.
- **One redemption per player**, without tracking the player across games.
- **Clear disclosure** of what the player gets and on what terms. EU consumer rules on in-game purchases point this way ([European Commission](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/social-media-online-games-and-search-engines_en)).
- **Platform store rules** may treat some rewards as purchases ([P-0021](P-0021-platform-holder-rules.md)).

## What "solved enough" looks like (Phase 2)

- [ ] An offer format, with test vectors
- [ ] Demo Game B grants a cosmetic for a Game A credential, with protection against claiming it twice
- [ ] A disclosure guide for integrators

## Candidate directions

1. **Offers as local configuration** in each game, using the rule format from [P-0014](P-0014-claim-interpretation.md).
2. **Published offers** that discovery services can list ([P-0027](P-0027-discovery.md)).

## Open questions

- **P-0019-Q1:** How can double redemption be prevented without a global player ID?
- **P-0019-Q2:** If the original item was *purchased* in Game A, does a reward in Game B count as a purchase under platform rules?
- **P-0019-Q3:** What disclosures are needed in different regions?
- **P-0019-Q4:** What happens to earned rewards when Game B shuts down ([P-0024](P-0024-durability-when-services-die.md))?

## How to help

- Design the offer format.
- Collect public examples of cross-game promotions and how they were run.

## References

- [portability-matrix.md](../docs/portability-matrix.md) · [legal-and-policy.md](../docs/legal-and-policy.md)
