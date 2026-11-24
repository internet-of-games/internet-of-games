---
id: P-0026
title: Conformance and interoperability testing
layer: cross-cutting
phase: 1
status: open
difficulty: medium
champion: unassigned
related: [P-0001, P-0010, P-0015, P-0025, P-0030]
last_reviewed: 2026-11-15
---

# P-0026: Conformance and interoperability testing

**In one sentence:** "compatible" has to mean something you can test, so we need shared test files, a validator, and regular events where implementations test against each other.

## Why it matters

Standards that can't be tested drift apart, with every implementation reading the spec a little differently. A standard also isn't real until two independent implementations work together ([design principle 9](../docs/design-principles.md#9-two-independent-implementations-before-anything-is-standard)).

## What exists today

- **OMI's staged process** requires implementations, glTF Validator support and sample assets before an extension can advance ([OMI](https://github.com/omigroup/gltf-extensions)).
- **Khronos maintains the glTF Validator** and sample models ([Khronos](https://www.khronos.org/gltf/)).
- **The OpenID Foundation runs conformance testing** for its protocols ([OpenID Foundation](https://openid.net/)).

## Plan

- **`test-vectors/`**: sample passports, avatars and credentials, valid *and* invalid (malformed, oversized, expired, revoked and forged). All synthetic and released under CC0.
- **A validator CLI** that checks a passport, an avatar or a credential against the profiles.
- **Conformance levels**, for example:
  - *Level 1: Recognize.* Read a passport and show the avatar or its fallback.
  - *Level 2: Verify.* Verify credentials and apply interpretation rules.
  - *Level 3: Issue.* Issue credentials and support revocation.
- **Interop events** where implementers test against each other and publish results.

## What "solved enough" looks like (Phase 1)

- [ ] Test vectors for every Phase 1 profile
- [ ] A validator CLI that runs locally and offline
- [ ] Both demo games pass Level 2, and Game A passes Level 3
- [ ] A results table published in this repository

## Open questions

- **P-0026-Q1:** Should a "compatible" mark exist, and who can use it ([OQ-2](../docs/open-questions.md#naming))?
- **P-0026-Q2:** Who maintains the test vectors, and how are changes reviewed?
- **P-0026-Q3:** How should the malicious-file corpus be shared safely ([P-0010](P-0010-avatar-budgets-and-file-safety.md))?
- **P-0026-Q4:** Should third-party implementations be able to run the conformance suite automatically?

## Champion brief

- **First deliverable:** The validator's command-line interface and output format, plus the first valid and invalid test files.
- **Decisions you'd drive:** whether a "compatible" mark exists (P-0026-Q1), who maintains the test files (P-0026-Q2) and how to share the malicious corpus (P-0026-Q3).
- **Helpful background:** test suites, interoperability events and specification work.
- **Commitment:** a few hours a week, until a proposal is ready for public review.

## How to help

- Write test vectors, especially invalid ones.
- Design the validator's command-line interface and output format.

## References

- [OMI glTF extensions](https://github.com/omigroup/gltf-extensions) · [Khronos glTF](https://www.khronos.org/gltf/)
