import pytest 
from traitlets.config import Config
from .base import BaseTestPreprocessor
from ...pipeline.preprocessors import RemoveSolutionCells
from nbformat.v4 import new_notebook

@pytest.fixture
def preprocessor():
    return RemoveSolutionCells()

class TestRemoveSolutionCells(BaseTestPreprocessor):

    def test_differing_tag_locations(self):
        nb = new_notebook()
        resources = {}
        lesson_cell = self.create_code_lesson_cell()
        solution_cell = self.create_code_solution_cell_tag_location()
        nb.cells = [lesson_cell, solution_cell]
        p = RemoveSolutionCells()
        nb, resources = p.preprocess(nb, resources)

        assert len(nb.cells) == 1
        assert nb.cells[0] == lesson_cell
    
    def test_altered_tag_config(self):
        c = Config()
        c.RemoveSolutionCells.code_tags = {'#==ANSWER=='}
        solution_cell = self.create_code_solution_cell_config_tag()
        lesson_cell = self.create_code_lesson_cell()
        nb = new_notebook()
        nb.cells = [lesson_cell, solution_cell]
        resources = {}
        p = RemoveSolutionCells(config=c)
        nb_out, resources = p.preprocess(nb, resources)

        assert len(nb_out.cells) == 1
        assert nb_out.cells[0] == lesson_cell

    # TODO
    def test_base_notebook(self, preprocess_base):
        pass
    
    # TODO
    def test_tag_casing_warning(self, preprocessor):
        pass
    
    # TODO
    def test_tag_formatting_warning(self, preprocessor):
        pass

    # Create no_solution_cells_notebook
    # Add no_solution_cells_notebook fixture to LoadNotebooks
    def test_no_solution_cells_user_warning(self, preprocessor, no_solution_cells_notebook):
        with pytest.warns(UserWarning):
            resources = {}
            preprocessor.preprocess(no_solution_cells_notebook, resources)





