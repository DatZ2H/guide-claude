#!/usr/bin/env python3
"""Cross-link checker: verify internal markdown links in guide/ files.

Standalone script — can be run:
  1. Manually: python3 .claude/hooks/link-check.py
  2. From /checkpoint command (integrated)
  3. As PreToolUse hook matching Bash git-commit commands (optional)

Exits 0 if all links valid, exits 1 if broken links found.
Output: list of broken links with file:line and suggested fix.
"""

import os
import re
import sys
import glob
import urllib.parse


def find_project_root():
    """Find project root by looking for VERSION file."""
    # Check environment variable first
    root = os.environ.get("CLAUDE_PROJECT_DIR", "")
    if root and os.path.isfile(os.path.join(root, "VERSION")):
        return root

    # Walk up from script location
    current = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        if os.path.isfile(os.path.join(current, "VERSION")):
            return current
        current = os.path.dirname(current)

    # Fallback: cwd
    return os.getcwd()


def extract_links(file_path):
    """Extract markdown links [text](path) from a file."""
    links = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_code_block = False
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Match [text](path) but not images ![text](url) or external URLs
        for match in re.finditer(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)", line):
            link_text = match.group(1)
            link_target = match.group(2)

            # Skip external URLs
            if link_target.startswith(("http://", "https://", "mailto:")):
                continue
            # Skip anchors-only
            if link_target.startswith("#"):
                continue

            links.append((i, link_text, link_target))

    return links


def check_link(file_path, link_target, project_root):
    """Check if a relative link target exists."""
    # Split off anchor
    path_part = link_target.split("#")[0]
    if not path_part:
        return True  # anchor-only, skip

    # URL decode
    path_part = urllib.parse.unquote(path_part)

    # Resolve relative to the file's directory
    file_dir = os.path.dirname(file_path)
    resolved = os.path.normpath(os.path.join(file_dir, path_part))

    return os.path.exists(resolved)


def main():
    project_root = find_project_root()
    guide_dir = os.path.join(project_root, "guide")

    if not os.path.isdir(guide_dir):
        print("guide/ directory not found at: " + guide_dir, file=sys.stderr)
        sys.exit(1)

    # Collect all .md files in guide/
    md_files = []
    for root, dirs, files in os.walk(guide_dir):
        for f in files:
            if f.endswith(".md") and not f.endswith(".bak"):
                md_files.append(os.path.join(root, f))

    broken_links = []

    for md_file in sorted(md_files):
        links = extract_links(md_file)
        for line_num, link_text, link_target in links:
            if not check_link(md_file, link_target, project_root):
                rel_file = os.path.relpath(md_file, project_root)
                broken_links.append({
                    "file": rel_file,
                    "line": line_num,
                    "text": link_text,
                    "target": link_target,
                })

    if broken_links:
        print(f"LINK CHECK — {len(broken_links)} broken link(s) found:\n")
        for bl in broken_links:
            print(f"  {bl['file']}:{bl['line']}")
            print(f"    [{bl['text']}]({bl['target']})")
            print(f"    -> Target not found\n")
        sys.exit(1)
    else:
        print(f"LINK CHECK — All internal links valid ({len(md_files)} files scanned)")
        sys.exit(0)


if __name__ == "__main__":
    main()
