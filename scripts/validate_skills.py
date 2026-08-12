#!/usr/bin/env python3
"""Lightweight structural validation for repository Agent Skills."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"
EXPECTED_SKILLS = ("long-task-polling", "risk-calibrated-validation")


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening YAML frontmatter delimiter")

    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"unreadable frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    else:
        raise ValueError("missing closing YAML frontmatter delimiter")

    return metadata


def main() -> int:
    errors: list[str] = []
    names: list[str] = []

    for directory_name in EXPECTED_SKILLS:
        skill_directory = SKILLS_ROOT / directory_name
        skill_file = skill_directory / "SKILL.md"

        if not skill_directory.is_dir():
            errors.append(f"missing Skill directory: {skill_directory.relative_to(ROOT)}")
            continue
        if not skill_file.is_file():
            errors.append(f"missing SKILL.md: {skill_file.relative_to(ROOT)}")
            continue

        try:
            metadata = read_frontmatter(skill_file)
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"{skill_file.relative_to(ROOT)}: {exc}")
            continue

        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if not name:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing name")
        if not description:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing description")
        if name and name != directory_name:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: name {name!r} does not match directory"
            )
        if name:
            names.append(name)

    if len(names) != len(set(names)):
        errors.append("Skill names must be unique")

    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts and path.stat().st_size == 0:
            errors.append(f"empty file: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print(f"PASS: validated {len(EXPECTED_SKILLS)} Skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
