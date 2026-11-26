# Commit messages

Clear commit messages keep the history readable for people and agents alike. Use this format:

```text
<type>(<scope>): <summary in the imperative, under 72 characters>

<optional body: what changed and why, wrapped at about 72 characters>

Signed-off-by: Your Name <your-email>
```

## Types

| Type | Use it for |
|---|---|
| `problem` | Adding or changing problem docs in `problems/` |
| `adr` | Adding a decision record, or annotating one |
| `spike` | Adding a spike |
| `docs` | Other documentation: vision, roadmap, research docs, glossary, references |
| `spec` | Normative specification text (from Phase 1 onward) |
| `tools` | The checker, the Makefile and the skills |
| `ci` | GitHub Actions and other repository automation |
| `community` | Contributing, governance, conduct and templates |
| `chore` | Anything that changes no meaning |

## Scope

Use the ID the change is about, such as `problem(P-0013): …` or `adr(ADR-0009): …`. For broader changes, name the area instead, such as `docs(landscape): …`. If nothing fits, leave the scope out.

## Examples

```text
problem(P-0013): compare Open Badges and SD-JWT credential profiles
adr(ADR-0009): choose a default player identifier method
docs(landscape): update platform figures for Q3 2026
tools: check that the decision index matches front matter
```

## Rules

- Make one logical change per commit.
- Name the question IDs a commit answers or changes, for example "Answers P-0003-Q1."
- Sign off under the [Developer Certificate of Origin](https://developercertificate.org/) with `git commit -s`. If an AI agent helped, the human who directed it reviews the change, signs it off and is responsible for it. An agent adds a sign-off only when that person tells it to.
- To credit an agent, add an `Assisted-by:` trailer with its name and model, for example `Assisted-by: Claude:claude-opus-5-5`. Don't use `Co-authored-by:` for an agent, because that presents it as an author. The Linux kernel's rules for AI coding assistants also use `Assisted-by:`, and say that only people can certify the DCO ([kernel guidance](https://docs.kernel.org/process/coding-assistants.html)).
- Never put secrets or personal data in commit messages. They stay public forever.
- Pull request titles follow the same format.
