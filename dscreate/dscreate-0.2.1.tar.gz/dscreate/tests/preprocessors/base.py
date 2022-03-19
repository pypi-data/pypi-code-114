import io
import os
import pytest
from traitlets import HasTraits, List
from nbformat import read
from .. import CreateCells, LoadNotebooks

class BaseTestPreprocessor(CreateCells, LoadNotebooks):

    required_attributes = ['description',
                            'preprocess',
                            'enabled']

    @pytest.fixture
    def preprocess_base(self, preprocessor, base_notebook):
        resources = {}
        nb, resources = preprocessor.preprocess(base_notebook, resources)
        return nb

    @pytest.fixture
    def preprocess_no_lesson_cells(self, preprocessor, no_lesson_cells_notebook):
        resources = {}
        nb, resources = preprocessor.preprocess(no_lesson_cells_notebook, resources)
        return nb

    def test_required_attributes(self, preprocessor) -> None:
        for attribute in BaseTestPreprocessor.required_attributes:
            assert hasattr(preprocessor,  attribute)


