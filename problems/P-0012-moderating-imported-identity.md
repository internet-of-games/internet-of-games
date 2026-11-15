---
id: P-0012
title: Moderating imported names and avatars
layer: appearance
phase: 2
status: open
difficulty: high
champion: unassigned
related: [P-0010, P-0011, P-0016]
last_reviewed: 2026-11-15
---

# P-0012: Moderating imported names and avatars

**In one sentence:** when a player arrives from another game, the receiving game still has to apply its own rules on names, avatars and behavior, quickly and fairly.

## Why it matters

Every game that shows user-created content takes responsibility for it. Imported names and avatars come from outside a game's own creator tools and filters, so they arrive unchecked. Without moderation hooks, no responsible game can accept them.

## What exists today

- **Each platform moderates its own user content** with its own tools and staff.
- **Hash matching** can catch known-illegal content.
- **Legal frameworks** for hosted content include notice-and-takedown (U.S. DMCA section 512) and the EU Digital Services Act's obligations for online platforms ([U.S. Copyright Office](https://www.copyright.gov/512/); [European Commission](https://digital-strategy.ec.europa.eu/en/policies/digital-services-act-package)).

## Constraints

- **The receiving game always has the final say**, and can replace a name or avatar locally.
- **Tell the player** what happened and why ("your avatar was replaced here because…").
- **A way to appeal.**
- **No cross-game punishment by default.** One game's moderation decision doesn't follow the player elsewhere ([P-0016](P-0016-portable-reputation.md)).

## What "solved enough" looks like (Phase 2)

- [ ] SDK hooks: a name-check callback, an avatar review queue, a local nickname override, and a fallback avatar
- [ ] A moderation guidance document for integrators
- [ ] A demo showing an imported avatar being held for review while a fallback is shown

## Candidate directions

1. **Treat names as display-only**, re-checked locally against each game's own rules (profanity, impersonation, uniqueness).
2. **Hold for review.** A new avatar is shown only to its owner until it passes local checks.
3. **Shared, opt-in hash lists** for content that is illegal everywhere, run through established industry and legal processes, not by this project.

## Open questions

- **P-0012-Q1:** Is there a safe way for games to share signals about known-bad files without creating unaccountable blacklists?
- **P-0012-Q2:** How should names in many scripts, and lookalike characters, be handled ([OQ-10](../docs/open-questions.md#people-and-safety))?
- **P-0012-Q3:** How should appearance descriptors be moderated ([P-0009](P-0009-cross-style-translation.md))?
- **P-0012-Q4:** How is liability split between the player, the issuing game and the receiving game?

## How to help

- Trust and safety professionals: review this doc.
- Design the SDK hook interfaces.

## References

- [U.S. Copyright Office: section 512](https://www.copyright.gov/512/)
- [EU Digital Services Act](https://digital-strategy.ec.europa.eu/en/policies/digital-services-act-package)
