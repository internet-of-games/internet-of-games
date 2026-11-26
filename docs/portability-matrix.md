# What should travel between games?

*Last reviewed: 2026-11-15*

The goal is for **everything that makes up a player** to be able to travel: their identity, look, possessions, history and relationships. At the same time, every game keeps its own rules. Some of this can travel now. Other parts need rights holders, platforms or regulators on board first. This page sets out what travels, when, and why.

**Rule of thumb:** *anything the player created, and any fact about what they did, can travel now. Anything a game sold, balanced or licensed travels later, and only on its owner's terms. Every game always decides what imported things mean in its world.*

## Key

| Mark | Meaning |
|---|---|
| ✅ | **First milestones.** Works without anyone sharing an economy or a license |
| 🔜 | **Later phases.** Needs more of the standard built first |
| 🔒 | **With the owner's permission.** Travels only when the rights holder opts in |
| 🔬 | **Research.** In scope, but needs research before design |
| ⚖️ | **Each game decides.** Never transferred directly, because every game keeps its own balance; games can still read claims about it |

## The matrix

| What | When | How | Who decides locally | Why | Problem |
|---|---|---|---|---|---|
| Display name | ✅ | Self-asserted, in the Carryfile | The receiving game can enforce its own naming rules (profanity, impersonation, uniqueness) | Players created it, but games still need to moderate it | [P-0012](../problems/P-0012-moderating-imported-identity.md) |
| Identifier | ✅ | A DID, or a different identifier per game | The player chooses whether games can correlate them | Recognition without tracking | [P-0003](../problems/P-0003-player-identifier.md), [P-0006](../problems/P-0006-privacy-unlinkability.md) |
| 3D avatar | ✅ | A VRM/glTF file with a hash, budgets and license metadata | The receiving game can reject it, scale it down or substitute it | A player-owned look is the heart of "same character" | [P-0008](../problems/P-0008-avatar-baseline.md), [P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md) |
| 2D portrait | ✅ | An image file with a hash | The receiving game can moderate it | A fallback that works in any game | [P-0008](../problems/P-0008-avatar-baseline.md) |
| Achievements and milestones | ✅ | Credentials signed by the issuing game, shown selectively | The receiving game maps them to local meaning, or ignores them | Continuity without importing power | [P-0013](../problems/P-0013-portable-claims.md), [P-0014](../problems/P-0014-claim-interpretation.md) |
| Playtime, rank, skill | ✅ | Coarse bands ("top 10%"), signed, and shared only if the player opts in | The receiving game | Useful for matchmaking and story, but a privacy and profiling risk | [P-0006](../problems/P-0006-privacy-unlinkability.md), [P-0013](../problems/P-0013-portable-claims.md) |
| Appearance description | 🔜 | Style-independent traits (hair, colors, build and so on) | The receiving game renders them in its own art style | A mesh can't cross art styles, but a description can | [P-0009](../problems/P-0009-cross-style-translation.md) |
| Age and eligibility | 🔜 | A yes/no claim ("over 13") from a trusted issuer, never a birthdate | The receiving game, based on its legal duties | Age ratings and child-safety law | [P-0007](../problems/P-0007-age-and-eligibility.md) |
| Accessibility and comfort preferences | 🔜 | A self-asserted settings vocabulary, private by default | The receiving game maps them to its own settings | High value and low risk, but they can reveal sensitive information | [P-0028](../problems/P-0028-portable-preferences.md) |
| World addresses and links | 🔜 | A stable address for each world and each place in it, like a URL | The destination game | This is the "internet" part: worlds that link to each other | [P-0029](../problems/P-0029-world-addressing-and-links.md), [P-0017](../problems/P-0017-world-handoff.md) |
| Friends and blocks | 🔜 | Opt-in; portable *blocks* may come first | The player and the game | Safety first, presence after | [P-0018](../problems/P-0018-friends-and-presence.md) |
| Cosmetic rewards | 🔜 | Game B **grants** its own item to holders of a Game A credential | Game B | A promotion, not a transfer of value | [P-0019](../problems/P-0019-cross-game-entitlements.md) |
| Purchased items from another game | 🔒 | Entitlements first; true cross-game ownership once rights holders and platforms agree | The selling game, plus the receiving game | Licenses and platform store rules | [P-0019](../problems/P-0019-cross-game-entitlements.md), [P-0021](../problems/P-0021-platform-holder-rules.md) |
| Licensed content (league players, film characters, music, brands, real people's likenesses) | 🔒 | Only when the rights holder licenses it across participating games | The rights holder, then each game | License scope, brand safety and likeness rights | [P-0011](../problems/P-0011-rights-licensing-likeness.md) |
| Avatars built from a game's own art | 🔒 | Only if that game allows export | The originating game | Those assets are the game's IP, not the player's | [P-0011](../problems/P-0011-rights-licensing-likeness.md) |
| Stats, abilities, levels | ⚖️ | Games can read claims about them, never imported numbers | Each game | One game's numbers are meaningless or unfair in another | [why-not-yet §5](why-not-yet.md#5-game-design-doesnt-transfer) |
| Items with gameplay effects | ⚖️ | The receiving game may grant its own equivalent | Each game | Balance and economy | [why-not-yet §5](why-not-yet.md#5-game-design-doesnt-transfer) |
| Currency and tradable value | 🔬 | To be designed after research | — | Fraud, consumer and financial law, platform rules, publisher economics | [P-0020](../problems/P-0020-connected-economies.md) |
| Moderation standing and bans | 🔬 | To be designed after research | — | Due process, defamation and data-protection risk | [P-0016](../problems/P-0016-portable-reputation.md) |
| World state and consequences | 🔬 | Possibly as signed "world facts" | Each game is its own canon | Very hard; see the research tracks | [P-0022](../problems/P-0022-persistent-consequences.md) |
| AI companion memory | 🔬 | Possibly as player-held summaries, never raw logs | The player | Privacy, safety and cost | [P-0023](../problems/P-0023-traveling-ai-characters.md) |

## Why "claims, not state" works

The things that never transfer directly (stats, balance-affecting items) are exactly the things each game *balances*. The things that travel first (name, look, facts) are things a game only has to *interpret*. A receiving game that gets "this player cleared the hardest raid in Game A" can:

- ignore it
- show it on a profile
- give a cosmetic title or outfit
- have a character mention it in dialogue

…all without touching a single number in its own balance or economy. Nintendo's amiibo has worked this way for about a decade, and Skylanders and Pokémon HOME follow the same pattern ([prior-art.md](prior-art.md)).
