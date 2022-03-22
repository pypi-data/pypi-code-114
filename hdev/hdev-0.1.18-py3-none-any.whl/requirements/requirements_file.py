"""hdev requirements implementation."""

import json
import os
from functools import cached_property, lru_cache
from glob import glob
from pathlib import PosixPath

from hdev.requirements.package import Package
from hdev.requirements.parse import parse


class RequirementsFile(PosixPath):
    """Represents a pinned, or unpinned requirements file."""

    @property
    def tox_env(self):
        """Get the tox env used with this file."""
        if env := self.settings().get("compile_in"):
            return env

        return "dev" if self.stem == "requirements" else self.stem

    @property
    def tox_env_requirements_file(self):
        """Get the requirements file used in the tox env for this file."""
        return RequirementsFile(self.with_name(f"{self.tox_env}.txt"))

    @property
    def pinned_file(self):
        """Get the pinned version of this file."""

        return RequirementsFile(self.with_suffix(".txt").absolute())

    @property
    def unpinned_file(self):
        """Get the unpinned version of this file."""

        return RequirementsFile(self.with_suffix(".in").absolute())

    @property
    def file_references(self):
        """Get any references from this file to other requirements files.

        :returns: A list of RequirementsFile objects
        """

        return (req for req in self._requirements if isinstance(req, RequirementsFile))

    @property
    def plain_dependencies(self):
        """Get plain python dependencies from this file.

        :returns: A list of Package objects
        """

        return (req for req in self._requirements if isinstance(req, Package))

    @lru_cache(1)
    def settings(self):
        """Read settings from a header in the file if any is present.

        The line must be the first line of the file in the following format:

            # hdev: {<JSON DICT>}

        :return: A dict of settings information
        :raises ValueError: If the JSON cannot be parsed
        """
        if not self.exists():
            return {}

        with open(self, encoding="utf-8") as handle:
            first_line = handle.readline()

        if first_line and first_line.startswith("# hdev"):
            try:
                return json.loads(first_line[6:])
            except json.JSONDecodeError as err:
                raise ValueError(
                    f"Cannot read settings from {self} as the JSON is malformed"
                ) from err

        return {}

    @cached_property
    def _requirements(self):
        return list(
            parse(
                lines=self.read_text("utf-8").split("\n"),
                base_dir=self.parent,
                ref_factory=lambda op, filename: RequirementsFile(filename)
                if op == "-r"
                else None,
                dep_factory=Package,
            )
        )

    @classmethod
    def find(cls, requirements_dir):
        """Find unpinned requirements in a directory.

        :return: An iterable of RequirementsFile in an order that is safe to
            compile
        """
        req_files = {}

        for file_name in glob(os.path.join(requirements_dir, "*.in")):
            req_file = cls(file_name).unpinned_file
            req_files[req_file] = [
                ref.unpinned_file for ref in req_file.file_references
            ]

        # Generate a sort key which is always bigger than any parents we
        # depend on
        def sort_key(req_file):
            return 1 + sum(sort_key(parent) for parent in req_files[req_file])

        return sorted(req_files, key=sort_key)
