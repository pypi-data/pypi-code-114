import types
from typing import Any, Dict, List, Optional, Tuple, Type, Union

import dataclasses
import enum
import json
import uuid
from dataclasses import MISSING, Field, field, make_dataclass

import numpy as np
from loguru import logger

from autodidaqt_common.enum import enum_mapping
from autodidaqt_common.json import RichEncoder
from autodidaqt_common.remote.utils import register_remote_schema_type
from autodidaqt_common.schema import ArrayType, ObjectType

TypeDefinitionID = str

# This is a global temporary variable which let's us reserve
# and assign IDs for types before they are entered into the registry.
# This is necessary in order to support circular type definitions.
_WORKING_IDS: Dict[type, TypeDefinitionID] = {}

# Registrations of various types
_TYPE_DEFINITIONS_BY_NAME: Dict[str, Type["TypeDefinition"]] = {}
_TYPE_DEFINITIONS_BY_ID: Dict[TypeDefinitionID, Type["TypeDefinition"]] = {}
_TYPE_CONSTRUCTORS_BY_ID: Dict[TypeDefinitionID, type] = {}


def generate_type_id(type) -> TypeDefinitionID:
    return str(uuid.uuid3(uuid.NAMESPACE_URL, f"daquiri://{type}"))


class TypeVariant(str, enum.Enum):
    Core = "core"
    Dataclass = "dataclass"
    Array = "array"
    Object = "object"
    Enum = "enum"


@register_remote_schema_type
class Value:
    type_id: TypeDefinitionID
    value: str

    def to_instance(self):
        return TypeDefinition.from_value(self)


@register_remote_schema_type
class RichFieldDefinition:
    type_id: TypeDefinitionID
    name: str
    default: Optional[Value] = None

    def to_tuple_format(self) -> Tuple[str, Any, Any]:
        field_info = None
        if self.default:
            field_info = field(default=self.default.to_instance())

        return (self.name, TypeDefinition.get_definition_by_id(self.type_id).type, field_info)

    @classmethod
    def from_field(cls, field: Field):
        type_def = TypeDefinition.from_type(field.type)
        default = field.default

        if default is not MISSING:
            default = type_def.to_value(default)

        return cls(
            type_id=type_def.id,
            name=field.name,
            default=default,
        )


