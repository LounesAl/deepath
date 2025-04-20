import os
from pathlib import Path
from .env import is_frozen, frozen_root, detect_project_root

def get_path(relative_path: str, root: str = None) -> str:
    if is_frozen():
        base = Path(frozen_root())
    elif root:
        base = Path(root).resolve()
    else:
        base = detect_project_root()
    
    abs_path = base / relative_path
    if not abs_path.exists():
        raise FileNotFoundError(f"[resopath] Path not found: {abs_path}")
    
    return str(abs_path)
