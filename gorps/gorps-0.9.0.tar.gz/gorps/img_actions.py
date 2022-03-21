import os
import sys
from typing import Optional
import warnings

from .model import Recipe, Image
from .exporters.yml import Exporter
from .exporters.base import slugify

FORMAT_BY_EXT = {
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "webm": "image/webm",
}


def set_image(recipe: Recipe, image: str, out: str) -> None:
    with open(image, "rb") as f:
        data = f.read()
    _, ext = os.path.splitext(image)
    fmt = get_fmt(image)
    if fmt is None:
        raise RuntimeError(f"Unsupported image extension: {ext}")
    recipe.image = Image(fmt=fmt, data=data)
    Exporter().export([recipe], out=out)


def extract_image(recipe: Recipe, out: Optional[str]) -> None:
    if recipe.image is None:
        raise AttributeError("The recipe does not contain an image")
    if out is not None:
        _, ext = os.path.splitext(out)
        if not ext:
            out = os.path.join(
                out,
                slugify(recipe.title),
                next(
                    ext for ext, fmt in FORMAT_BY_EXT.items() if fmt == recipe.image.fmt
                ),
            )
        fmt = get_fmt(out)
        if fmt != recipe.image.fmt:
            warnings.warn(
                f"Extension of output file {out} does not match image format {recipe.image.fmt}"
            )
        with open(out, "wb") as f:
            f.write(recipe.image.data)
    else:
        sys.stdout.buffer.write(recipe.image.data)


def get_fmt(path: str) -> Optional[str]:
    _, ext = os.path.splitext(path)
    ext = ext.lstrip(".")
    return FORMAT_BY_EXT.get(ext.lower())
