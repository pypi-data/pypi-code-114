import click
import antlr4

from .parser.CLexer import CLexer
from .parser.CParser import CParser

import c_syntax_validator as validator


@click.option(
    "--target",
    default="file",
    type=click.Choice([tgt.value for tgt in validator.InputTarget]),
    help="The type of source to parse (ie. expr/stmt/file)",
)
@click.argument("inputfile", type=click.File("rt"))
@click.command()
def c_syntax_validator(target, inputfile):
    """A parser/validator for C syntax"""
    try:
        validator.validate_text(inputfile.read(), validator.InputTarget(target))
    except validator.InvalidCodeException as f:
        raise click.ClickException(str(f))


if __name__ == "__main__":
    c_syntax_validator()
