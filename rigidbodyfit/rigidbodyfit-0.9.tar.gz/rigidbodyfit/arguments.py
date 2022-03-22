""" Define and retrieve all command line options.
"""

import argparse


def get_command_line_arguments(version: str):
    """build, parse and return command line arguments

    Args:
        version (str): the current program version

    Returns:
        the parsed command line arguments
    """

    program_name = "rigidbodyfit"
    description = ("")

    parser = argparse.ArgumentParser(
        description=description,
        prog=program_name,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--structure",
                        required=True,
                        help="input pdb structure filename",
                        metavar="input.pdb")

    parser.add_argument("--density",
                        required=True,
                        help="input mrc density filename",
                        metavar="input.mrc")

    parser.add_argument("--output-structure",
                        nargs='?',
                        default='fitted.pdb',
                        help="file to write the fitted structure to.",
                        metavar="fitted.pdb")

    parser.add_argument("--output-transform",
                        nargs='?',
                        const='transform.dat',
                        type=argparse.FileType('w'),
                        help="",
                        metavar="transform.dat")

    parser.add_argument(
        "--threshold",
        type=float,
        default=0.05,
        help="discard all data smaller than threshold * max(voxel value).")

    parser.add_argument(
        "--sampling-depth",
        type=int,
        default=7,
        help=
        "breadth of search with initial configurations. The higher the slower, but more accurate."
    )

    parser.add_argument("--version",
                        action="version",
                        version=(f"{program_name} {version}"))

    return parser.parse_args()
