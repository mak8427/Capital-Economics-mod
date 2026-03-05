#!/usr/bin/env python3
"""Pre-commit BOM check for common/*.txt and localization/*.yml files.

Rules:
- Any staged `.txt` file under a `common/` path must start with UTF-8 BOM.
- Any staged `.yml` file under a `localization/` path must start with UTF-8 BOM.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


UTF8_BOM = b"\xef\xbb\xbf"


def git_root() -> Path:
    out = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True)
    return Path(out.strip())


def staged_files(repo_root: Path) -> list[Path]:
    cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"]
    out = subprocess.check_output(cmd)
    if not out:
        return []
    parts = [p for p in out.decode("utf-8", errors="replace").split("\x00") if p]
    return [repo_root / p for p in parts]


def is_target(path: Path) -> bool:
    path_s = "/" + path.as_posix().lower() + "/"
    ext = path.suffix.lower()
    if ext == ".txt" and "/common/" in path_s:
        return True
    if ext == ".yml" and "/localization/" in path_s:
        return True
    return False


def has_bom(path: Path) -> bool:
    try:
        with path.open("rb") as handle:
            return handle.read(3) == UTF8_BOM
    except OSError:
        return False


def main() -> int:
    root = git_root()
    files = staged_files(root)

    targets = [p for p in files if p.is_file() and is_target(p)]
    missing = [p for p in targets if not has_bom(p)]

    if not missing:
        return 0

    print("BOM check failed. These staged files must start with UTF-8 BOM:")
    for p in missing:
        print(f" - {p.relative_to(root).as_posix()}")
    print("\nFix: re-save these files as UTF-8 with BOM, then re-stage.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
