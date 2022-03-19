import os
import io
import pytest
from nbformat import read
from nbformat.v4 import new_code_cell, new_markdown_cell


class CreateCells:

    def create_code_solution_cell(self):
        source = """#==SOLUTION==
num = 2 + 2
num
    """
        cell = new_code_cell(source=source)
        return cell

    def create_code_solution_cell_tag_location(self):
        source = """num = 2 + 2
num
#==SOLUTION==
"""
        cell = new_code_cell(source=source)
        return cell

    def create_code_solution_cell_tag_shared_line(self):
        source = """num = 2 + 2
num
#==SOLUTION==
"""
        cell = new_code_cell(source=source)
        return cell

    def create_code_lesson_cell(self):
        source = """num = 2 + 2
num
    """
        cell = new_code_cell(source=source)
        return cell

    def create_markdown_solution_cell(self):
        source = """==SOLUTION==
this is a markdown cell
        """
        cell = new_markdown_cell(source=source)
        return cell

    def create_markdown_solution_cell_tag_location(self):
        source = """this is a markdown cell

==SOLUTION==
        """
        cell = new_markdown_cell(source=source)
        return cell

    def create_markdown_solution_cell_tag_location(self):
        source = """this is a markdown cell

==SOLUTION==
        """
        cell = new_markdown_cell(source=source)
        return cell

    def create_code_solution_cell_config_tag(self):
        source = """#==ANSWER==
num = 2 + 2
num
    """
        cell = new_code_cell(source=source)
        return cell

    def create_markdown_solution_cell_config_tag(self):
        source = """==ANSWER==
this is a markdown cell
        """
        cell = new_markdown_cell(source=source)
        return cell

class LoadNotebooks:

    dir_path = os.path.abspath(os.path.dirname(__file__))

    def notebook_path(self, directory, file_name):
        return os.path.join(LoadNotebooks.dir_path, directory, file_name)

    def read_nb(self, filepath):
        with io.open(filepath, mode="r", encoding="utf-8") as file:
            nb = read(file, as_version=4)
        return nb

    @pytest.fixture
    def base_notebook(self):
        path = self.notebook_path('files', 'base_notebook.ipynb')
        nb = self.read_nb(path)
        return nb

    @pytest.fixture
    def no_lesson_cells_notebook(self):
        path = self.notebook_path('files', 'no_lesson_cells_notebook.ipynb')
        nb = self.read_nb(path)
        return nb

    @pytest.fixture
    def no_solution_cells_notebook(self):
        path = self.notebook_path('files', 'no_solution_cells_notebook.ipynb')
        nb = self.read_nb(path)
        return nb



