import gzip
import pickle

__all__ = ["save", "load"]

from typing import Any


def save(obj: Any, filename: str, zip: bool = True) -> None:
    """Save object to file.

    Args:
        obj: object to save.
        filename: file name where to save the object.
        zip: whether to compress file into zip.
    """
    if zip:
        with gzip.open(filename, "wb") as zf:
            pickle.dump(obj, zf)
    else:
        with open(filename, "wb") as f:
            pickle.dump(obj, f)


def load(filename: str, zip: bool = True) -> Any:
    """Load object from file.

    Args:
        filename: file name where to load the object from.
        zip: whether the file is compressed into zip.

    Returns:
        loaded object.
    """
    if zip:
        with gzip.open(filename, "rb") as zf:
            return pickle.load(zf)
    else:
        with open(filename, "rb") as f:
            return pickle.load(f)
