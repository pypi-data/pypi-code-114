#!/usr/bin/env python3

# @file commandLineInterface.py
# @author Muhammad Mohsin Khan

# This script caters the options provided
# by the user for optimization.

# Python import command
import argparse
import sys


def check_positive(value):

    '''
    This function checks whether an input value is negative or not of type int or float.

    Arguments
    ---------
    value : int or float
        Input value by the user

    Returns
    -------
    fvalue : float
        Value converted into float.

    Raises
    ------
    TypeError
        If the input value is negative or not of type int or float.
    '''

    try:
        float(value)

    except ValueError:
        raise argparse.ArgumentTypeError("invalid float value: '%s'" % value)

    fvalue = float(value)

    if fvalue <= 0:
        raise argparse.ArgumentTypeError("invalid positive value: %s" % value)

    return fvalue


def getOptions():

    '''
    This function reads the user input options and returns them to the main program.

    Returns
    -------
    args : argparse.Namespace
        Arguments provided by the user
    '''

    my_parser = argparse.ArgumentParser(description='Optimate - Automatic parameter optimizer for different material models.', prog='optimate', usage='%(prog)s [options]', epilog='(c) Optimate, 2021. All Rights Reserved.')
    my_parser.version = 'optimate 0.7.1'
    my_parser.add_argument('-e', '--experiment', action='store', type=str, nargs='+', required=True, help='experiment(s) to be optimized')
    my_parser.add_argument('-o', '--optimizer-method', action='store', type=str, choices=['nm', 'bfgs'], required=True, help='optimizer method for the optimizer')
    my_parser.add_argument('-m', '--material-model', action='store', type=str, choices=['nb', 'gf', 'kora', 'mgf', 'tkora', 'rkora'], required=True, help='material model to be optimized')
    my_parser.add_argument('-w', '--weight-exp', action='store', type=check_positive, nargs='+', help='weight w.r.t. experiments (in descending order of stress and/or strain)')
    my_parser.add_argument('-W', '--weight-time', action='store', type=check_positive, nargs='+', help='weight w.r.t. time intervals (for 1-10 hrs : 10-MaxTime hrs)')
    my_parser.add_argument('-c', '--convert-unit', action='store_true', help="convert time unit from hours to seconds")
    my_parser.add_argument('-p', '--plot', action='store_true', help='save plot(s)')
    my_parser.add_argument('-t', '--plot-time', action='store', type=check_positive, help='maximum time value for plotting')
    my_parser.add_argument('--pic-format', action='store', type=str, choices=['pdf', 'png'], default='pdf', help="plot picture format, default 'pdf'")
    my_parser.add_argument('--opti-mode', action='store', type=str, choices=['strain', 'rate'], default='strain', help="mode of comparison between experiment and simulation for the residual function, default 'strain'")
    my_parser.add_argument('--error', action='store', type=str, choices=['mape', 'mase'], default='mase', help="error definition used in the residual function, default 'mase'")
    my_parser.add_argument('--error-scale', action='store', type=str, choices=['log', 'lin'], default='log', help="scale of optimization in the residual function, default 'log'")
    my_parser.add_argument('--timeout', action='store', type=check_positive, default=3600, help="Maximum allowed time (in seconds) for optimization, default 3600 sec")
    my_parser.add_argument('--max-iter', action='store', type=check_positive, default=10000, help="Maximum iterations allowed for optimization, default 10000")
    my_parser.add_argument('-v', '--version', action='version', help='display version information')

    args = my_parser.parse_args()

    options = vars(args)

    if options['weight_exp'] == None:
        weight_exp = [None] * len(options['experiment'])

        for i in range(len(weight_exp)):
            weight_exp[i] = 1

        options['weight_exp'] = weight_exp

    if len(options['weight_exp']) != len(options['experiment']):
        print("error: optimate: number of weights w.r.t. experiments not equal to number of experiments")
        sys.exit(1)

    if options['weight_time'] == None:
        options['weight_time'] = [1, 1]

    if len(options['weight_time']) != 2:
        print("error: optimate: number of weights w.r.t. time intervals must be two")
        sys.exit(1)

    return args
