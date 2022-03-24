#!/usr/bin/env python3

# @file test_forecastingMetrics.py
# @author Muhammad Mohsin Khan

# This class provides tests for
# the forecastingMetrics' functions.

# Python import commands
import numpy as np
import time
from numpy.testing import assert_almost_equal, assert_array_almost_equal

# Optimate import
from optimate.utilities import forecastingMetrics as fm


class TestForecastingMetrics():

    """
    Basic test class for forecastingMetrics.py.
    """


    def test_error(self):

        """
        Test function for error().
        """

        actual = np.array([1,2,3])
        predicted = np.array([1.1, 2.2, 3.3])

        test = np.array([-0.1, -0.2, -0.3])
        res = fm.error(actual, predicted)
        assert_array_almost_equal(res, test, decimal=8)
        
    
    def test_mae(self):

        """
        Test function for mae().
        """

        actual = np.array([1,2,3])
        predicted = np.array([1.1, 2.2, 3.3])

        test = 0.20000000000000004
        res = fm.mae(actual, predicted)
        assert_almost_equal(res, test, decimal=8)
        
        
    def test_percentage_error(self):

        """
        Test function for percentage_error().
        """

        actual = np.array([1,2,3])
        predicted = np.array([1.1, 2.2, 3.3])

        test = np.array([-0.1, -0.1, -0.1])
        res = fm.percentage_error(actual, predicted)
        assert_array_almost_equal(res, test, decimal=8)
        
        
    def test_mape(self):

        """
        Test function for mape().
        """

        actual = np.array([1,2,3])
        predicted = np.array([1.1, 2.2, 3.3])

        test = 0.10000000000000003
        res = fm.mape(actual, predicted)
        assert_almost_equal(res, test, decimal=8)
        
        
    def test_mase(self):

        """
        Test function for mase().
        """

        actual = np.array([1,2,3])
        predicted = np.array([1.1, 2.2, 3.3])

        test = 0.20000000000000004
        res = fm.mase(actual, predicted)
        assert_almost_equal(res, test, decimal=8)
