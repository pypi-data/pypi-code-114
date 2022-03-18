"""
TODO
"""
import pytest
from pdm import Core
from pdm.project import Project
from pytest_cppython.plugin import InterfaceUnitTests

from cppython_pdm.plugin import CPPythonPlugin


class TestCPPythonInterface(InterfaceUnitTests):
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

    def test_install(self, interface: CPPythonPlugin):
        """
        TODO
        """
        interface.on_post_install(project=Project(Core(), None), candidates={}, dry_run=False)
