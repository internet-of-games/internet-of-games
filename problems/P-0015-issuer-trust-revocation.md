---
id: P-0015
title: Trusting issuers, revocation and cheating
layer: history
phase: 1
status: open
difficulty: high
champion: unassigned
related: [P-0013, P-0014, P-0024, P-0026]
last_reviewed: 2026-11-15
---

# P-0015: Trusting issuers, revocation and cheating

**In one sentence:** a signature proves who issued a claim, not whether that issuer is honest, so receiving games need a way to decide which games to trust, and issuers need a way to revoke claims that were obtained by cheating.

## Why it matters

- **Achievement mills.** Anyone can make a "game" that hands out impressive credentials.
- **Cheating and account boosting.** Players can buy or cheat their way to achievements.
- **Fraud follows value.** Valve restricted Counter-Strike key trading in 2019 because of fraud networks ([Engadget](https://www.engadget.com/2019-10-30-csgo-fraud-loot-box-key-trades.html)).

## What exists today

- **Bitstring Status List 1.0** (W3C Recommendation, May 2025) lets issuers revoke or suspend credentials. Verifiers download a compressed list, which hides *which* credential they're checking ([W3C](https://www.w3.org/TR/vc-bitstring-status-list/)).
- **Domain-bound identifiers** (`did:web`, `did:webvh`) tie an issuer to a web domain the studio controls ([did:webvh](https://identity.foundation/didwebvh/v1.0/)).
- **Trust lists** are a common pattern in identity systems: a verifier accepts issuers on a list it chooses.

## Constraints

- **No central gatekeeper is required.** Each game chooses whom to trust.
- **Works offline** with cached status lists, within documented freshness limits.
- **Checking status doesn't reveal the player** to the issuer.
- **Issuer key compromise** has a documented recovery path.

## What "solved enough" looks like (Phase 1)

- [ ] Demo Game B uses a local allow-list of issuers
- [ ] Revocation demonstrated with a status list: issue, revoke, then fail verification
- [ ] A documented cache freshness policy
- [ ] An issuer key-compromise scenario documented and tested

## Candidate directions

1. **Local allow-lists only** for Phase 1.
2. **Community-curated issuer registries**, possibly several competing ones, listing games that pass conformance ([P-0026](P-0026-conformance-and-interop-testing.md)).
3. **Reputation for issuers**, weighted by how many trusted games accept them.

## Open questions

- **P-0015-Q1:** Should there be a public issuer registry, and who runs it?
- **P-0015-Q2:** How do we stop achievement mills without blocking new indie games?
- **P-0015-Q3:** How fresh does a cached status list need to be?
- **P-0015-Q4:** What happens to credentials when an issuer's key is compromised, or when the issuer shuts down ([P-0024](P-0024-durability-when-services-die.md))?

## How to help

- Prototype status-list issuance and checking in the demo stack.
- Write the threat model for achievement mills and boosting.

## References

- [Bitstring Status List 1.0](https://www.w3.org/TR/vc-bitstring-status-list/) · [did:webvh v1.0](https://identity.foundation/didwebvh/v1.0/)
