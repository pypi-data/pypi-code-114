from .BaseConverter import BaseConverter
from ..preprocessors import *
from traitlets import default, List


class SolutionConverter(BaseConverter):

    name = 'SolutionConverter'
    printout = 'Updating solutions...'
    description = '''
    SolutionConverter generates the teacher facing  notebook.
    '''

    @default('solution')
    def solution_default(self) -> bool:
        return True

    preprocessors = List([ClearOutput, AddCellIndex, RemoveLessonCells, ExecuteCells]).tag(config=True)

    def start(self) -> None:

        if self.config.inline.enabled:
            self.config.inline.solution = True

        super(SolutionConverter, self).start()


