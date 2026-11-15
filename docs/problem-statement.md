# Problem statement

*Last reviewed: 2026-11-15*

## The problem

**Players can't carry a persistent identity across games made by different companies. That identity means who they are, what they look like and what they've done.**

Every game owns its own accounts, its own character creator and its own record of your history. Start a new game and you start as a new person. This holds even between games from the *same* publisher, and even between annual editions of the *same* franchise. NBA 2K, for example, doesn't carry your virtual currency from one yearly edition to the next (see [why-not-yet.md](why-not-yet.md#3-the-economies-are-the-business)).

## Who it affects

| Who | How |
|---|---|
| **Players** | They rebuild characters over and over, lose their history when a game shuts down, and get locked into whichever platform holds their identity. |
| **Small and mid-size developers** | They can't build on the identity, appearance or reputation players already have, so every player arrives as a stranger. They also pay to build the character creators and onboarding that large platforms provide for free. |
| **Large publishers and platforms** | They already solve this *inside* their own ecosystems with platform accounts, cross-progression and achievements, so they have little reason to solve it *between* ecosystems. See [why-not-yet.md](why-not-yet.md). |

## The central question

> **What is the smallest open standard, and the smallest working prototype, that would let two independently developed games recognize the same player character and preserve meaningful continuity between them?**

Each phrase is deliberate:

- **Smallest.** Past attempts that started with economies or full asset portability stalled, so we start with the minimum that's useful.
- **Open standard *and* working prototype.** A spec with no implementations is just a pitch deck, and an implementation with no spec is just another walled garden. We need both.
- **Independently developed.** That means different companies, engines, servers and art styles, with no shared backend that we control.
- **Recognize the same player character.** Both games can verify, with the player's consent, that they're dealing with the same player-controlled identity.
- **Meaningful continuity.** At minimum, the player's chosen name and look carry over, and at least one verifiable fact from Game A means something in Game B.

## Scope

### In scope (Phase 1)

- **Identity anchor:** an identifier for the player that no single company controls ([P-0003](../problems/P-0003-player-identifier.md))
- **Account linking:** connecting that identity to each game's existing accounts ([P-0004](../problems/P-0004-account-linking.md))
- **Privacy:** players choose what each game sees, and whether games can correlate them ([P-0006](../problems/P-0006-privacy-unlinkability.md))
- **Appearance:** a portable avatar baseline, safety budgets and rights metadata ([P-0008](../problems/P-0008-avatar-baseline.md), [P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md), [P-0011](../problems/P-0011-rights-licensing-likeness.md))
- **History:** signed, portable claims, and how a receiving game interprets them ([P-0013](../problems/P-0013-portable-claims.md), [P-0014](../problems/P-0014-claim-interpretation.md), [P-0015](../problems/P-0015-issuer-trust-revocation.md))
- **Durability, adoption cost and conformance** ([P-0024](../problems/P-0024-durability-when-services-die.md), [P-0025](../problems/P-0025-developer-adoption-cost.md), [P-0026](../problems/P-0026-conformance-and-interop-testing.md))

### Later

World-to-world travel, cross-game rewards, cross-style avatars, age signals, moderation, key recovery, portable preferences, friends and presence, discovery, and platform-holder rules. See [ROADMAP.md](../ROADMAP.md).

### Explicitly out of scope for now

- **Moving currencies or other tradable value** between games ([P-0020](../problems/P-0020-connected-economies.md) explains why).
- **Moving stats, power or items that affect game balance.**
- **Moving licensed content** such as league players, film characters, music or brands.
- **Shared world state and AI characters across games.** These are research tracks.
- **Any requirement for blockchains, tokens or wallets.** They aren't banned, just not required.

## What success looks like for Phase 1

The first proof is done when **all** of the following are true and anyone can reproduce them from this repository:

1. Two games, built by different people on different engines (for example Godot and web/three.js), each accept a player document that validates against schema v0.
2. Both games recognize the same player after a consent step, without either game's servers talking to the other.
3. Both games render the same VRM avatar. A game that can't use a 3D avatar falls back to a 2D portrait and an appearance description.
4. Game A issues a signed achievement credential. Game B verifies it **offline** (using cached public keys) and grants a local title or cosmetic.
5. Revoking the credential, or rotating the player's keys, behaves exactly as documented.
6. Shutting down every server run by this project doesn't stop steps 2 to 4 from working for players who already hold their files.
7. Both games and the validator safely reject a malformed or oversized avatar and a forged credential.
8. A developer who wasn't involved can integrate the SDK into a third small game in about a day.

## Constraints every solution must respect

These come from [design-principles.md](design-principles.md):

1. **No single company is in the critical path**, and that includes us.
2. **It works without crypto.**
3. **It's private by default:** minimal disclosure, consent for every share, and no cross-game tracking unless the player opts in.
4. **Each game keeps its own rules.** Receiving games interpret claims, and nothing is forced on them.
5. **It's file-first:** the player's files keep working if every service disappears.
6. **It's safe by default:** imported content is treated as untrusted input.
7. **It's cheap to adopt.** If integration takes more than a few days, nobody will adopt it.

## Why now

Several things changed between 2022 and 2026.

- **The standards matured.** W3C Verifiable Credentials 2.0 became a W3C Recommendation in May 2025. OpenID for Verifiable Presentations and OpenID for Verifiable Credential Issuance were finalized in July and September 2025. Selective-disclosure JWTs were published as RFC 9901. DID 1.1 reached Candidate Recommendation in March 2026. Open Badges 3.0 builds achievement credentials on Verifiable Credentials 2.0. VRM 1.0 is mature, and Khronos is turning it into general glTF avatar extensions. See [standards-map.md](standards-map.md).
- **The cautionary tales are recent.** Ready Player Me, the best-known cross-game avatar service, was acquired by Netflix and shut down its public services on 31 January 2026. Only exported files kept working. See [prior-art.md](prior-art.md#ready-player-me).
- **Regulation is moving.** EU member states are due to offer digital identity wallets by the end of 2026, age verification is being rolled out, and in November 2026 the European Commission proposed a Digital Fairness Act that covers virtual currencies. See [legal-and-policy.md](legal-and-policy.md).
- **AI is cutting the cost of making content**, which makes a universe of many smaller, interconnected games more plausible.
