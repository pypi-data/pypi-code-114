from __future__ import annotations
import sys

from loguru import logger

# Source:
#     https://stackoverflow.com/a/287944/667301
@logger.catch(default=True, onerror=lambda _: sys.exit(1))
class Color:
    """
    Select Graphic Rendition (SGR) color codes...
    https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters
    """

    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    # ORANGE below uses 256-color (8-bit) codes
    ORANGE = "\033[38;2;255;165;1m"
    #              ^^ (38 is Foreground, 48 is Background)

    # Source -> https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
    RED = "\u001b[31m"
    BLACK = "\u001b[30m"
    YELLOW = "\u001b[33m"
    MAGENTA = "\u001b[35m"
    WHITE = "\u001b[37m"

    BRIGHT_RED = "\u001b[31;1m"
    BRIGHT_GREEN = "\u001b[32;1m"
    BRIGHT_YELLOW = "\u001b[33;1m"
    BRIGHT_BLUE = "\u001b[34;1m"
    BRIGHT_MAGENTA = "\u001b[35;1m"
    BRIGHT_CYAN = "\u001b[36;1m"
    BRIGHT_WHITE = "\u001b[37;1m"
    BRIGHT_BLACK = "\u001b[30;1m"

    # Situational color names...
    HEADER = "\033[95m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    # End the colors...
    ENDC = "\033[0m"


C = Color()
