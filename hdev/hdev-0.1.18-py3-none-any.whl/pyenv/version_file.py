"""Tools for reading and formatting information from .python-version files."""

import re
from collections import OrderedDict
from pathlib import PosixPath

from hdev.pyenv.python_versions import PythonVersions


class PyenvVersionFile(PosixPath):
    """A pyenv version file.

    This pyenv version file can accept tags in the form of comments like this:

        3.8.8 # future floating

    Currently accepted tags (format dependent) are:

     * future - Included in local testing but not required to pass CI
     * floating - Use a wild build version where supported
    """

    def __init__(self, file_name):
        """Initialise the version file.

        :param file_name: Path to the file to parse
        :raises FileNotFoundError: If the provided file is missing
        """
        # The path is read by the parent class in __new__ as PosixPaths are
        # immutable. So no need to pass it to the constructor.
        super().__init__()

        if not self.exists():
            raise FileNotFoundError(f"Expected to find version file '{file_name}'.")

        self.tagged_versions = self._parse_version_file(file_name)

    def versions(self, exclude=None, floating=False, first=False):
        """Yield digits from the set which match the modifiers.

        :param exclude: A set of tags to exclude
        :param floating: Modify those marked "floating" to have the last digit
            replaced with "x"
        :param first: Return the first item only
        :return: A PythonVersions object
        :rtype: hdev.pyenv.python_versions.PythonVersions
        """

        exclude = set(exclude or [])

        versions = PythonVersions()

        for digits, tags in self.tagged_versions.items():
            if tags & exclude:
                continue

            if floating and "floating" in tags:
                digits = tuple([digits[0], digits[1], "x"])

            versions.append(digits)
            if first:
                break

        return versions

    _PYTHON_VERSION = re.compile(r"^(\d+).(\d+).(\d+)$")

    @classmethod
    def _parse_version_file(cls, file_name):
        # Add support for older versions of Python to guarantee ordering
        versions = OrderedDict()

        with open(file_name, encoding="utf-8") as handle:
            for line in handle:
                comment = ""

                if "#" in line:
                    comment = line[line.index("#") + 1 :]
                    line = line[: line.index("#")]

                line = line.strip()
                if not line:
                    continue

                tags = set(part.strip() for part in comment.strip().split(" "))
                tags.discard("")  # Drop anything caused by repeated spaces

                versions[PythonVersions.parse_string(line)] = tags

        return versions
