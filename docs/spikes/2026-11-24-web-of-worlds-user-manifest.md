# Spike: How does the Web of Worlds user manifest compare with our player passport?

*Date: 2026-11-24 · Problems: P-0003, P-0013, P-0017, P-0028, P-0029 · Time box: 1 day*

## Question

The Web of Worlds, an initiative of the Metaverse Standards Forum, proposes a portable "User Manifest" that carries a person's identity, avatar, preferences and assets between linked worlds ([prior art](../prior-art.md#web-of-worlds)). That's close to our player passport (working name). Before we design our own player document, where do the two designs agree, where do they differ, and how could this project relate to the initiative?

## Approach

We read the initiative's public material and compared it, concept by concept, with our layer model, design principles and problem docs:

- the whitepaper, dated 31 March 2026 and announced on 2 June 2026 ([whitepaper](https://webofworlds.github.io/initial_MSF_Whitepaper/gen/MSF-3DWebInterop_WoWWhitepaper.pdf); [announcement](https://metaverse-standards.org/news/blog/announcing-the-web-of-worlds-whitepaper-a-concrete-path-to-the-open-metaverse/))
- the draft API, version 0.0.1, last changed on 21 May 2026 ([repository](https://github.com/WebOfWorlds/WoWAPI); [user manifest API](https://github.com/WebOfWorlds/WoWAPI/blob/main/specification/OpenUserManifest/API.yaml))
- the initiative's home page and its list of implementations ([Web of Worlds](https://webofworlds.github.io/))
- the W3C and MSF breakout at TPAC on 30 October 2026 ([event](https://www.w3.org/events/meetings/437890c5-8be3-44d2-b5e8-d8cd2a69d847/); [meeting log](https://www.w3.org/2026/10/30-spatial-web-msf-irc))

## Findings

### 1. The two efforts aim at the same thing for people

Both want a person to move between independently run worlds without starting over, carrying what makes them recognizable, under their own control and private by default. The whitepaper's "Digital YOU" use case and our [mission](../problem-statement.md#the-mission) describe the same experience. Both build on the same standards: decentralized identifiers, W3C Verifiable Credentials and glTF, in line with [ADR-0004](../decisions/ADR-0004-compose-existing-open-standards.md).

### 2. The user manifest isn't specified yet

The whitepaper says the manifest will need standardizing so that wallets, issuers, verifiers and worlds read it the same way. The draft API's user manifest schema has only three fields (a name, an age as a number, and a link to an avatar file), behind a single read endpoint that returns the whole manifest. At the TPAC session, participants described the manifest as a lightweight record that points to data kept elsewhere, and asked whether a manifest, or something that connects identity and credentials, is the right mechanism at all. So there's no detailed design yet to adopt or to conflict with.

### 3. Concept by concept

| Web of Worlds concept | What it is | Our counterpart | Relationship |
|---|---|---|---|
| User Manifest | A JSON-LD file of metadata and links to a person's data: avatar and wearables, preferences, consent flags, credentials, profile fragments, privacy metadata, and also payment handles and NFT pointers | The player passport ([glossary](../glossary.md)) | **Same idea, different scope.** Theirs reaches into payments, digital goods and personal details; ours carries an identifier, appearance, claims and preferences, with economies deferred ([P-0020](../../problems/P-0020-connected-economies.md)) |
| User digital wallet | Holder software that keeps DIDs, private keys and private credentials, asks for consent and builds presentations with selective or derived proofs | The holder, or "passport app" ([layer model](../layer-model.md#the-roles)) | **Overlap.** Both are identity wallets. [ADR-0005](../decisions/ADR-0005-never-require-blockchains-tokens-or-wallets.md) rules out requiring a crypto wallet, not holder software, so this fits as long as no required path needs a blockchain |
| Public and private data, consent per item, data with a limited life | The person decides what a world may read without asking, what needs consent, and how long a world may keep it | Private by default, consent for each share ([P-0006](../../problems/P-0006-privacy-unlinkability.md)) | **Aligned** in principle. The draft schema's age field is a number; we use thresholds such as "over 13" and never a birthdate ([P-0007](../../problems/P-0007-age-and-eligibility.md)) |
| Verifiable Credentials, zero-knowledge proofs | Security and access items such as tickets and access cards, plus credentials | Signed claims about what a player did ([P-0013](../../problems/P-0013-portable-claims.md)) | **Overlap.** Same envelope. We add what a game needs on top: categories, coarse bands instead of exact numbers, and trust levels for offline issuers |
| Preferences | For example clothing per kind of experience, language and currency | Accessibility, comfort and control preferences ([P-0028](../../problems/P-0028-portable-preferences.md)) | **Overlap, different emphasis.** Theirs lean social and commercial; ours lean accessibility. A shared vocabulary could hold both |
| Avatar and wearables links | Links to assets in registered 3D formats (glTF, X3D, USD), resolved over the web or through DIDs | The avatar baseline ([P-0008](../../problems/P-0008-avatar-baseline.md)) | **Overlap, with a safety gap.** We require files with every resource embedded, budgets and license metadata ([P-0010](../../problems/P-0010-avatar-budgets-and-file-safety.md), [P-0011](../../problems/P-0011-rights-licensing-likeness.md)). Linked assets can change or disappear after a game has checked them |
| Personal information | Examples include a delivery address, clothing sizes and height | None | **Outside our scope.** Our privacy principle is to share the minimum a game needs ([design principle 6](../design-principles.md#6-private-by-default)) |
| Open Spatial World and its URI | Each world is an HTTP endpoint with one URI, from which people join, view or preview it | World addresses ([P-0029](../../problems/P-0029-world-addressing-and-links.md)) | **Overlap.** Our sketch also uses ordinary HTTPS addresses, but resolves them to a launch target per platform, because many games aren't web pages |
| Portals | Links from one world to an independent instance of another | World-to-world handoff ([P-0017](../../problems/P-0017-world-handoff.md)) | **Overlap.** Our handoff ticket adds who is arriving and which claims they chose to bring, with expiry and replay protection |
| Metaverse bookmarks | Addresses that capture a place, a viewpoint and even a moment | Places inside a world ([P-0029](../../problems/P-0029-world-addressing-and-links.md)) | **Overlap.** Their viewpoints and moments go beyond our sketch and are worth borrowing, with credit |
| AI agents using the same interfaces | Agents follow the same standards and methods as people | AI characters that travel ([P-0023](../../problems/P-0023-traveling-ai-characters.md)) | **Different problems.** Theirs are agents acting in worlds; ours are companions that carry memories |

### 4. What games need that the proposal doesn't cover yet

- **The receiving game decides what imported things mean.** Continuity as claims that each game interprets under its own rules, with no imported gameplay power ([ADR-0008](../decisions/ADR-0008-continuity-as-signed-claims-not-state.md), [P-0014](../../problems/P-0014-claim-interpretation.md)).
- **Imported avatars treated as untrusted input:** budgets, validation, license metadata and moderation hooks ([P-0010](../../problems/P-0010-avatar-budgets-and-file-safety.md), [P-0011](../../problems/P-0011-rights-licensing-likeness.md), [P-0012](../../problems/P-0012-moderating-imported-identity.md)).
- **Files that keep working offline and after shutdowns,** with offline verification ([P-0024](../../problems/P-0024-durability-when-services-die.md)). The draft API serves the manifest from an endpoint; our design starts from files the player holds ([design principle 1](../design-principles.md#1-file-first-service-optional)).
- **Native engines, consoles and stores,** not only browsers ([P-0021](../../problems/P-0021-platform-holder-rules.md), [P-0025](../../problems/P-0025-developer-adoption-cost.md)). The initiative's architecture is browser-first.
- **Age ratings and child safety** across games rated for everyone and for adults ([P-0007](../../problems/P-0007-age-and-eligibility.md)).
- **Linking existing game accounts** instead of replacing them ([P-0004](../../problems/P-0004-account-linking.md)), and conformance tests for games ([P-0026](../../problems/P-0026-conformance-and-interop-testing.md)).

### 5. Where the proposal meets our decisions

- **Composing existing standards:** fully aligned ([ADR-0004](../decisions/ADR-0004-compose-existing-open-standards.md)).
- **No required blockchain:** compatible if payment handles, NFT pointers and smart contracts stay optional fields ([ADR-0005](../decisions/ADR-0005-never-require-blockchains-tokens-or-wallets.md)).
- **Claims, not state:** the manifest points at assets and possessions, where we carry signed claims that each game interprets. These can coexist if a receiving game treats linked assets as offers it may accept, adapt or ignore ([ADR-0008](../decisions/ADR-0008-continuity-as-signed-claims-not-state.md)).

### 6. Where the work is heading

At TPAC, participants discussed whether the work should continue as an MSF initiative, a W3C incubation or interest group, or alongside the existing digital-twins interest group. They suggested a joint W3C, MSF and Khronos workshop to explore use cases and trade-offs before forming any group ([meeting log](https://www.w3.org/2026/10/30-spatial-web-msf-irc)). They also pointed to the MSF's "Universal Manifest" work as a reference for discovery and for linking arbitrary data, which is relevant to [P-0027](../../problems/P-0027-discovery.md).

## Limitations

- Both the whitepaper and the API are early drafts and will change. Every statement here describes them as of 24 November 2026.
- We read the meeting log rather than a recording of the session. We didn't open the shared mapping document or the slides, which are hosted on a document service.
- We haven't spoken to the initiative's participants, so we don't know their plans beyond the public record.
- We didn't run any of the listed implementations.

## Recommendation

There are three realistic ways to relate to the initiative. Choosing between them needs a decision record.

| Option | Gains | Costs |
|---|---|---|
| **A. Contribute a gaming profile to the user manifest** | One shared design across the open metaverse; builds upstream ([design principle 12](../design-principles.md#12-build-upstream)); access to the MSF's members | Moves at the initiative's pace and under its membership and IP terms; inherits a browser-first, JSON-LD design and a scope that includes payments and personal data |
| **B. Align now, stay separate for the moment** | We keep moving on game-specific needs while using the same building blocks, so our player document can map onto a user manifest field by field; we give feedback as the design forms | Two documents could drift apart; this needs ongoing contact to work |
| **C. Build independently and map later** | Fastest in the short term | Risks exactly the fragmentation our roadmap warns against ([ROADMAP.md](../../ROADMAP.md#what-would-change-this-roadmap)) |

**We recommend option B for now:** share our game requirements with the initiative, design the player document from the same building blocks with a field-by-field mapping in mind, and revisit option A when the proposed workshop happens or a formal group forms. Whatever the choice, credit the initiative wherever our design borrows from it, for example for viewpoints and moments in world addresses, and don't reuse its names for our own documents ([OQ-1](../open-questions.md#naming)).

## Sources

- Metaverse Standards Forum, [Web of Worlds whitepaper (PDF)](https://webofworlds.github.io/initial_MSF_Whitepaper/gen/MSF-3DWebInterop_WoWWhitepaper.pdf), dated 31 March 2026 · [announcement](https://metaverse-standards.org/news/blog/announcing-the-web-of-worlds-whitepaper-a-concrete-path-to-the-open-metaverse/), 2 June 2026
- Web of Worlds, [home page](https://webofworlds.github.io/) · [draft API repository](https://github.com/WebOfWorlds/WoWAPI), version 0.0.1, read through the GitHub API on 24 November 2026
- W3C, [TPAC 2026 breakout: mapping W3C standards to a Web of Worlds](https://www.w3.org/events/meetings/437890c5-8be3-44d2-b5e8-d8cd2a69d847/), 30 October 2026 · [meeting log](https://www.w3.org/2026/10/30-spatial-web-msf-irc)
