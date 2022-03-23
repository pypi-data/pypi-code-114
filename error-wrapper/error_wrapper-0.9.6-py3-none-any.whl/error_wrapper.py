""" Base error wrapping classes"""

import logging
from typing import Optional

ERROR_STATUS_DETAIL_PREFIX = 'Error: '
ERROR_STATUS_NO_ERRORS = 'No errors'
UNDEFINED_ERROR_DETAIL = 'Undefined error!'
EXCEPTION_NAME_POSTFIX = ': '


class BaseErrorWrapper:
    """
    Base error wrapper that allows class methods to share the operation execution state flag,
    and to handle errors and exceptions in a uniform way
    """
    _error: bool = False
    _error_detail: Optional[str] = None
    _exception_name: Optional[str] = None
    _report_prefix: Optional[str] = None
    _exception_name_in_detail: bool = False

    def __init__(self, report_prefix: str = None, exception_name_in_detail: bool = False):
        if report_prefix is not None:
            self._report_prefix = report_prefix
        self._exception_name_in_detail = exception_name_in_detail

    @property
    def error_status(self) -> str:
        """
        Returns current error status as string
        """
        if self._error:
            result = f'{ERROR_STATUS_DETAIL_PREFIX}{self._error_detail}'
        else:
            result = ERROR_STATUS_NO_ERRORS
        return result

    def __str__(self):
        return self.error_status

    def clear_instance_error(self):
        """
        Clear all error related fields and flags
        """
        self._error = False
        self._error_detail = None
        self._exception_name = None

    def raise_instance_error(self, message: Optional[str]):
        """
        Raise instance error with message
        """
        self._error = True
        self._error_detail = self._report_prefix or ''
        self._error_detail += message or UNDEFINED_ERROR_DETAIL

    def raise_instance_exception(self, exception: Exception):
        """
        Raise instance error from exception
        """
        self._error = True
        self._exception_name = exception.__class__.__name__
        self._error_detail = self._report_prefix or ''
        if self._exception_name_in_detail:
            self._error_detail += f'{self._exception_name}{EXCEPTION_NAME_POSTFIX}'
        self._error_detail += exception.__str__()

    @property
    def error(self) -> bool:
        """
        Returns error flag
        """
        return self._error

    @property
    def error_detail(self) -> str:
        """
        Returns error detail text
        """
        return self._error_detail

    @property
    def exception_name(self) -> str:
        """
        Returns triggered exception name
        """
        return self._exception_name


class ErrorWrapper(BaseErrorWrapper):
    """
    Adding uniform automatic logging capability
    """
    _logger: Optional[logging.Logger]
    _auto_logging: bool = False

    def __init__(self, report_prefix: str = None,
                 exception_name_in_detail: bool = False,
                 logger: Optional[logging.Logger] = None,
                 auto_logging: bool = False):
        super().__init__(report_prefix, exception_name_in_detail)
        if logger is not None:
            self._logger = logger
        self._auto_logging = auto_logging

    def write_log(self):
        """
        Write error detail text to log if logger defined
        """
        if self._logger is not None:
            self._logger.error(self.error_detail)

    def raise_instance_error(self, message: Optional[str]):
        """
        Raise instance error with message. Auto logging if auto_logging=True and logger defined
        """
        super().raise_instance_error(message)
        if self._auto_logging:
            self.write_log()

    def raise_instance_exception(self, exception: Exception):
        """
        Raise instance error from exception. Auto logging if auto_logging=True and logger defined
        """
        super().raise_instance_exception(exception)
        if self._auto_logging:
            self.write_log()

    @property
    def auto_logging(self) -> bool:
        """
        Returns auto logging flag
        """
        return self._auto_logging

    @auto_logging.setter
    def auto_logging(self, value: bool):
        """
        Sets auto logging flag
        """
        self._auto_logging = value


def run_method_if_no_errors(func):
    """
    Wrapper for methods that checks self.error before execution
    """
    # pylint: disable=R
    def func_wrapper(self, *args, **kwargs):
        if self.error:
            return
        else:
            func(self, *args, **kwargs)
    return func_wrapper
