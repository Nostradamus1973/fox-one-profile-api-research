# Fox One Profile API - Registration Code Flow

## Overview

The Fox One Profile API includes a device and registration-code authentication flow alongside the normal email/password login flow.

The analysed client exposes separate endpoints for creating, polling, and completing registration-code authentication.

## V2 endpoints

The observed V2 routes include:

- `/accountregcode/v2`
- `/accountregcode/jwt/v2`
- `/accountregcode/poll/v2`
- `/accountregcode/v2/oauth2/token`

Additional legacy/non-V2 routes were also present:

- `/accountregcode`
- `/accountregcode/jwt`
- `/accountregcode/poll`
- `/accountregcode/{REG_CODE}/profile`
- `/accountregcode/{REG_CODE}`

No live registration codes or authentication tokens are included in this repository.

## Registration-code request

`AccountRegCodeRequestV2` contains fields including:

- `deviceId`
- `isRegister`
- `isMvpd`
- query parameters used by the request

The registration-code flow therefore associates the request with the client device while allowing the server to determine the applicable account or authentication state.

## Polling

The polling endpoint is:

```text
/accountregcode/poll/v2
```

The analysed client recognizes the following polling states:

- `MISSING_MVPD`
- `MISSING_BOTH`
- `DONE_NO_ACCOUNT`
- `DONE`
- `MISSING_ACCOUNT`
- `DONE_NO_MVPD`
- `DONE_CHECK_AUTHN`

Unknown or null status values are also handled by the client.

Polling is a status-discovery mechanism. It does not itself represent the final authenticated token transition.

## JWT update

The JWT completion route is:

```text
/accountregcode/jwt/v2
```

`AccountRegCodeJwtRequestV2` contains:

- `deviceId`
- `regCode`
- request headers

The corresponding DTO contains:

- `regCode`
- `deviceId`

The request is a POST and uses the delegated authentication header:

```text
x-delegated-auth-flow: true
```

## Authentication transition

The JWT update request returns a `UserResponse`.

The Profile client success handler processes that response and stores the resulting authentication token set in the Token Manager, including:

- access token
- refresh token
- token expiration
- id token

This is the important authentication transition in the registration-code flow: the registration code and device identity are exchanged through the JWT route, and the resulting user response establishes the authenticated token state used by subsequent Profile API requests.

## Security notes

This repository intentionally excludes:

- live registration codes
- access tokens
- refresh tokens
- id tokens
- API keys
- device IDs
- user credentials
- private account data

All examples use placeholders or endpoint names derived from static client analysis.
