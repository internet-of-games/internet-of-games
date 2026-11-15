---
name: next-work
description: Use when asked what to work on next in the Internet of Games repository, or before picking up a problem, question or task. Lists unclaimed problems in roadmap order and explains how to claim and hand back work.
---

# Next work

## Find candidates

1. `make work` lists problems with no champion, starting with the earliest phase and the easiest work.
2. `make questions` lists every open question. To narrow it to one problem, run `python3 tools/docs.py questions --problem P-0013`.
3. `make index` prints the whole map as JSON, including which decisions affect each problem.
4. Check open GitHub issues and pull requests so you don't duplicate work that's already in flight.

## Choose

Prefer, in this order:

1. Work that unblocks the current phase in [ROADMAP.md](../../ROADMAP.md): the Phase 0 exit criteria first, then Phase 1 problems.
2. "How to help" items in those problem docs. They're sized for one contributor.
3. Open questions that a spike could answer through research ([docs/spikes](../../docs/spikes/README.md)).
4. Evidence fixes: stale review dates (`make check` warns about them) and links that `make external` reports as broken.

## Claim it

- Before starting large work, say what you're picking up in a GitHub Discussion or issue, and reference the IDs.
- A problem's champion is recorded in its `champion` field through a pull request. Agents never make themselves champions; a human does.

## Hand it back

- Open small, focused pull requests that reference IDs.
- Put results in a problem doc, a spike or an ADR, never in session notes committed to the repository.
