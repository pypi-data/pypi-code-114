from typing import Callable, Optional

import json
from dataclasses import dataclass

from autodidaqt_common.remote.command import deserialize_wire_types, serialize_wire_types

__all__ = ["Middleware", "LogMiddleware", "TranslateCommandsMiddleware", "WireMiddleware"]


@dataclass
class Middleware:
    outbound: Optional[Callable] = None
    inbound: Optional[Callable] = None

    def run_outbound(self, message):
        if self.outbound:
            message = self.outbound(message)

        return message

    def run_inbound(self, message):
        if self.inbound:
            message = self.inbound(message)

        return message


@dataclass
class LogMiddleware:
    outbound: bool = True
    inbound: bool = True

    def run_outbound(self, message):
        if self.outbound:
            print(message)

        return message

    def run_inbound(self, message):
        if self.inbound:
            print(message)

        return message


@dataclass
class TranslateCommandsMiddleware:
    def run_outbound(self, message):
        if hasattr(message, "to_json"):
            return serialize_wire_types(message)

        return message

    def run_inbound(self, message):
        try:
            message = json.loads(message)
        except json.JSONDecodeError:
            pass

        message = deserialize_wire_types(message)
        return message


@dataclass
class WireMiddleware:
    def run_outbound(self, message):
        return message.encode("utf-8")

    def run_inbound(self, message):
        return message.decode("utf-8")
