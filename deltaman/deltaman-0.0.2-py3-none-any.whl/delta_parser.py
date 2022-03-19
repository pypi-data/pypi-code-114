"""
Thanks to https://stackoverflow.com/questions/9775743/how-can-i-parse-free-text-time-intervals-in-python-ranging-from-years-to-second
"""  # noqa
from typing import List, Union
from datetime import timedelta
from functools import reduce
from operator import add, mul
import os.path

from lark import Lark, Transformer, Token

units = {
    "second": timedelta(seconds=1),
    "minute": timedelta(minutes=1),
    "hour": timedelta(hours=1),
    "day": timedelta(days=1),
    "week": timedelta(weeks=1),
    "month": timedelta(days=30),
    "year": timedelta(days=365),
}


class TreeToTimeDelta(Transformer):
    def delta(self, tree: List[timedelta]) -> timedelta:
        return reduce(add, tree, timedelta(seconds=0))

    def time(self, tree: List[Union[float, timedelta]]) -> timedelta:
        return mul(*tree)

    def unit(self, tokens: List[Token]) -> timedelta:
        return units[tokens[0].type.lower()]

    def number(self, tokens: List[Token]) -> float:
        return float(tokens[0].value)


with open(os.path.join(os.path.dirname(__file__), 'delta.lark')) as f:
    delta_grammar = f.read()

delta_parser = Lark(
    delta_grammar, parser='lalr', transformer=TreeToTimeDelta()
)

if __name__ == '__main__':
    for delta in (
        '3min',
        '10 seconds',
        '1d',
        '1d1h',
        '1m15s',
        '1m 15s',
        '2m-15s',
        '2m -1s',
    ):
        parsed_delta = delta_parser.parse(delta)
        print(f'* Input: {delta:20s} Parsed: {str(parsed_delta):20s} '
              f'(total seconds: {parsed_delta.total_seconds()})')
