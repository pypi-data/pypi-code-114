import os
import sys
import haohan_unittest


here = os.path.dirname(__file__)
loader = haohan_unittest.defaultTestLoader

def load_tests(*args):
    suite = haohan_unittest.TestSuite()
    for fn in os.listdir(here):
        if fn.startswith("test") and fn.endswith(".py"):
            modname = "haohan_unittest.test.testmock." + fn[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTest(loader.loadTestsFromModule(module))
    return suite
