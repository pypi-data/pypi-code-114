from __future__ import annotations
import termios
import fcntl
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

#     Ref -> https://stackoverflow.com/a/7259460/667301
def getchar(prompt_text="", allowed_chars=None):
    """
    Read a single character from the user

    Parameters
    ----------
    - `prompt_text` can be a message before reading user input
    - `allowed_chars` can be a `set({})` of allowed characters
    """
    assert isinstance(prompt_text, str)
    fd_stdin = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd_stdin)
    newattr = termios.tcgetattr(fd_stdin)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd_stdin, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd_stdin, fcntl.F_GETFL)
    fcntl.fcntl(fd_stdin, fcntl.F_SETFL, oldflags)

    # print("something", end="") end param ensures there's no automatic newline
    #     Ref -> https://stackoverflow.com/a/493399/667301
    # Sometimes you need flush() to make the print() render
    if isinstance(prompt_text, str) and (prompt_text != ""):
        print(prompt_text, end="")
        sys.stdout.flush()

    try:
        while True:
            try:
                single_char = sys.stdin.read(1)
                # Check whether the char is in `allowed_chars`...
                if isinstance(allowed_chars, set):
                    if (single_char in allowed_chars):
                        break

                # break, if allowed_chars is not a `set({})`...
                elif not isinstance(allowed_chars, set):
                    break
            except IOError:
                pass
    finally:
        termios.tcsetattr(fd_stdin, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd_stdin, fcntl.F_SETFL, oldflags)

    if isinstance(prompt_text, str) and (prompt_text != ""):
        print("")   # Move the cursor back to the far-left of terminal...
        sys.stdout.flush()

    return single_char


C = Color()
