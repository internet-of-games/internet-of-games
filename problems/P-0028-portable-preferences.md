---
id: P-0028
title: Portable player preferences (accessibility, comfort and controls)
layer: identity
phase: 2
status: open
difficulty: low
champion: unassigned
related: [P-0002, P-0006]
last_reviewed: 2026-11-15
---

# P-0028: Portable player preferences (accessibility, comfort and controls)

**In one sentence:** players who rely on subtitles, color-vision modes, larger text, reduced motion or remapped controls have to set them up again in every game, which makes these preferences a low-risk, high-value first thing to carry between games.

## Why it matters

- **It helps players right away**, including players with disabilities, from the very first game that supports it.
- **It threatens no one's business:** no store, economy or license is involved. That makes it a strong early reason for a game to adopt the standard ([P-0002](P-0002-why-would-a-game-join.md)).
- **It's continuity players actually feel:** "this game already knows how I play".

## What exists today

- **System-level accessibility settings** on consoles and operating systems, which some games read. These are platform-specific.
- **Community guidance** on accessible game design, such as the [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/).
- **No portable, cross-platform format** for a player's game preferences.

## A sketch: a small, self-asserted settings vocabulary

- **Subtitles:** on or off, size, background
- **Text scale**
- **Color-vision mode:** protanopia, deuteranopia or tritanopia
- **Reduce motion, flashing and camera shake**
- **Hold vs. toggle** for held inputs
- **Preferred difficulty-assist hints**
- **Control remapping hints** (abstract actions such as "jump" and "interact", not device-specific buttons)

Each game maps these onto its own settings and ignores anything it doesn't support.

## Constraints

- **Sensitive data.** Accessibility preferences can reveal health information, so they're **never shared by default**, are disclosed per game with consent, and are kept on the device where possible ([P-0006](P-0006-privacy-unlinkability.md)).
- **Advisory, not binding.** A game applies them as defaults the player can change.
- **Developed with accessibility experts and disabled players.**

## What "solved enough" looks like (Phase 2)

- [ ] Preference vocabulary v0, reviewed by accessibility practitioners
- [ ] Both demo games apply the preferences on first launch, after consent
- [ ] A privacy review completed

## Open questions

- **P-0028-Q1:** Which settings belong in v0?
- **P-0028-Q2:** How can preferences be shared with as little exposure as possible, for example by applying them locally without sending them to a server?
- **P-0028-Q3:** How should control remapping work across very different control schemes?
- **P-0028-Q4:** Who should maintain the vocabulary over time?

## How to help

- Accessibility practitioners and players: propose and review the v0 vocabulary.
- Survey common accessibility settings across popular games (from public information).

## References

- [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/)
