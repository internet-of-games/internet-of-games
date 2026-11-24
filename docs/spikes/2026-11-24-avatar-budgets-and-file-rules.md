# Spike: What budgets and file rules should the v0 avatar baseline use?

*Date: 2026-11-24 · Problems: P-0008, P-0010, P-0011 · Time box: 1 day*

## Question

An imported avatar is untrusted input, and games need to know in advance what they might receive ([P-0010](../../problems/P-0010-avatar-budgets-and-file-safety.md)). What numeric budgets should the Light, Standard and Heavy tiers use (P-0010-Q1), and what exactly should a v0 avatar file be allowed to contain, now that glTF can carry behavior and the glTF 2.1 draft lets files reference other files (P-0010-Q5)?

## Approach

We looked for public, documented avatar limits and found one detailed source: VRChat's avatar performance ranks and size limits for PC and mobile ([performance ranks](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/); [size limits](https://creators.vrchat.com/avatars/avatar-size-limits/)). They're one platform's choices, built on Unity asset bundles, but they reflect years of experience with user avatars in shared scenes. We combined them with the rules of the formats themselves: glTF 2.0 ([specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)) and VRM 1.0 ([specification](https://github.com/vrm-c/vrm-specification/tree/master/specification/VRMC_vrm-1.0)).

## Findings

### 1. What the evidence says about budgets

