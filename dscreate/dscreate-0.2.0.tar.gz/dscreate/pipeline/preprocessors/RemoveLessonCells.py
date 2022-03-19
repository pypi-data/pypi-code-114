from traitlets import Set
from warnings import warn
from copy import deepcopy
from .BasePreprocessor import DsCreatePreprocessor


class RemoveLessonCells(DsCreatePreprocessor):

    description = '''
    RemoveLessonCells removes cells that do not contain a tag included in the ``solution_tags`` variable.

    ``solution_tags`` are a  configurable variable. Defaults to {'#__SOLUTION__', '#==SOLUTION==', '__SOLUTION__', '==SOLUTION=='}
    '''
    
    solution_tags = Set({'#__SOLUTION__', '#==SOLUTION==', '__SOLUTION__', '==SOLUTION=='},
            help=("Tags indicating which cells are to be removed"
            )).tag(config=True)


    def is_solution(self, cell):
        """
        Checks that a cell has a solution tag. 
        """

        lines = set(cell.source.split("\n"))
        lines = {line.strip().replace(' ', '') for line in lines}

        return self.solution_tags.intersection(lines)



    def preprocess(self, nb, resources):

        nb_copy = deepcopy(nb)

        # Skip preprocessing if the list of patterns is empty
        if not self.solution_tags:
            return nb, resources

        # Filter out cells that meet the conditions
        cells = []
        for cell in nb_copy.cells:
            if self.is_solution(cell) or cell.cell_type == 'markdown':
                cells.append(self.preprocess_cell(cell))
         
        
        if len(nb_copy.cells) == len(cells):
            warn("No lesson cells were found in the notebook!" 
            " Double check the solution tag placement and formatting if this is not correct.", UserWarning)

        
        nb_copy.cells = cells



        return nb_copy, resources

    def preprocess_cell(self, cell):
        """
        Removes the solution tag from the solution cells.
        """

        lines = cell.source.split('\n')
        no_tags = [line for line in lines if line.strip().replace(' ', '') not in self.solution_tags]
        cell.source = '\n'.join(no_tags)
        return cell
