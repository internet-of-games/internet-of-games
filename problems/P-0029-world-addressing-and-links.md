---
id: P-0029
title: World addressing and links
layer: presence
phase: 2
status: open
difficulty: high
champion: unassigned
related: [P-0017, P-0021, P-0024, P-0027]
last_reviewed: 2026-11-15
---

# P-0029: World addressing and links

**In one sentence:** for games to form an *internet* rather than a list, every world, and every place inside a world, needs a stable address that other games can link to, the way every web page has a URL.

## Why it matters

The web became the web because any page can link to any other page. Today games have no equivalent. A game is identified by a different store listing on each platform, and there's no common way to say "this place, in that game." Without addresses:

- **travel between worlds** ([P-0017](P-0017-world-handoff.md)) has nothing to point at
- **discovery** ([P-0027](P-0027-discovery.md)) has nothing to list
- **a shared universe** ([P-0022](P-0022-persistent-consequences.md)) can't refer to where things happened

This is what turns many separate games into one connected universe, beyond simply sharing a player.

## What exists today

- **URLs and URIs** ([RFC 3986](https://www.rfc-editor.org/rfc/rfc3986.html)) are the web's universal addresses.
- **Operating-system deep links** open a specific screen in an installed app from a web link, for example Apple's [universal links](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) and Android's [App Links](https://developer.android.com/training/app-links).
- **Store and platform IDs** identify games, but only within each store or platform.
- **Spawn points.** OMI's `OMI_spawn_point` glTF extension marks places where players can arrive in a 3D world, which makes it a building block for "places inside worlds" ([OMI](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_spawn_point)).
- **Portals.** OMA3's draft Inter-World Portaling System describes moving between worlds ([specification](https://github.com/oma3dao/iwps-specification)).
- **Rooms as worlds.** Third Room used Matrix room addresses as world addresses ([GitHub](https://github.com/matrix-org/thirdroom)).

## A sketch

- **A world address is an ordinary HTTPS URL** on the game's own domain. Opened in a browser, it shows a page about the place. Opened from inside a game, it resolves to a **manifest** ([P-0027](P-0027-discovery.md)).
- **The manifest lists launch targets per platform**: a web URL, a desktop deep link, a store page for each console or mobile store, and so on. A single address then works everywhere, and falls back to "get this game" when the game isn't installed.
- **Places inside a world** (a stadium, a city, a story chapter, a server or instance) are paths or fragments under the world address, mapped to arrival points such as spawn points.
- **The game's identity** is tied to its domain, through the same identifier approach used for issuers ([P-0015](P-0015-issuer-trust-revocation.md)).

## Constraints

- **No central registry is required.** Anyone can create a world address, just as anyone can register a website.
- **Cross-platform:** the same address resolves to the right thing on every platform ([P-0021](P-0021-platform-holder-rules.md)).
- **Stable over time:** addresses survive game updates, and have a defined behavior when a game shuts down ([P-0024](P-0024-durability-when-services-die.md)).
- **Human-shareable:** an address can be pasted into chat, printed as a QR code or posted on social media.
- **Safe:** following a link never runs untrusted code and never shares player data without consent.

## What "solved enough" looks like (Phase 2)

- [ ] A world address format and the manifest fields for launch targets on each platform
- [ ] A demo: a link from Game A opens a specific place in Game B on the web and on desktop, and falls back to a "get the game" page when Game B isn't installed
- [ ] A documented behavior for addresses of games that have shut down

## Candidate directions

1. **Plain HTTPS URLs plus a manifest.** Works with today's web and OS deep links; needs the game to own a domain.
2. **A custom URI scheme.** Short and recognizable, but it needs OS registration and breaks in places that only accept web links.
3. **Identifier-based addresses**, such as a DID for the game plus a path. Neutral and verifiable, but unfamiliar to players.

## Open questions

- **P-0029-Q1:** Plain HTTPS URLs, a custom scheme, or identifier-based addresses?
- **P-0029-Q2:** How should places, instances and servers inside a world be addressed?
- **P-0029-Q3:** How does one address resolve to the right launch target on consoles, where deep linking is restricted?
- **P-0029-Q4:** What happens to a world's addresses when the game updates its map, or shuts down?

## How to help

- Survey how games already share deep links to specific places (for example, invite links), from public information.
- Prototype a manifest and a resolver for web and desktop.

## Decisions so far

- [ADR-0003](../docs/decisions/ADR-0003-universal-scope-built-in-risk-order.md): world addressing is part of the standard's universal scope, delivered in Phase 2.

## References

- [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986.html) · [Apple universal links](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) · [Android App Links](https://developer.android.com/training/app-links)
- [OMI_spawn_point](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_spawn_point) · [OMA3 Inter-World Portaling System](https://github.com/oma3dao/iwps-specification)
