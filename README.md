# 📦 deepath

**deepath** is a lightweight Python library that helps you reliably resolve file paths in any environment — from development to PyInstaller-frozen applications.

No more `"file not found"` errors when your app is bundled or run from a different working directory. `deepath` makes path handling robust and environment-aware.

---

## 🔧 Why deepath?

When you're building:

- ✅ Command-line tools
- ✅ Desktop apps with PyInstaller, cx_Freeze, Nuitka, Briefcase...
- ✅ Python packages that need to load files (e.g. configs, models, images)

…resolving the *correct* path to your files becomes tricky.

**deepath** simplifies this — with one call that just works:

```python
from deepath import deepath

path = deepath("assets/icon.png")
```

---

## 💡 Features

- 📦 **Handles frozen apps** (`sys._MEIPASS` detection for PyInstaller)
- 🧪 **Dev-friendly**: detects project root via `.env`, `.git`, or `pyproject.toml`
- 🔁 **Custom root override** if needed
- 💥 **Descriptive errors** when a path doesn’t exist

---

## 🚀 Installation

```bash
pip install deepath
```

---

## 🛠️ Usage

```python
from deepath import deepath

# Resolves path relative to the project root or frozen env
icon = deepath("assets/logo.svg")
```

---

## 🧪 CLI usage

You can also use it in your terminal:

```bash
python -m deepath assets/logo.svg
```

---

## 🧩 Supported Environments

- PyInstaller
- cx_Freeze
- Nuitka
- Dev mode
- CLI
- Python packages

---

## 📚 License

MIT License © 2025 Lounes ALLIOUI
