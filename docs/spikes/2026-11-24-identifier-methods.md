# Spike: Which identifier method should Phase 1 use?

*Date: 2026-11-24 · Problems: P-0003, P-0005, P-0006, P-0024 · Time box: 1 day*

## Question

Phase 1 needs a default identifier method, and a path to production ([P-0003](../../problems/P-0003-player-identifier.md), question P-0003-Q1). How do `did:key`, `did:web`, `did:webvh` and `did:plc` compare against P-0003's constraints, now that we know which signatures each engine can verify ([engine comparison](2026-11-24-signature-support-in-engines.md))?

## Approach

We read each method's specification and compared them on the constraints in P-0003: rotation and recovery without a new identifier, offline verification, hosting, per-game identifiers for privacy ([P-0006](../../problems/P-0006-privacy-unlinkability.md)), the signatures a game must verify, and what happens when a service disappears ([P-0024](../../problems/P-0024-durability-when-services-die.md)). The Web of Worlds proposal uses DIDs and DID resolvers but doesn't pick a method ([Web of Worlds comparison](2026-11-24-web-of-worlds-user-manifest.md)), so it doesn't narrow the choice.

## Findings

### 1. Side by side

| | `did:key` | `did:web` | `did:webvh` 1.0 | `did:plc` |
|---|---|---|---|---|
| **Change keys without a new identifier** | No: the identifier is the key | Yes, by editing the hosted document | Yes, with a verifiable history and optional pre-rotation keys | Yes, with rotation keys and a recovery window |
| **Needs a host or directory** | No | A web domain | A web host, which can be changed | The PLC directory |
| **Verify offline** | Always: the key is in the identifier | Only with a cached document | With a cached or carried copy of the log | With a cached operation log |
| **Per-game identifiers** | Free and instant | One path per game on a host, and the host sees them all | One log per game, each hosted | One registration per game in a public directory |
| **Signatures a game must check** | Whatever key type is used, for example P-256 | Whatever key types the document lists | Ed25519, with JSON canonicalization, for the log | ECDSA on P-256 or secp256k1, for operations |
| **If the service disappears** | Nothing to lose; a lost key loses the identifier | The identity goes with the domain | Survives a move to another host, if one exists | Updates stop until the directory is back |

The details behind the table:

- **`did:key`** expands deterministically into a DID document and doesn't support updating or deactivating it. Its own specification suggests methods with a registry where persistent identity, key rotation or recovery matter ([did:key](https://w3c-ccg.github.io/did-key-spec/)).
- **`did:web`** resolves to a document on a domain, so whoever controls the domain controls the identity ([standards map](../standards-map.md#identity-who-is-this-player)).
- **`did:webvh`** adds a self-certifying identifier derived from the first log entry, a verifiable chain of updates from creation to deactivation, and optional pre-rotation keys, host moves and witnesses ([did:webvh v1.0](https://identity.foundation/didwebvh/v1.0/)). Its log proofs must use the `eddsa-jcs-2022` suite.
- **`did:plc`** records signed operations in the central PLC directory, which checks them, including recovery time windows. An update can be undone by another rotation operation during a recovery window, currently 72 hours, and operations are encoded in DAG-CBOR for signing ([did:plc](https://web.plc.directory/spec/v0.1/did-plc)). The directory is moving to an independent organization ([AT Protocol blog](https://atproto.com/blog/plc-directory-org)).

### 2. What the comparison shows

- **Only `did:key` passes every offline test without caching.** It's also the only method that passes the cold-cache variant of the [kill-switch test](../kill-switch-test.md), and the only one where per-game identifiers cost nothing.
- **Only the registry-style methods meet P-0003's rotation constraint,** and that constraint matters for recovery ([P-0005](../../problems/P-0005-key-recovery.md)): with `did:key`, a lost key means a lost identifier, and credentials bound to it can't be presented any more.
- **Each registry-style method has a cost we already know.** `did:webvh` needs Ed25519 and canonicalization in every engine, plus a host for every identifier ([P-0003](../../problems/P-0003-player-identifier.md), question P-0003-Q2). `did:plc` puts one directory in the update path, and its operation logs are public, so per-game identifiers sharing a rotation key could be linked to each other. `did:web` ties the identity to a domain the player usually doesn't own.
- **Linking to existing accounts softens the rotation problem.** Because games keep their own accounts ([P-0004](../../problems/P-0004-account-linking.md)), a player who loses a per-game key can sign in the usual way and link a new one. What's lost are the credentials bound to the old key.

### 3. A combination worth testing

Use a cheap, private identifier per game, and a rotatable one only where a player wants a public persona:

- **Private mode:** a separate `did:key` for each game, created by the passport app with P-256 keys. Nothing to host, nothing to look up, and nothing to link across games ([P-0006](../../problems/P-0006-privacy-unlinkability.md)).
- **Public persona:** one `did:webvh` identifier with a verifiable history, hosted by a provider the player can leave.

This puts Ed25519 and hosting costs only on the players and games that use public personas. It needs testing against recovery (P-0005) and against how credentials move when a key changes.

## Limitations

- We compared specifications, not implementations, and we didn't measure resolution time or log sizes.
- The combination in section 3 is a design idea, not a tested one.
- Who hosts `did:webvh` identifiers for players without a domain (P-0003-Q2) is still open.

## Recommendation

- **For the Phase 1 demo, use `did:key` with P-256 keys.** It works offline in both Phase 1 engines with built-in cryptography, and it makes per-game identifiers trivial. Document its main limit plainly: no rotation, so a lost key loses the identifier and any credentials bound to it.
- **For production, explore the combination in section 3:** `did:key` per game for private mode, and `did:webvh` for public personas, behind one resolver that accepts an allow-list of methods (P-0003, direction 4).
- **Record the choice in a decision record,** and revisit it once recovery (P-0005) is designed in Phase 2.

## Sources

- W3C Credentials Community Group, [did:key method](https://w3c-ccg.github.io/did-key-spec/) · DIF, [did:webvh v1.0](https://identity.foundation/didwebvh/v1.0/) · [did:plc specification](https://web.plc.directory/spec/v0.1/did-plc) · AT Protocol, [independent PLC directory organization](https://atproto.com/blog/plc-directory-org), all read on 24 November 2026
- This repository: [engine signature comparison](2026-11-24-signature-support-in-engines.md), [Web of Worlds comparison](2026-11-24-web-of-worlds-user-manifest.md), [kill-switch test](../kill-switch-test.md), [standards map](../standards-map.md)
