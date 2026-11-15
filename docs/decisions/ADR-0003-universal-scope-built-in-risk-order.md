---
id: ADR-0003
title: Scope the project as a universal standard, built in order of risk
status: accepted
date: 2026-11-15
problems: [P-0002, P-0029, P-0030]
topics: [scope, roadmap]
supersedes: []
superseded_by: null
---

# ADR-0003: Scope the project as a universal standard, built in order of risk

## Context

The project was first described as letting "two independently developed games recognize the same player character". That framing is too narrow. The goal is the baseline that *every* game builds on: big publishers and indies, games from different companies and from the same company. It covers a player's whole digital life (identity, appearance, possessions, history and relationships), plus links between the worlds themselves. At the same time, earlier efforts that tried to do everything at once, starting with economies, stalled ([prior-art.md](../prior-art.md)).

This decision aims to set an ambitious scope without making the first deliverables unbuildable.

## Options

1. **Player-character portability between independent games only.** Achievable, but it leaves out most of the vision and casts the project as a niche.
2. **Everything at once, including economies.** Matches the ambition, but stalls on legal, business and safety risk.
3. **A universal scope, delivered in layers ordered by risk**, starting with a small first milestone.

## Decision

We will define the project's scope as a universal standard for every game, covering identity, appearance, possessions, history, relationships and links between worlds, and deliver it in layers ordered by risk, starting with a small first milestone.

## Consequences

- The docs distinguish the **scope** (everything) from the **milestones** (one proof at a time). See the [problem statement](../problem-statement.md).
- Currencies, purchased and licensed items, and shared worlds are "sequenced later, not excluded", and the roadmap now runs to Phase 5.
- Two problems were added: world addressing and links ([P-0029](../../problems/P-0029-world-addressing-and-links.md)) and built for every game ([P-0030](../../problems/P-0030-built-for-every-game.md)).
- Every proposal is now checked against universality, which adds design work early but avoids ruling out whole categories of games later.

## Universality and safety

This decision *is* the universality requirement ([P-0030](../../problems/P-0030-built-for-every-game.md)). Building in risk order delays the highest-stakes threats, especially fraud (T6 in the [threat model](../threat-model.md)), until research shows how to handle them.
