from types import ModuleType
from typing import Any, Dict, Optional, TypeVar

from importlib_metadata import entry_points

GROUP = "talisman.plugins"


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AbstractPluginManager(metaclass=Singleton):
    def __init__(self, attr: str, default=None):
        self._plugins = {}
        if default is not None:
            self._plugins[None] = default

        for entry_point in entry_points(group=GROUP):
            name = entry_point.name
            module = entry_point.load()
            if not isinstance(module, ModuleType):
                continue
            try:
                value = getattr(module, attr)
                if self._check_value(value):
                    self._plugins[name] = value
            except AttributeError:
                pass

    @property
    def plugins(self) -> Dict[Optional[str], Any]:
        return dict(self._plugins)

    @staticmethod
    def _check_value(value) -> bool:
        return True


_T = TypeVar('_T')


def flattened(data: Dict[str, Dict[str, _T]], delimiter: str = ':') -> Dict[str, _T]:
    result = {}
    for plugin, readers in data.items():
        for key, reader in readers.items():
            result[f"{plugin}{delimiter}{key}"] = reader
    return result
