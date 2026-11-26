---
id: P-0001
title: Neutral governance and an IP policy for specifications
layer: governance
phase: 0
status: open
difficulty: medium
champion: unassigned
related: [P-0002, P-0026]
last_reviewed: 2026-11-24
---

# P-0001: Neutral governance and an IP policy for specifications

**In one sentence:** a standard meant to connect competing games only works if no single company can control it (including this project's founders), and if contributors' patents and copyrights can't later be turned against the people implementing it.

## Why it matters

- Large companies avoid standards with unclear IP terms, and small studios can't afford to discover a patent problem after shipping.
- A "neutral" standard that one party can steer is just a walled garden with extra steps.
- Ready Player Me showed what happens when the cross-game layer belongs to one company ([prior-art.md](../docs/prior-art.md#ready-player-me)).

## What exists today

- **This repository** licenses code under Apache-2.0, which includes a patent license from contributors, and documents under CC BY 4.0. CC BY 4.0 explicitly **does not** license patents (section 2(b)(2) of [LICENSE-DOCS](../LICENSE-DOCS)). Specification text therefore needs its own policy.
- **OMI** develops glTF extensions as a W3C Community Group, and contributors sign the [W3C Community Contributor License Agreement](https://www.w3.org/community/about/process/cla/) before a proposal enters Stage 1 ([OMI process](https://github.com/omigroup/gltf-extensions)).
- **The Community Specification License** is a lightweight framework for developing specifications on GitHub with patent commitments built in ([Community Specification](https://github.com/CommunitySpecification/Community_Specification)).
- **The Open Web Foundation Agreement (OWFa 1.0)** is a patent and copyright commitment used for some open specifications ([Open Web Foundation](https://www.openwebfoundation.org/the-agreements/the-owf-1-0-agreements-granted-claims/owfa-1-0)).
- **A side-by-side comparison** of these agreements, with questions for a lawyer, is in a [spike](../docs/spikes/2026-11-24-specification-ip-policies.md).
- **Foundations and standards bodies** that could eventually host the work include the W3C (through Community Groups), DIF, the OpenID Foundation, Khronos and the Linux Foundation. The Metaverse Standards Forum coordinates between these bodies but is not a standards body itself ([Metaverse Standards Forum](https://metaverse-standards.org/)). How to take part in each, and what contributors agree to, is in [Working with upstream groups](../docs/upstream.md).

## Constraints

- Contributing must be easy: a DCO sign-off, not weeks of legal review.
- The choices must be compatible with later moving work upstream to OMI, W3C, DIF or Khronos.
- The rules must prevent capture by any single company, including the founder's ([design principle 5](../docs/design-principles.md#5-no-single-company-in-the-critical-path-including-us)).

## What "solved enough" looks like (Phase 0)

- [ ] [GOVERNANCE.md](../GOVERNANCE.md) adopted, covering roles, decisions, conflicts of interest and neutrality commitments
- [ ] A decision on the specification IP policy **before** the first normative spec text is merged
- [ ] Written criteria for when, and to where, the work moves to a neutral home

## Candidate directions

1. **Keep Apache-2.0 and CC BY 4.0 with the DCO, and add the Community Specification License for `/spec`.** Low friction, with patent commitments for specs.
2. **Develop the specs inside OMI or a W3C Community Group from the start.** This inherits an established CLA and community, at the cost of moving at their pace.
3. **Split by layer.** Identity and credential profiles go to DIF or the W3C Credentials Community Group, avatar and glTF work goes to OMI, Khronos or VRM, and this repository keeps the composition, test files and demos.
4. **Form a new foundation later** (for example under the Linux Foundation) if the community grows large enough to need one.

## Open questions

- **P-0001-Q1:** Which patent policy should govern specification text?
- **P-0001-Q2:** What size or adoption threshold should trigger moving to a neutral home, and which home?
- **P-0001-Q3:** Which anti-capture rules should we adopt, for example a cap on maintainers from any single employer?
- **P-0001-Q4:** Should there be a trademark policy for "compatible" claims ([OQ-2](../docs/open-questions.md#governance-and-funding))?

## How to help

- Compare how OMI, DIF work items and W3C Community Groups handle IP, and summarize the differences in a short table.
- If you've run an open standards effort before, share what you'd do differently.

## Decisions so far

- [ADR-0002](../docs/decisions/ADR-0002-license-code-apache-docs-cc-by.md): code is licensed under Apache-2.0 and documents under CC BY 4.0, with contributions under the DCO. The patent policy for specification text (P-0001-Q1) is still open.
- [ADR-0009](../docs/decisions/ADR-0009-say-which-license-covers-each-kind-of-file.md): each kind of file has its own license. Code samples and schemas in documents are also available under Apache-2.0, and test files are released under CC0.

## References

- [W3C Community Contributor License Agreement](https://www.w3.org/community/about/process/cla/)
- [Community Specification](https://github.com/CommunitySpecification/Community_Specification)
- [OWFa 1.0](https://www.openwebfoundation.org/the-agreements/the-owf-1-0-agreements-granted-claims/owfa-1-0)
- [Developer Certificate of Origin](https://developercertificate.org/)
