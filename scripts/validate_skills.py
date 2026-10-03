#!/usr/bin/env python3
"""Check skill metadata, local reference links, and accidental template assets."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
FRONTMATTER = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate_skill(folder: Path) -> list[str]:
    errors: list[str] = []
    entry = folder / "SKILL.md"
    if not entry.is_file():
        return [f"{folder}: missing SKILL.md"]
    text = entry.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        return [f"{entry}: missing YAML frontmatter"]
    fields: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if ":" not in line:
            errors.append(f"{entry}: malformed frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        if key in fields:
            errors.append(f"{entry}: duplicate {key}")
        fields[key] = value.strip().strip('"\'')
    if set(fields) != {"name", "description"}:
        errors.append(f"{entry}: frontmatter must contain only name and description")
    if not NAME.fullmatch(fields.get("name", "")) or fields.get("name") != folder.name:
        errors.append(f"{entry}: name must match kebab-case folder")
    if not fields.get("description"):
        errors.append(f"{entry}: empty description")
    if not text[match.end():].strip():
        errors.append(f"{entry}: empty body")
    for document in folder.rglob("*.md"):
        content = document.read_text(encoding="utf-8")
        for link in LINK.findall(content):
            target = link.split("#", 1)[0]
            if target and not re.match(r"^[a-z]+://", target) and not (document.parent / target).is_file():
                errors.append(f"{document}: broken link {link}")
    if (folder / "assets").exists():
        errors.append(f"{folder}: fixed assets/templates are outside this skill's scope")
    return errors


def main() -> int:
    folders = sorted(p for p in SKILLS.iterdir() if p.is_dir()) if SKILLS.exists() else []
    if not folders:
        print("No skills found", file=sys.stderr)
        return 1
    errors = [error for folder in folders for error in validate_skill(folder)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(folders)} skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
