# deepath

**deepath** is a small Python utility that reliably resolves absolute paths to resource files in both development and frozen (PyInstaller) environments.

## 🚀 Why deepath?

- Handles PyInstaller's `_MEIPASS` temp dirs (onefile/onedir)
- Works with virtualenvs and CLI tools
- Auto-detects project root using markers like `pyproject.toml`, `.git`, or `.env`
- Customizable via code or environment variables

## 🧩 Usage

```python
from deepath import deepath

path = deepath("assets/image.png")
```

## 🔧 CLI

```bash
deepath assets/image.png
```

## ⚙️ Custom Project Markers

In Python:

```python
from deepath.env import set_project_markers

set_project_markers([".myroot", "setup.cfg"])
```

Or with an environment variable:

```bash
export DEEPATH_MARKERS=".myroot,.customflag"
```

## ✅ Installation

```bash
pip install deepath
```