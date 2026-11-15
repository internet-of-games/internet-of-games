# Skills

Skills are step-by-step guides that AI agents load when a task matches them. Each one lives in `skills/<name>/SKILL.md`, with a short `name` and `description` in its front matter. The `.claude/skills` and `.cursor/skills` folders link here, so Claude Code and Cursor share the same skills.

| Skill | Use it when |
|---|---|
| [writing-problem-docs](writing-problem-docs/SKILL.md) | Adding a problem, or making a substantial change to one |
| [writing-adrs](writing-adrs/SKILL.md) | Recording a decision |
| [verifying-sources](verifying-sources/SKILL.md) | Adding or checking facts and citations |
| [next-work](next-work/SKILL.md) | Choosing what to work on next |

Skills are guardrail files: any change to them needs a maintainer's review ([AGENTS.md](../AGENTS.md), rule 15).
