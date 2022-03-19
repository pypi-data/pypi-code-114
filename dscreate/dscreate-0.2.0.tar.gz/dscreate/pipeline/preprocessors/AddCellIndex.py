from copy import deepcopy
from traitlets import Set, Int
from .BasePreprocessor import DsCreatePreprocessor


class AddCellIndex(DsCreatePreprocessor):

    description = '''
    AddCellIndex adds a metadata.index variable to a notebook and determines if a cell is a solution cell.
    This preprocessor is used primarily for ``--inline`` splits.
    '''
    index = Int(0)

    solution_tags = Set({'#__SOLUTION__', '#==SOLUTION==', '__SOLUTION__', '==SOLUTION=='},
            help=("Tags indicating which cells are to be removed"
            )).tag(config=True)

    def preprocess(self, nb, resources):

        nb_copy = deepcopy(nb)

        # Filter out cells that meet the conditions
        nb_copy.cells = [self.preprocess_cell(cell, resources, index)[0]
                    for index, cell in enumerate(nb_copy.cells)]

        return nb_copy, resources

    def preprocess_cell(self, cell, resources, cell_index):
        """
        No transformation is applied.
        """
        lines = set(cell.source.split("\n"))
        if self.solution_tags.intersection(lines):
            cell['metadata']['solution'] = True
        else:
            cell['metadata']['solution'] = False

        cell['metadata']['index'] = self.index
        self.index += 1
        return cell, resources
