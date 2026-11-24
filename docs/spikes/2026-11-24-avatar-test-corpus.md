# Spike: What should the malicious and edge-case avatar test files cover?

*Date: 2026-11-24 · Problems: P-0010, P-0026 · Time box: 1 day*

## Question

Phase 1 must show that malformed, oversized or hostile avatars are rejected safely by both demo games and the validator ([problem statement](../problem-statement.md#what-success-looks-like-for-phase-1), criterion 7). Which cases does the test corpus need, how should each file be made, and how do we share hostile files safely ([P-0026](../../problems/P-0026-conformance-and-interop-testing.md), question P-0026-Q3)?

## Approach

We started from the proposed v0 file rules and budgets ([avatar budgets and file rules](2026-11-24-avatar-budgets-and-file-rules.md)), the structure of binary glTF 2.0 ([specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)), the VRM 1.0 requirements ([specification](https://github.com/vrm-c/vrm-specification/tree/master/specification/VRMC_vrm-1.0)), and the kinds of loader bugs our threat model names, such as file paths inside a glTF file triggering command injection ([CVE-2022-3008](https://nvd.nist.gov/vuln/detail/CVE-2022-3008); [threat model, T5](../threat-model.md#t5-malicious-or-harmful-content)). For each rule we listed the inputs that try to break it.

## Findings

### 1. Each case is one change to a valid avatar

Every test file starts from the same small, valid, original avatar and applies exactly one change. When a file is rejected, the reason is unambiguous, and each rule gets tested on its own. Each case also has a boundary pair: one file exactly at a limit, which must pass, and one just over it, which must fail. That tests that validation is deterministic.

### 2. The cases

| Area | Case | Expected result |
|---|---|---|
| Container | The header's length is larger than the tier's file budget | Rejected before anything else is parsed |
| Container | The header's length doesn't match the real file size (truncated or padded) | Rejected |
| Container | Container version 3, from the glTF 2.1 draft | Rejected in v0 |
| Container | Chunk lengths that run past the end of the file, or misaligned chunks | Rejected |
| Structure | Node hierarchies nested thousands of levels deep | Rejected at a depth limit, without stack overflow |
| Structure | A node that is its own ancestor | Rejected; glTF node hierarchies can't contain cycles |
| Structure | Very large counts of nodes, meshes, accessors or materials | Rejected by count before memory is allocated |
| Structure | Indices that point outside their arrays | Rejected |
| Extensions | An unknown extension listed as required | Rejected |
| Extensions | An unknown optional extension | Ignored, and the avatar still loads |
| Extensions | `KHR_interactivity` or another behavior extension, required or optional | Rejected; no behavior in v0 |
| References | A `uri` pointing to a web address, a local path, a path that climbs out of a folder, or a data URI | Rejected; v0 files contain no `uri` at all |
| Data | Accessors or buffer views that read past the end of their buffer | Rejected |
| Data | Malformed sparse accessors | Rejected |
| Data | Triangle indices that point past the last vertex | Rejected |
| Data | Infinite or not-a-number values in positions, normals or weights | Rejected |
| Skinning | More than four joint influences per vertex (a second joint set) | Rejected in v0 |
| Images | A tiny compressed image that declares enormous dimensions (a decompression bomb) | Rejected from the image header, before decoding |
| Images | An image larger than the tier's largest side | Rejected |
| Images | Corrupt image data, or a declared type that doesn't match the data | Rejected without a crash |
| VRM | The VRM extension missing | Rejected |
| VRM | A required humanoid bone missing | Rejected |
| VRM | License fields or the thumbnail missing | Rejected |
| Budgets | Each limit exactly met, and exceeded by one (triangles, texture memory, materials, bones, spring-bone joints) | Accepted at the limit, rejected over it, or assigned to the next tier up, as the game chooses |

### 3. What a game does when it rejects a file

The game never crashes and never hangs. It shows the player's 2D portrait or a default avatar instead, and tells the player why, in words they can act on ([P-0012](../../problems/P-0012-moderating-imported-identity.md)). The validator reports the rule each file broke, so the reason is the same in every engine.

### 4. Making and sharing the files safely

- **Generate, don't collect.** A script builds every case from the valid base avatar, so the corpus contains no real-world malware and no third-party content. The script and its output are released under CC0, like all our test assets ([sourcing and originality](../sourcing-and-originality.md)).
- **Publish the generator and a manifest, not a pile of binaries.** A manifest lists each case, what it changes and the expected result, so conformance tests can read it (P-0026-Q3). Anyone can regenerate the files, and security scanners have nothing opaque to worry about.
- **Use the files as fuzzing seeds** for each demo game's loader, as P-0010's success criteria require ([P-0010](../../problems/P-0010-avatar-budgets-and-file-safety.md)).
- **Report real bugs privately.** If a case crashes a third-party loader, report it to that project through its own security process before publishing details ([SECURITY.md](../../SECURITY.md)).

## Limitations

- The list comes from the file rules and the formats, not from fuzzing results yet. Fuzzing will find cases nobody thought of.
- Limits such as the maximum node depth aren't chosen yet. Each needs an initial value and a test.
- Engine-specific importers may add their own risks, for example in how they handle materials.

## Recommendation

- Build the generator and manifest alongside the validator, starting with the container and reference cases, which carry the highest risk.
- Add a maximum node depth and maximum counts to the v0 file rules, with initial values.
- Fuzz both demo games' loaders with the corpus before declaring Phase 1 done.

## Sources

- Khronos, [glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html) · VRM Consortium, [VRM 1.0 specification](https://github.com/vrm-c/vrm-specification/tree/master/specification/VRMC_vrm-1.0)
- NIST, [CVE-2022-3008](https://nvd.nist.gov/vuln/detail/CVE-2022-3008)
- This repository: [avatar budgets and file rules](2026-11-24-avatar-budgets-and-file-rules.md), [threat model](../threat-model.md), [P-0010](../../problems/P-0010-avatar-budgets-and-file-safety.md), [P-0026](../../problems/P-0026-conformance-and-interop-testing.md)
