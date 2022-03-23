import os
# os.chdir("../")
# print(f"Current directory = {os.getcwd()}")
from trell_ai_util.APIHelper import remove_emoji
import unittest


class Test_APIHelper(unittest.TestCase):
    
        
    def test_remove_emoji(self):
        print("testing remove emoji function")
        self.assertEqual(remove_emoji("😡 Happy")," Happy")

