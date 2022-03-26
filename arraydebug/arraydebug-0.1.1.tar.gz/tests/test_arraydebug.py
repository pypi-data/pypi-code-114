#!/usr/bin/env python

"""Tests for `arraydebug` package."""

import numpy as np
import unittest
import arraydebug


class TestArraydebug(unittest.TestCase):
    def setUp(self) -> None:
        arraydebug.register_reprs()
        arraydebug.inject_repr()

    def tearDown(self) -> None:
        arraydebug.inject_repr()

    def test(self):
        self.assertEqual(repr(1), "1")
        self.assertEqual(repr("abc"), "'abc'")
        self.assertEqual(repr([1, 2, 3, 4]), "[1, 2, 3, 4]")

    def test_recover_repr(self):
        arr = np.arange(4)

        arraydebug.inject_repr()
        self.assertEqual(repr(arr), "<ndarray: shape=(4,), dtype=int64>\narray([0, 1, 2, 3])")

        arraydebug.recover_repr()
        self.assertEqual(repr(arr), "array([0, 1, 2, 3])")
