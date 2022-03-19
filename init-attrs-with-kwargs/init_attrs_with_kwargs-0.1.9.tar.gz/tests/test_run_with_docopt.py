from typing import *

import unittest

import docopt

from init_attrs_with_kwargs import InitAttrsWKwArgs


class RunWithDocopt(unittest.TestCase):
    def test_simple(self):
        doc = '''Get total of numbers.

        Usage:
        sample2 [--maximum|--minimum|--average] <number>...

        Options:
        --maximum, -M     Get the largest number.
        --minimum, -m     Get the smallest number.
        --average, -a     Get the average of the numbers.
        '''

        class MyArgs(InitAttrsWKwArgs):
            maximum: bool
            minimum: bool
            average: bool
            number: List[float]

        args = MyArgs(_cast_str_values=True, **docopt.docopt(doc, ["-m", "10.0"]))
        self.assertTrue(args.minimum)
        self.assertFalse(args.maximum)
        self.assertFalse(args.average)
        self.assertSequenceEqual(args.number, [10.0])

        args = MyArgs(_cast_str_values=True, **docopt.docopt(doc, ["-m", "10.0", "20.0"]))
        self.assertTrue(args.minimum)
        self.assertFalse(args.maximum)
        self.assertFalse(args.average)
        self.assertSequenceEqual(args.number, [10.0, 20.0])

        args = MyArgs(_cast_str_values=True, **docopt.docopt(doc, ["-M", "10.0", "20.0", "30.0"]))
        self.assertFalse(args.minimum)
        self.assertTrue(args.maximum)
        self.assertFalse(args.average)
        self.assertSequenceEqual(args.number, [10.0, 20.0, 30.0])



if __name__ == "__main__":
    unittest.main()
