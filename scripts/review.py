#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path

from openai import OpenAI


ROOT = Path(__file__).resolve().parent.parent

AGENTS_FILE = ROOT / "AGENTS.md"
REVIEWER_FILE = ROOT / ".opencode" / "agents" / "reviewer.md"


def load_file(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def get_git_diff() -> str:
    result = subprocess.run(
        ["git", "diff", "origin/main...HEAD"],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout


def build_prompt(global_rules: str,
                 reviewer_rules: str,
                 git_diff: str) -> str:

    return f"""
# CONTEXTE GLOBAL

{global_rules}

# ROLE

{reviewer_rules}

# DIFF GIT

```diff
{git_diff}