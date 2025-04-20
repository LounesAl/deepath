import sys
import os
from pathlib import Path

def is_frozen():
    return getattr(sys, 'frozen', False)

def frozen_root():
    return getattr(sys, '_MEIPASS', None)

def detect_project_root(markers=(".git", "pyproject.toml", ".env")):
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        for marker in markers:
            if (parent / marker).exists():
                return parent
    return Path.cwd()  # fallback
