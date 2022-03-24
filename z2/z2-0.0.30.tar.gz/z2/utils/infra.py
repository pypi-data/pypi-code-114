#from z2.process import run, im
from six.moves import input as _input

from loguru import logger as loguru_logger

def six_input(message=""):
    """A better input() than stdlib input()"""
    # https://stackoverflow.com/a/56373231/667301
    return _input(message)

class LogIt:
    """Modest loguru hack to indent the log message based on log level_id."""

    def __init__(self):
        ## Shortcut for loguru.logger.log()...
        self.level_id = "TRACE"  # <---- loguru requires a real level_id name

    def _log_hack(self, message):
        assert isinstance(self.level_id, str)
        assert isinstance(message, str)
        #return logger.log(level_id=self.level_id, message=message)
        return loguru_logger.log(self.level_id, "|"+message)

    def trace(self, message=None):
        raise NotImplementedError("FIXME - Something about loguru.logging.log.trace() is broken")
        assert isinstance(message, str)
        self.level_id = "TRACE"
        indent = 6
        return self._log_hack(message=indent*" " + message)

    def debug(self, message=None):
        assert isinstance(message, str)
        self.level_id = "DEBUG"
        indent = 5
        return self._log_hack(message=indent*" " + message)

    def info(self, message=None):
        assert isinstance(message, str)
        self.level_id = "INFO"
        indent = 4
        return self._log_hack(message=indent*" " + message)

    def success(self, message=None):
        assert isinstance(message, str)
        level = "SUCCESS"
        indent = 3
        return self._log_hack(message=indent*" " + message)

    def warning(self, message=None):
        assert isinstance(message, str)
        self.level_id = "WARNING"
        indent = 2
        return self._log_hack(message=indent*" " + message)

    def error(self, message=None):
        assert isinstance(message, str)
        self.level_id = "ERROR"
        indent = 1
        return self._log_hack(message=indent*" " + message)

    def critical(self, message=None):
        assert isinstance(message, str)
        self.level_id = "CRITICAL"
        indent = 0
        return self._log_hack(message=indent*" " + message)
