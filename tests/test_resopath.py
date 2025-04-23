import os
from pathlib import Path
from deepath import deepath
from deepath.env import set_project_markers

def test_existing_path(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("hello")
    os.chdir(tmp_path)
    assert Path(deepath("test.txt")).resolve() == f.resolve()

def test_missing_path(tmp_path):
    os.chdir(tmp_path)
    try:
        deepath("missing.txt")
    except FileNotFoundError:
        assert True
    else:
        assert False

def test_custom_markers(tmp_path):
    marker = tmp_path / ".myroot"
    marker.write_text("")
    f = tmp_path / "config.yaml"
    f.write_text("value")
    os.chdir(tmp_path)
    set_project_markers([".myroot"])
    assert Path(deepath("config.yaml")).resolve() == f.resolve()
