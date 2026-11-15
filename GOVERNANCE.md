# Governance

*This is an early-stage governance model for Phase 0. We expect it to change as the community grows. Changes to this file follow the decision process below.*

## Principles

1. **Neutrality.** No single company, including any founder's employer, can control the project's direction ([design principle 5](docs/design-principles.md#5-no-single-company-in-the-critical-path-including-us)).
2. **Transparency.** Decisions are made in public, in GitHub issues, pull requests and Discussions, and are recorded there.
3. **Evidence over authority.** Arguments backed by sources, data or working code carry more weight than titles.
4. **Build upstream.** When another standards community owns a layer, we contribute there ([design principle 12](docs/design-principles.md#12-build-upstream)).

## Roles

| Role | Who | Responsibilities |
|---|---|---|
| **Contributor** | Anyone who participates | Discuss, open issues, send pull requests |
| **Champion** | A contributor who volunteers to drive a specific problem | Gather evidence, propose directions, run discussions, keep the problem doc up to date |
| **Maintainer** | Listed in [MAINTAINERS.md](MAINTAINERS.md) | Review and merge, triage, enforce the Code of Conduct, make decisions when consensus fails |
| **Founder** | [@acterra12](https://github.com/acterra12) | During Phase 0, acts as the lead maintainer and breaks ties |

**Becoming a maintainer:** after sustained, high-quality contributions, any maintainer can nominate a contributor, and the existing maintainers confirm by lazy consensus (see below).

## How decisions are made

1. **Lazy consensus.** Propose a change in a pull request or Discussion. If there are no unresolved objections after **7 days**, a maintainer may merge it.
2. **Objections must be specific** and, where possible, come with an alternative.
3. **If consensus fails**, the maintainers decide by majority vote. During Phase 0 the founder breaks ties. Every decision is recorded with its reasoning.
4. **Moving a problem to `solved-enough`** requires the champion's proposal, a public review period of at least 14 days, and approval from a maintainer who isn't the champion.

## Conflicts of interest

Maintainers and champions disclose any affiliation relevant to their area, such as an employer that builds a competing product. Disclosures go in [MAINTAINERS.md](MAINTAINERS.md) or on the relevant problem doc.

## Path to a neutral home

Phase 0 runs from this GitHub organization. When the community grows, or when outside implementers rely on our specifications, we'll look at moving the work to a neutral foundation or into existing standards bodies, as discussed in [P-0001](problems/P-0001-neutral-governance-and-ip.md). Our anti-capture goal is that **no single employer should account for a majority of maintainers** once there are three or more.

## Code of Conduct enforcement

Maintainers enforce the [Code of Conduct](CODE_OF_CONDUCT.md). A maintainer who is involved in a report steps aside from handling it.

## Changing this document

Changes to governance follow the lazy-consensus process, with a minimum review period of **14 days**.
