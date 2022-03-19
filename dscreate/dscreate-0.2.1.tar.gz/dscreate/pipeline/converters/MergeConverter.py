import io
import os
from .BaseConverter import BaseConverter
from ..preprocessors import *
from nbformat import read
from nbformat.v4 import new_notebook
from traitlets import List, Unicode, Bool


class MergeConverter(BaseConverter):

    name = 'MergeConverter'
    printout = 'Merging notebooks...'
    description = '''
    MergeConverter reads in lesson and solution notebooks and merges them into an edit file.
    '''

    preprocessors = List([SortCells]).tag(config=True)
    output = Unicode(u'curriculum').tag(config=True)
    old = Bool(False).tag(config=True)

    def read_notebook(self, filepath):
        with io.open(filepath, mode="r", encoding="utf-8") as file:
            nb = read(file, as_version=4)
        return nb

    def paths(self):
        lesson_path = self.config.BaseConverter.output + '.ipynb'
        solution_path = os.path.join(self.config.BaseConverter.solution_dir, 
                                   lesson_path)
        return lesson_path, solution_path

    def start(self) -> None:
        nb = new_notebook()

        # Read in notebooks
        lesson, solution = self.paths()
        lesson_nb = self.read_notebook(lesson)
        solution_nb = self.read_notebook(solution)

        # Add solution metadata to notebooks 
        # That were split with old version of dscreate
        if self.old:
            for idx, cell in enumerate(lesson_nb.cells):
                cell['metadata']['solution'] = False
                lesson_nb.cells[idx] = cell

            for idx, cell in enumerate(solution_nb.cells):
                cell['metadata']['solution'] = True
                solution_nb.cells[idx] = cell

        # Concatenate cells
        nb.cells.extend(lesson_nb.cells)
        nb.cells.extend(solution_nb.cells)

        if self.old:
            nb.cells = [cell for cell in nb.cells if cell['metadata']['index'] != 'Placeholder']

        # Setup BaseConverter's write_notebook
        self.config.source_notebook = nb

        super(MergeConverter, self).start()

    


