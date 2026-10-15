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

## Enforcement status

These checks currently run and report pass/fail status on every push and
pull request, but **cannot yet block a merge or a direct push** - GitHub's
Free organization plan does not offer branch protection rules or rulesets on
private repositories. Enforcement becomes available once the org is on
GitHub Team (or Enterprise), or a given repository is made public. See
`../../SECURITY.md` for details.
