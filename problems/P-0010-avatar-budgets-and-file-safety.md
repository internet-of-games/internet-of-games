---
id: P-0010
title: Avatar budgets and file safety
layer: appearance
phase: 1
status: open
difficulty: medium
champion: unassigned
related: [P-0008, P-0012, P-0026]
last_reviewed: 2026-11-15
---

# P-0010: Avatar budgets and file safety

**In one sentence:** an imported avatar is untrusted input that can crash a game, wreck its frame rate or exploit its file parser, so we need budgets and validation that every game can rely on.

## Why it matters

- **Security.** 3D file loaders are attack surface. In one widely used glTF library, file paths inside an input file could trigger command injection ([CVE-2022-3008](https://nvd.nist.gov/vuln/detail/CVE-2022-3008)).
- **Performance.** A single extremely detailed avatar can drag down everyone's frame rate in a shared scene. Social VR platforms rank avatars by performance for exactly this reason ([VRChat performance ranking](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/)).
- **Behavior.** Khronos is developing glTF interactivity, which lets 3D files carry behavior. Future avatars might *do* things, not just look like things.

## What exists today

- **The Khronos glTF Validator** checks a file's structure ([Khronos glTF](https://www.khronos.org/gltf/)).
- **Platform-specific performance ranks** (polygons, materials, bones and so on), each tied to one platform's rules.
- **No shared, cross-engine budget profile.**

## Constraints

- **Several tiers** for mobile, PC and console (for example *Light*, *Standard* and *Heavy*).
- **Validation is deterministic:** the same file always gets the same result, everywhere.
- **No external references:** all resources are embedded, and nothing is fetched while a file loads.
- **No executable behavior in v0.**
- **Fail safe:** if a file is rejected, the game falls back to a 2D portrait or a default avatar, never a crash.

## What "solved enough" looks like (Phase 1)

- [ ] Budget tiers with numeric limits (file size, triangles, materials, textures and texture size, bones, morph targets, spring bones)
- [ ] A validator that enforces the tiers, with clear error messages
- [ ] A **malicious and edge-case test corpus**: oversized files, deeply nested nodes, external URLs, malformed buffers, zip-bomb-style textures
- [ ] Both demo games' loaders fuzzed against the corpus
- [ ] A "safe loading" guide for each target engine

## Candidate directions

1. **Our own tiered profile**, informed by existing platform rankings and engine limits.
2. **Adopt a Metaverse Standards Forum validation tool** if one emerges ([MSF](https://metaverse-standards.org/domain-groups/interoperable-characters-avatars/)).
3. **Load avatars in a sandbox**, for example parsing them in a WebAssembly module that's separate from game memory.

## Open questions

- **P-0010-Q1:** What are the exact numbers for each tier?
- **P-0010-Q2:** Should games automatically generate lower-detail versions on import?
- **P-0010-Q3:** Is sandboxed parsing practical in each engine?
- **P-0010-Q4:** Which features (spring bones, expressions) are allowed in the *Light* tier?

## How to help

- Contribute files to the malicious test corpus (synthetic only, CC0).
- Benchmark sample avatars on low-end hardware.

## References

- [CVE-2022-3008 (NVD)](https://nvd.nist.gov/vuln/detail/CVE-2022-3008)
- [VRChat avatar performance ranking](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/)
