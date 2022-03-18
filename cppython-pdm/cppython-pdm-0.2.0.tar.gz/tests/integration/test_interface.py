"""
TODO
"""
import pytest
from pdm import Core
from pytest_cppython.plugin import InterfaceIntegrationTests

from cppython_pdm.plugin import CPPythonPlugin


class TestCPPythonInterface(InterfaceIntegrationTests):
    """
    The tests for the PDM interface
    """

    @pytest.fixture(name="interface")
    def fixture_interface(self) -> CPPythonPlugin:
        """
        Override of the plugin provided interface fixture.

        Returns:
            ConsoleInterface -- The Interface object to use for the CPPython defined tests
        """
        return CPPythonPlugin(Core())
