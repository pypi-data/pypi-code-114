from traitlets.config import Configurable
from traitlets import Unicode, default
import nbformat
import os


class CollectCurriculum(Configurable):

    name = 'CollectCurriculum'
    printout = 'Reading curriculum file...'
    description = '''
    CollectCurriculum reads in the edit_file and stores the notebook in the application
    configuration object.
    '''
    enabled = True
    edit_file = Unicode('index.ipynb').tag(config=True)
    edit_branch = Unicode('curriculum').tag(config=True)

    def start(self) -> None:
        notebook = nbformat.read(self.edit_file, as_version=4)
        self.config.source_notebook = notebook



