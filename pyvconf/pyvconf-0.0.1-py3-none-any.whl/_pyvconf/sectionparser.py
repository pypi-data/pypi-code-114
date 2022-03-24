"""An abstract parser for configs with sections."""

from dataclasses import dataclass, field
from typing import TypeVar

from _pyvconf.parser import Parser
from _pyvconf.types import Sections

Config = TypeVar("Config")


# mypy gives a false positive for dataclasses with abstract methods.
# As a workaround, we could split the dataclass and abstract portions into
# their own classes, then compose the Parser from these two classes. See
# https://github.com/python/mypy/issues/5374#issuecomment-568335302. But,
# we will instead just suppress the error.
@dataclass  # type: ignore
class SectionParser(Parser[Config]):
    """Interface to parse a config source with sections."""
    sections: Sections = field(default_factory=dict)

