"""Export to yml (main format)"""

import os
from dataclasses import asdict
from collections import OrderedDict
from fractions import Fraction
from typing import Any, IO
import yaml

from ..model import Recipe
from .base import TextExporterBaseAtomic

home = os.path.expanduser("~")
recipe_dir = os.path.join(home, ".local", "var", "recipes")


def _represent_dictorder(self: yaml.Dumper, data: dict[str, Any]) -> yaml.MappingNode:
    return self.represent_mapping(
        "tag:yaml.org,2002:map",
        filter(lambda t: t[1] is not None and t != ("optional", False), data.items()),
    )


yaml.add_representer(OrderedDict, _represent_dictorder)


class Exporter(TextExporterBaseAtomic):
    name = "yml"
    ext = "yml"

    @staticmethod
    def export_stream(recipe: Recipe, stream: IO[str]) -> None:
        serialized = asdict(recipe, dict_factory=OrderedDict)  # type: ignore

        def represent_fraction(dumper: yaml.Dumper, data: Fraction) -> yaml.ScalarNode:
            if data.denominator == 1:
                return dumper.represent_scalar(
                    "tag:yaml.org,2002:int", str(data.numerator)
                )
            return dumper.represent_scalar("tag:yaml.org,2002:str", str(data))

        yaml.add_representer(
            Fraction,
            represent_fraction,
        )
        yaml.dump(
            serialized,
            stream,
            encoding="utf-8",
            allow_unicode=True,
        )
