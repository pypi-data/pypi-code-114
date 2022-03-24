"""A concrete INI file parser."""

# pylint: disable=too-few-public-methods

import configparser

from _pyvconf.sectionparser import SectionParser


class IniParser(SectionParser[str]):
    """Parses an INI file."""

    def parse(self, src: str) -> None:
        """Parse an INI file."""
        config = configparser.ConfigParser()
        config.read(src)
        # If we define Items in types.py as SectionProxy, then the next
        # line passes type checks after .mypy_cache is updated. Then we can
        # revert Items to being a dict, and the next line will continue to
        # pass type checks. However, we will just ignore the error for now.
        self.sections = dict(config.items())  # type: ignore

