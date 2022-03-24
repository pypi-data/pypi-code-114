import typing as T
from uuid import UUID
from enum import Enum
from datetime import datetime, timedelta
from decimal import Decimal
import edgedb
from devtools import debug
from pydantic import BaseModel, PrivateAttr, Field

from .cache import CacheManager
from .execute import query as execute_query
from .batch import Batch
from .constants import random_str

InsertType = T.TypeVar("InsertType", bound=BaseModel)
ThisNodeType = T.TypeVar("ThisNodeType", bound="Node")

BaseModelType = T.TypeVar("BaseModelType", bound=BaseModel)

TempNodeType = T.TypeVar("TempNodeType", bound="Node")
if T.TYPE_CHECKING:
    from .resolver import Resolver

    TempResolverType = T.TypeVar("TempResolverType", bound=Resolver)
    ResolverType = T.TypeVar("ResolverType", bound=Resolver)


class NodeException(Exception):
    pass


def model_dict_to_str(
    *,
    d: dict,
    edgedb_conversion_map: T.Dict[str, str],
    set_links_d: T.Dict[str, "Resolver"] = None,
) -> T.Tuple[str, T.Dict[str, T.Any]]:
    field_strs: T.List[str] = []
    variables = {}
    for field_name, val in d.items():
        type_cast_str = edgedb_conversion_map.get(field_name)
        if not type_cast_str:
            # resolvers will come up here so ignore them
            if field_name in set_links_d or val == set():
                continue
            raise NodeException(f"{field_name=} not in {edgedb_conversion_map=}")
        variable_name = f"{field_name}{random_str(10)}"
        field_str = f"{field_name} := <{type_cast_str}>${variable_name}"
        if type(val) is set:
            val = list(val)
            field_str = f"{field_name} := array_unpack(<array<{type_cast_str}>>${variable_name})"
        field_strs.append(field_str)
        variables[variable_name] = val
    if set_links_d:
        for field_name, resolver in set_links_d.items():
            update_operation_str = resolver.update_operation_str
            if not update_operation_str:
                raise NodeException(
                    f"Update resolver for {field_name} does not have an update operation."
                )
            field_str = (
                f"{field_name} {update_operation_str}"
                f" (SELECT DETACHED {resolver._model_name}{resolver.all_filters_str()})"
            )
            field_strs.append(field_str)
            for variable_name, variable_value in resolver._query_variables.items():
                if variable_name in variables:
                    raise NodeException(
                        f"Query variable {variable_name} for update resolver {field_name} "
                        f"already exists in variables {variables}."
                    )
                variables[variable_name] = variable_value
    s = f'{{ {", ".join(field_strs)} }}'
    return s, variables


def basemodel_to_str(
    model: BaseModelType,
    default_replace: bool = False,
    fields_to_exclude: T.Set[str] = None,
) -> T.Tuple[str, T.Dict[str, T.Any]]:
    # should exclude_none = True?
    from .resolver import Resolver, UpdateOperation

    model_d = model.dict(exclude_none=True, exclude=fields_to_exclude)

    set_links_d = {}
    for field_name in model.__fields__.keys():
        val = getattr(model, field_name)
        if isinstance(val, Resolver):
            if not val._update_operation and default_replace:
                val.update_operation(UpdateOperation.REPLACE)
            set_links_d[field_name] = val
            if field_name in model_d:
                del model_d[field_name]

    return model_dict_to_str(
        d=model_d,
        edgedb_conversion_map=model._edgedb_conversion_map,
        set_links_d=set_links_d,
    )


