---
id: P-0011
title: Rights, licensing and likeness
layer: appearance
phase: 1
status: open
difficulty: high
champion: unassigned
related: [P-0008, P-0009, P-0012, P-0019, P-0023]
last_reviewed: 2026-11-15
---

# P-0011: Rights, licensing and likeness

**In one sentence:** everything that travels needs a clear answer to "who owns this, and may this game show it?", and licensed content (leagues, films, music, brands, real people's likenesses) must never leak between games.

## Why it matters

- **Games don't own everything they show.** Sports games license teams and players for specific products ([why-not-yet §1](../docs/why-not-yet.md#1-the-licenses-dont-stretch)). Even tattoos on licensed athletes have led to lawsuits ([U.S. Copyright Office summary](https://www.copyright.gov/fair-use/summaries/Alexander-v-Take-Two-Interactive-Software-Inc-No-18-CV-966-S-D-Ill-Sept-25-2024.pdf)).
- **Players don't own what games sell them.** Game terms usually grant licenses, not ownership ([VGC](https://videogameschronicle.com/news/virtual-currencies-are-fictions-take-two-argues-in-microtransaction-theft-lawsuit)).
- **Avatars made in a game's own character creator** are usually built from that game's art, which the player can't export.
- **Players might upload infringing avatars** (famous characters, real people), and the games displaying them take on risk.

## What exists today

- **VRM license metadata.** A VRM file carries fields describing who may use the avatar and how ([VRM specification](https://github.com/vrm-c/vrm-specification)).
- **VRoid Hub** lets creators set usage conditions, and apps load avatars with consent through an API ([VRoid Hub API](https://developer.vroid.com/en/api)).
- **Licensing gates conversion even inside one company.** It limited which outfits could get LEGO styles in Fortnite ([Dexerto](https://dexerto.com/fortnite/fortnite-launches-over-1200-lego-skins-for-chapter-5-season-1-2412246)).
- **Notice-and-takedown regimes** for hosted content: the U.S. DMCA section 512 ([U.S. Copyright Office](https://www.copyright.gov/512/)) and the EU Digital Services Act ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/digital-services-act-package)).

## Constraints

- **License metadata is machine-readable and required.**
- **Default deny:** if the license is unclear, the avatar isn't displayed and the game falls back.
- **The portability matrix applies:** licensed content and a game's own assets never travel unless their owner explicitly allows it ([portability-matrix.md](../docs/portability-matrix.md)).
- **Real people's likenesses** follow each receiving game's policy, and impersonation is never allowed.

## What "solved enough" looks like (Phase 1)

- [ ] A license metadata profile (reusing VRM metadata and standard license identifiers such as CC0, CC BY and SPDX)
- [ ] Validator behavior defined for missing, unclear or restrictive licenses
- [ ] A plain-language page: "what you may not put in a passport"
- [ ] All demo avatars are original and CC0

## Candidate directions

1. **Use VRM's license metadata as is**, and add standard license identifiers for non-VRM assets.
2. **Optional export by the game.** A game can *choose* to let players export avatars made in its creator, under terms it sets.
3. **Takedown propagation.** A signed takedown notice that participating games can act on.

## Open questions

- **P-0011-Q1:** Should we encourage games to let players export avatars made in their creators, and on what terms?
- **P-0011-Q2:** How should takedowns propagate across games without becoming a censorship tool?
- **P-0011-Q3:** What's the rights status of AI-generated avatars, and how should they be labeled ([OQ-11](../docs/open-questions.md#people-and-safety))?
- **P-0011-Q4:** What should the policy be on likeness and impersonation?

## How to help

- People with media or IP law experience: review this doc. Public comments are welcome, but nothing here is legal advice.
- Map VRM license fields onto common license identifiers.

## References

- [VRM specification](https://github.com/vrm-c/vrm-specification) · [VRoid Hub API](https://developer.vroid.com/en/api)
- [legal-and-policy.md](../docs/legal-and-policy.md)
