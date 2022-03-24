 #!/usr/bin/env python3

# @file linearInterpolation.py
# @author Muhammad Mohsin Khan

# This script provides functions to interpolate
# 2-dimensional data linearly.

# Python import command
import numpy as np

__all__ = ['find_x_closeto_y', 'calc_setvalue']


def find_x_closeto_y(x, y, minMax="min"):

    """
    Returns indeces to the closest value in a list.

    Arguments
    ---------
    x : list of int or float
        Values to be searched
    y : list of int or float
        Array of values

    Returns
    -------
    pos : list of int or float
        Array of indeces corresponding to x searched in y

    Example
    -------
    >>> import linearInterpolation
    >>> values = [1,2,3,4,5]
    >>> pos = linearInterpolation.find_x_closeto_y([0.5,4.6], values)
    >>> pos
    array([0, 4])
    """

    pos = []

    for a in range(len(x)):
        if minMax.lower() == "min":
            pos.append(min(range(len(y)), key=lambda i: abs(y[i] - x[a])))

        else:
            pos.append(max(range(len(y)), key=lambda i: abs(y[i] - x[a])))

    pos = np.asarray(pos)

    return pos


def calc_setvalue(t, setTime, setvalue):

    """
    Returns a list of linearly interpolated values.

    Arguments
    ---------
    t        : list of int or float
        Time points for interpolation
    setTime  : list of int or float
        x axis of the data
    setvalue : list of int or float
        y axis of the data

    Returns
    -------
    val : list of int or float
        Interpolated values

    Example
    -------
    >>> import linearInterpolation
    >>> values = [0,1,2,3,4]
    >>> time = [1,2,3,4,5]
    >>> val = linearInterpolation.calc_setvalue([1.5,2.5,3.5], time, values)
    >>> val
    array([0.5, 1.5, 2.5])
    """

    val = []
    tTmpPos = find_x_closeto_y(t, setTime)

    # Linear interpolation between the two time points
    for a in range(len(tTmpPos)):
        if setTime[tTmpPos[a]] <= t[a] and setTime[-1] > t[a]:
            mTmp = (setvalue[tTmpPos[a] + 1] - setvalue[tTmpPos[a]])/(setTime[tTmpPos[a] + 1] - setTime[tTmpPos[a]])
        elif setTime[tTmpPos[a]] >= t[a]:
            mTmp = (setvalue[tTmpPos[a]] - setvalue[tTmpPos[a] - 1])/(setTime[tTmpPos[a]] - setTime[tTmpPos[a] - 1])
        elif t[a] > setTime[-1]:
            val.append(setvalue[-1])
            return val

        bTmp = setvalue[tTmpPos[a]] - mTmp*setTime[tTmpPos[a]]

        if mTmp*t[a] + bTmp == 0:
            val.append(1e-6)
        else:
            val.append(mTmp*t[a] + bTmp)

    val = np.asarray(val)

    return val
