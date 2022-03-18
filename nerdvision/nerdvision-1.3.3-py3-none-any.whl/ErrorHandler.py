import hashlib
import linecache
import logging
import os
import sys

from nerdvision import TYPES
from nerdvision.ContextUploadService import ContextUploadService
from nerdvision.Utils import Utils
from nerdvision.models.NVError import NVError, NVErrorFrame

our_logger = logging.getLogger("nerdvision")

if TYPES:
    from types import TracebackType, FrameType
    from typing import Union, Tuple, Type, Optional, Any


class ErrorHandler(object):
    roots = None

    def __init__(self, context_service, source_capture=False):
        # type: (ContextUploadService, bool) -> None
        self.context_service = context_service  # type: ContextUploadService
        self.source_capture = source_capture

    @staticmethod
    def load_roots(main=sys.modules['__main__']):
        # type: ({str}) -> {str}
        if ErrorHandler.roots is None:
            try:
                ErrorHandler.roots = set([
                                             # the path to the python executable
                                             os.path.abspath(
                                                 os.path.join(os.path.dirname(os.path.realpath(sys.executable)), '..')),
                                             # append python path (which can be not set) + then add the sys path as well
                                         ] + os.getenv('PYTHONPATH', '').split(os.pathsep) + sys.path)
                # the path to the main module
                if hasattr(main, '__file__'):
                    ErrorHandler.roots.add(os.path.dirname(main.__file__))
                ErrorHandler.roots = set([s for s in ErrorHandler.roots if s.strip()])
            except:
                our_logger.exception("Cannot load roots set defaulting to none.")
                ErrorHandler.roots = {}
        return ErrorHandler.roots

    def capture_exception(self, exception_type_or_tuple=None, value=None, tb=None):
        # type: (Union[BaseException, Type[BaseException], Tuple[Type[BaseException],BaseException, TracebackType]], BaseException, TracebackType) -> None
        """
        Captures an exception and extracts it into a NVError.
        If an exception is not provided, ask the system for the last error.

        :param exception_type_or_tuple: the exception to capture (as a tuple or value) or None
        :param value: the exception value
        :param tb: the traceback to process
        """

        if isinstance(exception_type_or_tuple, BaseException):
            exc_info = Utils.exc_info_from_exception(exception_type_or_tuple)
        elif isinstance(exception_type_or_tuple, tuple):
            exc_info = Utils.exc_info_from_exception(exception_type_or_tuple)
        elif isinstance(exception_type_or_tuple, type):
            exc_info = exception_type_or_tuple, value, tb
        else:
            exc_info = sys.exc_info()

        if exc_info[0] is None:
            our_logger.debug("No exception info found")
            return

        exc_type, exc_value, tb = exc_info

        nv_error = ErrorHandler.create_nv_error(exc_type, exc_value, tb, source_capture=self.source_capture)

        self.context_service.send_nv_error(nv_error)

    @staticmethod
    def trim_paths(path, roots):
        # type: (str, [str]) -> str
        for root in roots:
            if path.startswith(root):
                return path[len(root):]
        return path

    @staticmethod
    def create_nv_error(exception_type, exception, tb, roots=None, source_capture=False):
        # type: (Type[BaseException],BaseException, TracebackType, [str], bool) -> Optional[NVError]
        """
        Create an NV Error from the exception details

        :param exception_type: the type of the exception
        :param exception: the actual exception value
        :param tb: the traceback for the exception
        :param roots: the system roots to trim from the file names
        :param source_capture: should we capture the source line with the error
        :return: the NVError representation of the error
        """

        if roots is None:
            roots = ErrorHandler.load_roots()

        if tb is None:
            return None

        # python exception are made of 2 parts the traceback, which is the path from where we are to the
        # tracepoint and the stack, which is the path to here. So we need to combine them to get the real trace

        nv_error = NVError(exception_type.__name__, ', '.join(str(arg) for arg in exception.args))
        frame = tb.tb_frame
        while frame is not None:
            line_no = frame.f_lineno
            source_file = frame.f_code.co_filename
            func_name = frame.f_code.co_name
            _self = frame.f_locals.get('self', None)
            class_name = None
            if _self is not None:
                class_name = _self.__class__.__name__

            source = ErrorHandler.get_source_line(frame, line_no) if source_capture else None
            nv_error.add_frame(NVErrorFrame(class_name, func_name, line_no, ErrorHandler.trim_paths(source_file, roots),
                                            source.strip() if source else None))
            frame = frame.f_back

        frame = tb
        while frame is not None:
            line_no = frame.tb_lineno
            source_file = frame.tb_frame.f_code.co_filename
            func_name = frame.tb_frame.f_code.co_name
            _self = frame.tb_frame.f_locals.get('self', None)
            class_name = None
            if _self is not None:
                class_name = _self.__class__.__name__

            source = ErrorHandler.get_source_line(frame.tb_frame, line_no) if source_capture else None
            nv_error.push_frame(NVErrorFrame(class_name, func_name, line_no, ErrorHandler.trim_paths(source_file, roots),
                                             source.strip() if source else None))
            frame = frame.tb_next

        nv_error.id = ErrorHandler.create_id(exception_type.__name__, nv_error.trace[0].source_file, nv_error.trace[0].line_no)
        return nv_error

    @staticmethod
    def create_id(type_name, source_file, line_no):
        # type: (str, str, int) -> str
        return hashlib.md5((type_name + source_file + str(line_no)).encode('utf-8')).hexdigest()

    @staticmethod
    def get_source_line(frame, tb_lineno):
        # type: (FrameType, int) -> Optional[str]
        try:
            abs_path = frame.f_code.co_filename  # type: Optional[str]
        except Exception:
            abs_path = None

        if not abs_path:
            return None

        try:
            module = frame.f_globals["__name__"]
        except Exception:
            return None

        try:
            loader = frame.f_globals["__loader__"]
        except Exception:
            loader = None

        return ErrorHandler.get_line_from_file(abs_path, tb_lineno - 1, loader, module)

    @staticmethod
    def get_line_from_file(filename, lineno, loader=None, module=None):
        # type: (str, int, Optional[Any], Optional[str]) -> Optional[str]
        source = None
        if loader is not None and hasattr(loader, "get_source"):
            try:
                source_str = loader.get_source(module)  # type: Optional[str]
            except (ImportError, IOError):
                source_str = None
            if source_str is not None:
                source = source_str.splitlines()

        if source is None:
            try:
                source = linecache.getlines(filename)
            except (OSError, IOError):
                return None

        if not source:
            return None

        try:
            return ErrorHandler.strip_string(source[lineno].strip("\r\n"))
        except IndexError:
            # the file may have changed since it was loaded into memory
            return None

    @staticmethod
    def strip_string(value, max_length=200):
        # type: (str, int) -> str
        if not value:
            return value

        length = len(value)

        if length > max_length:
            return value[: max_length]
        return value
