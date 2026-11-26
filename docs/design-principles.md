# Design principles

*Last reviewed: 2026-11-15*

Each principle comes from something that went wrong, or right, in earlier attempts ([prior-art.md](prior-art.md)). Proposals in this repository should say how they follow each principle, or why they need an exception.

## 1. File-first, service-optional

The player's identity, avatar and credentials are **files the player holds**. Services can make things more convenient, but nothing should stop working when a service disappears.
*Learned from:* Ready Player Me, Disney Infinity, PlayStation Home, Third Room. → [P-0024](../problems/P-0024-durability-when-services-die.md)

## 2. Claims, not state

Games share **signed facts**, not stats, inventories or currencies.
*Learned from:* amiibo, Skylanders, Pokémon HOME; and, as the counterexample, every attempt that started with economies. → [portability-matrix.md](portability-matrix.md), [ADR-0008](decisions/ADR-0008-continuity-as-signed-claims-not-state.md)

## 3. The receiving game decides

Accepting anything is always optional. Each game maps foreign claims and avatars to its own rules and art style.
*Learned from:* amiibo, Pokémon HOME, LEGO styles in Fortnite. → [P-0014](../problems/P-0014-claim-interpretation.md)

## 4. Link accounts, don't replace them

Games keep their existing account systems. The Carryfile *links* to them, and players never need yet another password.
*Learned from:* platform accounts and Epic Online Services, which won because they fit how games already work. → [P-0004](../problems/P-0004-account-linking.md)

## 5. No single company in the critical path, including us

Identifiers, verification and file formats must work without any one company's servers. That includes servers run by this project.
*Learned from:* Ready Player Me; walled gardens in general. → [P-0001](../problems/P-0001-neutral-governance-and-ip.md), [P-0003](../problems/P-0003-player-identifier.md)

## 6. Private by default

Share the minimum, ask for consent each time, and don't let games correlate a player across titles unless the player chooses that. Never require a birthdate when "over 13" will do.
*Learned from:* data-protection law and children's privacy rules. → [P-0006](../problems/P-0006-privacy-unlinkability.md), [P-0007](../problems/P-0007-age-and-eligibility.md)

## 7. Imported content is untrusted input

Every avatar, name and credential from outside is validated, budgeted and allowed to fail safely.
*Learned from:* CVE-2022-3008 in a glTF loader, avatar performance-ranking systems on social platforms, and marketplace fraud. → [P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md), [P-0012](../problems/P-0012-moderating-imported-identity.md), [P-0015](../problems/P-0015-issuer-trust-revocation.md)

## 8. Compose existing standards; don't invent new ones

Use W3C Verifiable Credentials, DIDs, OpenID, glTF/VRM and Open Badges. Write a *profile*, not a new format, unless there's no other way.
*Learned from:* the maturity of those standards ([standards-map.md](standards-map.md)) and the cost of the many metaverse projects that started from scratch. → [ADR-0004](decisions/ADR-0004-compose-existing-open-standards.md)

## 9. Two independent implementations before anything is "standard"

Nothing is called stable until two independent implementations interoperate using shared test files.
*Learned from:* OMI's staged process and the IETF's "running code" culture. → [P-0026](../problems/P-0026-conformance-and-interop-testing.md)

## 10. Works without crypto, doesn't forbid it

No blockchain, token or wallet is ever required. Identifier methods that use one underneath are allowed if they meet the other principles.
*Learned from:* Ubisoft Quartz, and identity products bundled with wallets. → [ADR-0005](decisions/ADR-0005-never-require-blockchains-tokens-or-wallets.md)

## 11. Integration in a day

If adding the basics takes more than about a day, or needs a server, it won't happen. Ease of adoption is a feature that gets designed and tested.
*Learned from:* Epic Online Services (free and engine-agnostic) and every standard that died of complexity. → [P-0025](../problems/P-0025-developer-adoption-cost.md)

## 12. Build upstream

When another community already owns a layer, such as glTF extensions at OMI or Khronos, or credentials at W3C, DIF or OpenID, contribute there instead of forking.
*Learned from:* the fragmentation of the 2021–2023 metaverse era.

## 13. Built for every game

The standard must work for every kind of game: blockbusters and one-person projects, any genre, engine, platform, age rating or business model, online or fully offline, and between games from different companies or from the same one. Anything that only fits one kind of game belongs in an optional layer, not in the core.
*Learned from:* the goal itself. A baseline that leaves out whole categories of games isn't a baseline. → [P-0030](../problems/P-0030-built-for-every-game.md), [ADR-0003](decisions/ADR-0003-universal-scope-built-in-risk-order.md)
