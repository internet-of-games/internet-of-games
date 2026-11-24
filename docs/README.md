# Docs: reading guide

Suggested order for newcomers:

1. [Vision](../VISION.md): where we want to end up.
2. [Why doesn't NBA 2K plug into GTA VI?](why-not-yet.md): the real barriers, and why the obvious approach won't work.
3. [Problem statement](problem-statement.md): the precise problem, its scope and the success criteria.
4. [Landscape, late 2026](landscape-2026.md): who's doing what right now.
5. [Prior art](prior-art.md): what's been tried before, and what each attempt teaches us.
6. [Standards map](standards-map.md): existing standards to build on, layer by layer.
7. [Working with upstream groups](upstream.md): how to take part in each group whose standards we build on, and on what terms.
8. [Layer model](layer-model.md): how the pieces fit together.
9. [What should travel between games](portability-matrix.md): what carries over, and what deliberately doesn't.
10. [Design principles](design-principles.md): rules learned from earlier failures.
11. [Universality requirements](universality-requirements.md): what every design must allow, so that no kind of game is left out.
12. [Threat model](threat-model.md): what we protect, in priority order, and the threats every proposal must address.
13. [The kill-switch test](kill-switch-test.md): how we'll prove the standard keeps working after our own servers are gone.
14. [The business case](business-case.md): why a game would join.
15. [How interoperability happened elsewhere](interop-history.md): the web, email, phone numbers, banking and cross-play.
16. [Legal and policy landscape](legal-and-policy.md): rights, ratings, privacy and regulation. This isn't legal advice.
17. [Sourcing and originality](sourcing-and-originality.md): how we use other people's work, from facts and quotations to credit and licenses.
18. [Open questions](open-questions.md): cross-cutting questions that don't belong to any one problem.
19. [Glossary](glossary.md) and [References](references.md).

After that, pick a problem from [problems/README.md](../problems/README.md).

**Decisions** are recorded in [decisions/](decisions/README.md), and **investigations** in [spikes/](spikes/README.md). If you're working with an AI agent, start it at [AGENTS.md](../AGENTS.md).

## How we handle facts

- **Every factual claim should link to a source.** We prefer primary sources (filings, specifications, official announcements and repositories) over secondary reporting.
- **Where only secondary reporting exists, the text says so**, using words like "reported" or "according to".
- **Every doc carries a "Last reviewed" date.** Numbers, star counts and standards statuses go stale. Corrections are always welcome; open an issue using the *Evidence / correction* template.
- **Repository facts** (stars, last push, archived status) were read from the GitHub API on the review date.
- **We write in our own words.** We quote briefly, with links, and credit the ideas we build on ([sourcing and originality](sourcing-and-originality.md)).
- **Nothing here is legal advice.**
