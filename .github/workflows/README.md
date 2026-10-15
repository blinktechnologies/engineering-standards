# Blink-Tech Security Workflows

`security-scan.yml` is a reusable workflow (`on: workflow_call`) implementing
Blink-Tech's standard security checks:

- Secret detection (Gitleaks)
- Dependency vulnerability auditing (OSV-Scanner)
- Suspicious-file scanning
- Suspicious source-pattern scanning

`ci.yml` calls it locally for this repository. Other Blink-Tech repositories
call it remotely:

```yaml
jobs:
  security-scan:
    uses: blinktechnologies/engineering-standards/.github/workflows/security-scan.yml@main
    secrets: inherit
```

All actions referenced are pinned to a commit SHA, not a mutable version tag.

`codeql.yml` and `scorecard.yml` run CodeQL and the OpenSSF Scorecard. Both
require a public repository on GitHub's Free plan, which this repo now is.

## Enforcement status

This repository's `main` branch is protected: PR required, CODEOWNERS
review required, all four security-scan checks required, no force-pushes,
no deletions, linear history, enforced for admins too.

Private repositories in this org (e.g. `blinktech-website`) don't get this
enforcement on GitHub's Free plan - branch protection and rulesets are
Pro/Team-only there. They still get the scans in this workflow as a
report-only signal. See `../../SECURITY.md` for details.
