# Fox One Profile API - Token Lifecycle

## Overview

The analysed Profile client has a clear token lifecycle:

1. A successful login request produces a `UserResponse`.
2. The success handler updates the Token Manager.
3. Subsequent authenticated requests use the stored access token.
4. The request executor invokes refresh logic when required.
5. Refresh success replaces the token set.

## Login success

The `SystemSuccessResponseHandler` processes successful Profile API responses. For login v2, the handler receives the user response and stores the token set in the Token Manager.

The analysed values include:

```
accessToken
refreshToken
tokenExpiration
idToken
```

No token values are reproduced here.

## Request execution

The `OkHttpRequestTokenManagerExecutor` uses the Token Manager to retrieve the current access token and construct:

```
Authorization: Bearer <live-access-token>
```

This mechanism means that normal authenticated Profile API requests do not hard-code a token value into the client configuration.

## Token refresh

The Token Manager is configured with:

- `refreshOnExpire = true`
- `refreshOnAuthError = true`
- `refreshExpirationBuffer = 60000 ms`

The request executor interacts with the Token Manager refresh mechanism during request execution. The refresh path can be triggered by token expiration conditions or authentication errors.

## Centralized token refresh

The centralized refresher uses the Profile API `refreshCentralizedToken` route. The observed request is a form-urlencoded POST to:

```
/identityhydra/oauth2/token
```

The form fields observed in the client are:

```
client_id
grant_type
scope
code_verifier
refresh_token
```

The response is expected to contain:

```
accessToken
refreshToken
idToken
expiresIn
```

The expiration is translated from the response expiration field into the Token Manager time state.

## Privacy and security

This repository does not include actual tokens, API keys, device IDs, user credentials, or live response data.
