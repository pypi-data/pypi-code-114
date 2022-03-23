import unittest

import jsonschema
import yaml

from stepfunction_validator.stepfunction_validator import (
    StepFunctionValidatorException,
    StepFunctionValidator,
)


class TestValidation(unittest.TestCase):
    def setUp(self):
        self.stepfunction_validator = StepFunctionValidator()

    def test_ValidStepFunction(self):
        result = self.stepfunction_validator.validate(
            "test_scenarios/step_function.yml"
        )
        self.assertEqual(result.get("error"), None)

    def test_InvalidStepFunction(self):
        result = self.stepfunction_validator.validate(
            "test_scenarios/step_function_invalid.yml"
        )
        self.assertIsNotNone(result.get("error"), None)

    def test_SyntaxErrorStepFunction(self):
        result = self.stepfunction_validator.validate(
            "test_scenarios/step_function_syntax.yml"
        )
        self.assertIsNotNone(result.get("error"), None)