@register_remote_schema_type
class TypeDefinition:
    id: TypeDefinitionID
    variant: TypeVariant
    name: str
    fields: Optional[Dict[str, RichFieldDefinition]] = None
    info: Optional[Dict[str, str]] = None
    enum_fields: Optional[Dict[str, str]] = None
    enum_bases: List[TypeDefinitionID] = field(default_factory=list)

    def to_value(self, value) -> Value:
        return Value(type_id=self.id, value=self.instance_to_json(value))

    def hydrate_type(self) -> type:
        try:
            return self.type
        except KeyError:
            if self.variant == TypeVariant.Dataclass:
                fields = []
                for _, rich_field in self.fields.items():
                    fields.append(rich_field.to_tuple_format())

                return make_dataclass(self.name, fields)

            if self.variant == TypeVariant.Array:
                return np.ndarray

            if self.variant == TypeVariant.Enum:
                new_enum = types.new_class(
                    self.name,
                    [TypeDefinition.get_definition_by_id(b).type for b in self.enum_bases]
                    + [enum.Enum],
                    {},
                    lambda ns: ns.update(self.enum_fields),
                )
                print(new_enum)
                return new_enum

            raise NotImplementedError(f"Cannot hydrate type for {self}")

    @classmethod
    def from_value(cls, value: Value) -> Any:
        type_def = cls.get_definition_by_id(value.type_id)
        return type_def.json_to_instance(value.value)

    def instance_to_json(self, value):
        """
        `instance_to_json` and its partner method `json_to_instance` need to handle the following cases

        1. np.ndarray (corresponding to the ArrayType)
        2. core types, handled by defering to [module] json.{loads/dumps}
        3. enums
        4. dataclasses, handled by jerry-rigging dataclasses_json
           - this is handled in this way to reduce the burden on users to
             attach the decorator themselves. An alternative would be to call
             the decorator manually when we do type registration

        These functions are so named to avoid shadowing methods provided by dataclasses_json
        """
        if self.variant == TypeVariant.Array:
            arr: np.ndarray = value
            return json.dumps(arr.tolist())

        if self.variant == TypeVariant.Core:
            return json.dumps(value)

        if self.variant == TypeVariant.Enum:
            # safe as long as we add `int` or `str` to the enum type hierarchy
            return json.dumps(value)

        if self.variant == TypeVariant.Dataclass:
            try:
                return value.to_json()
            except AttributeError:
                return json.dumps(value, cls=RichEncoder)

        raise NotImplementedError

    def json_to_instance(self, json_data: str) -> Any:
        if self.variant == TypeVariant.Array:
            json_data = json.loads(json_data)
            return np.array(json_data)

        if self.variant == TypeVariant.Core:
            value = json.loads(json_data)
            # make sure we produce an int or float as appropriate
            return self.type(value)

        if self.variant == TypeVariant.Enum:
            self.type(json.loads(json_data))

        if self.variant == TypeVariant.Dataclass:
            try:
                return self.type.from_json(json_data)
            except AttributeError:
                dict_data = json.loads(json_data)
                return self.type(**dict_data)

        raise NotImplementedError

    @staticmethod
    def all_types() -> Dict[str, Type["TypeDefinition"]]:
        return {str(k): v for k, v in _TYPE_DEFINITIONS_BY_ID.items()}

    @classmethod
    def id_for_type(cls, type_):
        if type_ in _WORKING_IDS:
            return _WORKING_IDS[type_]

        return cls.from_type(type_).id

    @staticmethod
    def register_type_definition(type_def: Type["TypeDefinition"], type_: type):
        if type_def.id in _TYPE_DEFINITIONS_BY_ID or type_def.name in _TYPE_DEFINITIONS_BY_NAME:
            raise ValueError(f"Type definition {type_def} is already registered.")

        _TYPE_DEFINITIONS_BY_ID[type_def.id] = type_def
        _TYPE_DEFINITIONS_BY_NAME[type_def.name] = type_def
        _TYPE_CONSTRUCTORS_BY_ID[type_def.id] = type_

    @staticmethod
    def get_definition(registered_cls) -> Type["TypeDefinition"]:
        # TODO this is icky... we need a more compelling way of handling
        # Array and Object schemas
        if isinstance(registered_cls, ArrayType):
            return _TYPE_DEFINITIONS_BY_NAME["ndarray"]

        if not isinstance(registered_cls, type):
            logger.warning(f"Improperly handled type {registered_cls}")
            registered_cls = type(registered_cls)

        return _TYPE_DEFINITIONS_BY_NAME[registered_cls.__name__]

    @staticmethod
    def get_definition_by_id(id: TypeDefinitionID) -> Type["TypeDefinition"]:
        return _TYPE_DEFINITIONS_BY_ID[id]

    @property
    def type(self) -> type:
        return _TYPE_CONSTRUCTORS_BY_ID[self.id]

    @classmethod
    def from_core_type(cls, type_) -> Type["TypeDefinition"]:
        id = generate_type_id(type_.__name__)
        type_def = cls(id=id, variant=TypeVariant.Core, name=type_.__name__, fields=None)
        cls.register_type_definition(type_def, type_)
        return type_def

    @classmethod
    def from_type(cls, type_):
        try:
            return cls.get_definition(type_)
        except KeyError:
            pass

        if dataclasses.is_dataclass(type_) and not isinstance(type_, (ArrayType, ObjectType)):
            return cls.from_dataclass(type_)

        core_variants = {float, int, str}
        if isinstance(type_, type) and type_ in core_variants:
            return cls.from_core_type(type_)

        if isinstance(type_, type) and issubclass(type_, enum.Enum):
            type_def = cls.from_enum(type_)
            cls.register_type_definition(type_def, type_)
            return type_def

        type_def = None
        if isinstance(type_, ArrayType):
            logger.warning("Assuming naive implementation of Array and Object types.")
            # we need to think about parameterization of types
            id = generate_type_id("ArrayType")
            type_def = cls(
                id=id,
                name="ndarray",
                variant=TypeVariant.Array,
                # this probably doesn't function terribly well
                info={"shape": json.dumps(type_.shape), "dtype": str(type_.dtype)},
            )
            type_ = np.ndarray
        elif isinstance(type_, ObjectType):
            logger.warning("Assuming naive implementation of Array and Object types.")
            id = generate_type_id("ObjectType")
            type_def = cls(id=id, name="ObjectType", variant=TypeVariant.Object)

        assert type_def is not None
        cls.register_type_definition(type_def, type_)
        return type_def

    @classmethod
    def from_enum(cls, type_):
        return cls(
            id=generate_type_id(type_.__name__),
            name=type_.__name__,
            variant=TypeVariant.Enum,
            enum_fields=enum_mapping(type_),
        )

    @classmethod
    def from_dataclass(cls, data_cls):
        # preregister the type
        id = generate_type_id(data_cls.__name__)
        _WORKING_IDS[data_cls] = id

        fields = {}
        for field in dataclasses.fields(data_cls):
            fields[field.name] = RichFieldDefinition.from_field(field)

        type_def = cls(id=id, name=data_cls.__name__, fields=fields, variant=TypeVariant.Dataclass)

        # delete the temporary registration since we are about
        # to make a real registration
        del _WORKING_IDS[data_cls]
        cls.register_type_definition(type_def, data_cls)
        return cls


