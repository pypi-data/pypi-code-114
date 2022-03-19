import os
import nbformat
from traitlets.config import Config
from nbconvert.writers import FilesWriter
from nbconvert.exporters import NotebookExporter
from nbgrader.preprocessors import (ClearSolutions,
                                    LockCells,
                                    ComputeChecksums,
                                    CheckCellMetadata,
                                    ClearOutput,
                                    ClearHiddenTests,
                                    ClearMarkScheme)

def get_nbgrader_directory():
    """
    Helper function for finding the top level directory of an nbgrader course.

    This function searches for the word 'source' in the absolute path of the current working directory, and uses the
    placement of the source folder to find the top level of the nbgrader course

    Returns: str. directory path.
    """

    # Get current working directory
    path = os.getcwd()
    # Split and reverse the cwd path
    split = path.split(os.sep)[::-1]
    if 'source' not in split:
        return None

    # Move up a directory for each directory beneath and equal to the source directory
    top_directory = ''
    for idx in range(len(split)):
        top_directory = os.path.join(top_directory, '..')
        if split[idx] == 'source':
            break

    return top_directory

def nbgrader_generate(notebook_path, config=None):
    # Read in the notebook
    notebook = nbformat.read(notebook_path, as_version=4)

    # Set up the config
    if not config:
        c = Config()
    else:
        c = config
        
    c.NotebookExporter.preprocessors = [ClearSolutions,
                                        LockCells,
                                        ComputeChecksums,
                                        CheckCellMetadata,
                                        ClearOutput,
                                        ClearHiddenTests,
                                        ClearMarkScheme]

    # Convert the notebook
    exporter = NotebookExporter(config=c)
    nb, resources = exporter.from_notebook_node(notebook)
    fw = FilesWriter(config=c)
    fw.write(nb, resources, notebook_name='index')
