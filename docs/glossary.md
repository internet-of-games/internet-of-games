# Glossary

**Account linking.** Connecting a player's portable identity to their existing account in a game, without replacing that account. See [P-0004](../problems/P-0004-account-linking.md).

**Appearance descriptor.** A proposed style-independent description of how a character looks: hair, colors, build, signature items and so on. Any game can render it in its own art style. See [P-0009](../problems/P-0009-cross-style-translation.md).

**Avatar.** The visual representation of a player character. In this project it usually means a 3D file in glTF/VRM format, with a 2D portrait as a fallback.

**Budget (avatar).** Limits on file size, polygons, materials, bones and similar, so that an imported avatar can't overwhelm a game. See [P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md).

**Champion.** A contributor who takes responsibility for moving a problem doc forward: gathering evidence, proposing directions and running discussions.

**Claim.** A statement about a player, such as "cleared the final boss in Game A". It's *self-asserted* when the player states it and *issuer-attested* when a game signs it.

**Conformance.** Passing a shared set of tests that shows an implementation behaves as the specification requires. See [P-0026](../problems/P-0026-conformance-and-interop-testing.md).

**Cross-play / cross-progression.** Playing together across platforms, or carrying progress in *one* game across platforms. Both happen within a single game. This project is about continuity *between* different games.

**Credential (Verifiable Credential, VC).** A tamper-evident, signed set of claims made by an issuer, defined by the [W3C VC Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/).

**DID (Decentralized Identifier).** An identifier, such as `did:web:example.com`, that the subject controls through cryptographic keys, without a central registry. Defined by [W3C DID](https://www.w3.org/TR/did-1.0/). A *DID method* (for example `did:key`, `did:web`, `did:webvh` or `did:plc`) defines how a particular kind of DID is created and resolved.

**DID document.** The public document a DID resolves to. It lists the public keys and services associated with the identifier.

**Entitlement.** A right to an item that a game *grants* in its own system, for example "you may use this cosmetic". In this project, cross-game rewards are entitlements, not transfers. See [P-0019](../problems/P-0019-cross-game-entitlements.md).

**glTF.** A royalty-free 3D asset format from Khronos, sometimes called "the JPEG of 3D". Also standardized as ISO/IEC 12113:2022.

**Holder.** The party holding credentials; in this project, the player or their passport app.

**Interop event (plugfest).** A session where several independent implementations test against each other.

**Interpreter / interpretation.** A receiving game's local decision about what a verified foreign claim *means*. See [P-0014](../problems/P-0014-claim-interpretation.md).

**Issuer.** A party that signs a credential, for example the game where an achievement was earned.

**OpenID4VP / OpenID4VCI.** OpenID Foundation protocols for presenting and issuing verifiable credentials. Both reached Final in 2025.

**Pairwise identifier.** A different identifier for each game, so games can't correlate a player by comparing identifiers. See [P-0006](../problems/P-0006-privacy-unlinkability.md).

**Player passport (working name).** The small portable document at the center of this project. It references the player's identifier, avatar files, credentials and preferences. Its final name is still undecided ([OQ-1](open-questions.md#naming)).

**Problem doc.** A numbered document (`P-0001` and up) in [problems/](../problems/README.md) that describes one sub-problem: why it matters, what exists, constraints, success criteria and open questions.

**Receiving game / issuing game.** The game a player arrives in, and the game that signed a claim about them.

**Revocation / status list.** A way for an issuer to mark a credential as revoked or suspended after it was issued, for example because of cheating. See [Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/).

**SD-JWT.** Selective Disclosure for JSON Web Tokens ([RFC 9901](https://www.rfc-editor.org/rfc/rfc9901.html)). It lets a holder reveal only some claims from a signed credential.

**Selective disclosure.** Showing only the claims needed, such as "over 13" rather than a birthdate.

**Verifier.** A party that checks a credential's signature and status, usually the receiving game.

**VRM.** A glTF-based format for humanoid avatars, stewarded by the VRM Consortium. It adds a standard rig, expressions, physics for hair and cloth (spring bones), and license metadata.

**World address.** A stable, shareable address for a game world or a place inside it, similar to a web page's URL. See [P-0029](../problems/P-0029-world-addressing-and-links.md).

**Walled garden.** A platform where identity, content and purchases stay inside the platform owner's control.
