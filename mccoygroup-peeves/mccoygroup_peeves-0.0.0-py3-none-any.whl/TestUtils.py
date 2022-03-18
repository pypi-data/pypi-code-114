"""
All of the utilities that are used in writing tests for Peeves
"""

from .Timer import Timer
import unittest, os, sys

__all__ = [
    "TestRunner",
    "DebugTests",
    "ValidationTests",
    "TimingTests",
    "LoadTests",
    "TestManager",
    "DataGenerator",
    "load_tests",
    "validationTest",
    "debugTest",
    "dataGenTest",
    "timeitTest",
    "timingTest",
    "inactiveTest"
]

class TestManagerClass:
    """Just manages where things load from
    """
    log_file = "test_results.txt"
    log_results = False
    quiet_mode = False
    debug_tests = True
    validation_tests = False
    timing_tests = False
    data_gen_tests = False
    test_files = "All"
    test_name = ""
    def __init__(self,
                 test_root = None, test_dir = None, test_data = None,
                 base_dir = None, start_dir = None,
                 test_pkg = None, test_data_ext = "TestData"
                 ):
        """

        :param test_root: the root package
        :type test_root:
        :param test_dir: the directory to load tests from (usually test_root/test_pkg)
        :type test_dir:
        :param test_data: the directory to load test data from (usually test_dir/test_data_ext)
        :type test_data:
        :param base_dir: the overall base directory to do imports from
        :type base_dir:
        :param start_dir: the directory to start test discovery from
        :type start_dir:
        :param test_pkg: the name of the python package that holds all the tests
        :type test_pkg:
        :param test_data_ext: the extension from test_dir to look for data in (usually TestData)
        :type test_data_ext:
        """
        self._base_dir = base_dir
        self._start_dir = start_dir
        self._test_root = test_root
        self._base_dir_use_default = base_dir is None
        self._test_dir = test_dir
        self._test_dir_use_default = test_dir is None
        self._test_data = test_data
        self._test_data_use_default = test_data is None
        self._test_pkg = test_pkg
        self._test_pkg_validated = False
        self.data_ext = test_data_ext
    @property
    def test_root(self):
        if self._test_root is None:
            try:
                test_root = [ a for a in sys.argv if os.path.isdir(a) ][0] # you can pass the directory to run the tests as the first sys.argv arg
            except IndexError:
                test_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # or we'll assume it's two dirs up from here
            sys.path.insert(0, test_root) # not sure exactly what this does... might want to be more targeted with it
            self._test_root = test_root
        return self._test_root
    @test_root.setter
    def test_root(self, root):
        self._test_root = root
        if self._base_dir_use_default:
            self._base_dir = None
        if self._test_dir_use_default:
            self._test_dir = None
        if self._test_data_use_default:
            self._test_data = None
    @property
    def base_dir(self):
        if self._base_dir is None:
            self._base_dir = self.test_root
        return self._base_dir
    @base_dir.setter
    def base_dir(self, d):
        self._base_dir = d
        if d is not None:
            self._base_dir_use_default = False
    @property
    def start_dir(self):
        if self._start_dir is None:
            return self.test_dir
        return self._start_dir
    @start_dir.setter
    def start_dir(self, d):
        self._start_dir = d
        if d is not None:
            self._start_dir_use_default = False
    @property
    def test_pkg(self):
        if not self._test_pkg_validated:
            root = self.test_root
            # TODO: find some way to check it to figure out how many . we need to go up...
            # for now we'll just leave it, though
            if self._test_pkg is None:
                self._test_pkg = "Tests"
            if "." not in self._test_pkg:
                self._test_pkg = "."*(len(__package__.split(".")) - 1) + self._test_pkg
                # a basic guess as to what'll get us to the right spot...
            self._test_pkg_validated = True
        return self._test_pkg
    @test_pkg.setter
    def test_pkg(self, pkg):
        self._test_pkg = pkg
        self._test_pkg_validated = False
    @property
    def test_dir(self):
        # the Tests package _must_ be in the parent repository
        if self._test_dir is None:
            self._test_dir = os.path.join(self.test_root, self.test_pkg.split(".")[-1])
            if not os.path.isdir(self._test_dir) and self.test_pkg[0] == ".":
                raise IOError(
                    "Peeves expects a '{}' package at {} to hold all the tests because I wrote it bad".format(
                        self.test_pkg,
                        self.test_root
                        )
                    )
        return self._test_dir
    @test_dir.setter
    def test_dir(self, d):
        self._test_dir = d
        if d is not None:
            self._test_dir_use_default = False
    @property
    def test_data_dir(self):
        if self._test_data is None:
            self._test_data = os.path.join(self.test_dir, self.data_ext)
        return self._test_data
    @test_data_dir.setter
    def test_data_dir(self, d):
        self._test_data = d
        if d is not None:
            self._test_data_use_default = False
    def test_data(self, filename):
        return os.path.join(self.test_data_dir, filename)
    def run(self, exit=True, exit_code=None):
        from .run_tests import test_status
        if exit:
            sys.exit(test_status if exit_code is None else exit_code) #should kill everything...?
        return test_status
