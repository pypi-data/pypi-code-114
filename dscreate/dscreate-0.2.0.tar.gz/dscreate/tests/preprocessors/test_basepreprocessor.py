import pytest 
from .base import BaseTestPreprocessor
from ...pipeline.preprocessors import DsCreatePreprocessor


@pytest.fixture
def preprocessor():
    return DsCreatePreprocessor()

class TestDsCreatePreprocessor(BaseTestPreprocessor):

    pass

