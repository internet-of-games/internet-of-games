# Spike: Which credential format should carry achievement claims in Phase 1?

*Date: 2026-11-24 · Problems: P-0006, P-0013, P-0015 · Time box: 1 day*

## Question

Phase 1 needs Game A to sign an achievement claim that Game B verifies offline (success criterion 4). Should that claim use a strict profile of Open Badges 3.0, or SD-JWT-based Verifiable Credentials ([P-0013](../../problems/P-0013-portable-claims.md), question P-0013-Q1)?

## Approach

We read the formats' own specifications: Open Badges 3.0 ([1EdTech](https://www.imsglobal.org/spec/ob/v3p0)), SD-JWT ([RFC 9901](https://www.rfc-editor.org/rfc/rfc9901.html)), the SD-JWT-based Verifiable Credentials draft, revision 27 ([IETF](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/)), and OpenID for Verifiable Presentations 1.0 ([OpenID](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)). We compared them with what each engine can verify ([engine comparison](2026-11-24-signature-support-in-engines.md)), and we measured minimal synthetic examples of each.

## Findings

### 1. Side by side

| | Open Badges 3.0, JWT proof | Open Badges 3.0, embedded proof | SD-JWT credential |
|---|---|---|---|
| **Signature** | RS256 at minimum; other algorithms are allowed but, the specification warns, limit interoperability | The Data Integrity EdDSA suites, the only option the conformance tests support today | Any standard JOSE algorithm; the draft's examples use ES256 |
| **Canonicalization** | None: the signed bytes are verified as they are | JSON or RDF canonicalization, depending on the suite; the specification's examples use RDF, which needs a sizable library | None |
| **Selective disclosure** | No: the whole credential is shown | Not with the supported suite | Yes, claim by claim |
| **Revocation** | W3C Bitstring Status List | W3C Bitstring Status List | The IETF OAuth working group's [status list draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/) |
| **Finding the issuer's key** | Dereference a key URI; HTTP URLs are required, DID URLs allowed | Same | A `/.well-known/jwt-vc-issuer` file over HTTPS, or an X.509 certificate chain; DIDs are possible but not spelled out |
| **Size of our minimal example** | About 1.7 KB | Not measured | About 0.9 to 1.2 KB, depending on what's disclosed |
| **Browser presentation** | OpenID4VP defines a profile for JWT-secured credentials | OpenID4VP defines a profile for embedded proofs | OpenID4VP defines a profile for this format |

### 2. What each brings

- **Open Badges 3.0 already has an achievement vocabulary:** an achievement with a name, a description and criteria, plus evidence and alignment to frameworks ([1EdTech](https://www.imsglobal.org/spec/ob/v3p0)). It comes from education, so it has a large existing ecosystem, but it doesn't know about games.
- **Its default signature is large but universal.** RS256 is the one algorithm every engine we checked can verify, but its signatures are four times the size of ES256's.
- **Its embedded proof format is heavy for games.** The suites its conformance tests support need Ed25519 and a canonicalization step, neither of which Godot or Unity ships.
- **SD-JWT credentials are compact and private by design.** They carry salted digests instead of values, and the player reveals only the claims they choose ([RFC 9901](https://www.rfc-editor.org/rfc/rfc9901.html)). Batch issuance, one copy per game, keeps games from linking a player through the credential ([RFC 9901, section 10.1](https://www.rfc-editor.org/rfc/rfc9901.html#section-10.1); [P-0006](../../problems/P-0006-privacy-unlinkability.md#threats)).
- **SD-JWT credentials name their type with a `vct` value and describe it with type metadata,** which can be fetched by URL, looked up in a registry or cached ([IETF draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/)). A gaming achievement type would be defined this way.

### 3. Sizes, measured

We built minimal synthetic credentials for one made-up achievement, with a status-list entry and random bytes in place of real signatures:

| Example | Encoded size |
|---|---|
| Open Badges 3.0, JWT proof, RS256 | 1,677 bytes |
| Open Badges 3.0, JWT proof, ES256 | 1,421 bytes |
| SD-JWT credential, all three claims disclosed | 1,023 bytes |
| SD-JWT credential, one claim disclosed | 872 bytes |
| SD-JWT credential, one claim plus the player's key-binding proof | 1,184 bytes |

None of them leaves room for a player document within our 1,000-byte target ([universality requirements](../universality-requirements.md#4-small-enough-for-a-qr-code-or-a-link)). Either that target rises, or QR codes carry a pointer and the credential travels by link or file.

### 4. Revocation needs reconciling

Our revocation design assumes the W3C Bitstring Status List ([P-0015](../../problems/P-0015-issuer-trust-revocation.md)). Open Badges 3.0 uses it, but SD-JWT credentials point to the IETF status list draft instead. Choosing SD-JWT means updating P-0015 to that mechanism, or supporting both.

## Limitations

- Our size examples are minimal and synthetic. Real credentials with images, evidence or longer descriptions will be bigger.
- The SD-JWT credential specification and the IETF status list are still drafts, and may change before they're published.
- We didn't test any library or wallet.

## Recommendation

- **Use SD-JWT credentials with ES256 for Phase 1.** They're the most compact, they support selective disclosure, and both Phase 1 engines can verify ES256 with built-in cryptography.
- **Borrow Open Badges 3.0's achievement vocabulary** (name, description, criteria) for the gaming `vct` type, with credit, so a mapping to Open Badges stays easy for games that want to issue both (P-0013, direction 3).
- **Update P-0015** to cover the IETF status list, and revisit the size target in the universality requirements.
- **Record the choice in a decision record.**

## Sources

- 1EdTech, [Open Badges 3.0](https://www.imsglobal.org/spec/ob/v3p0), sections 8.1 to 8.5, read on 24 November 2026
- IETF, [RFC 9901](https://www.rfc-editor.org/rfc/rfc9901.html) · [SD-JWT-based Verifiable Credentials, revision 27](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) · [status list draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/)
- OpenID Foundation, [OpenID for Verifiable Presentations 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)
- This repository: [engine signature comparison](2026-11-24-signature-support-in-engines.md), [universality requirements](../universality-requirements.md), [P-0006](../../problems/P-0006-privacy-unlinkability.md), [P-0015](../../problems/P-0015-issuer-trust-revocation.md)
