---
id: ADR-0010
title: Call the portable player document a Carryfile
status: accepted
date: 2026-11-26
problems: ["*"]
topics: [naming, trademarks]
supersedes: []
superseded_by: null
---

# ADR-0010: Call the portable player document a Carryfile

## Context

The small document at the center of this project has gone by the working name "player passport". [OQ-1](../open-questions.md#naming) explains why that can't be its real name: "PLAYER PASSPORT" is another company's registered U.S. trademark, and "Passport" is already a web3 gaming identity product. The name will appear in every schema, package, app and conversation, so it should be settled before Phase 1 drafts its first profile ([ROADMAP.md](../../ROADMAP.md)).

OQ-1 asks for a name that's distinctive, describes the document, isn't already used in games or identity, and doesn't come from a fictional universe. Two earlier decisions rule out more words. We never require wallets or tokens ([ADR-0005](ADR-0005-never-require-blockchains-tokens-or-wallets.md)), and the document carries signed claims, not saved game state ([ADR-0008](ADR-0008-continuity-as-signed-claims-not-state.md)), so "wallet", "token", "save" and "progress" would all mislead.

This decision aims to give the document a name that players understand at first sight and that nobody in games or identity already uses.

## Options

We checked these names on 26 November 2026:

| Name | What it suggests | What we found |
|---|---|---|
| **Carryfile** | The file you carry from game to game | We found no game, app, package or identity product that uses it today. The U.S. filings for "Carryfile" and "Carry File" were both for paper folders, and both were cancelled in 2016 ([USPTO](https://tsdr.uspto.gov/statusview/sn74037914), [USPTO](https://tsdr.uspto.gov/statusview/sn76552371)) |
| Playfile | A file about how you play | A sports app already uses it for player identity, under the line "One Player. One Identity." ([site](https://playfile-115d6.web.app/)) |
| Wayfile | A file for the way between worlds | Several file managers use it, for example on [Linux](https://github.com/blackbartblues/Wayfile) |
| Roamfile | A file that roams with you | Said aloud, it sounds like "ROM file", a common term for a copy of a game cartridge's data ([ROM image](https://en.wikipedia.org/wiki/ROM_image)) |
| Playfolio | A portfolio of your games | A game-tracking app already uses it ([App Store](https://apps.apple.com/us/app/playfolio-game-tracker/id6762097810)) |
| Playprint | The mark you leave on play | It sounds like "fingerprint", which in privacy means tracking ([T3](../threat-model.md#t3-tracking-and-profiling)), and a family app uses it ([App Store](https://apps.apple.com/us/app/playprint-calm-adhd-families/id6783227343)) |
| Player document | Exactly what it is | Clear, but it's a description rather than a name, and it's hard to search for |

For each name we searched GitHub, Steam, Apple's App Store, Google Play, itch.io, npm, PyPI, the .com, .org and .dev domain registries, U.S. trademark records and the web. The nearest uses of Carryfile's parts are a document-vault app called "Carry" ([App Store](https://apps.apple.com/us/app/carry-a-vault/id6475613113)), a tax and investment service registered as CARRY ([USPTO](https://tsdr.uspto.gov/statusview/sn98553645)), and "carry file", a stationery term for a folder with a handle. None of them is a game or a player identity. Web searches turned up no "Carryfile" filing in the EU, UK or WIPO trademark registers, but their search tools block automated queries, so we couldn't search them directly. A search like this isn't a trademark clearance.

## Decision

We will call the portable player document a **Carryfile**: "Carryfiles" in the plural, and `carryfile` in code, schemas and file names.

- Use Carryfile wherever we mean our own document, in specifications, schemas, packages, apps and conversation. Software that keeps a player's Carryfile is a "Carryfile app".
- Keep "passport" only where it's someone else's name, such as Immutable Passport or the PLAYER PASSPORT trademark, and in dated records: spikes and accepted ADRs keep their original wording.
- Carryfile is the name of an open format, not a registered trademark ([TRADEMARKS.md](../../TRADEMARKS.md)). If the project ever wants to register it, a trademark lawyer should clear it first.

## Consequences

- One short, plain word replaces "player passport (working name)", and it says what players do with the document: carry it from game to game.
- "Carry file" is also a stationery term, so web searches for it return folders. Pairing it with "Internet of Games" fixes that.
- Living documents switch to Carryfile, and the glossary keeps "player passport" as a pointer for readers of older records.
- Whether the name should ever be registered, and by whom, belongs with [OQ-2](../open-questions.md#naming) and [P-0001](../../problems/P-0001-neutral-governance-and-ip.md).

## Universality and safety

- **Every game:** the name doesn't point to any genre, platform, rating or business model, and both of its parts are common English words that are easy to say and translate ([P-0030](../../problems/P-0030-built-for-every-game.md)).
- **Threats:** a distinctive name makes copycat "official" apps easier to spot ([T2](../threat-model.md#t2-account-takeover-and-impersonation)), and it avoids a word that suggests tracking ([T3](../threat-model.md#t3-tracking-and-profiling)).