TestManager = TestManagerClass()
TestManager.__name__ = "TestManager"
TestManager.__doc__ = """
    The main interface for managing what tests we might want to run.
    Instance of `TestManagerClass`
    """


TestCase = unittest.TestCase #just in case I want to change this up later
class DataGenerator:
    """Provides methods to generate relevant data for testing methods
    """

    seed = 15
    @classmethod
    def coords(cls, n=50):
        import numpy as np
        np.random.seed(cls.seed)
        return np.random.rand(n, 3)
    @classmethod
    def multicoords(cls, n=10, m=50):
        import numpy as np
        np.random.seed(cls.seed)
        return np.random.rand(n, m, 3)
    @classmethod
    def mats(cls, n=1):
        import numpy as np
        np.random.seed(cls.seed)
        return np.random.rand(n, 3, 3)
    @classmethod
    def vecs(cls, n=1):
        import numpy as np
        np.random.seed(cls.seed)
        return np.random.rand(n, 3)

    @classmethod
    def angles(cls, n=50, r=(0, 360), use_rad=False):
        import numpy as np
        np.random.seed(cls.seed)
        angles = np.random.uniform(*r, size=(n,))
        if use_rad:
            angles = np.rad2deg(angles)
        return angles
    @classmethod
    def dists(cls, n=50, minmax=(.5, 1.5)):
        import numpy as np
        np.random.seed(cls.seed)
        return np.random.uniform(*minmax, size=(n,))
    @classmethod
    def zmat(cls, ncoords=15, use_rad=False):
        import numpy as np
        np.random.seed(cls.seed)
        refs1 = np.sort(np.random.randint(0, ncoords, ncoords))
        refs2 = np.sort(np.random.randint(0, ncoords, ncoords))
        refs3 = np.sort(np.random.randint(0, ncoords, ncoords))
        ass = np.arange(0, ncoords)
        refs1 = np.amin(np.array((refs1, ass)), axis=0)
        refs2 = np.amin(np.array((refs2, ass)), axis=0)
        for i,rs in enumerate(zip(refs1, refs2)):
            r1, r2 = rs
            if i > 0 and r1 == r2:
                while r1 == r2:
                    r2 = (r2 + 1) % (i + 1)
                    # print(r1, r2, i)
                refs2[i] = r2
        refs3 = np.amin(np.array((refs3, ass)), axis=0)
        for i,rs in enumerate(zip(refs1, refs2, refs3)):
            r1, r2, r3 = rs
            if i > 1 and (r1 == r3 or r2 == r3):
                while (r1 == r3 or r2 == r3):
                    r3 = (r3 + 1) % (i + 1)
                refs3[i] = r3

        # raise Exception(np.array((refs1, refs1-refs2, refs1-refs3, refs2-refs3)))
        dists = DataGenerator.dists(ncoords)
        angles = DataGenerator.angles(ncoords, (0, 180), use_rad=use_rad)
        dihedrals = DataGenerator.angles(ncoords, (0, 360), use_rad=use_rad)

        return np.array([refs1+1, dists, refs2+1, angles, refs3+1, dihedrals ]).T
    @classmethod
    def zmats(cls, m=10, ncoords=15, use_rad=False):
        import numpy as np
        np.random.seed(cls.seed)
        return np.array([DataGenerator.zmat(ncoords, use_rad) for i in range(m)])

