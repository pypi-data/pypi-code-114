import json
import re
import typing as T
from enum import Enum
import os
from pathlib import Path
from black import format_str, FileMode
import edgedb
from pydantic import BaseModel
from devtools import debug
from .introspection import (
    introspect_objects,
    introspect_scalars,
    ObjectType,
    ScalarType,
    Link,
    Property,
    Cardinality,
)

PATH_TO_MODULE = "dgraph_orm.vendors.edgedb"
DEFAULT_INDENT = "    "
CONFIG_NAME = "GraphORM"


class GeneratorException(Exception):
    pass


def indent_lines(s: str, indent: str = DEFAULT_INDENT) -> str:
    chunks = s.split("\n")
    return indent + f"\n{indent}".join(chunks)


def imports() -> str:
    lines = [
        "from __future__ import annotations",
        "import typing as T",
        "from enum import Enum",
        "from datetime import datetime, date, timedelta",
        "from uuid import UUID",
        "from decimal import Decimal",
        "from edgedb import RelativeDuration, AsyncIOClient, create_async_client",
        "from pydantic import BaseModel, Field",
        f"from {PATH_TO_MODULE} import Node, Resolver, NodeException, ResolverException, UpdateOperation, Batch",
    ]
    return "\n".join(lines)


async def build_enums(client: edgedb.AsyncIOClient) -> str:
    scalar_types = await introspect_scalars(client)
    enum_strs: T.List[str] = []
    for scalar in scalar_types:
        if not scalar.enum_values:
            continue
        enum_value_strs: T.List[str] = [f'{e} = "{e}"' for e in scalar.enum_values]
        enum_value_str = "\n".join(enum_value_strs)
        s = f"class {scalar.node_name}(str, Enum):\n{indent_lines(enum_value_str)}"
        enum_strs.append(s)
    return "\n".join(enum_strs)


def build_node_link_function_str(link: Link) -> str:
    link_resolver_name = f"{link.target.model_name}Resolver"
    return f"""
async def {link.name}(
    self,
    resolver: {link_resolver_name} = None,
    refresh: bool = False,
    force_use_stale: bool = False,
) -> {link.type_str}:
    return await self.resolve(
        edge_name="{link.name}",
        edge_resolver=resolver or {link_resolver_name}(),
        refresh=refresh,
        force_use_stale=force_use_stale,
    )
    """


def build_resolver_link_function_str(node_resolver_name: str, link: Link) -> str:
    link_resolver_name = f"{link.target.model_name}Resolver"
    return f"""
def {link.name}(self, _: T.Optional[{link_resolver_name}] = None, /) -> {node_resolver_name}:
    if "{link.name}" in self._nested_resolvers:
        raise ResolverException("A resolver for `{link.name}` has already been provided.")
    self._nested_resolvers["{link.name}"] = _ or {link_resolver_name}()
    return self
    """


def build_update_function_str(node_resolver_name: str, links: T.List[Link]) -> str:
    link_strs: T.List[str] = []
    link_names: T.List[str] = []
    for link in links:
        if link.readonly:
            continue
        link_strs.append(
            f"{link.name}: T.Optional[{link.target.model_name}Resolver] = None"
        )
        link_names.append(link.name)
    link_params_str = ", ".join(link_strs)
    return f"""
async def update(
    self,
    given_resolver: {node_resolver_name} = None,
    error_if_no_update: bool = False,
    batch: Batch = None,
    given_client: AsyncIOClient = None,
    {link_params_str}
) -> None:
    set_links_d = {{{", ".join([f'"{link_name}": {link_name}' for link_name in link_names])}}}
    set_links_d = {{key: val for key, val in set_links_d.items() if val is not None}}
    
    return await super().update(
        given_resolver=given_resolver,
        error_if_no_update=error_if_no_update,
        set_links_d=set_links_d,
        batch=batch,
        given_client=given_client
    )
    """


