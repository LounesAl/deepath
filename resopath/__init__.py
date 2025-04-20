from .resolver import get_path

def __call__(*args, **kwargs):
    return get_path(*args, **kwargs)

__version__ = "0.1.0"
