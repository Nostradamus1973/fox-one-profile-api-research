# Fox One Profile API Research

Static-analysis research into the Fox One Android application's Profile API authentication and token lifecycle.

## Scope

This repository documents the client-side API architecture observed during analysis of the Fox One Android application, with particular focus on:

- Profile API routing
- `loginV2`
- email/password request construction
- authentication headers
- delegated-auth flow

The goal is to document the observed protocol structure for legitimate interoperability research.

## Safety

This repository does not contain access tokens, refresh tokens, id tokens, live API keys, user credentials, the original APK or proprietary decompiler tools. All runtime values are represented by placeholders.

## Status

Static analysis has established the client-side construction and authentication flow. Runtime credentials are intentionally not included.
