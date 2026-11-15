---
id: ADR-0005
title: Never require blockchains, tokens or wallets
status: accepted
date: 2026-11-15
problems: [P-0003, P-0020]
topics: [identity, economy]
supersedes: []
superseded_by: null
---

# ADR-0005: Never require blockchains, tokens or wallets

## Context

Several earlier cross-game efforts tied identity or items to tokens and crypto wallets. Examples include NFT cosmetics in a major game that ended in 2022, and identity products bundled with a wallet and a single ecosystem ([prior-art.md](../prior-art.md)). Requiring a wallet puts off players, restricts who can take part (minors, some regions), invites financial regulation, and ties the standard to particular networks. Some identifier methods, though, could reasonably use a ledger underneath.

This decision aims to keep the standard open to every player and every game.

## Decision

We will never require a blockchain, token or crypto wallet for any part of the standard. Methods that use a ledger underneath can be allowed when they meet every other principle, but every required path must work without one.

## Consequences

- Wider adoption, with no dependence on any one network.
- Less exposure to financial regulation, because the standard doesn't create tradable tokens.
- Projects built on blockchains can still take part through optional methods.
- How value moves between games remains a separate research question ([P-0020](../../problems/P-0020-connected-economies.md)).

## Universality and safety

Works for players of any age and region, and for every kind of game ([P-0030](../../problems/P-0030-built-for-every-game.md)). Lowers the risk of fraud and laundering (T6 in the [threat model](../threat-model.md)), because nothing in the standard is tradable by default.
