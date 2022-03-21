class SymException(Exception):
    """This is the base class for all exceptions raised by the Sym Runtime.

    Args:
        error_type: The class of exception (used as the first part of the error_code, e.g. AuthenticationError)
        name: The name of the exception (used as the second part of the error_code, e.g. INVALID_JWT)
        message: The exception message to display
    """

    def __init__(self, error_type: str, name: str, message: str):
        self.message = message
        self.error_code = f"{error_type}:{name}"
        super().__init__(self.message)

    def to_dict(self):
        return {
            "error": True,
            "message": self.message,
            "code": self.error_code,
        }
