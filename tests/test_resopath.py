import os
from resopath.resolver import get_path

def test_existing_path(tmp_path):
    f = tmp_path / "test.txt"
    f.write_text("hello")
    assert get_path("test.txt", root=str(tmp_path)) == str(f)

def test_missing_path(tmp_path):
    try:
        get_path("missing.txt", root=str(tmp_path))
    except FileNotFoundError:
        assert True
    else:
        assert False
