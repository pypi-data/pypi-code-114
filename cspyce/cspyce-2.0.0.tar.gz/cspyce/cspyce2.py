################################################################################
# cspyce/cspyce2.py
################################################################################
# module cspyce.cspyce2
#
# This module re-declares every cspyce1 function explicitly, with its list of
# argument names as used by CSPICE. The practical effect is that functions in
# cspyce2 module can be called in a fully Python-like way, the rightmost inputs
# in any order and identified by their names.
#
# NOTE: This file is generated automatically using program make_cspyce2.py:
#   python make_cspyce2.py > cspyce2.py
#
################################################################################

import sys
from functools import wraps

import cspyce.cspyce1 as cspyce1

PYTHON2 = sys.version_info[0] < 3

# This function makes cspyce2 look the same as cspyce1. It ensures that every
# location in the global dictionary and every function's internal link point
# a new function of the same name.

CSPYCE_FUNCTION_LOOKUP = {}


def relink_all(new_dict, old_dict):

    # Assign a new function to the dictionary at the same location as every
    # cspyce function found in the old dictionary

    dict_names = {}     # maps each function name to its dictionary locations
    old_funcs = {}      # maps each function name to its old function
    for (dict_name, old_func) in old_dict.items():
        if not callable(old_func):
            continue
        if 'SIGNATURE' not in old_func.__dict__:
            continue

        func_name = old_func.__name__
        old_funcs[func_name] = old_func

        if func_name not in dict_names:
            dict_names[func_name] = []

        dict_names[func_name].append(dict_name)

    for (name, keys) in dict_names.items():
        func = new_dict[name]
        for key in keys:
            new_dict[key] = func
            CSPYCE_FUNCTION_LOOKUP[func.__name__] = func

    # Make sure each cspyce function has the same properties and attributes as
    # the one in the old dictionary

    for (name, old_func) in old_funcs.items():
        func = new_dict[name]

        # Copy function properties
        func.__doc__ = old_func.__doc__

        if PYTHON2:
            func.func_defaults = old_func.func_defaults
        else:
            func.__defaults__ = old_func.__defaults__

        # Copy attributes
        for (key, value) in old_func.__dict__.items():
            if not callable(value):
                func.__dict__[key] = value
            else:
                # If it's a function, locate a new one with the same name
                func.__dict__[key] = new_dict[value.__name__]

# This is the old version of populate_cspyce2().  I have replace it with a different
# version because code should not be using exec() unless it absolutely has to.
# I'm leaving this old version here just incase there is some incompatibility I'm not
# aware of.
#
# def populate_cspyce2():
#     snippets = [
#         "def {name}({arglist}): return cspyce1.{name}({arglist})".format(
#              name=name, arglist=", ".join(func.ARGNAMES))
#         for name, func in cspyce1.__dict__.items()
#         if callable(func) and hasattr(func, 'ARGNAMES')
#     ]
#     code = "\n\n".join(snippets)
#     exec(code, globals(), globals())


def populate_cspyce2():
    def wrapper(f):
        @wraps(f)
        def runner(*args, **kwargs):
            return f(*args, **kwargs)
        return runner
    for name, func in cspyce1.__dict__.items():
        if callable(func) and hasattr(func, 'ARGNAMES'):
            globals()[name] = wrapper(func)




populate_cspyce2()
relink_all(globals(), cspyce1.__dict__)

################################################################################
