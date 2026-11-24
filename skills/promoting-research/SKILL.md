---
name: promoting-research
description: Use when bringing outside research into the Internet of Games docs, such as a standards update, a news item, a regulation, or a finding from a contributor, a newsletter or an AI research assistant. Covers checking it at the source, deciding where it goes, writing it in our own words, crediting others and handing it over for review.
---

# Promoting research into the docs

A research lead says something might be true and points to sources. This guide turns a lead into a sourced, original change to the docs. The rules behind it are in [docs/sourcing-and-originality.md](../../docs/sourcing-and-originality.md).

## 1. Check it at the source

For each claim in the lead:

1. Open the source it cites, then the primary source behind that: the specification's own page, the official announcement, the filing, the legal text or the repository. Claude Code users can give this step to the `source-verifier` agent, one lead at a time.
2. Record what the primary source actually says, its date, and whether the lead got it right, partly right or wrong. Leads are often slightly off: a draft described as final, a proposal described as law, a feature placed in the wrong version.
3. Look for anything newer, such as a later draft, a correction or a follow-up announcement.
4. Drop any claim you can only find in weak secondary reporting, in an AI-generated article, or behind a paywall or a login.

## 2. Compare it with what we already say

- Search the repository for the topic and its synonyms: `grep -rni '<topic>' docs problems`.
- Check the nearby facts while you're there. A new finding often shows that an older statement has gone stale.
- Check the problem docs it touches. Does it answer an open question, add an option or change a constraint?

## 3. Decide where it goes

| If the finding is… | It goes in… |
|---|---|
| A change in a standard's status, or a relevant new standard | [standards-map.md](../../docs/standards-map.md), and [landscape-2026.md](../../docs/landscape-2026.md) if it changes the big picture |
| A market or platform move | [landscape-2026.md](../../docs/landscape-2026.md) and the problem docs it affects |
| A law, a proposal or a court case | [legal-and-policy.md](../../docs/legal-and-policy.md) and the problem docs it affects |
| An earlier or parallel attempt at our problem | [prior-art.md](../../docs/prior-art.md), with its lesson |
| A fact that changes one problem's options or constraints | That problem doc's "What exists today" or "Constraints", plus a new open question if it raises one |
| Something that needs investigating | A spike ([guide](../../docs/spikes/README.md)), or a "How to help" task in the problem doc |

It's fine to decide that a finding doesn't belong anywhere. Say why in the pull request.

## 4. Write it

- Write from your notes on the facts, in your own words, at the point where readers need it. Lead with what it means for this project.
- Link the primary source at the claim. Add a secondary source only for analysis the primary source doesn't give, and say "according to".
- Credit the people whose ideas you describe.
- Give exact dates and versions, and say plainly when something is a draft or a proposal.
- Follow the doc's own guide for structure ([writing-problem-docs](../writing-problem-docs/SKILL.md), [writing-adrs](../writing-adrs/SKILL.md)).

## 5. Connect it

- Update `last_reviewed` or the `Last reviewed` line of every doc whose facts you checked.
- Add important new sources to [references.md](../../docs/references.md).
- Add back-links where other docs discuss the topic, and add new terms to the [glossary](../../docs/glossary.md).

## 6. Check and hand over

1. Run the [rights and originality review](../checking-rights/SKILL.md), or the `rights-reviewer` agent, and fix what it finds.
2. Run `make check`.
3. If you work for someone, show them the result and ask before you open a pull request. In the pull request, list the primary sources, say what you checked and say that an agent helped. Don't paste the lead's text there either.

## Red flags

- The only source for a claim is the lead itself.
- The lead quotes heavily. Its author may have copied the source; don't carry that over.
- A status word such as "ratified", "final", "law" or "launched" that you haven't read on the official page.
- A claim about what a company plans or intends that its own statements don't support.
