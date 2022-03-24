"""
Documentation helpers.
"""

from typing import Union
from itertools import chain
from pathlib import Path

from .models import Base


# Import eralchemy is installed:
try:
    from eralchemy import render_er
except ImportError:
    _has_eralchemy = False
else:
    _has_eralchemy = True


def requires_eralchemy(func):
    def wrapper(*args, **kwargs):
        if _has_eralchemy:
            return func(*args, **kwargs)
        raise ImportError(
            "eralchemy is required to do this. Install using 'pip install eralchemy'")
    return wrapper


@requires_eralchemy
def table_tags() -> dict:
    """
    List tags by table name. Used to generate the database ER diagrams.

    """
    return {tt: mm.info.get("er_tags", []) for tt, mm in Base.metadata.tables.items()}


@requires_eralchemy
def unique_tags() -> set:
    """
    Generate a list of unique table tags. Used to generate the database ER diagrams.

    """
    return set(chain(*[tt for tt in table_tags().values()]))


@requires_eralchemy
def tag_tables() -> dict:
    """
    List tables by tag. Used to generate the database ER diagrams.

    """
    return {
        tag: [table for table, tags in table_tags().items() if tag in tags]
        for tag in unique_tags()
    }


@requires_eralchemy
def save_graphs(path: Union[str, Path]):
    """
    Generate database ER diagrams. Creates one diagram with all tables and separate
    diagrams for each table tag.

    :param path: Base file for storing diagrams. The tag is appended to the base
        filename when saving the tag-specific diagrams.

    """
    if ~isinstance(path, Path):
        path = Path(path)

    render_er(Base, path.as_posix())
    for tag, tables in tag_tables().items():
        path_ = path.with_name(f"{path.stem}_{tag}{path.suffix}")
        render_er(Base, path_.as_posix(), include_tables=tables)
