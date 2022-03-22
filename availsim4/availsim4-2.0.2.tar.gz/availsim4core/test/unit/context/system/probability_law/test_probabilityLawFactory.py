# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import unittest

from availsim4core.src.context.system.probability_law.deterministic_law import DeterministicLaw
from availsim4core.src.context.system.probability_law.exponential_law import ExponentialLaw
from availsim4core.src.context.system.probability_law.normal_law import NormalLaw
from availsim4core.src.context.system.probability_law.probability_law_factory import ProbabilityLawFactory, \
    ProbabilityLawFactoryError


class test_probabilityLawFactory(unittest.TestCase):

    def test_build_ExponentialLaw(self):
        distribution_str = "EXP"
        parameters = []
        result = ProbabilityLawFactory.build(distribution_str, parameters)
        self.assertEqual(ExponentialLaw([]), result)

        distribution_str = "EXPONENTIAL"
        parameters = [2, 0]
        result = ProbabilityLawFactory.build(distribution_str, parameters)
        self.assertEqual(ExponentialLaw([2, 0]), result)

    def test_build_NormalLaw(self):
        distribution_str = "NORMAL"
        parameters = []
        result = ProbabilityLawFactory.build(distribution_str, parameters)
        self.assertEqual(NormalLaw([]), result)

    def test_build_DeterministicLaw(self):
        distribution_str = "FIX"
        parameters = []
        result = ProbabilityLawFactory.build(distribution_str, parameters)
        self.assertEqual(DeterministicLaw([]), result)

        distribution_str = "DETERMINISTIC"
        parameters = [2, 3]
        result = ProbabilityLawFactory.build(distribution_str, parameters)
        self.assertEqual(DeterministicLaw([2, 3]), result)

    def test_build_invalid_probability_law(self):
        distribution_str = "invalid"
        parameters = []
        with self.assertRaises(ProbabilityLawFactoryError) as context:
            ProbabilityLawFactory.build(distribution_str, parameters)
        self.assertTrue('wrong type of distribution function' in str(context.exception))
