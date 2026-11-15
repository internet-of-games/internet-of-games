---
id: P-0007
title: Age and eligibility signals across games
layer: identity
phase: 2
status: open
difficulty: high
champion: unassigned
related: [P-0005, P-0006, P-0012]
last_reviewed: 2026-11-15
---

# P-0007: Age and eligibility signals across games

**In one sentence:** games with different age ratings and legal duties need to know "is this player old enough, and allowed here?" without learning who the player is or when they were born.

## Why it matters

Ratings vary widely, even within one publisher: NBA 2K26 is rated E (Everyone) and Grand Theft Auto VI is rated M (Mature 17+) ([ESRB: NBA 2K26](https://www.esrb.org/ratings/40735/nba-2k26/); [ESRB: GTA VI](https://www.esrb.org/ratings/41627/grand-theft-auto-vi/)). A connected network of games has to keep younger players out of mature spaces and meet children's privacy rules, such as the amended U.S. COPPA Rule ([Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-publishes-final-coppa-rule-amendments)). Without portable age signals, every game repeats its own invasive checks, or skips them.

## What exists today

- **EU age verification.** The European Commission declared its privacy-preserving age-verification solution ready and urged every member state to offer one by 31 December 2026 ([European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-urges-member-states-rollout-eu-age-verification-app)).
- **EU Digital Identity Wallets**, which member states are due to offer by around the end of 2026 ([Inside Privacy](https://www.insideprivacy.com/minors/eu-sets-the-clock-on-age-verification-rollout-urged-by-end%E2%80%912026/)).
- **Mobile driving licences (ISO/IEC 18013-5)**, which can prove an age threshold without revealing a birthdate.
- **Selective disclosure** with SD-JWT ([RFC 9901](https://www.rfc-editor.org/rfc/rfc9901.html)) and presentation with OpenID4VP ([OpenID](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)).

## Constraints

- **Predicates only:** "over 13", "over 16" or "over 18". Never a birthdate.
- **Configurable trust:** each game decides which issuers it accepts (government wallets, parents, platforms or other games).
- **Children shouldn't need government ID.** Guardian-issued signals have to be possible.
- **Rules differ by region.** The signal format has to work everywhere, even though the legal requirements don't match.

## What "solved enough" looks like (Phase 2)

- [ ] An age-predicate credential profile, with test vectors
- [ ] The demo games accept age predicates from a configurable list of trusted issuers, including a mock issuer for testing
- [ ] A guardian-managed flow for minors, documented and demonstrated

## Candidate directions

1. **Accept existing government-grade age credentials** (EU age verification, digital identity wallets, mobile licences) wherever they're available.
2. **Guardian-issued credentials** for minors, linked to [P-0005](P-0005-key-recovery.md).
3. **Game-issued "verified" signals** that other games may choose to trust (see P-0007-Q3).

## Open questions

- **P-0007-Q1:** Which age thresholds should the profile include?
- **P-0007-Q2:** How should guardian-managed child passports work ([OQ-9](../docs/open-questions.md#people-and-safety))?
- **P-0007-Q3:** Can a game's own age check be reused by another game? What trust and liability does that imply?
- **P-0007-Q4:** How do we handle regions with conflicting legal requirements?

## How to help

- Map current age-assurance requirements by region (from public sources only).
- Test the EU age-verification solution's developer materials once they're available.

## References

- [European Commission: age verification rollout](https://digital-strategy.ec.europa.eu/en/news/commission-urges-member-states-rollout-eu-age-verification-app)
- [ESRB rating pages: NBA 2K26](https://www.esrb.org/ratings/40735/nba-2k26/) · [GTA VI](https://www.esrb.org/ratings/41627/grand-theft-auto-vi/)