class Node(BaseModel, T.Generic[InsertType]):
    id: UUID = Field(..., allow_mutation=False)

    _cache: CacheManager = PrivateAttr(default_factory=CacheManager)
    _used_resolver: "ResolverType" = PrivateAttr(None)
    _original_dict: dict = PrivateAttr(None)
    _deleted: bool = PrivateAttr(None)

    _edgedb_conversion_map: T.ClassVar[T.Dict[str, str]]

    _extra: dict = PrivateAttr(default=dict())

    @property
    def extra(self) -> dict:
        return self._extra

    class Config:
        validate_assignment = True

    class GraphORM:
        model_name: str = None
        client: edgedb.AsyncIOClient
        exclusive_fields: T.Set[str] = None
        resolver_type: T.ClassVar[T.Type["ResolverType"]]
        updatable_fields: T.ClassVar[T.Set[str]] = set()

    def to_resolver(self) -> "ResolverType":
        return self._used_resolver.__class__().filter(
            filter_str=".id = <uuid>$id", variables={"id": self.id}
        )

    @classmethod
    def to_resolver_many(
        cls: T.Type[ThisNodeType], nodes: T.List[ThisNodeType]
    ) -> "ResolverType":
        return cls.GraphORM.resolver_type().filter(
            ".id in array_unpack(<array<uuid>>$ids)",
            variables={"ids": [n.id for n in nodes]},
        )

    @property
    def cache(self) -> CacheManager:
        return self._cache

    @classmethod
    @property
    def db_client(cls) -> edgedb.AsyncIOClient:
        return cls.GraphORM.client

    def __repr__(self) -> str:
        r = super().__repr__()
        r = f"{r}, cache: {repr(self.cache)}" if not self.cache.is_empty() else r
        return r

    """CACHE"""

    async def resolve(
        self,
        edge_name: str,
        edge_resolver: "TempResolverType",
        refresh: bool = False,
        force_use_stale: bool = False,
        print_forced_refresh: bool = True,
    ) -> T.Optional[T.Union[TempNodeType, T.List[TempNodeType]]]:
        """return await self.resolve(
            name="artist", resolver=resolver, refresh=refresh, use_stale=use_stale
        )
        DID NOT INCLUDE STRICT, maybe will need it but for now i do not"""
        if refresh:
            self.cache.remove(edge_name)
        if edge_cache := self.cache.get(edge_name):
            if force_use_stale:
                return edge_cache.val
            if edge_cache.resolver.to_str() != edge_resolver.to_str():
                if print_forced_refresh:
                    print(
                        f"resolvers are different so removing {edge_name} from the cache, old: {edge_cache.resolver.to_str()}, new: {edge_resolver.to_str()}"
                    )
                self.cache.remove(edge_name)
        if not self.cache.exists(edge_name):
            self.used_resolver._nested_resolvers[edge_name] = edge_resolver
            self._used_resolver.clear_top_level_filters_and_variables()
            obj = await self.used_resolver.get(id=self.id)
            self.cache.replace(key=edge_name, cache=obj.cache.get(edge_name))
        return self.cache.get_val(edge_name)

    """CRUDS"""

    @property
    def used_resolver(self) -> "ResolverType":
        return self._used_resolver

    @classmethod
    async def add(
        cls: T.Type[ThisNodeType],
        insert: InsertType,
        given_resolver: "ResolverType" = None,
        batch: Batch = None,
        given_client: edgedb.AsyncIOClient = None,
        upsert_given_conflict_on: str = None,
        return_conflicting_model_on: str = None,
        custom_on_conflict_str: str = None,
    ) -> T.Optional[ThisNodeType]:
        """Turn insert into a string with variables"""
        if not given_resolver:
            given_resolver = cls.GraphORM.resolver_type()
        if custom_on_conflict_str:
            if return_conflicting_model_on or upsert_given_conflict_on:
                raise NodeException(
                    "You cannot give a custom conflict string with other conflict inputs."
                )
        if return_conflicting_model_on and upsert_given_conflict_on:
            raise NodeException(
                "You cannot both suppress a conflict and upsert given a conflict."
            )
        # I think default_replace=True is correct here. Your intention is to make sure these links are SET, not updated
        # if your intention is for them to update on upsert, then add ADD to the resolver
        s, variables = basemodel_to_str(insert, default_replace=True)
        insert_str = f"INSERT {cls._model_name} {s}"
        conflict_str = ""
        if custom_on_conflict_str:
            conflict_str = custom_on_conflict_str
        elif upsert_given_conflict_on:
            # replace s and variables
            fields_to_exclude = (
                set(insert.dict(exclude_none=True).keys())
                - cls.GraphORM.updatable_fields
            )
            update_s, update_variables = basemodel_to_str(
                insert, default_replace=True, fields_to_exclude=fields_to_exclude
            )
            variables.update(update_variables)
            conflict_str = f"UNLESS CONFLICT ON .{upsert_given_conflict_on} ELSE (UPDATE {cls._model_name} SET {update_s})"
        elif return_conflicting_model_on:
            conflict_str = f"UNLESS CONFLICT ON .{return_conflicting_model_on} ELSE (SELECT {cls._model_name})"
        if conflict_str:
            insert_str += f" {conflict_str}"
        if batch:
            batch.add(line=insert_str, variables={**variables})
            return None
        select_str = f"SELECT model {given_resolver.to_str()}"
        add_s = f"WITH model := ({insert_str}) {select_str}"
        raw_d = await execute_query(
            client=given_client or cls.db_client,
            query_str=add_s,
            variables=variables,
            only_one=True,
        )
        return given_resolver.parse_nested_obj(raw_d)

    @classmethod
    async def add_many(
        cls: T.Type[ThisNodeType],
        inserts: T.List[InsertType],
        given_resolver: "ResolverType" = None,
        given_client: edgedb.AsyncIOClient = None,
    ) -> T.List[ThisNodeType]:
        """This appears to have a max limit of something between 30 and 50, so must break it up"""
        if not given_resolver:
            given_resolver = cls.GraphORM.resolver_type()
        insert_strs: T.List[str] = []
        variables = {}
        for i, insert in enumerate(inserts):
            insert_str, insert_variables = basemodel_to_str(model=insert)
            insert_strs.append(insert_str)
            variables.update(insert_variables)
        insert_lines: T.List[str] = []
        model_name = cls._model_name
        model_enumerated_names: T.List[str] = []
        for i, insert_str in enumerate(insert_strs):
            model_enumerated_name = f"model_{i}"
            insert_lines.append(
                f"{model_enumerated_name} := (INSERT {model_name} {insert_str})"
            )
            model_enumerated_names.append(model_enumerated_name)
        insert_lines.append(f'models := ({" UNION ".join(model_enumerated_names)})')
        add_many_s = (
            f'WITH {", ".join(insert_lines)} SELECT models {given_resolver.to_str()}'
        )
        raw_d = await execute_query(
            client=given_client or cls.db_client,
            query_str=add_many_s,
            variables=variables,
        )
        return [given_resolver.parse_nested_obj(d) for d in raw_d]

    async def delete(
        self,
        given_resolver: "ResolverType" = None,
        batch: Batch = None,
        given_client: edgedb.AsyncIOClient = None,
    ) -> None:
        if not given_resolver:
            given_resolver = self._used_resolver
        given_resolver.clear_top_level_filters_and_variables()
        given_resolver.filter(filter_str=".id = <uuid>$id", variables={"id": self.id})
        if batch:
            batch.add(
                line=given_resolver.inner_delete_str(),
                variables=given_resolver._get_nested_query_variables(),
            )
            return
        raw_d = await execute_query(
            client=given_client or self.db_client,
            query_str=given_resolver.full_delete_str(),
            variables=given_resolver._get_nested_query_variables(),
            only_one=True,
        )
        if not raw_d:
            raise NodeException(
                f"No delete for {self._model_name}: {self.id} was registered."
            )
        node = given_resolver.parse_nested_obj(raw_d)
        node._deleted = True
        self.hydrate(new_node=node)

    @classmethod
    async def delete_many(
        cls: T.Type[ThisNodeType],
        models: T.List[ThisNodeType],
        given_resolver: "ResolverType" = None,
    ) -> None:
        if not given_resolver:
            given_resolver = cls.GraphORM.resolver_type()
        given_resolver.clear_top_level_filters_and_variables()
        given_resolver.filter(
            filter_str=".id in array_unpack(<array<uuid>>$ids)",
            variables={"ids": [model.id for model in models]},
        )
        raw_d = await execute_query(
            client=cls.db_client,
            query_str=given_resolver.full_delete_str(),
            variables=given_resolver._get_nested_query_variables(),
        )
        new_nodes = [given_resolver.parse_nested_obj(d) for d in raw_d]
        models_by_id: T.Dict[str, ThisNodeType] = {model.id: model for model in models}
        for new_node in new_nodes:
            new_node._deleted = True
            models_by_id[new_node.id].hydrate(new_node=new_node)

    def get_update_d(self) -> dict:
        current_d = self.dict()
        original_d = self._original_dict
        unset_key = "_UNSET_12398120"
        update_d = {}
        for field_name in self.GraphORM.updatable_fields:
            current_val = current_d.get(field_name, unset_key)
            original_val = original_d.get(field_name, unset_key)
            if current_val != original_val:
                if current_val != unset_key:
                    # if current val is not unset -> always set
                    if current_val is not None:
                        update_d[field_name] = current_val
                    else:
                        update_d[field_name] = set()
                else:
                    # current val is UNSET but original val is not
                    update_d[field_name] = set()
        return update_d

    async def update(
        self,
        given_resolver: "ResolverType" = None,
        error_if_no_update: bool = False,
        set_links_d: T.Dict[str, "Resolver"] = None,
        batch: Batch = None,
        given_client: edgedb.AsyncIOClient = None,
    ) -> None:
        """set_links_d -> {people_i_follow += (select Person filter .first_name = <str>first_name)}"""
        if not given_resolver:
            given_resolver = self._used_resolver
        update_d = self.get_update_d()
        if not update_d:
            message = f"No update registered for {self.id=}."
            if error_if_no_update:
                raise NodeException(message)
            else:
                print(message)
            return

        given_resolver.clear_top_level_filters_and_variables()
        given_resolver.filter(filter_str=".id = <uuid>$id", variables={"id": self.id})
        s, variables = model_dict_to_str(
            d=update_d,
            edgedb_conversion_map=self._edgedb_conversion_map,
            set_links_d=set_links_d,
        )

        given_resolver.validate_against_query_variables(variables)
        update_inner_str = (
            f"UPDATE {self._model_name} {given_resolver._filter_str} SET {s}"
        )

        variables_to_use = {**given_resolver._get_nested_query_variables(), **variables}

        if batch:
            batch.add(line=update_inner_str, variables=variables_to_use)
            return None

        update_s = (
            f"WITH model := ({update_inner_str}) "
            f"SELECT model {given_resolver.to_str(include_filters=False)}"
        )
        debug(update_s)
        raw_d = await execute_query(
            client=given_client or self.db_client,
            query_str=update_s,
            variables=variables_to_use,
            only_one=True,
        )
        if not raw_d:
            raise NodeException(
                f"No update for {self._model_name}: {self.id} was registered."
            )
        node = given_resolver.parse_nested_obj(raw_d)
        self.hydrate(new_node=node)

    @classmethod
    @property
    def _model_name(cls) -> str:
        model_name = getattr(cls.GraphORM, "model_name", None)
        if model_name is None:
            model_name = cls.__name__
        return model_name

    @classmethod
    @property
    def _exclusive_fields(cls) -> T.Set[str]:
        exclusive_fields = getattr(cls.GraphORM, "exclusive_fields", set())
        exclusive_fields.add("id")
        return exclusive_fields

    def hydrate(self, new_node: ThisNodeType) -> None:
        """Turns this node into the new node"""
        for field_name in new_node.__fields__.keys():
            new_field = getattr(new_node, field_name)
            old_field = getattr(self, field_name)
            if new_field != old_field:
                setattr(self, field_name, getattr(new_node, field_name))
        for private_attr_name in new_node.__private_attributes__.keys():
            setattr(self, private_attr_name, getattr(new_node, private_attr_name))

    async def refresh(self: ThisNodeType) -> None:
        if self._deleted:
            raise NodeException("Node is already deleted.")
        self._used_resolver.clear_top_level_filters_and_variables()
        new_node = await self._used_resolver.get(id=self.id)
        self.hydrate(new_node=new_node)
