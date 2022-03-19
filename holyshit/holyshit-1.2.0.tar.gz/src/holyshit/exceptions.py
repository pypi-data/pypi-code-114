class ContentUnavailable(Exception):
    """Raises when fetching content fails or type is invalid."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class ClosedSessionError(Exception):
    """Raises when attempting to interact with a closed client instance."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class InvalidEndpointError(Exception):
    """Raises when attempting to access a non-existent endpoint."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
