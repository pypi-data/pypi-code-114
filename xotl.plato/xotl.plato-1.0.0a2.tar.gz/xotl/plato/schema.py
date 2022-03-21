import collections.abc
import dataclasses
import enum
import sys
import typing as t
from dataclasses import dataclass
from datetime import date, datetime, timedelta

from typing_extensions import Annotated, get_args, get_origin
from xotl.tools.names import nameof
from xotl.tools.objects import classproperty, memoized_property

from .base import Describable, FullRepr
from .types import (
    BooleanType,
    DateTimeType,
    DateType,
    DurationType,
    FloatType,
    I,
    IntegerType,
    ListType,
    MappingType,
    OptionalType,
    S,
    Selection,
    Shape,
    StringType,
    Type,
)

SB = t.TypeVar("SB", bound="SchemaBase")


@dataclass
class SchemaBase(Describable):
    """Base class for schema objects.

    Schema objects are those that can be *statically* cast into `types
    <xotl.plato.types>`:mod:.  These objects can be `dumped <dump>`:meth: using
    the type object obtained with `get_static_type`:meth:.

    The type object basically maps *primitive* python types to the type system
    of `xotl.plato.types`:mod:.  This means that there cannot be recursive
    definitions.  You can provide a type yourself using
    `typing.Annotated`:class:.

    Example::

       >>> from dataclasses import dataclass
       >>> from typing_extensions import Annotated
       >>> from xotl.plato.types import *
       >>> from xotl.plato.schema import SchemaBase

       >>> @dataclass
       ... class Foo(SchemaBase):
       ...     name: str
       ...     tags: t.Sequence[str]
       ...     number: t.Optional[int]
       ...     age: Annotated[int, IntegerType(min_value=0, max_value=1000)]

       >>> Foo.get_static_type()
       SchemaType(shape={'name': StringType(),
                         'tags': ListType(of=StringType(...)),
                         'number': OptionalType(type=IntegerType()),
                         'age': IntegerType(min_value=0,
                                            min_included=True,
                                            max_value=1000,
                                            max_included=False)})

       >>> foo = Foo(name="bar", tags=["baz"], number=-100, age=2)
       >>> foo.dump()
       {'name': 'bar', 'tags': ['baz'], 'number': -100, 'age': 2}

       >>> infoolid = Foo(name="bar", tags=None, number=-100, age=2)
       >>> infoolid.dump()
       Traceback (most recent call last):
       ...
       TypeError: 'NoneType' object is not iterable

    Nested schemata are allowed::

       >>> @dataclass
       ... class Bar(SchemaBase):
       ...    name: str
       ...    foo: Foo

       >>> Bar.get_static_type()
       SchemaType(shape={'name': StringType(), 'foo': SchemaType(...)})

       >>> bar = Bar("bat", foo)
       >>> bar.dump()
       {'name': 'bat', 'foo': {...}}

       >>> inbarlid = Bar("bar", infoolid)
       >>> inbarlid.dump()
       Traceback (most recent call last):
       ...
       TypeError: 'NoneType' object is not iterable

    If some of the attributes of your object cannot be feasible represented by a
    type object they won't be included in the schema type::

       >>> @dataclass
       ... class Model:   # pretend is an ORM model
       ...    id: int

       >>> @dataclass
       ... class Reference(SchemaBase):
       ...     ref: Model

       >>> Reference.get_static_type()
       SchemaType(shape={})


    You can provide the classmethods ``parse_<fieldname>`` and ``dump_<fieldname>``
    to parse and dump the values of that attribute::

       >>> @dataclass
       ... class Reference(SchemaBase):
       ...     ref: Model
       ...
       ...     @classmethod
       ...     def parse_ref(cls, value: int) -> Model:
       ...         return Model(value)
       ...
       ...     @classmethod
       ...     def dump_ref(cls, value: Model, *, validate: bool = True) -> int:
       ...          return value.id

       >>> r = Reference(Model(10))
       >>> r.dump()
       {'ref': 10}

    .. warning:: You must provide BOTH classmethods; otherwise the attribute is
       not included in the schema type.

    Inheritance works a expected::

       >>> @dataclass
       ... class RelationRef(Reference):
       ...     target: Model
       ...     parse_target = Reference.parse_ref
       ...     dump_target = Reference.dump_ref

       >>> rel = RelationRef(Model(1), Model(2))
       >>> rel.dump()
       {'ref': 1, 'target': 2}

       >>> RelationRef.get_static_type()
       SchemaType(shape={'ref': ..., 'target': ...})

    Annotations that yield two (or more) different types are rejected::

       >>> @dataclass
       ... class NotAChance(Reference):
       ...    something: t.Union[str, int]

       >>> NotAChance.get_static_type()
       Traceback (most recent call last):
       ...
       TypeError: Impossible to find a unique type for something in ...

    Annotations of a classes inheriting from `enum.IntEnum`:class:, use
    `IntEnumType`:class: Annotations of classes inheriting from
    `enum.Enum`:class: (but not from `enum.IntEnum`:class:), use
    `EnumType`:class:.

    """

    @classproperty
    def namespace(cls) -> str:  # pragma: no cover
        return "schema"

    @classproperty
    def constructor_name(cls) -> str:  # pragma: no-cover
        return nameof(cls, typed=True, inner=True, full=True)

    @classmethod
    def get_static_type(cls) -> Type:
        res = _STATIC_TYPES_MAP.get(cls)
        if res is None:
            res = _STATIC_TYPES_MAP[cls] = SchemaType(cls)
        return res

    def dump(self) -> t.Mapping[str, t.Any]:  # pragma: no cover
        return self.get_static_type().dump(self)

    @classmethod
    def parse(
        cls: t.Type[SB],
        full_repr: t.Mapping[str, t.Any],
    ) -> SB:  # pragma: no cover
        return cls.get_static_type().parse(full_repr)

    @property
    def full_repr(self):  # pragma: no cover
        return {
            ":ns:": self.namespace,
            ":base:": self.constructor_name,
            **self.dump(),
        }


