"""Jinja templating helpers."""

from functools import lru_cache


@lru_cache(1)
def get_jinja_env():
    """Get a singleton Jinja2 environment for templating."""

    # pylint: disable=import-outside-toplevel
    from jinja2 import Environment, PackageLoader

    return Environment(loader=PackageLoader("hdev", package_path="resources/templates"))
