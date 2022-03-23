# https://docs.python.org/3/library/unittest.html

import unittest
import samp


class Testsamp(unittest.TestCase):
	'''
		this class tests the imaginary samp.py file functions.
	'''

	def setUp(self):
		print('setUp')

	def tearDown(self):
		print('test_11')

	def test_11(self):
		print('test_11')
		result=1;
		self.assertEqual(result, 1)
		self.assertEqual(result, 2)
		self.assertEqual(result, 3)
		self.assertEqual(result, 4)

	def test_22(self):
		print('test_22')
		result=1;
		self.assertEqual(result, 1)
		self.assertEqual(result, 2)
		self.assertEqual(result, 3)
		self.assertEqual(result, 4)

		with self.assertRaises(ValueError):
			samp.divide(10, 0)

if __name__ == '__main__':
	unittest.main()