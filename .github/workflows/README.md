# Blink-Tech Security Workflows

This directory documents the security workflows maintained by Blink-Tech.

## Planned workflows

- Malware and suspicious-file scanning
- Secret detection
- Dependency vulnerability auditing
- Static application security testing
- Pull-request security checks

All workflows must use least-privilege permissions and must not execute untrusted code with access to production secrets.

Security checks should report actionable findings and prevent protected-branch merges when required checks fail.
