---
id: P-0021
title: Platform-holder rules
layer: ownership
phase: 3
status: open
difficulty: high
champion: unassigned
related: [P-0002, P-0004, P-0017, P-0019, P-0020, P-0029, P-0030]
last_reviewed: 2026-11-15
---

# P-0021: Platform-holder rules

**In one sentence:** console makers and mobile app stores control identity, payments and certification on their platforms, so anything that touches purchases, accounts or links there has to fit their rules.

## Why it matters

Most players in the biggest games play on consoles or phones. Platform holders have blocked cross-platform features before. Cross-play itself only opened up in 2018, and court documents later showed a royalty policy tied to it ([PC Gamer](https://www.pcgamer.com/sony-charges-for-crossplay-support-to-protect-psn-revenue-documents-show)).

## What exists today

- **Epic Online Services** shows that cross-platform account and friend services can work across major platforms and stores ([Epic](https://onlineservices.epicgames.com/)).
- **Much platform policy is confidential**, available only to licensed developers under non-disclosure agreements.

## Approach

1. **Phases 1 and 2 target web, PC and mobile web**, where the rules are open.
2. **The core (identity, appearance and claims) doesn't need platform permission.** A console game could read a passport through ordinary account linking, a QR code or a companion app.
3. **Purchases and entitlements will need platform cooperation**, so we gather requirements before designing them.
4. **Engage platform holders later**, using working demos as evidence.

## Constraints

- **Contributors must never share confidential platform material** in this repository ([CONTRIBUTING.md](../CONTRIBUTING.md)).
- **Design for "works without platform cooperation"**, then for "works better with it".

## What "solved enough" looks like (Phase 3)

- [ ] A public summary of the platform policies relevant to identity, linking and entitlements, from public sources only
- [ ] A console-friendly passport flow (QR code or companion app) prototyped on a platform where that's allowed
- [ ] A conversation started with at least one platform holder

## Open questions

- **P-0021-Q1:** Which public platform policies affect identity linking and cross-game rewards?
- **P-0021-Q2:** What's the best way to get a passport into a console game: a QR code, a companion app or account linking?
- **P-0021-Q3:** Do cross-game reward offers count as purchases in store terms ([P-0019](P-0019-cross-game-entitlements.md))?
- **P-0021-Q4:** How can we learn from licensed developers without them breaking their agreements?

## How to help

- Summarize public store policies relevant to digital goods and account linking, citing sources.
- Prototype a QR-code passport flow.

## References

- [interop-history.md](../docs/interop-history.md) · [legal-and-policy.md §7](../docs/legal-and-policy.md#7-platform-rules)
