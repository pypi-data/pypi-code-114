"""
inspection and debugging helper functions
=========================================

this ae namespace portion provides useful helper functions for inspection and debugging.


call stack inspection
---------------------

:func:`module_attr` dynamically determines a reference to an attribute (variable, function, class, ...) in a module.

:func:`module_name`, :func:`stack_frames`, :func:`stack_var` and :func:`stack_vars` are inspecting the call stack frames
to determine e.g. variable values of the callers of a function/method.

.. hint::
    the :class:`AppBase` class uses these helper functions to determine the :attr:`version <AppBase.app_version>` and
    :attr:`title <AppBase.app_title>` of an application, if these values are not specified in the instance initializer.

another useful helper function provided by this portion to inspect and debug your code is :func:`full_stack_trace`.


dynamic execution of code blocks and expressions
------------------------------------------------

for the dynamic execution of functions and code blocks the helper functions :func:`try_call`, :func:`try_exec`
and :func:`exec_with_return` are provided. the helper function :func:`try_eval` evaluates dynamic expressions.

.. note::
    make sure the dynamically executed code block or expression string is secure to prevent code injections of malware.

.. hint::
    these functions are e.g. used by the :class:`~.literal.Literal` class to dynamically determine literal values.
"""
import ast
import datetime
import logging
import logging.config as logging_config
import os
import sys
import threading
import unicodedata
import weakref

from inspect import getinnerframes, getouterframes, getsourcefile
from string import ascii_letters, digits
from typing import Any, Callable, Dict, Generator, List, Optional, Tuple, Type
from _ast import stmt

from ae.base import DATE_ISO, DATE_TIME_ISO, UNSET, import_module, norm_name, norm_path             # type: ignore


__version__ = '0.3.13'


# suppress unused import err (needed e.g. for unpickling of dates via try_eval() and for include them into base_globals)
_d = (os, DATE_ISO, DATE_TIME_ISO,
      ascii_letters, digits, datetime, logging, logging_config, norm_name, norm_path, threading, unicodedata, weakref)

SKIPPED_MODULES = ('ae.base', 'ae.paths', 'ae.inspector', 'ae.core', 'ae.console', 'ae.gui_app',
                   'ae.gui_help', 'ae.kivy_app', 'ae.enaml_app',    # removed in V 0.1.4: 'ae.lisz_app_data',
                   'ae.beeware_app', 'ae.pyglet_app', 'ae.pygobject_app', 'ae.dabo_app',
                   'ae.qpython_app', 'ae.appjar_app',
                   'importlib._bootstrap', 'importlib._bootstrap_external')
""" skipped modules used as default by :func:`module_name`, :func:`stack_var` and :func:`stack_vars` """


def exec_with_return(code_block: str, ignored_exceptions: Tuple[Type[Exception], ...] = (),
                     glo_vars: Optional[Dict[str, Any]] = None, loc_vars: Optional[Dict[str, Any]] = None
                     ) -> Optional[Any]:
    """ execute python code block and return the resulting value of its last code line.

    :param code_block:          python code block to execute.
    :param ignored_exceptions:  tuple of ignored exceptions.
    :param glo_vars:            optional globals() available in the code execution.
    :param loc_vars:            optional locals() available in the code execution.
    :return:                    value of the expression at the last code line
                                or UNSET if either code block is empty, only contains comment lines, or one of
                                the ignorable exceptions raised or if last code line is no expression.

    inspired by this SO answer
    https://stackoverflow.com/questions/33409207/how-to-return-value-from-exec-in-function/52361938#52361938.
    """
    if glo_vars is None:
        glo_vars = base_globals
    elif '_add_base_globals' in glo_vars:
        glo_vars.update(base_globals)

    try:
        code_ast = ast.parse(code_block)    # raises SyntaxError if code block is invalid
        nodes: List[stmt] = code_ast.body
        if nodes:
            if isinstance(nodes[-1], ast.Expr):
                last_node = nodes.pop()
                if len(nodes) > 0:
                    # noinspection BuiltinExec
                    exec(compile(code_ast, "<ast>", 'exec'), glo_vars, loc_vars)
                # noinspection PyTypeChecker
                # .. and mypy needs getattr() instead of last_node.value
                return eval(compile(ast.Expression(getattr(last_node, 'value')), "<ast>", 'eval'), glo_vars, loc_vars)
            # noinspection BuiltinExec
            exec(compile(code_ast, "<ast>", 'exec'), glo_vars, loc_vars)
    except ignored_exceptions:
        pass                            # return UNSET if one of the ignorable exceptions raised in compiling

    return UNSET                        # mypy needs explicit return statement and value


