#!/usr/bin/env python3
"""Check that root release artifacts mirror src/ontology release artifacts."""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_ARTIFACTS = (
    "automatce.owl",
    "automatce.ttl",
    "automatce.json",
    "automatce-base.owl",
    "automatce-base.ttl",
    "automatce-base.json",
    "automatce-full.owl",
    "automatce-full.ttl",
    "automatce-full.json",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", type=Path)
    parser.add_argument("--ontology-dir", default="src/ontology", type=Path)
    parser.add_argument("--min-main-ttl-bytes", default=100_000, type=int)
    args = parser.parse_args()

    errors: list[str] = []
    root = args.root
    ontology_dir = args.ontology_dir

    for name in DEFAULT_ARTIFACTS:
        root_path = root / name
        source_path = ontology_dir / name

        if not root_path.exists():
            errors.append(f"{root_path}: missing root release artifact")
            continue
        if not source_path.exists():
            errors.append(f"{source_path}: missing source release artifact")
            continue

        root_bytes = root_path.read_bytes()
        source_bytes = source_path.read_bytes()
        if root_bytes != source_bytes:
            errors.append(f"{root_path}: does not match {source_path}")

    main_ttl = root / "automatce.ttl"
    if main_ttl.exists() and main_ttl.stat().st_size < args.min_main_ttl_bytes:
        errors.append(
            f"{main_ttl}: size is {main_ttl.stat().st_size} bytes; expected a built release artifact"
        )

    if errors:
        raise SystemExit("\n".join(errors))

    print("Root release artifacts match src/ontology release artifacts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
