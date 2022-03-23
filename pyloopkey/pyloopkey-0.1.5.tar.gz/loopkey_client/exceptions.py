"""Exceptions to be used in loopkey_client directory."""


class AuthenticationError(Exception):
    """Exception raised when authentication failed."""


class BadRequestError(Exception):
    """Exception raised when missing params."""

    def __init__(self, operation, missing):
        super().__init__(f"Error on {operation}. Missing {missing} parameters.")


class OperationError(Exception):
    """Exception raised when operation with 3rd party api fails."""

    status_code = 0

    def __init__(self, operation, error_description, status_code):
        self.status_code = status_code
        super().__init__(f"Error while trying to {operation}: {error_description}")


class NotSupportedError(Exception):
    """Exception raised when operation is not supported."""

    def __init__(self, operation):
        super().__init__(f"Operation error: {operation} not supported.")
