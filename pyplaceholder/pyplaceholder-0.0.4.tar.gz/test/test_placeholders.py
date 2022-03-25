import unittest

from mysutils.file import first_line
from mysutils.tmp import removable_tmp

from placeholder import parse_placeholders, replace_placeholders, has_placeholders, num_placeholders, \
    get_placeholders, get_placeholder, replace_file_placeholders, get_file_placeholders, get_file_placeholder


class PlaceholdersTestCase(unittest.TestCase):
    def test_parse(self) -> None:
        s = 'Some example of {term} \\{UN\\}'
        r = parse_placeholders(s)
        self.assertTupleEqual(r, ('Some example of {term} {UN}', [(16, 22)]))
        text, (init, end) = r[0], r[1][0]
        self.assertEqual(text[init:end], '{term}')
        s = 'Some example of <term> {UN}'
        r = parse_placeholders(s, '<', '>')
        self.assertTupleEqual(r, ('Some example of <term> {UN}', [(16, 22)]))
        text, (init, end) = r[0], r[1][0]
        self.assertEqual(text[init:end], '<term>')
        s = 'Some example of {term} {UN}'
        r = parse_placeholders(s)
        self.assertTupleEqual(r, ('Some example of {term} {UN}', [(16, 22), (23, 27)]))
        text, (init1, end1), (init2, end2) = r[0], r[1][0], r[1][1]
        self.assertListEqual([text[init1:end1], text[init2:end2]], ['{term}', '{UN}'])
        s = 'Some example of {term} \\{UN\\}'
        r = parse_placeholders(s, escapes=False)
        self.assertTupleEqual(r, ('Some example of {term} \\{UN\\}', [(16, 22)]))

    def test_replace(self) -> None:
        s = 'Some example of {term} \\{UN\\}'
        r = replace_placeholders(s, term='United Nations')
        self.assertEqual(r, 'Some example of United Nations {UN}')
        with self.assertRaises(KeyError):
            replace_placeholders(s, other='Hola')
        s = 'Some example of {term} {UN}'
        with self.assertRaises(KeyError):
            r = replace_placeholders(s, term='United Nations')
        r = replace_placeholders(s, term='United Nations', UN='(UN)')
        self.assertEqual(r, 'Some example of United Nations (UN)')

    def test_has_placeholders(self) -> None:
        s = 'Some example of {term} \\{UN\\}'
        self.assertTrue(has_placeholders(s))
        s = 'Some example of {term} {UN}'
        self.assertTrue(has_placeholders(s))
        s = 'Some example of \\{term\\} \\{UN\\}'
        self.assertFalse(has_placeholders(s))
        s = 'Some example of term UN'
        self.assertFalse(has_placeholders(s))

    def test_num_placeholders(self) -> None:
        s = 'Some example of {term} \\{UN\\}'
        self.assertEqual(num_placeholders(s), 1)
        s = 'Some example of {term} {UN}'
        self.assertEqual(num_placeholders(s), 2)
        s = 'Some example of \\{term\\} \\{UN\\}'
        self.assertEqual(num_placeholders(s), 0)
        s = 'Some example of term UN'
        self.assertEqual(num_placeholders(s), 0)

    def test_get_placeholders(self) -> None:
        s = 'Some example of {term} \\{UN\\}'
        self.assertListEqual(get_placeholders(s), ['term'])
        self.assertEqual(get_placeholder(s), 'term')
        s = 'Some example of {term} {UN}'
        self.assertListEqual(get_placeholders(s), ['term', 'UN'])
        self.assertEqual(get_placeholder(s), 'term')
        self.assertEqual(get_placeholder(s, pos=1), 'UN')
        s = 'Some example of {1} and {2}'
        self.assertListEqual(get_placeholders(s), ['1', '2'])
        self.assertListEqual(get_placeholders(s, type=int), [1, 2])
        self.assertEqual(get_placeholder(s), '1')
        self.assertEqual(get_placeholder(s, type=int), 1)
        self.assertEqual(get_placeholder(s, type=int, pos=1), 2)
        s = 'Some example of {1} and {term}'
        self.assertListEqual(get_placeholders(s, type=[int, str]), [1, 'term'])
        with self.assertRaises(ValueError):
            s = 'Some example of {1}'
            get_placeholders(s, type=[int, str])
        with self.assertRaises(ValueError):
            s = 'Some example of {1}, {2} and {3}'
            get_placeholders(s, type=[int, str])

    def test_file_placeholders(self) -> None:
        with removable_tmp() as file:
            replace_file_placeholders('test.txt', file, num=2, action='test')
            s = first_line(file)
            self.assertEqual(s, 'This is a test with 2 placeholders to test the functions to parse {placeholders}.')
            replace_file_placeholders('test.txt', file, escapes=False, num=2, action='test')
            s = first_line(file)
            self.assertEqual(s, 'This is a test with 2 placeholders to test the functions to parse \\{placeholders\\}.')
        self.assertListEqual(get_file_placeholders('test.txt'), ['num', 'action'])
        self.assertEqual(get_file_placeholder('test.txt'), 'num')
        self.assertEqual(get_file_placeholder('test.txt', pos=-1), 'action')


if __name__ == '__main__':
    unittest.main()
