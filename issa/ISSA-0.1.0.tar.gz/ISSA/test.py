#Import the Testcase Module
import unittest
from Functions import InputVariables
from DataProcesser import Processor

'''
Test some of the key functions from ISSA to ensure it was installed correct.
'''
class TestFunctions(unittest.TestCase):
    def test_datareturn(self):
        test = InputVariables.datareturn(1,[1],[.1],['Uniform'], 10).mean()
        self.assertNotEqual(abs(1-test), 0,"should not be 0")

if __name__ == '__main__':
    unittest.main()