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

- **Third-party copyrighted material:** game screenshots, logos, character art, ripped models or textures, music, or text copied from other sources beyond short, attributed quotes.
- **Confidential information:** anything covered by a non-disclosure agreement, including platform-holder documentation, unreleased product details or internal company material.
- **Personal data:** real players' names, emails, account IDs, or anything that identifies a real person, including in test files. Use made-up data.
- **Secrets:** API keys, tokens, passwords or private keys, even "test" ones.
- **Fan art of existing characters** as test avatars. Test assets must be original and released under CC0.

Mentioning products and companies by name to describe the problem is fine. See [TRADEMARKS.md](TRADEMARKS.md).

## Writing guidelines

- **Cite your sources.** Every factual claim should link to a source. Prefer primary sources (specifications, filings, official announcements, repositories). If you can only find secondary reporting, say "reported" or "according to".
- **Use plain language.** Write for a smart reader who isn't an expert in *your* field. Define jargon or link to the [glossary](docs/glossary.md).
- **Separate facts from opinions.** Proposals go under "candidate directions", not in the description of what exists.
- **Update "Last reviewed"** when you check a doc's facts.
- **Reference problem IDs** (`P-0013`, `P-0013-Q2`) so threads stay connected.
- **Be fair to the companies we discuss.** Describe what they've publicly said or done, not what we imagine they think.

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
2. Fill in the pull request template checklist.
3. A maintainer reviews it. Doc changes need one maintainer approval. Changes to problem *status* follow [GOVERNANCE.md](GOVERNANCE.md).
4. Be patient and kind. Reviews happen in people's spare time.

## Code of Conduct

Everyone taking part in this project follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## Security

Please don't report security problems in public issues. See [SECURITY.md](SECURITY.md).
