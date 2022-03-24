#!/usr/bin/env python3

# @file test_linearInterpolation.py
# @author Muhammad Mohsin Khan

# This class provides test for
# the linearInterpolation's function.

# Python import commands
import numpy as np
import time
from numpy.testing import assert_array_almost_equal

# Optimate import
from optimate.utilities import linearInterpolation as lin_inter


class TestLinearInterpolation():

    """
    Basic test class for linearInterpolation.py.
    """


    def test_find_x_closeto_y(self):

        """
        Test function for find_x_closeto_y().
        """

        values = np.array([1,2,3,4,5])
        
        test = np.array([0, 4])
        res = lin_inter.find_x_closeto_y([0.5,4.6], values)
        assert_array_almost_equal(res, test, decimal=8)
        
        
    def test_calc_setvalue(self):

        """
        Test function for calc_setvalue().
        """

        values = np.array([0,1,2,3,4])
        time = np.array([1,2,3,4,5])
        
        test = np.array([0.5, 1.5, 2.5])
        res = lin_inter.calc_setvalue([1.5,2.5,3.5], time, values)
        assert_array_almost_equal(res, test, decimal=8)
