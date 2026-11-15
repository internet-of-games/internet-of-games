# Decision records

An architecture decision record (ADR) captures one decision: its context, the options considered, what we chose and what follows from it. Problem docs explore; ADRs decide. [ADR-0001](ADR-0001-record-decisions-as-adrs.md) explains why we use them.

## How they work

- **One decision per record.** Files are named `ADR-NNNN-short-title.md`. Run `make next` to get the next number, and check open pull requests for numbers already in use.
- **Status** is `accepted`, `superseded` or `deprecated`. A record is accepted when its pull request merges, and the discussion happens during review.
- **Accepted records aren't rewritten.** Fixing typos, adding links or updating the status is fine. If the decision itself changes, write a new ADR that supersedes the old one and set `supersedes` and `superseded_by` on both.
- **Living documents follow decisions.** In the same pull request, update everything the decision affects: strike through answered questions in problem docs and link the ADR, and update the layer model, portability matrix or design principles if they change.
- **Every record states its impact** on universality ([P-0030](../../problems/P-0030-built-for-every-game.md)) and on the [threat model](../threat-model.md).
- **Full guide:** [skills/writing-adrs](../../skills/writing-adrs/SKILL.md). Template: [TEMPLATE.md](TEMPLATE.md). `make check` validates every record and this index.

## Index

| ID | Decision | Status | Date |
|---|---|---|---|
| [ADR-0001](ADR-0001-record-decisions-as-adrs.md) | Record decisions as ADRs | Accepted | 2026-11-15 |
| [ADR-0002](ADR-0002-license-code-apache-docs-cc-by.md) | License code under Apache-2.0 and documents under CC BY 4.0 | Accepted | 2026-11-15 |
| [ADR-0003](ADR-0003-universal-scope-built-in-risk-order.md) | Scope the project as a universal standard, built in order of risk | Accepted | 2026-11-15 |
| [ADR-0004](ADR-0004-compose-existing-open-standards.md) | Compose existing open standards instead of inventing new formats | Accepted | 2026-11-15 |
| [ADR-0005](ADR-0005-never-require-blockchains-tokens-or-wallets.md) | Never require blockchains, tokens or wallets | Accepted | 2026-11-15 |
| [ADR-0006](ADR-0006-permanent-ids-for-problems-questions-decisions.md) | Give problems, questions and decisions permanent IDs | Accepted | 2026-11-15 |
| [ADR-0007](ADR-0007-one-repository-until-there-is-code.md) | Keep everything in one repository until there is code | Accepted | 2026-11-15 |
| [ADR-0008](ADR-0008-continuity-as-signed-claims-not-state.md) | Carry continuity as signed claims, not transferred game state | Accepted | 2026-11-15 |
