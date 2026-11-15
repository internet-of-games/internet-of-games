---
id: P-0005
title: Key loss and account recovery for ordinary players
layer: identity
phase: 2
status: open
difficulty: high
champion: unassigned
related: [P-0003, P-0007, P-0024]
last_reviewed: 2026-11-15
---

# P-0005: Key loss and account recovery for ordinary players

**In one sentence:** if losing a phone means losing your identity forever, ordinary players won't use the system, so recovery has to be as easy as "forgot password" without handing control to one company.

## Why it matters

Seed phrases and lost wallets taught the world that self-custody is hard. But if recovery is handled by one custodian, we've rebuilt a central account provider. The [problem statement](../docs/problem-statement.md) says no single company should be in the critical path, and players also need to be able to get back in.

## What exists today

- **Passkeys (Web Authentication):** device-held keys, synced across a person's devices by their platform vendor ([W3C WebAuthn](https://www.w3.org/TR/webauthn-2/)). Familiar to players, but each sync ecosystem belongs to a vendor.
- **`did:plc` rotation keys:** the AT Protocol's identifier method supports rotating keys, and a higher-priority recovery key can override recent changes within a time limit ([did:plc](https://github.com/did-method-plc/did-method-plc)).
- **`did:webvh` pre-rotation:** a commitment to the *next* key is published in advance, which limits the damage if the current key is stolen ([did:webvh](https://identity.foundation/didwebvh/v1.0/)).
- **Social or guardian recovery:** several trusted parties together approve a recovery. Common in wallet designs; usability varies.

## Constraints

- **No single party can seize a player's identity**, including a recovery provider.
- **It must work for children**, where a guardian manages recovery ([P-0007](P-0007-age-and-eligibility.md)).
- **Credentials issued to a player survive a key rotation**, because they're bound to the identifier, not to a single key.
- **It must be low-friction:** a few taps, not a 24-word phrase.

## What "solved enough" looks like (Phase 2)

- [ ] A recovery design document with a threat model covering theft, loss, coercion and a malicious recovery provider
- [ ] Two working recovery paths in the demo, for example a passkey-backed device key plus a recovery key held by a chosen provider or guardian
- [ ] A test showing previously issued credentials still verify after a key rotation

## Candidate directions

1. **Passkeys plus a choice of recovery providers**, with the ability to switch providers.
2. **Pre-rotation (`did:webvh`) plus an offline recovery code** for advanced users.
3. **Guardian recovery for minors and anyone who wants it.**

## Open questions

- **P-0005-Q1:** Are synced passkeys good enough as the default for most players?
- **P-0005-Q2:** How do guardians manage a child's identity, and how is control handed over when the child grows up?
- **P-0005-Q3:** How do we prevent a "recovery" flow from becoming the easiest way to steal an account?
- **P-0005-Q4:** What happens to an identity when its owner dies? Is that in scope?

## How to help

- Survey how mainstream apps handle passkey recovery, and the lessons from wallet recovery UX.
- Draft the recovery threat model.

## References

- [W3C Web Authentication](https://www.w3.org/TR/webauthn-2/)
- [did:plc](https://github.com/did-method-plc/did-method-plc) · [did:webvh v1.0](https://identity.foundation/didwebvh/v1.0/)
