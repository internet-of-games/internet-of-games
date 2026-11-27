# Landscape, late 2026

*Last reviewed: 2026-11-15. This is a snapshot. Numbers, statuses and repository activity will move; corrections are welcome.*

**Summary:** the "metaverse" pitch of 2021 has faded. In its place there are two things. Walled gardens keep getting bigger, and a quiet layer of open standards keeps maturing. Nobody has yet *composed* those open standards into a shared foundation that games actually build on. That gap is where this project sits.

## 1. Walled gardens are winning

| Platform | Scale | Where identity lives |
|---|---|---|
| **Roblox** | $4.9B revenue and $6.8B bookings in 2025; 144M daily active users in Q4 2025; creators earned more than $1.5B in 2025 ([GamesBeat](https://gamesbeat.com/roblox-stock-rises-20-after-earnings-daily-active-users-up-69-in-q4/); [earnings call](https://www.fool.com/earnings/call-transcripts/2026/02/05/roblox-rblx-q4-2025-earnings-call-transcript/)) | A Roblox account and avatar work only inside Roblox. |
| **Fortnite / UEFN** | More than $1B paid to creators since 2023, announced 17 June 2026. Creator islands account for 47% of Fortnite playtime ([Tubefilter](https://www.tubefilter.com/2026/06/17/epic-games-unreal-editor-for-fortnite-creator-payouts/); [GamesBeat](https://gamesbeat.com/epic-games-has-paid-out-1-billion-to-creators-since-launching-unreal-editor-for-fortnite-in-2023/)) | An Epic account and Fortnite locker work only inside Epic's ecosystem. |

Epic is the big company that talks most about interoperability. Its CEO has argued that the metaverse has to be built on open protocols and standards ([Game Developer](https://gamedeveloper.com/business/tim-sweeney-says-only-hope-for-new-games-is-to-connect-to-economies-of-other-games-)). Epic has also said Unreal Engine 6 will connect Fortnite with other Unreal games ([PC Gamer](https://www.pcgamer.com/gaming-industry/epic-boss-tim-sweeney-says-unreal-engine-6-will-be-a-metaverse-joining-fortnite-and-other-unreal-games-including-an-upcoming-persistent-universe-in-development-with-disney)). In his Unreal Fest Tokyo keynote on 3 November 2026, Epic's CEO said UE6 will merge Unreal Engine and the Fortnite editor into one engine on an open, interoperable base, with cross-promotion and player value that carries between experiences as the goal. Its first preview is planned for late 2027: gameplay code moves to Epic's Verse language, and UE6 projects won't include Blueprints or the C++ gameplay framework ([Epic Games press release](https://prtimes.jp/main/html/rd/p/000000211.000036502.html), in Japanese; [4Gamer](https://www.4gamer.net/games/210/G021013/20261104013/), in Japanese). At Unite 2025, Unity said its in-app purchase tools would come to Unreal developers and that Unity-made games could take part in Fortnite's economy ([PocketGamer.biz](https://www.pocketgamer.biz/tim-sweeney-at-unite-2025-unitys-in-app-purchase-apis-coming-to-unreal-engine-devs)). That is interoperability **organized around one ecosystem's economy**, not a neutral standard.

Disney invested $1.5B in Epic in 2024 to build a persistent Disney universe connected to Fortnite ([GameSpot](https://www.gamespot.com/articles/a-disney-persistent-universe-tied-to-fortnite-is-in-the-works/1100-6520900/)). The first visible piece, *Disneyland Game Rush*, runs inside Fortnite ([Monorail News](https://monorailnews.com/disneyland-game-rush-marks-the-first-step-in-disneys-fortnite-persistent-universe/)). As of this review we found no confirmed launch date for the full universe.

## 2. Platform accounts are the de facto cross-game identity

Today, "one identity across many games" mostly means a **platform account**: PlayStation Network, Xbox, Nintendo, Steam or Epic. Each platform also keeps its own achievements and friends lists. The most open of these is **Epic Online Services**. It's free, works with any engine and any combination of stores and platforms, and can merge a player's Steam and Epic Games Store friends into a single list ([Epic](https://onlineservices.epicgames.com/); [Epic news](https://onlineservices.epicgames.com/news/epic-online-services-release-free-pc-crossplay-tools)). Even so, it's one company's service, and the identity it provides is that company's.

## 3. The 2021 metaverse pitch has receded

- **Meta** split Horizon Worlds off from its Quest VR platform in February 2026 and refocused it almost entirely on mobile. In March it reversed a plan to drop VR access, but development effort stays on mobile ([TechCrunch](https://techcrunch.com/2026/03/19/meta-decides-not-to-shut-down-horizon-worlds-on-vr-after-all/); [Engadget](https://engadget.com/ar-vr/meta-isnt-shutting-down-its-vr-metaverse-after-all-165520696.html)).
- **Ready Player Me**, the best-known cross-game avatar service, was acquired by Netflix in December 2025. Its public services, including its PlayerZero product and developer APIs, ended on 31 January 2026 ([PocketGamer.biz](https://www.pocketgamer.biz/netflix-acquires-avatar-creation-platform-ready-player-me); [AvatarSDK migration guide](https://avatarsdk.com/blog/2026/07/07/ready-player-me-migration-guide/)). See [prior-art.md](prior-art.md#ready-player-me).
- **Crypto worlds and NFT items** shrank. Ubisoft ended new NFT items in *Ghost Recon Breakpoint* in 2022 ([PC Gamer](https://www.pcgamer.com/ubisoft-ends-its-nft-experiment-in-ghost-recon-breakpoint-but-promises-theyre-coming-to-other-games)). The Sandbox cut about half its staff in 2025 ([CoinDesk](https://www.coindesk.com/business/2025/08/28/the-sandbox-cuts-50-staff-restructures-as-animoca-brands-take-control)). Web3 identity products such as Immutable Passport exist, but they're tied to one ecosystem and its wallet ([GamesBeat](https://gamesbeat.com/immutable-passport-hits-200k-unique-web3-gamers/)).

## 4. The open standards layer matured, quietly

| Piece | Status (verified 2026-11-15) |
|---|---|
| W3C Verifiable Credentials Data Model 2.0 | W3C Recommendation, 15 May 2025 ([W3C](https://www.w3.org/TR/vc-data-model-2.0/)) |
| W3C Bitstring Status List 1.0 (revocation) | W3C Recommendation, 15 May 2025 ([W3C](https://www.w3.org/TR/vc-bitstring-status-list/)) |
| Decentralized Identifiers (DID) 1.0 / 1.1 | 1.0 Recommendation July 2022; 1.1 Candidate Recommendation Snapshot, 5 March 2026 ([W3C 1.0](https://www.w3.org/TR/did-1.0/); [W3C 1.1](https://www.w3.org/TR/did-1.1/)) |
| OpenID for Verifiable Presentations 1.0 | Final, 9 July 2025 ([OpenID](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)) |
| OpenID for Verifiable Credential Issuance 1.0 | Final, 16 September 2025 ([OpenID](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)) |
| Selective Disclosure for JWTs (SD-JWT) | RFC 9901 ([RFC Editor](https://www.rfc-editor.org/rfc/rfc9901.html)) |
| Open Badges 3.0 (achievement credentials) | 1EdTech standard built on Verifiable Credentials 2.0; document revised June 2026 ([1EdTech](https://www.imsglobal.org/spec/ob/v3p0)) |
| VRM 1.0 avatar format | Stable. In October 2024 Khronos and the VRM Consortium agreed to collaborate ([Khronos](https://www.khronos.org/news/press/the-khronos-group-and-vrm-consortium-collaborate-to-advance-international-standardization-of-the-vrm-3d-avatar-file-format)). A Khronos Character and Avatar group formed in October 2025, with its first extensions planned for review in late 2026 ([Khronos SIGGRAPH 2026 slides](https://www.khronos.org/assets/uploads/developers/presentations/glTF_2_1_and_Beyond_-_SIGGRAPH_Jul26.pdf)) |
| OMI glTF extensions | Active. `KHR_audio_emitter` graduated to Khronos; physics, spawn points and seats are in progress. The identity-related extensions are archived ([OMI](https://github.com/omigroup/gltf-extensions)) |

The full picture is in [standards-map.md](standards-map.md). The pattern is clear: **each layer has a mature or maturing standard, but no one has assembled them into a gaming profile.**

## 5. Open-source worlds: small but alive

Repository activity, read from the GitHub API on 2026-11-15:

| Repository | What it is | Stars | Last push | Reading |
|---|---|---|---|---|
| [KhronosGroup/glTF](https://github.com/KhronosGroup/glTF) | glTF specification | 7,891 | 2026-11-15 | Active |
| [omigroup/gltf-extensions](https://github.com/omigroup/gltf-extensions) | OMI glTF extensions | 58 | 2026-11-15 | Active |
| [omigroup/omi-godot](https://github.com/omigroup/omi-godot) | Godot implementation of OMI extensions | 11 | 2026-11-15 | Active |
| [vrm-c/vrm-specification](https://github.com/vrm-c/vrm-specification) | VRM specification | 348 | 2026-10-02 | Active |
| [vrm-c/UniVRM](https://github.com/vrm-c/UniVRM) | VRM for Unity | 3,423 | 2026-10-19 | Active |
| [pixiv/three-vrm](https://github.com/pixiv/three-vrm) | VRM for three.js (web) | 2,290 | 2026-10-22 | Active |
| [V-Sekai/godot-vrm](https://github.com/V-Sekai/godot-vrm) | VRM for Godot | 482 | 2026-07-08 | Active |
| [w3c/vc-data-model](https://github.com/w3c/vc-data-model) | Verifiable Credentials specification | 376 | 2026-11-05 | Active |
| [1EdTech/openbadges-specification](https://github.com/1EdTech/openbadges-specification) | Open Badges specification | 206 | 2026-11-13 | Active |
| [decentralized-identity/didwebvh](https://github.com/decentralized-identity/didwebvh) | `did:webvh` method | 57 | 2026-11-02 | Active |
| [did-method-plc/did-method-plc](https://github.com/did-method-plc/did-method-plc) | `did:plc` method (AT Protocol) | 337 | 2026-10-28 | Active |
| [overte-org/overte](https://github.com/overte-org/overte) | Open-source social VR | 287 | 2026-11-14 | Active |
| [Hubs-Foundation/hubs](https://github.com/Hubs-Foundation/hubs) | Self-hostable web social worlds | 2,225 | 2026-10-29 | Active |
| [hyperfy-xyz/hyperfy](https://github.com/hyperfy-xyz/hyperfy) | Self-hostable web 3D worlds | 311 | 2026-04-21 | Slowing |
| [mml-io/mml](https://github.com/mml-io/mml) | Metaverse Markup Language | 137 | 2026-03-12 | Slowing |
| [oma3dao/iwps-specification](https://github.com/oma3dao/iwps-specification) | OMA3 Inter-World Portaling System | 4 | 2025-09-25 | Quiet |
| [ir-engine/ir-engine](https://github.com/ir-engine/ir-engine) | WebXR social engine | 106 | 2025-07-17 | Quiet |
| [matrix-org/thirdroom](https://github.com/matrix-org/thirdroom) | Matrix-based worlds | 658 | 2023-08-30 | Dormant |

"Last push" is the most recent push to any branch. It shows activity, not quality.

## 6. Regulators are paying attention

- **Virtual currencies:** in March 2025, EU consumer authorities published key principles for in-game virtual currencies, such as showing prices in real money ([European Commission](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/social-media-online-games-and-search-engines_en)).
- **The Digital Fairness Act:** proposed by the European Commission on 11 November 2026, according to law-firm analyses. It includes rules on paid virtual currencies and loot boxes, including protections for minors. It is a proposal, not yet law ([Ashurst](https://www.ashurstperkinscoie.com/en/insights/digital-fairness-act-brussels-takes-on-consumer-enforcement/); [Winston Taylor](https://www.winstontaylor.com/insights/the-eu-draft-digital-fairness-act-consumer-protection-for-the-digital-age)).
- **Game preservation:** the "Stop Destroying Videogames" European Citizens' Initiative was submitted in January 2026 with about 1.29 million verified signatures. In June 2026 the Commission declined to propose a binding law and opted for a voluntary code of conduct instead ([Lewis Silkin](https://www.lewissilkin.com/insights/2026/06/24/european-commission-stops-short-of-imposing-mandatory-requirements-following-citi-102n4yy)).
- **Digital identity and age checks:** EU member states must offer digital identity wallets by around the end of 2026, and the Commission has urged every member state to offer an age-verification app by 31 December 2026 ([European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-urges-member-states-rollout-eu-age-verification-app); [Inside Privacy](https://www.insideprivacy.com/minors/eu-sets-the-clock-on-age-verification-rollout-urged-by-end%E2%80%912026/)).
- **Children's privacy (US):** amendments to the COPPA Rule took effect in June 2025, with most compliance due by April 2026 ([Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-publishes-final-coppa-rule-amendments)).

More detail is in [legal-and-policy.md](legal-and-policy.md).

## 7. Demand for "be anyone, do anything" worlds is real

- **Roleplay servers.** Rockstar acquired Cfx.re, the team behind the FiveM and RedM roleplay platforms for GTA V and Red Dead Redemption 2, in August 2023 ([Game Developer](https://gamedeveloper.com/business/rockstar-acquires-community-roleplay-team-cfx-re)). Players there live persistent lives: they hold jobs, run businesses and serve in police and city governments.
- **Player politics.** EVE Online players elect a council every year. The 2026 election (CSM 21) drew 32,675 votes ([EVE Online](https://www.eveonline.com/news/view/heres-your-csm-21)).
- **Very large audiences.** The scale of Roblox and Fortnite shows that people want many experiences under one identity. Today that identity just happens to belong to the platform.

## What this means for the Internet of Games

1. **Don't compete with walled gardens on content.** Build the neutral layer they don't have an incentive to build.
2. **Don't invent new standards where good ones exist.** The work is *composition*: a gaming profile across Verifiable Credentials, DIDs, OpenID and glTF/VRM, plus working code.
3. **Don't depend on any company's service**, including ours. Ready Player Me showed what happens otherwise.
4. **Start where interoperability is an advantage, then grow toward every game.** Small and mid-size games, web games and open-source engines come first; the standard has to be ready for the biggest games too ([P-0030](../problems/P-0030-built-for-every-game.md)).
5. **Work upstream.** OMI, Khronos/VRM and the W3C and OpenID communities are active, so contribute to them instead of forking.
