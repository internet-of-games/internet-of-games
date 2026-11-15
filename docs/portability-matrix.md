# What should travel between games?

*Last reviewed: 2026-11-15*

The [vision](../VISION.md) says the goal is "to preserve identity and meaningful continuity while allowing games to maintain their own rules." This page turns that into a concrete position for each piece of a character.

**Rule of thumb:** *if the player created it, or it describes a fact, it can travel. If a game sold it, balanced it or licensed it, it stays where it is, though the receiving game may choose to grant an equivalent.*

| What | Travels? | How | Who decides locally | Why | Problem |
|---|---|---|---|---|---|
| Display name | ✅ Yes | Self-asserted, in the player document | The receiving game can enforce its own naming rules (profanity, impersonation, uniqueness) | Players created it; games still need to moderate it | [P-0012](../problems/P-0012-moderating-imported-identity.md) |
| Identifier | ✅ Yes (with privacy) | A DID, or a different identifier per game | The player chooses whether games can correlate them | Recognition without tracking | [P-0003](../problems/P-0003-player-identifier.md), [P-0006](../problems/P-0006-privacy-unlinkability.md) |
| 3D avatar | ✅ Yes | A VRM/glTF file with a hash, budgets and license metadata | The receiving game can reject it, scale it down or substitute it | Player-owned appearance is the heart of "same character" | [P-0008](../problems/P-0008-avatar-baseline.md), [P-0010](../problems/P-0010-avatar-budgets-and-file-safety.md) |
| Appearance description | ✅ Yes | Style-independent traits (hair, colors, build and so on) | The receiving game renders them in its own art style | A mesh can't cross art styles; a description can | [P-0009](../problems/P-0009-cross-style-translation.md) |
| 2D portrait | ✅ Yes | An image file with a hash | The receiving game can moderate it | A fallback for any game | [P-0008](../problems/P-0008-avatar-baseline.md) |
| Achievements and milestones | ✅ Yes, as claims | Credentials signed by the issuing game, shown selectively | The receiving game maps them to local meaning, or ignores them | Continuity without importing power | [P-0013](../problems/P-0013-portable-claims.md), [P-0014](../problems/P-0014-claim-interpretation.md) |
| Playtime, rank, skill | ⚠️ Carefully | Coarse bands ("top 10%"), signed, shown only if the player chooses | The receiving game | Useful for matchmaking and story, but risky for privacy and profiling | [P-0006](../problems/P-0006-privacy-unlinkability.md), [P-0013](../problems/P-0013-portable-claims.md) |
| Age and eligibility | ✅ Yes, minimal | A yes/no claim ("over 13") from a trusted issuer, never a birthdate | The receiving game, based on its legal duties | Ratings and child-safety law | [P-0007](../problems/P-0007-age-and-eligibility.md) |
| Accessibility and comfort preferences | ✅ Yes, opt-in | Self-asserted settings vocabulary, kept private by default | The receiving game maps them to its own settings | High value and low risk, though they can reveal sensitive information | [P-0028](../problems/P-0028-portable-preferences.md) |
| Friends and blocks | ⏳ Later | Opt-in; portable *blocks* may come first | Player and game | Safety first, presence later | [P-0018](../problems/P-0018-friends-and-presence.md) |
| Cosmetic rewards | ✅ Yes, as entitlements | Game B **grants** its own item to holders of a Game A credential | Game B | A promotion, not a transfer of value | [P-0019](../problems/P-0019-cross-game-entitlements.md) |
| Moderation standing, bans | ❌ Not by default | Research only | — | Due process, defamation and data-protection risk | [P-0016](../problems/P-0016-portable-reputation.md) |
| Stats, abilities, levels | ❌ No | — | — | Balance: one game's numbers are meaningless or unfair in another | [why-not-yet §5](why-not-yet.md#5-game-design-doesnt-transfer) |
| Items with gameplay effects | ❌ No | — | — | Balance and economy | [why-not-yet §5](why-not-yet.md#5-game-design-doesnt-transfer) |
| Currency and tradable value | ❌ Not now | Research only | — | Fraud, consumer and financial law, platform rules, publisher economics | [P-0020](../problems/P-0020-connected-economies.md) |
| Purchased cosmetics from another game's store | ❌ Not as a transfer | Only as an entitlement the receiving game chooses to grant | Game B | Licenses and platform store rules | [P-0019](../problems/P-0019-cross-game-entitlements.md), [P-0021](../problems/P-0021-platform-holder-rules.md) |
| Licensed content (league players, film characters, music, brands, real people's likenesses) | ❌ Never | — | — | License scope, brand safety, likeness rights | [P-0011](../problems/P-0011-rights-licensing-likeness.md) |
| Avatars built from a game's own art assets | ❌ Not by default | Only if that game explicitly allows export | The originating game | Those assets are the game's IP, not the player's | [P-0011](../problems/P-0011-rights-licensing-likeness.md) |
| World state and consequences | 🔬 Research | Possibly as signed "world facts" | Each game is its own canon | Very hard; see the research tracks | [P-0022](../problems/P-0022-persistent-consequences.md) |
| AI companion memory | 🔬 Research | Possibly as player-held summaries, never raw logs | The player | Privacy, safety and cost | [P-0023](../problems/P-0023-traveling-ai-characters.md) |

## Why "claims, not state" works

The things that can't travel (stats, items, currency) are exactly the things each game *balances*. The things that can travel (name, look, facts) are things a game only has to *interpret*. A receiving game that gets a claim like "this player cleared the hardest raid in Game A" can:

- ignore it
- show it on a profile
- give a cosmetic title or outfit
- have a character mention it in dialogue

…without changing a single number in its own balance or economy. Nintendo's amiibo has worked this way for about a decade, and Skylanders and Pokémon HOME show the same pattern ([prior-art.md](prior-art.md)).
