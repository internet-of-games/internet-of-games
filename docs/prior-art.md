# Prior art

*Last reviewed: 2026-11-24*

People have tried to carry characters, items and identity between experiences many times. This page records what was tried, what happened, and **what each attempt teaches**. Those lessons feed directly into the [design principles](design-principles.md).

## At a glance

| Attempt | What traveled | Scope | Outcome | Main lesson |
|---|---|---|---|---|
| [Nintendo amiibo](#nintendo-amiibo) | A figure, with optional save data | Many Nintendo-platform games | Long-running | The receiving game decides what an item means |
| [Skylanders](#skylanders) | Character level and upgrades, stored on the toy | One series | Series ended | Data can travel with the player; older games clamp it to their own rules |
| [Disney Infinity](#disney-infinity) | Characters across play sets | One publisher | Discontinued in 2016, online services ended in 2017 | When the publisher exits, the cross-game layer dies |
| [Pokémon HOME](#pokémon-home) | Individual creatures | One franchise, many games | Active | The target game decides what's allowed in |
| [LEGO styles in Fortnite](#lego-styles-in-fortnite) | Outfits, re-made in another art style | One company | Active | Changing art style means re-authoring or describing the look, and licensing gates it |
| [Mii](#mii) | A character described by parameters | One platform | Long-running | A *description* can be drawn in many styles; a mesh can't |
| [Platform achievements](#platform-achievements-and-accounts) | Achievement history | One platform | Universal | Players value a meta-identity, but it's locked to the platform |
| [Epic Online Services](#platform-achievements-and-accounts) | Account, friends, achievements | Any engine or store, one company | Active and free | Identity infrastructure can be free if it serves a strategy |
| [PlayStation Home](#playstation-home) | A social avatar and spaces | One platform | Closed in 2015 | Platform social worlds can close with no successor |
| [Ready Player Me](#ready-player-me) | Hosted cross-app avatars | Thousands of apps | Acquired, public services shut down January 2026 | **File-first, service-optional** |
| [VRoid Hub](#vroid-hub) | VRM avatars with usage conditions | Apps that integrate its API | Active | License metadata plus consent flows are practical |
| [Immutable Passport](#immutable-passport) | Web3 identity and wallet | One ecosystem | Active | Bundling identity with a wallet limits who adopts it |
| [Ubisoft Quartz](#ubisoft-quartz) | NFT cosmetics | One game | NFT drops ended in 2022 | Tokenizing items doesn't create interoperability or demand |
| [OMI glTF extensions](#open-metaverse-interoperability-group-omi) | World behavior, such as physics and seats | Open standard | Active | Standards move through implementations; identity extensions stalled |
| [OMA3 portaling](#oma3-inter-world-portaling-system) | Moving between worlds | Draft specification | Quiet since 2025 | Portaling is specified on paper but not deployed |
| [Web of Worlds](#web-of-worlds) | A user manifest (identity, avatar, preferences, assets) and links between worlds | Proposed open architecture, not specific to games | Whitepaper and draft API, 2026 | Others are designing a general version of our identity and travel layers |
| [Third Room](#third-room) | Identity and worlds over Matrix | Open source | Dormant since 2023 | The right architecture can still lose its funding |
| [Mozilla Hubs](#mozilla-hubs) | Web social worlds | Open source | Mozilla left in 2024; the community continues | Community stewardship can outlive a corporate exit |
| [Bluesky / AT Protocol](#bluesky-and-the-at-protocol) | Portable account identity (DIDs) | A social network | Active | Portable identity can work at consumer scale if it's hidden behind a normal user experience |
| [Open Metaverse Foundation](#open-metaverse-foundation) | (Specifications, with identity in scope) | Linux Foundation project | Little visible output | A foundation without builders stalls |
| [Roleplay servers and EVE Online](#roleplay-servers-and-eve-online) | Persistent lives and politics | One game each | Thriving | Demand for "be anyone" worlds is real |

## Nintendo amiibo

One figure works in many games, and **each game decides what the figure does there**. Nintendo distinguishes *read-only* games, which just read the figure, from *read/write* games, which store save data on it. A figure can hold save data for only one read/write game at a time ([Nintendo amiibo FAQ](https://en-americas-support.nintendo.com/app/answers/detail/a_id/13260/p/603/c/947)).

**Lesson:** this is the closest existing model to what we want. The thing that travels is small and stable, and its meaning is local. A receiving game is free to ignore it. See [P-0014](../problems/P-0014-claim-interpretation.md).

## Skylanders

Each toy carries a chip that stores the character's progress, including upgrades and stats, so a character keeps its progress across the series. According to fan documentation, level caps rose over the series, and an older game clamps a higher-level figure to its own cap without erasing the stored level ([Skylanders Wiki](https://skylanderswiki.com/wiki/Console_Stats); [Game Developer](https://www.gamedeveloper.com/business/skylanders-and-the-birth-of-the-toys-to-life-market)).

**Lesson:** the receiving game applies **its own limits** to imported data and never rewrites the player's history.

## Disney Infinity

Disney discontinued Disney Infinity in May 2016 and wound down its online services in phases through early 2017 ([Shacknews](https://shacknews.com/article/96072/disney-infinity-reveals-timeline-for-shutdown-of-online-services)).

**Lesson:** a cross-game layer owned by one publisher dies when that publisher leaves the business.

## Pokémon HOME

Pokémon HOME moves creatures between compatible Pokémon games, but **only into games that support that particular creature**. Scarlet and Violet, for example, don't include every species ([Pokémon HOME](https://home.pokemon.com/en-us/); [VGC](https://www.videogameschronicle.com/guide/pokemon-home-scarlet-and-violet-compatibility-when-does-it-go-live)).

**Lesson:** compatibility lists work. The **target** decides what may enter.

## LEGO styles in Fortnite

When LEGO Fortnite launched in December 2023, more than 1,200 existing Fortnite outfits gained a LEGO-style version. These were rolled out gradually and given free to people who already owned the originals, and licensing determined which outfits could be converted ([PC Gamer](https://www.pcgamer.com/fortnite-is-adding-a-lego-themed-survival-crafting-mode-that-includes-lego-versions-of-over-1200-pre-existing-skins); [Dexerto](https://dexerto.com/fortnite/fortnite-launches-over-1200-lego-skins-for-chapter-5-season-1-2412246)).

**Lesson:** even one company controlling everything had to make a new version of every outfit for a new art style. Moving across styles needs either per-style authoring or a style-independent description that each game renders in its own way. Licensing applies at every step. See [P-0009](../problems/P-0009-cross-style-translation.md) and [P-0011](../problems/P-0011-rights-licensing-likeness.md).

## Mii

Nintendo's Mii characters are built from a set of parameters (face shape, hairstyle, colors, proportions) rather than being a fixed mesh. That lets many games draw the same Mii in their own style ([Wikipedia](https://en.wikipedia.org/wiki/Mii)).

**Lesson:** a **description** of a character travels across art styles far better than a 3D file does. This is the basis of the "appearance descriptor" idea in [P-0009](../problems/P-0009-cross-style-translation.md).

## Platform achievements and accounts

Console and PC platforms have offered cross-game achievement histories and friends lists for years. Xbox, PlayStation and Steam each have their own. **Epic Online Services** goes further: it's free, works with any engine and any combination of stores and platforms, and can merge a player's Steam and Epic Games Store friends into a single list ([Epic](https://onlineservices.epicgames.com/); [Epic news](https://onlineservices.epicgames.com/news/epic-online-services-release-free-pc-crossplay-tools)).

**Lesson:** players value a meta-identity that spans games, and identity infrastructure can be offered for free. But these identities belong to the platform, and a game can't verify them outside it.

## PlayStation Home

Sony's social world for PS3 closed on 31 March 2015 after phased content shutdowns, with no successor ([Game Informer](https://gameinformer.com/b/news/archive/2014/09/26/playstation-home-going-offline-in-europe-on-march-31-2015)).

**Lesson:** a platform can close the spaces where people's avatars and belongings lived, so nothing important should exist *only* inside one service.

## Ready Player Me

Ready Player Me offered hosted, cross-app avatars and APIs to a large developer community. Netflix acquired the company in December 2025, and its public services, including the PlayerZero product and the developer APIs, ended on 31 January 2026. Avatars that had already been exported as `.glb` files kept working, but integrations that relied on the hosted APIs stopped ([PocketGamer.biz](https://www.pocketgamer.biz/netflix-acquires-avatar-creation-platform-ready-player-me); [GamesBeat](https://gamesbeat.com/netflix-acquires-ready-player-me-avatar-maker/); [AvatarSDK migration guide](https://avatarsdk.com/blog/2026/07/07/ready-player-me-migration-guide/)).

**Lesson:** this is the most important cautionary tale for our project. **A portable identity hosted by one company is portable only until that company exits.** Files in open formats survived; the service didn't. See [P-0024](../problems/P-0024-durability-when-services-die.md).

## VRoid Hub

pixiv's VRoid Hub lets external applications load avatars that users have uploaded, through an OAuth-based API. Each avatar's creator sets conditions on how it may be used ([VRoid Hub API](https://developer.vroid.com/en/api)).

**Lesson:** machine-readable usage conditions combined with a consent step is a practical, proven pattern. See [P-0011](../problems/P-0011-rights-licensing-likeness.md).

## Immutable Passport

Immutable's "Passport" is a web3 identity and wallet that it describes as working across the games and marketplaces in its ecosystem ([Decrypt](https://decrypt.co/210334/immutable-debuts-passport-gaming-wallet-gods-unchained-more); [GamesBeat](https://gamesbeat.com/immutable-passport-hits-200k-unique-web3-gamers/)).

**Lesson:** tying identity to a wallet and to one ecosystem limits adoption to that ecosystem. It also means the word "passport" is already taken in this space; see [open-questions.md](open-questions.md#naming).

## Ubisoft Quartz

Ubisoft sold NFT cosmetics ("Digits") for *Ghost Recon Breakpoint* in 2021 and 2022. New Digits ended when the game stopped receiving content in April 2022 ([PC Gamer](https://www.pcgamer.com/ubisoft-ends-its-nft-experiment-in-ghost-recon-breakpoint-but-promises-theyre-coming-to-other-games); [Decrypt](https://decrypt.co/97090/ubisoft-tezos-nfts-other-games-ghost-recon-support-ends)).

**Lesson:** putting an item on a blockchain doesn't make another game able, or willing, to use it. Interoperability is a design and business agreement, not a storage format.

## Open Metaverse Interoperability Group (OMI)

OMI develops glTF extensions through a staged process. An extension needs implementations, validator support and sample assets before it can advance, and contributors sign the W3C Community Contributor License Agreement. As of this review, physics extensions and spawn points are at Stage 1 and seats at Stage 2. `KHR_audio_emitter` graduated to Khronos. The identity-related extensions, `OMI_personality` and `OMI_link`, are **archived** ([OMI glTF extensions](https://github.com/omigroup/gltf-extensions)).

**Lesson:** standards make progress through working implementations. Identity is the unfinished part. We should build on OMI's process, not around it.

## OMA3 Inter-World Portaling System

OMA3, a web3 consortium, drafted a specification for moving users between virtual worlds and published it for comment in 2024. It has a liaison with the Metaverse Standards Forum ([Metaverse Standards Forum](https://metaverse-standards.org/news/blog/metaverse-standards-forum-enters-liaison-agreement-with-oma3/); [specification repository](https://github.com/oma3dao/iwps-specification)). The repository was last updated in September 2025.

**Lesson:** world-to-world travel has been specified on paper but not widely deployed. See [P-0017](../problems/P-0017-world-handoff.md).

## Web of Worlds

The Web of Worlds, an initiative of the Metaverse Standards Forum, proposes an open architecture in which 3D worlds link to each other the way web pages do. Each world has a URI, worlds connect through portals, assets use existing formats, and a person carries a "User Manifest" with their identity, avatar, preferences and assets from world to world, managed in a digital wallet with DIDs and Verifiable Credentials ([whitepaper](https://webofworlds.github.io/initial_MSF_Whitepaper/gen/MSF-3DWebInterop_WoWWhitepaper.pdf); [MSF announcement](https://metaverse-standards.org/news/blog/announcing-the-web-of-worlds-whitepaper-a-concrete-path-to-the-open-metaverse/)). The initiative has published a draft API and lists early implementations, and a W3C breakout at TPAC in October 2026 mapped it against existing W3C standards ([Web of Worlds](https://webofworlds.github.io/); [W3C event](https://www.w3.org/events/meetings/437890c5-8be3-44d2-b5e8-d8cd2a69d847/)).

**Lesson:** others see the same gap. The Web of Worlds is general-purpose and early, while our work is specific to games: how a receiving game interprets claims, avatar budgets, offline play, age ratings and native engines. We should learn from it, bring game requirements to it and build on it where it fits, instead of designing around it.

## Third Room

Third Room, from the Matrix.org Foundation, built virtual worlds as Matrix rooms so that identity and social connections could follow users between worlds. Its repository hasn't been pushed to since August 2023 ([GitHub](https://github.com/matrix-org/thirdroom)).

**Lesson:** an architecture can be right and still lose its funding and team. Protocols outlive single projects, and we should design for that.

## Mozilla Hubs

Mozilla ended its support for Hubs on 31 May 2024. The codebase continues under the community-run Hubs Foundation ([Mozilla](https://support.mozilla.org/en-US/kb/end-support-mozilla-hubs); [Hubs Foundation](https://github.com/Hubs-Foundation/hubs)).

**Lesson:** open source plus community stewardship can outlive a corporate exit.

## Bluesky and the AT Protocol

Every Bluesky account has a decentralized identifier (`did:plc`), so an account can move between hosting providers. Bluesky has started handing the directory behind `did:plc` to an independent organization ([AT Protocol blog](https://atproto.com/blog/plc-directory-org)). Tens of millions of accounts have been created, although active use fell in 2026 ([TechCrunch](https://techcrunch.com/2026/08/11/blueskys-active-user-base-is-shrinking-as-its-focus-expands-beyond-the-app/)).

**Lesson:** portable, decentralized identity can work for ordinary people at scale **if the cryptography stays invisible**. Identity technology alone doesn't create engagement, though; the product still has to be good.

## Open Metaverse Foundation

The Linux Foundation launched the Open Metaverse Foundation in January 2023, with identity among its areas of interest ([SD Times](https://sdtimes.com/software-development/linux-foundation-launches-open-metaverse-foundation/)). As of this review we couldn't find public specifications or code it has delivered. That finding is limited by our search, not proof that nothing exists.

**Lesson:** a foundation needs builders and a concrete first deliverable. Governance on its own doesn't ship anything.

## Roleplay servers and EVE Online

Community-run roleplay servers for GTA V and Red Dead Redemption 2 grew large enough that Rockstar acquired the team behind them in 2023 ([Game Developer](https://gamedeveloper.com/business/rockstar-acquires-community-roleplay-team-cfx-re)). EVE Online's players elect a council every year; CSM 21 in 2026 drew 32,675 votes ([EVE Online](https://www.eveonline.com/news/view/heres-your-csm-21)).

**Lesson:** the "be anyone, do anything" part of the [vision](../VISION.md) already exists inside single games, and it grew out of communities and mods. Persistent societies are possible; connecting them *across* games is the unsolved part.
