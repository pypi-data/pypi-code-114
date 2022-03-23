try:
    import unittest2 as unittest
except ImportError:
    import unittest as unittest

from battlenet_client.util import *


class UtilityTests(unittest.TestCase):

    def test_localize(self):
        locale = localize('EnuS')
        self.assertIsInstance(locale, str)
        self.assertEqual(locale[:2], 'en')
        self.assertEqual(locale[-2:], 'US')
        self.assertEqual(locale, 'en_US')

    def test_localize_wrong_type(self):
        self.assertRaises(TypeError, lambda: localize(1))
        self.assertRaises(TypeError, lambda: localize(['EnuS', 'EngB']))
        self.assertRaises(TypeError, lambda: localize(('EnuS', 'EngB')))
        self.assertRaises(TypeError, lambda: localize({'lang': 'en', 'country': 'US'}))

    def test_localize_wrong_lang_country(self):
        self.assertRaises(ValueError, lambda: localize('zzus'))
        self.assertRaises(ValueError, lambda: localize('enZZ'))

    def test_slugify(self):
        name = slugify('Zul\'jin')
        self.assertEqual(name, 'zuljin')

    def test_slugify_case(self):
        name = slugify('Zul\'jin')
        self.assertTrue(name.islower())

    def test_slugify_type_error(self):
        self.assertRaises(TypeError, lambda: slugify(1))
        self.assertRaises(TypeError, lambda: slugify(['EnuS', 'EngB']))
        self.assertRaises(TypeError, lambda: slugify(('EnuS', 'EngB')))
        self.assertRaises(TypeError, lambda: slugify({'lang': 'en', 'country': 'US'}))

    def test_slugify_no_apostrophe(self):
        name = slugify('Zul\'jin')
        self.assertEqual(name.find('\''), -1)

    def test_slugify_no_space(self):
        name = slugify('Moon Guard')
        self.assertEqual(name.find(' '), -1)