class NonRegisteredType(Type[S, I], abstract=True):
    """Base class for types that don't support reconstruction from full_repr."""

    def __init_subclass__(cls, **kwargs):
        kwargs["abstract"] = True
        super().__init_subclass__(**kwargs)


# Schemata are reported as object types, its shape given by the schema's types.
# But internally we use the SchemaType to integrate the parse/dump methods with
# the type ecosystem.
@dataclass(unsafe_hash=True)
class SchemaType(NonRegisteredType[t.Mapping[str, S], SB]):
    schemacls: t.Type[SB]

    @property
    def shape(self) -> Shape[Type]:
        def _get_fields(cls):
            try:
                return dataclasses.fields(cls)
            except TypeError:
                return []

        classes = list(reversed([base for base in self.schemacls.mro()]))
        return {
            field.name: field_type
            for cls in classes
            for field in _get_fields(cls)
            if (field_type := self._get_type_for_attr(field, cls)) is not None
        }

    def __repr__(self):  # pragma: no cover
        return f"SchemaType(shape={dict(self.shape)})"

    @classproperty
    def constructor_name(cls) -> str:  # pragma: no cover
        return "object"

    @property
    def simplified_repr(self) -> str:  # pragma: no cover
        shape_args = [
            f"{name}: {type_.simplified_repr}"
            for name, type_ in self.shape.items()
        ]
        return f"{self.constructor_name}[{{{', '.join(shape_args)}}}]"

    @property
    def full_repr(self):  # pragma: no cover
        return {
            ":ns:": self.namespace,
            ":base:": self.constructor_name,
            "shape": {
                name: type_.full_repr for name, type_ in self.shape.items()
            },
        }

    def parse(self, raw_value: t.Mapping[str, S]) -> SB:
        return self.schemacls(
            **{
                attr: self.shape[attr].parse(value)
                for attr, value in raw_value.items()
            }
        )

    def dump(
        self,
        value: SB,
        *,
        validate: bool = True,
    ) -> t.Mapping[str, S]:
        return {
            attr: type.dump(getattr(value, attr), validate=validate)
            for attr, type in self.shape.items()
        }

    def _get_type_for_attr(
        self,
        field: dataclasses.Field,
        cls: t.Type,
    ) -> t.Optional[Type]:
        """Get the underlying BaseType of an attribute.

        :param attr_name:  The name of the attribute.

        If the underlying form doesn't have a type hint for `attr_name`,
        return None.

        Hints made by `typing_extensions.Annotated`:any: take precedence.  A
        BaseType in the anotations is selected.  No attempt to match the annotated
        type and the BaseType is made.

        If we can't find an appropriate BaseType, return None.  If the annotation
        has more that one possible BaseType, raise a TypeError.

        """
        try:
            annotation = getattr(cls, "__annotations__", {})[field.name]
        except KeyError:
            return None
        else:
            attr_name = field.name
            if isinstance(annotation, str):
                annotation = self._eval_annotation(annotation, cls)
            base_type = self._get_type_from_annotation(annotation, attr_name)
            if self._needs_custom_type(attr_name):
                return CustomizedAttrType(  # type: ignore
                    self.schemacls,
                    attr_name,
                    base_type=base_type,
                )
            else:
                return base_type

    def _eval_annotation(
        self,
        annotation: str,
        cls,
    ) -> t.Any:  # pragma: no cover
        """Evaluates the annotation in the module of the schemacls."""
        module = sys.modules[cls.__module__]
        return eval(annotation, vars(module))

    def _get_type_from_annotation(
        self,
        annotation: t.Any,
        attr_name: str,
    ) -> t.Optional[Type]:
        candidates: t.List[Type] = []
        origin = get_origin(annotation) or annotation
        if origin is Annotated:
            main, *annotations = get_args(annotation)
            types = tuple(arg for arg in annotations if isinstance(arg, Type))
            candidates.extend(types)
            if not types:
                res = self._get_type_from_annotation(main, attr_name)
                if res is not None:
                    candidates.append(res)
        elif isinstance(origin, type) and issubclass(origin, enum.IntEnum):
            return IntEnumType(origin)
        elif isinstance(origin, type) and issubclass(origin, enum.Enum):
            return EnumType(origin)
        elif isinstance(origin, type) and issubclass(origin, SchemaBase):
            # TODO: Detect recursive structures which are not supported by our
            # Type Language.  In any case Python will reach its recursion limit.
            candidate = origin.get_static_type()
            if candidate is not None:
                candidates.append(candidate)
        elif origin in (
            list,
            collections.abc.Sequence,
            set,
            collections.abc.Set,
        ):
            arg = get_args(annotation)[0]
            res = self._get_type_from_annotation(arg, attr_name)
            if res is not None:
                candidates.append(ListType(res))
        elif origin is t.Union:
            args = get_args(annotation)
            subtypes = tuple(
                result
                for arg in args
                if arg is not type(None)  # noqa
                if (result := self._get_type_from_annotation(arg, attr_name))
                is not None
            )
            if subtypes:
                if any(arg is type(None) for arg in args):  # noqa
                    candidates.extend(OptionalType(t) for t in subtypes)
                else:
                    candidates.extend(subtypes)
        elif origin in (collections.abc.Mapping, dict):
            key_annotation, value_annotation = get_args(annotation)
            key_type = self._get_type_from_annotation(key_annotation, attr_name)
            value_type = self._get_type_from_annotation(
                value_annotation, attr_name
            )
            if key_type is not None and value_type is not None:
                candidates.append(MappingType(key_type, value_type))
        if (
            not candidates
            and (base := _PYTHON_TYPES_MAP.get(origin)) is not None
        ):
            candidates.append(base())
        if not candidates:
            return None
        else:
            result, *extra = candidates
            if extra:
                raise TypeError(
                    f"Impossible to find a unique type for {attr_name} in {self.schemacls}"
                )
            return result

    def _needs_custom_type(self, attr_name):
        return self.schemacls._has_custom_parse_method(
            attr_name
        ) and self.schemacls._has_custom_dump_method(attr_name)


