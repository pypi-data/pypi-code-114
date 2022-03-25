"""
Warning:

    This module and its submodules are deprecated, import its symbols directly from :mod:`atoti` if ``atoti`` is installed and from :mod:`atoti-query <atoti_query>` otherwise.
"""

from atoti_core import deprecated
from atoti_query import (
    Auth as Auth,
    BasicAuthentication,
    ClientCertificate as ClientCertificate,
    TokenAuthentication,
)


def create_basic_authentication(username: str, password: str) -> Auth:
    """
    Warning:

        This function is deprecated, use :class:`atoti_query.BasicAuthentication` instead.
    """
    deprecated(
        "`create_basic_authentication()` is deprecated, use `BasicAuthentication` instead."
    )
    return BasicAuthentication(username=username, password=password)


def create_token_authentication(token: str) -> Auth:
    """
    Warning:

        This function is deprecated, use :class:`atoti_query.TokenAuthentication` instead.
    """
    deprecated(
        "`create_token_authentication()` is deprecated, use `TokenAuthentication` instead."
    )
    return TokenAuthentication(token=token)
