# Fox One Profile API - Authentication

## Overview

The Fox One Profile client uses three authentication-related elements:

- a client-provided `x-api-key`
- a live `x-delegated-auth-flow` header when the flow requires it
- an authenticated `Authorization: Bearer <live-access-token>` header for normal authenticated requests.

No runtime values are published here.

## Profile API base configuration

The production Profile API base URL observed in the application code is:

```
https://prod-bifrost-api.foxplus.com/
```

The app provides the Profile client with configuration values including the API key and base URL. The live API key value is not included in this repository.

## BaseClient headers

The analysed `BaseApiClient.getHeaders()` method adds the basic client headers, including:

```text
x-api-key: <analysis-placeholder>
```

For certain delegated authentication routes, the client adds:

```http
x-delegated-auth-flow: true
```

## Bearer authentication

Regular authenticated requests use:

```text
Authorization: Bearer <live-access-token>
```

The analysed `OkHttpRequestTokenManagerExecutor` reads the access token from the Token Manager and prepends `Bearer ` to it before setting the Authorization header.

## Token Manager

The Profile client is connected to a singleton Token Manager state. The analysis shows the following defaults:

```text
refreshOnExpire = true
refreshOnAuthError = true
refreshExpirationBuffer = 60000 ms
preferences prefix = foxkit_tokens_v1_
```

The Token Manager stores the authentication token set and provides the access token to the request executor.

## Refresh behavior

The analysis shows that the request executor also invokes the Token Manager refresh mechanism during request execution. This can be activated when token expiration is approaching or when the app's authentication error path triggers refresh logic.

## Live values

This repository deliberately does not include:

- actual API keys
- access tokens
- refresh tokens
- id tokens
- device IDs or user credentials
