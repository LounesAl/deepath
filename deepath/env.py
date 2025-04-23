import os
import sys
from pathlib import Path

_default_markers = [".git", "pyproject.toml", ".env"]

def set_project_markers(markers):
    """
    Set the project markers used to detect the project root.
    """
    global _default_markers
    _default_markers = markers

def _get_markers_from_env():
    """
    Get project markers from the environment variable DEEPATH_MARKERS.
    """
    val = os.getenv("DEEPATH_MARKERS", "")
    return [m.strip() for m in val.split(",") if m.strip()]

def is_frozen():
    return getattr(sys, 'frozen', False)

def frozen_root():
    """
    Returns the path to the temporary extraction folder used by PyInstaller.
    """
    return getattr(sys, '_MEIPASS', None)

def executable_dir():
    """
    Returns the directory of the frozen executable.
    """
    return Path(sys.executable).parent if hasattr(sys, 'executable') else None

def detect_project_root():
    """
    Attempts to find the project root by walking up from the current working directory
    and checking for known project markers.
    """
    current = Path.cwd()
    use_markers = _default_markers or _get_markers_from_env()
    for parent in [current] + list(current.parents):
        for marker in use_markers:
            if (parent / marker).exists():
                return parent
    return Path.cwd()

