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

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr.encoding != "utf-8":
    sys.stderr.reconfigure(encoding="utf-8")


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


def heading_to_anchor(heading_text):
    """Convert a markdown heading to its anchor ID (GitHub-style)."""
    # Remove markdown formatting
    text = re.sub(r"[*_`~]", "", heading_text)
    # Remove inline links — keep link text
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Lowercase
    text = text.lower().strip()
    # Replace spaces and consecutive hyphens
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def extract_headings(file_path):
    """Extract all heading anchors from a markdown file."""
    anchors = set()
    if not os.path.exists(file_path):
        return anchors
    with open(file_path, "r", encoding="utf-8") as f:
        in_code = False
        for line in f:
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            match = re.match(r"^#{1,6}\s+(.+)", line)
            if match:
                anchors.add(heading_to_anchor(match.group(1)))
    return anchors


# Cache for heading extraction (avoid re-reading same file)
_heading_cache = {}


def get_headings_cached(file_path):
    """Get headings with caching."""
    if file_path not in _heading_cache:
        _heading_cache[file_path] = extract_headings(file_path)
    return _heading_cache[file_path]


def check_link(file_path, link_target, project_root):
    """Check if a relative link target exists. Returns (file_ok, anchor_ok)."""
    # Split off anchor
    parts = link_target.split("#", 1)
    path_part = parts[0]
    anchor = parts[1] if len(parts) > 1 else None

    if not path_part:
        return True, True  # anchor-only within same file, skip for now

    # URL decode
    path_part = urllib.parse.unquote(path_part)

    # Resolve relative to the file's directory
    file_dir = os.path.dirname(file_path)
    resolved = os.path.normpath(os.path.join(file_dir, path_part))

    file_exists = os.path.exists(resolved)

    if not file_exists:
        return False, False

    # Check anchor if present
    if anchor:
        headings = get_headings_cached(resolved)
        anchor_decoded = urllib.parse.unquote(anchor).lower()
        # Normalize anchor for comparison
        anchor_normalized = re.sub(r"-+", "-", re.sub(r"[^\w\s-]", "", anchor_decoded).replace(" ", "-")).strip("-")
        if anchor_normalized not in headings and anchor_decoded not in headings:
            return True, False

    return True, True


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
    broken_anchors = []

    for md_file in sorted(md_files):
        links = extract_links(md_file)
        for line_num, link_text, link_target in links:
            file_ok, anchor_ok = check_link(md_file, link_target, project_root)
            rel_file = os.path.relpath(md_file, project_root)
            if not file_ok:
                broken_links.append({
                    "file": rel_file,
                    "line": line_num,
                    "text": link_text,
                    "target": link_target,
                })
            elif not anchor_ok:
                broken_anchors.append({
                    "file": rel_file,
                    "line": line_num,
                    "text": link_text,
                    "target": link_target,
                })

    has_issues = broken_links or broken_anchors

    if broken_links:
        print(f"LINK CHECK — {len(broken_links)} broken file link(s):\n")
        for bl in broken_links:
            print(f"  {bl['file']}:{bl['line']}")
            print(f"    [{bl['text']}]({bl['target']})")
            print(f"    -> File not found\n")

    if broken_anchors:
        print(f"LINK CHECK — {len(broken_anchors)} broken anchor(s):\n")
        for ba in broken_anchors:
            print(f"  {ba['file']}:{ba['line']}")
            print(f"    [{ba['text']}]({ba['target']})")
            print(f"    -> Heading anchor not found in target file\n")

    if has_issues:
        sys.exit(1)
    else:
        print(f"LINK CHECK — All internal links valid ({len(md_files)} files scanned)")
        sys.exit(0)


if __name__ == "__main__":
    main()
