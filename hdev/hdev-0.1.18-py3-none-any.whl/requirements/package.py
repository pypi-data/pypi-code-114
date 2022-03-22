"""Methods for discovering information about packages."""

import re
from functools import cached_property, lru_cache

from packaging.markers import default_environment
from packaging.requirements import Requirement
from packaging.utils import canonicalize_name
from packaging.version import InvalidVersion, Version


@lru_cache(1)
def _package_info():
    # pylint: disable=import-outside-toplevel
    import json

    import importlib_resources

    # Info we've gathered manually
    return json.loads(
        importlib_resources.files("hdev.resources.data")
        .joinpath("packages.json")
        .read_bytes()
    )


@lru_cache(1)
def _pypi_api():
    # pylint: disable=import-outside-toplevel
    from hdev.requirements.pypi_api import PyPIAPI

    return PyPIAPI()


class Package(Requirement):
    """A python package with handy metadata access."""

    _data = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # A store of what types of requirement context we've been used in
        self.requirement_types = set()

        self.canonical_name = canonicalize_name(self.name)

    @property
    def info(self):
        return self.get_data()["info"]

    @property
    def releases(self):
        return self.get_data()["releases"]

    def get_data(self):
        if self._data is None:
            self._data = _pypi_api().get(self.name)

        return self._data

    @cached_property
    def requirements(self):
        """Get the install requirements of this package."""
        return self.get_requirements()

    def get_requirements(self, req_type=None):
        """Get specific types of requirements (like "tests")."""
        requires = self.info["requires_dist"]

        if not requires:
            return []

        env = default_environment()
        env["extra"] = req_type

        reqs = []
        for item in requires:
            req = Package(item)
            if req.marker is None or req.marker.evaluate(env):
                reqs.append(req)

        return reqs

    @cached_property
    def latest_release(self):
        """Get details of the latest release of this package."""

        # Something in requests or JSON parsing is discarding the order given
        # to us by PyPI. This means the versions end up sorted in lexical order
        # so  1.1, 1.10, 1.9 ...

        last_version = None

        for version_string in self.releases.keys():
            try:
                version = Version(version_string)
            except InvalidVersion:
                continue

            if not last_version or version >= last_version:
                last_version = version

        if not last_version:
            raise ValueError("No suitable release found")

        return last_version, self.releases[str(last_version)]

    @cached_property
    def python_versions(self):
        """Get the supported python versions."""

        return self._sorted_version_list(
            self.declared_versions + self.implied_versions + self.known_versions
        )

    @cached_property
    def undeclared_versions(self):
        """Get a list of inferred (but not declared) versions."""

        return self._sorted_version_list(
            set(self.python_versions) - set(self.declared_versions)
        )

    @cached_property
    def declared_versions(self):
        """Get version information from the declared classifiers."""

        return self._sorted_version_list(self._declared_versions())

    def _declared_versions(self):
        for classifier in self.info["classifiers"]:
            parts = classifier.split(" :: ")

            # We are looking for:
            # ["Programming Language", "Python", <VERSION> ]
            # ["Programming Language", "Python", <VERSION>, "Only" ]

            if (
                len(parts) < 3
                or parts[0] != "Programming Language"
                or parts[1] != "Python"
            ):
                continue

            try:
                yield Version(parts[2])
            except InvalidVersion:
                continue

    _PYTHON_CODE_REGEX = re.compile(r"^(?:cp|pp)(\d\d\d?)$")
    _PYTHON_MINIMUM_REGEX = re.compile(r">=(\d.\d+)")

    @cached_property
    def implied_versions(self):
        """Get version information based on the compiled wheels."""

        _package_version, dists = self.latest_release

        versions = []

        for dist in dists:
            # Imply support for a version of python from minimum requirements
            if requires := dist["requires_python"]:
                for match in self._PYTHON_MINIMUM_REGEX.findall(requires):
                    versions.append(match)

            # Try and guess the version from the declared python version
            python_version = dist["python_version"]

            if match := self._PYTHON_CODE_REGEX.match(python_version):
                digits = match.group(1)
                versions.append(f"{digits[0]}.{digits[1:]}")
            else:
                if "py2" in python_version:
                    versions.append("2")
                if "py3" in python_version:
                    versions.append("3")

        return self._sorted_version_list(versions)

    @cached_property
    def known_versions(self):
        """Get version information based on our hand curated information."""

        if info := _package_info().get(self.canonical_name):
            return self._sorted_version_list(info["python_versions"].keys())

        return []

    def max_python_version(self, method="python", default="???"):
        values = getattr(self, f"{method}_versions")
        if not values:
            return default

        return values[-1]

    _URL_LOCATIONS = {
        "package_url": "Package",
        "project_url": "Project",
        "release_url": "Release",
        "home_page": "Homepage",
    }
    _GITHUB_REGEX = re.compile(r"^(https://github\.com/[^/]+/[^/]+/?).*", re.IGNORECASE)

    @cached_property
    def urls(self):
        """Get urls associated with the package."""

        urls = {}

        for location, description in self._URL_LOCATIONS.items():
            if url := self.info.get(location):
                urls[url] = description

        if project_urls := self.info.get("project_urls"):
            for description, url in project_urls.items():
                urls[url] = description

        urls[f"https://pypi.org/project/{self.name}/"] = "PyPI"
        urls[f"https://snyk.io/advisor/python/{self.name}"] = "Health"

        for url in urls:
            if match := self._GITHUB_REGEX.match(url):
                urls[match.group(1)] = "Github"
                break

        return {description: url for url, description in urls.items()}

    def as_dict(self):
        """Get a pure data version suitable for serialisation."""

        def string_list(items):
            return [str(i) for i in items]

        return {
            "name": self.canonical_name,
            "urls": self.urls,
            "python_versions": {
                "all": string_list(self.python_versions),
                "known": string_list(self.known_versions),
                "declared": string_list(self.declared_versions),
                "implied_versions": string_list(self.implied_versions),
            },
            "requirement_types": list(self.requirement_types),
        }

    @classmethod
    def _sorted_version_list(cls, items):
        unique = set(
            item if isinstance(item, Version) else Version(item) for item in items
        )

        return list(sorted(unique))

    def __eq__(self, other):
        if not isinstance(other, Package):
            return False

        return str(self) == str(other)
