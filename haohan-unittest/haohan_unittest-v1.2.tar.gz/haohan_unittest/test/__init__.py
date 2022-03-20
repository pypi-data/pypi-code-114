import os
import sys
import haohan_unittest


here = os.path.dirname(__file__)
loader = haohan_unittest.defaultTestLoader

def suite():
    suite = haohan_unittest.TestSuite()
    for fn in os.listdir(here):
        if fn.startswith("test") and fn.endswith(".py"):
            modname = "haohan_unittest.test." + fn[:-3]
            __import__(modname)
            module = sys.modules[modname]
            suite.addTest(loader.loadTestsFromModule(module))
    suite.addTest(loader.loadTestsFromName('haohan_unittest.test.testmock'))
    return suite


if __name__ == "__main__":
    haohan_unittest.main(defaultTest="suite")
