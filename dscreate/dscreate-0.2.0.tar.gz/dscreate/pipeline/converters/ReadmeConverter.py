from . import BaseConverter
from nbconvert.exporters import MarkdownExporter
from nbconvert.preprocessors import ExtractOutputPreprocessor
from ..preprocessors import AddLanguage
from traitlets import default, Unicode, Type
import os

class ReadmeConverter(BaseConverter):

    name = 'ReadmeConverter'
    printout = 'Generating README...'
    description = '''
    Generates the readme for a notebook.

    This converter has a ``notebook_path`` configurable variable that indicates what notebook should be converted.
    notebook_path defaults to 'index.ipynb' when ``--inline`` is False and ``.solution_files/index.ipynb`` when
    ``--inline`` is True.

    No preprocessors are applied by the ReadmeConverter.
    '''
    
    exporter_class = Type(MarkdownExporter).tag(config=True)
    output = Unicode('README').tag(config=True)

    notebook_path = Unicode(config=True)
    @default('notebook_path')
    def notebook_path_default(self) -> str:
        if self.config.inline.enabled and self.config.inline.solution:
            return os.path.join(self.solution_dir,  'index.ipynb')
        
        return 'index.ipynb'

    @default('preprocessors')
    def preprocessors_default(self) -> list:
        return [ExtractOutputPreprocessor, AddLanguage]

    def convert_notebook(self) -> None:
        """
        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        """
        resources = self.init_notebook_resources()
        output, resources = self.exporter.from_filename(self.notebook_path, resources=resources)
        self.write_notebook(output, resources)
