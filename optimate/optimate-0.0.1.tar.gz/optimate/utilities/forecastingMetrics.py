#!/usr/bin/env python3

# @file forecasting_metrics.py
# @author Muhammad Mohsin Khan

# This file provide different
# forecasting metrics.

# Python import commands
import numpy as np

__all__ = ['error', 'mae', 'percentage_error', 'mape', 'mase']


def error(actual: np.ndarray, predicted: np.ndarray):

    '''
    Calculates the statistical error.

    Arguments
    ---------
    actual    : numpy.ndarray [-]
        A list of actual values (shape = (x,))
    predicted : numpy.ndarray [-]
        A list of predicted values (shape = (x,))

    Returns
    -------
    error : float [-]
        Statistical Error
    '''

    error = actual - predicted

    return error


def mae(actual: np.ndarray, predicted: np.ndarray):

    '''
    Calculates the mean absolute error.

    Arguments
    ---------
    actual    : numpy.ndarray [-]
        A list of actual values (shape = (x,))
    predicted : numpy.ndarray [-]
        A list of predicted values (shape = (x,))

    Returns
    -------
    mae : float [-]
        Mean absolute error
    '''

    mae =  np.mean(np.abs(error(actual, predicted)))
    return mae


def percentage_error(actual: np.ndarray, predicted: np.ndarray):

    '''
    Calculates the percentage error.

    Arguments
    ---------
    actual    : numpy.ndarray [-]
        A list of actual values (shape = (x,))
    predicted : numpy.ndarray [-]
        A list of predicted values (shape = (x,))

    Returns
    -------
    percentage_error : float [-]
        Percentage error (Not multiplied by 100)
    '''
    
    percentage_error = error(actual, predicted) / actual

    return percentage_error


def mape(actual: np.ndarray, predicted: np.ndarray):

    '''
    Calculates the mean absolute percentage error.

    Arguments
    ---------
    actual    : numpy.ndarray [-]
        A list of actual values (shape = (x,))
    predicted : numpy.ndarray [-]
        A list of predicted values (shape = (x,))

    Returns
    -------
    mape : float [-]
        Mean absolute percentage error (Not multiplied by 100)
    '''

    mape = np.mean(np.abs(percentage_error(actual, predicted)))

    return mape


def mase(actual : np.ndarray, predicted : np.ndarray):

    '''
    Calculates the mean absolute scaled error.

    Arguments
    ---------
    actual    : numpy.ndarray [-]
        A list of actual values (shape = (x,))
    predicted : numpy.ndarray [-]
        A list of predicted values (shape = (x,))

    Returns
    -------
    mase : float [-]
        Mean absolute scaled error
    '''

    forecast_error = mae(actual, predicted)
    naive_forecast = np.mean(np.abs(np.diff(actual)))
    mase = forecast_error / naive_forecast

    return mase
