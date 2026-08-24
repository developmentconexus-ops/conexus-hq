#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def exact_path_exists(root: Path, relative: str) -> bool:
    """Return True only when every path component exists with exact casing."""
    current = root
    for part in Path(relative).parts:
        if not current.is_dir():
            return False
        entries = {entry.name: entry for entry in current.iterdir()}
        if part not in entries:
            return False
        current = entries[part]
    return current.exists()


REQUIRED = [
    "README.md",
    "AGENTS.md",
    "docs/index.md",
    "docs/roadmap.md",
    "docs/decisions/index.md",
    "docs/portfolio/map.md",
    "docs/development/repository-rules.md",
    "docs/phases/hq-0-repository-foundation.md",
]

for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        errors.append(f"missing required file: {relative}")

bootstrap_paths = [ROOT / "AGENTS.md", ROOT / "docs/index.md", ROOT / "docs/roadmap.md"]
if all(path.is_file() for path in bootstrap_paths):
    bootstrap_size = sum(path.stat().st_size for path in bootstrap_paths)
    if bootstrap_size > 20 * 1024:
        errors.append(f"bootstrap budget exceeded: {bootstrap_size} bytes > 20480 bytes")

status_marker = "<!-- current-status-authority -->"
status_owners: list[str] = []
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"markdown is not UTF-8: {path.relative_to(ROOT)}")
        continue
    if status_marker in text:
        status_owners.append(path.relative_to(ROOT).as_posix())

if status_owners != ["docs/roadmap.md"]:
    errors.append(f"mutable status marker must exist only in docs/roadmap.md; found {status_owners}")

forbidden_exact = [
    "docs/INDEX.md",
    "docs/NOW.md",
    "docs/operations/roadmap.md",
    "CLAUDE.md",
]
for relative in forbidden_exact:
    if exact_path_exists(ROOT, relative):
        errors.append(f"forbidden legacy surface present: {relative}")

for prefix in ["docs/superpowers", "docs/work"]:
    if (ROOT / prefix).exists():
        errors.append(f"temporary/noncanonical surface present in candidate: {prefix}")

allowed_top_level = {".github", "docs", "scripts", "AGENTS.md", "README.md"}
for path in ROOT.iterdir():
    if path.name == ".git":
        continue
    if path.name not in allowed_top_level:
        errors.append(f"unexpected top-level surface: {path.name}")

markdown_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    for raw_target in markdown_link.findall(text):
        target = raw_target.strip().split()[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"link escapes repository: {path.relative_to(ROOT)} -> {raw_target}")
            continue
        if not resolved.exists():
            errors.append(f"broken relative link: {path.relative_to(ROOT)} -> {raw_target}")

if errors:
    print("repository verification FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("repository verification PASSED")
print("- required bootstrap present")
print("- bootstrap budget <= 20 KiB")
print("- sole mutable status marker = docs/roadmap.md")
print("- forbidden legacy/temporary surfaces absent")
print("- top-level surface bounded")
print("- relative Markdown links resolve")
