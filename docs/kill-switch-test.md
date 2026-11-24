# The kill-switch test

*Last reviewed: 2026-11-24. A test procedure for Phase 1. It will be refined once the demo games exist.*

The sixth Phase 1 success criterion says that shutting down every server this project runs mustn't stop recognition, avatar loading or credential verification for players who already hold their files ([problem statement](problem-statement.md#what-success-looks-like-for-phase-1); [P-0024](../problems/P-0024-durability-when-services-die.md)). This page describes how to prove it, and drafts the end-of-life procedure that issuers follow so their credentials outlive them.

## What counts as a project server

Anything this project operates that a player or a game could reach: the website, any default host for player identifiers, any status-list or key mirror, any directory of games, and the issuing services of demo games when the project runs them. List every hostname from the deployed configuration before the test, so nothing is missed.

Servers run by other parties, such as a game studio's own issuer, aren't project servers. Variant B below covers them.

## Setup

- Both demo games installed on each test device: a desktop computer, a mid-range phone and a web browser.
- A test player, made up for the test, holding their player document, avatar file and one credential issued by Game A.
- Game B has run once online, so it has cached Game A's public keys and status list.

## Procedure

1. **Baseline, online.** Run the full Phase 1 flow and record each result: Game B recognizes the player, loads the avatar, verifies the Game A credential and grants the local title.
2. **Cut the project off.** Block every project hostname, for example with hosts-file entries that point nowhere, a firewall rule, or a network without internet access on phones. Keep each game's own caches.
3. **Run the flow again.** Every step from step 1 must succeed.
4. **Variant A, revoked credential.** Revoke the credential while online, let Game B refresh its cached status list, then cut the network and run again. Game B must refuse the claim.
5. **Variant B, issuer gone.** Also block Game A's own hosts. Verification must still work from cached keys, and Game B must apply its documented freshness rule to the cached status list ([P-0015](../problems/P-0015-issuer-trust-revocation.md), question P-0015-Q3).
6. **Variant C, cold cache.** Install Game B fresh, with nothing cached, and stay offline. Recognition and avatar loading must still work. Credential verification succeeds only if the issuer's keys can be checked without the network. Otherwise Game B must say so plainly and treat the claim as unverified, never as valid.

Variant C tests a design choice: an identifier whose keys are inside the identifier (such as `did:key`) passes; one that must be looked up on a server (such as `did:web`) fails unless its keys travel with the credential or were cached. The result feeds the choice of identifier method ([P-0003](../problems/P-0003-player-identifier.md)).

## Recording results

| Step | Device | Expected | Result | Notes |
|---|---|---|---|---|
| 3. Recognize the player | | Succeeds | | |
| 3. Load the avatar | | Succeeds | | |
| 3. Verify the credential and grant the title | | Succeeds | | |
| 4. Revoked credential | | Refused | | |
| 5. Issuer gone | | Succeeds, within the freshness rule | | |
| 6. Cold cache | | Recognition and avatar succeed; the credential is verified or clearly marked unverified | | |

Publish the filled-in table with the Phase 1 results, along with the game versions, the device models and the list of blocked hostnames.

## Draft: the issuer end-of-life procedure

Before an issuer, such as a game that signs achievement credentials, shuts down, it should:

1. **Announce the date** to its players, early enough for them to back up their files.
2. **Publish its final public keys,** and any identifier document or log needed to check them, somewhere that will outlast it, and let players download them.
3. **Freeze its status lists:** publish final versions and state that they will never change. Whether frozen lists keep revocations in force or credentials become valid forever is still open (P-0024-Q1).
4. **Stop issuing,** and retire its signing keys.
5. **Hand its final keys and lists to an archive,** if one exists. Who runs such an archive is open (P-0024-Q2).
6. **Mark its game manifest as retired,** so directories and other games know ([P-0027](../problems/P-0027-discovery.md)).

Whether following this procedure should be part of conformance is open too (P-0024-Q3).
