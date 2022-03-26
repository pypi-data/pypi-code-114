"""
In-house Website Generator
"""

import argparse
import logging
import traceback

from . import VERSION
from . import simple
from .template import engine
from .template import build


def main(args: argparse.Namespace) -> int:
    if args.silent:
        log_level = logging.ERROR
    elif args.verbose:
        log_level = logging.INFO
    else:
        log_level = logging.WARNING
    logging.basicConfig(format="%(levelname)s: %(message)s", level=log_level)
    
    try:
        if args.command == "build":
            cmd_build(args)
        elif args.command == "template":
            cmd_template(args)
    except Exception:
        print("INTERNAL ERROR")
        traceback.print_exc()
        return 1
    return 0


def cmd_build(args):
    simple.generate_site(
        args.sources[0], args.output,
        template=args.template)


def cmd_template(args):
    if args.preview:
        build.build_preview(args.template, args.output)
    else:
        engine.render(
            args.template, args.output,
            docs=args.docs[0])


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
    parser.add_argument("--version",
        action="version",
        version=f"%(prog)s {VERSION}")
    
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="verbose output")
    parser.add_argument(
        "--silent", action="store_true",
        help="print errors only")
    
    subparsers = parser.add_subparsers(
        dest = "command",
        title= "Template tools",
        description="""
        hiçbir zaman
        insanın kafasında böyle
        yekpare kristal top gibi parlayan tek bir düşünce olmuyor """)

    parser_build = subparsers.add_parser("build")
    parser_build.add_argument(
        "sources", metavar="source-dir", type=str, nargs=1,
        help="root directory of content documents")
    parser_build.add_argument(
        "-o", "--output", metavar="output-dir", type=str, default="public",
        help="output directory")
    parser_build.add_argument(
        "-t", "--template",
        metavar="template-dir", type=str, default="basic",
        help="template directory")

    parser_template = subparsers.add_parser("template")
    parser_template.add_argument(
        "docs", metavar="content-dir", type=str, nargs="?",
        help="directory that contains content documents")
    parser_template.add_argument(
        "-t", "--template", metavar="template-root", type=str, required=True,
        help="template directory")
    parser_template.add_argument(
        "-o", "--output", metavar="build-dir", type=str, required=True,
        help="output destination.\This must not be the same with the template-dir.")
    parser_template.add_argument(
        "-p", "--preview", action="store_true",
        help="build template with sample data")
    
    args = parser.parse_args()
    if (args.command == "template"
        and not (args.preview or args.docs)
    ):
        parser.error("content-dir is required if not building with --preview")
    sys.exit(main(args))
