class TuxbakeError(Exception):
    """Base class for all Tuxbuild exceptions"""

    error_help = ""
    error_type = ""


class TuxbakeRunCmdError(TuxbakeError):
    error_help = "Process call failed"
    error_type = "Configuration"
