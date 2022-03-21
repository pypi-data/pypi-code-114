"""svg export"""

import os
from collections.abc import Iterable
from typing import Optional, Any, TypeVar, cast
import warnings

from ..model import Recipe
from .templating import fill_template, find_placeholders, FallbackValue
from .templating.exporter import TemplateExporterBase


class Exporter(TemplateExporterBase):
    name = "svg"
    ext = "svg"

    def export(self, recipes: Iterable[Recipe], out: str) -> None:
        for file_number, rendered_template in enumerate(
            fill_template_multi_slot(self.template, recipes, variables=self.variables)
        ):
            base, ext = os.path.splitext(out)
            with open(f"{base}-{file_number:02}{ext}", "w", encoding="utf-8") as f:
                f.write(rendered_template)

    def export_multifile(self, recipes: Iterable[Recipe], out_dir: str) -> None:
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir, exist_ok=True)
        for rcp in recipes:
            rendered_template = fill_template(
                self.template, env={"recipe": rcp, **self.variables}
            )
            with open(
                os.path.join(out_dir, rcp.title + "." + self.ext), "w", encoding="utf-8"
            ) as f:
                f.write(rendered_template)


def fill_template_multi_slot(
    template: str, recipes: Iterable[Recipe], variables: dict[str, Any]
) -> Iterable[str]:
    slot_numbers = scan_slot_numbers(template, root="recipes")
    if max(slot_numbers) + 1 != len(slot_numbers):
        warnings.warn(
            f"The slot numbers {','.join(str(n) for n in slot_numbers)} have gaps!"
        )
    for chunk in chunked(recipes, max(slot_numbers) + 1):
        if len(chunk) < len(slot_numbers):
            chunk += [cast(Recipe, FallbackValue[str](""))] * (
                len(slot_numbers) - len(chunk)
            )
        yield fill_template(template, env={"recipes": chunk, **variables})


T = TypeVar("T")


def chunked(items: Iterable[T], size: int) -> Iterable[list[T]]:
    items = iter(items)
    while True:
        chunk = [item for _, item in zip(range(size), items)]
        if not chunk:
            return
        yield chunk


def scan_slot_numbers(template: str, root: str) -> list[int]:
    def scan_placeholder(marker: str) -> Optional[int]:
        if not marker.startswith("["):
            return None
        try:
            return int(marker.lstrip("[").split("]")[0])
        except ValueError:
            return None

    placeholders = [
        placeholder.strip()[len(root) :]
        for placeholder in find_placeholders(template)
        if placeholder.strip().startswith(root)
    ]
    slot_numbers = (scan_placeholder(placeholder) for placeholder in placeholders)
    return sorted({n for n in slot_numbers if n is not None})
