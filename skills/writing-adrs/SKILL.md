---
name: writing-adrs
description: Use when recording a decision in docs/decisions/ in the Internet of Games repository, or when superseding or annotating an existing decision record. Covers when to write one, structure, status rules, living-document updates and checks.
---

# Writing ADRs

An ADR records a single decision. Problem docs explore options; an ADR closes a question.

## When to write one

Write an ADR when:

- a question in a problem doc has an answer the community agrees on
- a choice will be hard to reverse, or others will build on it

Don't write one for small, easily reversed choices or for open exploration. Use a problem doc or a spike for those.

## Steps

1. Get the next number with `make next`. Check open pull requests for numbers already in flight.
2. Copy [docs/decisions/TEMPLATE.md](../../docs/decisions/TEMPLATE.md) to `docs/decisions/ADR-NNNN-short-slug.md`.
3. Fill in the front matter:
   - `id` matches the file name.
   - `title` matches the heading (`# ADR-NNNN: Title`) and is phrased as an instruction ("Choose…", "Keep…").
   - `status: accepted`. The pull request is the proposal, and merging it is the acceptance.
   - `problems` lists the problem IDs the decision settles or affects. Use `["*"]` only for project-wide decisions.
   - `topics` adds tags that make the ADR easier to find.
4. Write the sections:
   - **Context:** the situation, linking to problem docs rather than repeating them. End with one sentence that starts "This decision aims to …".
   - **Options** (optional): real alternatives only, each with its main trade-off.
   - **Decision:** open with the choice in one sentence ("We will …"), then add only what's needed to apply it.
   - **Consequences:** what gets easier, what gets harder, and what new questions come up.
   - **Universality and safety:** the effect on every kind of game ([P-0030](../../problems/P-0030-built-for-every-game.md)) and on threats T1–T8 in the [threat model](../../docs/threat-model.md), or "Not applicable: process decision".
5. Stick to one decision. If you find yourself writing "We will also…", that's a second ADR.
6. Keep implementation out. The ADR's pull request contains the decision and the living-document updates; track follow-up work in issues.

## Update the living documents in the same pull request

- Add a row for the ADR to [docs/decisions/README.md](../../docs/decisions/README.md).
- In each affected problem doc, strike through the questions it answers and link the ADR (`- ~~**P-0003-Q1:** …~~ Decided in [ADR-0009](…).`). Add the ADR to that doc's "Decisions so far" section.
- If the decision changes [layer-model.md](../../docs/layer-model.md), [portability-matrix.md](../../docs/portability-matrix.md), [design-principles.md](../../docs/design-principles.md) or the threat model, make small, targeted edits there.
- Don't rewrite whole sections, and don't touch documents the decision doesn't affect.

## Changing a decision later

- Accepted ADRs are records. Fixing typos and broken links, adding cross-links and changing the status are fine. Rewriting Context, Decision or Consequences is not.
- To change a decision, write a new ADR with `supersedes: [ADR-old]`. Set the old ADR to `status: superseded` with `superseded_by: ADR-new`, and update both index rows.
- Use `deprecated` for a decision that no longer applies and isn't being replaced.

## Finish

`make check` must pass. Commit as `adr(ADR-NNNN): <summary>` and sign off.

## Red flags

- **The Context restates a problem doc at length.** Link to it instead.
- **The Decision opens with mechanics.** Lead with the choice.
- **A number or limit has no stated basis.** Give the basis, or mark it as an initial value to revisit.
- **`problems` lists more than three problems.** The decision may be too broad.
