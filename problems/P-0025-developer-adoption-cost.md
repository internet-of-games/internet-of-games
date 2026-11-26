---
id: P-0025
title: Developer adoption cost
layer: cross-cutting
phase: 1
status: open
difficulty: medium
champion: unassigned
related: [P-0002, P-0026, P-0030]
last_reviewed: 2026-11-15
---

# P-0025: Developer adoption cost

**In one sentence:** if integrating takes more than a few days, nobody will do it, so adopting the Carryfile has to be cheaper than building your own character creator.

## Why it matters

Interoperability only pays off once many games support it, and every one of them has to decide it's worth the effort first ([P-0002](P-0002-why-would-a-game-join.md)). The most successful cross-game services are free and work with any engine. Epic Online Services is an example ([Epic](https://onlineservices.epicgames.com/)).

## What exists today

- **VRM loaders** exist for Unity ([UniVRM](https://github.com/vrm-c/UniVRM)), the web ([three-vrm](https://github.com/pixiv/three-vrm)) and Godot ([godot-vrm](https://github.com/V-Sekai/godot-vrm)).
- **Identifier and credential libraries** exist mostly for web and server languages (JavaScript/TypeScript, Rust, Go, Python, Java). Engine-native support in GDScript, Unity C# and Unreal C++ is thin.

## Targets

| Target | Phase |
|---|---|
| Godot (GDScript, with C# if useful) | 1 |
| Web (TypeScript, three.js) | 1 |
| Unity (C#) | 3 |
| Unreal (C++) | 3 |

- **"Hello Carryfile" in fewer than about 50 lines** of game code.
- **No server required** for the basic flow (recognize a player, load an avatar, verify a credential).
- **Clear errors** and **safe defaults** (budgets on, privacy on).

## What "solved enough" looks like (Phase 1)

- [ ] SDKs for Godot and the web, with quickstarts
- [ ] A developer who wasn't involved integrates the basics into a third small game in about a day, and writes up what was hard (this is success criterion 8 in the [problem statement](../docs/problem-statement.md#what-success-looks-like-for-phase-1))

## Candidate directions

1. **Native libraries per engine.** Most idiomatic, but the most work to maintain.
2. **A shared core compiled to WebAssembly**, wrapped for each engine. One implementation of the hard parts, at the cost of build complexity.
3. **A small native "Carryfile app"** that games talk to locally. Simple for games, but it adds an extra install for players.

## Open questions

- **P-0025-Q1:** Which signature algorithms can each engine verify out of the box?
- **P-0025-Q2:** Is a shared WebAssembly core practical for Godot, Unity and Unreal?
- **P-0025-Q3:** How do we keep cryptographic dependencies small and auditable?
- **P-0025-Q4:** What constraints do mobile platforms add?

## Champion brief

- **First deliverable:** A table of the signature algorithms each target engine can verify out of the box, and a sketch of the smallest "hello Carryfile" integration.
- **Decisions you'd drive:** native libraries or a shared WebAssembly core (P-0025-Q2), and how to keep dependencies small and auditable (P-0025-Q3).
- **Helpful background:** game development in Godot or on the web, and SDK design.
- **Commitment:** a few hours a week, until a proposal is ready for public review.

## How to help

- Check signature verification support in Godot, Unity and Unreal.
- Volunteer to be the "outside developer" who tests the integration time.

## References

- [design-principles.md §11](../docs/design-principles.md#11-integration-in-a-day)
