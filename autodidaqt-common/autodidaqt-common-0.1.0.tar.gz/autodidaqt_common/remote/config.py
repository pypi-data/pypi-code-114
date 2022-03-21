from dataclasses import dataclass

__all__ = ["RemoteConfiguration"]


@dataclass
class RemoteConfiguration:
    ui_address: str
