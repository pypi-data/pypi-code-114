'''
Created on Sep 29, 2021

@author: Sgoldberg
'''
import io
from pickle import TRUE
import unittest

from iserver import ezx_msg
from iserver.msgs import LogonRequest
from iserver.msgs import LogonResponse
from tests.data import MsgWithBlockFields, GrandChild


class Parent(object):
    def __init__(self):
        self.parent_name = None
        

class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
        self.child_name = None
        
        




class Test(unittest.TestCase):
    
    def testParentChild(self):
        c = Child()
        self.assertTrue(hasattr(c, 'child_name'), 'child name')
        self.assertTrue(hasattr(c, 'parent_name'), 'parent name')
        
        
        

    def testListAttributes(self):
        l = LogonRequest()
        print(f'vars={vars(l)}')
        for name, value in vars(l).items():
            print(f"{name}={value}")

    def testEncodeNameValue(self):
        buffer = io.StringIO()
        ezx_msg.encode_name_value("myName", 2, buffer)
        
        ezx_msg.encode_name_value(2, None, 'hi')
        
    def testDoubleToString(self):
        value = 123.45
        print(str(value))
        
        value = value + .01
        print(str(value))
   
    def test_to_str(self):     
        value = 123.45
        print(ezx_msg.to_string(value))
        
        value = value + .01
        print(ezx_msg.to_string(value))   
        
        value = 543210
        print(ezx_msg.to_string(value))
    
    def test_get_string_char(self):
        s = "Hello World"
        self.assertEqual('d', s[-1], "got last char")
        

    def test_filter(self):
        l = [1, 2, 3, 4, 5];
        f = lambda x : x % 2 == 0
        result = list(filter(f, l))
        print(f'result={result}')
        self.assertEqual(2, len(result))
        
    def test_attr_functions(self):
        msg = LogonResponse()
        name = 'returnCode'
        self.assertTrue(hasattr(msg, name))
        
        name = 'destinations'
        self.assertTrue(hasattr(msg, name))
        
        name = 'returnCode'
        value = getattr(msg, name)
        self.assertIsNone(value, f"get attr {name}")
        
        name = 'destinations'
        value = getattr(msg, name)
        self.assertIsNone(value, f"get attr {name}")
        
        
    # API types
    # list
    # double
    # GroupAccount
    # int
    # LocalTimeStamp
    # LogonType
    # String
    # UTCTimeStamp        
    def test_convert_api_field_value(self):
        s = "aString"
        t = str(s)
        self.assertEqual(s, t)
        
    
    def test_meta_class1(self):
        msg = MsgWithBlockFields()
        self.assertTrue(hasattr(msg, '__block_fields__'))
        self.assertTrue(hasattr(msg, '__block_fields_by_name__'))
        
    def test_meta_class_with_multiple_inheritance(self):
        msg = GrandChild()
        self.assertTrue(hasattr(msg, '__block_fields__'))
        self.assertTrue(hasattr(msg, '__block_fields_by_name__'))
        
    
    def test_lambda_with_closure(self):
        class Simple:
            def __init__(self):
                self.is_enabled = False  

        closure_obj = Simple()
        predicate = lambda : closure_obj.is_enabled
        
        self.assertFalse(predicate(), 'before change to object')
        closure_obj.is_enabled = True
        self.assertTrue(predicate(), 'lambda evaluated state of closure object')
        
        
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testListAttributes']
    unittest.main()
