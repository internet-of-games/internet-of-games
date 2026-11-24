---
id: P-0020
title: Connected economies and value transfer
layer: ownership
phase: research
status: open
difficulty: research
champion: unassigned
related: [P-0002, P-0019, P-0021]
last_reviewed: 2026-11-24
---

# P-0020: Connected economies and value transfer

**In one sentence:** letting money or tradable value move between games is the most-requested and most dangerous feature, so we treat it as research until the legal, economic and safety questions have answers.

## Why it's research, not roadmap

| Risk | Evidence |
|---|---|
| **Publishers' revenue depends on closed economies** | 78% of Take-Two's FY2026 net bookings came from recurrent consumer spending, including virtual currency ([Take-Two](https://www.businesswire.com/news/home/20260521450562/en/Take-Two-Interactive-Software-Inc.-Reports-Results-for-Fourth-Quarter-and-Fiscal-Year-2026)) |
| **Currency doesn't cross even within one franchise** | NBA 2K's virtual currency doesn't carry over between editions; Take-Two calls virtual currencies "fictions" governed by its terms ([VGC](https://videogameschronicle.com/news/virtual-currencies-are-fictions-take-two-argues-in-microtransaction-theft-lawsuit); [Kotaku](https://kotaku.com/2k-forced-in-court-to-explain-why-nba-2k-players-cant-transfer-digital-currency-you-have-no-ownership-or-other-rights-to-virtual-items-2000736199)) |
| **Fraud and money laundering** | Valve restricted Counter-Strike key trading in 2019 because of fraud networks ([Engadget](https://www.engadget.com/2019-10-30-csgo-fraud-loot-box-key-trades.html)) |
| **Consumer protection** | EU principles on in-game virtual currencies (March 2025) and the proposed Digital Fairness Act (November 2026) ([European Commission](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/social-media-online-games-and-search-engines_en); [proposal](https://commission.europa.eu/document/download/0575d59f-554f-4a9e-b54b-e6b717175809_en?filename=Proposal+for+a+Digital+Fairness+Act.pdf)) |
| **Financial regulation** | The Digital Fairness Act proposal says currencies locked inside one game, with no cash value and no trading outside it, fall outside EU payment-services and crypto-asset rules ([proposal](https://commission.europa.eu/document/download/0575d59f-554f-4a9e-b54b-e6b717175809_en?filename=Proposal+for+a+Digital+Fairness+Act.pdf), recital 61). Currencies that cross games would give up those properties ([legal-and-policy §5](../docs/legal-and-policy.md#5-virtual-currencies-loot-boxes-and-consumer-protection)) |
| **Platform terms** | Platform holders set commercial terms for cross-platform revenue ([PC Gamer](https://www.pcgamer.com/sony-charges-for-crossplay-support-to-protect-psn-revenue-documents-show)) |
| **Tokens don't create demand** | Ubisoft's NFT items ended in 2022 ([PC Gamer](https://www.pcgamer.com/ubisoft-ends-its-nft-experiment-in-ghost-recon-breakpoint-but-promises-theyre-coming-to-other-games)) |
| **Balance and inflation** | Every game's economy is tuned on its own terms ([why-not-yet §3](../docs/why-not-yet.md#3-the-economies-are-the-business)) |

## What is *not* research

Rewards granted by the receiving game ([P-0019](P-0019-cross-game-entitlements.md)) need no value transfer and are on the roadmap.

## Research questions

- **P-0020-Q1:** Is there any form of value movement that's safe, such as gifting a cosmetic with no resale, or one-way conversion into a non-tradable reward?
- **P-0020-Q2:** Would a neutral "clearing house" between games be regulated as a payment or e-money service? (This needs real legal input.)
- **P-0020-Q3:** How could subscription "world passes" split revenue between participating games **without a shared currency**, for example by engagement, as platforms already do with creators ([business-case.md](../docs/business-case.md))?
- **P-0020-Q4:** What did crypto-gaming experiments actually learn, good and bad, once the hype is set aside?

## How to help

- Economists and game designers: write short research notes on the questions above.
- Anyone: collect public post-mortems from games that tried to run shared or open economies.

## Decisions so far

- [ADR-0005](../docs/decisions/ADR-0005-never-require-blockchains-tokens-or-wallets.md): no blockchain, token or wallet may ever be required.
- [ADR-0008](../docs/decisions/ADR-0008-continuity-as-signed-claims-not-state.md): balance-affecting state isn't transferred directly. When cross-game value arrives, it builds on claims, starting with entitlements.

## References

- [legal-and-policy.md §5–6](../docs/legal-and-policy.md#5-virtual-currencies-loot-boxes-and-consumer-protection)
- [why-not-yet.md §3](../docs/why-not-yet.md#3-the-economies-are-the-business)
