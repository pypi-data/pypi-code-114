import math
import numbers

import numpy as np

from .base_space import BaseSpace

def old_div(a, b):
    """
    DEPRECATED: import ``old_div`` from ``past.utils`` instead.

    Equivalent to ``a / b`` on Python 2 without ``from __future__ import
    division``.

    TODO: generalize this to other objects (like arrays etc.)
    """
    if isinstance(a, numbers.Integral) and isinstance(b, numbers.Integral):
        return a // b
    else:
        return a / b

class PBTSpace(BaseSpace):

    def __init__(self, search_space = None):
        self.library = 'pbt'
        super().__init__(search_space)    
        
    def reset_space(self):
        self.search_space = {}

    def append(self, space_value):
        self.search_space[space_value[0]] = space_value[1]

    def categorical(self, label, categories, grid_search = False):
        return (label, categories)

    def uniform(self, label, low, high):
        return (label, lambda: np.random.uniform(low, high))
    
    def uniformint(self, label, low, high):
        return (label, lambda : np.random.randint(low, high))

    def loguniform(self, label, low, high, base=10):
        logmin = math.log(low) / math.log(base)
        logmax = math.log(high) / math.log(base)
        return (label, lambda: base**(np.random.uniform(logmin, logmax)))

    def qloguniform(self, label, low, high, base=10):
        logmin = math.log(low) / math.log(base)
        logmax = math.log(high) / math.log(base)
        return (label, lambda: 
            round(old_div(base**(np.random.uniform(logmin, logmax)),q))*q)

    def quniform(self, label, low, high, q):
        return (labelm, lambda: 
            round(old_div(np.random.uniform(low, high),q))*q)

    def quniformint(self, label, low, high, q):
        return (label, lambda : 
            round(old_div(np.random.uniform(low, high),q))*q)

    def normal(self, mu, sigma):
        return (label, lambda : sigma*np.random.randn()+mu)

    def qnormal(self, mu, sigma, q):
        return (label, lambda : 
            round(old_div(sigma*np.random.randn()+mu,q))*q)

    def lognormal(self, mu, sigma, base=math.e):
        return (label, lambda : 
            math.pow(sigma*np.random.randn()+mu, base))

    def qlognormal(self, mu, sigma, q, base=math.e):
        return (label, lambda _: 
            round(old_div(math.pow(sigma*np.random.randn()+mu, base),q))*q )    

    def fixed(self, value):
        return (label, [value])