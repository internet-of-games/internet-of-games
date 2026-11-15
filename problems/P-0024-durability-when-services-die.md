---
id: P-0024
title: Durability when services die
layer: cross-cutting
phase: 1
status: open
difficulty: medium
champion: unassigned
related: [P-0003, P-0005, P-0013, P-0015, P-0029]
last_reviewed: 2026-11-15
---

# P-0024: Durability when services die

**In one sentence:** everything a player carries has to keep working when the company or project that issued it disappears.

## Why it matters

The history of this space is a history of shutdowns:

| What | What happened | Source |
|---|---|---|
| Ready Player Me | Acquired by Netflix in December 2025; public services and APIs ended 31 January 2026; exported `.glb` files kept working | [PocketGamer.biz](https://www.pocketgamer.biz/netflix-acquires-avatar-creation-platform-ready-player-me) |
| Disney Infinity | Discontinued in 2016; online services wound down by 2017 | [Shacknews](https://shacknews.com/article/96072/disney-infinity-reveals-timeline-for-shutdown-of-online-services) |
| PlayStation Home | Closed 31 March 2015 | [Game Informer](https://gameinformer.com/b/news/archive/2014/09/26/playstation-home-going-offline-in-europe-on-march-31-2015) |
| Third Room | No repository activity since August 2023 | [GitHub](https://github.com/matrix-org/thirdroom) |
| NFT items in *Ghost Recon Breakpoint* | Still tradable after support ended, but no longer usable in the game once its servers shut down | [Decrypt](https://decrypt.co/97090/ubisoft-tezos-nfts-other-games-ghost-recon-support-ends) |

Regulators are paying attention too. The European Commission answered the "Stop Destroying Videogames" initiative in June 2026 by committing to a voluntary code of conduct for games at the end of their life ([Lewis Silkin](https://www.lewissilkin.com/insights/2026/06/24/european-commission-stops-short-of-imposing-mandatory-requirements-following-citi-102n4yy)).

## Design commitments

1. **Player-held files.** The passport, avatar and credentials are files the player can back up.
2. **Content-addressed references.** Files are referenced by hash, so they can be mirrored anywhere.
3. **Embedded resources.** Avatars and badge images carry what they need inside the file.
4. **Offline verification** with cached issuer keys.
5. **Identifier methods that survive the loss of a host** ([P-0003](P-0003-player-identifier.md)).
6. **An "end of life" procedure for issuers:** before shutting down, a game publishes its final public keys and freezes its revocation lists, so credentials it issued stay verifiable.

## What "solved enough" looks like (Phase 1)

- [ ] A **"kill switch" test** that runs both demo games with every project-operated server offline. Recognition, avatar loading and credential verification still work for existing players.
- [ ] A documented end-of-life procedure for issuers
- [ ] A test for verifying credentials from an issuer that has shut down

## Open questions

- **P-0024-Q1:** What happens to revocation when an issuer disappears? Is the list frozen, or are credentials treated as valid forever?
- **P-0024-Q2:** Who archives issuers' final keys and status lists? Do we need an archive service, and who would run it?
- **P-0024-Q3:** Should following an end-of-life procedure be part of conformance ([P-0026](P-0026-conformance-and-interop-testing.md))?
- **P-0024-Q4:** How do players back up their passports simply and safely?

## How to help

- Design the kill-switch test.
- Draft the end-of-life procedure.

## References

- [prior-art.md](../docs/prior-art.md) · [design-principles.md §1](../docs/design-principles.md#1-file-first-service-optional)
