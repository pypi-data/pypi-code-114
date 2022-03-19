from copy import deepcopy
from .BasePreprocessor import DsCreatePreprocessor

class SortCells(DsCreatePreprocessor):

    description = '''
    Sorts the cells of a notebook according to the metadata.index variable
    and adds a solution tag back to solution cells.
    '''
    
    def preprocess(self, nb, resources):
        
        nb_copy = deepcopy(nb)
        # Sort cells
        cells = list(sorted(nb_copy.cells, key=lambda x: int(x['metadata']['index'])))

        # Remove duplicates
        nb_copy.cells = []
        indices = []
        idx_mapper = {}
        for idx, cell in enumerate(cells):
            # Inline markdown solution cells require the solution notebook's source be used
            # as the edit_file source. Here, if the lesson cell was added first, we overwrite
            # the source with the solution cell's data
            if cell.cell_type == 'markdown' and cell.metadata.solution and cell.metadata.index in indices:
                replace_idx = idx_mapper[cell.metadata.index]
                nb_copy.cells[replace_idx] = self.preprocess_cell(cell, resources, idx)[0]

            if cell['metadata']['index'] not in indices:
                nb_copy.cells.append(self.preprocess_cell(cell, resources, idx)[0])
                idx_mapper[cell.metadata.index] = len(nb_copy.cells) - 1
                indices.append(cell['metadata']['index'])

        return nb_copy, resources

    def preprocess_cell(self, cell, resources, cell_index):

        # Add solution tag to solution cells
        if cell.get('metadata', {}).get('solution', {}):
            if cell.cell_type == 'code':
                cell.source = '#==SOLUTION==\n' + cell.source
            else:
                cell.source = '==SOLUTION==\n\n' + cell.source

        return cell, resources
