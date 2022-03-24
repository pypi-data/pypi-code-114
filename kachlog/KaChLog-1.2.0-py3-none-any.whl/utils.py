import os
from typing import Dict

from ._changelog import (
    _unreleased,
    actual_version,
    from_dict,
    from_release,
    from_semantic,
    release,
    to_dict,
)
from ._versioning import (
    bump,
    bump_major,
    bump_minor,
    bump_patch,
    get_bump_type,
    is_semantic,
)
from .exceptions import (
    ChangelogDoesNotExistError,
    InvalidSemanticVersion,
    VersionDoesNotExistError,
)
from .templates import DEFAULT_VERSION, TYPES_OF_CHANGE


class ChangelogUtils:
    TYPES_OF_CHANGE = TYPES_OF_CHANGE

    def __init__(self, changelog_path="CHANGELOG.md"):
        self.CHANGELOG = changelog_path
        self.__data = {}

    @property
    def data(self) -> Dict:
        """
        Create and hold structured data of the current changelog
        """
        if not os.path.isfile(self.CHANGELOG):
            raise ChangelogDoesNotExistError
        if not self.__data:
            self.__data = to_dict(self.CHANGELOG, show_unreleased=True)
        return self.__data

    def initialize_changelog_file(self, sections: bool = False) -> str:
        """
        Creates a changelog if one does not already exist
        """
        if os.path.isfile(self.CHANGELOG):
            return f"{self.CHANGELOG} already exists"
        self.__data = {"unreleased": _unreleased(sections)}
        self.write_changelog()
        return f"Created {self.CHANGELOG}"

    def write_changelog(self) -> None:
        """
        writes the lines out to the changelog
        """
        with open(self.CHANGELOG, "w", encoding="utf-8") as changelog:
            changelog.write(from_dict(self.data))
        self.__data = {}  # after write force self.data to reload

    def update_section(self, section, message: str) -> None:
        """Updates a section of the changelog with message"""
        if section in self.data["unreleased"]:
            self.data["unreleased"][section].append(message)
        else:
            self.data["unreleased"][section] = [message]
        self.write_changelog()

    def get_current_version(self) -> str:
        """Gets the Current Application Version Based on Changelog"""
        version, _ = actual_version(self.data)
        if version:
            return version
        return DEFAULT_VERSION

    def get_release_suggestion(self) -> str:
        """Suggests a release type"""
        return get_bump_type(self.data["unreleased"])

    def get_new_release_version(self, release_type: str = "suggest") -> str:
        """
        Returns the version of the new release
        """

        _, semantic_version = actual_version(self.data)
        if release_type == "major":
            bump_major(semantic_version)
        elif release_type == "minor":
            bump_minor(semantic_version)
        elif release_type == "patch":
            bump_patch(semantic_version)
        else:
            semantic_version = bump(self.data["unreleased"], semantic_version)
        return from_semantic(semantic_version)

    def cut_release(self, version: str = None, sections: bool = False) -> None:
        """Cuts a release and updates changelog"""
        if not is_semantic(version):
            raise InvalidSemanticVersion(version)

        out_version = release(self.data, version, sections)
        self.write_changelog()
        return f"Released {out_version}"

    def get_changes(self, version: str) -> str:
        """
        Returns changes in in all categories in selected version
        """
        if version != "unreleased" and not is_semantic(version):
            raise InvalidSemanticVersion(version)
        if version not in self.data:
            raise VersionDoesNotExistError
        return from_release(self.data[version], version)
