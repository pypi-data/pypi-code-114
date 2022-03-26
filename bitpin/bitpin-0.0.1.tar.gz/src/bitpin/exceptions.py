import typing as t


__all__ = [
    'BitpinExceptions',
    'RequestsExceptions',
    'RequestTimeout',
    'InvalidToken',
    'InvalidResponse',
    'StatusCodeError',
    'JSONDecodingError'
]


class BitpinExceptions(Exception):
    def __init__(
            self, func_name: str, message: t.Union[str, t.Type[Exception], Exception], *args, **kwargs
    ):
        """
        Base exception class for Bitpin.

        :param func_name: function name that raise exception
        :type func_name: str

        :param message: message of exception
        :type message: str | Exception

        :param args: args of exception
        :type args: t.Any

        :param kwargs: kwargs of exception
        :type kwargs: t.Any

        :return: None
        :rtype: None
        """

        self.__func_name = func_name
        self.__message = str(message)
        self.__args = args
        self.__kwargs = kwargs
        super().__init__(self.__message)

    def __str__(self):
        __str = f'[{self.__func_name}] -> {self.__message}'

        if self.__args:
            __str += f' | Args: {self.args}'
        if self.__kwargs:
            __str += f' | Kwargs: {self.__kwargs}'

        return __str


class RequestsExceptions(BitpinExceptions):
    """ Exception class for requests error. """


class RequestTimeout(RequestsExceptions):
    """ Exception class for requests timeout error. """


class InvalidToken(RequestsExceptions):
    """ Exception class for invalid token error. """


class ProcessExceptions(BitpinExceptions):
    """ Exception class for process error. """


class StatusCodeError(ProcessExceptions):
    """ Exception class for status code error. """


class JSONDecodingError(ProcessExceptions):
    """ Exception class for json decode error. """


class InvalidResponse(ProcessExceptions):
    """ Exception class for invalid response error. """
