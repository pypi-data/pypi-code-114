from .voice import cli
from . import __name__ as package_name
import sys

if __name__ == '__main__':  # pragma: no cover
    cli(sys.argv[1:], 'python -m '+package_name)
