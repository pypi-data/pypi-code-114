from os.path import abspath, dirname, join, isfile, normpath, relpath
from pandas.testing import assert_frame_equal
import xarray.testing as xrt
from numpy.testing import assert_allclose
from scipy.interpolate import interp1d
import matplotlib.pylab as plt
from datetime import datetime
import mhkit.wave as wave
from io import StringIO
import pandas as pd
import numpy as np
import contextlib
import unittest
import netCDF4
import inspect
import pickle
import json
import sys
import os
import time
from random import seed, randint

testdir = dirname(abspath(__file__))
datadir = normpath(join(testdir,relpath('../../examples/data/wave')))


class TestResourceSpectrum(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        omega = np.arange(0.1,3.5,0.01)
        self.f = omega/(2*np.pi)
        self.Hs = 2.5
        self.Tp = 8
        df = self.f[1] - self.f[0]
        Trep = 1/df
        self.t = np.arange(0, Trep, 0.05)
            
    @classmethod
    def tearDownClass(self):
        pass
    
    def test_pierson_moskowitz_spectrum(self):
        S = wave.resource.pierson_moskowitz_spectrum(self.f,self.Tp,self.Hs)
        Tp0 = wave.resource.peak_period(S).iloc[0,0]
        
        error = np.abs(self.Tp - Tp0)/self.Tp
        
        self.assertLess(error, 0.01)
           
    def test_jonswap_spectrum(self):
        S = wave.resource.jonswap_spectrum(self.f, self.Tp, self.Hs)
        Hm0 = wave.resource.significant_wave_height(S).iloc[0,0]
        Tp0 = wave.resource.peak_period(S).iloc[0,0]
        
        errorHm0 = np.abs(self.Tp - Tp0)/self.Tp
        errorTp0 = np.abs(self.Hs - Hm0)/self.Hs
        
        self.assertLess(errorHm0, 0.01)
        self.assertLess(errorTp0, 0.01)
    
    def test_plot_spectrum(self):            
        filename = abspath(join(testdir, 'wave_plot_spectrum.png'))
        if isfile(filename):
            os.remove(filename)
        
        S = wave.resource.pierson_moskowitz_spectrum(self.f,self.Tp, self.Hs)
        
        plt.figure()
        wave.graphics.plot_spectrum(S)
        plt.savefig(filename, format='png')
        plt.close()
        
        self.assertTrue(isfile(filename))

if __name__ == '__main__':
    unittest.main() 