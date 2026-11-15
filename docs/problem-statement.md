# Problem statement

*Last reviewed: 2026-11-15*

## The problem

**Every game is an island.** A player's identity, appearance, possessions, history and relationships are locked inside each game, and games have no common way to connect to one another.

Each game owns its own accounts, its own character creator, its own items and its own record of what you've done. Start a new game and you start as a new person, with nothing. This happens between games from different companies, and also between games from the *same* publisher, and even between yearly editions of the *same* franchise: NBA 2K, for example, doesn't carry your virtual currency over to the next edition (see [why-not-yet.md](why-not-yet.md#3-the-economies-are-the-business)).

Where "one identity across many experiences" does exist, it lives inside a single company's walled garden, such as Roblox, Fortnite or a console platform account. Nothing connects those gardens to each other or to the rest of gaming, and there's no shared standard anyone could build on to connect them.

## Who it affects

| Who | How |
|---|---|
| **Players** | They rebuild themselves from scratch in every game, lose their history and purchases when a game shuts down, and get locked into whichever platform holds their identity. |
| **Small and mid-size developers** | Every player arrives as a stranger, and they have to build their own character creators and onboarding that big platforms get for free. |
| **Large publishers** | Even their own games don't connect, and every new title starts its audience from zero. Today they solve this only *inside* their own ecosystems, using platform accounts and cross-progression. |
| **Platforms and engines** | Each one builds its own identity, avatar and social systems, and none of them work with anyone else's. |

## The mission

> **Build the open, universal standard that connects every game into one persistent universe. A player's identity, appearance, possessions, history and relationships travel with them, worlds link to each other the way websites do, and every game, from the biggest blockbuster to a one-person project, can build on it.**

Each part of that sentence matters:

- **Open and universal.** Anyone can use it and no single company owns it. It has to work for *every* kind of game: any genre, engine, platform, age rating, business model or scale, online or offline ([P-0030](../problems/P-0030-built-for-every-game.md)).
- **Connects every game.** That means games from different companies and games from the same company. It should be the easiest way for a publisher to connect its own titles, too.
- **One persistent universe.** The goal is more than portable characters. Worlds should be able to link to each other, so players can move between them ([P-0029](../problems/P-0029-world-addressing-and-links.md), [P-0017](../problems/P-0017-world-handoff.md)).
- **Identity, appearance, possessions, history and relationships.** The whole of a player's digital life, not only their avatar.
- **The baseline that everything else builds on.** Web standards made it possible for anyone to build a website. This standard should make it possible for anyone to build a game that joins the connected world.

## The first milestone

> **What is the smallest piece of the standard, and the smallest working prototype, that proves two games built by different teams can recognize the same player and keep meaningful continuity between them?**

The first milestone is deliberately small. It *is not* the scope of the project; it's the first proof that the foundation works.

- **Smallest.** Past attempts that started with economies or full asset portability stalled. Starting with a narrow working slice is how a standard earns trust.
- **Standard *and* prototype.** A spec with no implementations is just a pitch deck, and an implementation with no spec is just another walled garden.
- **Different teams.** This is the hardest case: different companies, engines, servers and art styles. If it works there, it works within one company too.
- **Meaningful continuity.** At minimum, the player's chosen name and look carry over, and at least one verifiable fact from Game A means something in Game B.

## Scope of the standard

The standard covers every layer of the [layer model](layer-model.md). The layers are built in order of risk, not importance:

| Layer | What it covers | Problems | Built in |
|---|---|---|---|
| **Governance and trust** | Neutral rules, IP policy, conformance, safety, universality | [P-0001](../problems/P-0001-neutral-governance-and-ip.md), [P-0002](../problems/P-0002-why-would-a-game-join.md), [P-0024](../problems/P-0024-durability-when-services-die.md)–[P-0026](../problems/P-0026-conformance-and-interop-testing.md), [P-0030](../problems/P-0030-built-for-every-game.md) | Phase 0 onward |
| **Identity** | Identifier, account linking, privacy, recovery, age, preferences | [P-0003](../problems/P-0003-player-identifier.md)–[P-0007](../problems/P-0007-age-and-eligibility.md), [P-0028](../problems/P-0028-portable-preferences.md) | Phases 1–2 |
| **Appearance** | Avatar baseline, art-style translation, budgets, rights, moderation | [P-0008](../problems/P-0008-avatar-baseline.md)–[P-0012](../problems/P-0012-moderating-imported-identity.md) | Phases 1–2 |
| **History** | Signed claims, how games interpret them, trust, reputation | [P-0013](../problems/P-0013-portable-claims.md)–[P-0016](../problems/P-0016-portable-reputation.md) | Phase 1, with research |
| **Travel and links** | World addresses, handoff between worlds, friends, discovery | [P-0017](../problems/P-0017-world-handoff.md), [P-0018](../problems/P-0018-friends-and-presence.md), [P-0027](../problems/P-0027-discovery.md), [P-0029](../problems/P-0029-world-addressing-and-links.md) | Phases 2–3 |
| **Ownership and economy** | Cross-game rewards, cross-game ownership, value transfer, platform rules | [P-0019](../problems/P-0019-cross-game-entitlements.md)–[P-0021](../problems/P-0021-platform-holder-rules.md) | Phases 2–5 |
| **Shared worlds** | Persistent consequences, AI characters that travel | [P-0022](../problems/P-0022-persistent-consequences.md), [P-0023](../problems/P-0023-traveling-ai-characters.md) | Research, then Phase 5 |

### Sequenced later, not excluded

These are part of the standard's scope. They come later because they carry the most risk, not because they matter less:

- **Currencies and tradable value** need legal, financial and anti-fraud answers first ([P-0020](../problems/P-0020-connected-economies.md)).
- **Purchased and licensed items** need rights holders and platforms to opt in ([P-0011](../problems/P-0011-rights-licensing-likeness.md), [P-0021](../problems/P-0021-platform-holder-rules.md)).
- **Shared world state and AI characters** are still open research ([P-0022](../problems/P-0022-persistent-consequences.md), [P-0023](../problems/P-0023-traveling-ai-characters.md)).

### Never part of the standard

- **Forcing a game to accept anything.** Each game always decides what imported things mean in its world. Stats and balance stay each game's own; games can read claims about them, but never have imported power pushed on them.
- **Requiring blockchains, tokens or wallets.**

## What success looks like for Phase 1

The first milestone is complete when **all** of these are true and anyone can reproduce them from this repository:

1. Two games, built by different people on different engines (for example Godot and web/three.js), each accept a player document that validates against schema v0.
2. Both games recognize the same player after a consent step, without either game's servers talking to the other.
3. Both games render the same VRM avatar. A game that can't use a 3D avatar falls back to a 2D portrait and an appearance description.
4. Game A issues a signed achievement credential. Game B verifies it **offline** (using cached public keys) and grants a local title or cosmetic.
5. Revoking the credential, or rotating the player's keys, behaves as documented.
6. Shutting down every server operated by this project doesn't stop steps 2–4 from working for players who already hold their files.
7. A malformed or oversized avatar, or a forged credential, is safely rejected by both games and by the validator.
8. A developer who wasn't involved can integrate the SDK into a third small game in about a day.

## Constraints every solution must respect

These come from [design-principles.md](design-principles.md):

1. **It must work for every game:** any genre, engine, platform, age rating, business model and scale, online or offline.
2. **No single company in the critical path**, including us.
3. **It works without crypto.**
4. **Private by default:** minimal disclosure, consent for every share, no cross-game tracking unless the player opts in.
5. **Each game keeps its own rules.** Receiving games interpret what arrives, and nothing is forced on them.
6. **File-first:** the player's files keep working even if every service disappears.
7. **Safe by default:** imported content is treated as untrusted input.
8. **Cheap to adopt:** if integration takes more than a few days, it won't be adopted.

## Why now

Several things changed between 2022 and 2026:

- **The standards matured.** W3C Verifiable Credentials 2.0 became a W3C Recommendation in May 2025. OpenID for Verifiable Presentations and OpenID for Verifiable Credential Issuance went final in July and September 2025. Selective-disclosure JWTs were published as RFC 9901. DID 1.1 reached Candidate Recommendation in March 2026. Open Badges 3.0 builds achievement credentials on Verifiable Credentials 2.0. VRM 1.0 is mature, and Khronos is turning it into general glTF avatar extensions. See [standards-map.md](standards-map.md).
- **The cautionary tales are recent.** Ready Player Me, the best-known cross-game avatar service, was acquired by Netflix and shut down its public services on 31 January 2026, and only exported files kept working. See [prior-art.md](prior-art.md#ready-player-me).
- **Regulation is moving.** EU member states are due to offer digital identity wallets by the end of 2026, age verification is rolling out, and in November 2026 the European Commission proposed a Digital Fairness Act covering virtual currencies. See [legal-and-policy.md](legal-and-policy.md).
- **AI is cutting the cost of making content**, which makes a universe of many interconnected games far more achievable.
