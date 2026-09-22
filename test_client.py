#!/usr/bin/env python3
"""Sanitized Fox One Profile API login-v2 test client.

Requires the caller to provide their own Fox One credentials and the client
API key through FOX_API_KEY. No credentials or token values are written to
disk or printed in full.
"""

import getpass
import json
import os
import sys
import uuid
import urllib.error
import urllib.request

ENDPOINT = "https://prod-bifrost-api.foxplus.com/account/login/v2"


def main():
    api_key = os.environ.get("FOX_API_KEY")
    if not api_key:
        print("ERROR: set FOX_API_KEY in your environment.", file=sys.stderr)
        print("Example: FOX_API_KEY='<your-key>' python3 test_client.py", file=sys.stderr)
        return 2

    email = input("Fox One email: ").strip()
    if not email:
        print("ERROR: email is required.", file=sys.stderr)
        return 2

    password = getpass.getpass("Fox One password: ")
    device_id = input("Device ID [press Enter to generate UUID]: ").strip() or str(uuid.uuid4())

    payload = {
        "email": email,
        "password": password,
        "deviceId": device_id,
        "isTermsOfServiceAgreementNeeded": False,
        "receipts": [],
    }

    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "x-api-key": api_key,
            "x-delegated-auth-flow": "true",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read().decode("utf-8", errors="replace")
            status = response.status
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        status = exc.code
    except urllib.error.URLError as exc:
        print(f"NETWORK ERROR: {exc.reason}", file=sys.stderr)
        return 3

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = {"raw_response": raw[:2000]}

    # Never print live authentication material.
    if isinstance(data, dict):
        for key in (
            "accessToken",
            "refreshToken",
            "idToken",
            "token",
            "jwt",
            "authorization",
        ):
            if key in data:
                data[key] = "<redacted>"

    print(f"HTTP {status}")
    print(json.dumps(data, indent=2, sort_keys=True))
    print()
    print("No password, API key, or live token was written to disk.")

    return 0 if 200 <= status < 300 else 4


if __name__ == "__main__":
    raise SystemExit(main())
