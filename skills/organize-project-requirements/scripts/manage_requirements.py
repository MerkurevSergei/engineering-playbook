#!/usr/bin/env python3
"""Safely initialize a requirements package or add a capability module."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = SKILL_DIR / "assets" / "requirements-template"
CAPABILITY_TEMPLATE = SKILL_DIR / "assets" / "capability-template.md"


def relative_directory(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise argparse.ArgumentTypeError("directory must be a non-empty relative path without '..'")
    return path


def slugify(value: str) -> str:
    slug = "".join(character if character.isalnum() else "-" for character in value.casefold())
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "capability"


def baseline_id(project_name: str) -> str:
    value = "".join(character if character.isalnum() else "-" for character in project_name.upper())
    value = re.sub(r"-+", "-", value).strip("-")
    return f"BRS-{value or 'PROJECT'}"


def render(text: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def ensure_within(root: Path, target: Path) -> None:
    root = root.resolve()
    target = target.resolve()
    if target != root and root not in target.parents:
        raise ValueError(f"target escapes project root: {target}")


def template_files() -> list[Path]:
    if not TEMPLATE_DIR.is_dir():
        raise FileNotFoundError(f"requirements template not found: {TEMPLATE_DIR}")
    return sorted(path for path in TEMPLATE_DIR.rglob("*") if path.is_file())


def init_package(args: argparse.Namespace) -> int:
    project_root = args.project_root.resolve()
    if not project_root.is_dir():
        print(f"Project root does not exist or is not a directory: {project_root}", file=sys.stderr)
        return 2
    target = project_root / args.directory
    ensure_within(project_root, target)

    project_name = args.project_name or project_root.name
    values = {
        "PROJECT_NAME": project_name,
        "BASELINE_ID": args.baseline_id or baseline_id(project_name),
        "CREATED_DATE": date.today().isoformat(),
    }

    files = template_files()
    existing = target.exists() and any(target.iterdir())
    if existing and not args.merge:
        print(f"Refusing to modify non-empty directory without --merge: {target}", file=sys.stderr)
        return 2

    created = 0
    skipped = 0
    for source in files:
        destination = target / source.relative_to(TEMPLATE_DIR)
        if destination.exists():
            print(f"SKIP   {destination}")
            skipped += 1
            continue
        print(f"CREATE {destination}")
        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(render(source.read_text(encoding="utf-8"), values), encoding="utf-8")
        created += 1

    action = "Would create" if args.dry_run else "Created"
    print(f"{action} {created} file(s); skipped {skipped} existing file(s).")
    return 0


def next_capability_id(capabilities_dir: Path) -> str:
    numbers: list[int] = []
    if capabilities_dir.exists():
        for path in capabilities_dir.iterdir():
            match = re.match(r"CAP-(\d{3,})-", path.name)
            if match:
                numbers.append(int(match.group(1)))
    return f"CAP-{max(numbers, default=0) + 1:03d}"


def add_capability(args: argparse.Namespace) -> int:
    project_root = args.project_root.resolve()
    if not project_root.is_dir():
        print(f"Project root does not exist or is not a directory: {project_root}", file=sys.stderr)
        return 2
    requirements_dir = project_root / args.directory
    capabilities_dir = requirements_dir / "capabilities"
    ensure_within(project_root, capabilities_dir)

    if not (requirements_dir / "README.md").is_file():
        print(f"Requirements package not found: {requirements_dir}", file=sys.stderr)
        return 2
    if not CAPABILITY_TEMPLATE.is_file():
        print(f"Capability template not found: {CAPABILITY_TEMPLATE}", file=sys.stderr)
        return 2

    capability_id = args.capability_id or next_capability_id(capabilities_dir)
    if not re.fullmatch(r"CAP-\d{3,}", capability_id):
        print("Capability ID must match CAP-###", file=sys.stderr)
        return 2

    duplicate_ids = sorted(capabilities_dir.glob(f"{capability_id}-*"))
    if duplicate_ids:
        print(f"Capability ID already exists: {duplicate_ids[0]}", file=sys.stderr)
        return 2

    target = capabilities_dir / f"{capability_id}-{slugify(args.name)}" / "README.md"
    ensure_within(project_root, target)
    if target.exists():
        print(f"Refusing to overwrite existing capability: {target}", file=sys.stderr)
        return 2

    values = {
        "CAPABILITY_ID": capability_id,
        "CAPABILITY_NAME": args.name,
        "CAPABILITY_OUTCOME": args.outcome or "TBD — create a research question and assign an owner.",
        "CREATED_DATE": date.today().isoformat(),
    }
    print(f"CREATE {target}")
    if not args.dry_run:
        target.parent.mkdir(parents=True, exist_ok=False)
        target.write_text(render(CAPABILITY_TEMPLATE.read_text(encoding="utf-8"), values), encoding="utf-8")
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    subparsers = result.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="create a requirements package")
    init.add_argument("--project-root", type=Path, default=Path.cwd())
    init.add_argument("--directory", type=relative_directory, default=Path("requirements"))
    init.add_argument("--project-name")
    init.add_argument("--baseline-id")
    init.add_argument("--merge", action="store_true", help="create missing files without overwriting existing ones")
    init.add_argument("--dry-run", action="store_true")
    init.set_defaults(run=init_package)

    capability = subparsers.add_parser("add-capability", help="create one capability module")
    capability.add_argument("--project-root", type=Path, default=Path.cwd())
    capability.add_argument("--directory", type=relative_directory, default=Path("requirements"))
    capability.add_argument("--name", required=True)
    capability.add_argument("--outcome")
    capability.add_argument("--capability-id")
    capability.add_argument("--dry-run", action="store_true")
    capability.set_defaults(run=add_capability)
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        return args.run(args)
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
