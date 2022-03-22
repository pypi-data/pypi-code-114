from functools import lru_cache

import requests
from diskcache import Cache
from packaging.utils import canonicalize_name


class PyPIAPI:
    """Handy access to the PyPI JSON API."""

    # pylint: disable=too-few-public-methods

    cache = Cache("~/.hdev_pypi_cache", expires=3600 * 5)  # 5 hours expiry time

    """Interface to the PyPI JSON API for getting data about packages."""

    def get(self, project_name):
        """Get details of a specific package."""

        return self._get(canonicalize_name(project_name))

    @lru_cache(1024)
    def _get(self, name):
        try:
            return self.cache[name]
        except KeyError:
            print(f"Getting details from PyPI for: {name}")
            response = requests.get(f"https://pypi.org/pypi/{name}/json", timeout=1)
            response.raise_for_status()

            data = self.cache[name] = response.json()
            return data
