import pytest 
from traitlets.config import Config
from .base import BaseTestPreprocessor
from ...pipeline.preprocessors import RemoveLessonCells
from nbformat.v4 import new_notebook

@pytest.fixture
def preprocessor():
    return RemoveLessonCells()

class TestRemoveLessonCells(BaseTestPreprocessor):

    
    def test_no_lesson_cells_user_warning(self, preprocessor, no_lesson_cells_notebook):
        with pytest.warns(UserWarning):
            resources = {}
            preprocessor.preprocess(no_lesson_cells_notebook, resources)

    def test_differing_tag_locations(self):
        nb = new_notebook()
        resources = {}
        lesson_cell = self.create_code_lesson_cell()
        solution_cell = self.create_code_solution_cell_tag_location()
        nb.cells = [lesson_cell, solution_cell]
        p = RemoveLessonCells()
        nb, resources = p.preprocess(nb, resources)

        assert len(nb.cells) == 1
        assert nb.cells[0] == p.preprocess_cell(solution_cell)
    
    def test_altered_tag_config(self):
        c = Config()
        c.RemoveLessonCells.solution_tags = {'#==ANSWER=='}
        solution_cell = self.create_code_solution_cell_config_tag()
        lesson_cell = self.create_code_lesson_cell()
        nb = new_notebook()
        nb.cells = [lesson_cell, solution_cell]
        resources = {}
        p = RemoveLessonCells(config=c)
        nb_out, resources = p.preprocess(nb, resources)

        assert len(nb_out.cells) == 1
        assert nb_out.cells[0] == p.preprocess_cell(solution_cell)

    # def test_base_notebook(self, preprocess_base):


    """
    1. Test that a warning is raised if no lesson cells are found.
    2. Test differring locations for tags
    4. Test changing tag configuration
    7. Test cell remove for example notebook
    8. Test length of cells once lesson cells have been removed
    9. Test empty cell
    """



