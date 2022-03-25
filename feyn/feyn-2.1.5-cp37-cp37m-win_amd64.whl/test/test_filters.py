import unittest

import feyn
from . import quickmodels

class TestExcludeFunctions(unittest.TestCase):
    def setUp(self):
        self.test_models = [
            quickmodels.get_unary_model(["x"], "y", fname=fname)
            for fname in ["gaussian1", "exp", "log"]
        ]

    def test_exclude_single_function_filter(self):
        f = feyn.filters.ExcludeFunctions("gaussian1")
        self.assertEqual(2, len(list(filter(f, self.test_models))))

    def test_multiple_function_exclusion(self):
        f = feyn.filters.ExcludeFunctions(["gaussian1", "exp"])
        self.assertEqual(1, len(list(filter(f, self.test_models))))


class TestComplexity(unittest.TestCase):
    def test_complexity_filter(self):
        test_models = [
            quickmodels.get_unary_model(["x"], "y", fname=fname)
            for fname in ["gaussian1", "exp"]
        ]

        test_models += [quickmodels.get_simple_binary_model(["x","y"],"z")]

        f = feyn.filters.Complexity(3)
        self.assertEqual(1, len(list(filter(f, test_models))))


class TestContainsInput(unittest.TestCase):
    def test_contains_filter(self):
        models = [
            quickmodels.get_simple_binary_model(["x", name], "y") for name in ["cheese", "kase", "ost"]
        ]


        f = feyn.filters.ContainsInputs("kase")
        self.assertEqual(1, len(list(filter(f, models))))



class TestContainsFunctions(unittest.TestCase):
    def test_contains_filter(self):
        test_models = [
            quickmodels.get_unary_model(["x"], "y", fname=fname)
            for fname in ["gaussian1", "exp", "log"]
        ]

        test_models += [
            quickmodels.get_complicated_binary_model(["x","y"], "z", fname)
            for fname in ["exp", "log"]
        ]

        with self.subTest("Check for model built with single function."):
            f = feyn.filters.ContainsFunctions("log")
            self.assertEqual(1, len(list(filter(f, test_models))))

        with self.subTest("Check for model built with list of functions."):
            f = feyn.filters.ContainsFunctions(["add", "exp"])
            self.assertEqual(1, len(list(filter(f, test_models))))



