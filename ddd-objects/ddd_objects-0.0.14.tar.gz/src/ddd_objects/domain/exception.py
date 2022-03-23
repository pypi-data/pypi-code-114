class BaseError(Exception):
    def __init__(self, error_info:str, return_code: int, *args: object) -> None:
        '''
        return_code 与 value_obj中的ReturnCode相对应
        '''
        super().__init__(error_info, *args)
        self.return_code = return_code

class NotExistsError(BaseError):
    def __init__(self, error_info: str, *args: object) -> None:
        return_code = 1
        super().__init__(error_info, return_code, *args)

class AlreadyExistsError(BaseError):
    def __init__(self, error_info: str, *args: object) -> None:
        return_code = 2
        super().__init__(error_info, return_code, *args)

class FormatError(BaseError):
    def __init__(self, error_info: str, *args: object) -> None:
        return_code = 3
        super().__init__(error_info, return_code, *args)

class ParameterError(BaseError):
    def __init__(self, error_info: str, *args: object) -> None:
        return_code = 4
        super().__init__(error_info, return_code, *args)

class NULLError(BaseError):
    def __init__(self, error_info: str, *args: object) -> None:
        return_code = 5
        super().__init__(error_info, return_code, *args)

class OperationError(BaseError):
    def __init__(self, error_info: str, *args: object) -> None:
        return_code = 6
        super().__init__(error_info, return_code, *args)


class ValueError(BaseError):
    def __init__(self, error_info: str, *args: object) -> None:
        return_code = 7
        super().__init__(error_info, return_code, *args)

class OtherError(BaseError):
    def __init__(self, error_info: str, *args: object) -> None:
        return_code = 8
        super().__init__(error_info, return_code, *args)

class IDNotExistError(NotExistsError):
    pass

class UpdateError(OperationError):
    pass

class OverLimitError(ValueError):
    pass

class KeyExistError(AlreadyExistsError):
    pass

class WrongReturnCodeError(Exception):
    pass

class ResultFormatError(FormatError):
    pass