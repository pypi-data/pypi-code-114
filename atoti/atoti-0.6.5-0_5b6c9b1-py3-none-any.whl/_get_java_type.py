from typing import Any, Mapping, Type

from atoti_core import JavaType, is_numeric_type, to_array_type

# Currently, supported types for Python constants.
_PYTHON_TYPE_TO_JAVA_TYPE: Mapping[Type[Any], JavaType] = {
    str: "string",
    # Use the widest type to avoid compilation problems
    int: "long",
    float: "double",
}


def get_java_type(value: Any) -> JavaType:
    python_type = type(value)

    if python_type == list:
        first_element_type = get_java_type(value[0])
        if not is_numeric_type(first_element_type):
            raise TypeError("Only lists of numeric values are supported.")
        return to_array_type(first_element_type)

    try:
        return _PYTHON_TYPE_TO_JAVA_TYPE[python_type]
    except KeyError as error:
        raise TypeError(
            f"Python type: {python_type} has no corresponding Java type."
        ) from error
