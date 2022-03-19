from typing import *

from enum import Enum

import unittest

from init_attrs_with_kwargs import InitAttrsWKwArgs


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class InitAttrsWKwArgsTest(unittest.TestCase):
    def test_simple(self):
        class BFISE(InitAttrsWKwArgs):
            b: bool
            f: float
            i: int
            s: str
            e: Color

        v0: BFISE = BFISE()

        v1: BFISE = BFISE(b=True)
        self.assertEqual(v1.b, True)

        v2: BFISE = BFISE(b=False)
        self.assertEqual(v2.b, False)

        v3: BFISE = BFISE(b=True, f=2.0, i=3, s='four', e=Color.RED)
        self.assertEqual(v3.b, True)
        self.assertEqual(v3.f, 2.0)
        self.assertEqual(v3.i, 3)
        self.assertEqual(v3.s, 'four')
        self.assertEqual(v3.e, Color.RED)

    def test_cast_str_values(self):
        class BFISE(InitAttrsWKwArgs):
            b: bool
            f: float
            i: int
            s: str
            e: Color

        v: BFISE = BFISE(_cast_str_values=False)
        v: BFISE = BFISE(_cast_str_values=True)

        v: BFISE = BFISE(_cast_str_values=True, b='', f='2.0', i='3', s='four', e='RED')
        self.assertEqual(v.b, False)
        self.assertEqual(v.f, 2.0)
        self.assertEqual(v.i, 3)
        self.assertEqual(v.s, 'four')
        self.assertEqual(v.e, Color.RED)

    def test_cast_str_values_without_need_for_casting(self):
        class BFISE(InitAttrsWKwArgs):
            b: bool
            f: float
            i: int
            s: str
            e: Color

        v: BFISE = BFISE(_cast_str_values=True, b=True, f=2.0, i=3, s='four', e=Color.RED)
        self.assertEqual(v.b, True)
        self.assertEqual(v.f, 2.0)
        self.assertEqual(v.i, 3)
        self.assertEqual(v.s, 'four')
        self.assertEqual(v.e, Color.RED)

    def test_cast_str_values_wrong_type(self):
        class BFISE(InitAttrsWKwArgs):
            b: bool
            f: float
            i: int
            s: str
            e: Color

        self.assertRaises(ValueError, lambda: BFISE(_cast_str_values=True, f=''))
        self.assertRaises(ValueError, lambda: BFISE(_cast_str_values=True, f='x'))
        self.assertRaises(ValueError, lambda: BFISE(_cast_str_values=True, i=''))
        self.assertRaises(ValueError, lambda: BFISE(_cast_str_values=True, i='x'))
        self.assertRaises(ValueError, lambda: BFISE(_cast_str_values=True, e=''))
        self.assertRaises(ValueError, lambda: BFISE(_cast_str_values=True, e='WHITE'))

    def test_cast_str_values_wrong_syntax(self):
        class FI(InitAttrsWKwArgs):
            f: float
            i: int

        self.assertRaises(NameError, lambda: FI(**{'---f': 1.0}))
        self.assertRaises(NameError, lambda: FI(**{'-0': 1.0}))

    def test_cast_str_values_wrong_attr_names(self):
        class BFISE(InitAttrsWKwArgs):
            b: bool
            f: float
            i: int
            s: str
            e: Color

        self.assertRaises(KeyError, lambda: BFISE(x=''))

    def test_cast_str_values_optional(self):
        class BFISE_O(InitAttrsWKwArgs):
            b: Optional[bool]
            f: Optional[float]
            i: Optional[int]
            s: Optional[str]
            e: Optional[Color]

        v: BFISE_O = BFISE_O(_cast_str_values=True, b='', f='2.0', i='3', s='four', e='RED')
        self.assertEqual(v.b, False)
        self.assertEqual(v.f, 2.0)
        self.assertEqual(v.i, 3)
        self.assertEqual(v.s, 'four')
        self.assertEqual(v.e, Color.RED)

    def test_cast_str_values_optional_twisted(self):
        class FI_O(InitAttrsWKwArgs):
            f: Optional[float]
            i: Optional[int]

        v: FI_O = FI_O(_cast_str_values=True, f='2.0', i='3')
        self.assertEqual(v.f, 2.0)
        self.assertEqual(v.i, 3)

    def test_cast_str_values_list(self):
        class FI_L(InitAttrsWKwArgs):
            fl: List[float]
            il: List[int]

        v: FI_O = FI_L(_cast_str_values=True, fl=['1.0', '2.0'], il=['3', '4'])
        self.assertEqual(v.fl, [1.0, 2.0])
        self.assertEqual(v.il, [3, 4])


if __name__ == "__main__":
    unittest.main()
