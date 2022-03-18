from msvcrt import putwch, getwch
from warnings import warn
from .exception import FunctionNotSupportWarning
def stdout(*text: str) -> None:
    """
    Put text to the console.
    :param text: The text to be shown.
    :type text: str
    """
    for t in text:
        if len(t) == 1:
            putwch(t)
        else:
            for c in t:
                putwch(c)
def backspace(count: int = 1) -> None:
    """
    Delete text on the console.
    Warning: count MUST bigger than 1!
    :param count: How many texts do you want to delete.
    :type count: int
    """
    if count < 1:
        raise ValueError("count MUST bigger than 1!")
    for _ in range(count):
        putwch('\b')
    for _ in range(count):
        putwch(' ')
    for _ in range(count):
        putwch('\b')
def stdin(prompt: str = "", echoChar: str = None) -> str:
    """
    Read what user typed.
    :param prompt: Show the prompt.
    :type prompt: str
    :param echoChar: If you want to show a single char when user was typing.
    :type echoChar: str
    :return: The text that the user typed.
    """
    warn(FunctionNotSupportWarning(
        "This Function Do Not Support Key 'Ctrl-V'."
        ),
        stacklevel=5
    )
    stdout(prompt)
    s = ''
    if echoChar is not None:
        if isinstance(echoChar, str):
            if len(echoChar) > 1:
                echoChar = echoChar[:1]
            elif not len(echoChar):
                echoChar = -1
        else:
            try:
                echoChar = str(echoChar)
                if len(echoChar) > 1:
                    echoChar = echoChar[:1]
                elif not len(echoChar):
                    echoChar = -1
            except:
                echoChar = None
    while True:
        c = getwch()
        if c == '\r' or c == '\n':
            break
        if c == '\003':
            raise KeyboardInterrupt
        if c == '\b':
            s = s[:-1]
            if len(s) >= 1:
                backspace()
        else:
            s = s + c
            if echoChar is not None:
                putwch(echoChar)
            elif echoChar != -1:
                putwch(c)
    stdout('\r\n')
    return s