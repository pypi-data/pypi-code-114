from . import ReadmeConverter
from traitlets import default, Unicode, Type
from nbconvert.exporters import MarkdownExporter, Exporter


class SourceConverter(ReadmeConverter):

    name = 'SourceConverter'
    printout = 'Updating solution branch...'
    description = '''
    SourceConverter generates a teacher facing readme for an nbgrader assignment.
    '''

    def convert_notebook(self) -> None:
        super(ReadmeConverter, self).convert_notebook()




        

        