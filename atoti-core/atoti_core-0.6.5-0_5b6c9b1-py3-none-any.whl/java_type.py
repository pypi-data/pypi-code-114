from typing import Any, Literal, cast

from typing_extensions import TypeGuard

from .literal import get_literal_args

_BooleanJavaType = Literal["boolean"]

_NumericJavaType = Literal["double", "float", "int", "long"]

_PrimitiveJavaType = Literal[_BooleanJavaType, _NumericJavaType]

_DateJavaType = Literal[
    "LocalDate",
    "LocalDateTime",
    "ZonedDateTime",
]

_TimeJavaType = Literal["LocalTime"]

_TemporalJavaType = Literal[_DateJavaType, _TimeJavaType]

_NumericArrayJavaType = Literal[
    "double[]",
    "float[]",
    "int[]",
    "long[]",
]

_ArrayJavaType = Literal[_NumericArrayJavaType, "Object[]"]

JavaType = Literal[
    _PrimitiveJavaType,
    _ArrayJavaType,
    _TemporalJavaType,
    "Object",
    "string",
]

_ARRAY_SUFFIX = "[]"


def parse_java_type(value: str) -> JavaType:
    # Used by UDAFs.
    if value == "IVector":
        return "double[]"

    value = value.lower()

    try:
        return next(
            cast(Any, java_type)
            for java_type in get_literal_args(JavaType)
            if value == cast(str, java_type).lower()
        )
    except StopIteration as error:
        raise TypeError(f"""Expected a Java type but got "{value}".""") from error


def is_array_type(java_type: JavaType) -> TypeGuard[_ArrayJavaType]:
    return java_type in get_literal_args(_ArrayJavaType)


def to_array_type(java_type: JavaType) -> _ArrayJavaType:
    java_type = parse_java_type(f"{java_type}{_ARRAY_SUFFIX}")
    if not is_array_type(java_type):
        raise TypeError(f"Expected {java_type} to be an array type.")
    return java_type


def is_date_type(java_type: JavaType) -> TypeGuard[_DateJavaType]:
    return java_type in get_literal_args(_DateJavaType)


def is_time_type(java_type: JavaType) -> TypeGuard[_TimeJavaType]:
    return java_type in get_literal_args(_TimeJavaType)


def is_temporal_type(java_type: JavaType) -> TypeGuard[_TemporalJavaType]:
    return java_type in get_literal_args(_TemporalJavaType)


def is_numeric_type(java_type: JavaType) -> TypeGuard[_NumericJavaType]:
    return java_type in get_literal_args(_NumericJavaType)


def is_numeric_array_type(java_type: JavaType) -> TypeGuard[_NumericArrayJavaType]:
    return java_type in get_literal_args(_NumericArrayJavaType)


def is_boolean_type(java_type: JavaType) -> TypeGuard[_BooleanJavaType]:
    return java_type in get_literal_args(_BooleanJavaType)


def is_primitive_type(java_type: JavaType) -> TypeGuard[_PrimitiveJavaType]:
    return java_type in get_literal_args(_PrimitiveJavaType)