class DebugTestClass(unittest.TestSuite):
    """The set of fast tests in the test suite"""
    pass
DebugTests = DebugTestClass()
DebugTests.__name__ = "DebugTests"
class ValidationTestClass(unittest.TestSuite):
    """The set of slow tests in the test suite"""
    pass
ValidationTests = ValidationTestClass()
ValidationTests.__name__ = "ValidationTests"
class TimingTestClass(unittest.TestSuite):
    """The set of timing tests in the test suite"""
    pass
TimingTests = TimingTestClass()
TimingTests.__name__ = "TimingTests"
class InactiveTestClass(unittest.TestSuite):
    """The set of inactive tests in the test suite"""
    pass
InactiveTests = InactiveTestClass()
InactiveTests.__name__ = "InactiveTests"
class DataGenTestClass(unittest.TestSuite):
    """The set of tests in the test suite that exist to generate data"""
    pass
DataGenTests = DataGenTestClass()
DataGenTests.__name__ = "DataGenTests"

def timingTest(fn):
    timer = Timer()(fn)
    def Timing(*args, **kwargs):
        return timer(*args, **kwargs)
    return Timing
def timeitTest(**kwargs):
    timer = Timer(**kwargs)
    def wrap(fn):
        inner_fn = timer(fn)
        def Timing(*args, **kwargs):
            return inner_fn(*args, **kwargs)
        return Timing
    return wrap

def inactiveTest(fn):
    def Inactive(*args, **kwargs):
        return fn(*args, **kwargs)
    Inactive.__og_name__ = fn.__name__
    return Inactive

def debugTest(fn):
    def Debug(*args, **kwargs):
        return fn(*args, **kwargs)
    Debug.__og_name__ = fn.__name__
    return Debug

def dataGenTest(fn):
    def DataGen(*args, **kwargs):
        return fn(*args, **kwargs)
    DataGen.__og_name__ = fn.__name__
    return DataGen

def validationTest(fn):
    def Validation(*args, **kwargs):
        return fn(*args, **kwargs)
    Validation.__og_name__ = fn.__name__
    return Validation

def TestRunner(**kw):
    if not "resultclass" in kw:
        kw["resultclass"] = unittest.TextTestResult
    if not "verbosity" in kw:
        kw["verbosity"] = 2
    return unittest.TextTestRunner(**kw)

_test_loader_map = {
    "Debug" : DebugTests,
    "Validation": ValidationTests,
    "Timing" : TimingTests,
    "Inactive" : InactiveTests,
    "DataGen": DataGenTests
}

class ManagedTestLoader:
    manager = TestManager
    @classmethod
    def load_tests(cls, loader, tests, pattern):
        from itertools import chain

        pkgs = cls.manager.test_files
        names = cls.manager.test_name
        if isinstance(names, str):
            names = names.split(",")
        test_packages = None if pkgs == "All" else set(pkgs)
        if test_packages is None:
            tests = list(chain(*((t for t in suite) for suite in tests)))
        else:
            def _get_suite_name(suite):
                for test in suite:
                    return type(test).__module__.split(".")[-1]
            tests_named = {_get_suite_name(suite):suite for suite in tests}
            tests = []
            for k in tests_named:
                if k in test_packages:
                    tests.extend(tests_named[k])

        for test in tests:
            method = getattr(test, test._testMethodName)
            ttt = method.__name__
            try:
                og = method.__og_name__
            except AttributeError:
                og = ttt
            og = og.split("test_")[-1]

            if names is not None:
                if og not in names:
                    continue
                for suite in _test_loader_map.values():
                    suite.addTest(test)
            else:
                if ttt not in _test_loader_map:
                    ttt = "Debug"
                suite = _test_loader_map[ttt]
                suite.addTest(test)
        #
        # return _test_loader_map.values()

load_tests = ManagedTestLoader.load_tests
def LoadTests(start_dir, manager=TestManager):
    ManagedTestLoader.manager = manager
    unittest.defaultTestLoader.discover(
        start_dir,
        top_level_dir=manager.base_dir
    )
