1) In your case, I recommend using the «Identity Brokering» / «Identity Federation» architectural pattern:
1.1) Keycloak (`K`) delegates the authentication process to a trusted external identity provider (`IP`).
1.2) Microsoft Entra ID (`EI`) acts as the authoritative `IP`: it stores users’ credentials, verifies their authenticity (authentication), and provides user information.
1.3) `K` acts as an identity broker: an intermediary service that establishes a trust relationship with `EI`.
1.4) The end-user application (`A`) does not interact directly with `EI`.
Instead, it fully trusts `K`, which provides it with a unified interface for authentication and authorization.
2) My approach (point 1) provides the following advantages:
2.1) Centralized `IP` management.
If other identity providers are added in the future, all changes will be made centrally in `K`.
`A` will remain unchanged because it will still only interact with `K`.
`A` developers do not need to implement the logic for interacting with the various protocols and APIs of multiple `IP`’s.
They only need to integrate with a single service (`K`) using a single standardized protocol.
2.2) Token enrichment and transformation.
`K` can receive information from the external `IP` and then enrich or transform it before passing it to `A`.
E.g., it can map groups from `EI` to `K`'s internal roles.
3) In my approach, `K` performs a dual role:
3.1) From the perspective of `A`, `K` is its `IP`.
`A` contacts `K` for authentication and receives tokens from it.
3.2) From the perspective of `EI`, `K` is a client application that requests authentication. 
In protocol terminology, it acts as «Service Provider» (`SP`) or «Relying Party» (`RP`).
4) The duality of point 3 is critical for troubleshooting. 
E.g., an authentication failure can be related to either the token that `K` receives from `EI` (its role as `SP`/`RP`) or the token that it issues to the end application (its role as `IP`). 
A clear distinction between these roles precisely localizes the source of the problem.
5) `K` supports 2 main protocols for identity federation: Security Assertion Markup Language (SAML) 2.0 and OpenID Connect (`OIDC`) 1.0.
In your case, I recommend `OIDC`:
5.1) The project’s technology stack, specified by you in the tags («Java», «JavaScript», «PHP», «Amazon Web Services») is oriented toward modern web technologies and cloud services.
5.2) `OIDC` is a more modern standard, built as a simple identity layer on top of the OAuth 2.0 authorization protocol. `OIDC` uses the JSON format and JWT («JSON Web Tokens») to transmit data. 
It was designed to meet the needs of modern web applications, mobile clients, and RESTful APIs.
6) My recommended interaction flow:
6.1) The user (`U`) attempts to access a protected resource in `A`.
6.2) `A`, upon detecting the absence of an active session, redirects `U` to the `K` login page.
6.3) `K`, in turn, sees that `U` is not authenticated, and redirects `U` to the configured external `IP`: `EI`.
6.4) `U` enters their corporate credentials on the `EI` sign-in page and is successfully authenticated.
6.5) `EI` generates an «ID Token» (`T`), containing claims about `U`, including its group identifiers, and redirects `U`'s browser back to the special «Redirect URI» in `K`.
6.6) `K` receives `T` from `EI`, verifies its digital signature and validity.
6.7) `K` extracts the claims from `T`.
6.8) Based on the claims, `K` either creates a new user account for `U` in its database or updates the existing one. 
The key process takes place here: mapping of group identifiers from the «groups» claim to `K`'s internal roles.
6.9) `K` creates its session for `U`.
6.10) `K` generates its tokens (`K-TT`) for `A`:
- It's «ID Token» (not to be confused with `T`)
- «Access Token».
`K-TT` contain the roles that were assigned to `U` inside `K`.
6.11) `K` redirects the browser of `U` back to the «Redirect URI» of `A`.
6.12) `A` receives `K-TT` from `K`, validates them, and extracts from them the information about the roles of `U`.
6.13) `A` decides on granting or denying `U` access to the requested resource.
---
My GitHub profile: https://github.com/dmitrii-fediuk