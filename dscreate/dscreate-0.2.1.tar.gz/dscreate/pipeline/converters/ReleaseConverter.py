from . import BaseConverter
from traitlets import default, Unicode, Type
from nbconvert.exporters import MarkdownExporter, Exporter
from nbgrader.preprocessors import (ClearSolutions, LockCells, 
                                    ComputeChecksums, ClearOutput, 
                                    ClearHiddenTests, ClearMarkScheme)

class ReleaseConverter(BaseConverter):

    name = 'ReleaseConverter'
    printout = 'Generating Release README...'
    description = '''
    ReleaseConverter replicates ``nbgrader generate``
    '''
    exporter_class = Type(MarkdownExporter, klass=Exporter).tag(config=True)

    @default('preprocessors')
    def preprocessors_default(self) -> list:
        return [ClearSolutions, 
                ClearOutput, 
                ClearHiddenTests, 
                ClearMarkScheme]

    notebook_path = Unicode('index.ipynb').tag(config=True)
    output = Unicode('README').tag(config=True)

    def convert_notebook(self) -> None:
        """
        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        """
        resources = self.init_notebook_resources()
        output, resources = self.exporter.from_filename(self.notebook_path, resources=resources)
        self.write_notebook(output, resources)

        