def add_quotes(lst: T.Iterable[str]) -> T.Iterable[str]:
    return [f'"{o}"' for o in lst]


def build_orm_config(
    model_name: str, updatable_fields: T.Set[str], exclusive_fields: T.Set[str]
) -> str:
    return f"""
class {CONFIG_NAME}:
    model_name = "{model_name}"
    client = client
    updatable_fields: T.Set[str] = {{{', '.join(add_quotes(sorted(list(updatable_fields))))}}}
    exclusive_fields: T.Set[str] = {{{', '.join(add_quotes(sorted(list(exclusive_fields))))}}}
    """


def stringify_dict(d: T.Dict[str, str]) -> str:
    inner = [f'"{k}":"{v}"' for k, v in d.items()]
    return f"{{{','.join(inner)}}}"


def edgedb_conversion_type_from_prop(prop: Property) -> str:
    s = prop.target.name
    pattern = r"default::\w+"
    s = re.sub(pattern, "std::str", s)
    return s


def build_node_and_resolver(object_type: ObjectType) -> str:
    # need to sort props and links by required, exclusive, no default, rest
    object_type.properties.sort(
        key=lambda x: f"{x.required}-{x.is_exclusive}-{x.default}",
        reverse=True,
    )
    object_type.links.sort(
        key=lambda x: f"{x.required}-{x.is_exclusive}-{x.default}",
        reverse=True,
    )
    # start with the properties
    node_resolver_name = f"{object_type.node_name}Resolver"
    property_strs: T.List[str] = []
    insert_property_strs: T.List[str] = []
    updatable_fields: T.Set[str] = set()
    exclusive_fields: T.Set[str] = set()

    node_edgedb_conversion_map: T.Dict[str, str] = {}
    insert_edgedb_conversion_map: T.Dict[str, str] = {}

    for prop in object_type.properties:
        conversion_type = edgedb_conversion_type_from_prop(prop)
        node_edgedb_conversion_map[prop.name] = conversion_type
        if not prop.readonly:
            updatable_fields.add(prop.name)
        if prop.is_exclusive:
            exclusive_fields.add(prop.name)
        default_value_str = "..." if prop.required else "None"
        allow_mutation_str = f"allow_mutation={not prop.readonly}"
        property_strs.append(
            f"{prop.name}: {prop.type_str} = Field({default_value_str}, {allow_mutation_str})"
        )
        # for insert type
        if prop.name != "id":
            insert_edgedb_conversion_map[prop.name] = conversion_type
            insert_type_str = prop.type_str
            # if required but has default, add optional back
            if prop.required and prop.default:
                insert_type_str = f"T.Optional[{insert_type_str}]"
            default_value_str = (
                " = None" if insert_type_str.startswith("T.Optional[") else ""
            )
            insert_property_strs.append(
                f"{prop.name}: {insert_type_str}{default_value_str}"
            )
    link_function_strs: T.List[str] = []
    resolver_function_strs: T.List[str] = []
    updatable_links: T.Set[str] = set()
    exclusive_links: T.Set[str] = set()
    for link in object_type.links:
        if link.name == "__type__":
            continue
        if not link.readonly:
            updatable_links.add(link.name)
        if link.is_exclusive:
            exclusive_links.add(link.name)
        link_function_strs.append(build_node_link_function_str(link))
        resolver_function_strs.append(
            build_resolver_link_function_str(
                node_resolver_name=node_resolver_name, link=link
            )
        )
        # for insert
        insert_resolver_str = f"{link.target.model_name}Resolver"
        if (not link.required) or (link.required and link.default):
            insert_resolver_str = f"T.Optional[{insert_resolver_str}]"
        default_value_str = (
            " = None" if insert_resolver_str.startswith("T.Optional[") else ""
        )
        insert_property_strs.append(
            f"{link.name}: {insert_resolver_str}{default_value_str}"
        )
    orm_config_str = build_orm_config(
        model_name=object_type.node_name,
        updatable_fields={*updatable_fields, *updatable_links},
        exclusive_fields={*exclusive_fields, *exclusive_links},
    )

    insert_model_name = f"{object_type.node_name}Insert"

    # insert type
    insert_inner_str = "\n".join(insert_property_strs)
    insert_conversion_map_str = f"_edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {stringify_dict(insert_edgedb_conversion_map)}"
    insert_s = f"class {insert_model_name}(BaseModel):\n{indent_lines(insert_inner_str)}\n\n{indent_lines(insert_conversion_map_str)}"

    # node
    node_properties_str = "\n".join(property_strs)
    node_conversion_map_str = f"_edgedb_conversion_map: T.ClassVar[T.Dict[str, str]] = {stringify_dict(node_edgedb_conversion_map)}"
    node_link_functions_str = "\n".join(link_function_strs)
    update_function_str = build_update_function_str(
        node_resolver_name=node_resolver_name, links=object_type.links
    )
    node_inner_strs = [
        node_properties_str,
        "\n",
        node_conversion_map_str,
        node_link_functions_str,
        update_function_str,
        orm_config_str,
    ]
    node_inner_str = "\n".join(node_inner_strs)
    node_s = f"class {object_type.node_name}(Node[{insert_model_name}]):\n{indent_lines(node_inner_str)}"

    # resolver
    resolver_properties_str = f"_node = {object_type.node_name}"
    resolver_link_functions_str = "\n".join(resolver_function_strs)
    resolver_inner_strs = [resolver_properties_str, resolver_link_functions_str]
    resolver_inner_str = "\n".join(resolver_inner_strs)
    resolver_s = f"class {node_resolver_name}(Resolver[{object_type.node_name}]):\n{indent_lines(resolver_inner_str)}"

    final_s = (
        f"{object_type.node_name}.{CONFIG_NAME}.resolver_type = {node_resolver_name}"
    )
    return f"{insert_s}\n{node_s}\n{resolver_s}\n{final_s}"


