# c and s are the parameters for the command line arguments that are required
# click is a library to create this whole command line tool
import glob
import os.path
import sys

import click

from stepfunction_validator.stepfunction_validator import (
    StepFunctionValidator,
    StepFunctionValidatorException,
)


@click.command()
@click.option(
    "-s",
    "--step-function-file",
    help="Your stepfunctions YAML file, will take all .yml / .yaml in current dir if empty or if a directory is passed",
)
@click.option(
    "-j",
    "--json-schema-file",
    default="",
    help="Optionally, the JSON step function schema (or any other schema)",
)
@click.option("--lint/--no-lint", default=True)
def main(step_function_file, json_schema_file=None, lint=True):
    """
    YAML validator for the CLI

    Example: python app.py -c <test.yaml> [-s <stepfunctions_schema.json>]
    This will validate a YAML file against the schema you provided in CLI

    Created by Nilesh
    https://github.com/NileshDebix
    """

    # Load the json_file from the command line that was given as a argument
    try:
        stepfunction_validator = StepFunctionValidator(
            json_schema_file=json_schema_file, yaml_linting=lint
        )
    except StepFunctionValidatorException as e:
        print(e)
        sys.exit(1)

    good_result = True
    if step_function_file:
        if not os.path.exists(step_function_file):
            print("YAML file " + step_function_file + " not found")
            ctx = click.get_current_context()
            click.echo(ctx.get_help())
            sys.exit(1)
        if os.path.isdir(step_function_file):
            yamls = glob.glob(step_function_file + "/*.yml")
        else:
            yamls = [step_function_file]
    else:
        yamls = glob.glob("./*.yml")
        if not yamls:
            print("No YAML files found in the current directory")
            ctx = click.get_current_context()
            click.echo(ctx.get_help())
            sys.exit(1)

    for yaml in yamls:
        result = stepfunction_validator.validate(yaml)
        if lint:
            if result.get("linting"):
                good_result = False
                for lint_line in result.get("linting"):
                    print(lint_line)
        if result.get("error"):
            good_result = False
            print(result.get("error"))

    if good_result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
