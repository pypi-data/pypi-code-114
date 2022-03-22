from __future__ import annotations

import argparse
from typing import Sequence

from tokenize_rt import reversed_enumerate
from tokenize_rt import src_to_tokens
from tokenize_rt import tokens_to_src


def octal8(src: str) -> str:
    """
    Replace base-10 integers with base-8 integers.
    """
    tokens = src_to_tokens(src)
    for i, token in reversed_enumerate(tokens):
        if token.name == "NUMBER":
            try:
                tokens[i] = token._replace(src=oct(int(token.src)))
            except ValueError:  # already not base-10
                pass

    return tokens_to_src(tokens)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="*")
    args = parser.parse_args(argv)

    ret = 0
    for filename in args.filename:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()

        new_contents = octal8(contents)

        with open(filename, "w") as f:
            f.write(new_contents)

        ret |= new_contents != contents

    return ret


if __name__ == "__main__":
    raise SystemExit(main())
