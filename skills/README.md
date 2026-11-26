# Skills

Skills are step-by-step guides that AI agents load when a task matches them. Each one lives in `skills/<name>/SKILL.md`, with a short `name` and `description` in its front matter. The `.claude/skills` and `.cursor/skills` folders link here, so Claude Code and Cursor share the same skills.

| Skill | Use it when |
|---|---|
| [writing-problem-docs](writing-problem-docs/SKILL.md) | Adding a problem, or making a substantial change to one |
| [writing-adrs](writing-adrs/SKILL.md) | Recording a decision |
| [verifying-sources](verifying-sources/SKILL.md) | Adding or checking facts and citations |
| [next-work](next-work/SKILL.md) | Choosing what to work on next |
| [promoting-research](promoting-research/SKILL.md) | Bringing outside research into the docs |
| [checking-rights](checking-rights/SKILL.md) | Checking a change for copying, credit, licenses and confidential material |
| [visual-summaries](visual-summaries/SKILL.md) | Writing a pull request description, an issue, a Discussion or a long comment |

Claude Code users also get two review agents in `.claude/agents/`: `source-verifier` and `rights-reviewer`. They run on Claude's Opus model, report what they find and don't change files.

Skills are guardrail files: any change to them needs a maintainer's review ([AGENTS.md](../AGENTS.md), rule 15).
