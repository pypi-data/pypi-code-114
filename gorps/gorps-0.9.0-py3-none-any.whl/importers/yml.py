"""yml import"""

import os
import glob
from collections.abc import Sequence, Iterable
from typing import IO

import yaml

from ..model import Recipe

HOME = os.path.expanduser("~")
RECIPE_DIR = os.path.join(HOME, ".local", "var", "recipes")


def load(
    sources: Iterable[str] = (),
) -> Iterable[Recipe]:
    """Load recipes from specified sources (files / directories / symlinks), filtered by titles (if not None)"""
    if not sources:
        if not os.path.isdir(RECIPE_DIR):
            return []
        sources = (RECIPE_DIR,)
    files = sorted(collect_files(sources))
    return (load_recipe(f) for f in files)


def load_recipe(path: str) -> Recipe:
    """Load a single recipe"""
    with open(path, encoding="utf-8") as f:
        return load_recipe_from_stream(f)


def load_recipe_from_stream(stream: IO[str]) -> Recipe:
    return Recipe.from_dict(yaml.safe_load(stream))


def collect_files(sources: Iterable[str]) -> Sequence[str]:
    """From an iterable of files / directories / links, form a list of files either directly listed or contained (recursively) in a listed directory"""
    sources = set(sources)
    files = {src for src in sources if os.path.isfile(src)}
    directories = sources - files
    invalid_dirs = [src_dir for src_dir in directories if not os.path.isdir(src_dir)]
    if invalid_dirs:
        raise ValueError(
            f"Input paths {', '.join(invalid_dirs)} are neither files nor directories nor links to thereof."
        )
    return list(files) + sum(
        (
            glob.glob(os.path.join(src_dir, "**", "*.yml"), recursive=True)
            for src_dir in directories
        ),
        [],
    )
