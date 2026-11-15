# Why doesn't NBA 2K plug into GTA VI?

*Last reviewed: 2026-11-15. Names of games and companies appear only to describe the problem; see [TRADEMARKS.md](../TRADEMARKS.md).*

It's a fair question. NBA 2K and Grand Theft Auto are two of the biggest game series in the world. Imagine walking out of one and into the other as the same person, and paying for a *world* instead of a game.

Here's the surprising part: **both series already belong to the same company.** Take-Two Interactive publishes through three labels: Rockstar Games (Grand Theft Auto, Red Dead Redemption), 2K (NBA 2K, among others) and Zynga ([Take-Two FY2026 results](https://www.businesswire.com/news/home/20260521450562/en/Take-Two-Interactive-Software-Inc.-Reports-Results-for-Fourth-Quarter-and-Fiscal-Year-2026)). Grand Theft Auto VI is scheduled for 19 November 2026 ([Forbes](https://www.forbes.com/sites/brianmazique/2026/05/12/grand-theft-auto-6-release-date-and-everything-confirmed/)).

So this isn't a case of rival companies refusing to cooperate. The walls are structural, and most of them would still stand even if every executive wanted to connect the games.

## The short answer

| Wall | In one line |
|---|---|
| [1. Licenses](#1-the-licenses-dont-stretch) | The rights that make NBA 2K possible are written for one kind of product. |
| [2. Ratings](#2-the-ratings-dont-mix) | One game is rated *E for Everyone* and the other *M for Mature 17+*. |
| [3. Economies](#3-the-economies-are-the-business) | In-game spending is most of the business, and it's built to stay inside each game. It doesn't even carry from one NBA 2K edition to the next. |
| [4. Engines and bodies](#4-the-engines-and-bodies-dont-match) | The games use different engines, skeletons, animation sets and art styles. |
| [5. Game design](#5-game-design-doesnt-transfer) | Stats, balance and progression *are* the product. |
| [6. Platforms](#6-the-platforms-set-the-terms) | Console makers own identity, stores and payments, and they set the terms. |
| [7. Liability and safety](#7-liability-safety-and-fraud-follow-the-player) | Imported content brings imported risk: offensive or infringing avatars, cheating, fraud and malicious files. |
| [8. Strategy](#8-they-believe-they-already-have-a-metaverse) | The company's leadership has said its online games already *are* the "metaverse". |

## 1. The licenses don't stretch

NBA 2K depends on licensing agreements with the NBA and the players' union (NBPA) that cover teams, leagues, and player names and likenesses. The 2018 extension was reported to be worth up to $1.1 billion over seven years ([theScore](https://www.thescore.com/nba/news/1700280); [NBA](https://pr.nba.com/nba-nbpa-and-2k-announce-longterm-partnership-expansion)). The partnership was extended again in 2025, when the NBA and Take-Two also launched a joint media venture ([TheWrap](https://www.thewrap.com/nba-take-two-interactive-media-joint-venture-licensing-partnership-renewal/)).

Licenses like these are negotiated for particular products and contexts. A league and a players' union agreeing to appear in a basketball simulation is not the same as agreeing to appear in an adults-only crime sandbox. Even a single athlete's appearance carries layers of rights. Tattoo artists have sued over tattoos reproduced on athletes in sports games. 2K won the NBA 2K case on summary judgment in 2020 ([Sports Illustrated](https://www.si.com/nba/2020/04/06/nba-2k-ruling-tattoo-artists)), but in a WWE 2K case a jury found for the artist in 2022 ([Technology & Marketing Law Blog](https://blog.ericgoldman.org/?p=24511); [U.S. Copyright Office fair-use summary](https://www.copyright.gov/fair-use/summaries/Alexander-v-Take-Two-Interactive-Software-Inc-No-18-CV-966-S-D-Ill-Sept-25-2024.pdf)).

**What this means for us:** licensed content can't be what travels between games. What *can* travel is what the **player** creates or earns: a chosen name, their own avatar, and facts about what they did. See [P-0011](../problems/P-0011-rights-licensing-likeness.md).

## 2. The ratings don't mix

The ESRB rates NBA 2K26 **E (Everyone)**, with notices for user interaction and in-game purchases that include random items ([ESRB](https://www.esrb.org/ratings/40735/nba-2k26/)). It rates Grand Theft Auto VI **M (Mature 17+)**, with descriptors that include intense violence, strong sexual content, and use of drugs and alcohol ([ESRB](https://www.esrb.org/ratings/41627/grand-theft-auto-vi/)).

Put the two games into one connected experience and you either wall off the younger audience or pull everything up to the strictest rating. Children's privacy law adds more obligations: the U.S. COPPA Rule was amended in 2025, with most of the new requirements due by April 2026 ([Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-publishes-final-coppa-rule-amendments)). Whatever connects games has to carry **age and eligibility signals** without exposing who the player is. See [P-0007](../problems/P-0007-age-and-eligibility.md).

## 3. The economies are the business

In Take-Two's fiscal year 2026, **78% of net bookings came from "recurrent consumer spending"**, which covers virtual currency, add-on content, in-game purchases and in-game advertising. NBA 2K and GTA Online are named among the top contributors ([Take-Two FY2026 results](https://www.businesswire.com/news/home/20260521450562/en/Take-Two-Interactive-Software-Inc.-Reports-Results-for-Fourth-Quarter-and-Fiscal-Year-2026)).

Each of these economies is tuned on its own, and they don't cross even *within* a franchise. NBA 2K's virtual currency (VC) doesn't carry over from one yearly edition to the next. In a class action over this, Take-Two argued that virtual currencies are "fictions" governed by the publisher's terms ([VGC](https://videogameschronicle.com/news/virtual-currencies-are-fictions-take-two-argues-in-microtransaction-theft-lawsuit)). According to testimony unsealed in 2026, 2K has no technical way to carry VC between editions and no plan to build one ([Kotaku](https://kotaku.com/2k-forced-in-court-to-explain-why-nba-2k-players-cant-transfer-digital-currency-you-have-no-ownership-or-other-rights-to-virtual-items-2000736199)).

If currency can't cross from NBA 2K26 to NBA 2K27, moving it into an entirely different game with a different economy is a far bigger ask. Cross-game currency also runs into consumer-protection and financial rules (see [legal-and-policy.md](legal-and-policy.md)).

**What this means for us:** currencies are out of scope at first. Rewards *can* cross as entitlements, such as "players who did X in Game A get cosmetic Y here". That's a promotion, not a transfer of value. See [P-0019](../problems/P-0019-cross-game-entitlements.md) and [P-0020](../problems/P-0020-connected-economies.md).

## 4. The engines and bodies don't match

Every major game has its own engine, skeleton conventions, animation library, shaders, physics and performance budget. A character model built for one game is not a drop-in for another. Even when one company controls *everything*, moving characters across art styles is manual work. When Epic launched LEGO Fortnite, it gave **more than 1,200** existing Fortnite outfits a LEGO-style version. Those versions were made outfit by outfit and rolled out gradually, and licensing decided which outfits could be converted at all ([PC Gamer](https://www.pcgamer.com/fortnite-is-adding-a-lego-themed-survival-crafting-mode-that-includes-lego-versions-of-over-1200-pre-existing-skins); [Dexerto](https://dexerto.com/fortnite/fortnite-launches-over-1200-lego-skins-for-chapter-5-season-1-2412246)).

**What this means for us:** a mesh on its own isn't enough. Portable appearance needs a common baseline format (glTF/VRM), performance budgets, and a style-independent *description* that each game can render in its own way. See [P-0008](../problems/P-0008-avatar-baseline.md) and [P-0009](../problems/P-0009-cross-style-translation.md).

## 5. Game design doesn't transfer

A shooting stat from one game means nothing in a basketball sim, and importing power from somewhere else breaks competitive balance. In many games progression *is* the product: the grind, the unlocks, the build. A "universal character" that carried its stats would break every game's balance and economy at once.

**What this means for us:** continuity should come from **claims, not state**. One game can say "this player reached the final level of Game A", and the receiving game decides what that's worth locally, if anything. Nintendo's amiibo has worked this way across many games for about a decade ([Nintendo FAQ](https://en-americas-support.nintendo.com/app/answers/detail/a_id/13260/p/603/c/947)). See [P-0014](../problems/P-0014-claim-interpretation.md).

## 6. The platforms set the terms

On consoles, identity (PlayStation Network, Xbox network), the store and payments all belong to the platform holder. Even cross-*play*, where players on different consoles play together, was resisted until Sony opened up Fortnite cross-play in September 2018. Documents from the *Epic v. Apple* trial later showed a Sony policy that charged publishers a royalty when a cross-platform game's revenue shifted away from PlayStation ([PC Gamer](https://www.pcgamer.com/sony-charges-for-crossplay-support-to-protect-psn-revenue-documents-show)). Anything that moves purchases or entitlements across platforms will have to deal with store rules and certification requirements. See [P-0021](../problems/P-0021-platform-holder-rules.md).

## 7. Liability, safety and fraud follow the player

When a game accepts a player from another game, it accepts their name, avatar and claims, and the **risk** that comes with them:

- **Offensive or infringing content.** Whoever displays an imported avatar may be responsible for it.
- **Malicious files.** 3D file parsers are an attack surface. One widely used glTF loader had a command-injection flaw that could be triggered by file paths inside an input file ([CVE-2022-3008](https://nvd.nist.gov/vuln/detail/CVE-2022-3008)).
- **Fraud and money laundering.** In 2019 Valve stopped newly bought Counter-Strike container keys from being traded or resold. It said nearly all of the keys being traded or sold on its marketplace were believed to be fraud-sourced ([Engadget](https://www.engadget.com/2019-10-30-csgo-fraud-loot-box-key-trades.html)).

**What this means for us:** every import is untrusted input. Budgets, validation, signatures and revocation are core requirements, not extras. See [P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md), [P-0012](../problems/P-0012-moderating-imported-identity.md) and [P-0015](../problems/P-0015-issuer-trust-revocation.md).

## 8. They believe they already have a "metaverse"

In 2021, Take-Two CEO Strauss Zelnick said he was skeptical of Meta's metaverse vision and argued that GTA Online, Red Dead Online and NBA 2K's online modes already deliver what people mean by the word ([CNBC](https://www.cnbc.com/2021/11/04/take-two-ceo-strauss-zelnick-says-hes-skeptical-about-facebooks-metaverse.html)). In 2022 he warned that chasing the buzzword guarantees nothing unless it creates real value for consumers ([VGC](https://www.videogameschronicle.com/news/take-two-boss-warns-it-may-not-end-well-for-companies-betting-on-blockchain-based-metaverses)).

From a large publisher's point of view, its online worlds already *are* worlds you buy into. Connecting them to other worlds adds cost and risk and splits revenue, in exchange for benefits nobody has yet proven.

## The market built "buy the world," as walled gardens

Buying a *world* rather than a game isn't hypothetical. It's how the biggest platforms already work.

- **Roblox** had $6.8B in bookings in 2025 and 144M daily active users in the fourth quarter, and creators earned more than $1.5B over the year ([GamesBeat](https://gamesbeat.com/roblox-stock-rises-20-after-earnings-daily-active-users-up-69-in-q4/); [earnings call transcript](https://www.fool.com/earnings/call-transcripts/2026/02/05/roblox-rblx-q4-2025-earnings-call-transcript/)).
- **Fortnite**: creator-made islands accounted for 47% of playtime by mid-2026, and Epic has paid creators more than $1B since 2023 ([Tubefilter](https://www.tubefilter.com/2026/06/17/epic-games-unreal-editor-for-fortnite-creator-payouts/)). Epic has described Unreal Engine 6 as a way to connect Fortnite with other Unreal games, including a persistent Disney universe ([PC Gamer](https://www.pcgamer.com/gaming-industry/epic-boss-tim-sweeney-says-unreal-engine-6-will-be-a-metaverse-joining-fortnite-and-other-unreal-games-including-an-upcoming-persistent-universe-in-development-with-disney)).
- **Subscriptions** such as Game Pass and PlayStation Plus sell access to a library of games, while your identity remains the platform account.

In every case, **identity, appearance and history stay inside one company's ecosystem.** Where interoperability exists at all, it's between that company's own products.

## What would have to be true for this to change

1. **A neutral, cheap standard that doesn't ask anyone to share their economy or their licenses.** It should start with what the *player* owns: a name, a self-made avatar and verifiable facts. That's this project.
2. **Clear value for the receiving game.** Examples include easier onboarding, players who arrive with an identity and avatar ready to go, cross-promotion and better retention. See [business-case.md](business-case.md).
3. **Proof from small games first.** For an indie game, belonging to a bigger network is a selling point, not a risk.
4. **Regulatory tailwinds.** These include data-portability rights, EU consumer rules on virtual currencies, the proposed Digital Fairness Act, pressure to preserve games and digital identity wallets. See [legal-and-policy.md](legal-and-policy.md).
5. **Player pressure.** Cross-play went from "not happening" to standard practice within a few years, once one hit game and its players pushed for it. See [interop-history.md](interop-history.md).

## Where this project fits

Our goal is a standard so useful, safe and cheap that **every** game chooses to build on it, the biggest included. We can't force that, and the walls described above are real. So the standard is designed around them:

- It **never asks a game to give up** its economy, its licenses or its rules. Each game decides what imported things mean in its world.
- It **starts with what players own**: their identity, their look and verifiable facts about what they've done. Ownership and economies come later, on their owners' terms.
- It **proves its value first where adoption is easiest**, then grows, the way the web grew from a few small sites to everything.
- It's **ready for the moments that change an industry's mind**: regulation, player pressure, or one hit game adopting it.

Cross-play went from "never" to standard practice within a few years. A shared foundation for identity and continuity can follow the same path.
