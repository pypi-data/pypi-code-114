from contextlib import contextmanager
from typing import Callable, Dict, Optional


@contextmanager
def dummy_credential_manager(
    *,
    image: str,
    registry_credentials: Optional[Dict],
    log_status: Callable
):
    """
    Credential context manager that does nothing.

    This can used when no credentials are included.
    """
    yield


def get_dummy_credential_manager():
    """
    Construct a dummy credential manager without having to think about arguments.
    """
    return dummy_credential_manager(image="", registry_credentials=None, log_status=lambda s: None)
