"""
TODO
"""

from typing import Type

from cppython.project import Project as CPPythonProject
from cppython.project import ProjectConfiguration
from cppython_core.schema import GeneratorDataType, Interface, PyProject
from pdm import Core, Project
from pdm.models.candidates import Candidate
from pdm.signals import post_install


class CPPythonPlugin(Interface):
    """
    TODO
    """

    def __init__(self, core: Core) -> None:

        self.project = None
        post_install.connect(self.on_post_install)

    def read_generator_data(self, generator_data_type: Type[GeneratorDataType]) -> GeneratorDataType:
        return generator_data_type()

    def write_pyproject(self) -> None:
        """
        TODO:
        """

        pass

    def on_post_install(self, project: Project, candidates: dict[str, Candidate], dry_run: bool):
        """
        TODO
        """
        self.project = project

        pdm_pyproject = project.pyproject

        if pdm_pyproject is None:
            return

        pyproject = PyProject(**pdm_pyproject)
        configuration = ProjectConfiguration(verbose=bool(project.core.ui.verbosity))
        cppython_project = CPPythonProject(configuration, self, pyproject)

        cppython_project.install()

    def print(self, string: str) -> None:

        if self.project:
            self.project.core.ui.echo(string)
