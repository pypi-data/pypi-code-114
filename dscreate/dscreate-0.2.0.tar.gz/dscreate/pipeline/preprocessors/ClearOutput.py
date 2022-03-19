from nbconvert.preprocessors import ClearOutputPreprocessor
from .BasePreprocessor import DsCreatePreprocessor

class ClearOutput(DsCreatePreprocessor, ClearOutputPreprocessor):
    
    description = '''
ClearOutput removes the outputs for notebook cells.
    '''