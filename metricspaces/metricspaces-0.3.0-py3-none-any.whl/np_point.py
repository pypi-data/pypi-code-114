"""
A basic point class wrapping a numpy array.
"""


import numpy as np

class NumpyPoint:
    def __init__(self, point):
        self.point = point
        self.hash = hash(str(point))

    def __hash__(self):
        return self.hash

    def distsq(self, other):
        return sum((a-b)**2 for a,b in zip(self.point,other.point))

    def dist(self, other):
        return self.distsq(other) ** (0.5)
