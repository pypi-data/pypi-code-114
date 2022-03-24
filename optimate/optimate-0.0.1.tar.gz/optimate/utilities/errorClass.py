#!/usr/bin/env python3

# @file classError.py
# @author Muhammad Mohsin Khan

# This file provides different Error
# classes for Optimate

# Python import commands
import os
import pandas as pd


class Error(Exception):

    """Base class for exceptions in this module."""
    pass


class DirectoryNotFoundError(Error):

    """Raised if Data folder does not exist."""

    def __init__(self, error_message = None):
        super().__init__()
        self.error_message = error_message


    def check_path_subfunction(self, path):

        try:
            os.listdir(path)
        except:
            error_message = "optimate: error: no such file or directory: '" + path + "'"
            raise DirectoryNotFoundError(error_message)


    def check_path(self, path):

        try:
            self.check_path_subfunction(path)
        except DirectoryNotFoundError as e:
            raise e


class DataNotFoundError(Error):

    """Raised if data files are not present."""

    def __init__(self, error_message = "optimate: error: data file(s) not found"):
        super().__init__()
        self.error_message = error_message


    def check_data_subfunction(self, files):

        try:
            files[0]
        except:
            error_message = "optimate: error: data file(s) not found"
            raise DataNotFoundError(error_message)


    def check_data(self, files):

        try:
            self.check_data_subfunction(files)
        except DataNotFoundError as e:
            raise e


class InitialFileNotFoundError(Error):

    """Raised if initial guess file does not exist."""

    def __init__(self, error_message = "optimate: error: initial guess file not found"):
        super().__init__()
        self.error_message = error_message


    def check_initial_file_subfunction(self, initial_file):

        try:
            pd.read_csv(initial_file)
        except:
            error_message = "optimate: error: initial guess file not found"
            raise InitialFileNotFoundError(error_message)


    def check_initial_file(self, initial_file):

        try:
            self.check_initial_file_subfunction(initial_file)
        except InitialFileNotFoundError as e:
            raise e


class LoggingFileNotFoundError(Error):

    """Raised if logging config file does not exist."""

    def __init__(self, error_message = "optimate: error: logging config file not found"):
        super().__init__()
        self.error_message = error_message


class ExperimentSortingError(Error):

    """Raised if experiment file name(s) are not according to convention."""

    def __init__(self, error_message = "optimate: error: experiment file name(s) are not according to convention"):
        super().__init__()
        self.error_message = error_message


class WrongConstantsError(Error):

    """Raised if constants of the material models of optimate are not correct."""

    def __init__(self, error_message = None):
        super().__init__()
        self.error_message = error_message


    def check_constants_subfunction(self, constants, model):

        param = {}

        if model == "nb":
            for a in constants.keys():
                if a in ['K', 'n', 'm', 'temp']:
                    param[a] = constants[a]
                else:
                    error_message = "optimate: error: wrong constants for norton-bailey"
                    raise WrongConstantsError(error_message)

            for key in param:
                if type(param[key]) == str or type(param[key]) == list or type(param[key]) == tuple or type(param[key]) == dict or type(param[key]) == complex:
                    error_message = "optimate: error: wrong type of constants for norton-bailey"
                    raise WrongConstantsError(error_message)

            return param

        elif model == "kora":
            for a in constants.keys():
                if a in ["E", "ny", "k0", "n", "eta", "m", "a", "d", "beta", "gamma", "r0", "pi", "omega", "b", "c", "B1", "B2", "p", "w", "Af", "kf", "rf", "Ac", "kc", "rc", "ac_"]:
                    param[a] = constants[a]
                else:
                    error_message = "optimate: error: wrong constants for kora"
                    raise WrongConstantsError(error_message)

            for key in param:
                if type(param[key]) == str or type(param[key]) == list or type(param[key]) == tuple or type(param[key]) == dict or type(param[key]) == complex:
                    error_message = "optimate: error: wrong type of constants for kora"
                    raise WrongConstantsError(error_message)

            return param

        elif model == "gf":
            for a in constants.keys():
                if a in ["A10", "QA1", "a10", "Qa10", "a11", "Qa11", "ca1", "n1", "b1", "m10", "m11", "d1", "g1", "r12", "o12", "A20", "QA2", "a20", "Qa20", "a21", "Qa21", "ca2", "n2", "b2", "A30", "QA3", "a30", "a31", "n3", "b3", "m30", "m31", "d3", "g3", "r23", "o23", "kontraktion"]:
                    param[a] = constants[a]
                else:
                    error_message = "optimate: error: wrong constants for implicit garofalo"
                    raise WrongConstantsError(error_message)

            for key in param:
                if type(param[key]) == str or type(param[key]) == list or type(param[key]) == tuple or type(param[key]) == dict or type(param[key]) == complex:
                    error_message = "optimate: error: wrong type of constants for implicit garofalo"
                    raise WrongConstantsError(error_message)

            return param


    def check_constants(self, constants, model):

        try:
            param = self.check_constants_subfunction(constants, model)
        except WrongConstantsError as e:
            raise e

        return param


