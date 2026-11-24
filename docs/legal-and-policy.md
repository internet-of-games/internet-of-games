# Legal and policy landscape

*Last reviewed: 2026-11-24.*

> **Not legal advice.** This page maps the issues a portable player identity runs into, so contributors know which questions to ask. Laws differ by country and change often. Anyone building a product on this work should get qualified legal advice.

## 1. Who owns in-game things?

Game terms of service usually give players a **license** to use in-game items and currency, not ownership. In a class action over NBA 2K's virtual currency, Take-Two argued that virtual currencies are "fictions" governed by the publisher's terms ([VGC](https://videogameschronicle.com/news/virtual-currencies-are-fictions-take-two-argues-in-microtransaction-theft-lawsuit)).

**Implication:** we shouldn't design anything that depends on players "owning" items from another game. What players can carry is what they actually control: their chosen name, avatars they have the rights to, and signed statements *about* them ([portability-matrix.md](portability-matrix.md)).

## 2. Intellectual property, licensing and likeness

- **Licensed content is scoped.** Sports leagues, players' unions, film studios and music labels license their content for particular products ([why-not-yet §1](why-not-yet.md#1-the-licenses-dont-stretch)).
- **Rights can be layered and surprising.** Tattoo artists have sued over tattoos reproduced on athletes in games, with mixed results ([Sports Illustrated](https://www.si.com/nba/2020/04/06/nba-2k-ruling-tattoo-artists); [U.S. Copyright Office summary](https://www.copyright.gov/fair-use/summaries/Alexander-v-Take-Two-Interactive-Software-Inc-No-18-CV-966-S-D-Ill-Sept-25-2024.pdf)).
- **User uploads can infringe.** A player might upload an avatar based on a famous character, or on a real person's likeness. Services that host user content generally rely on notice-and-takedown regimes, such as the U.S. DMCA's section 512 ([U.S. Copyright Office](https://www.copyright.gov/512/)) and the EU Digital Services Act ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/digital-services-act-package)).
- **Machine-readable licenses help.** VRM files carry license metadata, and avatar hubs such as VRoid Hub let creators set usage conditions ([VRoid Hub API](https://developer.vroid.com/en/api)).

→ [P-0011](../problems/P-0011-rights-licensing-likeness.md), [P-0012](../problems/P-0012-moderating-imported-identity.md)

## 3. Age ratings and children

- Ratings differ widely between games: NBA 2K26 is rated E (Everyone) and Grand Theft Auto VI is rated M (Mature 17+) by the ESRB ([NBA 2K26](https://www.esrb.org/ratings/40735/nba-2k26/); [GTA VI](https://www.esrb.org/ratings/41627/grand-theft-auto-vi/)).
- In the U.S., the amended COPPA Rule took effect in June 2025, with most compliance due by April 2026 ([Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-publishes-final-coppa-rule-amendments)).
- The EU is rolling out privacy-preserving age verification, and has urged member states to offer it by 31 December 2026 ([European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-urges-member-states-rollout-eu-age-verification-app)).
- Ratings are gaining legal weight. Under the proposed Digital Fairness Act, a game whose age rating (for example from PEGI) says it suits people under 18 counts as directed at minors, which brings in the protections in [§5](#5-virtual-currencies-loot-boxes-and-consumer-protection) ([proposal](https://commission.europa.eu/document/download/0575d59f-554f-4a9e-b54b-e6b717175809_en?filename=Proposal+for+a+Digital+Fairness+Act.pdf), recital 62).

→ [P-0007](../problems/P-0007-age-and-eligibility.md)

## 4. Privacy and data portability

- The EU's GDPR requires data minimization and gives people a right to data portability, among other rights ([GDPR on EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)).
- A cross-game identifier is personal data, and if it's used carelessly it becomes a tracking identifier. Sharing data between games raises questions about who is the controller, what the legal basis is, and whether consent was given.
- Preferences such as accessibility settings can reveal sensitive information, like health data.

→ [P-0006](../problems/P-0006-privacy-unlinkability.md), [P-0028](../problems/P-0028-portable-preferences.md)

## 5. Virtual currencies, loot boxes and consumer protection

- In March 2025, EU consumer authorities published key principles for in-game virtual currencies, including showing prices in real money ([European Commission](https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/social-media-online-games-and-search-engines_en)).
- The European Commission proposed a **Digital Fairness Act** on 11 November 2026. The regulation would repeal the EU's 2005 Unfair Commercial Practices Directive and take its place ([proposal, COM(2026) 1100](https://commission.europa.eu/document/download/0575d59f-554f-4a9e-b54b-e6b717175809_en?filename=Proposal+for+a+Digital+Fairness+Act.pdf)). For games, it would:
  - require the real-money value to be shown for anything priced in a paid virtual currency (Article 14)
  - require disclosure of what paid random rewards, such as loot boxes, can contain and the odds of getting each item, plus a way to switch them off (Article 15)
  - in products aimed at minors, or known to be used by them, keep paid virtual currencies switched off unless a parent or guardian approves, and offer minors no paid random rewards and no pay-to-win or pay-to-progress purchases (Articles 14 to 16). A minor is anyone under 18.
- It's a proposal. It would apply 12 months after it enters into force, and the European Parliament and the Council will now negotiate it. One law firm doesn't expect it in force before 2028 ([Paul Weiss](https://www.paulweiss.com/insights/client-memos/european-commission-proposes-the-digital-fairness-act)). Earlier analyses: [Ashurst](https://www.ashurstperkinscoie.com/en/insights/digital-fairness-act-brussels-takes-on-consumer-enforcement/), [Winston Taylor](https://www.winstontaylor.com/insights/the-eu-draft-digital-fairness-act-consumer-protection-for-the-digital-age).
- The proposal notes that virtual currencies locked inside one game, with no cash value and no way to cash them out or trade them outside it, fall outside the EU's payment-services and crypto-asset rules (recital 61). It doesn't say what applies to currencies that cross games, but those would lose exactly the properties the recital relies on. That's one more reason [P-0020](../problems/P-0020-connected-economies.md) stays research.

→ [P-0019](../problems/P-0019-cross-game-entitlements.md), [P-0020](../problems/P-0020-connected-economies.md)

## 6. Value transfer, fraud and financial rules

Anything that lets value move between games or between people attracts fraud and money laundering. Valve restricted trading of newly purchased Counter-Strike keys in 2019 for exactly this reason ([Engadget](https://www.engadget.com/2019-10-30-csgo-fraud-loot-box-key-trades.html)). Cross-game currencies or tradable assets may also trigger payment, e-money or anti-money-laundering rules in some places. That's a major reason [P-0020](../problems/P-0020-connected-economies.md) is research only.

## 7. Platform rules

Console and mobile platforms control their stores, payments and certification, and they set commercial terms for cross-platform features. Documents from the *Epic v. Apple* trial showed a Sony royalty policy tied to cross-platform play ([PC Gamer](https://www.pcgamer.com/sony-charges-for-crossplay-support-to-protect-psn-revenue-documents-show)). Much platform policy is confidential to licensed developers. Contributors **must not share confidential material** here.

→ [P-0021](../problems/P-0021-platform-holder-rules.md)

## 8. Game preservation

The "Stop Destroying Videogames" European Citizens' Initiative gathered about 1.29 million verified signatures. In June 2026 the Commission responded by opting for a voluntary code of conduct instead of a binding law ([Lewis Silkin](https://www.lewissilkin.com/insights/2026/06/24/european-commission-stops-short-of-imposing-mandatory-requirements-following-citi-102n4yy)). Players' identities and histories outliving shut-down games is a design goal of this project ([P-0024](../problems/P-0024-durability-when-services-die.md)).

## 9. Interoperability mandates

The EU Digital Markets Act requires designated "gatekeepers" to open certain services to interoperability ([European Commission](https://digital-markets-act.ec.europa.eu/index_en)). It wasn't written with games in mind, but it shows regulators will mandate interoperability when they think markets need it ([interop-history.md](interop-history.md)).

## How this project protects itself and its contributors

- **Licenses:** Apache-2.0 for code, which includes a patent license from contributors, and CC BY 4.0 for documents. Note that CC BY 4.0 doesn't license patents, so the IP policy for specification text is still open ([P-0001](../problems/P-0001-neutral-governance-and-ip.md)).
- **Developer Certificate of Origin:** contributors certify that they have the right to submit their work ([CONTRIBUTING.md](../CONTRIBUTING.md)).
- **No third-party game content:** no game screenshots, logos, characters, ripped assets or copied text beyond short attributed quotes ([TRADEMARKS.md](../TRADEMARKS.md)).
- **Synthetic data only:** test passports, avatars and credentials are made-up and released under CC0. No real players' data.
- **No confidential information:** nothing covered by an NDA, including platform documentation.
