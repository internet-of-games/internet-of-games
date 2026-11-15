---
id: P-0002
title: Why would a game join?
layer: governance
phase: 0
status: open
difficulty: high
champion: unassigned
related: [P-0001, P-0019, P-0020, P-0021, P-0025, P-0028, P-0030]
last_reviewed: 2026-11-15
---

# P-0002: Why would a game join?

**In one sentence:** nobody adopts a standard because it's elegant, so we need a concrete, evidence-backed answer to "what does my game get, and what does it cost?"

## Why it matters

Large publishers profit from keeping players inside their own ecosystems. Take-Two, for example, made 78% of its net bookings from in-game spending in fiscal year 2026 ([Take-Two](https://www.businesswire.com/news/home/20260521450562/en/Take-Two-Interactive-Software-Inc.-Reports-Results-for-Fourth-Quarter-and-Fiscal-Year-2026)), and its CEO has argued that its online games already deliver the "metaverse" ([CNBC](https://www.cnbc.com/2021/11/04/take-two-ceo-strauss-zelnick-says-hes-skeptical-about-facebooks-metaverse.html)). Without a clear benefit, even sympathetic studios won't spend engineering time on interoperability. See [why-not-yet.md](../docs/why-not-yet.md).

## What exists today

- **Free identity infrastructure that serves a strategy.** Epic Online Services is free across engines and stores ([Epic](https://onlineservices.epicgames.com/)).
- **Platforms paying creators to attract content.** Roblox creators earned more than $1.5B in 2025, and Fortnite creators passed $1B in total by 2026 ([GamesBeat](https://gamesbeat.com/roblox-stock-rises-20-after-earnings-daily-active-users-up-69-in-q4/); [Tubefilter](https://www.tubefilter.com/2026/06/17/epic-games-unreal-editor-for-fortnite-creator-payouts/)).
- **Cross-game rewards that already work inside one company.** These include amiibo and LEGO styles in Fortnite ([prior-art.md](../docs/prior-art.md)).
- **The business-case hypotheses** in [business-case.md](../docs/business-case.md).

## Constraints

- The evidence must be honest, including results that don't support the idea.
- No game should have to share revenue data publicly. Use aggregates and voluntary interviews.

## What "solved enough" looks like (Phase 0 to 3)

- [ ] Phase 0: a written thesis listing hypotheses H1 to H6 from [business-case.md](../docs/business-case.md)
- [ ] Phase 1 and 2: measurements from the demo games (time to first play with and without an imported avatar, and so on)
- [ ] Phase 2: interviews with at least 10 developers across genres, summarized publicly
- [ ] Phase 3: a business-case brief good enough to bring to a mid-size studio

## Candidate directions

1. **Start where the incentives already line up:** indie, social, roleplay and sports-management games.
2. **Lead with low-risk value:** accessibility preferences ([P-0028](P-0028-portable-preferences.md)) and age signals ([P-0007](P-0007-age-and-eligibility.md)) help every game and threaten no one's store.
3. **Cross-promotion as the first visible payoff:** "bring your badge" campaigns ([P-0019](P-0019-cross-game-entitlements.md)).

## Open questions

- **P-0002-Q1:** Which genres benefit most? Sports sims, RPGs, social games, roleplay?
- **P-0002-Q2:** What paid services can exist around the standard without compromising its neutrality?
- **P-0002-Q3:** Would subscription "world passes" need a shared way to split revenue, and who would run it ([P-0020](P-0020-connected-economies.md))?
- **P-0002-Q4:** How do we measure onboarding gains ethically, without tracking players across games?

## How to help

- If you run a game, share (in aggregate) how many players drop off during character creation or onboarding.
- Draft an interview guide for developers.
- Collect public examples of cross-promotions between unrelated games, and what they achieved.

## Decisions so far

- [ADR-0003](../docs/decisions/ADR-0003-universal-scope-built-in-risk-order.md): the project's scope is a universal standard for every game, delivered in layers ordered by risk.

## References

- [business-case.md](../docs/business-case.md)
- [why-not-yet.md](../docs/why-not-yet.md)