- **Mobile is about four to seven times tighter than PC.** VRChat ranks a PC avatar "Good" at up to 70,000 triangles and 75 MB of texture memory, and a mobile avatar "Good" at up to 10,000 triangles and 18 MB ([performance ranks](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/)).
- **Draw calls matter as much as triangles.** The same ranks cap skinned meshes and material slots (each material slot adds draw calls), and mobile allows only one or two of each.
- **Secondary motion has a cost.** Bones moved by physics (VRChat's PhysBones, the same idea as VRM spring bones) have their own limits: up to 16 affected bones for a "Good" mobile avatar and 64 for a "Good" PC avatar.
- **Download size is capped separately:** 10 MB on Android and 200 MB on PC, with uncompressed limits of 40 MB and 500 MB ([size limits](https://creators.vrchat.com/avatars/avatar-size-limits/)).
- **Mobile users see "Medium" and better by default,** so VRChat's mobile "Medium" rank is effectively the practical ceiling there.
- **We found no public budget for morph targets** (blend shapes), which VRM uses for facial expressions.

### 2. What the formats already fix

- **A VRM 1.0 humanoid defines 55 bones, of which 15 are required** ([humanoid](https://github.com/vrm-c/vrm-specification/blob/master/specification/VRMC_vrm-1.0/humanoid.md)), so a bone budget of 150 leaves plenty of room for hair, clothes and accessories.
- **glTF lets clients support only one set of four joint weights per vertex**, and files with more may animate incorrectly on such clients ([glTF 2.0, skinned mesh attributes](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)).
- **A binary glTF file stores its total length in its header,** as a 32-bit number ([glTF 2.0, binary format](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)). A loader can compare that length with the budget before reading anything else. The draft glTF 2.1 removes that ceiling with a 64-bit container ([Khronos](https://www.khronos.org/events/gltf-2.1-town-hall)).
- **VRM's metadata already carries a thumbnail and license fields,** including who may use the avatar, commercial use, redistribution, modification, a license URL, and whether violent, sexual, political or religious, or antisocial use is allowed ([meta](https://github.com/vrm-c/vrm-specification/blob/master/specification/VRMC_vrm-1.0/meta.md)).
- **VRM 1.0 is a family of extensions:** the core avatar description (`VRMC_vrm`), spring bones, node constraints and the MToon toon material, plus newer additions ([specification folder](https://github.com/vrm-c/vrm-specification/tree/master/specification)).

### 3. Proposed tiers (initial values)

Each value is a starting point to test with sample avatars, not a decision.

| Limit | Light (phones, standalone headsets) | Standard (PC and consoles) | Heavy (high-end PC) | Basis |
|---|---|---|---|---|
| File size | 10 MB | 50 MB | 200 MB | VRChat's mobile and PC download limits for Light and Heavy; Standard is our guess, to measure |
| Triangles | 15,000 | 70,000 | 70,000 | VRChat mobile "Medium"; VRChat PC "Good" through "Poor" |
| Texture memory, decoded | 25 MB | 75 MB | 150 MB | VRChat mobile "Medium", PC "Good", PC "Poor" |
| Largest texture side | 1,024 px | 2,048 px | 4,096 px | Fits the memory budgets: a decoded 2,048 × 2,048 texture with mipmaps takes about 22 MB |
| Skinned meshes | 2 | 2 | 16 | VRChat mobile "Medium", PC "Good", PC "Poor" |
| Material slots | 2 | 8 | 32 | Same |
| Bones | 150 | 150 | 400 | Same |
| Spring-bone joints | 32 | 64 | 256 | VRChat's limits on bones affected by PhysBones |
| Joint influences per vertex | 4 | 4 | 4 | glTF clients may support only four |
| Morph targets | To measure | To measure | To measure | No public budget found |

### 4. Proposed v0 file rules

1. **One file:** binary glTF 2.0 in container version 2. Reject container version 3 and any file that references other files, until the baseline adopts glTF 2.1. That's a candidate answer to P-0010-Q5.
2. **Check size first:** compare the length in the header with the tier's file budget before parsing anything else.
3. **Everything embedded:** buffers come from the file's binary chunk and images from buffer views. No `uri` properties at all, so nothing is ever fetched.
4. **Images in PNG or JPEG only,** the two formats every glTF loader must handle. Compressed GPU textures can come later.
5. **An allowlist of extensions:** `VRMC_vrm` (required), `VRMC_springBone`, `VRMC_node_constraint`, `VRMC_materials_mtoon`, `KHR_materials_unlit` and `KHR_texture_transform`. Reject a file whose required extensions fall outside the list, and ignore other optional ones. Behavior extensions such as `KHR_interactivity` are never allowed in v0 ([P-0010](../../problems/P-0010-avatar-budgets-and-file-safety.md)).
6. **A complete humanoid:** all 15 required VRM bones, and at most one set of four joint weights per vertex.
7. **License fields and a thumbnail are required.** The license fields feed [P-0011](../../problems/P-0011-rights-licensing-likeness.md), which decides how games act on them. The thumbnail doubles as the 2D fallback portrait ([P-0008](../../problems/P-0008-avatar-baseline.md)).
8. **Deterministic results:** the same file gets the same result everywhere. Validators run the Khronos glTF Validator's checks plus these rules.

## Limitations

- VRChat's numbers come from one platform, one engine and one asset format, and mostly from social VR. Other genres may need different budgets.
- We haven't measured anything. Texture memory depends on formats and mipmaps, and file size depends on compression.
- We didn't find public budgets from game engines or consoles, and console figures are under NDA.
- The extension allowlist was drafted from the VRM specification, not tested against real avatars.

## Recommendation

- Add these values to P-0010 as candidates, and test them with the CC0 sample avatars and on low-end hardware before a decision record fixes them.
- Adopt the v0 file rules as the starting point for the validator and the malicious test files. Rejecting glTF 2.1 for now keeps v0 safe without closing the door.
- Measure morph-target costs on mobile before setting a budget, and add the question to P-0010 if it stays open.
- Credit VRChat's public ranks as the basis for these numbers wherever they appear.

## Sources

- VRChat, [Performance Ranks](https://creators.vrchat.com/avatars/avatar-performance-ranking-system/) and [Avatar Size Limits](https://creators.vrchat.com/avatars/avatar-size-limits/), read on 24 November 2026
- Khronos, [glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html) · [glTF 2.1 town hall](https://www.khronos.org/events/gltf-2.1-town-hall)
- VRM Consortium, [VRM 1.0 specification](https://github.com/vrm-c/vrm-specification/tree/master/specification): [humanoid](https://github.com/vrm-c/vrm-specification/blob/master/specification/VRMC_vrm-1.0/humanoid.md) and [meta](https://github.com/vrm-c/vrm-specification/blob/master/specification/VRMC_vrm-1.0/meta.md), read through the GitHub API on 24 November 2026
