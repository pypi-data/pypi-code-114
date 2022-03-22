import json
import re
from enum import Enum


class PythonVersions(list):
    """A list which supports getting python versions in multiple styles.

    For all methods which accept style:

    :raises ValueError: For an unrecognised style
    """

    class Style(Enum):
        """An enumeration of supported styles."""

        PLAIN = "plain"
        """e.g. 3.8.8 3.9.2"""

        JSON = "json"
        """e.g.["3.6.12", "3.8.8", "3.9.2"]

        This is valid JSON and can be included in scripts.
        """

        TOX = "tox"
        """e.g. py27,py36,py37

        Which can be used in comprehensions like this:
            tox -e {py27,py36}-tests
        """

    _PYTHON_VERSION = re.compile(r"^(\d+).(\d+).(\d+)$")

    @classmethod
    def parse_string(cls, version_string):
        """Parse a version string into a tuple of digits.

        :returns: A tuple of integers
        :raises ValueError: If the version cannot be decoded
        """
        match = cls._PYTHON_VERSION.match(version_string)
        if not match:
            raise ValueError(f"Could not parse python version from: '{version_string}'")

        return tuple(int(digit) for digit in match.groups())

    @classmethod
    def from_strings(cls, version_strings):
        """Create a PythonVersions object from a list of version strings.

        This will ignore non numeric versions.

        :param version_strings: Strings to parse
        :return: PythonVersions object
        """
        versions = cls()
        for version_string in version_strings:
            # We can't / don't have to deal with `pypy` installs yet
            if version_string == "system" or version_string.startswith("pypy"):
                continue

            versions.append(cls.parse_string(version_string))

        return versions

    def format(self, style):
        """Get the python versions as a list in a variety of styles.

        :param style: One of the styles above
        :return: A generator of values in the chosen format
        :rtype: str
        """
        return (self.format_digits(value, style) for value in self)

    @classmethod
    def format_digits(cls, digits, style):
        """Get a single python version as a string in a variety of styles.

        :param digits: Tuple of digits
        :param style: One of the styles above
        :return: String formatted version
        :raises ValueError: For styles we do not understand
        """
        style = cls.Style(style)

        if style in (cls.Style.PLAIN, cls.Style.JSON):
            return f"{digits[0]}.{digits[1]}.{digits[2]}"

        assert style == cls.Style.TOX

        return f"py{digits[0]}{digits[1]}"

    def as_string(self, style):
        """Get the python versions as a string in a variety of styles.

        :param style: One of the styles above
        :return: A string representing all of the versions

        :raises ValueError: For an unrecognised style
        """
        style = self.Style(style)
        values = self.format(style)

        if style == self.Style.PLAIN:
            return " ".join(values)

        if style == self.Style.TOX:
            return ",".join(values)

        assert style == self.Style.JSON

        return json.dumps(list(values))
