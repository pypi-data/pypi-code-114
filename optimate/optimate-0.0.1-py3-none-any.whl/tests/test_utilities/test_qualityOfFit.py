#!/usr/bin/env python3

# @file test_qualityOfFit.py
# @author Muhammad Mohsin Khan

# This class provides test for
# the qualityOfFit's function.

# Python import commands
import numpy as np
import time
from numpy.testing import assert_almost_equal

# Optimate import
from optimate.utilities import qualityOfFit as qof


class TestQualityOfFit():

    """
    Basic test class for qualityOfFit.py.
    """


    def test_QoF(self):

        """
        Test function for QoF().
        """

        x = np.array([[1. , 0.1],
                      [2. , 0.2],
                      [3. , 0.3]])
        
        y = np.array([[1.  , 0.11],
                      [2.  , 0.22],
                      [3.  , 0.33]])

        exp = {0: x}
        sim = {0: y}
        
        test = 83.97315692739596
        res = qof.QoF(exp, sim)
        assert_almost_equal(res, test, decimal=8)
