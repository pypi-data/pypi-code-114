from nbconvert.preprocessors import ExecutePreprocessor
from .BasePreprocessor import DsCreatePreprocessor

class ExecuteCells(DsCreatePreprocessor, ExecutePreprocessor):
    
    description = '''
    ExecuteCells runs code cells in a notebook.
    '''