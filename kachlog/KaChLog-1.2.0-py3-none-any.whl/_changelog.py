import datetime
import re
from typing import Dict, Iterable, List, Optional, Union

from ._versioning import (
    actual_version,
    bump,
    from_semantic,
    semantic_order,
    to_semantic,
    to_sorted_semantic,
)
from .exceptions import InvalidSemanticVersion
from .templates import BASE, TYPES_OF_CHANGE


def is_release(line: str) -> bool:
    return line.startswith("## ")


def add_release(changes: Dict[str, dict], line: str) -> dict:
    release_line = line[3:].lower().strip(" ")
    # A release is separated by a space between version and release date
    # Release pattern should match lines like: "[0.0.1] - 2020-12-31" or [Unreleased]
    version, release_date = (
        release_line.split(" ", maxsplit=1)
        if " " in release_line
        else (release_line, None)
    )
    version = unlink(version)

    metadata = {"version": version, "release_date": extract_date(release_date)}
    try:
        metadata["semantic_version"] = to_semantic(version)
    except InvalidSemanticVersion:
        pass

    return changes.setdefault(version, {"metadata": metadata})


def unlink(value: str) -> str:
    return value.lstrip("[").rstrip("]")


def extract_date(date: str) -> str:
    if not date:
        return date

    return date.lstrip(" -(").rstrip(" )")


def is_category(line: str) -> bool:
    return line.startswith("### ")


def add_category(release_dict: dict, line: str) -> List[str]:
    category = line[4:].lower().strip(" ")
    return release_dict.setdefault(category, [])


# Link pattern should match lines like: "[1.2.3]: https://github.com/user/project/releases/tag/v0.0.1"
link_pattern = re.compile(r"^\[(.*)\]: (.*)$")


def is_link(line: str) -> bool:
    return link_pattern.fullmatch(line) is not None


def add_information(category: List[str], line: str):
    category.append(line.lstrip(" *-").rstrip(" -"))


def to_raw_dict(changelog_path: str) -> Dict[str, dict]:
    changes = {}
    # As URLs can be defined before actual usage, maintain a separate dict
    urls = {}
    with open(changelog_path, "r", encoding="utf-8") as change_log:
        current_release = {}
        for line in change_log:
            clean_line = line.strip(" \n")

            if is_release(clean_line):
                current_release = add_release(changes, clean_line)
            elif is_link(clean_line):
                link_match = link_pattern.fullmatch(clean_line)
                urls[link_match.group(1).lower()] = link_match.group(2)
            elif clean_line:
                current_release["raw"] = current_release.get("raw", "") + line

    # Add url for each version (create version if not existing)
    for version, url in urls.items():
        changes.setdefault(version, {"metadata": {"version": version}})["metadata"][
            "url"
        ] = url

    unreleased_version = None
    for version, current_release in changes.items():
        metadata = current_release["metadata"]
        # If there is an empty release date, it identify the unreleased section
        if ("release_date" in metadata) and not metadata["release_date"]:
            unreleased_version = version

    changes.pop(unreleased_version, None)

    return changes


def to_dict(
    changelog_path: Union[str, Iterable[str]], *, show_unreleased: bool = False
) -> Dict[str, dict]:
    """
    Convert changelog markdown file following keep a changelog format into python dict.

    :param changelog_path: Path to the changelog file, or context manager providing iteration on lines.
    :param show_unreleased: Add unreleased section (if any) to the resulting dictionary.
    :return python dict containing version as key and related changes as value.
    """
    # Allow for changelog as a file path or as a context manager providing content
    try:
        with open(changelog_path, "r", encoding="utf-8") as change_log:
            return _to_dict(change_log, show_unreleased)
    except TypeError:
        return _to_dict(changelog_path, show_unreleased)


