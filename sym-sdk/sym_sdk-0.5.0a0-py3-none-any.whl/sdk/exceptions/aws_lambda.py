from sym.sdk.exceptions.sym_exception import SymException


class AWSLambdaError(SymException):
    """This is the base class for all AWS Lambda exceptions raised by the Sym Runtime.

    Args:
        name: The name of the exception (used as the second part of the error_code, e.g. FATAL_FUNCTION_ERROR)
        message: The exception message to display
    """

    def __init__(self, name: str, message: str):
        super().__init__(error_type="AWSLambda", name=name, message=message)
