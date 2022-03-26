import torch
import unittest
from inspect import cleandoc

import arraydebug  # noqa


class TestTorch(unittest.TestCase):
    def setUp(self) -> None:
        arraydebug.register_reprs()
        arraydebug.inject_repr()

    def test_1D(self):
        """
        <Tensor: shape=(4,), dtype=int64, device='cpu'>
        tensor([0, 1, 2, 3])
        """
        arr = torch.arange(4)
        self.assertEqual(repr(arr), cleandoc(self.test_1D.__doc__))

    def test_1D_long(self):
        """
        <Tensor: shape=(10000,), dtype=float32, device='cpu'>
        tensor([0.0000e+00, 1.0000e+00, 2.0000e+00,  ..., 9.9970e+03, 9.9980e+03,
                9.9990e+03])
        """
        arr = torch.arange(10000, dtype=torch.float32)
        self.assertEqual(repr(arr), cleandoc(self.test_1D_long.__doc__))

    def test_2D(self):
        """
        <Tensor: shape=(3, 4), dtype=int64, device='cpu'>
        tensor([[ 0,  1,  2,  3],
                [ 4,  5,  6,  7],
                [ 8,  9, 10, 11]])
        """
        arr = torch.arange(3 * 4).reshape(3, 4)
        self.assertEqual(repr(arr), cleandoc(self.test_2D.__doc__))

    def test_2D_long(self):
        """
        <Tensor: shape=(100, 100), dtype=int64, device='cpu'>
        tensor([[   0,    1,    2,  ...,   97,   98,   99],
                [ 100,  101,  102,  ...,  197,  198,  199],
                [ 200,  201,  202,  ...,  297,  298,  299],
                ...,
                [9700, 9701, 9702,  ..., 9797, 9798, 9799],
                [9800, 9801, 9802,  ..., 9897, 9898, 9899],
                [9900, 9901, 9902,  ..., 9997, 9998, 9999]])
        """
        arr = torch.arange(10000).reshape(100, 100)
        self.assertEqual(repr(arr), cleandoc(self.test_2D_long.__doc__))

    def test_requires_grad(self):
        """
        <Tensor: shape=(3, 4), dtype=float64, device='cpu', requires_grad=True>
        tensor([[ 0.,  1.,  2.,  3.],
                [ 4.,  5.,  6.,  7.],
                [ 8.,  9., 10., 11.]], dtype=torch.float64, requires_grad=True)
        """
        arr = torch.arange(3 * 4, dtype=torch.float64).reshape(3, 4)
        arr.requires_grad_(True)
        self.assertEqual(repr(arr), cleandoc(self.test_requires_grad.__doc__))
