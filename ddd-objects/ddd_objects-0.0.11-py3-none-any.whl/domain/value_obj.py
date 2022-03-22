from typing import Any

from objects.domain.exception import ResultFormatError


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


class Result(ValueObject):
    def __init__(self, value=None, error_info=None):
        super().__init__(value)
        self.error_info=error_info
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'error_info' and __value is not None and self.value is not None:
            raise ResultFormatError('If error_info is not none, then value must be none')
        return super().__setattr__(__name, __value)

class AOResult(Result):
    pass
