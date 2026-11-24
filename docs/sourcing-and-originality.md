# Sourcing and originality

*Last reviewed: 2026-11-24. This page explains how the project uses other people's work. It isn't legal advice.*

Everything this project knows comes from other people's work: specifications, research, news, open-source projects and earlier attempts at the same problem. We depend on that work, so we handle it with care. Readers need to trust our facts, the people we learn from deserve credit, and a project that asks the whole industry to trust a neutral standard can't be careless with anyone's rights.

## The short version

1. **Use facts, not phrasing.** Facts such as dates, statuses and figures are free to use. The way someone wrote them isn't. Read the source, then write the fact in your own words and link to the source.
2. **Quote rarely and briefly.** A quotation is at most 40 words, in quotation marks, with a link to its source. `make check` rejects longer ones.
3. **Credit ideas where you use them.** If a design, an argument or a term came from someone else, name them at that point in the text, not only in a list of references.
4. **Use only what anyone can see.** Nothing confidential, leaked, paywalled, private or personal.
5. **A lead isn't a source.** A summary from an AI tool, a newsletter or a chat tells you where to look. Find the original, check the fact there and cite the original. The summary's own text never goes into the repository.

## Facts, words and ideas

Copyright protects the way something is expressed, not the facts or ideas behind it ([U.S. Copyright Office](https://www.copyright.gov/help/faq/faq-protect.html)). The WTO's TRIPS Agreement sets the same line for its member countries ([Article 9(2)](https://www.wto.org/english/docs_e/legal_e/27-trips_04_e.htm)). That gives three rules:

- **Facts:** use them, with a citation at the claim ([verifying-sources](../skills/verifying-sources/SKILL.md)).
- **Words:** don't reuse them. Rewriting an article sentence by sentence, swapping a few words each time, still copies its expression even when no sentence matches exactly. This is called close paraphrase. Work from your notes on the facts instead, and organize the text around this project's questions, not the article's structure.
- **Ideas:** copyright doesn't protect them, but taking credit for them is still wrong. When we build on someone's proposal, we say so where we use it, and we record it in [prior art](prior-art.md) or the [standards map](standards-map.md).

Names that other projects coined, for a product or for a concept in their proposal, can be used to refer to that thing. Don't adopt them as names for our own work ([OQ-1](open-questions.md#naming)).

## Quotations

- Quote when the exact words matter: a definition, a commitment, a status, or a claim you're about to examine. Don't quote to avoid writing.
- Keep each quotation to 40 words or fewer, in quotation marks, with its source linked beside it. A few short quotations from one source are fine. Quoting most of a source isn't.
- Use block quotes only for this project's own text, such as the mission.
- Say who is speaking, by role where possible, for example "the working group's chairs wrote".

## What you may reuse

| Material | Usual terms | What we do |
|---|---|---|
| News articles, blogs and company pages | All rights reserved | Use the facts, quote briefly and link |
| Specifications and standards (W3C, IETF, Khronos, OpenID Foundation, 1EdTech, ISO and others) | Each body's own license and patent policy | Link to them and describe them. Don't copy their text, schemas or figures unless a maintainer has checked the license |
| Wikipedia and other share-alike content (CC BY-SA) | Copies must carry the same license | Cite it to point readers to facts, but don't copy its text: our docs are licensed under CC BY 4.0 ([ADR-0002](decisions/ADR-0002-license-code-apache-docs-cc-by.md)) |
| Permissive content (CC BY, CC0) and permissive code (Apache-2.0, MIT, BSD) | Reuse allowed, usually with attribution and the license notice | Possible, with attribution and a maintainer's agreement in the pull request |
| Code under other licenses, such as the GPL | Conditions that conflict with Apache-2.0 | Don't copy it into this repository |
| Images, screenshots, logos, figures, charts and slides | All rights reserved, often trademarks too | Don't add them. Draw our own diagrams from the facts |
| Datasets and long tables | Can be protected as a collection | Cite the figures you need; don't copy whole tables |
| Public meeting minutes and mailing lists | Public, but they record people's words and names | Summarize, cite, quote briefly and refer to people by role |

## What we never use

- **Confidential material:** anything under a non-disclosure agreement, platform-holder documentation for licensed developers, internal company documents, private repositories and private messages.
- **Leaks.** Wait for a public statement from the organization itself, even when the press reports a leak widely.
- **Paywalled or restricted pages.** Readers must be able to check our sources. Don't get around a paywall, a login or a block on automated access. Find another public source, or ask a person to check by hand.
- **Personal data about private individuals** ([AGENTS.md](../AGENTS.md), rule 1).
- **AI-generated pages as evidence.** Some news sites publish articles written by AI. Find the primary source they summarize.
- **Material from contributors' other work,** such as their employers' projects ([AGENTS.md](../AGENTS.md), rule 2).

## Working with AI tools

AI agents and research assistants are welcome here ([CONTRIBUTING.md](../CONTRIBUTING.md#working-with-ai-agents)), and they need the same care as any other source:

- **Their research is a lead.** It can be wrong, out of date or invented, and it can repeat a source's wording closely. Check every fact at the original source and write the text fresh.
- **Their drafts are drafts.** Before you sign off, compare an agent's text with the sources it used. `make overlap` helps.
- **You're responsible for what you sign off.** Under the [Developer Certificate of Origin](https://developercertificate.org/) you certify that you have the right to submit your contribution. You can only say that about text whose origin you know.
- **Say that an agent helped** in the pull request description.

## Describing companies and people fairly

- Report what an organization said or did, with a dated source. Don't guess at motives.
- Give the other side. If a company explains a decision, include its reason.
- When we disagree with someone's approach, say why, with evidence, in a problem doc or a decision record.
- Use the names of companies and products only to describe the problem ([TRADEMARKS.md](../TRADEMARKS.md)).

## How we check

| Check | What it catches |
|---|---|
| `make check` | Quotations longer than 40 words, and possible secrets or personal data in any file |
| `make overlap SOURCE=page.html` | Runs of 8 or more words that match a saved copy of a source page. Keep the copy outside the repository |
| [checking-rights](../skills/checking-rights/SKILL.md) | The full review: copied words, credit, licenses, confidential material, personal data, trademarks and fairness |
| The pull request template | A checklist every contributor confirms |

People who use Claude Code also get a [`rights-reviewer` agent](../.claude/agents/rights-reviewer.md) that runs the full review on a branch, and a [`source-verifier` agent](../.claude/agents/source-verifier.md) that checks claims against their sources.

## If something slipped through

- **Rights holders, and people mentioned in these docs,** can ask for a correction or removal through the contacts in [MAINTAINERS.md](../MAINTAINERS.md). For anything sensitive, use the private reporting form described in [SECURITY.md](../SECURITY.md).
- **Maintainers act quickly.** They fix or remove the material and say so in the pull request. Because git keeps old versions, they can also remove it from the history when that's needed.
