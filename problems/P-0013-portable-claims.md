---
id: P-0013
title: Portable achievement and history claims
layer: history
phase: 1
status: open
difficulty: medium
champion: unassigned
related: [P-0006, P-0014, P-0015, P-0022, P-0024]
last_reviewed: 2026-11-24
---

# P-0013: Portable achievement and history claims

**In one sentence:** a game needs a standard way to say "this player did X here", signed so that any other game can check it without contacting the issuing game.

## Why it matters

This is the core of "meaningful continuity" in the [problem statement](../docs/problem-statement.md). Today's platform achievements (Xbox, PlayStation, Steam and similar) are real history, but they're locked to their platform and can't be verified anywhere else.

## What exists today

- **The W3C Verifiable Credentials Data Model 2.0** (Recommendation, May 2025) provides a standard signed envelope for claims ([W3C](https://www.w3.org/TR/vc-data-model-2.0/)).
- **Open Badges 3.0** (1EdTech) already defines an `AchievementCredential` built on Verifiable Credentials 2.0, with an issuer, a description, criteria, an image and evidence ([1EdTech](https://www.imsglobal.org/spec/ob/v3p0)). It was designed for education, but the shape fits games closely.
- **SD-JWT** ([RFC 9901](https://www.rfc-editor.org/rfc/rfc9901.html)) allows selective disclosure. An SD-JWT-based credential format is going through the IETF ([draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/)).
- **OpenID4VCI 1.0** (Final, September 2025) defines how an issuer delivers a credential to a holder ([OpenID](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)).

## A sketch of a game achievement credential

- **Issuer:** the game's identifier (for example a `did:web` on the studio's domain)
- **Subject:** the player's identifier for that game (which may be pairwise, see [P-0006](P-0006-privacy-unlinkability.md))
- **Achievement:** an ID, a localizable name and description, a criteria description and an optional image
- **Category (optional):** from a small shared list, such as "completed main story", "reached max level" or "won a season"
- **Bands, not exact numbers:** "top 10%" rather than "rank 4,512"
- **Issued and valid dates; status-list entry** for revocation ([P-0015](P-0015-issuer-trust-revocation.md))

## Constraints

- **Verification works offline** with cached issuer keys.
- **Small:** fits comfortably in a QR code or a deep link where possible.
- **Selective disclosure:** the player chooses which credentials to show ([P-0006](P-0006-privacy-unlinkability.md)).
- **No personal data** beyond what the claim needs.
- **Localizable** names and descriptions.

## What "solved enough" looks like (Phase 1)

- [ ] "Achievement Credential v0": a profile of Open Badges 3.0 *or* SD-JWT credentials, with examples
- [ ] Valid, expired, revoked and forged test vectors
- [ ] Demo Game A issues a credential, and demo Game B verifies it offline

## Candidate directions

1. **A strict profile of Open Badges 3.0.** It reuses an existing standard and tools, but brings JSON-LD complexity.
2. **SD-JWT credentials** with our own small schema. Simpler for game developers and selective disclosure is built in, but it's less standard for achievements.
3. **Support both**, with a mapping between them. More work, but the widest compatibility.

A [comparison of the formats](../docs/spikes/2026-11-24-credential-formats.md), with measured sizes, suggests SD-JWT credentials with ES256 for Phase 1, using Open Badges 3.0's achievement vocabulary so a mapping stays easy.

## Open questions

- **P-0013-Q1:** Open Badges 3.0 as is, or a lighter SD-JWT-based profile?
- **P-0013-Q2:** Should there be a shared achievement category list, and who maintains it?
- **P-0013-Q3:** How should playtime and skill be expressed without enabling profiling?
- **P-0013-Q4:** Should images be embedded (durable but larger) or linked (smaller but can break)?

## Champion brief

- **First deliverable:** Example achievement credentials for made-up games, written in both candidate formats and compared side by side.
- **Decisions you'd drive:** Open Badges 3.0 or SD-JWT credentials (P-0013-Q1), a shared category list (P-0013-Q2) and embedded or linked images (P-0013-Q4).
- **Helpful background:** W3C Verifiable Credentials, JSON-LD or JWT tooling, and game achievement systems.
- **Commitment:** a few hours a week, until a proposal is ready for public review.

## How to help

- Map Open Badges 3.0 fields onto typical game achievements.
- Write example credentials for three made-up games in different genres.

## Decisions so far

- [ADR-0004](../docs/decisions/ADR-0004-compose-existing-open-standards.md): we build on existing credential standards rather than a new format.
- [ADR-0008](../docs/decisions/ADR-0008-continuity-as-signed-claims-not-state.md): continuity travels as signed claims that receiving games interpret, not as transferred game state.

## References

- [VC Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) · [Open Badges 3.0](https://www.imsglobal.org/spec/ob/v3p0) · [RFC 9901](https://www.rfc-editor.org/rfc/rfc9901.html) · [OpenID4VCI 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)
