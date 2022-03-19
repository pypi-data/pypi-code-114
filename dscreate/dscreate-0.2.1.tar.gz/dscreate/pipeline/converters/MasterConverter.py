from .BaseConverter import BaseConverter
from ..preprocessors import ClearOutput, RemoveSolutionCells, AddCellIndex
from traitlets import default, List

class MasterConverter(BaseConverter):

    name = 'MasterConverter'
    printout = 'Updating master branch...'
    description = '''
    The master converter is used to generate the student facing notebook.

    The preprocessors default to the nbconvert ClearOutput and dscreate RemoveSolutions preprocessors.
    '''

    preprocessors = List([ClearOutput, AddCellIndex, RemoveSolutionCells]).tag(config=True)

    def start(self) -> None:

        if self.config.inline.enabled:
            self.config.inline.solution = False

        super(MasterConverter, self).start()
