import tempfile
import io
import os
import pytest
import shutil    
from git import Repo
from traitlets import HasTraits, List
from traitlets.config import Config
from nbformat import read
from .. import CreateCells, LoadNotebooks

class BaseTestConverter(CreateCells, LoadNotebooks):

    required_attributes = ['description',
                            'preprocess',
                            'enabled']


    @pytest.fixture
    def git_remote(self, tmp_path):
        """
        1. Creates a temporary directory
        2. `.git` subdirectory. 
        3. Initializes a bare git repository 
           that serves as the remote pushes are sent to
        4. Returns the path to the git repository
        """
        d = tmp_path / ".git"
        d.mkdir()
        repo = Repo.init(d, bare=True)
        return d

    @pytest.fixture
    def dir_test(self, tmp_path, git_remote):
        """
        1. Creates a temporary directorys
        2. Clones the bare git repository into
           the temporary directory.
        3. Creates a `test` remote that points to a github repository containing
           test files.
        4. Fetches from the `test` remote
        5. Checks out the curriculum branch
        6. Removes the `test` remote
        7. Returns the path to the repository
        """
        d = tmp_path / 'repo'
        d.mkdir()
        cloned_repo = Repo.clone_from(git_remote, d)
        remote = cloned_repo.create_remote('test', url=self.repo_test())
        remote.fetch()
        cloned_repo.git.checkout('curriculum')
        cloned_repo.git.remote('rm', 'test')

        return d

    def repo_test(self):
        """
        Returns the url for a test repository.
        """
        return 'https://github.com/learn-co-curriculum/dscreate-create-test.git'

    def edit_file(self):
        """
        Returns the name of the edit .ipynb file. 
        """
        return 'index.ipynb'

    @pytest.fixture
    def config(self, dir_test):
        """
        Sets up the config for the converters.

        1. Changes the current working directory the the `dir_test` repository
        2. Reads in the edit file in the repository
        3. Initializes a traitlets config object
        4. Sets the `source_notebook` config
        5. Sets the `inline` configs
        6. Returns the config object
        """
        cwd = os.getcwd()
        os.chdir(dir_test)
        nb = self.read_nb(self.edit_file())
        c = Config()
        c.source_notebook = nb
        c.inline = Config()
        c.inline.enabled = False
        c.inline.solution = False
        os.chdir(cwd)
        return c

    @pytest.fixture
    def inline_config(self, config):
        config.inline.enabled = True
        config.inline.solution = True
        return config

