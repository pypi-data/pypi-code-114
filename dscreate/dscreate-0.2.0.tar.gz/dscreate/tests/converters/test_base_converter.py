import pytest 
import os
from .base import BaseTestConverter
from ...pipeline import BaseConverter, RemoveLessonCells
from nbconvert.exporters import Exporter, NotebookExporter
from nbconvert.writers import FilesWriter
from traitlets.traitlets import TraitError
from traitlets.config import Config
from nbformat import read


class TestBaseConverter(BaseTestConverter):

    @pytest.fixture
    def converter(self, config):
        converter = BaseConverter(config=config)
        return converter

    @pytest.fixture
    def inline_converter(self, inline_config):
        converter = BaseConverter(config=inline_config)
        return converter

    @pytest.fixture
    def converters(self, converter, inline_converter):
        return [converter, inline_converter]

    @pytest.fixture
    def run_converter(self, dir_test, config) -> None:
        cwd = os.getcwd()
        os.chdir(dir_test)
        converter = BaseConverter(config=config)
        converter.start()
        os.chdir(cwd)
        return dir_test

    def test_converter_init(self, converters):
        for conv in converters:
            config = conv.config

            # Ensure default exporter preprocessors have been removed
            assert config.Exporter.default_preprocessors == []
            # Ensure the parent class has been initialized
            assert hasattr(conv, 'parent')


    def test_traits(self, converters):
        traits = ['name', 'printout', 'description',
                  'exporter_class', 'preprocessors', 
                  'solution', 'enabled',
                  'solution_dir', 'output']
        for conv in converters:
             for trait in traits:
                 assert hasattr(conv, trait)

    def test_default_converter_traits(self, converters):
        for conv in converters:
            
            assert conv.exporter_class == NotebookExporter
            assert conv.preprocessors == []
            assert type(conv.solution) == bool
            assert conv.solution == False
            assert type(conv.enabled) == bool
            assert conv.enabled == True
            assert conv.solution_dir == os.path.join(os.getcwd(), '.solution_files')
            assert conv.output == 'index'
            
            try:
                conv.writer
            except TraitError:
                pass
            try:
                conv.exporter
            except TraitError:
                pass

    def test_default_run(self, converter, dir_test):
        cwd = os.getcwd()
        os.chdir(dir_test)

        converter.start()

        saved_cells = self.read_nb(self.edit_file()).cells
        orig_cells = converter.config.source_notebook.cells
        assert len(saved_cells) == len(orig_cells)

        os.chdir(cwd)

    def test_preprocessor_disabled(self, converter, dir_test):
        cwd = os.getcwd()
        os.chdir(dir_test)
        converter.preprocessors = [RemoveLessonCells]
        
        config = Config()
        config.RemoveLessonCells.enabled = False
        converter.update_config(config)

        converter.start()
        
        assert converter.exporter._trait_values['_preprocessors'][0].__class__ == RemoveLessonCells

        saved_cells = self.read_nb(self.edit_file()).cells
        orig_cells = converter.config.source_notebook.cells
        assert len(saved_cells) == len(orig_cells)

        os.chdir(cwd)

    def test_preprocessor_enabled(self, converter, dir_test):
        cwd = os.getcwd()
        os.chdir(dir_test)
        converter.preprocessors = [RemoveLessonCells]
        
        config = Config()
        config.RemoveLessonCells.enabled = True
        converter.update_config(config)

        converter.start()
        
        assert converter.exporter._trait_values['_preprocessors'][0].__class__ == RemoveLessonCells

        saved_cells = self.read_nb(self.edit_file()).cells
        orig_cells = converter.config.source_notebook.cells
        assert len(saved_cells) != len(orig_cells)

        os.chdir(cwd)

    def test_inline_default(self, inline_config, dir_test):
        cwd = os.getcwd()
        os.chdir(dir_test)
        assert cwd != os.getcwd()
        solution_dir = os.path.join(dir_test, '.solution_files')
        inline_config.BaseConverter.solution_dir = solution_dir
        converter = BaseConverter(config=inline_config)
        solution_dir_before = os.path.isdir(solution_dir)
        assert solution_dir_before == False
        converter.start()
        solution_dir_after = os.path.isdir(solution_dir)
        assert solution_dir_before != solution_dir_after
        os.chdir(cwd)

    def test_output_config(self, config, dir_test):
        cwd = os.getcwd()
        os.chdir(dir_test)

        config.BaseConverter.output = 'test_file'
        converter = BaseConverter(config=config)
        converter.start()

        assert os.path.isfile('test_file.ipynb')

        os.chdir(cwd)








    

    
        




    
            


            




    

        

