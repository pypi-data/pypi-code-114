"""Represents a `setup.cfg` file."""
from configparser import ConfigParser
from pathlib import PosixPath

from hdev.requirements.package import Package


class SetupConfigFile(PosixPath):
    """Represents a `setup.cfg` file."""

    def __init__(self, *_, **__):
        if not self.exists():
            raise FileNotFoundError(f"Could not find setup file: {self}")

        self._parser = ConfigParser()
        self._parser.read(self)

    _REQUIREMENTS_LOCATIONS = {"install": "install_requires", "tests": "tests_require"}

    def requirements(self):
        """Get a dict of requirements types to Package objects."""
        requirements = {}

        for name, location in self._REQUIREMENTS_LOCATIONS.items():
            if text_block := self._parser.get("options", location, fallback=None):
                requirements[name] = [
                    Package(item) for item in text_block.split("\n") if item
                ]

        return requirements
