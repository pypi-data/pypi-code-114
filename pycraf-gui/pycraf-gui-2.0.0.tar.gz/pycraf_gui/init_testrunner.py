#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:

    # Create the test function for self test
    from astropy.tests.runner import TestRunner, keyword

    class MyRunner(TestRunner):

        @keyword(False)
        def dogui(self, opt, kwargs):
            """
            dogui : `bool`
                The parameter description for the run_tests docstring.
            """
            # Return value must be a list with a CLI parameter for pytest.
            return ['--dogui'] if opt else ['']

    test = MyRunner.make_test_runner_in(os.path.dirname(__file__))

except ImportError:

    def test():

        import warnings
        warnings.warn(
            'Package "astropy" is needed for using the "test()" function'
            )

test.__test__ = False
__all__ = ['test']