async def build_nodes_and_resolvers(client: edgedb.AsyncIOClient) -> str:
    object_types = await introspect_objects(client)
    node_strs: T.List[str] = []
    for object_type in object_types:
        node_strs.append(build_node_and_resolver(object_type))
    update_forward_refs_str = "\n".join(
        [f"{o.node_name}Insert.update_forward_refs()" for o in object_types]
    )
    nodes_str = "\n".join(node_strs)
    return f"{nodes_str}\n\n{update_forward_refs_str}"


class DBVendor(str, Enum):
    edgedb = "edgedb"


class TLSSecurity(str, Enum):
    insecure = "insecure"


class DBConfig(BaseModel):
    vendor: DBVendor
    host: str
    password: str
    tls_security: TLSSecurity


def build_client(db_config: DBConfig) -> str:
    return f"""
client = create_async_client(
    tls_security="{db_config.tls_security.value}", host="{db_config.host}", password="{db_config.password}"
)
    """


def validate_output_path(path: Path) -> None:
    if not os.path.isdir(path):
        if os.path.isfile(path):
            raise GeneratorException(
                f"output path {path=} must be a directory, not a file."
            )
        if not os.path.exists(path):
            os.makedirs(path)


async def generate(config_path: Path, output_path: Path) -> None:
    validate_output_path(output_path)
    for db_name, db_config_d in json.loads(open(config_path).read()).items():
        db_config = DBConfig.parse_obj(db_config_d)
        client = edgedb.create_async_client(
            tls_security=db_config.tls_security,
            host=db_config.host,
            password=db_config.password,
        )
        imports_str = imports()
        client_str = build_client(db_config)
        enums_str = await build_enums(client)
        nodes_and_resolvers_str = await build_nodes_and_resolvers(client)

        s = "\n".join([imports_str, client_str, enums_str, nodes_and_resolvers_str])
        s = format_str(s, mode=FileMode())

        open(output_path / f"{db_name}.py", "w").write(s)
