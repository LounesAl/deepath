from pathlib import Path
from .env import is_frozen, frozen_root, detect_project_root, executable_dir

def deepath(relative_path: str) -> str:
    """
    Resolves the absolute path for a given relative path across environments:
    - Development (project root detected via markers)
    - Frozen apps (PyInstaller onefile or onedir mode)

    Args:
        relative_path (str): A path relative to the project root or frozen base.

    Returns:
        str: An absolute path if the file exists.

    Raises:
        FileNotFoundError: If the file does not exist at the resolved location.
    """
    if is_frozen():
        # Try _MEIPASS first, then fallback to executable's directory
        base = Path(frozen_root() or executable_dir())
    else:
        base = detect_project_root()

    abs_path = base / relative_path

    if not abs_path.exists():
        raise FileNotFoundError(f"[deepath] Path not found: {abs_path}")

    return str(abs_path)