@dataclass
class EnumType(NonRegisteredType[t.Union[str, enum.Enum], enum.Enum]):
    """Allows to dump/parse values of a given `enum.Enum`:class:.

    .. rubric:: Parsing and dumping

    The serialized form is the *name of the member* in the enumeration class.

    `dump`:meth: only accepts values of the enumeration class.  `parse`:meth:
    looks by the name of the member in the enumeration class.

    Example::

       >>> class COLORS(enum.IntEnum):
       ...     RED = 0xFF0000
       ...     GREEN = 0x00FF00
       ...     BLUE = 0x0000FF

       >>> enumtype = EnumType(COLORS)
       >>> enumtype.parse('RED')
       <COLORS.RED: 16711680>

       >>> enumtype.parse(COLORS.BLUE)
       <COLORS.BLUE: 255>

       >>> enumtype.parse(255)
       Traceback (most recent call last):
       ...
       TypeError: Invalid member name 255

    """

    enumcls: t.Type[enum.Enum]

    @classproperty
    def constructor_name(cls) -> str:  # pragma: no cover
        return "str"

    @property
    def simplified_repr(self) -> str:  # pragma: no cover
        return self._base_type.simplified_repr

    @property
    def full_repr(self) -> FullRepr:  # pragma: no cover
        return self._base_type.full_repr

    @memoized_property
    def _base_type(self) -> StringType:  # pragma: no cover
        return StringType(selection=self.selection)

    @memoized_property
    def selection(self) -> Selection:
        return Selection.from_pairs(
            (str(value), name)
            for name, value in self.enumcls.__members__.items()
        )

    def parse(self, raw_value: t.Union[str, enum.Enum]) -> enum.Enum:
        if isinstance(raw_value, self.enumcls):
            return raw_value
        if not isinstance(raw_value, str):  # pragma: no cover
            raise TypeError(f"Invalid member name {raw_value}")
        try:
            return getattr(self.enumcls, raw_value)
        except AttributeError:  # pragma: no cover
            raise ValueError(
                f"Unknown member {raw_value!r} in {self.enumcls!r}"
            )

    def dump(
        self,
        value: enum.Enum,
        *,
        validate: bool = True,
    ) -> str:
        # We must ignore `validate` because `value` must of the right
        # enumeration.
        if not isinstance(value, self.enumcls):  # pragma: no cover
            raise ValueError(f"Unkown value {value!r} in {self.enumcls!r}")
        return value.name


