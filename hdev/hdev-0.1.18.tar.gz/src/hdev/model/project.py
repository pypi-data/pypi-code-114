"""A model object for a checked out Hypothesis project."""

import os
from enum import Enum
from functools import cached_property
from pathlib import Path


class Project:
    """A checked out Hypothesis project (app or lib)."""

    # For easy mocking
    root_dir = None
    type = None

    class Type(Enum):
        APPLICATION = "application"
        LIBRARY = "library"

    def __init__(self, root_dir, type_=None):
        """Initialize a Project object.

        :param root_dir: The root of the project
        :param type_: The type of the project (if this is not specified it will
            be automatically determined)
        """
        self.root_dir = Path(root_dir).absolute()
        self.type = self.Type(type_) if type_ else self.get_type()

    @property
    def config(self):
        # pylint: disable=import-outside-toplevel
        from hdev.configuration import Configuration

        return Configuration.load(self.root_dir / "pyproject.toml")

    def requirements(self):
        """Get a dict of lists of requirements."""

        # pylint: disable=import-outside-toplevel
        from hdev.requirements.requirements_file import RequirementsFile
        from hdev.requirements.setup_file import SetupConfigFile

        if self.type == self.Type.APPLICATION:
            # Should be reading from pyproject.toml to get the requirements dir?
            req_files = RequirementsFile.find(self.root_dir / "requirements")

            return {
                req_file.stem: list(req_file.plain_dependencies)
                for req_file in req_files
            }

        return SetupConfigFile(self.root_dir / "setup.cfg").requirements()

    @classmethod
    def from_child_dir(cls, dir_path):
        dir_path = Path(dir_path).absolute()

        search_dir = Path(dir_path)
        if not search_dir.exists():
            raise NotADirectoryError(search_dir)

        while not (search_dir / "pyproject.toml").is_file():
            if search_dir == search_dir.parent:
                raise EnvironmentError(
                    f"Cannot find a project in any parent directory of '{dir_path}'"
                )

            search_dir = search_dir.parent

        return Project(search_dir)

    @classmethod
    def find(cls, dir_path, filter_type=None, filter_name=None):
        for project in cls.from_parent_dir(dir_path):
            if filter_type and project.type != filter_type:
                continue

            if filter_name and project.name not in filter_name:
                continue

            yield project

    @classmethod
    def from_parent_dir(cls, dir_path, max_depth=4):
        dir_path = dir_path.absolute()
        root_depth = len(dir_path.parts)

        for root, dirs, _files in os.walk(dir_path):
            path = Path(root)

            has_git = ".git" in dirs

            if has_git or (len(path.parts) - root_depth) == max_depth:
                # Prevent recursing into this dir
                dirs.clear()

            if not has_git:
                continue

            try:
                yield Project(root_dir=path)
            except EnvironmentError:
                continue

    @cached_property
    def name(self):
        return self.config.get("tool.hdev.project_name")

    def get_type(self):
        """Get the type of this project (app or library)."""

        try:
            return Project.Type(self.config.get("tool.hdev.project_type"))
        except (ValueError, KeyError) as err:
            raise EnvironmentError(
                f"Directory {self.root_dir} doesn't look like a Hypothesis project"
            ) from err
