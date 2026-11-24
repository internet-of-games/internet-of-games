# Working with upstream groups

*Last reviewed: 2026-11-24. Membership terms and fees change often, so check each group's own pages before joining. This isn't legal advice.*

We build on other communities' standards instead of forking them ([design principle 12](design-principles.md#12-build-upstream)). For each group whose work we depend on, this page says what it owns that matters to us, how an outsider can take part, what that costs, and what you agree to when you contribute. The [standards map](standards-map.md) says which of their standards we use.

**Before you sign anything,** read the agreement in full. Most agreements include patent commitments, and some ask you to confirm that your employer agrees, so check your employment terms first.

## At a glance

| Group | What matters to us | Open to individuals? | Cost to take part | What contributors agree to | Our problems |
|---|---|---|---|---|---|
| [OMI](#omi) | glTF extensions for virtual worlds, such as spawn points and physics | Yes | Free | The W3C Community Contributor License Agreement | [P-0008](../problems/P-0008-avatar-baseline.md), [P-0017](../problems/P-0017-world-handoff.md), [P-0029](../problems/P-0029-world-addressing-and-links.md) |
| [W3C Credentials Community Group](#w3c-credentials-community-group) | Decentralized identifiers, credentials and related reports | Yes | Free | The W3C Community Contributor License Agreement | [P-0003](../problems/P-0003-player-identifier.md), [P-0013](../problems/P-0013-portable-claims.md), [P-0015](../problems/P-0015-issuer-trust-revocation.md) |
| [Decentralized Identity Foundation](#decentralized-identity-foundation) | Identifier methods, credentials and their tooling | Some: freelancers and sole founders, or feedback only | Free for small organizations and individuals; tiered for others | DIF's membership agreement | [P-0003](../problems/P-0003-player-identifier.md), [P-0005](../problems/P-0005-key-recovery.md), [P-0013](../problems/P-0013-portable-claims.md) |
| [OpenID Foundation](#openid-foundation) | OpenID4VP, OpenID4VCI and related credential protocols | Yes | Free to contribute; membership is optional and paid | The OpenID Contribution Agreement | [P-0004](../problems/P-0004-account-linking.md), [P-0013](../problems/P-0013-portable-claims.md) |
| [Khronos](#khronos) | glTF, and the character and avatar extensions being developed with the VRM Consortium | Through the public glTF repository; working groups need company membership | Free on GitHub; membership is paid | Khronos's contributor agreement for the repository; its IP framework for members | [P-0008](../problems/P-0008-avatar-baseline.md), [P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md), [P-0026](../problems/P-0026-conformance-and-interop-testing.md) |
| [VRM Consortium](#vrm-consortium) | The VRM avatar format and its license metadata | Through the public specification repository; members are organizations | Membership has an annual fee | No contributor agreement found for the repository | [P-0008](../problems/P-0008-avatar-baseline.md), [P-0011](../problems/P-0011-rights-licensing-likeness.md) |
| [Metaverse Standards Forum](#metaverse-standards-forum-and-the-web-of-worlds) | Coordination between standards bodies, and the Web of Worlds initiative | No; members are organizations | Free at the Participant level; tiered dues at the Principal level | Membership creates no patent licensing obligations | [P-0001](../problems/P-0001-neutral-governance-and-ip.md), [P-0027](../problems/P-0027-discovery.md), [P-0029](../problems/P-0029-world-addressing-and-links.md) |

## OMI

OMI, the Open Metaverse Interoperability Group, is a W3C Community Group whose specifications are glTF extensions and related standards for moving between virtual worlds ([W3C group page](https://www.w3.org/community/metaverse-interop/)). Its active extensions cover physics, audio, spawn points, seats, sky and vehicles; its identity-related extensions are archived ([extensions repository](https://github.com/omigroup/gltf-extensions)).

- **How to take part:** the GitHub organization and the Discord server are open to everyone, and the extensions group holds weekly meetings, with notes in GitHub Discussions. Substantive contributions require joining the W3C Community Group ([contributing guide](https://github.com/omigroup/gltf-extensions/blob/main/CONTRIBUTING.md)).
- **Cost:** joining needs a free W3C account; anyone may join ([W3C group page](https://www.w3.org/community/metaverse-interop/)).
- **Agreement:** the [W3C Community Contributor License Agreement](https://www.w3.org/community/about/process/cla/), accepted on joining. It gives a royalty-free copyright license to each contribution and a royalty-free patent commitment for the essential claims in it. Our [IP policy comparison](spikes/2026-11-24-specification-ip-policies.md) explains it in more detail.

## W3C Credentials Community Group

The group explores how credentials are created, stored, presented and verified under the user's control, including decentralized identity, and publishes reports such as Data Integrity ([group page](https://www.w3.org/community/credentials/)).

- **How to take part:** anyone may join. It has a public mailing list and a GitHub organization ([w3c-ccg](https://github.com/w3c-ccg)), and holds regular calls. A person who isn't affiliated with a W3C member can join as an individual; employees of W3C members join through their organization ([W3C Community Group FAQ](https://www.w3.org/community/about/faq/)).
- **Cost:** free, with a W3C account ([FAQ](https://www.w3.org/community/about/faq/)).
- **Agreement:** the same W3C Community Contributor License Agreement, plus a voluntary [final specification agreement](https://www.w3.org/community/about/process/final/) for finished reports.

## Decentralized Identity Foundation

DIF develops specifications and reference code for decentralized identity. Its working groups include Claims and Credentials, DID Methods, and Identifiers and Discovery ([working groups](https://identity.foundation/working-groups)).

- **How to take part:** the free Contributor level lets startups, small organizations, academics and non-profits join working-group meetings and consensus and contribute code. Individuals can join at that level if they're freelancers or sole founders, after signing an IP clearance as an individual. A free Feedback Only level, in a personal capacity, allows comments on published specifications but not meetings or technical contributions, and isn't open to people who are employed ([join page](https://identity.foundation/join/)).
- **Cost:** free at the Contributor and Feedback Only levels; tiered for Associate members ([join page](https://identity.foundation/join/)).
- **Agreement:** every level signs a DIF agreement. Its terms are in the [DIF Project Charter](https://github.com/decentralized-identity/org/blob/main/Org%20documents/Membership%20agreements/DIF%20Project%20Charter%20_4.0.3.pdf), linked from the join page.

## OpenID Foundation

The OpenID Foundation develops OpenID Connect and the OpenID for Verifiable Credentials protocols. Its Digital Credentials Protocols working group maintains the presentation and issuance specifications we cite ([working groups](https://openid.net/wg/)).

- **How to take part:** membership isn't required to contribute to a working group. Contributors sign the Contribution Agreement first, then join the mailing lists, issue trackers and regular calls ([working groups](https://openid.net/wg/); [foundation](https://openid.net/foundation/)).
- **Cost:** contributing is free. Membership is optional; individual membership was listed at $50 ([member benefits](https://openid.net/foundation/benefits-members/)).
- **Agreement:** the [Contribution Agreement](https://openid.net/intellectual-property/openid-foundation-contribution-agreements/), which brings in the foundation's IPR Policy and process. According to that page, the policy includes a copyright license in contributions and a patent non-assertion agreement.

## Khronos

Khronos maintains glTF through its 3D Formats Working Group, and is working with the VRM Consortium on avatar extensions ([glTF](https://www.khronos.org/gltf/)).

- **How to take part:** anyone can open issues and pull requests on the [glTF repository](https://github.com/KhronosGroup/glTF) after signing the Khronos contributor license agreement for that repository. Contributed specification text is licensed under CC BY 4.0 and other files under Apache-2.0 ([contributing guide](https://github.com/KhronosGroup/glTF/blob/main/CONTRIBUTING.adoc)). Khronos also lists a Discord channel and a community forum. Joining a working group requires company membership ([membership](https://www.khronos.org/members/)).
- **Cost:** the repository is free. Membership fees are tiered by type and size, for example $1,000 a year for academic members and from $4,000 a year for small companies ([membership](https://www.khronos.org/members/)).
- **Agreement:** members and adopters license each other royalty-free under the [Khronos IP framework](https://www.khronos.org/members/ip-framework), which covers conformant implementations of ratified specifications.

## VRM Consortium

The VRM Consortium, a Japanese general incorporated association, develops VRM, the glTF-based humanoid avatar format with built-in usage permissions ([VRM Consortium](https://vrm-consortium.org/en/)).

- **How to take part:** the [specification repository](https://github.com/vrm-c/vrm-specification) is public, with open issues. Membership is for organizations, at a voting level and a supporting level, through the Consortium's secretariat ([VRM Consortium](https://vrm-consortium.org/en/)).
- **Cost:** each membership level has an annual fee; the amount isn't published.
- **Agreement:** we found no contributor agreement for the specification repository. The [VRM Public License](https://vrm.dev/en/licenses/1.0/) is a license for avatar data, not for contributions.

## Metaverse Standards Forum and the Web of Worlds

The Forum coordinates requirements between standards bodies; it doesn't write standards or set IP terms itself ([FAQ](https://metaverse-standards.org/faq/)). Its Web of Worlds initiative, a subgroup of the Spatial Computing Working Group, is the closest effort to ours ([comparison](spikes/2026-11-24-web-of-worlds-user-manifest.md)).

- **How to take part:** membership is open to organizations; the Forum says it can't currently accept individual members ([Forum](https://metaverse-standards.org/)). The Web of Worlds working group runs through the members' portal, but its [API repository](https://github.com/WebOfWorlds/WoWAPI) and its implementations are public on GitHub under Apache-2.0 ([Web of Worlds](https://webofworlds.github.io/)).
- **Cost:** Participant membership is free; Principal dues depend on the organization's size ([members](https://metaverse-standards.org/members/)).
- **Agreement:** the Forum says participation creates no patent licensing obligations ([members](https://metaverse-standards.org/members/)).

## Where our work might live upstream

These are candidate homes, not decisions ([P-0001](../problems/P-0001-neutral-governance-and-ip.md), direction 3).

| Our work | Candidate homes |
|---|---|
| Avatar baseline, budgets and safety rules | Khronos and the VRM Consortium, through their public repositories |
| glTF extensions for arriving and moving between worlds | OMI |
| Identifier method choice and test vectors | DIF's identifier groups, the W3C Credentials Community Group |
| A gaming profile for achievement credentials | The W3C Credentials Community Group, DIF's Claims and Credentials group |
| How games present and receive credentials | The OpenID Foundation's Digital Credentials Protocols group |
| World addresses, links and manifests | The Web of Worlds initiative, OMI |