def full_stack_trace(ex: Exception) -> str:
    """ get full stack trace from an exception.

    :param ex:                  exception instance.
    :return:                    str with stack trace info.
    """
    ret = f"Exception {ex!r}. Traceback:\n"
    trace_back = sys.exc_info()[2]
    if trace_back:
        def ext_ret(item):
            """ process traceback frame and add as str to ret """
            nonlocal ret
            ret += f'File "{item[1]}", line {item[2]}, in {item[3]}\n'
            lines = item[4]  # mypy does not detect item[]
            if lines:
                for line in lines:
                    ret += ' ' * 4 + line.lstrip()

        for frame in reversed(getouterframes(trace_back.tb_frame)[1:]):
            ext_ret(frame)
        for frame in getinnerframes(trace_back):
            ext_ret(frame)
    return ret


def module_attr(import_name: str, attr_name: str = "") -> Optional[Any]:
    """ determine dynamically a reference to a module or to any attribute (variable/func/class) declared in the module.

    :param import_name:         import-/dot-name of the distribution/module/package to load/import.
    :param attr_name:           name of the attribute declared within the module. do not specify or pass an empty
                                string to get/return a reference to the imported module instance.
    :return:                    module instance or module attribute value
                                or None if module not found
                                or UNSET if module attribute doesn't exist.

    .. note:: a previously not imported module will *not* be added to `sys.modules` by this function.

    """
    mod_ref = sys.modules.get(import_name, None) or import_module(import_name)
    return getattr(mod_ref, attr_name, UNSET) if mod_ref and attr_name else mod_ref


def module_file_path(local_object: Optional[Callable] = None) -> str:
    """ determine the absolute path of the module from which this function got called.

    :param local_object:        optional local module, class, method, function, traceback, frame, or code object of the
                                calling module (passing `lambda: 0` also works). omit to use instead the `__file__`
                                module variable (which will not work if the module is frozen by py2exe/PyInstaller).
    :return:                    module path (inclusive module file name) or empty string if path not found/determinable.
    """
    if local_object:
        file_path = getsourcefile(local_object)
        if file_path:
            return norm_path(file_path)

    # if getattr(sys, 'frozen', False):
    #    path_without_file = os.getcwd()
    return stack_var('__file__', depth=2) or ""   # or use sys._getframe().f_code.co_filename


def module_name(*skip_modules: str, depth: int = 0) -> Optional[str]:
    """ find the first module in the call stack that is *not* in :paramref:`~module_name.skip_modules`.

    :param skip_modules:        module names to skip (def=this ae.core module).
    :param depth:               the calling level from which on to search. the default value 0 refers the frame and
                                the module of the caller of this function.
                                pass 1 or an even higher value if you want to get the module name of a function/method
                                in a deeper level in the call stack.
    :return:                    the module name of the call stack level specified by :paramref:`~module_name.depth`.
    """
    if not skip_modules:
        skip_modules = SKIPPED_MODULES
    return stack_var('__name__', *skip_modules, depth=depth + 1)


def stack_frames(depth: int = 1) -> Generator:  # Generator[frame, None, None]
    """ generator returning the call stack frame from the level given in :paramref:`~stack_frames.depth`.

    :param depth:               the stack level to start; the first returned frame by this generator. the default value
                                (1) refers the next deeper stack frame, respectively the one of the caller of this
                                function. pass 2 or a higher value if you want to start with an even deeper frame/level.
    :return:                    generated frames of the call stack.
    """
    try:
        while True:
            depth += 1
            # noinspection PyProtectedMember,PyUnresolvedReferences
            yield sys._getframe(depth)          # pylint: disable=protected-access
    except (TypeError, AttributeError, ValueError):
        pass


def stack_var(name: str, *skip_modules: str, scope: str = '', depth: int = 1) -> Optional[Any]:
    """ determine variable value in calling stack/frames.

    :param name:                variable name to search in the calling stack frames.
    :param skip_modules:        module names to skip (def=see :data:`SKIPPED_MODULES` module constant).
    :param scope:               pass 'locals' to only check for local variables (ignoring globals) or
                                'globals' to only check for global variables (ignoring locals). the default value (an
                                empty string) will not restrict the scope, returning either a local or global value.
    :param depth:               the calling level from which on to search. the default value (1) refers the next
                                deeper stack frame, which is the caller of the function. pass 2 or an even higher
                                value if you want to start the variable search from a deeper level in the call stack.
    :return:                    the variable value of a deeper level within the call stack or UNSET if the variable was
                                not found.
    """
    glo, loc, _deep = stack_vars(*skip_modules, find_name=name, min_depth=depth + 1, scope=scope)
    variables = glo if name in glo and scope != 'locals' else loc
    return variables.get(name, UNSET)


