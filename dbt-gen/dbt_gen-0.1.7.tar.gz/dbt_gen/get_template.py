try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import templates


def print_default_template(args):
    print(pkg_resources.read_text(templates, "base_model.sql"))


def config_parser(parser):
    parser.set_defaults(func=print_default_template)
