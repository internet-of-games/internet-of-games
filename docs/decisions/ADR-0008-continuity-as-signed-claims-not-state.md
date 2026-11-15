---
id: ADR-0008
title: Carry continuity as signed claims, not transferred game state
status: accepted
date: 2026-11-15
problems: [P-0013, P-0014, P-0020]
topics: [architecture, history, economy]
supersedes: []
superseded_by: null
---

# ADR-0008: Carry continuity as signed claims, not transferred game state

## Context

The central design question is what a game receives about a player who arrives from another game. Moving state directly, such as stats, inventories or currencies, breaks each game's balance, economy and licenses ([why-not-yet.md](../why-not-yet.md)). Systems that already work across games share a pattern: the receiving game interprets what arrives under its own rules. Examples are amiibo, Skylanders and Pokémon HOME ([prior-art.md](../prior-art.md)).

This decision aims to give players real continuity without forcing any game to give up control of its own rules.

## Options

1. **Transfer state directly.** It's simple to describe, but it breaks balance, economies and licenses, and no game would accept it.
2. **A shared global state or economy.** Maximally connected, but it needs one controller, which the [design principles](../design-principles.md) rule out.
3. **Signed claims interpreted locally.** Games share verifiable facts, and each receiving game decides what they mean.

## Decision

We will carry continuity between games as signed claims about the player: identity, appearance and verifiable facts about what they've done. Each receiving game verifies these claims and interprets them under its own rules. Transferring state that affects balance directly isn't part of the standard. When cross-game ownership and value arrive, they will be built on top of claims, starting with entitlements ([P-0019](../../problems/P-0019-cross-game-entitlements.md)).

## Consequences

- Each game keeps control of its balance and economy, and continuity can be adopted gradually.
- Richer continuity needs shared vocabularies for claims ([P-0013](../../problems/P-0013-portable-claims.md)) and conventions for interpreting them ([P-0014](../../problems/P-0014-claim-interpretation.md)).
- The same claim can mean different things in different games. That's intentional, and it should be explained clearly to players.
- Trust and revocation become central ([P-0015](../../problems/P-0015-issuer-trust-revocation.md)).

## Universality and safety

Claims work offline and across every genre and platform ([P-0030](../../problems/P-0030-built-for-every-game.md)). Not moving value reduces fraud and malicious-content risk (T6 and T5 in the [threat model](../threat-model.md)). Claims add a forgery risk (T4), handled by signatures and revocation, and a tracking risk (T3), handled by selective disclosure.
