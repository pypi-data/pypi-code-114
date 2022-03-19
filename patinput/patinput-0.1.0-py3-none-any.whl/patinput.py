import sys
from typing import Callable, Union

from patinput import its_win32
from patinput.getch import getch


if its_win32:
    _right_arrow = 77
    _left_arrow = 75
    _del = 83
    _back_space = 8
    _enter = 13
    _check_special_key_1 = lambda b: b == 224
else:
    _right_arrow = 67
    _left_arrow = 68
    _del = 51
    _back_space = 127
    _enter = 13
    _check_special_key_1 = lambda b: b == 27 and getch()[0] == 91 
    

def patinput(
    allowness: Callable[[int, int, str], bool]=lambda a,b,c: True, 
    prompt: str="", 
    default: str="",
    interrupt: Callable[[int, int, str], bool]=lambda a,b,c: False, 
    ends_nl: bool=True
) -> Union[str, None]:
    """
    This function gets input from standard input, like the input function. Furthermore, this function received a defined pattern 
    and force user to enter the input in a defined pattern and restrict entering illegal characters as the input.

    Args:
        allowness (Callable[[int, int, str], bool], optional): 
            A function that determines which character is allowed in defined position and situation. The first argument is 
            the input character's ASCII code. The second one is the position of the cursor and the last one is the input 
            string until that moment. Finally, returns True value if the input character is legal in this state and otherwise 
            returns False value.
            Default to the function returns True always.

        default (str, optional):
            The default value that is pre-typed in input field.
        
        prompt (str, optional):
            If the prompt argument is present, it is written to standard output without a trailing newline.

        interrupt (Callable[[int, int, str], bool], optional): 
            A function that determines when the input getting procedure must interrupt. The first argument is the input 
            character's ASCII code. The second one is the position of the cursor and the last one is the input string until 
            that moment.
            Default to the function returns True always.

        ends_nl (bool, optional): 
            After receiving input from the user, print a new line, if this argument is True. Defaults to True.

    Returns:
        Union[str, None]: Input string that user have entered. If it returns None, it means that was interrupted.
    """

    def simprint(*args, **kwargs):
        """
        A simplified print function that new lines at the end of each printed string and white spaces between strings which 
        were passed as arguments are removed.
        """
        print(*args, **kwargs, end="", sep="")

    if prompt:
        simprint(prompt, flush=True)

    if default:
        cursor_pos = len(default)
        inp = default
        simprint(default, flush=True)
    else:
        cursor_pos = 0
        inp = ""
        
    while True:
        b = getch()
        b = b[0]
        if interrupt(b, cursor_pos, inp):
            return None
        if b == _enter:  # Enter
            if ends_nl:
                print()
            return inp
        elif b == _back_space:  # Backspace
            if cursor_pos > 0:
                addition = inp[cursor_pos:]
                simprint(
                    "\033[1D",  # backward
                    "\033[0K",  # remove line
                    addition,  # inp[cursor_pos:]
                )
                if len(addition) > 0:
                    simprint(f"\033[{len(addition)}D")  # move cursor to original position
                inp = inp[:cursor_pos-1] + inp[cursor_pos:]
                cursor_pos -= 1
        elif _check_special_key_1(b):  # Arrow keys
            b = getch()[0]
            if b == _right_arrow:  # Right
                if cursor_pos < len(inp):
                    simprint("\033[1C")
                    cursor_pos += 1
            elif b == _left_arrow:  # Left
                if cursor_pos > 0:
                    simprint("\033[1D")
                    cursor_pos -= 1
            elif b == _del:  # Del
                if cursor_pos < len(inp):
                    addition = inp[cursor_pos+1:]
                    simprint(
                        "\033[0K",  # remove line
                        addition,  # inp[cursor_pos+1:]
                        f"\033[{len(addition)}D",  # move cursor to original position
                    )
                    inp = inp[:cursor_pos] + addition
            else:
                continue
        elif b >= 32 and b <= 255 and allowness(b, cursor_pos, inp):
            char = chr(b)
            addition = inp[cursor_pos:]
            simprint(char, addition)
            if len(addition) > 0:
                simprint(f"\033[{len(addition)}D")
            inp = inp[:cursor_pos] + char + inp[cursor_pos:]
            cursor_pos += 1
        sys.stdout.flush()

