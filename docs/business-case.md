# The business case: why would a game join?

*Last reviewed: 2026-11-15. This is a set of hypotheses to test, not proven claims. See [P-0002](../problems/P-0002-why-would-a-game-join.md).*

A standard gets adopted when it saves money, earns money or is required. Elegance alone doesn't do it. This page sets out the case as honestly as we can, including the reasons a game might say no.

## Who gains what

| Party | Possible gains | Costs and risks |
|---|---|---|
| **A receiving game** (accepts Carryfiles) | Players arrive with a name and avatar ready, so there's less onboarding friction. Recognizing a player's history from elsewhere can build attachment. It may cost less than building a full character creator. It's a marketing hook ("bring your character"). | Integration work, moderating imported content, liability, and players spending less time in its own character creator and cosmetics store. |
| **An issuing game** (signs claims) | Players can take their achievements with them, which is a reason to finish the game. Other games may reward its players, which works as free cross-promotion. Its brand travels with its badges. | Key management and revocation, plus support questions. |
| **Players** | They keep their identity and history, start new games faster, and keep their files if a game shuts down. They control what's shared. | They need to understand consent screens and look after their files or keys. |
| **Platforms and stores** | Possibly smoother onboarding and age checks. | It may weaken the lock-in that platform accounts provide. See [P-0021](../problems/P-0021-platform-holder-rules.md). |

## Hypotheses we need to test

Every hypothesis needs evidence from demos, from developer interviews, or from data that studios share in aggregate.

- **H1, onboarding.** Importing a ready-made avatar and name shortens the time to first play and reduces drop-off during setup.
- **H2, acquisition.** Cross-game rewards ("bring your badge from Game A") are a cheap way for small games to find players.
- **H3, retention.** Players who are greeted as *who they are* stay longer than players who start as strangers.
- **H4, cost.** Accepting a standard avatar costs a small studio less than building and maintaining a full character creator.
- **H5, compliance.** Reusing a privacy-preserving age signal costs less than running separate age checks in every game.
- **H6, marketing.** Being "Internet of Games compatible" is a selling point in its own right, at least for indie, social and roleplay games.

## Small games first, every game eventually

The goal is every game, the biggest included ([the mission](problem-statement.md#the-mission)). The *order* matters, though. For a large publisher, its existing player base and its control over identity are assets, and interoperability puts both at risk ([why-not-yet.md](why-not-yet.md)). For a small or mid-size game it's the reverse: there's no captive audience, so joining a larger network is all upside. The web grew the same way, with small sites linking to each other long before large portals joined in.

What changes a large publisher's calculation:

- **A network big enough to matter:** players who arrive with an identity ready, and a reason to come back.
- **Lower costs:** shared identity, avatars and age checks instead of building and maintaining their own.
- **Their own portfolio:** the standard as the easiest way to connect *their own* titles ([P-0030](../problems/P-0030-built-for-every-game.md)).
- **Regulation and player expectations** that make portability the norm ([legal-and-policy.md](legal-and-policy.md)).

## Business models *around* an open standard

The standard itself must stay free and neutral. Companies, including community members, can still build businesses **around** it without any of them becoming required:

1. **Carryfile apps and hosting services.** Apps that hold a player's documents and keys, back them up and help with recovery. These would compete with each other, and players could switch freely ([P-0005](../problems/P-0005-key-recovery.md)).
2. **Avatar creation and marketplaces.** Tools and stores for avatars that work in many games. Ready Player Me showed demand for this; [P-0024](../problems/P-0024-durability-when-services-die.md) explains how to avoid its fate.
3. **"World pass" subscriptions.** This is the founder's original question: *buy the world, not the game.* A subscription bundle could include many participating games and pay each one by engagement. Large platforms already pay creators by engagement inside their own worlds ([Tubefilter on Fortnite](https://www.tubefilter.com/2026/06/17/epic-games-unreal-editor-for-fortnite-creator-payouts/); [GamesBeat on Roblox](https://gamesbeat.com/roblox-stock-rises-20-after-earnings-daily-active-users-up-69-in-q4/)). In an open network, **several bundles could compete** for the same games, and because identity is portable, players could switch bundles without losing who they are. The bundle handles the money and the standard handles identity, so the two stay separate. How this would work is an open question ([P-0020](../problems/P-0020-connected-economies.md), Q3).
4. **Cross-promotion networks.** Services that help games run "do X there, get Y here" campaigns ([P-0019](../problems/P-0019-cross-game-entitlements.md)).
5. **Conformance testing and certification.** Paid help passing the open test suite. The test suite itself stays free ([P-0026](../problems/P-0026-conformance-and-interop-testing.md)).

## Reasons a game might say no, and our answers

| Objection | Our current answer |
|---|---|
| "It'll cannibalize my cosmetics store." | Nothing *forces* a game to display imported avatars. A game can accept identity and claims only, or show imported avatars only in certain modes. |
| "Imported content is a moderation nightmare." | Budgets, validation and moderation hooks are built in, the game keeps the final say, and it can always fall back to its own avatar ([P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md), [P-0012](../problems/P-0012-moderating-imported-identity.md)). |
| "My players don't care." | Possibly true for some genres. We need evidence by genre (P-0002 Q1). |
| "It's too much engineering." | Then we've failed principle 11. The integration target is about one day ([P-0025](../problems/P-0025-developer-adoption-cost.md)). |
| "The platform won't allow it." | Identity and claims don't need platform cooperation. Purchases and entitlements might ([P-0021](../problems/P-0021-platform-holder-rules.md)). |
| "Who's liable when something goes wrong?" | This is still open. See [legal-and-policy.md](legal-and-policy.md) and [P-0012](../problems/P-0012-moderating-imported-identity.md). |
