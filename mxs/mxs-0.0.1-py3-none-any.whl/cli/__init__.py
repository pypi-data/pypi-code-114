"""
MXS is the Math eXploration Solver.
Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com


    mxs [args] [<command>] [<args>]

    mxs pattern --pv  # Reslove the position and value of an atom
                        within a line pattern
"""
import argparse

from mxs.__version__ import __version__
from .error import ExitCode
from .solvers import pattern_solver

# create the top-level parser
parser = argparse.ArgumentParser(
    prog='mxs',
    description='Use mxs to explore solutions for math problems.',
    conflict_handler='resolve',
    formatter_class=argparse.RawTextHelpFormatter,
    epilog='\n \n',
)

parser.add_argument(
    '-j', '--json',
    action='store_true',
    dest='json',
    help='Output the result set in JSON'
)

parser.add_argument(
    '--version',
    action='version',
    version='%(prog)s ' + f'version { __version__}'
)

# Add subparser below for each mxs command
subparsers = parser.add_subparsers(
    title='mxs commands',
)

# create the parser for the "pattern" command
parser_pattern = subparsers.add_parser(
    'pattern',
    formatter_class=argparse.RawTextHelpFormatter,
    help='solve a problem involving a pattern'
)

parser_pattern.add_argument(
    'problem',
    choices=[
        'pv',
    ],
    metavar='problem',
    help=('The type of pattern problem to solve.'
          ' Choices include pv (position/value).')
)

parser_pattern.set_defaults(func=pattern_solver)

args_optional = set(
    {
        'json': None
    }
)


def main():
    args = parser.parse_args() or None
    # logger.info(f"cli args: {vars(args)}")
    args_given = set(vars(args))
    check = args_given ^ args_optional

    if len(check) > 0:
        try:
            args.func(args)
        except SystemExit as e:
            return e.code
        else:
            return ExitCode.EX_SUCCESS
    else:
        parser.print_help()
        return ExitCode.EX_USAGE
