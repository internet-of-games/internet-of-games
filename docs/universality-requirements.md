# Universality requirements

*Last reviewed: 2026-11-24. These are initial requirements to test in Phase 1. Targets marked "our target" are choices to measure against, not facts.*

The standard has to work for every kind of game: blockbusters and one-person projects, any genre, engine, platform, age rating and business model, online or offline ([P-0030](../problems/P-0030-built-for-every-game.md)). Decisions made early can quietly rule out whole categories of games, so every Phase 1 design is checked against this list. Problem docs check against it in their "Works for every game?" section, and decision records in "Universality and safety".

## The requirements

### 1. Nothing needs a network once keys are cached

Recognizing a player, loading their avatar and verifying a credential make **zero network calls** when the issuer's public keys and status lists are already cached. Fully offline games must work, and a game must keep working when every service, ours included, is gone ([design principle 1](design-principles.md#1-file-first-service-optional); [P-0024](../problems/P-0024-durability-when-services-die.md)).

### 2. Nothing depends on a single company

No required step relies on one company's servers, accounts, store or browser, including this project's ([design principle 5](design-principles.md#5-no-single-company-in-the-critical-path-including-us)). Native engines, consoles and cloud streaming have to work without a web browser in the loop ([P-0021](../problems/P-0021-platform-holder-rules.md)).

### 3. Every layer above the smallest profile is optional

The smallest useful profile, for game jams and tiny games, is **recognition only**: a per-game player identifier, a display name and a 2D portrait. Avatars, credentials, preferences and travel are each optional additions ([P-0030](../problems/P-0030-built-for-every-game.md), question P-0030-Q4). Conformance levels follow the same steps ([P-0026](../problems/P-0026-conformance-and-interop-testing.md)).

### 4. Small enough for a QR code or a link

- A QR code holds at most 2,953 bytes of binary data, at the largest size and the lowest error correction ([DENSO WAVE](https://www.qrcode.com/en/about/standards.html)). Codes that full are hard to scan from a screen. **Our target:** a player document plus one credential fits in 1,000 bytes, so it fits a code that's easy to scan, with error correction to spare.
- HTTP recommends that software support URIs of at least 8,000 octets ([RFC 9110, section 4.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-4.1)), but apps and platforms often handle less. **Our target:** anything that has to travel in a link, such as a handoff ticket, stays under 2,000 bytes.
- Compact signatures help: ECDSA and Ed25519 signatures are 64 bytes, while a 2048-bit RSA signature is 256 bytes ([engine signature comparison](spikes/2026-11-24-signature-support-in-engines.md)).

### 5. Fast on modest hardware

**Our target:** verifying a player document and one credential takes under 100 milliseconds on the slowest phone we choose as a reference device, with keys cached. That keeps verification inside an ordinary loading screen. Phase 1 measures it.

### 6. Honest about how much a claim proves

Every claim carries one of three trust levels, and each receiving game chooses the lowest it accepts ([P-0015](../problems/P-0015-issuer-trust-revocation.md), question P-0030-Q2):

| Trust level | Meaning |
|---|---|
| `server-signed` | Signed by the issuer on infrastructure the player doesn't control |
| `device-signed` | Signed on the player's device, for example by an offline game. Someone determined can extract such keys, so it proves less |
| `self-asserted` | Stated by the player, unsigned or signed only with the player's own key |

### 7. Neutral about age, genre and business model

- **Age:** only age thresholds such as "over 13", never a birthdate, so the same signals work in games rated for everyone and in games for adults ([P-0007](../problems/P-0007-age-and-eligibility.md)).
- **Genre and art style:** nothing in the core assumes a humanoid character, a level system or a particular art style. A game that can't show a 3D avatar falls back to the portrait and a description ([P-0008](../problems/P-0008-avatar-baseline.md), [P-0009](../problems/P-0009-cross-style-translation.md)).
- **Business model:** nothing in the core assumes a store, a payment or an account type. Premium, free-to-play, subscription and ad-supported games all fit.

### 8. Works at any scale

Verification happens inside each game, so no central service sits in the login path, and issuers' status lists can be cached and mirrored ([P-0015](../problems/P-0015-issuer-trust-revocation.md)). The same design has to hold for a game with a dozen players and a platform with a hundred million.

### 9. Works inside one company, too

A publisher can use one issuer identity across all its titles while each title still gets its own player identifier, so connecting its own portfolio is as easy as connecting with others ([P-0030](../problems/P-0030-built-for-every-game.md), question P-0030-Q3).

### 10. Usable by everyone

Consent screens, fallbacks and error messages follow accessibility guidance such as the [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/), and display names work in any script ([OQ-10](open-questions.md#people-and-safety)).

### 11. Cheap to adopt

The basics integrate in about a day, without a server ([design principle 11](design-principles.md#11-integration-in-a-day); [P-0025](../problems/P-0025-developer-adoption-cost.md)).

## How to use this page

- When you propose a design, say which requirements it meets, which it bends and why, and which it breaks. A design that breaks one needs a decision record.
- Targets change only with evidence: measurements from the demo games or from integrators. Record the evidence when you change a number.
