# Threat model

*Last reviewed: 2026-11-15*

A standard that lets players carry their identity everywhere also lets *harm* travel everywhere. Every proposal in this repository has to name the threats on this page that it affects and say how it handles them ([AGENTS.md](../AGENTS.md), rule 9). This is a living document: add threats as the design grows, in the same pull request that creates them.

## What we protect, in priority order

When protections conflict, the higher priority wins.

1. **People's safety**, especially children's.
2. **Control of identity.** Only the player can act as the player.
3. **Privacy.** Players decide who learns what about them.
4. **Integrity of claims.** What's signed is true, and it can't be forged or replayed.
5. **The stability and security of games.** Imported content can't harm the game that receives it.
6. **An open ecosystem.** No single party can capture, censor or switch off the network.

## Threats

### T1. Harm that follows players between games

- **What:** harassment, stalking or grooming that moves with a victim from game to game. A persistent identity makes a target easier to find.
- **Examples:** a harasser recognizes the same player in a new game; an adult tracks a child across games.
- **Mitigations:** private mode by default, with a different identifier in each game ([P-0006](../problems/P-0006-privacy-unlinkability.md)); portable block lists ([P-0018](../problems/P-0018-friends-and-presence.md)); age signals and guardian controls ([P-0007](../problems/P-0007-age-and-eligibility.md), [P-0005](../problems/P-0005-key-recovery.md)); local moderation in every receiving game ([P-0012](../problems/P-0012-moderating-imported-identity.md)).
- **Residual risk:** a player who chooses a public persona is easier to find.

### T2. Account takeover and impersonation

- **What:** someone steals a player's keys or tricks a recovery flow, then acts as that player everywhere at once. That's a far bigger prize than a single game account.
- **Examples:** phishing through a fake handoff link ([P-0017](../problems/P-0017-world-handoff.md)); social engineering against a recovery provider; malware that steals device keys.
- **Mitigations:** key rotation and recovery with a time-limited undo ([P-0005](../problems/P-0005-key-recovery.md)); short-lived, single-use handoff tickets; passkeys; per-game identifiers that limit the damage.
- **Residual risk:** recovery is always a trade-off between getting locked out and being taken over.

### T3. Tracking and profiling

- **What:** games, ad networks or data brokers link a player's activity across games.
- **Examples:** matching identical identifiers, avatar file hashes, display names or play patterns; the same signed credential shown in two games ([P-0006](../problems/P-0006-privacy-unlinkability.md#threats)); an issuer learning everywhere its credentials are used.
- **Mitigations:** per-game identifiers, selective disclosure, and coarse bands instead of exact stats ([P-0006](../problems/P-0006-privacy-unlinkability.md), [P-0013](../problems/P-0013-portable-claims.md)); revocation checks that don't reveal which credential is being checked ([P-0015](../problems/P-0015-issuer-trust-revocation.md)); preferences that stay private by default ([P-0028](../problems/P-0028-portable-preferences.md)).
- **Residual risk:** behavior can still link players. We can reduce correlation, not eliminate it.

### T4. Forged, replayed or cheated claims

- **What:** fake credentials, replayed presentations, achievements bought or cheated, and "achievement mills" that hand out impressive credentials.
- **Examples:** a fake game issues "world champion" badges; someone extracts an offline game's signing key ([P-0030](../problems/P-0030-built-for-every-game.md)).
- **Mitigations:** signatures and revocation ([P-0013](../problems/P-0013-portable-claims.md), [P-0015](../problems/P-0015-issuer-trust-revocation.md)); issuer allow-lists; lower trust levels for offline issuers; by default, receiving games grant cosmetic effects, not gameplay power ([P-0014](../problems/P-0014-claim-interpretation.md)).
- **Residual risk:** even a trusted issuer can be wrong or compromised.

### T5. Malicious or harmful content

- **What:** avatar files or images that exploit file parsers, overwhelm performance, or show illegal, offensive or infringing content.
- **Examples:** a command-injection flaw in a glTF loader ([CVE-2022-3008](https://nvd.nist.gov/vuln/detail/CVE-2022-3008)); an avatar with millions of triangles in a shared scene; a costume copied from a famous film character.
- **Mitigations:** budgets, validation, no external references, no executable behavior in v0, sandboxed parsing and fallbacks ([P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md)); moderation hooks ([P-0012](../problems/P-0012-moderating-imported-identity.md)); license metadata ([P-0011](../problems/P-0011-rights-licensing-likeness.md)).
- **Residual risk:** new parser bugs keep appearing, and moderation is never perfect.

### T6. Fraud and money laundering

- **What:** anything of value that can move between games or people attracts fraud, theft and laundering.
- **Examples:** in 2019 Valve stopped newly bought Counter-Strike keys from being traded or resold, citing fraud ([Engadget](https://www.engadget.com/2019-10-30-csgo-fraud-loot-box-key-trades.html)).
- **Mitigations:** no value transfer until research shows how to do it safely ([P-0020](../problems/P-0020-connected-economies.md)); rewards as non-tradable entitlements ([P-0019](../problems/P-0019-cross-game-entitlements.md)).
- **Residual risk:** it rises sharply the moment anything becomes tradable.

### T7. Capture, censorship and shutdown

- **What:** one company, directory or registry, or this project itself, gains control of the network, blocks participants, or disappears and breaks it.
- **Examples:** a hosted avatar service shutting down ([Ready Player Me, 2026](prior-art.md#ready-player-me)); a single identifier directory going offline; one large member steering the standard.
- **Mitigations:** file-first design and offline verification ([P-0024](../problems/P-0024-durability-when-services-die.md)); several identifier methods and hosts ([P-0003](../problems/P-0003-player-identifier.md)); no required directory or registry ([P-0027](../problems/P-0027-discovery.md), [P-0029](../problems/P-0029-world-addressing-and-links.md)); neutral governance ([P-0001](../problems/P-0001-neutral-governance-and-ip.md)).
- **Residual risk:** convenience keeps pulling toward centralization.

### T8. Attacks on the project's own tools and process

- **What:** compromised SDKs, dependencies, build pipelines or documentation, including text planted in issues, pull requests or web pages to steer AI agents (prompt injection).
- **Examples:** a malicious dependency in a passport library; a tampered CI workflow; a pull request that quietly weakens an agent's instructions.
- **Mitigations:** minimal dependencies (the checker uses only Python's standard library); CI actions pinned to exact commits with read-only permissions; maintainer review of guardrail files ([CODEOWNERS](../.github/CODEOWNERS)); agents treat outside content as data, never as instructions ([AGENTS.md](../AGENTS.md), rule 16); signed releases once there's code to release.
- **Residual risk:** every dependency and every contributor is a matter of trust.

## How to use this page

- In a problem doc or ADR, list the threats it affects (for example "T2, T3") and how it handles each one.
- If a proposal creates a new kind of threat, add it here in the same pull request.
- To report a vulnerability in published work, see [SECURITY.md](../SECURITY.md).