class WrongArgumentsError(Error):

    """Raised if arguments of the classes classOptimizer and classVisualization are not correct."""

    def __init__(self, error_message = None):
        super().__init__()
        self.error_message = error_message


    def check_arguments_subfunction(self, arguments, optimate_class):

        param = {}

        if optimate_class == "optimizer":
            for a in arguments.keys():
                if a in ['exp', 'method', 'model', 'files', 'path']:
                    param[a] = arguments[a]
                else:
                    error_message = "optimate: error: wrong arguments for optimizer"
                    raise WrongArgumentsError(error_message)

            return param

        if optimate_class == "visualization":
            for a in arguments.keys():
                if a in ['files', 'path_data', 'path_results']:
                    param[a] = arguments[a]
                else:
                    error_message = "optimate: error: wrong arguments for visualization"
                    raise WrongArgumentsError(error_message)

            return param


    def check_arguments(self, arguments, optimate_class):

        try:
            param = self.check_arguments_subfunction(arguments, optimate_class)
        except WrongArgumentsError as e:
            raise e

        return param


class ArgumentsTypeError(Error):

    """Raised if constants of the material models of optimate are not correct"""

    def __init__(self, error_message = None):
        super().__init__()
        self.error_message = error_message


    def check_arguments_type_subfunction(self, params):

        for a in params:
            if type(a) == str or type(a) == list or type(a) == tuple or type(a) == dict or type(a) == complex:
                error_message = "optimate: error: wrong type of constants"
                raise ArgumentsTypeError(error_message)


    def check_arguments_type(self, params):

        try:
            param = self.check_arguments_type_subfunction(params)
        except ArgumentsTypeError as e:
            raise e


class ArgumentsIndexError(Error):

    """Raised if the length of initial guess constants is not equal to the material models' constants."""

    def __init__(self, error_message = None):
        super().__init__()
        self.error_message = error_message


    def check_arguments_index_subfunction(self, arguments, model):

        if model == "nb":
            if len(arguments) != 3:
                error_message = "optimate: error: wrong number of material constants for  norton-bailey"
                raise ArgumentsIndexError(error_message)

        if model == "kora":
            if len(arguments) != 4:
                error_message = "optimate: error: wrong number of material constants for  kora"
                raise ArgumentsIndexError(error_message)

        if model == "gf":
            if len(arguments) != 36:
                error_message = "optimate: error: wrong number of material constants for  implicit garofalo"
                raise ArgumentsIndexError(error_message)


    def check_arguments_index(self, arguments, model):

        try:
            param = self.check_arguments_index_subfunction(arguments, model)
        except ArgumentsIndexError as e:
            raise e


class MaxTimeReachedError(Error):

    """Raised if the maximum allowed time for the optimization is reached."""

    def __init__(self, error_message = ''):
        super().__init__()
        self.error_message = error_message


    def check_max_time_subfunction(self, time, maxtime):

        if time >= maxtime:
            error_message = "optimate: error: Maximum time for optimization reached"
            raise MaxTimeReachedError(error_message)


    def check_max_time(self, time, maxtime):

        try:
            param = self.check_max_time_subfunction(time, maxtime)
        except MaxTimeReachedError as e:
            raise e
