from optparse import OptionParser
from .version import version


def arg_parser():
    parser = OptionParser(version=version)
    parser.add_option(
        "-d",
        "--decrypt",
        action="store_true",
        dest="decrypt",
        default=False,
        help="decrypt file",
    )
    parser.add_option(
        "-g",
        "--gen-key",
        action="store_true",
        dest="gen_key",
        default=None,
        help="generate a random encryption key",
    )
    parser.add_option(
        "-o",
        "--output-file",
        action="store",
        dest="output_filename",
        default=None,
        help="write to output file instead of stdout",
    )
    parser.add_option(
        "-k",
        "--key-env",
        action="store",
        dest="key_env",
        default=None,
        help="environment variable name containing the encryption key",
    )
    parser.add_option(
        "-f",
        "--force",
        action="store_true",
        dest="force",
        default=False,
        help="overwrite output file if it exists",
    )
    (options, args) = parser.parse_args()
    return (options, args)
