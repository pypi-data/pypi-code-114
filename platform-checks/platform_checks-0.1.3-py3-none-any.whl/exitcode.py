#   -------------------------------------------------------------
#   Platform checks - exit codes
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Exit codes for Nagios / NRPE
#   License:        Trivial work, not eligible to copyright
#   -------------------------------------------------------------


OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3


def ok_or_critical(is_successful):
    return OK if is_successful else CRITICAL


def ok_or_warning(is_successful):
    return OK if is_successful else WARNING
