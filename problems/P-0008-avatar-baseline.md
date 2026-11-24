---
id: P-0008
title: A portable avatar baseline
layer: appearance
phase: 1
status: open
difficulty: medium
champion: unassigned
related: [P-0009, P-0010, P-0011]
last_reviewed: 2026-11-24
---

# P-0008: A portable avatar baseline

**In one sentence:** define the minimum avatar file that every participating game can load (format, rig, materials, metadata), plus what happens when a game can't use it.

## Why it matters

"Same character" starts with "same look". If every game needs a different file format, portable appearance never happens. Ready Player Me showed there's demand for cross-app avatars, and that **files in open formats** are the part that survives ([prior-art.md](../docs/prior-art.md#ready-player-me)).

## What exists today

- **glTF 2.0** is the royalty-free delivery format for 3D content, also published as ISO/IEC 12113:2022 ([Khronos](https://www.khronos.org/gltf/)).
- **VRM 1.0** builds on glTF to describe humanoid avatars: a standard bone layout, expressions, look-at, spring-bone physics for hair and clothes, and license metadata ([VRM specification](https://github.com/vrm-c/vrm-specification)).
- **There are implementations for three of our likely targets**, all active in 2026: [UniVRM](https://github.com/vrm-c/UniVRM) (Unity), [three-vrm](https://github.com/pixiv/three-vrm) (web) and [godot-vrm](https://github.com/V-Sekai/godot-vrm) (Godot).
- **Khronos and the VRM Consortium** are turning VRM concepts into general glTF avatar extensions. The first set was planned for review in late 2026 ([Khronos slides](https://www.khronos.org/assets/uploads/developers/presentations/glTF_2_1_and_Beyond_-_SIGGRAPH_Jul26.pdf)).
- **glTF 2.1** is in draft. Every glTF 2.0 file stays valid, and the revision adds scenes composed from several files, bounding volumes, thumbnails stored inside the file, and a binary container with 64-bit sizes ([Khronos](https://www.khronos.org/events/gltf-2.1-town-hall)). Those thumbnails could serve as the 2D fallback; composing an avatar from several files needs a safety decision first ([P-0010](P-0010-avatar-budgets-and-file-safety.md)).
- **The Metaverse Standards Forum's** Interoperable Characters/Avatars group lists an avatar translation framework, test assets and a validation tool among its deliverables ([MSF](https://metaverse-standards.org/domain-groups/interoperable-characters-avatars/)).

## Constraints

- **It must load in Godot, Unity, Unreal and on the web** (Unreal support needs investigating).
- **License metadata is required** ([P-0011](P-0011-rights-licensing-likeness.md)).
- **Budgets are required** ([P-0010](P-0010-avatar-budgets-and-file-safety.md)).
- **There's always a fallback:** a 2D portrait plus an appearance description ([P-0009](P-0009-cross-style-translation.md)).
- **All resources are embedded:** no external URLs inside the file.

## What "solved enough" looks like (Phase 1)

- [ ] An "Avatar Baseline v0" profile: a subset of VRM 1.0, plus required metadata, budgets and the 2D fallback
- [ ] At least three sample avatars, made for this project and released under CC0, with no third-party IP
- [ ] Validator checks for the profile
- [ ] The same sample avatar renders in both demo games

## Candidate directions

1. **VRM 1.0 now, and track the Khronos avatar extensions**, with a migration path when they're ratified.
2. **Plain glTF plus our own metadata.** Simpler, but it throws away VRM's rig and expression conventions.
3. **Wait for the Khronos extensions.** Cleaner in the long run, but it would stall Phase 1.

Our current lean is option 1.

## Open questions

- **P-0008-Q1:** Use VRM 1.0 now, or wait for the Khronos character extensions?
- **P-0008-Q2:** How should non-humanoid characters such as creatures and vehicles be handled ([OQ-6](../docs/open-questions.md#scope))?
- **P-0008-Q3:** What's the state of VRM support in Unreal, and who could help?
- **P-0008-Q4:** What should the baseline say about animation? Should games retarget their own animations, or should avatars carry some?

## How to help

- Make CC0 test avatars: original designs only, with no fan art of existing characters.
- Test the sample avatars in Godot, Unity, Unreal and three.js, and record what breaks.

## Decisions so far

- [ADR-0004](../docs/decisions/ADR-0004-compose-existing-open-standards.md): we build on existing open standards, so the avatar baseline starts from glTF and VRM rather than a new format.

## References

- [glTF](https://www.khronos.org/gltf/) · [VRM specification](https://github.com/vrm-c/vrm-specification)
- [Khronos and the VRM Consortium collaboration](https://www.khronos.org/news/press/the-khronos-group-and-vrm-consortium-collaborate-to-advance-international-standardization-of-the-vrm-3d-avatar-file-format)
