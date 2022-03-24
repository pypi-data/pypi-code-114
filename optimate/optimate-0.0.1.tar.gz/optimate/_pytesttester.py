"""
Pytest test running.

This module implements the ``test()`` function for optimate modules. The usual
method for doing that is to put the following in the module
``__init__.py`` file::

    from optimate._pytesttester import PytestTester
    test = PytestTester(__name__)
    del PytestTester
"""
import sys
import os

__all__ = ['PytestTester']



def _show_optimate_info():
    import optimate as opt

    print("optimate version %s" % opt.__version__)


class PytestTester:
    
    """
    Pytest test runner.
    
    A test function is typically added to a package's __init__.py like so::
      from numpy._pytesttester import PytestTester
      test = PytestTester(__name__).test
      del PytestTester
      
    Calling this test function finds and runs all tests associated with the
    module and all its sub-modules.
    
    Attributes
    ----------
    module_name : str
        Full path to the package to test.
        
    Parameters
    ----------
    module_name : module name
        The name of the module to test.
    """
    
    def __init__(self, module_name):
        self.module_name = module_name
        

    def __call__(self, extra_argv=None, coverage=False, tests=None):
        
        """
        Run tests for module using pytest.
        
        Parameters
        ----------
        extra_argv : list, optional
            List with any extra arguments to pass to pytests.
            
        coverage : bool, optional
            If True, report coverage of optimate code. Default is False.
            Requires installation of (pip) pytest-cov.
            
        tests : test or list of tests
            Tests to be executed with pytest '--pyargs'
            
        Returns
        -------
        result : bool
            Return True on success, false otherwise.
            
        Notes
        -----
        Each optimate module exposes `test` in its namespace to run all tests for
        it. For example, to run all tests for numpy.lib:
        
        >>> opt.test()
        
        Examples
        --------
        >>> result = opt.test()
        ...
        
        """
        
        import pytest

        module = sys.modules[self.module_name]
        module_path = os.path.abspath(module.__path__[0])

        # setup the pytest arguments
        pytest_args = ["-l"]

        # offset verbosity. The "-q" cancels a "-v".
        pytest_args += ["-q"]

        if extra_argv:
            pytest_args += list(extra_argv)

        if coverage:
            pytest_args += ["--cov=" + module_path]

        if tests is None:
            tests = [self.module_name]

        pytest_args += ["--pyargs"] + list(tests)

        # run tests.
        _show_optimate_info()

        try:
            code = pytest.main(pytest_args)
        except SystemExit as exc:
            code = exc.code

        return code == 0
