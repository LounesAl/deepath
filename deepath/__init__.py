from .resolver import deepath

def __call__(*args, **kwargs):
    return deepath(*args, **kwargs)

__version__ = "0.1.0"
