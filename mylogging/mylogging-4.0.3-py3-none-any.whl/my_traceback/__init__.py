"""Contain tools for logging of caught exceptions or and raised errors.

Usually there is one function that is heavily used and it is 'enhance_excepthook'. If you call it and 
then somewhere use raise, it will make it colorful, highlight a user message and if debugging, remove extra
stack frames.

Another name for this subpackage is also exceptions as this is hard to separate those terms.
"""
from mylogging.my_traceback.my_traceback_module import (
    enhance_excepthook,
    get_traceback_str_with_removed_frames,
    format_traceback,
    raise_enhanced,
    remove_debug_stack_trace,
    enhance_excepthook_reset,
)

__all__ = [
    "enhance_excepthook",
    "get_traceback_str_with_removed_frames",
    "format_traceback",
    "raise_enhanced",
    "remove_debug_stack_trace",
    "enhance_excepthook_reset",
]
