---
name: writing-problem-docs
description: Use when adding a new problem doc under problems/ or substantially changing an existing one in the Internet of Games repository. Covers IDs, front matter, structure, citations, two-way links, the index and the checks.
---

# Writing problem docs

A problem doc describes one sub-problem of the mission. It explores options; it doesn't decide between them. Decisions go in ADRs ([writing-adrs](../writing-adrs/SKILL.md)).

## Before you start

1. Make sure the problem isn't already covered. Read [problems/README.md](../../problems/README.md) and search for the topic (`grep -rn '<topic>' problems docs`).
2. If it's a variant of an existing problem, add to that doc instead of creating a new one.
3. Get the next ID with `make next`, and check open pull requests for the same number.

## Write the doc

1. Copy [problems/TEMPLATE.md](../../problems/TEMPLATE.md) to `problems/P-NNNN-short-slug.md`.
2. Fill in the front matter:
   - `id` matches the file name, and `title` matches the first heading (`# P-NNNN: Title`).
   - `layer`, `phase`, `status` and `difficulty` use the values listed in the template.
   - `related` lists problem IDs in sorted order. Every problem you list must list this one back.
   - `last_reviewed` is today's date.
3. Write the sections:
   - **In one sentence:** the problem, not a solution.
   - **Why it matters:** what breaks for players or developers.
   - **What exists today:** prior art and standards, with every claim cited.
   - **Constraints:** link the design principles that apply.
   - **What "solved enough" looks like:** testable checkboxes for the problem's phase.
   - **Candidate directions:** at least two real options, each with what it gains and what it costs. Don't pick a winner; that's an ADR's job.
   - **Threats:** which threats in the [threat model](../../docs/threat-model.md) apply, and how each option handles them.
   - **Works for every game?:** how the options hold up across game sizes, genres, platforms, ratings and connectivity ([P-0030](../../problems/P-0030-built-for-every-game.md)).
   - **Open questions:** written as `- **P-NNNN-Q1:** …` and numbered from 1, in order.
   - **Champion brief** (for problems in the current or next phase): the first deliverable, the decisions a champion would drive, helpful background and the expected commitment.
   - **How to help:** concrete tasks a newcomer could pick up.
   - **References.**

## Connect it

1. Add the reciprocal `related` entry to every problem you listed.
2. Find existing passages that substantively discuss the topic (search for the topic and its synonyms). Add one back-link at each such passage, not one at every mention.
3. Add a row to [problems/README.md](../../problems/README.md) in the right phase section, matching the front matter exactly.
4. If the problem changes the architecture, update [docs/layer-model.md](../../docs/layer-model.md) and the scope table in the [problem statement](../../docs/problem-statement.md).
5. Add new terms to [docs/glossary.md](../../docs/glossary.md).

## Finish

1. `make check` must pass with no errors.
2. Commit as `problem(P-NNNN): <summary>`, signed off (`git commit -s`), following [COMMITS.md](../../COMMITS.md).

## Changing an existing problem doc

- Never renumber or reuse IDs. Add new questions at the end of the list.
- Don't delete answered questions. Strike them through and link the ADR that answered them.
- If you change `status` or `phase`, update the index row as well.
- If you re-check facts, update `last_reviewed`.

## Red flags

- **The doc recommends one answer.** Move that decision into an ADR.
- **A claim has no source.** Find one, or remove the claim.
- **An option lists gains but no costs.** You haven't looked hard enough.
- **The doc only works for one kind of game.** Revisit [P-0030](../../problems/P-0030-built-for-every-game.md).
