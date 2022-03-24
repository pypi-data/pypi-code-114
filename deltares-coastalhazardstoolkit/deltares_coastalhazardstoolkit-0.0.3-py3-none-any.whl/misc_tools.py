# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:28:15 2021

@author: ormondt
"""

from scipy.interpolate import RegularGridInterpolator
import numpy as np

def interp2(x0,y0,z0,x1,y1):
    
    f = RegularGridInterpolator((y0, x0), z0,
                                bounds_error=False, fill_value=np.nan)    
    # reshape x1 and y1
    sz = x1.shape
    x1 = x1.reshape(sz[0]*sz[1])
    y1 = y1.reshape(sz[0]*sz[1])    
    # interpolate
    z1 = f((y1,x1)).reshape(sz)        
    
    return z1

def findreplace(file_name, str1, str2):

    #read input file
    fin = open(file_name, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    data = data.replace(str1, str2)
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(file_name, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()