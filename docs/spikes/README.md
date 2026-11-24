# Spikes

A spike is a time-boxed investigation that answers **one question** with research or a quick prototype, for example: "Which identifier methods can a Godot game verify without extra libraries?"

- **Naming:** `YYYY-MM-DD-short-topic.md`, using the date the spike was written up. The title starts with `Spike:`.
- **Start from** [TEMPLATE.md](TEMPLATE.md).
- **Show your work:** every spike lists its sources and its limitations. Prototype code belongs in a pull request or a linked branch, not in this folder.
- **Feed the result back:** update the problem doc's options or questions, or propose an ADR if the spike settles a decision.
- **Spikes are point-in-time records.** Don't update the findings later; if things change, write a new spike.

## Spikes so far

| Date | Spike | Problems |
|---|---|---|
| 2026-11-24 | [How does the Web of Worlds user manifest compare with our player passport?](2026-11-24-web-of-worlds-user-manifest.md) | P-0003, P-0013, P-0017, P-0028, P-0029 |
| 2026-11-24 | [Which IP policy should govern our specification text?](2026-11-24-specification-ip-policies.md) | P-0001 |
| 2026-11-24 | [Which signature algorithms can each engine verify without extra libraries?](2026-11-24-signature-support-in-engines.md) | P-0003, P-0013, P-0025 |
| 2026-11-24 | [What budgets and file rules should the v0 avatar baseline use?](2026-11-24-avatar-budgets-and-file-rules.md) | P-0008, P-0010, P-0011 |
| 2026-11-24 | [How should a game write down what foreign claims mean to it?](2026-11-24-claim-interpretation-rules.md) | P-0014, P-0019 |
| 2026-11-24 | [What should the malicious and edge-case avatar test files cover?](2026-11-24-avatar-test-corpus.md) | P-0010, P-0026 |
| 2026-11-24 | [Which identifier method should Phase 1 use?](2026-11-24-identifier-methods.md) | P-0003, P-0005, P-0006, P-0024 |

More candidates are in the "How to help" sections of the [problem docs](../../problems/README.md).
