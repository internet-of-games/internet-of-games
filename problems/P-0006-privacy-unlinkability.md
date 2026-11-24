---
id: P-0006
title: Privacy and unlinkability across games
layer: identity
phase: 1
status: open
difficulty: high
champion: unassigned
related: [P-0003, P-0004, P-0007, P-0013, P-0017, P-0018, P-0023, P-0028]
last_reviewed: 2026-11-24
---

# P-0006: Privacy and unlinkability across games

**In one sentence:** a universal player identifier is also a universal tracking ID, so players need to show each game only what they choose, and stop games (and anyone those games share data with) from correlating them unless they opt in.

## Why it matters

- **Harassment:** a stalker or harasser shouldn't be able to follow someone from game to game.
- **Commercial tracking:** cross-game identifiers are valuable to data brokers.
- **Law:** data minimization and consent are legal requirements in many places, such as under the EU's GDPR ([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)), and children's data gets extra protection ([P-0007](P-0007-age-and-eligibility.md)).

At the same time, the [vision](../VISION.md) wants a *recognizable* persistent character. The answer has to be **player choice**, not a single global setting.

## What exists today

- **Selective disclosure:** SD-JWT ([RFC 9901](https://www.rfc-editor.org/rfc/rfc9901.html)) lets a holder reveal some claims and hide others.
- **Verifiable Credentials 2.0** ([W3C](https://www.w3.org/TR/vc-data-model-2.0/)) supports a range of signature and disclosure methods.
- **Per-relationship identifiers:** using a different identifier for each game is a well-known technique in identity systems.
- **Status lists with herd privacy:** checking whether a credential has been revoked doesn't reveal *which* credential is being checked ([Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/)).

## Two modes the player chooses between, per game

| Mode | What games see | Good for |
|---|---|---|
| **Public persona** | The same identifier, name and look everywhere | Streamers, social and roleplay play, being "the same character" |
| **Private** | A different identifier per game, and only the claims the player chooses | Everyone else, by default |

## A subtle risk: the avatar is a fingerprint

Even with separate identifiers, **an identical avatar file or hash** in two games could link a player. Mitigations to explore: re-encoding avatars per game, not exposing raw hashes to other players, and letting players use different avatars in private mode.

## Constraints

- **Private by default** ([design principle 6](../docs/design-principles.md#6-private-by-default)).
- **No personal data in test vectors** or demos; synthetic data only.
- **Telemetry and analytics** in the reference SDK are off by default.

## What "solved enough" looks like (Phase 1)

- [ ] A privacy design document covering both modes and the threats each faces
- [ ] The demos support public-persona and private modes
- [ ] Selective disclosure demonstrated: Game B sees only the credential the player chose
- [ ] Documented mitigations for avatar-based correlation

## Candidate directions

1. **Per-game identifiers derived from one master key**, with proofs of common ownership shown only on request.
2. **SD-JWT credentials** for selective disclosure in Phase 1, tracking newer unlinkable signature schemes for later.
3. **A minimal disclosure UI pattern** that the SDK provides, so every game shows consent the same way.

## Threats

Threat IDs refer to the [threat model](../docs/threat-model.md). Public-persona mode accepts some linking by design; private mode has to resist it.

| Threat | In private mode | Mitigations to explore |
|---|---|---|
| Harassment that follows a player (T1) | A harasser has to link the player through other signals. In public-persona mode the player is recognizable everywhere by choice | Private by default; switching any game to private at any time; portable blocks ([P-0018](P-0018-friends-and-presence.md)); no presence by default |
| Linking by identifier (T3) | Defeated if each game gets a different identifier | Per-game identifiers that can't be compared (direction 1) |
| Linking by credential (T3) | The same signed credential shown in two games links them, even if no claim is disclosed. With salted-hash selective disclosure such as SD-JWT, games that compare notes can always tell they saw the same credential ([RFC 9901, section 10.1](https://www.rfc-editor.org/rfc/rfc9901.html#section-10.1)) | Batch issuance: a separate copy of each credential for each game, with fresh keys and salts ([RFC 9901, section 10.1](https://www.rfc-editor.org/rfc/rfc9901.html#section-10.1)). Unlinkable signature schemes later |
| Linking through the issuer (T3) | An issuer that learns where its credentials are presented can follow the player. SD-JWT can't stop this if a game forwards the presentation to the issuer ([RFC 9901, section 10.1](https://www.rfc-editor.org/rfc/rfc9901.html#section-10.1)) | Offline verification, so issuers aren't contacted when a credential is shown, and status lists downloaded whole ([P-0015](P-0015-issuer-trust-revocation.md)) |
| Linking by status-list position (T3) | A credential's position in a status list is the same in every game it's shown to | Per-game credential copies, each with its own position |
| Linking by avatar file (T3) | An identical file or hash in two games links them (P-0006-Q3) | Re-encode avatars for each game, don't show hashes to other players, and allow a different avatar per mode |
| Linking by name and behavior (T3) | Display names, play times and habits can still link players | Per-game display names, coarse bands instead of exact numbers in claims ([P-0013](P-0013-portable-claims.md)), and clear warnings |
| What a claim reveals (T3) | Every claim names its issuer: showing "cleared the final boss in Game A" tells Game B the player plays Game A | Show players what each claim reveals before they share it |
| Analytics creep (T3) | Games build profiles from imported claims (P-0006-Q4) | Keep only what the game uses, and publish an analytics policy for integrators |

We can reduce correlation, not eliminate it; the threat model records that as residual risk for T3.

## Open questions

- **P-0006-Q1:** Should the default be private for everyone, or should it depend on the game's genre?
- **P-0006-Q2:** How much complexity does selective disclosure add for game developers?
- **P-0006-Q3:** How do we stop avatar files, display names or play patterns from linking a player who chose private mode?
- **P-0006-Q4:** What analytics is a game allowed to derive from imported claims?

## Champion brief

- **First deliverable:** A privacy design document covering the public-persona and private modes and the threats each one faces.
- **Decisions you'd drive:** the default mode (P-0006-Q1), how to stop avatars, names and play patterns from linking a player (P-0006-Q3), and what analytics games may derive (P-0006-Q4).
- **Helpful background:** privacy engineering, selective disclosure, and the basics of data-protection law.
- **Commitment:** a few hours a week, until a proposal is ready for public review.

## How to help

- Write the threat model for both modes.
- Prototype per-game identifier derivation and test it against correlation attacks.

## References

- [RFC 9901 (SD-JWT)](https://www.rfc-editor.org/rfc/rfc9901.html) · [VC Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) · [Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/)
- [GDPR (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
