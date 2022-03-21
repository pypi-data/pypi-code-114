from dataclasses import dataclass

from dataclasses_json import LetterCase, dataclass_json


def normalized_name(cmd_or_cmd_class) -> str:
    if not isinstance(cmd_or_cmd_class, type):
        cmd_or_cmd_class = type(cmd_or_cmd_class)

    return cmd_or_cmd_class.__name__


REMOTE_SCHEMA_TYPES = {}
ALL_COMMANDS = {}
ALL_RESPONSES = {}
ALL_WIRE_MESSAGES = {}


def register_remote_schema_type(cls):
    cls = dataclass(cls)
    cls = dataclass_json(letter_case=LetterCase.CAMEL)(cls)
    name = normalized_name(cls)

    REMOTE_SCHEMA_TYPES[name] = cls
    ALL_WIRE_MESSAGES[name] = cls

    return cls
