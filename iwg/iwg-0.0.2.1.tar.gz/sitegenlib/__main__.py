"""
In-house Website Generator
"""

import argparse

from . import simple
from . import VERSION


def main(args: argparse.Namespace) -> int:
    
    simple.generate(args.sources[0], args.out, template=args.template)
    return 0


if __name__ == "__main__":
    import sys

    parser = argparse.ArgumentParser(
        prog="sitegen",
        formatter_class=argparse.RawTextHelpFormatter,
        description=" ".join(it.strip() for it in """
            Generates a static website using source
            documents and an HTML template""".splitlines()),
        epilog=("""
        hey you, standing in the aisles
        with itchy feet and fading smiles
        
        can you hear me? """))
    
    parser.add_argument("sources",
        metavar="source-dir", type=str, nargs=1,
        help="root directory of content documents")
    parser.add_argument("-o", "--output",
        metavar="output-dir",
        dest="out", type=str, default="public",
        help="output directory")
    parser.add_argument("-t", "--template",
        metavar="template-dir",
        type=str, default="basic",
        help="template directory")
        
    parser.add_argument("--version",
        action="version",
        version=f"%(prog)s {VERSION}")

    sys.exit(main(parser.parse_args()))
