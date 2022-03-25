import re
import unittest
import sys
import random

import httpretty
import numpy as np
import pandas as pd
import pytest

import feyn._httpclient
import feyn.filters
import feyn.losses
from feyn import fit_models, prune_models
from feyn._qlattice import connect_qlattice

from test import quickmodels


@pytest.mark.integration
class TestSDK(unittest.TestCase):
    def test_qlattice_init_arguments_validation(self):
        with self.subTest("raises if config is combined with qlattice or token"):
            with self.assertRaises(ValueError):
                connect_qlattice(config="section", qlattice="qlattice-id", api_token="token")

            with self.assertRaises(ValueError):
                connect_qlattice(config="section", qlattice="qlattice-id")

            with self.assertRaises(ValueError):
                connect_qlattice(config="section", api_token="token")

        with self.subTest("raises if only token is specified"):
            with self.assertRaises(ValueError):
                connect_qlattice(api_token="token")

        with self.subTest("raises if only api_token is missing by qlattice is specified"):
            with self.assertRaises(ValueError):
                connect_qlattice(qlattice="qlattice-id")

    def test_can_sample_classification_models_from_qlattice(self):
        lt = connect_qlattice()
        lt.reset()
        models = lt.sample_models(["age", "smoker", "sex"], "charges", kind="classification", max_complexity=2)

        self.assertTrue(models)

    def test_can_sample_regression_models_from_qlattice(self):
        lt = connect_qlattice()
        lt.reset()
        models = lt.sample_models(["age", "smoker", "sex"], "charges", kind="regression", max_complexity=2)

        self.assertTrue(models)

    def test_empty_dic_can_be_passed_to_stypes(self):
        lt = connect_qlattice()
        lt.reset()
        models = lt.sample_models(
            ["age", "smoker", "sex"],
            "charges",
            kind="regression",
            max_complexity=2,
            stypes={},
        )

        self.assertTrue(models)

    def test_fit_models(self):
        models = [quickmodels.get_simple_binary_model(["age", "smoker"], "insurable")]

        data = pd.DataFrame(
            {
                "age": np.array([10, 16, 30, 60]),
                "smoker": np.array([0, 1, 0, 1]),
                "insurable": np.array([1, 1, 1, 0]),
            }
        )

        with self.subTest("Can fit with default arguments and increment sample_count"):
            fit_models(models, data, n_samples=4)
            self.assertEqual(models[0]._sample_count, 4)

        with self.subTest("Can fit with named loss function"):
            fit_models(models, data, loss_function="absolute_error", n_samples=4)

        with self.subTest("Can fit with sample weights as list of floats"):
            fit_models(models, data, sample_weights=[1.0, 2.0, 3.0, 4.0], n_samples=4)

        with self.subTest("Can fit with sample weights as np.array"):
            fit_models(models, data, sample_weights=np.array([1.0, 2.0, 3.0, 4.0]), n_samples=4)

    def test_lattice_auto_run_works(self):
        lt = connect_qlattice()
        lt.reset()

        data = pd.DataFrame(
            {
                "age": np.array([10, 16, 30, 60]),
                "smoker": np.array([0, 1, 0, 1]),
                "insurable": np.array([1, 1, 1, 0]),
            }
        )

        best_models = lt.auto_run(
            data,
            "insurable",
            max_complexity=2,
            function_names=["exp", "log"],
            n_epochs=1,
        )
        self.assertTrue(best_models)

    def test_auto_run_all_parameters(self):
        """Run auto_run with all parameters specified"""

        lt = connect_qlattice()
        lt.reset()

        data = pd.DataFrame(
            {"age": np.array([1, 2, 3]), "smoker": np.array([0, 0, 1]), "insurable": np.array([0, 0.2, 0.4])}
        )
        stypes = {"smoker": "c"}

        starting_models = [quickmodels.get_specific_model(inputs=["age", "smoker"], output='insurable', equation="'age'+('age'*'smoker')")]

        models = lt.auto_run(
            data=data,
            output_name="insurable",
            kind="regression",
            stypes=stypes,
            n_epochs=1,
            threads=2,
            max_complexity=8,
            query_string="'age' + 'smoker'",
            loss_function="absolute_error",
            criterion="aic",
            sample_weights=[random.random() for _ in range(len(data))],
            function_names=["add", "multiply", "sqrt", "gaussian"],
            starting_models = starting_models,
        )

    def test_lattice_auto_run_validates_data(self):
        lt = connect_qlattice()
        lt.reset()

        data = pd.DataFrame(
            {"age": np.array([1, 2, 3]), "smoker": np.array([0, 0, 1]), "insurable": np.array([0, 0.2, 0.4])}
        )
        with self.assertRaises(ValueError):
            models = lt.auto_run(data, "insurable", "classification", max_complexity=2, n_epochs=1)

    @pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
    def test_prune_keep_n_as_npint_raises(self):
        lt = connect_qlattice()
        models = [quickmodels.get_simple_binary_model(["x", "y"], "z")]
        keep_n = np.int_(5)
        with self.assertRaises(TypeError):
            prune_models(models, keep_n=keep_n)

    def test_reproducible_auto_run(self):
        data = pd.DataFrame(
            {
                "age": np.array([10, 16, 30, 60]),
                "smoker": np.array(['no', 'yes', 'no', 'yes']),
                "insurable": np.array([1, 1, 1, 0]),
            }
        )
        stypes = {"smoker": "c"}
        lt = connect_qlattice()

        lt.reset(random_seed=31)
        first_models = lt.auto_run(
            data,
            "insurable",
            stypes=stypes,
            max_complexity=3,
            n_epochs=1,
            query_string="'age' * 'smoker'"
        )

        lt.reset(random_seed=31)
        second_models = lt.auto_run(
            data,
            "insurable",
            stypes=stypes,
            max_complexity=3,
            n_epochs=1,
            query_string="'age' * 'smoker'"
        )

        self.assertEqual(first_models, second_models)

    def test_update_lattice_with_models(self):
        lt = connect_qlattice()
        lt.reset()
        models = lt.sample_models(["age", "smoker", "insurable"], "insurable", max_complexity=2)

        with self.subTest("Can update with several models"):
            lt.update(models[:10])

        with self.subTest("Can update with empty list"):
            lt.update([])

    def test_can_sample_models_with_any_column_as_output(self):
        lt = connect_qlattice()
        lt.reset()
        columns = ["age", "smoker"]
        for target in columns:
            models = lt.sample_models(columns, target, max_complexity=2)
            self.assertTrue(models)

    def test_can_sample_models_with_function_names(self):
        lt = connect_qlattice()
        lt.reset()
        columns = ["age", "smoker"]
        fnames = ['exp', 'log']

        models = lt.sample_models(columns, 'smoker', max_complexity=2, function_names=fnames)
        self.assertTrue(models)

    def test_can_sample_models_with_gaussian(self):
        lt = connect_qlattice()
        lt.reset()
        columns = ["age", "smoker"]
        fnames = ['gaussian']

        models = lt.sample_models(columns, 'smoker', max_complexity=2, function_names=fnames)
        self.assertTrue(models)

    def test_can_sample_models_with_query(self):
        lt = connect_qlattice()
        lt.reset()
        models = lt.sample_models(list("xy"), "out", max_complexity=3, query_string="'x' + 'y'")

        add_code = lt.context.lookup_by_fname("add", 2)
        expected_seq = [add_code, 10000, 10001]
        self.assertTrue(expected_seq, models[0]._program[:3])

    def test_cant_sample_models_with_complex_query(self):
        lt = connect_qlattice()
        lt.reset()

        with self.assertRaises(ValueError):
            _ = lt.sample_models(list("xy"), "out", max_complexity=3, query_string="'x' + func('y')")

    def test_model_fitting(self):
        lt = connect_qlattice()
        lt.reset()
        models = lt.sample_models(
            ["age", "smoker", "insurable"],
            "insurable",
            max_complexity=2,
            kind="classification",
        )[:5]

        data = pd.DataFrame(
            {
                "age": np.array([10, 16, 30, 60]),
                "smoker": np.array([0, 1, 0, 1]),
                "insurable": np.array([1, 1, 1, 0]),
            }
        )

        with self.subTest("Fitted list is sorted by loss"):
            fitted_models = fit_models(models, data, n_samples=4)
            explicitly_sorted = sorted([m.loss_value for m in fitted_models], reverse=False)
            fitted_losses = [m.loss_value for m in fitted_models]
            for esl, fl in zip(explicitly_sorted, fitted_losses):
                self.assertAlmostEqual(esl, fl)

        with self.subTest("Can provide the name of a loss function"):
            fitted_with_ae = fit_models(models, data, loss_function="absolute_error", n_samples=4)
            explicitly_sorted = sorted([m.loss_value for m in fitted_with_ae], reverse=False)
            fitted_losses = [m.loss_value for m in fitted_with_ae]
            for esl, fl in zip(explicitly_sorted, fitted_losses):
                self.assertAlmostEqual(esl, fl)

    def test_retries_failed_requests(self):

        with httpretty.enabled():
            # Ideally we would have liked to just mock out the update http call.
            # But it is not possible in httpretty. And at same time, we are
            # creating the socket through request.session and init time of the
            # qlattice. So this socket cannot be highjacked by httpretty.
            # See this: https://github.com/gabrielfalcao/HTTPretty/issues/381
            http_client = feyn._httpclient.HttpClient("http://example.org/api")
            http_client.get_adapter("http://").max_retries.backoff_factor = 0.1  # Instant retries

            httpretty.register_uri(httpretty.POST, re.compile(r"http://.*"), status=502)

            req = http_client.post("/reset", json={"seed": 42})
            self.assertEqual(req.status_code, 502)

            self.assertEqual(len(httpretty.latest_requests()), 3, "Did not retry the failed requests")

    def test_DataFrame_as_input_names(self):
        lt = connect_qlattice()
        lt.reset()
        input_names = pd.DataFrame({"smoker": [1, 2, 3, 4], "age": [5, 6, 7, 10], "target": [6, 8, 10, 12]})
        output_name = "target"

        models = lt.sample_models(input_names, output_name)
        self.assertIsNotNone(models[0])
