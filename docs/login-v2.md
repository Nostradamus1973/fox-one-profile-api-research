# Fox One Profile API - Login V2

## Production endpoint

The application routes the Profile API login request to:

```
https://prod-bifrost-api.foxplus.com/account/login/v2
```

**Method:** `POST`

```http
Content-Type: application/json; charset=utf-8
```

## Headers

The client builds the basic Profile API headers with:

- `x-api-key: <analysis-placeholder>`
- `x-delegated-auth-flow: true`

The app's production API key value is not included in this repository.

## LoginRequestV2 fields

The analysed client model contains the following fields:

```text
email
password
userType
deviceId
facebookToken
googleToken
recaptchaToken
isTermsOfServiceAgreementNeeded
receipts
headers
```

## Regular email/password path

The actual app caller constructs `LoginRequestV2.Builder` and sets only:

```text
email
password
deviceId
```

The builder defaults the remaining request values. The boolean `isTermsOfServiceAgreementNeeded` defaults to false, and receipts are initialized as an empty list.

The resulting normal request can be represented as:

```json
{
  "email": "<email>",
  "password": "<password>",
  "deviceId": "<device-id>",
  "isTermsOfServiceAgreementNeeded": false,
  "receipts": []
}
```

The optional null fields are not expected to be emitted under normal Gson serialization of the Profile client.

## Response

Success is handled as `UserResponse`. The system success handler stores the access token, refresh token, token expiration, and id token in the Token Manager.
