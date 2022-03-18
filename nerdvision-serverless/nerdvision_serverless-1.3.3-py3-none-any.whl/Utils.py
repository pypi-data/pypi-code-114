import sys
import time
import uuid


class Utils(object):

    @staticmethod
    def is_python_3():
        return sys.version_info[0] == 3

    @staticmethod
    def generate_uid():
        return uuid.uuid4().hex

    @staticmethod
    def time_ms():
        return int(round(time.time() * 1000))

    @staticmethod
    def exc_info_from_exception(error):
        """
        Gets the type, value and traceback from a exception.
        Returns none if the passed in type is not an exception
        or there is no traceback.

        Provided by https://github.com/getsentry/sentry-python

        :param error: the exception to retrieve the data from
        :return exc_type: the type of exception
        :return exc_value: the value of the exception
        :return tb: the traceback from the exception
        """

        if isinstance(error, tuple) and len(error) == 3:
            exc_type, exc_value, tb = error
        elif isinstance(error, BaseException):
            tb = getattr(error, "__traceback__", None)
            if tb is not None:
                exc_type = type(error)
                exc_value = error
            else:
                # Python 2 sometimes does not have a traceback so we patch in the system traceback
                return Utils.exc_info_from_exception((type(error), error, sys.exc_info()[2]))
        else:
            return None

        return exc_type, exc_value, tb