def stack_vars(*skip_modules: str,
               find_name: str = '', min_depth: int = 1, max_depth: int = 0, scope: str = ''
               ) -> Tuple[Dict[str, Any], Dict[str, Any], int]:
    """ determine all global and local variables in a calling stack/frames.

    :param skip_modules:        module names to skip (def=see :data:`SKIPPED_MODULES` module constant).
    :param find_name:           if passed then the returned stack frame must contain a variable with the passed name.
    :param scope:               scope to search the variable name passed via :paramref:`~stack_vars.find_name`. pass
                                'locals' to only search for local variables (ignoring globals) or 'globals' to only
                                check for global variables (ignoring locals). passing an empty string will find the
                                variable within either locals and globals.
    :param min_depth:           the call stack level from which on to search. the default value (1) refers the next
                                deeper stack frame, respectively to the caller of this function. pass 2 or a higher
                                value if you want to get the variables from a deeper level in the call stack.
    :param max_depth:           the maximum depth in the call stack from which to return the variables. if the specified
                                argument is not zero and no :paramref:`~stack_vars.skip_modules` are specified then the
                                first deeper stack frame that is not within the default :data:`SKIPPED_MODULES` will be
                                returned. if this argument and :paramref:`~stack_var.find_name` get not passed then the
                                variables of the top stack frame will be returned.
    :return:                    tuple of the global and local variable dicts and the depth in the call stack.
    """
    if not skip_modules:
        skip_modules = SKIPPED_MODULES
    glo = loc = {}
    depth = min_depth + 1   # +1 for stack_frames()
    for frame in stack_frames(depth=depth):
        depth += 1
        glo, loc = frame.f_globals, frame.f_locals

        if glo.get('__name__') in skip_modules:
            continue
        if find_name and (find_name in glo and scope != 'locals' or find_name in loc and scope != 'globals'):
            break
        if max_depth and depth > max_depth:
            break
    # experienced strange overwrites of locals (e.g. self) when returning f_locals directly (adding .copy() fixed it)
    # check if f_locals is a dict (because enaml is using their DynamicScope object which is missing a copy method)
    if isinstance(loc, dict):
        loc = loc.copy()
    return glo.copy(), loc, depth - 1


def try_call(callee: Callable, *args, ignored_exceptions: Tuple[Type[Exception], ...] = (), **kwargs) -> Optional[Any]:
    """ execute callable while ignoring specified exceptions and return callable return value.

    :param callee:              pointer to callable (either function pointer, lambda expression, a class, ...).
    :param args:                function arguments tuple.
    :param ignored_exceptions:  tuple of ignored exceptions.
    :param kwargs:              function keyword arguments dict.
    :return:                    function return value or UNSET if an ignored exception got thrown.
    """
    ret = UNSET
    try:  # catch type conversion errors, e.g. for datetime.date(None) while bool(None) works (->False)
        ret = callee(*args, **kwargs)
    except ignored_exceptions:
        pass
    return ret


def try_eval(expr: str, ignored_exceptions: Tuple[Type[Exception], ...] = (),
             glo_vars: Optional[Dict[str, Any]] = None, loc_vars: Optional[Dict[str, Any]] = None) -> Optional[Any]:
    """ evaluate expression string ignoring specified exceptions and return evaluated value.

    :param expr:                expression to evaluate.
    :param ignored_exceptions:  tuple of ignored exceptions.
    :param glo_vars:            optional globals() available in the expression evaluation.
    :param loc_vars:            optional locals() available in the expression evaluation.
    :return:                    function return value or UNSET if a ignored exception got thrown.
    """
    ret = UNSET

    if glo_vars is None:
        glo_vars = base_globals
    elif '_add_base_globals' in glo_vars:
        glo_vars.update(base_globals)

    try:  # catch type conversion errors, e.g. for datetime.date(None) while bool(None) works (->False)
        ret = eval(expr, glo_vars, loc_vars)
    except ignored_exceptions:
        pass
    return ret


def try_exec(code_block: str, ignored_exceptions: Tuple[Type[Exception], ...] = (),
             glo_vars: Optional[Dict[str, Any]] = None, loc_vars: Optional[Dict[str, Any]] = None) -> Optional[Any]:
    """ execute python code block string ignoring specified exceptions and return value of last code line in block.

    :param code_block:          python code block to be executed.
    :param ignored_exceptions:  tuple of ignored exceptions.
    :param glo_vars:            optional globals() available in the code execution.
    :param loc_vars:            optional locals() available in the code execution.
    :return:                    function return value or UNSET if an ignored exception got thrown.
    """
    ret = UNSET
    try:
        ret = exec_with_return(code_block, glo_vars=glo_vars, loc_vars=loc_vars)
    except ignored_exceptions:
        pass
    return ret


base_globals = globals()        #: default if no global variables get passed in dynamic code/expression evaluations
