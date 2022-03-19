from traitlets import Unicode
from warnings import warn
from copy import deepcopy
from .BasePreprocessor import DsCreatePreprocessor


class AddLanguage(DsCreatePreprocessor):

    description = '''
    Adds name of coding language to code blocks.
    '''

    language = Unicode('python').tag(config=True)

    def preprocess(self, nb, resources):

        nb_copy = deepcopy(nb)

        if not 'language_info' in nb_copy.metadata:
            nb_copy.metadata['language_info'] = {}

        nb_copy.metadata['language_info']['name'] = self.language

        return nb_copy, resources


