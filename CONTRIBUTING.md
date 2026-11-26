# Contributing to the Internet of Games

Thanks for being here. This project is at **Phase 0**: we're defining the problem before we write specs or code. Right now, the most valuable contributions are **evidence, critique and careful thinking**.

## Ways to contribute

| You want to… | Do this |
|---|---|
| Ask a question or float an idea | Start a thread in **GitHub Discussions** |
| Fix a fact, add a source or flag something out of date | Open an issue with the **Evidence / correction** template, or send a pull request |
| Propose a new sub-problem | Open an issue with the **New problem** template |
| Work on an existing problem | Comment on it in Discussions, referencing its ID (`P-0008`), or offer to champion it |
| Improve the docs | Send a pull request |

Not sure where to start? See the **good first problems** in [problems/README.md](problems/README.md#good-first-problems).

## What we can and can't accept

This is a public repository, and everything in it has to be safe to share. **Please don't submit:**

- **Third-party copyrighted material:** game screenshots, logos, character art, ripped models or textures, music, or text copied from other sources beyond short, attributed quotes. See [sourcing and originality](docs/sourcing-and-originality.md).
- **Confidential information:** anything covered by a non-disclosure agreement, including platform-holder documentation, unreleased product details or internal company material.
- **Personal data:** real players' names, emails, account IDs, or anything that identifies a real person, including in test files. Use made-up data.
- **Secrets:** API keys, tokens, passwords or private keys, even "test" ones.
- **Fan art of existing characters** as test avatars. Test assets must be original and released under CC0.

Mentioning products and companies by name to describe the problem is fine. See [TRADEMARKS.md](TRADEMARKS.md).

## Writing guidelines

- **Cite your sources.** Every factual claim should link to a source. Prefer primary sources (specifications, filings, official announcements, repositories). If you can only find secondary reporting, say "reported" or "according to".
- **Write in your own words.** Quote briefly (40 words at most) with a link, and credit the ideas you build on. The full rules are in [sourcing and originality](docs/sourcing-and-originality.md).
- **Use plain language.** Write for a smart reader who isn't an expert in *your* field. Define jargon or link to the [glossary](docs/glossary.md).
- **Separate facts from opinions.** Proposals go under "candidate directions", not in the description of what exists.
- **Update "Last reviewed"** when you check a doc's facts.
- **Reference problem IDs** (`P-0013`, `P-0013-Q2`) so threads stay connected.
- **Be fair to the companies we discuss.** Describe what they've publicly said or done, not what we imagine they think.

## Problem docs, decisions and spikes

- **Problem docs** (`problems/`) explore one sub-problem: options, trade-offs and open questions. Guide: [skills/writing-problem-docs](skills/writing-problem-docs/SKILL.md).
- **Decision records** (`docs/decisions/`) record what we decided and why. Guide: [skills/writing-adrs](skills/writing-adrs/SKILL.md).
- **Spikes** (`docs/spikes/`) report time-boxed investigations. Guide: [docs/spikes/README.md](docs/spikes/README.md).

Every proposal names the threats it affects ([threat model](docs/threat-model.md)) and explains how it works for every kind of game ([P-0030](problems/P-0030-built-for-every-game.md)).

## Working with AI agents

AI agents are welcome tools here, and the repository is set up for them.

- **Point your agent at [AGENTS.md](AGENTS.md).** It has the rules, a map of the repository and a guide for each kind of task. Claude Code loads it automatically through [CLAUDE.md](CLAUDE.md), and the [skills](skills/README.md) work in both Claude Code and Cursor.
- **You're responsible for what your agent submits.** Review it, check its sources, and sign off the commits yourself.
- **AI research is a lead, not a source.** Check every fact at the original source and write the text yourself ([sourcing and originality](docs/sourcing-and-originality.md#working-with-ai-tools)).
- **Say in the pull request description that an agent helped.**
- **Don't commit an agent's plans, task lists or scratch notes.** Put durable results in a problem doc, an ADR or a spike.

## Developer Certificate of Origin (DCO)

We don't use a contributor license agreement. Instead, every commit must be signed off under the [Developer Certificate of Origin](https://developercertificate.org/), which certifies that you wrote the contribution or otherwise have the right to submit it under this project's licenses:

```sh
git commit -s -m "Clarify P-0013 credential fields"
```

This adds a `Signed-off-by: Your Name <your-email>` line. If you want to keep your email private, use your [GitHub no-reply address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address).

## Licenses

By contributing, you agree that:

- **code** you contribute is licensed under the [Apache License 2.0](LICENSE)
- **documentation and specification text** you contribute is licensed under [CC BY 4.0](LICENSE-DOCS)

The IP policy for future specification text may add a patent commitment. That's being decided in [P-0001](problems/P-0001-neutral-governance-and-ip.md), and it won't apply retroactively without contributors' agreement.

## Pull requests

1. Keep each pull request focused on one problem or topic.
2. Run `make check`, and `make test` if you changed `tools/`, then fix any errors. CI runs the same checks.
3. Write commit messages and the pull request title following [COMMITS.md](COMMITS.md).
4. Fill in the pull request template checklist.
5. Start the description with three short lines: what changes, why, and what you need from reviewers. A summary card and a diagram help too, and `make visuals` builds them ([visual summaries](skills/visual-summaries/SKILL.md)). Agents always add them.
6. A maintainer reviews it. Doc changes need one maintainer's approval. Changes to a problem's *status*, and new decision records, follow [GOVERNANCE.md](GOVERNANCE.md).
7. Be patient and kind. Reviews happen in people's spare time.

## Code of Conduct

Everyone taking part in this project follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## Security

Please don't report security problems in public issues. See [SECURITY.md](SECURITY.md).
