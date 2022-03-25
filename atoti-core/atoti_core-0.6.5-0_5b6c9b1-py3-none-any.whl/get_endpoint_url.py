from typing import Collection, Literal, Optional
from urllib.parse import urljoin

from .server_versions import ServerVersions

_SUPPORTED_PIVOT_VERSIONS = ("4", "5", "6")


def _get_supported_version_index(
    server_versions: ServerVersions,
    *,
    namespace: str,
    supported_versions: Collection[str],
) -> int:
    exposed_versions = [
        version["id"] for version in server_versions["apis"][namespace]["versions"]
    ]

    try:
        return next(
            index
            for index, version in enumerate(exposed_versions)
            if version in supported_versions
        )
    except StopIteration as error:
        raise RuntimeError(
            f"Exposed {namespace} versions: {exposed_versions} don't match the supported ones: {supported_versions}."
        ) from error


def get_endpoint_url(
    *,
    session_url: str,
    namespace: str,
    route: str,
    server_versions: ServerVersions,
    attribute_name: Literal["restPath", "wsPath"] = "restPath",
    version_index: Optional[int] = None,
) -> str:
    if not session_url.endswith("/"):
        session_url = f"{session_url}/"

    if attribute_name == "wsPath":
        session_url = session_url.replace("http", "ws", 1)

    version_index = (
        _get_supported_version_index(
            server_versions,
            namespace="pivot",
            supported_versions=_SUPPORTED_PIVOT_VERSIONS,
        )
        if namespace == "pivot"
        else version_index
    )

    path = next(
        server_api["versions"][version_index or 0].get(attribute_name)
        for name, server_api in server_versions["apis"].items()
        if name == namespace
    )

    if path is None:
        raise RuntimeError(
            f"Missing {attribute_name} for {namespace} namespace of {session_url}."
        )

    return urljoin(session_url, f"{path.lstrip('/')}/{route}")
