"""Random values workflow plugin module"""
import uuid
from secrets import token_urlsafe
from typing import Optional

from cmem_plugin_base.dataintegration.types import StringParameterType, Autocompletion
from cmem_plugin_base.dataintegration.description import Plugin, PluginParameter
from cmem_plugin_base.dataintegration.entity import (
    Entities,
    Entity,
    EntitySchema,
    EntityPath,
)
from cmem_plugin_base.dataintegration.plugins import WorkflowPlugin


class RandomMethods(StringParameterType):
    """Random method type"""

    allow_only_autocompleted_values: bool = True

    autocomplete_value_with_labels: bool = True

    def autocomplete(
        self, query_terms: list[str], project_id: Optional[str] = None
    ) -> list[Autocompletion]:
        return [
            Autocompletion(
                value="token_urlsafe", label="Return a random URL-safe text string"
            ),
            Autocompletion(value="token_hex", label="converted to two hex digits"),
        ]


@Plugin(
    label="Random Values",
    plugin_id="Example-RandomValues",
    description="Generates random values of X rows a Y values.",
    documentation="""
This example workflow operator python plugin from the cmem-plugin-examples package
generates random values.

The values are generated in X rows a Y values. Both parameter can be specified:

- 'number_of_entities': How many rows do you need.
- 'number_of_values': How many values per row do you need.
""",
    parameters=[
        PluginParameter(
            name="number_of_entities",
            label="Entities (Rows)",
            description="How many rows will be created per run.",
        ),
        PluginParameter(
            name="number_of_values",
            label="Values (Columns)",
            description="How many values are created per entity / row.",
        ),
        PluginParameter(
            name="random_function",
            label="Randomize Function",
            param_type=RandomMethods(),
        ),
    ],
)
class RandomValues(WorkflowPlugin):
    """Example Workflow Plugin: Random Values"""

    def __init__(
        self,
        number_of_entities: int = 10,
        number_of_values: int = 5,
        random_function: str = "token_urlsafe",
    ) -> None:
        if number_of_entities < 1:
            raise ValueError("Entities (Rows) needs to be a positive integer.")
        if number_of_values < 1:
            raise ValueError("Values (Columns) needs to be a positive integer.")
        self.number_of_entities = number_of_entities
        self.number_of_values = number_of_values

    def execute(self, inputs=()) -> Entities:
        self.log.info("Start creating random values.")
        self.log.info(f"Config length: {len(self.config.get())}")
        value_counter = 0
        entities = []
        for _ in range(self.number_of_entities):
            entity_uri = f"urn:uuid:{str(uuid.uuid4())}"
            values = []
            for _ in range(self.number_of_values):
                values.append([token_urlsafe(16)])
                value_counter += 1
            entities.append(Entity(uri=entity_uri, values=values))
        paths = []
        for path_no in range(self.number_of_values):
            path_uri = f"https://example.org/vocab/RandomValuePath/{path_no}"
            paths.append(EntityPath(path=path_uri))
        schema = EntitySchema(
            type_uri="https://example.org/vocab/RandomValueRow",
            paths=paths,
        )
        self.log.info(f"Happy to serve {value_counter} random values.")
        return Entities(entities=entities, schema=schema)
