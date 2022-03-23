"""Functions for my_traceback subpackage."""

from __future__ import annotations
from typing import Type, Sequence
import traceback as traceback_module
import sys
from types import TracebackType
import textwrap

from typing_extensions import Literal

from ..str_formating import format_str
from ..colors.colors_module import colors_config, colorize_traceback
from ..str_formating import format_str

sys_hook_backup = sys.excepthook


def raise_enhanced(
    exception_type: Type[Exception],
    value: BaseException | None,
    traceback: None | TracebackType,
    clean_debug_extra: bool = True,
    highlight: bool = True,
    indent: int = 2,
) -> None:
    """Enhance printed exception.

    Message as well as traceback. It adds colors if configured. You can call
    it directly. This function can be directly assigned to sys.excepthook.

    Args:
        exception_type (Type[Exception]): E.g. <class 'RuntimeError'>.
        value (BaseException | None): E. g. RuntimeError.
        traceback (None | TracebackType): Traceback.
        clean_debug_extra (bool, optional): There can be some extra lines of stack trace for example when
            debugging. This will remove those lines. E.g. lines from VS Code python extension or runpy.py.
            Defaults to True.
        highlight (bool, optional): Highlight main message from the error. Defaults to True.
        indent (int, optional): Whether indent raised message or not. Defaults to 2.

    """
    traceback_list = traceback_module.format_exception(exception_type, value, traceback)

    if clean_debug_extra:
        traceback_list = remove_debug_stack_trace(traceback_list)

    traceback_str = ""
    for i in traceback_list:
        traceback_str = traceback_str + i

    traceback_str = colorize_traceback(traceback_str)

    if indent:
        traceback_str = textwrap.indent(text=traceback_str, prefix=" " * indent)

    if str(value) and highlight:
        traceback_str = traceback_str.rstrip()[: traceback_str.rstrip().rfind("\n")]

        traceback_str = traceback_str + format_str(
            str(value), caption=exception_type.__name__, indent=2 * indent
        )

    print(f"\n\n{traceback_str}")


def enhance_excepthook():
    """Change default excepthook to formatted one.

    That means that if there is a uncaught raise, output message with traceback will be colored if
    possible.
    """
    sys.excepthook = raise_enhanced


def enhance_excepthook_reset():
    """Reset original excepthook."""
    sys.excepthook = sys_hook_backup


def get_traceback_str_with_removed_frames(lines: Sequence[str], exact_match: bool = True) -> str:
    """Remove particular levels of stack trace defined by content.

    Note:
        If not using exact_match, beware of not using short message that can be also elsewhere, where not
        supposed, as it can make debugging a nightmare.

    Args:
        lines (list): Line in call stack that we want to hide.
        exact_match (bool, optional): If True, stack frame will be removed only if it is exactly the same.
            If False, then line can be just subset of stack frame.

    Returns:
        str: String traceback ready to be printed.

    Example:
        >>> def buggy():
        ...     return 1 / 0
        ...
        >>> try:
        ...     buggy()
        ... except ZeroDivisionError:
        ...     traceback = get_traceback_str_with_removed_frames([])
        ...     traceback_cleaned = get_traceback_str_with_removed_frames(["buggy()"])
        >>> "buggy()" in traceback
        True
        >>> "buggy()" not in traceback_cleaned
        True

    """
    exc = traceback_module.TracebackException(*sys.exc_info())  # type: ignore

    if exact_match:
        for i in exc.stack[:]:
            if i.line in lines:
                exc.stack.remove(i)

    else:
        for i in exc.stack[:]:
            for j in lines:
                if i.line and i.line in j:
                    exc.stack.remove(i)

    return "".join(exc.format())


def remove_debug_stack_trace(traceback_list: list[str]) -> list[str]:
    """On windows when debugging (at least in VS Code) caught stack trace from raise function contain extra
    files not used by user or imported library. All the extra lines come from runpy.py. This will remove such
    a lines so the error is more readable.

    Args:
        traceback_list (list[str]): List of stack trace messages.

    Returns:
        str: Returns actual list of strings without extra runpy.py content.
    """
    clean_tracebacks = []

    for i in traceback_list:
        if not any([pattern in i for pattern in ["extensions\\ms-python", "lib\\runpy.py"]]):
            clean_tracebacks.append(i)

    return clean_tracebacks


def format_traceback(
    message: str = "",
    caption: str = "error_type",
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "ERROR",
    remove_frame_by_line_str: None | list = None,
) -> str:
    """Raise warning with current traceback as content. It means, that error was caught, but still
    something crashed.

    Args:
        message (str): Any string content of traceback.
        caption (str, optional): Caption of warning. If 'error_type', than Error type (e.g. ZeroDivisionError)
        is used. Defaults to 'error_type'.
        level (Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], optional): Defaults to "DEBUG".
        stack_level (int, optional): How many calls to log from error. Defaults to 3.
        remove_frame_by_line_str(None | list, optional): If there is some level in stack that should be
        omitted, add line here. Defaults to None.
    """
    if remove_frame_by_line_str:
        separated_traceback = get_traceback_str_with_removed_frames(remove_frame_by_line_str)

    else:
        separated_traceback = traceback_module.format_exc()

    if caption == "error_type":
        try:
            caption = sys.exc_info()[1].__class__.__name__
        except AttributeError:
            caption = "Error"

    if colors_config.USE_COLORS:
        separated_traceback = colorize_traceback(separated_traceback)

    separated_traceback = separated_traceback.rstrip()

    separated_traceback = format_str(
        message=message,
        caption=caption,
        use_object_conversion=False,
        uncolored_message=f"\n\n{separated_traceback}" if message else f"{separated_traceback}",
        level=level,
    )

    return separated_traceback
