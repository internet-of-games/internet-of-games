# Spike: Which signature algorithms can each engine verify without extra libraries?

*Date: 2026-11-24 · Problems: P-0003, P-0013, P-0025 · Time box: 1 day*

## Question

Recognizing a player and checking a claim both come down to verifying a signature inside the game. Which of the common algorithms (RSA with PKCS#1 v1.5 or PSS, ECDSA on the P-256 curve, and Ed25519) can Godot, browsers, Unity and Unreal verify with what they ship, and what does that mean for our choice of identifier method and credential format ([P-0025](../../problems/P-0025-developer-adoption-cost.md), question P-0025-Q1)?

## Approach

We read the engines' own documentation and source code, browser compatibility data, and the specifications of the identifier methods we're considering. We didn't run any code, and consoles are out of scope, because their platform documentation is under NDA.

## Findings

### 1. Built-in verification by engine

| Engine | RS256 (RSA, PKCS#1 v1.5) | PS256 (RSA-PSS) | ES256 (ECDSA, P-256) | Ed25519 |
|---|---|---|---|---|
| **Godot 4.7** | Yes | No | Yes, but signatures must be DER-encoded | No |
| **Browsers (Web Crypto)** | Yes | Yes | Yes | Yes, in Chrome 137, Firefox 129, Safari 17 and later |
| **Unity (.NET Standard)** | Yes, in the class library | In the class library; platform support varies | Yes, in the class library | No |
| **Unreal (PlatformCrypto plugin)** | Listed | Listed | Not listed | Listed |

The details behind each row:

- **Godot.** The `Crypto` class signs and verifies a hash with a `CryptoKey`, which can be an RSA or an elliptic-curve key; SHA-256 comes from `HashingContext` ([Crypto](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/Crypto.xml); [CryptoKey](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/CryptoKey.xml)). In the 4.7.2 release (18 August 2026), verification goes through mbedTLS's generic verify call, which expects ECDSA signatures in DER form ([source](https://github.com/godotengine/godot/blob/4.7.2-stable/modules/mbedtls/crypto_mbedtls.cpp)). The development branch moved to mbedTLS 4.1 and the PSA Crypto API in July 2026; its verify function handles RSA with PKCS#1 v1.5 and ECDSA, and still takes DER signatures for compatibility ([source](https://github.com/godotengine/godot/blob/master/modules/mbedtls/crypto_mbedtls.cpp)). Neither has an RSA-PSS or Ed25519 path. JOSE signatures put ECDSA values side by side instead of in DER ([RFC 7518, section 3.4](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.4)), so a game must convert them, which takes a few lines of code.
- **Browsers.** The Web Cryptography API defines RSASSA-PKCS1-v1_5, RSA-PSS and ECDSA on the P-256, P-384 and P-521 curves ([W3C](https://www.w3.org/TR/WebCryptoAPI/)), and every major browser has supported signing and verifying for years. Ed25519 arrived later: Chrome 137, Firefox 129 and Safari 17, with the same versions on mobile ([MDN browser compatibility data](https://github.com/mdn/browser-compat-data/blob/main/api/SubtleCrypto.json)). Web Crypto has no secp256k1 curve.
- **Unity.** Unity's default API compatibility level is .NET Standard ([Unity manual](https://docs.unity3d.com/Manual/dotnet-profile-support.html)), whose class library includes RSA and ECDSA ([Microsoft](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.ecdsa)). Unity warns that some system libraries need platform-specific implementations, so each target platform has to be tested. .NET has no Ed25519 class: the proposal to add one is still open, with no target release ([dotnet/runtime#63174](https://github.com/dotnet/runtime/issues/63174)). The MIT-licensed BouncyCastle .NET library implements it ([Ed25519Signer](https://github.com/bcgit/bc-csharp/blob/master/crypto/src/crypto/signers/Ed25519Signer.cs)).
- **Unreal.** According to Epic's API reference, the PlatformCrypto plugin wraps the platform's cryptography or OpenSSL, and lists verification of RS256 and PS256 signatures over a hash and an Ed25519 verifier class ([PlatformCrypto](https://dev.epicgames.com/documentation/unreal-engine/API/PluginIndex/PlatformCrypto); [FEncryptionContextOpenSSL](https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/PlatformCryptoContext/FEncryptionContextOpenSSL); [FVerifierEd25519OpenSSL](https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/PlatformCryptoContext/FVerifierEd25519OpenSSL)). Those pages don't render without JavaScript, so we couldn't read them in full; check them by hand. We saw no ES256 method.

### 2. Signature size matters for QR codes and links

An ES256 signature is 64 bytes ([RFC 7518](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.4)), and so is an Ed25519 signature ([RFC 8032](https://www.rfc-editor.org/rfc/rfc8032.html)). An RSA signature is as long as its key, so 256 bytes for a 2048-bit key ([RFC 8017](https://www.rfc-editor.org/rfc/rfc8017.html)), and RSA public keys are much larger too. Claims are supposed to fit in a QR code or a deep link where possible ([P-0013](../../problems/P-0013-portable-claims.md)), which favors the elliptic-curve algorithms.

### 3. Identifier methods bring their own requirements

- **`did:webvh` 1.0** accepts exactly one proof suite for its log entries and witnesses, `eddsa-jcs-2022` ([specification](https://identity.foundation/didwebvh/v1.0/)), which uses Ed25519 with JSON canonicalization ([W3C](https://www.w3.org/TR/vc-di-eddsa/)). Resolving it inside a game therefore needs Ed25519 and a canonicalization routine.
- **`did:plc`** supports only secp256k1 and P-256 rotation keys, signs operations with ECDSA over SHA-256, and requires signatures in "low-S" form ([specification](https://web.plc.directory/spec/v0.1/did-plc)). P-256 keys can be checked with built-in APIs; secp256k1 keys would need a library everywhere, browsers included.
- **`did:key`** and **`did:web`** carry whatever key type the player chooses, so they impose nothing beyond the chosen algorithm.

### 4. Libraries where the engine falls short

On the web, the MIT-licensed [`jose`](https://github.com/panva/jose) library handles JWS, JWT and JWK with RSA, ECDSA and EdDSA. For Unity, BouncyCastle .NET fills the Ed25519 gap. For Godot, Ed25519 would need native code, for example a GDExtension built for every target platform, which adds the build and maintenance cost P-0025 warns about.

## Limitations

- We read documentation and source code; we didn't run verification tests on real devices.
- Unreal's API pages couldn't be read automatically, and we didn't read Unreal's source.
- Unity's support can differ by platform and scripting backend; we didn't test any platform.
- Consoles, and any engine-specific changes after 24 November 2026, aren't covered.

## Recommendation

- **For the two Phase 1 engines (Godot and the web), ES256 with P-256 keys is the only compact choice that both verify with built-in APIs today.** Godot needs a small converter from the JOSE signature format to DER.
- **RS256 works everywhere we looked,** but its signatures and keys are several times larger, which works against QR codes and deep links.
- **Choosing Ed25519**, which `did:webvh` 1.0 requires, means shipping an Ed25519 library for Godot and Unity, and requiring recent browsers. That's a real cost, but a one-time one, and some of our candidate standards assume it.
- Feed this into the comparisons of identifier methods ([P-0003](../../problems/P-0003-player-identifier.md)) and credential formats ([P-0013](../../problems/P-0013-portable-claims.md)): a method that forces Ed25519 or secp256k1 should count that cost against itself.

## Sources

- Godot, [Crypto](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/Crypto.xml) and [CryptoKey](https://github.com/godotengine/godot/blob/4.7.2-stable/doc/classes/CryptoKey.xml) class references and the [mbedTLS module](https://github.com/godotengine/godot/blob/4.7.2-stable/modules/mbedtls/crypto_mbedtls.cpp) (4.7.2-stable), plus the [development branch](https://github.com/godotengine/godot/blob/master/modules/mbedtls/crypto_mbedtls.cpp), read through the GitHub API on 24 November 2026
- W3C, [Web Cryptography API](https://www.w3.org/TR/WebCryptoAPI/) · MDN, [browser compatibility data for SubtleCrypto](https://github.com/mdn/browser-compat-data/blob/main/api/SubtleCrypto.json) (updated 6 October 2026)
- Unity, [.NET profile support](https://docs.unity3d.com/Manual/dotnet-profile-support.html) · Microsoft, [ECDsa class](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.ecdsa) · [dotnet/runtime#63174](https://github.com/dotnet/runtime/issues/63174) · [BouncyCastle .NET](https://github.com/bcgit/bc-csharp)
- Epic Games, Unreal Engine API reference: [PlatformCrypto](https://dev.epicgames.com/documentation/unreal-engine/API/PluginIndex/PlatformCrypto), [FEncryptionContextOpenSSL](https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/PlatformCryptoContext/FEncryptionContextOpenSSL), [FVerifierEd25519OpenSSL](https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/PlatformCryptoContext/FVerifierEd25519OpenSSL)
- IETF, [RFC 7518](https://www.rfc-editor.org/rfc/rfc7518.html), [RFC 8017](https://www.rfc-editor.org/rfc/rfc8017.html), [RFC 8032](https://www.rfc-editor.org/rfc/rfc8032.html)
- DIF, [did:webvh v1.0](https://identity.foundation/didwebvh/v1.0/) · W3C, [Data Integrity EdDSA Cryptosuites](https://www.w3.org/TR/vc-di-eddsa/) · [did:plc specification](https://web.plc.directory/spec/v0.1/did-plc)
- [panva/jose](https://github.com/panva/jose)
