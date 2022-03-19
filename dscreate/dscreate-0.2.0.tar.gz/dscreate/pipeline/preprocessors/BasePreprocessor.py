from nbconvert.preprocessors import Preprocessor
from traitlets import Bool

class DsCreatePreprocessor(Preprocessor):

    description = '''
    The base preprocessor object for dscreate.
    '''
    enabled = Bool(True, help="Whether to use this preprocessor when running dscreate").tag(config=True)

