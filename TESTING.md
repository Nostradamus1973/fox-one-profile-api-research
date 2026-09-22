# Running the Fox One Login V2 Test Client

This is a sanitized interoperability test. It sends **your own** Fox One email/password to the documented Profile API endpoint and prints a sanitized response.

## Requirements

- Python 3.9+
- A valid Fox One account you are authorized to test
- The Fox One client API key supplied through the environment variable `FOX_API_KEY`

The API key is intentionally **not** stored in this repository.

## Run

Clone the repository, then run:

```bash
cd fox-one-profile-api-research
FOX_API_KEY='<your-api-key>' python3 test_client.py
```

The client prompts for the email and password using `getpass`, so the password is not echoed to the terminal.

A device ID can be entered explicitly, or the client will generate a UUID for testing.

## Request reproduced

The client sends:

- `POST https://prod-bifrost-api.foxplus.com/account/login/v2`
- `Content-Type: application/json; charset=utf-8`
- `x-api-key: <your supplied key>`
- `x-delegated-auth-flow: true`

The normal email/password payload is:

```json
{
  "email": "<email>",
  "password": "<password>",
  "deviceId": "<device-id>",
  "isTermsOfServiceAgreementNeeded": false,
  "receipts": []
}
```

## Safety

The test client does not write credentials or tokens to disk. Authentication tokens are redacted before response output.

Do not paste passwords, API keys, access tokens, refresh tokens, or other private account data into GitHub issues, chat messages, or source files.
