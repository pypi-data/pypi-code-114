from sym.sdk.exceptions.sym_exception import SymException


class SlackError(SymException):
    """This is the base class for all SlackErrors.

    Args:
        name: The name of the exception (used as the second part of the error code, e.g. NOT_IN_CHANNEL
        message: The exception message to display
    """
