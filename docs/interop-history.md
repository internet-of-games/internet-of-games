# How interoperability happened elsewhere

*Last reviewed: 2026-11-15*

Games aren't the first industry where large companies each kept users inside their own walls. Looking at how other walls came down helps us predict what could change games, and what won't.

## The patterns

| Case | What was closed | What opened it | Main force |
|---|---|---|---|
| **The web** | Dial-up online services, each a walled garden of content ([Wikipedia](https://en.wikipedia.org/wiki/Closed_platform)) | Open protocols (HTTP, HTML) that anyone could publish on without permission | A simpler open standard plus network effects |
| **Email** | Early email systems that couldn't reach each other | A common protocol ([SMTP, RFC 5321](https://www.rfc-editor.org/rfc/rfc5321.html)), with each address belonging to a domain | An open standard. Abuse was then handled by reputation systems, not a central gatekeeper |
| **Phone numbers** | Your number belonged to your carrier | Regulators required carriers to let customers keep their number when they switched ([FCC](https://www.fcc.gov/guides/portability-keeping-your-phone-number-when-changing-service-providers)) | **Regulation** |
| **Banking data** | Each bank held its customers' data | Rules requiring banks to open their data to authorized third parties: the EU's PSD2 ([EUR-Lex](https://eur-lex.europa.eu/eli/dir/2015/2366/oj)) and the UK's Open Banking order ([UK government](https://www.gov.uk/government/publications/retail-banking-market-investigation-order-2017)) | **Regulation** |
| **Console cross-play** | Players on different consoles couldn't play together | Sony opened up Fortnite cross-play in September 2018 after pressure from players and Epic. It has since become common, though on the platforms' terms ([PC Gamer](https://www.pcgamer.com/sony-charges-for-crossplay-support-to-protect-psn-revenue-documents-show)) | **Player pressure** behind one hit game |
| **"Sign in with…"** | Every site had its own password | Open protocols ([OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html)) | An open standard. The identity itself, however, ended up concentrated in a few large providers |
| **Social media accounts** | Your account belonged to the platform | The AT Protocol gives each account a portable identifier, so it can move between hosting providers ([AT Protocol](https://atproto.com/); [PLC directory](https://atproto.com/blog/plc-directory-org)) | Product design |

## Lessons for games

1. **Open standards win when they're *simpler* than the proprietary option** and give each adopter value on day one, before the network exists. For a game, that means the SDK has to be useful even if only one other game supports it.
2. **Regulation can force interoperability when incumbents won't.** Phone numbers and banking data opened because regulators required it. Games now face regulatory attention on virtual currencies, preservation, data portability and age checks ([legal-and-policy.md](legal-and-policy.md)). We should be ready with a workable, privacy-preserving answer *before* rules are written.
3. **An open protocol doesn't guarantee a decentralized outcome.** "Sign in with…" used open protocols, yet identity ended up concentrated in a handful of providers. That's why we care about **who controls the identifier** ([P-0003](../problems/P-0003-player-identifier.md)), not just which protocol is used.
4. **Player pressure plus one hit game can break a "never".** Cross-play went from impossible to standard practice quickly. A single popular game adopting portable identity could do the same.
5. **Abuse handling has to be designed in from the start.** Email's open design invited spam, and the fix took decades of reputation systems. Our equivalents are moderation of imported content ([P-0012](../problems/P-0012-moderating-imported-identity.md)) and issuer trust ([P-0015](../problems/P-0015-issuer-trust-revocation.md)).
6. **Interoperability often arrives on the incumbents' terms.** Cross-play came with platform royalty policies attached. We should expect platform holders to set conditions ([P-0021](../problems/P-0021-platform-holder-rules.md)), and design so that the *core* (identity, appearance and claims) never depends on their permission.
