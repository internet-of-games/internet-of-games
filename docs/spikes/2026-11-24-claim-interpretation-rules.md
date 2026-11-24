# Spike: How should a game write down what foreign claims mean to it?

*Date: 2026-11-24 · Problems: P-0014, P-0019 · Time box: 1 day*

## Question

Verifying that a player cleared the final boss in Game A only matters if Game B can decide, simply and safely, what that means locally ([P-0014](../../problems/P-0014-claim-interpretation.md)). What should those local rules look like, and can cross-game reward offers ([P-0019](../../problems/P-0019-cross-game-entitlements.md)) use the same format?

## Approach

A design exercise. We started from the constraints in P-0014 and P-0019, the way amiibo, Skylanders and Pokémon HOME let the receiving game decide ([prior art](../prior-art.md)), and the EU's proposed rules on paid items ([legal and policy](../legal-and-policy.md#5-virtual-currencies-loot-boxes-and-consumer-protection)). We compared two styles of rule and wrote examples for three made-up games.

## Findings

### 1. What a rule needs

- **A match:** which issuers the game trusts, which achievement or category, optionally a band (such as "top 10%"), and the lowest trust level it accepts, for example rejecting claims signed on a player's device by an offline game ([P-0030](../../problems/P-0030-built-for-every-game.md)).
- **A verified claim:** the rule runs only after the signature, the revocation status and the expiry have been checked, so rules never deal with raw, unverified data.
- **An effect named by the game:** a title, a cosmetic, a profile badge or a line of dialogue, using the game's own item IDs. Nothing is imported.
- **A limit:** for example once per player, counted under the game's own identifier for that player ([P-0019](../../problems/P-0019-cross-game-entitlements.md), question P-0019-Q1).

### 2. Two styles of rule

| Style | Gains | Costs |
|---|---|---|
| **Fixed-shape rules:** a small JSON object with known fields | Any engine can evaluate it with a few dozen lines of code; easy to read and review; no code runs | Can't express unusual combinations of conditions |
| **A general expression language,** such as the [Common Expression Language](https://github.com/cel-expr/cel-spec) (Apache-2.0) or [JSON Logic](https://github.com/jwadhams/json-logic-js) (MIT) | Rules can combine any conditions | Every engine needs an interpreter for the language; rules are harder to review; more room for mistakes |

### 3. A sketch of the fixed-shape format

```json
{
  "version": 0,
  "rules": [
    {
      "id": "veteran-of-game-a",
      "when": {
        "issuers": ["did:web:game-a.example"],
        "category": "completed-main-story",
        "min_trust": "server-signed"
      },
      "then": [
        { "kind": "title", "item": "game-a-veteran" },
        { "kind": "narrative", "item": "innkeeper-greets-veteran" }
      ],
      "limit": "once-per-player"
    }
  ]
}
```

- `when` matches a verified claim. Leaving out `issuers` means "any issuer on the game's trust list".
- `then` lists effects. `kind` comes from a short list (`cosmetic`, `title`, `social`, `narrative`, `other`) so integration guides and conformance tests can check that, by default, effects don't touch gameplay power. The format can't stop a game granting power; it makes the choice visible.
- `item` is the receiving game's own ID; display text, translations and art stay in the game.

### 4. Offers reuse the same format

An offer is a rule that the game publishes, plus what a player needs to decide: a description, the terms, the limit and the dates. A game's manifest could list its offers so directories can show them ([P-0027](../../problems/P-0027-discovery.md)). Redemption is recorded under the game's own identifier for the player, so nothing tracks the player across games.

### 5. Keeping offers clear of the EU's proposed rules on paid items

The proposed Digital Fairness Act deals with paid virtual currencies, paid random rewards and pay-to-win purchases ([legal and policy §5](../legal-and-policy.md#5-virtual-currencies-loot-boxes-and-consumer-protection)). A reward granted free, on the strength of a claim, falls outside those categories. Two habits keep it that way:

- **Make offers deterministic.** A free random reward isn't the paid kind the proposal targets, but a fixed reward is easier to explain and keeps offers away from loot-box mechanics altogether.
- **Never require a purchase in the receiving game.** An offer that needs a payment is a purchase, and the price rules apply, along with the stricter rules for games used by minors.

This is a design habit, not legal advice; integrators should check the rules in their markets.

### 6. Shared categories and rarity

- **Issuer-specific rules are enough for Phase 1.** A rule can name one issuer and one achievement.
- **A short shared list of categories** would let a game honor, say, any trusted issuer's "completed-main-story" claim. A seed list of five or six categories, maintained in this repository with additions by pull request, answers part of P-0013-Q2 and P-0014-Q4.
- **Rarity hints from issuers** (P-0014-Q1) are easy to inflate. A rule could use them, but games should treat them as claims from an interested party, and v0 can leave them out.

### 7. Three examples

| Receiving game | Rule | Effect |
|---|---|---|
| A fantasy role-playing game | Any trusted issuer's `completed-main-story` claim | The title "Veteran of another world" and a greeting from the innkeeper |
| A racing game | A `won-a-season` claim from two named sports sims | A free paint job, once per player, published as an offer with its terms |
| A narrative adventure | A `reached-max-level` claim from any trusted issuer | A character mentions "a legendary journey elsewhere", without naming the other game, so the line suits any issuer |

## Limitations

- No implementation or user testing yet.
- We didn't interview game designers about the rules they'd want.
- The point about the Digital Fairness Act rests on a proposal that may change, and isn't legal advice.

## Recommendation

- Use fixed-shape rules for Phase 1, and keep an expression language as a later option if real rules outgrow them.
- Define the effect kinds and a seed list of shared categories, and test both in the demo games.
- Write offers as rules with a published description and terms, deterministic and free by default.
- Treat rarity hints as optional and leave them out of v0.

## Sources

- Problem docs [P-0013](../../problems/P-0013-portable-claims.md), [P-0014](../../problems/P-0014-claim-interpretation.md), [P-0019](../../problems/P-0019-cross-game-entitlements.md) and [P-0030](../../problems/P-0030-built-for-every-game.md); [prior art](../prior-art.md); [legal and policy](../legal-and-policy.md)
- [Common Expression Language specification](https://github.com/cel-expr/cel-spec) · [JSON Logic for JavaScript](https://github.com/jwadhams/json-logic-js), read through the GitHub API on 24 November 2026
