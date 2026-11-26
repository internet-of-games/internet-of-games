# Vision

> *One character. A persistent identity. Different games and experiences. Extraordinary freedom. An interconnected world that evolves with the player's decisions.*

This is the long-term vision behind the Internet of Games. The project's founder, [@acterra12](https://github.com/acterra12), first wrote it down, and the community now maintains it. It describes where we want to end up. It is **not** the first thing we'll build; for that, see [ROADMAP.md](ROADMAP.md).

## 1. The big idea

Why do video games exist as completely separate universes?

Imagine creating a character once and then living as that person across many games. You could start in a sprawling open-world city, pursue a professional basketball career, then ride into a frontier western, **all as the same person**. Instead of building a stranger from scratch every time you pick up a new game, you'd have one identity that follows you from experience to experience.

Science fiction has imagined this for decades, most famously with the OASIS in *Ready Player One*. But in that story, one company owns the entire world. We want the open version: an **Internet of Games**, where every game, from the biggest blockbusters to one-person projects, can join a larger persistent universe the way websites join the web, with no single owner.

## 2. What makes it different

This isn't one giant game with lots of activities. It's a world in which different games become different *places* inside one larger ecosystem:

- **Universal character.** Your identity persists across participating games.
- **Travel between worlds.** You move between experiences without starting over.
- **Freedom.** You choose radically different careers, lifestyles and activities.
- **Continuity.** Your history and choices can matter beyond any one game.
- **Shared universe.** Games stop being completely isolated.
- **No VR requirement.** It has to work on normal gaming hardware. VR is optional.

Crucially, **the games don't have to look or play alike.** A sports sim keeps its sports mechanics and an open-world adventure keeps its exploration and combat. They simply take part in a shared universe.

## 3. Be anyone, do anything

The long-term ambition goes further than hopping between today's games. It's a world with real freedom, where you might:

- become a professional athlete
- run for political office
- negotiate international agreements
- start businesses, switch careers and live through very different chapters, all within one character's lifetime

A sports career, a political career and a business venture wouldn't need to be separate games. They'd be things your character *does*, in worlds rich enough in real-world knowledge that these activities feel meaningful, and where actions have consequences that carry forward.

## 4. Why AI matters

AI could let small teams and independent creators build worlds that used to require very large studios. The bigger opportunity isn't AI-written dialogue, though. It's **worlds that respond to what players actually do**: persistent characters, changing economies, relationships, businesses and political systems, in worlds that remember.

The breakthrough would be **AI-driven worlds with meaningful freedom and persistent consequences**, not just worlds full of AI-generated conversation.

## 5. The building blocks

| Building block | What it means |
|---|---|
| **Carryfile** | A persistent player identity that many games recognize, with a shared character profile and history. |
| **Portable character and assets** | Moving the compatible parts of a character between games: appearance, cosmetics, and possibly some possessions. |
| **Connected economies** | Some way for value or purchases to work across games. This is the hardest and riskiest piece, so it comes last (see [P-0020](problems/P-0020-connected-economies.md)). |
| **Interoperability standards** | Common interfaces, so different developers can build for the same ecosystem **without** using the same engine. |
| **AI-generated and adaptive worlds** | Tools that make large, living worlds cheaper to build and maintain. |

The central design challenge is **deciding which parts of a character carry between games, and how each game interprets them.** The goal isn't to make every item or ability work everywhere. It's to preserve *identity and meaningful continuity* while every game keeps its own rules.

## 6. A platform of games versus a universe of games

Roblox and similar platforms prove that one platform can contain thousands of experiences. That isn't the same as what we're after:

| A platform with thousands of separate games | A universe of connected experiences |
|---|---|
| One company owns the identity, the store and the rules | The identity belongs to the player; games join voluntarily |
| Your character stays inside that platform | Your character travels to any game that supports the standard |
| Leaving the platform means losing everything | Leaving one game doesn't erase who you are |

## 7. The baseline for every game

This isn't meant to be a niche for small games. If it works, it should become the **baseline that every game builds on**, the way every website builds on web standards:

- **Every kind of game:** blockbusters and one-person projects; sports, RPGs, shooters, sims and social worlds; online and offline.
- **Every platform:** console, PC, mobile, web and VR.
- **Every relationship between games:** games from different companies, and games from the same company. A publisher should find the standard the easiest way to connect its own titles, too.
- **Everything players care about,** not just their character: their look, their possessions, their history, their friends and their preferences, plus links between the worlds themselves.

A standard only becomes the baseline if it's open, cheap to adopt, safe and owned by no one. Those are the rules we hold ourselves to ([design principles](docs/design-principles.md)).

## 8. How we get there

The destination is huge, so the steps are small. We won't start by building the OASIS, or by asking the biggest publishers to connect their games ([here's why that isn't happening yet](docs/why-not-yet.md)). We'll start with the smallest proof that the foundation works:

> **Two games, built by different teams, that both recognize the same player, show the same avatar, and honor one achievement earned in the other.**

Then we add layers and games, one proof at a time. A natural early showcase is a **connected sports universe**: separate baseball, basketball and football management sims, possibly from different developers, sharing athletes, careers and histories. Its focus on simulation and management rather than big-budget graphics keeps it buildable, while still showing what continuity across games feels like.

## 9. The long-term picture

Instead of buying a separate world every time we play something new, we'd each keep one ongoing digital existence. Developers would specialize: some in sports sims, others in political systems, adventure worlds, businesses or entirely new kinds of play. A common identity and an interoperable ecosystem would connect them all, and AI would make many more of these worlds possible.

Individual games would become destinations inside something much larger.
