---
id: P-0004
title: Linking existing game accounts without a new account system
layer: identity
phase: 1
status: open
difficulty: medium
champion: unassigned
related: [P-0003, P-0006, P-0021]
last_reviewed: 2026-11-24
---

# P-0004: Linking existing game accounts without a new account system

**In one sentence:** games already have account systems and platform logins, so the passport has to *link* to them, without replacing them and without making players create yet another account.

## Why it matters

No game will rip out its account system to adopt a standard, and players won't welcome another password. Linking is how the passport fits into how games already work ([design principle 4](../docs/design-principles.md#4-link-accounts-dont-replace-them)).

## What exists today

- **OAuth 2.0 and OpenID Connect** are how most online services, games included, handle login ([OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html)).
- **Epic Online Services** is free, works with any engine and any combination of stores and platforms, and lets players find friends across PC stores ([Epic](https://onlineservices.epicgames.com/); [Epic news](https://onlineservices.epicgames.com/news/epic-online-services-release-free-pc-crossplay-tools)). It shows that cross-store identity works, but within one company's service.
- **OpenID for Verifiable Presentations 1.0** (Final, July 2025) defines how a holder presents credentials to a verifier ([OpenID4VP](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)).
- **The W3C Digital Credentials API** (Working Draft, 23 November 2026) lets a web page ask the browser for credentials held in a wallet. The draft requires browsers to support OpenID4VP and ISO mobile-document presentation ([W3C](https://www.w3.org/TR/digital-credentials/)). Its working group is preparing a first level for Candidate Recommendation, and the chairs say the open privacy issues must be resolved first ([chairs' report](https://lists.w3.org/Archives/Public/public-fedid-wg/2026Nov/0001.html)). It helps web games; games on native engines don't go through a browser.
- **Self-Issued OpenID Provider v2** (draft) lets the user act as their own identity provider ([SIOPv2](https://openid.net/specs/openid-connect-self-issued-v2-1_0.html)).

## A sketch of the flow

1. The player logs into Game A as usual.
2. Game A asks: "Link your passport?" The player approves in their passport app.
3. The passport app proves control of the player's identifier, for example by signing a challenge from the game.
4. Game A stores the link between its own account and that identifier. It can also issue the player a signed "account linked" credential.
5. Either side can remove the link at any time.

## Constraints

- **Consent for each game; unlink at any time.**
- **No global list of a player's accounts** unless the player chooses to publish one.
- **Per-game identifiers by default** ([P-0006](P-0006-privacy-unlinkability.md)).
- **Must work for games with no online accounts at all**, using only a local profile.
- **Platform terms may restrict some flows** ([P-0021](P-0021-platform-holder-rules.md)).

## What "solved enough" looks like (Phase 1)

- [ ] A documented linking flow, with a threat model covering phishing, replay and account takeover
- [ ] A reference implementation for a web game with existing accounts, and for a game with only local profiles
- [ ] Unlinking demonstrated in both

## Candidate directions

1. **OpenID4VP presentation of a DID-bound credential.** Standard and future-proof, but heavier.
2. **A simple signed challenge** ("prove you control this DID"). Light and easy to implement in an engine, but less standard.
3. **SIOPv2-style login**, where the passport app acts as the player's own identity provider. Elegant, but SIOPv2 is still a draft.

## Open questions

- **P-0004-Q1:** Should Phase 1 use OpenID4VP or a simpler challenge-response?
- **P-0004-Q2:** Should "account linked" credentials exist, and can they be revoked?
- **P-0004-Q3:** What constraints do console platforms place on linking flows?
- **P-0004-Q4:** How should multiple characters per player work ([OQ-7](../docs/open-questions.md#scope))?

## Champion brief

- **First deliverable:** A threat model for the linking flow, then the two candidate flows prototyped in a web demo.
- **Decisions you'd drive:** OpenID4VP or a simple challenge for Phase 1 (P-0004-Q1), and whether "account linked" credentials exist (P-0004-Q2).
- **Helpful background:** OAuth and OpenID Connect, game account systems and security review.
- **Commitment:** a few hours a week, until a proposal is ready for public review.

## How to help

- Write a threat model for the linking flow.
- Prototype both candidate flows in a web demo.

## References

- [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html) · [OpenID4VP 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) · [SIOPv2](https://openid.net/specs/openid-connect-self-issued-v2-1_0.html)
