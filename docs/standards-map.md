# Standards map

*Last reviewed: 2026-11-24. Statuses were read from the official pages on the review date.*

We do **not** plan to invent new low-level standards. Almost every layer of a portable player identity already has a mature or maturing open standard. What's missing is a **gaming profile** that composes them, plus implementations that game engines can actually use. This page maps the building blocks to the [layer model](layer-model.md).

The **Fit** column is our current thinking, not a decision. Decisions happen in the linked problem docs.

## Identity: who is this player?

| Standard | Steward | Status | Fit |
|---|---|---|---|
| [Decentralized Identifiers (DID) 1.0](https://www.w3.org/TR/did-1.0/) | W3C | Recommendation, July 2022 | The data model for a player identifier that no single company owns ([P-0003](../problems/P-0003-player-identifier.md)) |
| [DID 1.1](https://www.w3.org/TR/did-1.1/) | W3C | Candidate Recommendation Snapshot, 5 March 2026 | Track it; we expect to target 1.1 |
| `did:key` | W3C Credentials Community Group | Community specification, widely implemented | The simplest option: no hosting needed, but no key rotation. Good enough for prototypes |
| `did:web` | W3C Credentials Community Group | Community specification | Tied to a web domain; whoever controls the host controls the identity |
| [`did:webvh` 1.0](https://identity.foundation/didwebvh/v1.0/) | Decentralized Identity Foundation (DIF) | Version 1.0 | `did:web` plus a verifiable history, which adds key rotation and the ability to move hosts. A strong candidate |
| [`did:plc`](https://github.com/did-method-plc/did-method-plc) | AT Protocol / PLC directory | In production for Bluesky; the directory is moving to an independent organization ([blog](https://atproto.com/blog/plc-directory-org)) | Proven at consumer scale, with rotation and migration. Relies on one directory today |
| [Web Authentication (passkeys)](https://www.w3.org/TR/webauthn-2/) | W3C / FIDO Alliance | W3C Recommendation | Device-held keys that players already know how to use; useful for recovery ([P-0005](../problems/P-0005-key-recovery.md)) |

## Login and account linking: connecting to accounts games already have

| Standard | Steward | Status | Fit |
|---|---|---|---|
| OAuth 2.0 ([RFC 6749](https://www.rfc-editor.org/rfc/rfc6749.html)) and [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | IETF / OpenID Foundation | Final, ubiquitous | This is how games already log players in. We link to these accounts rather than replace them ([P-0004](../problems/P-0004-account-linking.md)) |
| [OpenID for Verifiable Presentations 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) | OpenID Foundation | Final, 9 July 2025 | How a player presents a passport or claims to a game |
| [Self-Issued OpenID Provider v2](https://openid.net/specs/openid-connect-self-issued-v2-1_0.html) | OpenID Foundation | Draft | A login where the player is their own identity provider. Worth watching |
| [W3C Digital Credentials](https://www.w3.org/TR/digital-credentials/) | W3C Federated Identity Working Group | Working Draft, 23 November 2026. "Level 1" is being prepared for Candidate Recommendation; privacy issues on unlinkability and unlinkable revocation are still open ([chairs' report](https://lists.w3.org/Archives/Public/public-fedid-wg/2026Nov/0001.html); [#279](https://github.com/w3c-fedid/digital-credentials/issues/279); [#280](https://github.com/w3c-fedid/digital-credentials/issues/280)) | How a web page asks the browser for a credential held in a wallet. The draft requires browsers to support OpenID4VP and ISO mobile-document presentation, and recommends issuance support. Useful for web games, but native engines don't go through a browser, so Phase 1 can't depend on it ([P-0004](../problems/P-0004-account-linking.md)) |

## History and claims: what has this player done?

| Standard | Steward | Status | Fit |
|---|---|---|---|
| [Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/) | W3C | Recommendation, 15 May 2025 | The envelope for any signed claim ([P-0013](../problems/P-0013-portable-claims.md)) |
| [Bitstring Status List 1.0](https://www.w3.org/TR/vc-bitstring-status-list/) | W3C | Recommendation, 15 May 2025 | Revocation and suspension of credentials with "herd privacy" ([P-0015](../problems/P-0015-issuer-trust-revocation.md)) |
| [SD-JWT, RFC 9901](https://www.rfc-editor.org/rfc/rfc9901.html) | IETF | Standards Track RFC | Selective disclosure: show one claim without the others ([P-0006](../problems/P-0006-privacy-unlinkability.md)) |
| [SD-JWT-based Verifiable Credentials](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) | IETF OAuth WG | Internet-Draft under IESG evaluation, with enough ballot positions to pass (revision 27, 16 November 2026) | A simpler JSON format for credentials. A possible alternative to the JSON-LD form |
| [OpenID for Verifiable Credential Issuance 1.0](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) | OpenID Foundation | Final, 16 September 2025 | How a game issues a credential into a player's passport |
| [Open Badges 3.0](https://www.imsglobal.org/spec/ob/v3p0) | 1EdTech | Standard built on Verifiable Credentials 2.0; document revised June 2026 | Already defines `AchievementCredential`, with issuer, criteria, image and evidence. The closest existing "achievement" vocabulary. Designed for education, so it needs a gaming profile |

## Appearance: what does this player look like?

| Standard | Steward | Status | Fit |
|---|---|---|---|
| [glTF 2.0](https://www.khronos.org/gltf/) | Khronos (also ISO/IEC 12113:2022) | Stable international standard | The base 3D format ([P-0008](../problems/P-0008-avatar-baseline.md)) |
| [glTF 2.1](https://www.khronos.org/events/gltf-2.1-town-hall) | Khronos | Draft, presented at a public town hall on 17 November 2026; every glTF 2.0 file stays valid ([Khronos](https://www.khronos.org/news/archives/introducing-gltf-2.1-with-complex-scenes)) | Adds scenes composed from several files, bounding volumes, thumbnails stored inside the file, and a binary container with 64-bit sizes. Composing by reference clashes with our rule that avatar files embed everything, and the bigger container removes the old size ceiling, so avatar budgets have to cap size themselves ([P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md)) |
| [VRM 1.0](https://github.com/vrm-c/vrm-specification) | VRM Consortium | Stable; implemented for Unity, the web (three.js) and Godot | The humanoid avatar profile on top of glTF: rig, expressions, look-at, spring bones and license metadata. Our likely Phase 1 baseline |
| Khronos character and avatar extensions | Khronos 3D Formats Working Group, with the VRM Consortium | In development. A Character and Avatar group formed in October 2025, and its first extensions (spring bones, toon shading, marking a model as a character) were planned for review in late 2026 ([slides](https://www.khronos.org/assets/uploads/developers/presentations/glTF_2_1_and_Beyond_-_SIGGRAPH_Jul26.pdf)) | Track it closely. Long term, our baseline should follow these |
| Interoperable Characters/Avatars Working Group | [Metaverse Standards Forum](https://metaverse-standards.org/domain-groups/interoperable-characters-avatars/) | Chartered in August 2023. Listed deliverables include an avatar translation framework, test assets and a validation tool | Coordinate with them; we should reuse their test assets rather than duplicate them |
| MPEG Avatar Representation Format | ISO/IEC MPEG | Presented to the Forum as a framework for avatar storage and exchange ([event](https://metaverse-standards.org/event/special-sdo-session-avatar-standards-communication/)) | Watch |
| OpenUSD | Alliance for OpenUSD | Widely used for authoring | Mainly a content-creation format; glTF is the delivery format for games |

## World behavior (adjacent to our scope)

| Standard | Steward | Status | Fit |
|---|---|---|---|
| [OMI glTF extensions](https://github.com/omigroup/gltf-extensions) | OMI (a W3C Community Group) | Stage 1: physics body, gravity, joint, shape and spawn point. Stage 2: seat. Graduated: `KHR_audio_emitter`. Archived: `OMI_link`, `OMI_personality`, `OMI_collider` | The right home for any glTF extensions we need, and a model process for staged maturity |
| [glTF interactivity (`KHR_interactivity`)](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_interactivity/Specification.adoc) | Khronos | Ratified ([extension registry](https://github.com/KhronosGroup/glTF/blob/main/extensions/README.md)) | Lets 3D files carry behavior graphs. That's powerful, but it means imported content can *do* things. Under our rule of no executable behavior in v0, avatar files can't carry it ([P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md)) |

## Presence and travel

| Standard | Steward | Status | Fit |
|---|---|---|---|
| [Inter-World Portaling System](https://github.com/oma3dao/iwps-specification) | OMA3 | Draft. Repository last updated September 2025 | The closest prior art for moving between worlds ([P-0017](../problems/P-0017-world-handoff.md)) |
| [ActivityPub](https://www.w3.org/TR/activitypub/) | W3C | Recommendation, January 2018 | A federated social protocol; an option for presence and friends ([P-0018](../problems/P-0018-friends-and-presence.md)) |
| [Matrix](https://spec.matrix.org/latest/) | Matrix.org Foundation | Stable specification | Federated messaging. Third Room used it for worlds |
| [AT Protocol](https://atproto.com/) | Bluesky and community | In production | Portable accounts and social graph at scale |

## Age and eligibility

| Standard or system | Steward | Status | Fit |
|---|---|---|---|
| EU age-verification solution | European Commission | Declared technically ready; member states urged to offer one by 31 December 2026 ([European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-urges-member-states-rollout-eu-age-verification-app)) | A privacy-preserving source of "over 18" proofs ([P-0007](../problems/P-0007-age-and-eligibility.md)) |
| EU Digital Identity Wallet | EU (the eIDAS framework) | Member states due to offer wallets by around the end of 2026 | A future source of trusted age and residency claims |
| Mobile driving licences (ISO/IEC 18013-5) | ISO/IEC | Published standard | Can prove an age threshold without revealing a birthdate |

## Efforts that span several layers

| Effort | Steward | Status | Fit |
|---|---|---|---|
| [Web of Worlds](https://webofworlds.github.io/) | Metaverse Standards Forum, Spatial Computing Working Group | A whitepaper (March 2026), a draft API and early implementations ([whitepaper](https://webofworlds.github.io/initial_MSF_Whitepaper/gen/MSF-3DWebInterop_WoWWhitepaper.pdf); [API](https://webofworlds.github.io/WoWAPI)) | Linked 3D worlds with a URI each, portals and "metaverse bookmarks", plus a portable User Manifest (identity, avatar, preferences and assets) built on DIDs, Verifiable Credentials and wallets. It's general-purpose, not specific to games. The closest effort to our whole stack, so we're comparing the two before designing further |

## Who to work with

| Organization | What they do | How we relate |
|---|---|---|
| [Metaverse Standards Forum](https://metaverse-standards.org/) | Coordinates standards bodies; isn't one itself | Present our use case and reuse its test assets |
| [Web of Worlds](https://webofworlds.github.io/) | A Metaverse Standards Forum subgroup designing an open architecture for linked worlds | Compare designs and bring gaming requirements |
| [OMI](https://omigroup.org/) | glTF extensions for open worlds; a W3C Community Group | Propose glTF-level work there |
| [Khronos](https://www.khronos.org/gltf/) and the [VRM Consortium](https://vrm-consortium.org/en/) | glTF and VRM; avatar extensions | Follow and implement them, and give feedback from game use cases |
| [W3C Credentials Community Group](https://www.w3.org/community/credentials/) | DIDs and Verifiable Credentials | Propose a gaming credential profile |
| [Decentralized Identity Foundation](https://identity.foundation/) | DID methods, interoperability work | Choose a DID method and contribute test cases |
| [OpenID Foundation](https://openid.net/) | OpenID for Verifiable Credentials and Presentations; conformance testing | Use their protocols and conformance suites |
| [1EdTech](https://www.1edtech.org/) | Open Badges | Explore an Open Badges profile for games |

## Gaps: what doesn't exist yet

1. **A gaming credential profile.** Achievements, milestones and ranks expressed as Verifiable Credentials or Open Badges with game-appropriate fields and privacy defaults ([P-0013](../problems/P-0013-portable-claims.md)).
2. **A portable player document** that combines an identifier, an avatar reference, claims and preferences into one small file ([P-0003](../problems/P-0003-player-identifier.md), [P-0008](../problems/P-0008-avatar-baseline.md), [P-0013](../problems/P-0013-portable-claims.md)). The Web of Worlds User Manifest is a general-purpose proposal for this, and a gaming profile might build on it.
3. **A style-independent appearance description**, so games with different art styles can draw "the same person" ([P-0009](../problems/P-0009-cross-style-translation.md)).
4. **A shared avatar safety and budget profile** that works across engines ([P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md)).
5. **Conventions for interpreting foreign claims** ([P-0014](../problems/P-0014-claim-interpretation.md)).
6. **Engine-native libraries.** DID and credential tooling exists mostly for web and server languages, not for GDScript, Unity C# or Unreal C++ ([P-0025](../problems/P-0025-developer-adoption-cost.md)).
