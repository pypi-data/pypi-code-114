#!/usr/bin/env python3

# @file dataPointClass.py
# @author Muhammad Mohsin Khan

# This class is used to return data points
# of experiments as a class with information
# of the experiment.

__all__ = ['dataPoint']

class dataPoint():

    '''
    This class is used to save and process data.
    '''

    def __init__(self, **args):

        '''
        Initializes an instance of the dataPoint class with provided arguments.

        Arguments
        ---------
        strain      : int or float [-]
            Strain value
        stress      : int or float [MPa]
            Stress value
        temp        : int or float [°C]
            Temperature
        time        : int or float [sec or hrs]
            Time
        weight_time : list of int or float [-]
            Weight assigned w.r.t. time for optimization
        exp         : str [-]
            Experiment type i.e., creep or relaxation
        '''

        for k in args.keys():
            self.__setattr__(k, args[k])

        mandatory='time', 'strain', 'stress', 'temp', 'weight_time', 'exp'

        for m in mandatory:
            try:
                args[m]
            except:
                raise Exception('parameter {0} mandatory'.format(m))
