"""
In-house Site Generator
"""

from typing import List

from . import simple


def main(*args: List[str]) -> int:
    if len(args) >= 3:
        simple.generate(args[1], args[2])
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main(*sys.argv))
