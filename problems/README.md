# Problem index

Each problem doc describes one sub-problem of the [mission](../docs/problem-statement.md#the-mission): why it matters, what already exists, the constraints, what "solved enough" means, candidate directions, and numbered open questions.

**How to reference them:** use the ID, such as `P-0008`, or a question ID, such as `P-0008-Q2`, in issues, pull requests, discussions and commit messages.

## Phase 0: foundations

| ID | Problem | Layer | Difficulty | Status |
|---|---|---|---|---|
| [P-0001](P-0001-neutral-governance-and-ip.md) | Neutral governance and an IP policy for specifications | governance | medium | open |
| [P-0002](P-0002-why-would-a-game-join.md) | Why would a game join? | governance | high | open |

## Phase 1: same character, two games

| ID | Problem | Layer | Difficulty | Status |
|---|---|---|---|---|
| [P-0003](P-0003-player-identifier.md) | A player identifier that no single company owns | identity | medium | open |
| [P-0004](P-0004-account-linking.md) | Linking existing game accounts without a new account system | identity | medium | open |
| [P-0006](P-0006-privacy-unlinkability.md) | Privacy and unlinkability across games | identity | high | open |
| [P-0008](P-0008-avatar-baseline.md) | A portable avatar baseline | appearance | medium | open |
| [P-0010](P-0010-avatar-budgets-and-file-safety.md) | Avatar budgets and file safety | appearance | medium | open |
| [P-0011](P-0011-rights-licensing-likeness.md) | Rights, licensing and likeness | appearance | high | open |
| [P-0013](P-0013-portable-claims.md) | Portable achievement and history claims | history | medium | open |
| [P-0014](P-0014-claim-interpretation.md) | How a receiving game interprets foreign claims | history | medium | open |
| [P-0015](P-0015-issuer-trust-revocation.md) | Trusting issuers, revocation and cheating | history | high | open |
| [P-0024](P-0024-durability-when-services-die.md) | Durability when services die | cross-cutting | medium | open |
| [P-0025](P-0025-developer-adoption-cost.md) | Developer adoption cost | cross-cutting | medium | open |
| [P-0026](P-0026-conformance-and-interop-testing.md) | Conformance and interoperability testing | cross-cutting | medium | open |
| [P-0030](P-0030-built-for-every-game.md) | Built for every game | cross-cutting | high | open |

## Phase 2: travel, rewards and a third team

| ID | Problem | Layer | Difficulty | Status |
|---|---|---|---|---|
| [P-0005](P-0005-key-recovery.md) | Key loss and account recovery for ordinary players | identity | high | open |
| [P-0007](P-0007-age-and-eligibility.md) | Age and eligibility signals across games | identity | high | open |
| [P-0009](P-0009-cross-style-translation.md) | Cross-style appearance translation | appearance | research | open |
| [P-0012](P-0012-moderating-imported-identity.md) | Moderating imported names and avatars | appearance | high | open |
| [P-0017](P-0017-world-handoff.md) | World-to-world handoff | presence | medium | open |
| [P-0029](P-0029-world-addressing-and-links.md) | World addressing and links | presence | high | open |
| [P-0019](P-0019-cross-game-entitlements.md) | Cross-game rewards as entitlements | ownership | medium | open |
| [P-0028](P-0028-portable-preferences.md) | Portable player preferences (accessibility, comfort and controls) | identity | low | open |

## Phase 3: network effects

| ID | Problem | Layer | Difficulty | Status |
|---|---|---|---|---|
| [P-0018](P-0018-friends-and-presence.md) | Portable friends, blocks and presence | presence | high | open |
| [P-0021](P-0021-platform-holder-rules.md) | Platform-holder rules | ownership | high | open |
| [P-0027](P-0027-discovery.md) | Discovery: finding participating games | presence | medium | open |

## Research tracks (toward Phase 5)

| ID | Problem | Layer | Difficulty | Status |
|---|---|---|---|---|
| [P-0016](P-0016-portable-reputation.md) | Portable reputation and moderation standing | history | research | open |
| [P-0020](P-0020-connected-economies.md) | Connected economies and value transfer | ownership | research | open |
| [P-0022](P-0022-persistent-consequences.md) | Persistent consequences across games | world | research | open |
| [P-0023](P-0023-traveling-ai-characters.md) | AI characters that travel between games | world | research | open |

## Good first problems

These are good starting points if you're new:

- **[P-0028](P-0028-portable-preferences.md):** propose accessibility settings for v0.
- **[P-0008](P-0008-avatar-baseline.md):** make original CC0 test avatars and test them in an engine you know.
- **[P-0013](P-0013-portable-claims.md):** write example achievement credentials for made-up games.
- **[P-0003](P-0003-player-identifier.md):** compare identifier methods in a table.

## Status lifecycle

| Status | Meaning |
|---|---|
| `open` | The problem is described; nobody is actively driving it yet |
| `exploring` | A champion is gathering evidence and options |
| `proposal` | A concrete direction has been proposed and is in public review |
| `solved-enough` | Good enough for its phase, with tests or demos proving it |
| `parked` | Deliberately set aside, with the reason written in the doc |

To change a status, open a pull request that updates both the problem doc's front matter and this index. See [GOVERNANCE.md](../GOVERNANCE.md).

## Proposing a new problem

Open an issue using the **New problem** template. If maintainers agree it's distinct from the existing problems, it gets the next free ID and a doc based on [TEMPLATE.md](TEMPLATE.md). IDs are never reused, even if a problem is merged into another or parked.
