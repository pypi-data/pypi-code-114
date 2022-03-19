import argparse
from pathlib import Path
from typing import Any


def parse_args(args: list[str] | None = None) -> tuple[list[Path], dict[str, Any]]:
    parser = argparse.ArgumentParser()
    parser.add_argument('--allow-empty', action='store_true')
    parser.add_argument('paths', type=Path, nargs='+', help='paths to check')
    parsed = parser.parse_args(args)

    kwargs = vars(parsed)
    paths = kwargs.pop('paths')
    return paths, kwargs


def check(*paths: Path, allow_empty: bool = False) -> int:
    """
    return codes:
    0 - success, no __init__.py found
    1 - found __init__.py files
    """

    n_inits = 0
    for directory in paths:
        for file in directory.rglob('__init__.py'):
            if allow_empty:
                with open(file) as f:
                    if f.read(1) == '':
                        continue
            print(file)
            n_inits += 1

    if n_inits > 0:
        print(f'error: found {n_inits} {"non_empty" if allow_empty else ""}__init__.py files')
        return 1
    return 0


def main() -> int:
    paths, kwargs = parse_args()
    return check(*paths, **kwargs)


if __name__ == '__main__':
    raise SystemExit(main())
