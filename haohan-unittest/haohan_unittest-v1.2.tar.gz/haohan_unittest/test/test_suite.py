import haohan_unittest

import gc
import sys
import weakref
from haohan_unittest.test.support import LoggingResult, TestEquality


### Support code for Test_TestSuite
################################################################

class Test(object):
    class Foo(haohan_unittest.TestCase):
        def test_1(self): pass
        def test_2(self): pass
        def test_3(self): pass
        def runTest(self): pass

def _mk_TestSuite(*names):
    return haohan_unittest.TestSuite(Test.Foo(n) for n in names)

################################################################


class Test_TestSuite(haohan_unittest.TestCase, TestEquality):

    ### Set up attributes needed by inherited tests
    ################################################################

    # Used by TestEquality.test_eq
    eq_pairs = [(haohan_unittest.TestSuite(), haohan_unittest.TestSuite())
               ,(haohan_unittest.TestSuite(), haohan_unittest.TestSuite([]))
               ,(_mk_TestSuite('test_1'), _mk_TestSuite('test_1'))]

    # Used by TestEquality.test_ne
    ne_pairs = [(haohan_unittest.TestSuite(), _mk_TestSuite('test_1'))
               ,(haohan_unittest.TestSuite([]), _mk_TestSuite('test_1'))
               ,(_mk_TestSuite('test_1', 'test_2'), _mk_TestSuite('test_1', 'test_3'))
               ,(_mk_TestSuite('test_1'), _mk_TestSuite('test_2'))]

    ################################################################
    ### /Set up attributes needed by inherited tests

    ### Tests for TestSuite.__init__
    ################################################################

    # "class TestSuite([tests])"
    #
    # The tests iterable should be optional
    def test_init__tests_optional(self):
        suite = haohan_unittest.TestSuite()

        self.assertEqual(suite.countTestCases(), 0)
        # countTestCases() still works after tests are run
        suite.run(haohan_unittest.TestResult())
        self.assertEqual(suite.countTestCases(), 0)

    # "class TestSuite([tests])"
    # ...
    # "If tests is given, it must be an iterable of individual test cases
    # or other test suites that will be used to build the suite initially"
    #
    # TestSuite should deal with empty tests iterables by allowing the
    # creation of an empty suite
    def test_init__empty_tests(self):
        suite = haohan_unittest.TestSuite([])

        self.assertEqual(suite.countTestCases(), 0)
        # countTestCases() still works after tests are run
        suite.run(haohan_unittest.TestResult())
        self.assertEqual(suite.countTestCases(), 0)

    # "class TestSuite([tests])"
    # ...
    # "If tests is given, it must be an iterable of individual test cases
    # or other test suites that will be used to build the suite initially"
    #
    # TestSuite should allow any iterable to provide tests
    def test_init__tests_from_any_iterable(self):
        def tests():
            yield haohan_unittest.FunctionTestCase(lambda: None)
            yield haohan_unittest.FunctionTestCase(lambda: None)

        suite_1 = haohan_unittest.TestSuite(tests())
        self.assertEqual(suite_1.countTestCases(), 2)

        suite_2 = haohan_unittest.TestSuite(suite_1)
        self.assertEqual(suite_2.countTestCases(), 2)

        suite_3 = haohan_unittest.TestSuite(set(suite_1))
        self.assertEqual(suite_3.countTestCases(), 2)

        # countTestCases() still works after tests are run
        suite_1.run(haohan_unittest.TestResult())
        self.assertEqual(suite_1.countTestCases(), 2)
        suite_2.run(haohan_unittest.TestResult())
        self.assertEqual(suite_2.countTestCases(), 2)
        suite_3.run(haohan_unittest.TestResult())
        self.assertEqual(suite_3.countTestCases(), 2)

    # "class TestSuite([tests])"
    # ...
    # "If tests is given, it must be an iterable of individual test cases
    # or other test suites that will be used to build the suite initially"
    #
    # Does TestSuite() also allow other TestSuite() instances to be present
    # in the tests iterable?
    def test_init__TestSuite_instances_in_tests(self):
        def tests():
            ftc = haohan_unittest.FunctionTestCase(lambda: None)
            yield haohan_unittest.TestSuite([ftc])
            yield haohan_unittest.FunctionTestCase(lambda: None)

        suite = haohan_unittest.TestSuite(tests())
        self.assertEqual(suite.countTestCases(), 2)
        # countTestCases() still works after tests are run
        suite.run(haohan_unittest.TestResult())
        self.assertEqual(suite.countTestCases(), 2)

    ################################################################
    ### /Tests for TestSuite.__init__

    # Container types should support the iter protocol
    def test_iter(self):
        test1 = haohan_unittest.FunctionTestCase(lambda: None)
        test2 = haohan_unittest.FunctionTestCase(lambda: None)
        suite = haohan_unittest.TestSuite((test1, test2))

        self.assertEqual(list(suite), [test1, test2])

    # "Return the number of tests represented by the this test object.
    # ...this method is also implemented by the TestSuite class, which can
    # return larger [greater than 1] values"
    #
    # Presumably an empty TestSuite returns 0?
    def test_countTestCases_zero_simple(self):
        suite = haohan_unittest.TestSuite()

        self.assertEqual(suite.countTestCases(), 0)

    # "Return the number of tests represented by the this test object.
    # ...this method is also implemented by the TestSuite class, which can
    # return larger [greater than 1] values"
    #
    # Presumably an empty TestSuite (even if it contains other empty
    # TestSuite instances) returns 0?
    def test_countTestCases_zero_nested(self):
        class Test1(haohan_unittest.TestCase):
            def test(self):
                pass

        suite = haohan_unittest.TestSuite([haohan_unittest.TestSuite()])

        self.assertEqual(suite.countTestCases(), 0)

    # "Return the number of tests represented by the this test object.
    # ...this method is also implemented by the TestSuite class, which can
    # return larger [greater than 1] values"
    def test_countTestCases_simple(self):
        test1 = haohan_unittest.FunctionTestCase(lambda: None)
        test2 = haohan_unittest.FunctionTestCase(lambda: None)
        suite = haohan_unittest.TestSuite((test1, test2))

        self.assertEqual(suite.countTestCases(), 2)
        # countTestCases() still works after tests are run
        suite.run(haohan_unittest.TestResult())
        self.assertEqual(suite.countTestCases(), 2)

    # "Return the number of tests represented by the this test object.
    # ...this method is also implemented by the TestSuite class, which can
    # return larger [greater than 1] values"
    #
    # Make sure this holds for nested TestSuite instances, too
    def test_countTestCases_nested(self):
        class Test1(haohan_unittest.TestCase):
            def test1(self): pass
            def test2(self): pass

        test2 = haohan_unittest.FunctionTestCase(lambda: None)
        test3 = haohan_unittest.FunctionTestCase(lambda: None)
        child = haohan_unittest.TestSuite((Test1('test2'), test2))
        parent = haohan_unittest.TestSuite((test3, child, Test1('test1')))

        self.assertEqual(parent.countTestCases(), 4)
        # countTestCases() still works after tests are run
        parent.run(haohan_unittest.TestResult())
        self.assertEqual(parent.countTestCases(), 4)
        self.assertEqual(child.countTestCases(), 2)

    # "Run the tests associated with this suite, collecting the result into
    # the test result object passed as result."
    #
    # And if there are no tests? What then?
    def test_run__empty_suite(self):
        events = []
        result = LoggingResult(events)

        suite = haohan_unittest.TestSuite()

        suite.run(result)

        self.assertEqual(events, [])

    # "Note that unlike TestCase.run(), TestSuite.run() requires the
    # "result object to be passed in."
    def test_run__requires_result(self):
        suite = haohan_unittest.TestSuite()

        try:
            suite.run()
        except TypeError:
            pass
        else:
            self.fail("Failed to raise TypeError")

    # "Run the tests associated with this suite, collecting the result into
    # the test result object passed as result."
    def test_run(self):
        events = []
        result = LoggingResult(events)

        class LoggingCase(haohan_unittest.TestCase):
            def run(self, result):
                events.append('run %s' % self._testMethodName)

            def test1(self): pass
            def test2(self): pass

        tests = [LoggingCase('test1'), LoggingCase('test2')]

        haohan_unittest.TestSuite(tests).run(result)

        self.assertEqual(events, ['run test1', 'run test2'])

    # "Add a TestCase ... to the suite"
    def test_addTest__TestCase(self):
        class Foo(haohan_unittest.TestCase):
            def test(self): pass

        test = Foo('test')
        suite = haohan_unittest.TestSuite()

        suite.addTest(test)

        self.assertEqual(suite.countTestCases(), 1)
        self.assertEqual(list(suite), [test])
        # countTestCases() still works after tests are run
        suite.run(haohan_unittest.TestResult())
        self.assertEqual(suite.countTestCases(), 1)

    # "Add a ... TestSuite to the suite"
    def test_addTest__TestSuite(self):
        class Foo(haohan_unittest.TestCase):
            def test(self): pass

        suite_2 = haohan_unittest.TestSuite([Foo('test')])

        suite = haohan_unittest.TestSuite()
        suite.addTest(suite_2)

        self.assertEqual(suite.countTestCases(), 1)
        self.assertEqual(list(suite), [suite_2])
        # countTestCases() still works after tests are run
        suite.run(haohan_unittest.TestResult())
        self.assertEqual(suite.countTestCases(), 1)

    # "Add all the tests from an iterable of TestCase and TestSuite
    # instances to this test suite."
    #
    # "This is equivalent to iterating over tests, calling addTest() for
    # each element"
    def test_addTests(self):
        class Foo(haohan_unittest.TestCase):
            def test_1(self): pass
            def test_2(self): pass

        test_1 = Foo('test_1')
        test_2 = Foo('test_2')
        inner_suite = haohan_unittest.TestSuite([test_2])

        def gen():
            yield test_1
            yield test_2
            yield inner_suite

        suite_1 = haohan_unittest.TestSuite()
        suite_1.addTests(gen())

        self.assertEqual(list(suite_1), list(gen()))

        # "This is equivalent to iterating over tests, calling addTest() for
        # each element"
        suite_2 = haohan_unittest.TestSuite()
        for t in gen():
            suite_2.addTest(t)

        self.assertEqual(suite_1, suite_2)

    # "Add all the tests from an iterable of TestCase and TestSuite
    # instances to this test suite."
    #
    # What happens if it doesn't get an iterable?
    def test_addTest__noniterable(self):
        suite = haohan_unittest.TestSuite()

        try:
            suite.addTests(5)
        except TypeError:
            pass
        else:
            self.fail("Failed to raise TypeError")

    def test_addTest__noncallable(self):
        suite = haohan_unittest.TestSuite()
        self.assertRaises(TypeError, suite.addTest, 5)

    def test_addTest__casesuiteclass(self):
        suite = haohan_unittest.TestSuite()
        self.assertRaises(TypeError, suite.addTest, Test_TestSuite)
        self.assertRaises(TypeError, suite.addTest, haohan_unittest.TestSuite)

    def test_addTests__string(self):
        suite = haohan_unittest.TestSuite()
        self.assertRaises(TypeError, suite.addTests, "foo")

    def test_function_in_suite(self):
        def f(_):
            pass
        suite = haohan_unittest.TestSuite()
        suite.addTest(f)

        # when the bug is fixed this line will not crash
        suite.run(haohan_unittest.TestResult())

    def test_remove_test_at_index(self):
        if not haohan_unittest.BaseTestSuite._cleanup:
            raise haohan_unittest.SkipTest("Suite cleanup is disabled")

        suite = haohan_unittest.TestSuite()

        suite._tests = [1, 2, 3]
        suite._removeTestAtIndex(1)

        self.assertEqual([1, None, 3], suite._tests)

    def test_remove_test_at_index_not_indexable(self):
        if not haohan_unittest.BaseTestSuite._cleanup:
            raise haohan_unittest.SkipTest("Suite cleanup is disabled")

        suite = haohan_unittest.TestSuite()
        suite._tests = None

        # if _removeAtIndex raises for noniterables this next line will break
        suite._removeTestAtIndex(2)

    def assert_garbage_collect_test_after_run(self, TestSuiteClass):
        if not haohan_unittest.BaseTestSuite._cleanup:
            raise haohan_unittest.SkipTest("Suite cleanup is disabled")

        class Foo(haohan_unittest.TestCase):
            def test_nothing(self):
                pass

        test = Foo('test_nothing')
        wref = weakref.ref(test)

        suite = TestSuiteClass([wref()])
        suite.run(haohan_unittest.TestResult())

        del test

        # for the benefit of non-reference counting implementations
        gc.collect()

        self.assertEqual(suite._tests, [None])
        self.assertIsNone(wref())

    def test_garbage_collect_test_after_run_BaseTestSuite(self):
        self.assert_garbage_collect_test_after_run(haohan_unittest.BaseTestSuite)

    def test_garbage_collect_test_after_run_TestSuite(self):
        self.assert_garbage_collect_test_after_run(haohan_unittest.TestSuite)

    def test_basetestsuite(self):
        class Test(haohan_unittest.TestCase):
            wasSetUp = False
            wasTornDown = False
            @classmethod
            def setUpClass(cls):
                cls.wasSetUp = True
            @classmethod
            def tearDownClass(cls):
                cls.wasTornDown = True
            def testPass(self):
                pass
            def testFail(self):
                fail
        class Module(object):
            wasSetUp = False
            wasTornDown = False
            @staticmethod
            def setUpModule():
                Module.wasSetUp = True
            @staticmethod
            def tearDownModule():
                Module.wasTornDown = True

        Test.__module__ = 'Module'
        sys.modules['Module'] = Module
        self.addCleanup(sys.modules.pop, 'Module')

        suite = haohan_unittest.BaseTestSuite()
        suite.addTests([Test('testPass'), Test('testFail')])
        self.assertEqual(suite.countTestCases(), 2)

        result = haohan_unittest.TestResult()
        suite.run(result)
        self.assertFalse(Module.wasSetUp)
        self.assertFalse(Module.wasTornDown)
        self.assertFalse(Test.wasSetUp)
        self.assertFalse(Test.wasTornDown)
        self.assertEqual(len(result.errors), 1)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 2)
        self.assertEqual(suite.countTestCases(), 2)


    def test_overriding_call(self):
        class MySuite(haohan_unittest.TestSuite):
            called = False
            def __call__(self, *args, **kw):
                self.called = True
                haohan_unittest.TestSuite.__call__(self, *args, **kw)

        suite = MySuite()
        result = haohan_unittest.TestResult()
        wrapper = haohan_unittest.TestSuite()
        wrapper.addTest(suite)
        wrapper(result)
        self.assertTrue(suite.called)

        # reusing results should be permitted even if abominable
        self.assertFalse(result._testRunEntered)


if __name__ == '__main__':
    haohan_unittest.main()
