"""
MXS is the Math eXploration Solver.
Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com

The error module provides custom LED Error Classes, as well as an ExitCode
class that supplies exit code values used when exiting the LED program.
Errror messages are available in the LED log file, which is located at
~/.local/log/led.log by default.

In bash, the exit code can be retrieved in the usual manner, by querying
$? after the program exits.

Exit codes for many (most) systems are usually 0 for success and 1 for
general failure.

BSD has attempted to standardize exit codes. These values are usually defined
in /usr/include/sysexits.h on Linux systems.

The codes and their meanings can also be found online at:

https://man.openbsd.org/sysexits.3
"""

from enum import Enum, IntEnum


class ExitCode(IntEnum):
    """Enumeration of exit codes.

    This class implements POSIX error codes, as found in
    /usr/include/sysexits.h on the Linux platform and
    described in the manual page for sysexit on BSD systems,
    including Darwin (macOS).

    Additional information is availble from The Linux Documnetation Project
    at http://tldp.org/LDP/abs/html/exitcodes.html
    """
    EX_SUCCESS = 0  # command exits successfully
    EX_GENERAL = 1  # catchall for general errors
    EX_USAGE = 64  # command line usage error
    EX_DATAERR = 65  # data format error
    EX_NOINPUT = 66  # cannot open input
    EX_NOUSER = 67  # addressee unknown
    EX_NOHOST = 68  # host name unknown
    EX_UNAVAILABLE = 69  # service unavailable
    EX_SOFTWARE = 70  # internal software error
    EX_OSERR = 71  # system error (e.g., can't fork)
    EX_OSFILE = 72  # critical OS file missing
    EX_CANTCREAT = 73  # can't create (user) output file
    EX_IOERR = 74  # input/output error
    EX_TEMPFAIL = 75  # temp failure; user is invited to retry
    EX_PROTOCOL = 76  # remote error in protocol
    EX_NOPERM = 77  # permission denied
    EX_CONFIG = 78  # configuration error
    EX_SIGINT = 130  # keyboard interrupt


class MXSError(Exception):
    """Base class for exceptions in this package."""
    pass
