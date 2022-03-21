"""
We have remote commands essentially corresponding to RPC for 

[x] HEARTBEAT [id]
[x]    HEARTBEAT

[x] SHUTDOWN [reason]
[p]    SHUTTING_DOWN_ETA [shutdown_summary]

[x] GET_ALL_STATE
[x]    PROVIDE_ALL_STATE

CONFIGURE
    PROVIDE_CONFIGURATION

[x] PAUSE_RUN
    PROVIDE_EXPERIMENT_STATE

[x] STOP_RUN
    PROVIDE_EXPERIMENT_STATE

START_RUN [config]
    PROVIDE_EXPERIMENT_STATE

QUEUE_RUN [config]
    PROVIDE_QUEUE_POSITION

WRITE_AXIS [instrument] [axis] [value]
    PROVIDE_AXIS_VALUE

READ_AXIS [instrument] [axis]
    PROVIDE_AXIS_VALUE

RUN_DEBUGGER_COMMAND [command_string]
    PROVIDE_DEBUGGER_STATE

Additionally, the remote may receive some messages which are not
directly in response to a command. These are

PROVIDE_RUN_SUMMARY

PROVIDE_RUN_SUMMARY

ENTER_DEBUGGER [task_reference]
    PROVIDE_DEBUGGER_STATE [task_reference]
"""

from typing import Any, List, Union

import json
import uuid
from dataclasses import dataclass, field

from dataclasses_json import LetterCase, dataclass_json
from loguru import logger

from autodidaqt_common.remote.schema import RemoteApplicationState, Value, typedef
from autodidaqt_common.remote.utils import (
    ALL_COMMANDS,
    ALL_RESPONSES,
    ALL_WIRE_MESSAGES,
    normalized_name,
)

__all__ = [
    "serialize_wire_types",
    "deserialize_wire_types",
    # Internal
    "InternalMessage",
    "RequestShutdown",
    "AcknowledgeShutdown",
    # Remote Commands
    "RemoteCommand",
    "ShutdownCommand",
    "GetAllStateCommand",
    "SetScanConfigCommand",
    "PauseRunCommand",
    "StopRunCommand",
    "StartRunCommand",
    "QueueRunCommand",
    "HeartbeatCommand",
    "ReadAxisCommand",
    # Remote Responses
    "RemoteResponse",
    "AllState",
    "ShutdownEta",
    "AxisRead",
    "RecordData",
    "RunSummary",
    "Log",
]

AxisPath = List[Union[str, int]]

def deserialize_wire_types(message: Any) -> Any:
    if not isinstance(message, dict):
        return message

    message_type = message.get("type")
    if message_type not in ALL_WIRE_MESSAGES:
        return message

    cmd_cls = ALL_WIRE_MESSAGES[message_type]

    try:
        return cmd_cls.from_dict(message["message"])
    except Exception as e:
        logger.error(cmd_cls)
        logger.error(message)
        import pprint

        pprint.pprint(json.loads(message["message"]))
        raise e


def serialize_wire_types(cmd: Any) -> str:
    try:
        return json.dumps({"type": normalized_name(cmd), "message": cmd.to_dict()})
    except TypeError as e:
        print(cmd)
        raise e


def register_command(cls):
    if not issubclass(cls, RemoteCommand):
        raise TypeError(f"{cls} must subclass RemoteCommand to be registered as a command.")
    cls = dataclass(cls)
    cls = dataclass_json(letter_case=LetterCase.CAMEL)(cls)

    ALL_COMMANDS[normalized_name(cls)] = cls
    ALL_WIRE_MESSAGES[normalized_name(cls)] = cls
    return cls


def register_response(cls):
    if not issubclass(cls, RemoteResponse):
        raise TypeError("Must subclass RemoteResponse to be registered as a response.")
    cls = dataclass(cls)
    cls = dataclass_json(letter_case=LetterCase.CAMEL)(cls)

    ALL_RESPONSES[normalized_name(cls)] = cls
    ALL_WIRE_MESSAGES[normalized_name(cls)] = cls
    return cls


def register_internal_message(cls):
    if not issubclass(cls, InternalMessage):
        raise TypeError("Must subclass InternalMessage to be registered as an internal message.")

    cls = dataclass(cls)
    cls = dataclass_json(letter_case=LetterCase.CAMEL)(cls)

    ALL_WIRE_MESSAGES[normalized_name(cls)] = cls
    return cls


class InternalMessage:
    @classmethod
    def command_name(cls):
        return normalized_name(cls.__name__)


@register_internal_message
class RequestShutdown(InternalMessage):
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    async def respond_did_shutdown(self, app):
        await app.messages.put(AcknowledgeShutdown(parent_id=self.id))


@register_internal_message
class AcknowledgeShutdown(InternalMessage):
    parent_id: str = field(default_factory=lambda: str(uuid.uuid4()))


class RemoteCommand:
    @classmethod
    def command_name(cls):
        return normalized_name(cls.__name__)


class RemoteResponse:
    @classmethod
    def command_name(cls):
        return normalized_name(cls.__name__)


@register_command
class ShutdownCommand(RemoteCommand):
    pass


@register_response
class ShutdownEta(RemoteResponse):
    eta: float


@register_command
class GetAllStateCommand(RemoteCommand):
    pass


@register_response
class AllState(RemoteResponse):
    state: RemoteApplicationState


@register_command
class SetScanConfigCommand(RemoteCommand):
    scan_config: Value

    @classmethod
    def from_scan_config(cls, scan_config):
        type_def = typedef(scan_config)
        return cls(scan_config=type_def.to_value(scan_config))


@register_command
class PauseRunCommand(RemoteCommand):
    pass


@register_command
class StopRunCommand(RemoteCommand):
    pass


@register_command
class StartRunCommand(RemoteCommand):
    pass


@register_command
class StartManualRunCommand(RemoteCommand):
    pass


@register_command
class QueueRunCommand(RemoteCommand):
    pass


@register_command
class PointCommand(RemoteCommand):
    pass

@register_command
class StepCommand(RemoteCommand):
    reads: List[AxisPath]
    writes: List[List[
        Union[
            AxisPath,
            Value,
        ]
    ]]

@register_command
class HeartbeatCommand(RemoteCommand):
    id: str = field(default_factory=lambda: str(uuid.uuid4()))


@register_response
class AxisRead(RemoteResponse):
    axis_path: AxisPath

    read_time: str
    value: Value


@register_response
class RecordData(RemoteResponse):
    point: int
    step: int
    path: AxisPath
    value: Value
    time: str


@register_command
class ReadAxisCommand(RemoteCommand):
    axis_path: AxisPath


@register_command
class WriteAxisCommand(RemoteCommand):
    axis_path: AxisPath
    value: Value


@register_response
class RunSummary(RemoteResponse):
    pass


@register_response
class Log(RemoteResponse):
    # We could provide a lot more information here using the structured
    # information at
    # https://loguru.readthedocs.io/en/stable/api/logger.html#sink
    msg: str


FORWARD_TO_EXPERIMENT_MESSAGE_CLASSES = (
    SetScanConfigCommand,
    StartRunCommand,
    StartManualRunCommand,
    PointCommand,
    StepCommand,
    PauseRunCommand,
    StopRunCommand,
    QueueRunCommand,
)
