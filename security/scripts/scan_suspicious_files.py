
#!/usr/bin/env python3
"""Basic suspicious-file scanner for Blink-Tech repositories."""

import argparse
import sys
from pathlib import Path

# These extensions deserve review in ordinary source repositories.
SUSPICIOUS_EXTENSIONS = {
    ".scr",
    ".pif",
    ".hta",
    ".vbs",
    ".vbe",
    ".wsf",
    ".wsh",
    ".ps1",
    ".bat",
    ".cmd",
    ".com",
}

# Common names of files that may contain executable startup behavior.
SUSPICIOUS_NAMES = {
    "autorun.inf",
}

# Directories that should not be scanned as project source.
IGNORED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
}


def scan_repository(root: Path) -> list[str]:
    """Return paths that deserve manual security review."""
    findings = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        if any(part in IGNORED_DIRS for part in path.parts):
            continue

        if path.suffix.lower() in SUSPICIOUS_EXTENSIONS:
            findings.append(
                f"Review suspicious extension: {path.relative_to(root)}"
            )

        if path.name.lower() in SUSPICIOUS_NAMES:
            findings.append(
                f"Review suspicious filename: {path.relative_to(root)}"
            )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report potentially suspicious repository files."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Repository directory to scan (default: current directory).",
    )
    args = parser.parse_args()

    root = Path(args.directory).resolve()

    if not root.is_dir():
        print(f"ERROR: Not a directory: {root}", file=sys.stderr)
        return 2

    findings = scan_repository(root)

    if findings:
        print("Security review findings:")
        for finding in findings:
            print(f"- {finding}")

        # These are review flags, not proof of malware.
        return 1

    print("No files matched the configured review rules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
