#!/usr/bin/env python3

# @file quality_of_fit.py
# @author Muhammad Mohsin Khan

# This file provide function to
# calcualte mean quality of fit
# of experiment and their simulation.

# Python import commands
import numpy as np

# Optimate utilities
from . import forecastingMetrics
from .forecastingMetrics import mape

__all__ = ['QoF']


def QoF(exp: dict, sim: dict):

    '''
    Calculates the mean quality of fit.

    Arguments
    ---------
    exp : dict [-]
        A dict of experiments
    sim : dict [-]
        A dict of simulations

    Returns
    -------
    QoF : float [-]
        Mean quality of fit using MAPE
    '''

    QoF = 0
    
    for i in exp.keys():
        x1 = exp[i][:,1]
        x0 = exp[i][:,0]
        y0 = sim[i][:,0][1:]
        y1 = sim[i][:,1][1:]
        QoF += mape(np.log(x1), np.interp(np.log(x0), np.log(y0), np.log(y1)))
        
    QoF = 100 - (np.mean(QoF) * 100)

    return QoF
