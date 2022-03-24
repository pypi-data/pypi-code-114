#!/usr/bin/env python3

# @file experimentSorter.py
# @author Muhammad Mohsin Khan

# This file provide a function for sorting
# creep experiments in descending order of
# stress followed by relaxation experiments
# in descending order of strain.

# Python import commands
import logging

# Optimate utilities
from . import errorClass
from .errorClass import ExperimentSortingError

__all__ = ['sorter']


logger = logging.getLogger('optimate')


def sorter(filenameExpData):

    '''
    Sorts the creep and relaxation experiments in descending order of stress and initial strain respectively.

    Arguments
    ---------
    filenameExpData : list of str [-]
        List of experiments to be optimized
        
    Returns
    -------
    experiments : list of str [-]
        Sorted list of experiments to be optimized
    '''
    
    logger.debug('Sorting creep experiments in descending order of stress')

    try:
        # Separate creep experiment from input list of experiments
        creep_experiments = [i for i in filenameExpData if "Cre" in i]
        creep_dict = {}
        
        # Save experiments in a dictionary with stresses as keys and expeiment names as value
        for i in creep_experiments:
            creep_dict[float(i.split("_")[1])] = i

        # Sort key value pair of dictionary in descending order
        reversed_keys = list(reversed(sorted(creep_dict.keys())))

        experiments = []

        # Save sorted experiments in a list
        for i in reversed_keys:
            experiments.append(creep_dict[i])

        logger.debug('Sorting relaxation experiments in descending order of strain')
        
        # Separate relaxation experiment from input list of experiments
        relax_experiments = [i for i in filenameExpData if "Rel" in i]
        relax_dict = {}
        
        # Save experiments in a dictionary with strains as keys and expeiment names as value
        for i in relax_experiments:
            relax_dict[float(i.split("_")[1])] = i
            
        # Sort key value pair of dictionary in descending order
        reversed_keys = list(reversed(sorted(relax_dict.keys())))

        # Save sorted experiments in the previously generated list
        for i in reversed_keys:
            experiments.append(relax_dict[i])

    except (IndexError, ValueError):
        # Raised error when naming convention of experiment files are wrong
        raise ExperimentSortingError
    
    return experiments
