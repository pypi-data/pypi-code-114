import os
import typing
from traitlets import List, Bool, default, Instance, Type, Unicode
from traitlets.config import Configurable, Config
from nbconvert.exporters import Exporter, NotebookExporter
from nbconvert.writers import FilesWriter


class BaseConverter(Configurable):

    name = u'base-converter'
    printout = 'Writing notebook...'
    description = '''
    The base converter that is inherited by all dscreate converters.

    The base converter initializes and activates the exporter and filewriter objects.
    If the  ``--inline`` flag is used with ``ds create``, a `.solution_dir` directory is created.

    The base converter has an ``--output`` argument that allows you to change the name of the output file. 
    This variable defaults to ``'index'``

    When the base converter is used a step in the pipeline, the edit_file is written to disk unchanged.
    '''
    # The writer and exporter objects must be an instance of a particular type.
    # Here we use traitlets to ensure this requirement is met.
    writer = Instance(FilesWriter)
    exporter = Instance(Exporter)

    # The exporter class will change based on the filetype we are converting to.
    # The default exporter class converts a .ipynb file to another .ipynb file
    exporter_class = Type(NotebookExporter, klass=Exporter).tag(config=True)

    # The list of preprocessors used by the exporter.
    # The default list is empty, meaning the notebook will be
    # converted without change (This is primarily used for converting to markdown)
    preprocessors = List([], config=True)

    # The solution attribute is necessary for `inline` notebook splits
    # By default this attribute is set to false. When set to true, the
    # output directory used by the fileswriter is changed to the `solution_dir`
    # attribute
    solution = Bool(False)

    # enabled is a required attribute for all
    # converter objects, and is used by 
    # DsPipeline to ignore disabled converters 
    # (Typically disabled via user provided configurations)
    enabled = Bool(True).tag(config=True)

    # solution_dir is the path for solution files when using an `inline` notebook split
    solution_dir = Unicode(os.path.join(os.getcwd(), '.solution_files')).tag(config=True)

    # The name of the output file. 
    # This default to `index` to match the default
    # exporter class (Notebook). 
    output = Unicode(u'index').tag(config=True)

    def __init__(self, **kwargs) -> None:
        """
        Set up configuration file.
        """
        # Handle configurations via traitlets
        super(BaseConverter, self).__init__(**kwargs)
        # Create an empty config object
        c = Config()
        # Remove the default preprocessors used by nbconvert
        c.Exporter.default_preprocessors = []
        # Update the configurations
        self.update_config(c)

    def start(self) -> None:
        """
        Activate the converter
        """
        # ========= SETUP ===============
        # The fileswriter writes the 
        # transformed notebook and images to disk
        self.writer = FilesWriter(parent=self, config=self.config)

        # The exporter handles the transformation process
        # for a notebook
        self.exporter = self.exporter_class(config=self.config)

        # Add the preprocessors to the exporter
        self._init_preprocessors()

        # ========= ACTIVATION ==========
        self.convert_notebook()

    def _init_preprocessors(self) -> None:
        """
        Here we add the preprocessors to the exporter pipeline
        with the `register_preprocessor` method.
        """
        for pp in self.preprocessors:

            self.exporter.register_preprocessor(pp)


    def convert_notebook(self) -> None:
        """
        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        """
        resources = self.init_notebook_resources()
        output, resources = self.exporter.from_notebook_node(self.config.source_notebook, resources)
        self.write_notebook(output, resources)

    def init_notebook_resources(self) -> dict:
        """
        The resources argument, when passed into an exporter,
        tell the exporter what directory to include in the path 
        for external images via `output_files_dir`. 

        The `output_name` value is required by nbconvert and is typically 
        the name of the original notebook.
        """

        resources = {}
        resources['unique_key'] = self.output
        if self.config.inline.enabled and self.config.inline.solution:
            resources['output_files_dir'] = os.path.join(os.pardir, f'{self.output}_files')
        else:
            resources['output_files_dir'] = f'{self.output}_files'
        return resources

    def write_notebook(self, output, resources) -> None:
        """
        Sets the output directory for the file write
        and writes the file to disk. 
        """
        if self.config.inline.enabled and self.config.inline.solution:
            if not os.path.isdir(self.solution_dir):
                os.mkdir(self.solution_dir)
            self.writer.build_directory = self.solution_dir 

        self.writer.write(output, resources, notebook_name=self.output)



    

        
        

        