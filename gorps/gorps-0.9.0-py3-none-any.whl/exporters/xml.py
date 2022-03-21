"""xml export"""

import os
from os import PathLike
from collections.abc import Iterable, Sequence
from typing import Optional, Union, Any, IO
from xml.etree import ElementTree

from ..model import Recipe
from .templating import fill_template, eval_restricted, dict_selector, find_placeholders
from .templating.exporter import TemplateExporterBase


class Exporter(TemplateExporterBase):
    name = "xml"
    ext = "xml"

    def export(self, recipes: Iterable[Recipe], out: str) -> None:
        return process_xml_template(self.template, self.build_environment(recipes), out)

    def export_multifile(self, recipes: Iterable[Recipe], out_dir: str) -> None:
        for recipe in recipes:
            process_xml_template(
                self.template,
                {**self.variables, "recipe": recipe},
                os.path.join(out_dir, recipe.title + "." + self.ext),
            )


Source = Union[str, bytes, PathLike[str], PathLike[bytes], int, IO[Any]]


def process_xml_template(
    template: str, environment: dict[str, Any], dest: Source
) -> None:
    namespaces = {}

    class TreeBuilder(ElementTree.TreeBuilder):
        """This is needed to preserve the namespace prefix."""

        @staticmethod
        def start_ns(prefix: str, uri: str) -> None:
            ElementTree.register_namespace(prefix, uri)
            namespaces[prefix] = uri

    # Ugly hack to prevent namespace processing of ElementTree:
    template = template.replace("v-bind:", "v-bind---")
    tree = ElementTree.fromstring(
        template, parser=ElementTree.XMLParser(target=TreeBuilder())
    )
    processed_doc = process_xml_tree_template(tree, environment, namespaces)
    ElementTree.ElementTree(processed_doc).write(
        dest, encoding="unicode", xml_declaration=True
    )


def process_xml_tree_template(
    tree: ElementTree.Element, environment: dict[str, Any], namespaces: dict[str, str]
) -> ElementTree.Element:
    (processed_doc,) = process_xml_node(tree, environment, namespaces)
    return processed_doc


def substitute_namespaces(attribute_name: str, namespaces: dict[str, str]) -> str:
    try:
        namespace, name = attribute_name.split(":", 1)
        return "{" + namespaces[namespace] + "}" + name
    except ValueError:
        return attribute_name


def process_xml_node(
    tree: ElementTree.Element,
    environment: dict[str, Any],
    namespaces: dict[str, str],
    override_attributes: Optional[dict[str, str]] = None,
) -> list[ElementTree.Element]:
    if override_attributes is None:
        override_attributes = tree.attrib
    for attribute, processor in (
        ("v-if", process_xml_node_if),
        ("v-for", process_xml_node_for),
    ):
        if attribute in override_attributes:
            return processor(tree, environment, namespaces)
    if tree.tag == "template":
        return process_xml_node_template(
            tree, environment, namespaces, override_attributes
        )
    new_attributes = {
        key: val
        for key, val in override_attributes.items()
        if not key.startswith("v-bind")
    }
    for key, val in override_attributes.items():
        key = key.replace("v-bind---", "v-bind:")
        if key.startswith("v-bind:"):
            attribute_name = key[len("v-bind:") :]
            attribute_value = dict_selector(val)(environment)
            new_attributes[attribute_name] = attribute_value
        if key == "v-bind":
            attributes = dict_selector(val)(environment).items()
            attributes = {
                substitute_namespaces(key, namespaces): val for key, val in attributes
            }
            new_attributes.update(attributes)

    new_tree = ElementTree.Element(tree.tag, new_attributes)
    text, sub_nodes = process_text(tree.text, environment)
    for e in sub_nodes:
        new_tree.extend(e)
    new_tree.text = text
    tail, sibling_nodes = process_text(tree.tail, environment)
    new_tree.tail = tail
    for child in tree:
        new_tree.extend(process_xml_node(child, environment, namespaces))
    return [new_tree] + sibling_nodes


def process_text(
    text: Optional[str], environment: dict[str, Any]
) -> tuple[Optional[str], list[ElementTree.Element]]:
    converted = text and fill_template_xml(text, environment)
    if isinstance(converted, str) or converted is None:
        return converted, []
    return None, converted


def fill_template_xml(
    template: str, env: dict[str, Any]
) -> Union[str, list[ElementTree.Element]]:
    try:
        marker = next(find_placeholders(template))
    except StopIteration:
        return template
    if not template.replace("{{" + marker + "}}", "").strip():
        value = eval_restricted(marker.strip(), env)
        if isinstance(value, list) and all(
            isinstance(e, ElementTree.Element) for e in value
        ):
            return value
    return fill_template(template, env)


def process_xml_node_for(
    tree: ElementTree.Element, environment: dict[str, Any], namespaces: dict[str, str]
) -> list[ElementTree.Element]:
    instruction = tree.attrib["v-for"]
    loop_vars_raw, selector = instruction.split(" in ")
    loop_range = dict_selector(selector.strip())(environment)
    loop_vars = [var.strip() for var in loop_vars_raw.split(",")]
    return sum(
        (
            process_xml_node(
                tree,
                environment={
                    **environment,
                    **dict(sloppy_zip(loop_vars, items)),
                },
                namespaces=namespaces,
                override_attributes={
                    key: val for key, val in tree.attrib.items() if key != "v-for"
                },
            )
            for items in loop_range
        ),
        [],
    )


def sloppy_zip(loop_vars: Sequence[Any], items: Any) -> Iterable[tuple[Any, Any]]:
    if len(loop_vars) > 1:
        return zip(loop_vars, items)
    return zip(loop_vars, [items])


def process_xml_node_if(
    tree: ElementTree.Element, environment: dict[str, Any], namespaces: dict[str, str]
) -> list[ElementTree.Element]:
    expression = tree.attrib["v-if"]
    evaluated = eval_restricted(expression, environment)
    if evaluated:
        return process_xml_node(
            tree,
            environment,
            namespaces=namespaces,
            override_attributes={
                key: val for key, val in tree.attrib.items() if key != "v-if"
            },
        )
    return []


def process_xml_node_template(
    tree: ElementTree.Element,
    environment: dict[str, Any],
    namespaces: dict[str, str],
    override_attributes: dict[str, str],
) -> list[ElementTree.Element]:
    if override_attributes:
        raise ValueError(
            f"No attributes other than v-if, v-for allowed in <template>. Attributes: {', '.join(tree.attrib)}"
        )
    return sum((process_xml_node(child, environment, namespaces) for child in tree), [])
