import unittest

import numpy as np
import pandas as pd

import feyn

from . import quickmodels
from feyn._qepler import qeplertrainer

class TestTrainer(unittest.TestCase):

    def test_fit_initializes_scale(self):
        model = quickmodels.get_unary_model(["input"], "y")

        # Should not raise
        losses, params = qeplertrainer.fit_models([model], pd.DataFrame({
                "input": np.array([42, 0, 100, 50]),
                "y": np.array([0.1, 0.3, 0.2, 0.9])
            }), 10000, loss="squared_error")

        # self.assertNotEqual(losses[0], 0)

        input_element = params[0][2]
        self.assertEqual(input_element["scale"], .02)

        self.assertEqual(params[0][0]["scale"], 0.4)

    def xtest_reproduces_memory_leak(self):

        for iteration in range(1000):
            # Should not raise
            print(f"Iteration {iteration}")
            models = [quickmodels.get_unary_model(["input"], "y") for  _ in range(5)]

            losses, params = qeplertrainer.fit_models(models, pd.DataFrame({
                    "input": np.array([42, 0, 100, 50]),
                    "y": np.array([0.1, 0.3, 0.2, 0.9])
                }), 1000000, loss="squared_error")

    def test_fit_models_checks_output_stypes(self):
        regression_model = quickmodels.get_unary_model()
        classification_model = quickmodels.get_unary_model(stypes={"y": "b"})
        data = pd.DataFrame.from_dict({
            "x": np.array([1, 2, 3]),
            "y": np.array([0.3, 0.2, 0.5]),
        })

        with self.assertRaises(ValueError):
            feyn.fit_models([regression_model, classification_model], data)

        feyn.fit_models([regression_model], data)
        feyn.fit_models([classification_model], data)

