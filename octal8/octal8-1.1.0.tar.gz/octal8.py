from __future__ import annotations

import argparse
import ast
from typing import TYPE_CHECKING
from typing import Sequence

from tokenize_rt import Offset
from tokenize_rt import reversed_enumerate
from tokenize_rt import src_to_tokens
from tokenize_rt import tokens_to_src

if TYPE_CHECKING:
    from pathlib import Path


def _rewrite_file(filename: str) -> int:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()

    found: set[Offset] = set()
    tree = ast.parse(contents, filename=filename)
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Constant)  # py3.8+
            and isinstance(node.value, int)
            and not isinstance(node.value, bool)
            or isinstance(node, ast.Num)  # py3.7
            and isinstance(node.n, int)
            and not isinstance(node.n, bool)
        ):
            found.add(Offset(node.lineno, node.col_offset))

    tokens = src_to_tokens(contents)
    for i, token in reversed_enumerate(tokens):
        if token.offset in found:
            if not token.src.startswith("0"):  # base-10 int
                tokens[i] = token._replace(src=oct(int(token.src)))

    new_contents = tokens_to_src(tokens)
    with open(filename, "w") as f:
        f.write(new_contents)

    return new_contents != contents


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="*")
    args = parser.parse_args(argv)

    ret = 0
    for filename in args.filename:
        ret |= _rewrite_file(filename)

    return ret


if __name__ == "__main__":
    raise SystemExit(main())


def test_main(tmp_path: Path) -> None:
    target = tmp_path / "target.py"
    target.write_text(
        """\
from typing import Literal

CONSTANT = 1234
my_bool = True


def foo(default=12) -> Literal[6]:
    return 6


x = 9_000
y = 12.34
z = 60 * 60 * 1
print(f"{x + 7}")

EIGHT = 0o10
"""
    )

    main((str(target),))

    assert (
        target.read_text()
        == """\
from typing import Literal

CONSTANT = 0o2322
my_bool = True


def foo(default=0o14) -> Literal[0o6]:
    return 0o6


x = 0o21450
y = 12.34
z = 0o74 * 0o74 * 0o1
print(f"{x + 7}")

EIGHT = 0o10
"""
    )