# Register standard types
for t in [str, int, float]:
    TypeDefinition.from_type(t)


class ExperimentStates(str, enum.Enum):
    Startup = "STARTUP"
    Idle = "IDLE"
    Running = "RUNNING"
    Paused = "PAUSED"
    Shutdown = "SHUTDOWN"


class ExperimentTransitions(str, enum.Enum):
    Initialize = "initialize"
    Start = "start"
    StartManual = "start_manual"
    Shutdown = "shutdown"
    Stop = "stop"
    Pause = "pause"


@register_remote_schema_type
class RemoteMethodInfo:
    name: str


@register_remote_schema_type
class RemotePropertyInfo:
    name: str


@register_remote_schema_type
class RemoteAxisState:
    path: List[Union[str, int]]
    schema: TypeDefinitionID


@register_remote_schema_type
class RemoteDriverInfo:
    driver_cls_name: str


@register_remote_schema_type
class RemoteProfileInfo:
    name: str


@register_remote_schema_type
class RemoteInstrumentState:
    flat_axes: List[RemoteAxisState]
    driver_info: RemoteDriverInfo
    methods_info: Dict[str, RemoteMethodInfo]
    properties_info: Dict[str, RemotePropertyInfo]
    profiles_info: Dict[str, RemoteProfileInfo]

    is_simulating: bool

    active_profile_name: Optional[str] = None


@register_remote_schema_type
class RemoteExperimentState:
    scan_methods: List[TypeDefinitionID]
    fsm_state: ExperimentStates


@register_remote_schema_type
class RemoteApplicationState:
    instruments: Dict[str, RemoteInstrumentState]
    extra_types: Dict[str, TypeDefinition]
    experiment_state: RemoteExperimentState


def typedef(type_or_instance) -> TypeDefinition:
    if not isinstance(type_or_instance, (type, ArrayType, ObjectType)):
        type_or_instance = type(type_or_instance)

    return TypeDefinition.from_type(type_or_instance)
