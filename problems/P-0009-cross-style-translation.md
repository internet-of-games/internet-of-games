---
id: P-0009
title: Cross-style appearance translation
layer: appearance
phase: 2
status: open
difficulty: research
champion: unassigned
related: [P-0008, P-0011]
last_reviewed: 2026-11-15
---

# P-0009: Cross-style appearance translation

**In one sentence:** a realistic 3D avatar won't fit in a pixel-art game, a minifigure world or a stylized cartoon, so we need a way for each game to render "the same person" in its own art style.

## Why it matters

The [vision](../VISION.md) says games don't have to look alike. If appearance only travels as a 3D mesh, it can only travel between games with similar art styles. That would leave out most of the medium.

## What exists today

- **LEGO styles in Fortnite.** More than 1,200 outfits got hand-made LEGO versions, rolled out gradually, and licensing limited which could be converted ([PC Gamer](https://www.pcgamer.com/fortnite-is-adding-a-lego-themed-survival-crafting-mode-that-includes-lego-versions-of-over-1200-pre-existing-skins)). This is proof that even one company with full control has to *re-author* characters to change style.
- **Mii.** Characters defined by parameters render consistently across many games and styles on one platform ([Wikipedia](https://en.wikipedia.org/wiki/Mii)). This is proof that a *description* travels better than a mesh.
- **Character creators everywhere** use parameter sliders: body type, hair style, colors, accessories.
- **AI generation tools** can restyle images and 3D models, but the rights to their outputs are unsettled ([P-0011](P-0011-rights-licensing-likeness.md)).

## Idea: an appearance descriptor

A small, optional, style-independent description that the player controls. For example:

- build and height *class* (not measurements)
- skin tone from a palette
- hair style category and hair color
- eye color, facial hair
- signature colors and signature accessories
- mobility aids (wheelchair, prosthetics) and other features the player wants represented

Each game maps these traits onto its own art assets. The player can review the result ("Is this you?") and adjust it.

## Constraints

- **Not biometric.** It's a creative description chosen by the player, never generated from photos without explicit consent.
- **Inclusive vocabulary.** Developed with input from the communities being described; avoid stereotyped categories.
- **The receiving game is responsible** for its interpretation, and the player can override it.
- **No copyrighted reference images** in examples or test data.

## What "solved enough" looks like (Phase 2)

- [ ] Descriptor vocabulary v0, with documented design reasoning
- [ ] Two demo games with very different art styles render recognizably similar characters from the same descriptor
- [ ] A small, consent-based recognizability study: can players pick out "their" character?

## Candidate directions

1. **A hand-designed descriptor vocabulary**, with each game mapping it to its own assets.
2. **Deriving the descriptor automatically from the VRM file**, then letting the player edit it.
3. **AI-assisted style translation**, done locally by the receiving game, with clear provenance labels ([OQ-11](../docs/open-questions.md#people-and-safety)).

## Open questions

- **P-0009-Q1:** Which traits are universal enough to include?
- **P-0009-Q2:** How do we describe skin tone, hair texture, body shape and disability respectfully, and who should review the vocabulary?
- **P-0009-Q3:** Should AI-based style translation be in scope, and who owns its output?
- **P-0009-Q4:** Should the descriptor be derived from the 3D avatar, or be independent of it?

## How to help

- Survey how character creators in different genres define their parameters (from public information).
- Propose a first trait list and test it on original characters.

## References

- [LEGO styles in Fortnite (PC Gamer)](https://www.pcgamer.com/fortnite-is-adding-a-lego-themed-survival-crafting-mode-that-includes-lego-versions-of-over-1200-pre-existing-skins)
- [Mii (Wikipedia)](https://en.wikipedia.org/wiki/Mii)
