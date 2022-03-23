from typing import Any

from .exception import WrongReturnCodeError, ResultFormatError


class ValueObject:
    def __init__(self, value=None):
        self.value = value
        self.is_writable = True
        self.is_changeable = True
        self.is_unique = False
    
    def get_value(self):
        return self.value

    def set_unique(self, is_unique=False):
        self.is_unique = is_unique
        return self

    def set_changeable(self, is_changeable=False):
        self.is_changeable = is_changeable
        return self

class Page(ValueObject):
    def __init__(self, value=None, page_size=10):
        super().__init__(value)
        if value is None:
            self.value = 0
        self.page_size = page_size


class ID(ValueObject):
    def __init__(self, value=None):
        super().__init__(value)
        self.is_writable = False
        self.is_changeable = False
        self.is_unique = True

class ReturnCode(ValueObject):
    SUCCEED_CODE = 0
    NOT_EXIST_CODE = 1
    ALREADY_EXIST_CODE = 2
    FORMAT_CODE = 3
    PARAMETER_CODE = 4
    NULL_CODE = 5
    OPERATION_CODE = 6
    VALUE_CODE = 7
    OTHER_CODE = 8
    def __init__(self, value=None):
        if value is None:
            self.value = self.SUCCEED_CODE
        else:
            super().__init__(value)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name=='value' and (__value>8 or __value<0):
            raise WrongReturnCodeError(f'Wrong return code: {__value}')
        return super().__setattr__(__name, __value)

class Result(ValueObject):
    def __init__(
        self, 
        value=None, 
        succeed=True, 
        return_code:ReturnCode=ReturnCode(), 
        error_info=None,
        error_traceback=None
    ):
        super().__init__(value)
        self.error_info=error_info
        self.error_traceback = error_traceback
        self.succeed = succeed
        self.return_code = return_code

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'error_info' and __value is not None and self.value is not None:
            raise ResultFormatError('If error_info is not none, then value must be none')
        return super().__setattr__(__name, __value)

    def get_value(self):
        return self.value

    def get_return_code(self):
        return self.return_code.get_value()