def _to_dict(change_log: Iterable[str], show_unreleased: bool) -> Dict[str, dict]:
    changes = {}
    # As URLs can be defined before actual usage, maintain a separate dict
    urls = {}
    current_release = {}
    category = []
    for line in change_log:
        line = line.strip(" \n")

        if is_release(line):
            current_release = add_release(changes, line)
            category = current_release.setdefault("uncategorized", [])
        elif is_category(line):
            category = add_category(current_release, line)
        elif is_link(line):
            link_match = link_pattern.fullmatch(line)
            urls[link_match.group(1).lower()] = link_match.group(2)
        elif line:
            add_information(category, line)

    # Add url for each version (create version if not existing)
    for version, url in urls.items():
        changes.setdefault(version, {"metadata": {"version": version}})["metadata"][
            "url"
        ] = url

    # Avoid empty uncategorized
    unreleased_version = None
    for version, current_release in changes.items():
        metadata = current_release["metadata"]
        if not current_release.get("uncategorized"):
            current_release.pop("uncategorized", None)

        # If there is an empty release date, it identify the unreleased section
        if ("release_date" in metadata) and not metadata["release_date"]:
            unreleased_version = version

    if not show_unreleased:
        changes.pop(unreleased_version, None)
    elif "unreleased" not in changes:
        changes["unreleased"] = _unreleased()

    return changes


def from_release(release_dict: dict, version: str) -> str:
    content = ""
    metadata = release_dict["metadata"]
    content += f"\n## [{metadata['version'].capitalize()}]"

    if metadata.get("release_date"):
        content += f" - {metadata['release_date']}"

    uncategorized = release_dict.get("uncategorized", [])
    for category_content in uncategorized:
        content += f"\n* {category_content}"
    if uncategorized:
        content += "\n"
    version_changes = ""
    for category_name, category_content in release_dict.items():
        if category_name in ["metadata", "uncategorized"]:
            continue
        if category_content or version == "unreleased":
            version_changes += f"\n### {category_name.capitalize()}"

            for categorized in category_content:
                version_changes += f"\n- {categorized}"

            version_changes += "\n"
    if version_changes:
        content += "\n"
    content += version_changes
    if not version_changes:
        content += "\n"
    return content


def from_dict(changelog: Dict[str, dict]) -> str:
    content = BASE
    versions = [version for version, _ in to_sorted_semantic(changelog.keys())]
    versions.append("unreleased")  # unreleased shoud be there for this
    for version in reversed(versions):
        content += from_release(changelog[version], version)

    content += "\n"

    for version in reversed(versions):
        current_release = changelog[version]
        metadata = current_release["metadata"]
        if not metadata.get("url"):
            continue

        content += f"[{metadata['version'].capitalize()}]: {metadata['url']}\n"

    return content


def _unreleased(sections: bool = False) -> Dict:
    unreleased = {"metadata": {"version": "unreleased", "release_date": None}}
    if sections:
        unreleased.update({change_type: [] for change_type in TYPES_OF_CHANGE})
    return unreleased


def release(
    changelog: Dict[str, dict], new_version: str = None, sections: bool = False
) -> Optional[str]:
    """
    Release a new version based on changelog unreleased content.

    :param changelog_path: Path to the changelog file.
    :param new_version: The new version to use instead of trying to guess one.
    :return: The new version, None if there was no change to release.
    """
    new_release = changelog["unreleased"].copy()
    metadata = {}
    current_version, current_semantic_version = actual_version(changelog)
    if not new_version:
        metadata["semantic_version"] = bump(new_release, current_semantic_version)
        new_version = from_semantic(metadata["semantic_version"])
    else:
        metadata["semantic_version"] = to_semantic(new_version)
        compare = semantic_order(
            (new_version, metadata["semantic_version"]),
            (current_version, current_semantic_version),
        )
        if compare <= 0:  # input version lower than current (newest) version
            raise InvalidSemanticVersion(new_version)

    if new_version:
        metadata["version"] = new_version
    metadata["release_date"] = datetime.date.today().isoformat()
    new_release.update({"metadata": metadata})
    changelog.update({"unreleased": _unreleased(sections), new_version: new_release})
    return new_version
