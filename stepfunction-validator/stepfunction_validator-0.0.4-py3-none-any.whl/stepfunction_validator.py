import json
import os
import re

import yaml
from yaml import FullLoader
import yamllint
from yamllint import linter, config
from jsonschema import Draft7Validator, Draft3Validator, validate
from jsonschema.exceptions import best_match


class StepFunctionValidatorException(Exception):
    pass


class StepFunctionValidator:
    def __init__(self, json_schema_file=None, yaml_linting=False):
        if not json_schema_file:
            schema_path = os.path.dirname(os.path.realpath(__file__))
            json_schema_file = os.path.join(schema_path, "stepfunctions_schema.json")
        self.json_schema_file = json_schema_file
        self.yaml_linting = yaml_linting
        self.yaml_config = yamllint.config.YamlLintConfig("extends: default")

    @staticmethod
    def _load_json_schema(json_schema_file):
        with open(json_schema_file) as f:
            json_schema = json.load(f)
        return json_schema

    @staticmethod
    def _load_yaml(yaml_file):
        with open(yaml_file, "r") as f:
            step_function_yaml = yaml.load(f, Loader=FullLoader)
        return step_function_yaml

    def _lint_yaml(self, yaml_file):
        return yamllint.linter.run(yaml_file, self.yaml_config)

    def _validate_stepfunction(self, yamldata, json_schema):
        v = Draft7Validator(json_schema)
        errors = sorted(v.iter_errors(yamldata), key=lambda e: e.path)
        return errors

    def _linting(self, step_function_file):
        linting_results = self._lint_yaml(step_function_file)
        return [
            f"{step_function_file}:{line.line}:{line.desc} ({line.rule})"
            for line in linting_results
        ]

    def _format_validate_error(self, step_function_file, validation_error):
        formatted_error = (
            f"{step_function_file}:{validation_error.message}. Failed validating"
            f" {validation_error.validator} in {validation_error.schema_path}: {validation_error.schema}"
        )
        return formatted_error

    def _validate_files(self, *filenames):
        for test_file in filenames:
            if not os.path.exists(test_file):
                raise StepFunctionValidatorException(
                    "File " + test_file + " does not exist"
                )
            if not os.access(test_file, os.R_OK):
                raise StepFunctionValidatorException(
                    "File " + test_file + " could not be read"
                )

    def validate(self, step_function_file):
        result = {}
        self._validate_files(step_function_file, self.json_schema_file)

        error = None

        try:
            yaml_dict = self._load_yaml(step_function_file)
        except yaml.parser.ParserError as e:
            flat_error = re.sub("\\s+", " ", str(e))
            error = f"{step_function_file}:{flat_error}"

        if not error:
            if self.yaml_linting:
                result["linting"] = self._linting(step_function_file)

            schema = self._load_json_schema(self.json_schema_file)
            validate_results = self._validate_stepfunction(yaml_dict, schema)
            raw_error = best_match(validate_results)
            if raw_error:
                error = self._format_validate_error(step_function_file, raw_error)

        if error:
            result["error"] = error
        return result
