# Spike: Which IP policy should govern our specification text?

*Date: 2026-11-24 · Problems: P-0001 · Time box: 1 day*

> **Not legal advice.** This spike compares public agreements so the community can ask better questions. The final choice should be reviewed by a lawyer who knows open-source and standards licensing.

## Question

Our documents are licensed under CC BY 4.0 and our code under Apache-2.0, with contributions certified under the Developer Certificate of Origin ([ADR-0002](../decisions/ADR-0002-license-code-apache-docs-cc-by.md)). CC BY 4.0 grants no patent rights, so specification text needs its own policy before the first normative text is merged ([P-0001](../../problems/P-0001-neutral-governance-and-ip.md), question P-0001-Q1). Which policy fits a neutral, easy-to-join project that may later move its work into a standards body?

## Approach

We read the official text of each realistic option and compared what it grants, who commits to what, and when:

- CC BY 4.0 and the DCO, as used today ([LICENSE-DOCS](../../LICENSE-DOCS); [DCO](https://developercertificate.org/))
- the Community Specification License 1.0 and its contributor agreement, governance and contribution policies ([repository](https://github.com/CommunitySpecification/Community_Specification))
- the W3C Community Contributor License Agreement and the W3C Community Final Specification Agreement, which W3C Community Groups, including OMI, use ([CLA](https://www.w3.org/community/about/process/cla/); [final specification agreement](https://www.w3.org/community/about/process/final/))
- the Open Web Foundation Agreement 1.0 ([OWFa 1.0](https://www.openwebfoundation.org/the-agreements/the-owf-1-0-agreements-granted-claims/owfa-1-0))

## Findings

### 1. What each option grants

| Option | Copyright in the specification text | Patent commitment | Who commits, and when |
|---|---|---|---|
| **CC BY 4.0 with the DCO** (today) | Anyone may copy and adapt it, with attribution | None: CC BY 4.0 says patent rights aren't licensed (section 2(b)(2)) | Contributors certify origin with each sign-off; nothing about patents |
| **Community Specification License 1.0** | Anyone may copy and adapt it, with attribution to the working group | Royalty-free patent licenses from contributors. For drafts, they cover claims needed to implement each contributor's own contributions; once the group approves a specification, they cover the whole approved specification. Implementers also license each other, and contributors additionally promise royalty-free licenses on reasonable and non-discriminatory terms | Contributors agree by making a contribution. Implementers get the patent license by indicating agreement, for example by shipping the license with their code or adding themselves to a notices file |
| **W3C Community Group agreements** | Under the contributor agreement, each contribution may be copied and adapted with attribution; under the final specification agreement, the whole specification | Royalty-free licenses for the essential claims in each contributor's own contributions, binding for the life of the patents. Signing the final specification agreement is voluntary and extends the commitment to the whole specification | Participants agree to the contributor agreement when they join the group. The final agreement is signed in response to a call for commitments |
| **OWFa 1.0** | Anyone may copy and adapt the specification, with attribution | A promise not to assert patent claims needed to implement the specification, plus a commitment to license them royalty-free on reasonable and non-discriminatory terms | Each signer commits for a named specification |

### 2. How they handle the hard cases

- **A contributor who later sues.** The Community Specification License and the OWFa end the licenses of anyone who sues over the covered patents. The W3C agreements allow the license to be suspended instead.
- **Changing your mind.** The Community Specification License lets a contributor exclude specific patent claims by notice within 45 days of a contribution, or before a draft is approved; a contributor who leaves keeps the commitments already made. The W3C contributor agreement lets a contributor withdraw a contribution within 45 days, and drops any contribution not included in the specification within 150 days.
- **Moving the work later.** The W3C agreements spell out what happens when a Community Group's work moves to a W3C Working Group: the commitments continue, under the W3C Patent Policy. The Community Specification governance policy requires the working group's approval before a specification is submitted to another standards body.
- **Employers.** The Community Specification contributor agreement asks each contributor to confirm they have their employer's permission when the employer holds relevant rights.

### 3. How each fits the way we work

| Option | Fits a GitHub pull-request workflow? | Extra steps for contributors | Extra steps for implementers, including game studios |
|---|---|---|---|
| CC BY 4.0 with the DCO | Yes | Sign off commits | None, but no patent protection |
| Community Specification License 1.0 | Yes; it was designed for repositories | Read and accept the agreements; confirm employer permission | Indicate agreement to receive the patent license, for example by including the license file |
| W3C Community Group agreements | Partly: participation runs through a W3C account and group membership | Join the group and accept the contributor agreement | None beyond following the specification |
| OWFa 1.0 | Yes, but there's no process attached | Sign for each specification, usually near its final version | None beyond following the specification |

### 4. Where each leaves the project

The Community Specification License keeps everything in this repository with the least ceremony, and it was developed through the Joint Development Foundation with the OWF agreements as one of its inspirations ([README](https://github.com/CommunitySpecification/Community_Specification/blob/main/Readme.md)). The W3C agreements are the natural choice if our specifications are written inside a W3C Community Group, for example together with the Web of Worlds work or a credentials group ([Web of Worlds comparison](2026-11-24-web-of-worlds-user-manifest.md)). The OWFa is a commitment, not a process, so it would need governance written around it.

### 5. Projects that moved to the Community Specification License later

Two specifications adopted the Community Specification License after starting under other licenses. Both kept earlier text under its original license instead of asking every earlier contributor to relicense:

- **SPDX** provides its specification under the Community Specification License 1.0. Portions from copyright holders who haven't contributed since the change stay under CC BY 3.0 ([SPDX specification license](https://github.com/spdx/spdx-spec/blob/development/v3.0.1/LICENSE)).
- **SLSA** puts content contributed after it adopted the Community Specification governance model under that license. Earlier portions from contributors who haven't contributed since stay under Apache-2.0 ([SLSA README](https://github.com/slsa-framework/slsa#license)).

The same path would be open to us: existing text stays under CC BY 4.0, and new specification text comes in under the new license. As we read the license, its patent commitments would cover only contributions made under it.

## Limitations

- We compared the agreements' texts, not how courts treat them, and we didn't consult a lawyer.
- We didn't read the W3C Patent Policy sections that both W3C agreements refer to, or the signing pages for those agreements.
- We didn't survey which specifications in our space use which agreement. The two examples in finding 5 come from software supply-chain standards.

## Recommendation

Decide where our specifications will live first, because that largely decides the policy:

- **If they stay in this repository,** the Community Specification License 1.0 is the closest fit: it works with pull requests, keeps the DCO's low friction, and covers the whole approved specification with royalty-free patent commitments. Keep Apache-2.0 for code, and say which license applies to schemas and test vectors.
- **If they're written in a W3C Community Group,** that group's agreements apply, and our own policy only needs to cover what stays here.

That choice depends on how we relate to the Web of Worlds and other upstream groups, which needs its own decision record. Before adopting either policy, a lawyer should answer these questions:

1. Can specification text move from CC BY 4.0 docs into a Community Specification repository without asking every earlier contributor? Our contributing guide promises the policy won't apply retroactively without their agreement. SPDX and SLSA kept earlier text under its original license (finding 5); would that work for us?
2. Does a DCO sign-off count as accepting the Community Specification agreements, or do we need a separate record?
3. How should we handle contributors whose employers may hold relevant patents?
4. What does a game studio have to do to receive the patent license, and is that realistic for a small team?
5. Which license should cover schemas, examples and test vectors: the specification license or Apache-2.0? For now, [ADR-0009](../decisions/ADR-0009-say-which-license-covers-each-kind-of-file.md) puts schemas and code samples under Apache-2.0 and test vectors under CC0.
6. If our work later moves to a W3C group or another standards body, what happens to commitments made under our policy?

## Sources

- Creative Commons, [CC BY 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode), section 2(b)(2), also in [LICENSE-DOCS](../../LICENSE-DOCS)
- [Developer Certificate of Origin](https://developercertificate.org/)
- Community Specification, [repository](https://github.com/CommunitySpecification/Community_Specification), read through the GitHub API on 24 November 2026: the license, contributor agreement, governance policy and contribution policy
- W3C, [Community Contributor License Agreement](https://www.w3.org/community/about/process/cla/) and [Community Final Specification Agreement](https://www.w3.org/community/about/process/final/), read on 24 November 2026
- Open Web Foundation, [OWFa 1.0](https://www.openwebfoundation.org/the-agreements/the-owf-1-0-agreements-granted-claims/owfa-1-0)
- SPDX, [specification license](https://github.com/spdx/spdx-spec/blob/development/v3.0.1/LICENSE), and SLSA, [README](https://github.com/slsa-framework/slsa#license), both read on 24 November 2026