@dataclass
class IntEnumType(NonRegisteredType[t.Union[str, int], enum.IntEnum]):
    """Allows to dump/parse values of a given IntEnum.

    .. rubric:: Parsing and dumping

    The serialized form is the integer *value of the member* in the enumeration
    class.

    Example::

       >>> class COLORS(enum.IntEnum):
       ...     RED = 0xFF0000
       ...     GREEN = 0x00FF00
       ...     BLUE = 0x0000FF

       >>> enumtype = IntEnumType(COLORS)
       >>> enumtype.dump(COLORS.RED)
       16711680

       >>> enumtype.parse(COLORS.BLUE)
       <COLORS.BLUE: 255>

       >>> enumtype.parse(255)
       <COLORS.BLUE: 255>

    """

    enumcls: t.Type[enum.IntEnum]

    @classproperty
    def constructor_name(cls) -> str:  # pragma: no cover
        return "int"

    @property
    def simplified_repr(self) -> str:  # pragma: no cover
        return self._base_type.simplified_repr

    @property
    def full_repr(self) -> FullRepr:
        return self._base_type.full_repr

    @memoized_property
    def _base_type(self) -> IntegerType:
        return IntegerType(selection=self.selection)

    @memoized_property
    def selection(self) -> Selection:
        return Selection.from_pairs(
            (int(value), name)
            for name, value in self.enumcls.__members__.items()
        )

    def parse(self, raw_value: t.Union[str, int]) -> enum.IntEnum:
        if isinstance(raw_value, str):
            which = raw_value
        else:
            which = next(
                (
                    name
                    for value, name in self.selection
                    if value == int(raw_value)
                ),
                "",
            )
        try:
            return getattr(self.enumcls, which)
        except AttributeError:  # pragma: no cover
            raise ValueError(
                f"Unknown member {raw_value!r} in {self.enumcls!r}"
            )

    def dump(
        self,
        value: enum.IntEnum,
        *,
        validate: bool = True,
    ) -> t.Union[str, int]:
        # We must ignore `validate` because `value` must of the right
        # enumeration.
        if not isinstance(value, self.enumcls):  # pragma: no cover
            raise ValueError(f"Unkown value {value!r} in {self.enumcls!r}")
        return int(value)


# DON'T make this a subclass of BaseType; it is not a type in the language of
# ADR 59 (and it cannot be).  We only need this to customize the *type* of
# form's field that have a ``parse_`` method.
@dataclass(unsafe_hash=False)
class CustomizedAttrType(t.Generic[S, I]):
    schemacls: t.Type[SchemaBase]
    field_name: str
    base_type: t.Optional[Type[S, I]] = None

    def __post_init__(self):
        assert self.schemacls._has_custom_parse_method(self.field_name)
        assert self.schemacls._has_custom_dump_method(self.field_name)

    @property
    def constructor_name(self) -> str:  # pragma: no cover
        assert self.base_type is not None
        return self.base_type.constructor_name

    @property
    def simplified_repr(self) -> str:  # pragma: no cover
        assert self.base_type is not None
        return self.base_type.simplified_repr

    @property
    def full_repr(self):  # pragma: no cover
        assert self.base_type is not None
        return self.base_type.full_repr

    def parse(self, raw_value: S) -> I:
        return getattr(self.schemacls, f"parse_{self.field_name}")(raw_value)

    def dump(self, value: I, *, validate: bool = True) -> S:
        return getattr(self.schemacls, f"dump_{self.field_name}")(
            value, validate=validate
        )


_PYTHON_TYPES_MAP: t.MutableMapping[t.Type, t.Callable[[], Type]] = {
    bool: BooleanType,
    int: IntegerType,
    str: StringType,
    float: FloatType,
    date: DateType,
    datetime: DateTimeType,
    timedelta: DurationType,
}


def register_simple_type_map(
    which: t.Type,
    type_factory: t.Callable[[], Type],
) -> None:
    """Register a type factory for SchemaType.

    When casting python types to the type system we use, this registry to know
    which type to instance.

    This can be used to change (globally) the default type builder for a given
    type.

    For instance, if your applications uses pytz_ instead of `zoneinfo`:mod:,
    you can make all your schemata use ``use_pytz`` like this::

       >>> register_simple_type_map(datetime.datetime, lambda: DateTimeType(use_pytz=True))  # doctest: +SKIP

    .. _pytz: https://pypi.org/project/pytz/

    """
    _PYTHON_TYPES_MAP[which] = type_factory


_STATIC_TYPES_MAP: t.Dict[t.Type[SchemaBase], Type] = {}
