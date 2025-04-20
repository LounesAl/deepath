# 📦 resopath

**resopath** is a lightweight Python library that helps you reliably resolve file paths in any environment — from development to PyInstaller-frozen applications.

No more `"file not found"` errors when your app is bundled or run from a different working directory. `resopath` makes path handling robust and environment-aware.

---

## 🔧 Why resopath?

When you're building:

- ✅ Command-line tools
- ✅ Desktop apps with PyInstaller, cx_Freeze, Nuitka, Briefcase...
- ✅ Python packages that need to load files (e.g. configs, models, images)

…resolving the *correct* path to your files becomes tricky.

**resopath** simplifies this — with one call that just works:

```python
import resopath as rp

path = rp("assets/icon.png")
```

---

## 💡 Features

- 📦 **Handles frozen apps** (`sys._MEIPASS` detection for PyInstaller)
- 🧪 **Dev-friendly**: detects project root via `.env`, `.git`, or `pyproject.toml`
- 🔁 **Custom root override** if needed
- 💥 **Descriptive errors** when a path doesn’t exist
- 🧼 Importable as `rp` and callable directly: `rp("file.png")`

---

## 🚀 Installation

```bash
pip install resopath
```

---

## 🛠️ Usage

```python
import resopath as rp

# Resolves path relative to the project root or frozen env
icon = rp("assets/logo.svg")

# Or override the root explicitly
cfg = rp("config/settings.yaml", root="src")
```

---

## 🧪 CLI usage

You can also use it in your terminal:

```bash
python -m resopath assets/logo.svg
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