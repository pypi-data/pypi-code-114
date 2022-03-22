#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from .matlab_like import svd,diag,eps,size
def orth(A):
    Q,S=svd(A)
    S=diag(S)
    tol = max(size(A)) * S[0] * eps('double')
    r = sum(S > tol)
    Q = Q[:,0:r]
    return Q