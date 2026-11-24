---
id: P-0003
title: A player identifier that no single company owns
layer: identity
phase: 1
status: open
difficulty: medium
champion: unassigned
related: [P-0004, P-0005, P-0006, P-0024]
last_reviewed: 2026-11-24
---

# P-0003: A player identifier that no single company owns

**In one sentence:** games need a stable way to recognize "the same player" that doesn't depend on any one company's account system staying online, in business or friendly.

## Why it matters

Today the only identities that span games are platform accounts (PlayStation, Xbox, Nintendo, Steam, Epic), and each belongs to its platform. When an identity service shuts down, everything that depended on it breaks, as happened with Ready Player Me in January 2026 ([prior-art.md](../docs/prior-art.md#ready-player-me)).

## What exists today

| Option | How it works | Strengths | Weaknesses |
|---|---|---|---|
| Platform accounts | A company-issued account ID | Familiar, already integrated | Owned by the platform; can't be verified elsewhere |
| [DID 1.0](https://www.w3.org/TR/did-1.0/) / [DID 1.1](https://www.w3.org/TR/did-1.1/) | A W3C standard data model for identifiers controlled by keys | Neutral, standard (1.0 has been a Recommendation since 2022; 1.1 is a Candidate Recommendation as of March 2026) | Players must never have to see or manage keys |
| `did:key` | The identifier *is* a public key | No hosting needed; simplest | Keys can't be rotated, so a lost key means a lost identity |
| `did:web` | The identifier resolves to a document on a web domain | Simple and familiar | Whoever controls the domain controls the identity |
| [`did:webvh`](https://identity.foundation/didwebvh/v1.0/) | `did:web` plus a verifiable history log | Key rotation, can move hosts, auditable history | Still needs some host |
| [`did:plc`](https://github.com/did-method-plc/did-method-plc) | Signed operations recorded in a directory | Used for every Bluesky account; supports rotation and migration | One directory today, now moving to an independent organization ([AT Protocol blog](https://atproto.com/blog/plc-directory-org)) |

The methods differ in the signatures a game must verify: `did:webvh` 1.0 requires Ed25519, and `did:plc` uses secp256k1 or P-256 keys. Which of those each engine can verify without extra libraries is in a [spike](../docs/spikes/2026-11-24-signature-support-in-engines.md).

## Constraints

- **Ordinary players never handle raw keys** ([P-0005](P-0005-key-recovery.md)).
- **It must work offline**, or with cached data, for verification.
- **It must support key rotation and recovery** without changing the identifier.
- **It must allow privacy:** different identifiers for different games when the player wants that ([P-0006](P-0006-privacy-unlinkability.md)).
- **No blockchain is required** ([design principle 10](../docs/design-principles.md#10-works-without-crypto-doesnt-forbid-it)).

## What "solved enough" looks like (Phase 1)

- [ ] One default DID method chosen, and an allow-list of others
- [ ] Documented key generation, storage, rotation and resolution
- [ ] Test vectors: valid, rotated, malformed and deactivated identifiers
- [ ] Both demo games resolve and recognize the same player identifier

## Candidate directions

1. **`did:webvh` by default.** Any "passport provider" can host it, players can self-host or switch providers, and the history makes rotations auditable.
2. **`did:plc` by default.** It's proven at consumer scale, but depends on one directory, even if that directory is independently run.
3. **`did:key` for Phase 1 only**, with a documented migration to (1) or (2). This is the fastest way to a working demo.
4. **Several methods behind one resolver library**, with games accepting any method on an allow-list.

## Open questions

- **P-0003-Q1:** Which method is the default for Phase 1, and which for production?
- **P-0003-Q2:** Who hosts identifiers for players who don't have their own domain, and how do they switch hosts?
- **P-0003-Q3:** Do we want human-readable handles (for example domain-based handles, as on Bluesky), and how do they relate to display names?
- **P-0003-Q4:** Do we need one global identifier at all, or only per-game identifiers plus proofs that they belong to the same player ([P-0006](P-0006-privacy-unlinkability.md))?

## Champion brief

- **First deliverable:** A comparison of `did:key`, `did:web`, `did:webvh` and `did:plc` against the constraints above, including which ones each target engine can verify, and how they relate to the identifiers in the Web of Worlds proposal ([comparison](../docs/spikes/2026-11-24-web-of-worlds-user-manifest.md)).
- **Decisions you'd drive:** the Phase 1 default and the path to production (P-0003-Q1), and hosting and switching hosts (P-0003-Q2).
- **Helpful background:** decentralized identifiers and key management, plus some experience with a game engine.
- **Commitment:** a few hours a week, until a proposal is ready for public review.

## How to help

- Build a comparison table of DID methods against the constraints above.
- Prototype resolving each method in GDScript and in TypeScript.
- Check which cryptographic algorithms each engine supports out of the box ([P-0025](P-0025-developer-adoption-cost.md)).

## Decisions so far

- [ADR-0004](../docs/decisions/ADR-0004-compose-existing-open-standards.md): we build on existing open standards (here, decentralized identifiers) rather than inventing a new identifier format.
- [ADR-0005](../docs/decisions/ADR-0005-never-require-blockchains-tokens-or-wallets.md): no blockchain, token or wallet may ever be required; identifier methods that use a ledger are allowed only as options.

## References

- [W3C DID 1.0](https://www.w3.org/TR/did-1.0/) · [DID 1.1](https://www.w3.org/TR/did-1.1/)
- [did:webvh v1.0](https://identity.foundation/didwebvh/v1.0/)
- [did:plc](https://github.com/did-method-plc/did-method-plc) · [PLC directory organization](https://atproto.com/blog/plc-directory-org)
