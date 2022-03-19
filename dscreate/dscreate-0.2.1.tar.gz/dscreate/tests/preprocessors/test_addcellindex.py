import pytest 
import os
from .base import BaseTestPreprocessor
from ...pipeline.preprocessors import AddCellIndex
from nbformat.v4 import new_notebook

@pytest.fixture
def preprocessor():
    return AddCellIndex()

class TestAddCellIndex(BaseTestPreprocessor):

    def test_has_index(self, preprocess_base) -> None:
        
        cells = preprocess_base.cells
        for cell in cells:
            assert 'index' in cell.get('metadata', {})

    def test_has_solution(self, preprocess_base):
        cells = preprocess_base.cells
        for cell in cells:
            assert 'solution' in cell.get('metadata', {})
    
    def test_solution_cell(self, preprocessor):
        solution_cell = self.create_code_solution_cell()
        nb = new_notebook()
        nb.cells = [solution_cell]
        resources = {}
        nb, resources = preprocessor.preprocess(nb, resources)
        assert 'index' in nb.cells[0]['metadata']
        assert isinstance(nb.cells[0]['metadata']['index'], int)
        assert isinstance('solution' in nb.cells[0]['metadata'], bool)

    def test_solution_markers(self,  preprocess_base):
        solution_markers = [cell.get('metadata', {}).get('solution') for cell in preprocess_base.cells]
        marker_keys = [False, False, True,  True,  True, True, False, False]
        assert len(solution_markers) ==  len(marker_keys)
        
        for check, key in zip(solution_markers, marker_keys):
            assert isinstance(check, bool)
            assert check == key

