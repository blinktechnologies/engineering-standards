
#!/usr/bin/env python3
"""Flag potentially dangerous source-code patterns for manual review."""

import argparse
import re
import sys
from pathlib import Path

IGNORED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
}

SOURCE_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx",
    ".mjs", ".cjs", ".sh", ".ps1", ".bat",
    ".cmd", ".php", ".rb", ".go", ".java",
}

# These are review indicators, not definitive malware signatures.
RULES = {
    "Dynamic code execution": re.compile(
        r"\beval\s*\(|\bexec\s*\("
    ),
    "Obfuscated PowerShell indicator": re.compile(
        r"(?i)-encodedcommand\b"
    ),
    "Suspicious download-and-execute indicator": re.compile(
        r"(?i)\b(?:downloadstring|downloadfile)\s*\("
    ),
    "Potentially unsafe shell execution": re.compile(
        r"\bos\.system\s*\(|\bshell\s*=\s*True\b"
    ),
}


def scan_file(path: Path) -> list[tuple[int, str]]:
    """Return line numbers and rule names for matching lines."""
    findings = []

    try:
        with path.open(
            "r",
            encoding="utf-8",
            errors="replace",
        ) as file:
            for line_number, line in enumerate(file, start=1):
                for rule_name, pattern in RULES.items():
                    if pattern.search(line):
                        findings.append((line_number, rule_name))
    except OSError as exc:
        print(f"WARNING: Cannot read {path}: {exc}", file=sys.stderr)

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Find source-code patterns requiring security review."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Repository directory to scan.",
    )
    args = parser.parse_args()

    root = Path(args.directory).resolve()

    if not root.is_dir():
        print(f"ERROR: Not a directory: {root}", file=sys.stderr)
        return 2

    total = 0

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        if any(part in IGNORED_DIRS for part in path.parts):
            continue

        if path.suffix.lower() not in SOURCE_EXTENSIONS:
            continue

        for line_number, rule_name in scan_file(path):
            relative_path = path.relative_to(root)
            print(
                f"REVIEW: {relative_path}:{line_number}: {rule_name}"
            )
            total += 1

    if total:
        print(f"\nFound {total} potential security review finding(s).")
        return 1

    print("No configured suspicious patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
