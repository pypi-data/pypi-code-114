from typing import Optional, Union, Any
from collections.abc import Iterable

from ...model import Recipe
from ..base import ExporterBase


class TemplateExporterBase(ExporterBase):
    def __init__(self, template: str, variables: Optional[dict[str, Any]] = None):
        self.template = template
        if variables is None:
            self.variables = {}
        else:
            self.variables = variables

    def build_environment(self, recipes: Iterable[Recipe]) -> dict[str, Any]:
        recipes = list(recipes)
        recipe_env: dict[str, Union[Recipe, list[Recipe]]] = {"recipes": recipes}
        if len(recipes) == 1:
            recipe_env["recipe"] = recipes[0]
        return {**self.variables, **recipe_env}
