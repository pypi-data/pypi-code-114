#!/usr/bin/python
# -*- coding: utf-8 -*-
from .orth import orth
import numpy as np
from .matlab_like import rand
def orthbase(lin,col):
    if lin != col:
        Ro = orth(rand(lin,col+1))
        mret = Ro[:,1:]
    else:
        mret = orth(rand(lin,col))
    return np.array(mret)