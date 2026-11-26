# Open questions

*Last reviewed: 2026-11-15*

These are questions that cut across several problems. Questions that belong to a single problem live in that [problem doc](../problems/README.md), with an ID such as `P-0003-Q1`. Discuss these in GitHub Discussions and reference the ID (for example `OQ-1`).

## Naming

**OQ-1: What should the portable player document be called?**
"Player passport" is only a working name, and it can't become the final one. "PLAYER PASSPORT" is a registered U.S. trademark of Silicon Valley Exercise Analytics for athlete-management software (Reg. No. 6,598,438, registered in December 2021; [USPTO record](https://tsdr.uspto.gov/#caseNumber=88697709&caseType=SERIAL_NO&searchType=statusSearch)). "Passport" is also used for a web3 gaming identity product ([Immutable Passport](https://gamesbeat.com/immutable-passport-hits-200k-unique-web3-gamers/)), and trademark filings exist for similar terms such as "Universal Gamer Tag" ([Justia](https://trademark.justia.com/owners/random-games-company-inc-5004361)). Until we choose, use "player passport" only to describe the document, never as the name of a specification, schema, package, app or domain. We need a name that's distinctive, descriptive and not already claimed in the games or identity space, chosen before Phase 1 drafts its first profile. That rules out any product's trademark and any name from a fictional universe.

**OQ-2: Do we need a mark for "compatible" games?**
A clear "works with the Internet of Games" mark could help players and developers, but it needs rules about who can use it and how compatibility is tested ([P-0026](../problems/P-0026-conformance-and-interop-testing.md), [P-0001](../problems/P-0001-neutral-governance-and-ip.md)).

## Governance and funding

**OQ-3: Where should the specifications live long-term?**
Options include staying here, proposing parts to OMI (a W3C Community Group), to DIF or the W3C Credentials Community Group, or to a new foundation. See [P-0001](../problems/P-0001-neutral-governance-and-ip.md).

**OQ-4: How do we fund the work without being captured?**
Possibilities include grants for open internet infrastructure (for example, [NLnet](https://nlnet.nl/) funds open-source internet and identity work), sponsorship with neutrality rules, and in-kind contributions from studios. Every option needs a conflict-of-interest policy.

**OQ-5: How do we engage large publishers and platform holders?**
Their participation would help, but the standard must not be shaped around a single company's business. What can they contribute without taking control?

## Scope

**OQ-6: Should we support non-humanoid characters?**
These include creatures, vehicles, abstract shapes and characters that are a team rather than one person. VRM assumes a humanoid. Is "humanoid only" acceptable for Phase 1?

**OQ-7: One player, many characters?**
Should a passport hold several characters (personas), each with its own name, look and history? How does that interact with privacy ([P-0006](../problems/P-0006-privacy-unlinkability.md))?

**OQ-8: What should the first demo games be?**
They need to be small, different enough to prove the point, and fun enough to show people. Candidates include:
- a basketball management sim and a baseball management sim that share an athlete's career (the "connected sports universe" from the [vision](../VISION.md))
- a 3D adventure (Godot) and a 2D puzzle game (web)

## People and safety

**OQ-9: Can children have passports, and who controls them?**
How should guardian controls, age signals and consent work for minors ([P-0005](../problems/P-0005-key-recovery.md), [P-0007](../problems/P-0007-age-and-eligibility.md))?

**OQ-10: How do names work across languages and scripts?**
How should we handle display names in any script, games that only render some scripts, and names that look identical but use different characters?

**OQ-11: How should AI-generated avatars and content be labeled?**
Should passports or avatars carry provenance information, for example via [C2PA content credentials](https://c2pa.org/), so games and players know what was AI-generated? What are the rights implications ([P-0011](../problems/P-0011-rights-licensing-likeness.md))?

## Process

**OQ-12: How do we decide when a problem is "solved enough"?**
The current rule is that the problem's champion proposes it, there's a public review period, and a maintainer confirms. Is that enough once outside implementers depend on our decisions? See [GOVERNANCE.md](../GOVERNANCE.md).
