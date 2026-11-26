# Roadmap

The destination is a **universal standard that every game builds on** ([the mission](docs/problem-statement.md#the-mission)). The roadmap is organized by **what we can prove** along the way, not by dates. Each phase ends with something working that anyone can run. The phase numbers match the `phase` field in each [problem doc](problems/README.md).

## Phase 0: Define the problem *(now)*

**Goal:** a shared, well-sourced understanding of the problem, and a community that wants to work on it.

- [x] Problem docs: vision, problem statement, landscape, prior art, standards map, layer model and numbered sub-problems
- [x] Decision records, a threat model, an agent guide and automated checks for the docs
- [x] Settle the name for the portable player document: it's a Carryfile ([ADR-0010](docs/decisions/ADR-0010-call-the-player-document-a-carryfile.md))
- [ ] Contact adjacent communities and record where each piece of our work should live upstream. These include OMI, the VRM Consortium and Khronos avatar work, the Metaverse Standards Forum and its Web of Worlds initiative, the W3C Credentials Community Group, DIF and the OpenID Foundation ([how to take part](docs/upstream.md)).
- [ ] Hold the first open community call and publish the notes in Discussions
- [ ] Recruit champions for the Phase 1 problems
- [ ] Decide the IP policy for specification text ([P-0001](problems/P-0001-neutral-governance-and-ip.md))

**Exit criteria:** every Phase 1 problem has a champion and at least one candidate direction discussed in public.

## Phase 1: Same character, two games

**Goal:** the first end-to-end proof that the foundation works. We'll build two small games, independently, on different engines (for example one in Godot and one on the web with three.js). Together they must:

1. accept the same **Carryfile** (schema v0)
2. recognize the same player, with the player's consent, using an identifier no single company controls
3. show the same **avatar** (VRM), with a fallback for a game with a very different art style
4. let Game A **issue a signed claim** ("cleared the final boss"), and let Game B **verify it offline** and **honor it** as a local title or cosmetic
5. keep working if every server this project runs goes away

**Deliverables:** Carryfile schema v0, achievement credential profile v0, avatar baseline profile v0, a validator CLI, test vectors (sample Carryfiles, avatars and credentials, including deliberately broken ones), two demo games and a written threat model.

**Problems that must reach "solved enough":** [P-0003](problems/P-0003-player-identifier.md), [P-0004](problems/P-0004-account-linking.md), [P-0006](problems/P-0006-privacy-unlinkability.md), [P-0008](problems/P-0008-avatar-baseline.md), [P-0010](problems/P-0010-avatar-budgets-and-file-safety.md), [P-0011](problems/P-0011-rights-licensing-likeness.md), [P-0013](problems/P-0013-portable-claims.md), [P-0014](problems/P-0014-claim-interpretation.md), [P-0015](problems/P-0015-issuer-trust-revocation.md), [P-0024](problems/P-0024-durability-when-services-die.md), [P-0025](problems/P-0025-developer-adoption-cost.md), [P-0026](problems/P-0026-conformance-and-interop-testing.md) and [P-0030](problems/P-0030-built-for-every-game.md), whose written universality requirements keep Phase 1 from ruling out any kind of game.

The exact success criteria are in the [problem statement](docs/problem-statement.md#what-success-looks-like-for-phase-1).

## Phase 2: Travel, rewards and a third team

**Goal:** prove the system works for a team that didn't design it.

- **World-to-world handoff:** arrive in Game B from Game A with context ([P-0017](problems/P-0017-world-handoff.md))
- **World addresses and links:** a link in one game opens a specific place in another, just as one web page links to another ([P-0029](problems/P-0029-world-addressing-and-links.md))
- **Cross-game rewards** granted as entitlements, not currency ([P-0019](problems/P-0019-cross-game-entitlements.md))
- **Cross-style avatars:** a stylized game shows a recognizable version of a realistic avatar ([P-0009](problems/P-0009-cross-style-translation.md))
- **Age and eligibility signals** that don't reveal identity ([P-0007](problems/P-0007-age-and-eligibility.md))
- **Moderation hooks** for imported names and avatars ([P-0012](problems/P-0012-moderating-imported-identity.md))
- **Key recovery** that ordinary players can manage ([P-0005](problems/P-0005-key-recovery.md))
- **Portable accessibility and comfort preferences** ([P-0028](problems/P-0028-portable-preferences.md))
- A **third game from an outside team** integrates within a week, using only the docs and the SDK
- A first **interop event**, where several implementations test against each other

## Phase 3: Network effects and neutral governance

- SDKs or plugins for the major engines (Godot, web, Unity, Unreal)
- **Discovery:** how players find participating games ([P-0027](problems/P-0027-discovery.md))
- **Friends and presence** across games ([P-0018](problems/P-0018-friends-and-presence.md))
- **Platform-holder rules** for consoles and mobile stores ([P-0021](problems/P-0021-platform-holder-rules.md))
- Upstream the mature pieces to the right standards bodies, and move governance to a neutral home once the community is big enough to need one ([P-0001](problems/P-0001-neutral-governance-and-ip.md))
- Approach mid-size studios and publishers with evidence from Phases 1 and 2 ([P-0002](problems/P-0002-why-would-a-game-join.md))

## Phase 4: The baseline for every game

**Goal:** the standard becomes what every game builds on.

- Version 1.0 of the standard, under neutral governance, with conformance testing and a "compatible" mark ([P-0001](problems/P-0001-neutral-governance-and-ip.md), [P-0026](problems/P-0026-conformance-and-interop-testing.md))
- Built-in support in major engines, so new games get it by default
- Adoption by large publishers and platforms, including publishers connecting their *own* portfolios ([P-0030](problems/P-0030-built-for-every-game.md))
- **Cross-game ownership** beyond rewards: purchased and licensed items that travel when rights holders and platforms opt in ([P-0011](problems/P-0011-rights-licensing-likeness.md), [P-0019](problems/P-0019-cross-game-entitlements.md), [P-0021](problems/P-0021-platform-holder-rules.md))

## Phase 5: The full universe

**Goal:** the rest of the [vision](VISION.md), one persistent universe.

- **Connected economies**, once the legal, financial and anti-fraud picture is clear ([P-0020](problems/P-0020-connected-economies.md))
- **Persistent consequences across games** ([P-0022](problems/P-0022-persistent-consequences.md))
- **AI characters that travel between games** ([P-0023](problems/P-0023-traveling-ai-characters.md))
- **Portable reputation and moderation standing** ([P-0016](problems/P-0016-portable-reputation.md))

This work **starts now as research** because it's the hardest and riskiest part. It moves into concrete phases as the research matures.

## What would change this roadmap

- **An existing effort is already building a piece** (for example at OMI, Khronos or the Metaverse Standards Forum, whose Web of Worlds initiative is the closest so far). We'd join it rather than duplicate it.
- **A Phase 1 problem turns out to be much harder than expected.** We'd narrow the demo instead of stalling.
- **A larger studio wants to run a pilot.** We'd prioritize what it needs, as long as the standard stays neutral.
