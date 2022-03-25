"""
MIT License

Copyright (c) 2020-2022 Chris1320

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import sys
import time

from hashlib import blake2b

# from . import info as pinfo  # Package info; to avoid confusion with the info method in Logger() class.

# Try to import an optional package
try:
    from colorama import init as cm_init
    from colorama import Fore as cm_fore
    from colorama import Back as cm_back
    # from colorama import Style as cm_style
    COLORAMA_SUPPORT = True

except ImportError:
    COLORAMA_SUPPORT = False


class Logger():
    """
    The logger class.
    """

    def __init__(self, name: str, logfile: str, **kwargs):
        """
        The initialization method of the Logger() class.

        name         : str,     The name of the logging object.
        logfile      : str,     the path where to write the logs.
        kwargs       : dict,    The keyword arguments.

        Available kwargs:
        autoforget     : bool,    If True, the logger will delete logs on memory when it reaches a specified size. (Default: False)
        logsize        : int,    The number of logs stored in memory before deleting it from memory. (Default: 100)
        mode           : bool,    set to the following modes: (Default: `append`)
            append     :          Append logs to existing file.
            overwrite  :          Overwrite existing file. (Unavailable when `autoforget` is True.)

        loglevel       : int,     Log level to save.
                     1 = Critical
                     2 = Error
                     3 = Warning
                     4 = Info
                     5 = Debug
        memory         : bool,    If True, store logs in memory and manually call `dumpLogs()` to dump to file. (Default: False; False when `autoforget` is True or when mode is `append`.)
        session_id     : str,     The session id of the logger.
        timestamp      : str,     A strftime-compatible format to use. If None, `time.asctime()` is used instead.
        show_output    : bool,    If True, print the logs to the console. (Default: False)
        log_format     : str,     The format of the log.
           {session_id}: The Session ID of the logger object.
           {type}     : The log level/type.
           {timestamp} : The timestamp of the log.
           {message}   : The message of the log.
        max_logfile_sz : float,   (WIP) The maximum size of the logfile in MB. Set to `None` to disable limit. (Default: 10)
        """

        self.name = str(name)
        self.logfile = str(logfile)

        # Get optional parameters from kwargs.
        # * Get autoforget.
        if type(kwargs.get("autoforget", False)) is bool:
            self.autoforget = kwargs.get("autoforget", False)

        else:
            raise ValueError("autoforget must be a boolean.")

        # * Get the maximum log size. (To be used when autoforget is True.)
        self.logsize = int(kwargs.get("logsize", 100))

        # * Get mode.
        if kwargs.get("mode", "append") == "append":
            self.__mode = "append"

        elif kwargs.get("mode", "append") == "overwrite":
            if self.autoforget:
                raise ValueError("`autoforget` is True, mode cannot be set to `overwrite`.")

            self.__mode = "overwrite"

        else:
            raise ValueError("mode must be `append` or `overwrite`.")

        # * Get log level.
        self.loglevel = int(kwargs.get("loglevel", 3))
        if self.loglevel < 1 or self.loglevel > 5:
            raise ValueError("loglevel must be an integer between 1 and 5.")

        # * Get memory.
        if type(kwargs.get("memory", False)) is bool:
            if (self.__mode == "append" or self.autoforget) and kwargs.get("memory", False):
                raise ValueError("`memory` cannot be set to True when `mode` is `append` or `autoforget` is True.")

            else:
                self.memory = kwargs.get("memory", False)

        else:
            raise ValueError("memory must be a boolean.")

        # Format:
        # {
        #     <session 1>: [<logs>],
        #     <session 2>: [<logs>]
        # }

        # * Generate or get new session ID.
        self.__session_id = str(kwargs.get("session_id", self.__generateSessionID()))

        # * Get timestamp format.
        if kwargs.get("timestamp", None) is None:
            self.timestamp_format = None

        else:
            self.timestamp_format = str(kwargs.get("timestamp"))

        # * Set show_output.
        if type(kwargs.get("show_output", False)) is bool:
            self.show_output = kwargs.get("show_output", False)

        else:
            raise ValueError("show_output must be a boolean.")

        if self.show_output:
            if COLORAMA_SUPPORT:
                cm_init()  # Initialize colorama if show_output is True.

        # * Set log_format.
        self.log_format = str(kwargs.get("log_format", ":{type}: [{session_id}] ({timestamp}) {caller} | {message}"))

        # * Set maximum logfile size. (in megabytes)
        if kwargs.get("max_logfile_sz", 10.0) is None:
            self.max_logfile_sz = None

        else:
            self.max_logfile_sz = float(kwargs.get("max_logfile_sz", 10.0))

        self.__session_logs = []  # Create the list that will contain the new logs.
        self.latest_log = None  # The latest log.

        # * Check if logfile already exists.
        if os.path.exists(self.logfile):
            if self.__mode == "append":
                pass

            elif self.__mode == "overwrite":
                with open(self.logfile, 'w') as f:
                    pass  # Remove contents from logfile

            else:
                raise FileExistsError("The logfile already exists.")

    @staticmethod
    def __generateSessionID() -> str:
        """
        Generate a new session ID.

        :returns str: The new session ID.
        """

        return blake2b(str(time.time()).encode()).hexdigest().upper()[:8]

    def __timestamper(self) -> str:
        """
        Return time using <self.timestamp_format>.

        :returns str: The formatted time.
        """

        return time.asctime() if self.timestamp_format is None else str(time.strftime(self.timestamp_format))

    def __write_to_file(self, line: str) -> None:
        """
        Write <line> to a line.

        line: str, the log to write.

        :returns void:
        """

        with open(self.logfile, "a") as file:
            file.write(self._format_log(line))

    def _format_log(self, log: dict) -> str:
        """
        Format the log into a string.

        log: dict, the log in dictionary form.

        :returns str: The string form of the log.
        """

        return "{0}\n".format(self.log_format.format(
            session_id=self.__session_id,
            type=log["type"].upper(),
            timestamp=log["timestamp"],
            message=log["msg"],
            caller=f"{log['caller']}()"
        ))

    def __sizeWatcher(self) -> None:
        """
        Monitor the size of the logs and save them to file when it reaches the number of specified log size.

        :returns void:
        """

        if self.autoforget:
            if len(self.__session_logs) > self.logsize:
                self.__session_logs.pop(0)  # Clear the oldest session log.

        if self.max_logfile_sz is not None:
            if os.path.exists(self.logfile):
                if os.path.getsize(self.logfile) > self.max_logfile_sz * 1024 * 1024:
                    # ? Is this too much to process?
                    # FIXME: This algorithm degrades performance SIGNIFICANTLY.
                    with open(self.logfile, 'r') as f:
                        logs = f.readlines()  # Get ALL logs from the file.

                    with open(self.logfile, 'w') as f:
                        for i in range(0, len(logs) - 1):
                            if i != 0:  # Don't write the oldest log. (Which is located at the top of the file)
                                f.write(logs[i])

    def dumpLogs(self) -> None:
        """
        Manually dump <self.__session_logs> to <self.logfile>.
        Raises a PermissionError when self.memory is False.

        :returns void:
        """

        if not self.memory:
            raise PermissionError("self.memory is not True, logs are automatically written to logfile.")

        if self.__mode == "append":
            mode = 'a'

        elif self.__mode == "overwrite":
            mode = 'w'

        else:
            raise ValueError("Invalid mode.")

        with open(self.logfile, mode) as f:
            for log in self.__session_logs:
                f.write(self._format_log(log))

    def flushLogs(self) -> None:
        """
        Manually clear session logs from memory.
        Raises a PermissionError when self.memory is False.

        :returns void:
        """

        if not self.memory:
            raise PermissionError("self.memory is not True. `autoforget` can be used instead.")

        self.__session_logs = []

    def getLoggerInfo(self) -> dict:
        """
        Return a dictionary containing information about the logger.

        :returns dict:
        """

        return {
            "name": self.name,
            "logfile": self.logfile,

            "autoforget": self.autoforget,
            "logsize": self.logsize,
            "mode": self.__mode,
            "loglevel": self.loglevel,
            "memory": self.memory,
            "session_id": self.__session_id,
            "timestamp": self.timestamp_format,
            "show_output": self.show_output,
            "log_format": self.log_format,
            "stats": {
                "log_size": len(self.__session_logs),
            }
        }

    def getAllLogs(self):
        """
        Return self.__session_logs.

        :returns list:
        """

        return self.__session_logs

    def debug(self, msg: str):
        """
        Log a debug message.

        msg: str, The message to log.

        :returns void:
        """

        if self.loglevel >= 5:  # Check if log will be stored.
            log = {
                "timestamp": self.__timestamper(),
                "type": "debug",
                "msg": msg,
                "caller": sys._getframe(1).f_code.co_name
            }
            if not self.autoforget:
                self.__session_logs.append(log)

            if self.show_output:
                if COLORAMA_SUPPORT:
                    print("{0}[{1}DEBUG{0}] {3}(): {1}{2}{0}".format(cm_fore.RESET, cm_fore.LIGHTBLACK_EX, msg, log["caller"]))

                else:
                    print("[DEBUG] {1}(): {0}".format(msg, log["caller"]))

            if not self.memory:  # If self.memory if False, save to logfile.
                self.__write_to_file(log)

            self.latest_log = log

        self.__sizeWatcher()

    def info(self, msg: str):
        """
        Log an info message.

        msg: str, The message to log.

        :returns void:
        """

        if self.loglevel >= 4:  # Check if log will be stored.
            log = {
                "timestamp": self.__timestamper(),
                "type": "info",
                "msg": msg,
                "caller": sys._getframe(1).f_code.co_name
            }
            self.__session_logs.append(log)

            if self.show_output:
                if COLORAMA_SUPPORT:
                    print("{0}[{1}i{0}] {1}{2}{0}".format(cm_fore.RESET, cm_fore.LIGHTGREEN_EX, msg))

                else:
                    print("[i] {0}".format(msg))

            if not self.memory:  # If self.memory if False, save to logfile.
                self.__write_to_file(log)

            self.latest_log = log

        self.__sizeWatcher()

    def warning(self, msg: str):
        """
        Log a warning message.

        msg: str, The message to log.

        :returns void:
        """

        if self.loglevel >= 3:  # Check if log will be stored.
            log = {
                "timestamp": self.__timestamper(),
                "type": "warning",
                "msg": msg,
                "caller": sys._getframe(1).f_code.co_name
            }
            if not self.autoforget:
                self.__session_logs.append(log)

            if self.show_output:
                if COLORAMA_SUPPORT:
                    print("{0}[{1}!{0}] {1}{2}{0}".format(cm_fore.RESET, cm_fore.LIGHTYELLOW_EX, msg))

                else:
                    print("[!] {0}".format(msg))

            if not self.memory:  # If self.memory if False, save to logfile.
                self.__write_to_file(log)

            self.latest_log = log

        self.__sizeWatcher()

    def error(self, msg: str):
        """
        Log an error message.

        msg: str, The message to log.

        :returns void:
        """

        if self.loglevel >= 2:  # Check if log will be stored.
            log = {
                "timestamp": self.__timestamper(),
                "type": "error",
                "msg": msg,
                "caller": sys._getframe(1).f_code.co_name
            }
            if not self.autoforget:
                self.__session_logs.append(log)

            if self.show_output:
                if COLORAMA_SUPPORT:
                    print("{0}[{1}E{0}] {1}{2}{0}".format(cm_fore.RESET, cm_fore.LIGHTRED_EX, msg))

                else:
                    print("[E] {0}".format(msg))

            if not self.memory:  # If self.memory if False, save to logfile.
                self.__write_to_file(log)

            self.latest_log = log

        self.__sizeWatcher()

    def critical(self, msg: str):
        """
        Log a critical error message.

        msg: str, The message to log.

        :returns void:
        """

        if self.loglevel >= 1:  # Check if log will be stored.
            log = {
                "timestamp": self.__timestamper(),
                "type": "critical",
                "msg": msg,
                "caller": sys._getframe(1).f_code.co_name
            }
            if not self.autoforget:
                self.__session_logs.append(log)

            if self.show_output:
                if COLORAMA_SUPPORT:
                    print("{0}{3}[{1}CRITICAL{0}] {2}{4}".format(cm_fore.RESET, cm_fore.BLACK, msg, cm_back.LIGHTRED_EX, cm_back.RESET))

                else:
                    print("[CRITICAL] {0}".format(msg))

            if not self.memory:  # If self.memory if False, save to logfile.
                self.__write_to_file(log)

            self.latest_log = log

        self.__sizeWatcher()
