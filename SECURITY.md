# Security Policy

This repository defines the shared security automation and standards used
across all Blink-Tech repositories.

## Reporting a vulnerability

Please use GitHub's private vulnerability reporting on the affected
repository (**Security** tab -> **Report a vulnerability**) rather than
opening a public issue. If that option is unavailable, email
allidev8@gmail.com.

## What runs on every repository

Every Blink-Tech repository calls the reusable workflow defined in
[`.github/workflows/security-scan.yml`](.github/workflows/security-scan.yml):

- **Secret scanning** - Gitleaks, scanning full commit history on every push and pull request.
- **Dependency vulnerability scanning** - OSV-Scanner across all detected lockfiles/manifests.
- **Suspicious file scan** - flags executable/script extensions (`.scr`, `.ps1`, `.hta`, `.vbs`, ...) that don't belong in ordinary source repositories.
- **Suspicious code pattern scan** - flags indicators such as dynamic code execution, encoded PowerShell, and download-and-execute patterns for manual review.

These are review signals, not proof of malware - a flagged finding should be
triaged by a human before merging.

## Known platform limitation

GitHub's Free organization plan does not support branch protection rules or
repository rulesets on **private** repositories, so these checks currently
run and report status but cannot yet technically block a direct push or a
merge. Enforcement requires either upgrading to GitHub Team (or Enterprise)
or making a repository public. See the engineering-standards README for the
current decision status.
