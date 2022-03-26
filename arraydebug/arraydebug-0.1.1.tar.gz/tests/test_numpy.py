import numpy as np
import unittest
from inspect import cleandoc

import arraydebug  # noqa


class TestNumpy(unittest.TestCase):
    def setUp(self) -> None:
        arraydebug.register_reprs()
        arraydebug.inject_repr()

    def test_1D(self):
        """
        <ndarray: shape=(4,), dtype=int64>
        array([0, 1, 2, 3])
        """
        arr = np.arange(4)
        self.assertEqual(repr(arr), cleandoc(self.test_1D.__doc__))

    def test_1D_long(self):
        """
        <ndarray: shape=(10000,), dtype=float32>
        array([0.000e+00, 1.000e+00, 2.000e+00, ..., 9.997e+03, 9.998e+03,
               9.999e+03], dtype=float32)
        """
        arr = np.arange(10000, dtype=np.float32)
        self.assertEqual(repr(arr), cleandoc(self.test_1D_long.__doc__))

    def test_2D(self):
        """
        <ndarray: shape=(3, 4), dtype=int64>
        array([[ 0,  1,  2,  3],
               [ 4,  5,  6,  7],
               [ 8,  9, 10, 11]])
        """
        arr = np.arange(3 * 4).reshape(3, 4)
        self.assertEqual(repr(arr), cleandoc(self.test_2D.__doc__))

    def test_2D_long(self):
        """
        <ndarray: shape=(100, 100), dtype=int64>
        array([[   0,    1,    2, ...,   97,   98,   99],
               [ 100,  101,  102, ...,  197,  198,  199],
               [ 200,  201,  202, ...,  297,  298,  299],
               ...,
               [9700, 9701, 9702, ..., 9797, 9798, 9799],
               [9800, 9801, 9802, ..., 9897, 9898, 9899],
               [9900, 9901, 9902, ..., 9997, 9998, 9999]])
        """
        arr = np.arange(10000).reshape(100, 100)
        self.assertEqual(repr(arr), cleandoc(self.test_2D_long.__doc__))
