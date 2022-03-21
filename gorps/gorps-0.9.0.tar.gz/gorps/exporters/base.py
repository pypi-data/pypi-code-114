import os
from abc import ABC
from collections.abc import Iterable
from typing import IO

from ..model import Recipe


class ExporterBase:
    """Exporter Interface"""

    name: str
    ext: str

    def export(self, recipes: Iterable[Recipe], out: str) -> None:
        raise RuntimeError(
            f"Eporting to a single file is not supported by {type(self).__name__}"
        )

    def export_multifile(self, recipes: Iterable[Recipe], out_dir: str) -> None:
        raise RuntimeError(
            f"Eporting to multiple files is not supported by {type(self).__name__}"
        )


class TextExporterBase(ExporterBase):
    """Text exporter specialization"""

    @classmethod
    def export(cls, recipes: Iterable[Recipe], out: str) -> None:
        with open(out, "w", encoding="utf-8") as f:
            for recipe in recipes:
                cls.export_stream(recipe, f)

    @classmethod
    def export_multifile(cls, recipes: Iterable[Recipe], out_dir: str) -> None:
        for rcp in recipes:
            cls.export([rcp], os.path.join(out_dir, slugify(rcp.title) + "." + cls.ext))

    @classmethod
    def export_stream(cls, recipe: Recipe, stream: IO[str]) -> None:
        raise NotImplementedError("Not implemented")


class TextExporterBaseAtomic(TextExporterBase, ABC):
    """Only one recipe per file allowed"""

    @classmethod
    def export(cls, recipes: Iterable[Recipe], out: str) -> None:
        recipes = list(recipes)
        if len(recipes) > 1:
            raise RuntimeError(
                f"Eporting multiple recipes to a single file is not supported by {cls.__name__}"
            )
        super().export(recipes, out)


def slugify(name: str) -> str:
    return name.lower().replace(" ", "-")
