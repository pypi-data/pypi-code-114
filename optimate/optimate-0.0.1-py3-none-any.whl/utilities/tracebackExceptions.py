#!/usr/bin/env python3

# @file tracebackExceptions.py
# @author Muhammad Mohsin Khan

# This file provide functions for extracting,
# formatting and tracing exceptions.

# Python import commands
import sys, logging, traceback


logger = logging.getLogger('optimate')


def log_exception(e):

    '''
    Logs the extracted exception in the logger.

    Arguments
    ---------
    e : type
        Exception type
    '''

    logger.info("Tracing error...")
    logger.error("Function {function_name} raised {exception_class} ({exception_docstring}): {exception_message}".format(
        function_name = extract_function_name(),
        exception_class = e.__class__,
        exception_docstring = e.__doc__,
        exception_message = e.error_message))


def extract_function_name():

    '''
    Extracts the name of the function.

    Returns
    -------
    fname : str
        Name of the function
    '''

    logger.info("Extracting name of the function")
    tb = sys.exc_info()[-1]
    stk = traceback.extract_tb(tb, 1)
    fname = stk[0][3]

    return fname
