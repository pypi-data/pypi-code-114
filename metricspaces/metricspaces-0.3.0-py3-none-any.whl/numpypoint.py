"""
A basic point class wrapping a numpy array.
"""

import numpy as np

def L_p(p):
    class Point:
        def __init__(self, point):
            self.point = point
            self.hash = hash(str(point))

        def __hash__(self):
            return self.hash

        if p == 2:
            def distsq(self, other):
                return sum((a-b)**2 for a,b in zip(self, other))

        if p == 'inf':
            def dist(self, other):
                return max(abs(a-b) for a,b in zip(self, other))
        else:
            def dist(self, other):
                d = sum(abs(a-b)**p for a,b in zip(self, other))
                return d ** (1/p)

        def __str__(self):
            return str(self.point)

        def __iter__(self):
            return iter(self.point)
    return Point

NumpyPoint = L_p(2)
