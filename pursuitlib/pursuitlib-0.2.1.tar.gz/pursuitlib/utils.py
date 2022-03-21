import os
from typing import List


def is_null_or_empty(value) -> bool:
    return value is None or str(value) == ""


def is_null_or_white_space(value) -> bool:
    if value is None:
        return True
    return is_null_or_empty(str(value).strip())


def get_oneline_string(string: str) -> str:
    return string.replace("\n", "").replace("\r", "").replace("\t", "")


def list_to_string(objects: List) -> str:
    return ", ".join(map(str, objects))


def get_env(name: str, default = None) -> str:
    value = os.getenv(name, default)
    if value is None:
        raise EnvironmentError(f"The environment variable \"{name}\" is not defined")
    return value


def delete_file(path: str):
    if os.path.isfile(path):
        os.remove(path)
