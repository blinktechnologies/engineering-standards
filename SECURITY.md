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

## Enforcement status

This repository is public, which unlocks real enforcement on GitHub's Free
plan: branch protection on `main` requires a pull request, CODEOWNERS
review, all four checks above passing, no force-pushes, no branch/tag
deletion, and linear history - enforced for admins too. CodeQL (Python) and
the OpenSSF Scorecard also run here, both of which require a public repo on
the Free plan.

`blinktech-website` and any other **private** repository in this org does
not get this enforcement on GitHub's Free plan - branch protection and
rulesets return "Upgrade to GitHub Pro" there. Those repos still get the
scans in this workflow (report-only), plus Dependabot alerts and private
vulnerability reporting, which are free regardless of visibility or plan.
Real enforcement on private repos requires upgrading the org to GitHub
Team (or Enterprise).
