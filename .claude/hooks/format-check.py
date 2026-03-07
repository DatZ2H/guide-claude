#!/usr/bin/env python3
"""PostToolUse hook: validate heading hierarchy and code block tags in guide/ files.

Fires after Edit or Write on guide/**/*.md files.
Reads tool_input from stdin JSON, checks the edited file for format issues.
Outputs JSON with additionalContext if issues found — Claude sees the warning and can self-correct.
"""

import sys
import json
import re
import os


def check_format(file_path):
    """Check heading hierarchy and code block language tags."""
    issues = []

    if not os.path.exists(file_path):
        return issues

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # --- Check 1: Heading hierarchy (no skipped levels) ---
    prev_level = 0
    for i, line in enumerate(lines, 1):
        match = re.match(r"^(#{1,6})\s", line)
        if match:
            level = len(match.group(1))
            if prev_level > 0 and level > prev_level + 1:
                issues.append(
                    f"Line {i}: Heading skip — h{prev_level} -> h{level} "
                    f"(expected <= h{prev_level + 1})"
                )
            prev_level = level

    # --- Check 2: Code blocks must have language tags ---
    in_code_block = False
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_code_block:
                # Opening fence — check for language tag
                lang = stripped[3:].strip()
                if not lang:
                    issues.append(f"Line {i}: Code block missing language tag")
                in_code_block = True
            else:
                # Closing fence
                in_code_block = False

    # --- Check 3: Source markers presence ---
    # At least one source marker expected in guide/ content files (not overview/index)
    basename = os.path.basename(file_path).lower()
    is_content_file = not basename.startswith("00-")  # skip overview/index files
    if is_content_file:
        has_source = False
        source_patterns = [
            re.compile(r"\[Nguồn:"),
            re.compile(r"\[Ứng dụng Kỹ thuật\]"),
            re.compile(r"\[Cập nhật\s+\d{2}/\d{4}\]"),
        ]
        for line in lines:
            for pat in source_patterns:
                if pat.search(line):
                    has_source = True
                    break
            if has_source:
                break
        if not has_source:
            issues.append(
                "No source markers found — expected at least one "
                "[Nguồn: ...], [Ứng dụng Kỹ thuật], or [Cập nhật MM/YYYY]"
            )

    # --- Check 4: Banned emoji in prose ---
    banned = [
        "\U0001f4a1", "\U0001f680", "\U0001f60a", "\U0001f3af", "\u2728",
        "\U0001f4cc", "\U0001f525", "\U0001f449", "\U0001f4dd", "\U0001f4aa",
        "\U0001f914", "\u2b50", "\U0001f3d7\ufe0f", "\U0001f4ca", "\U0001f6e0\ufe0f",
    ]
    for i, line in enumerate(lines, 1):
        for emoji in banned:
            if emoji in line:
                issues.append(f"Line {i}: Banned emoji found — remove or replace with callout syntax")
                break  # one warning per line is enough

    return issues


def main():
    # Read hook input from stdin
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if not file_path:
        sys.exit(0)

    # Normalize path separators
    normalized = file_path.replace("\\", "/")

    # Only check guide/**/*.md files
    if "/guide/" not in normalized and not normalized.startswith("guide/"):
        sys.exit(0)
    if not normalized.endswith(".md"):
        sys.exit(0)
    # Skip .bak files
    if normalized.endswith(".bak"):
        sys.exit(0)

    issues = check_format(file_path)

    if issues:
        warning = "FORMAT CHECK — issues found in {}:\n{}".format(
            os.path.basename(file_path),
            "\n".join(f"  - {issue}" for issue in issues),
        )
        result = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": warning,
            }
        }
        json.dump(result, sys.stdout)

    sys.exit(0)


if __name__ == "__main__":
    main()
