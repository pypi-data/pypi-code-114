from .BaseController import BaseController
from .. import DsPipeline
from git import GitCommandError
from traitlets import Bool, Unicode, Int
from traitlets import default

class CommitController(BaseController):

    name = 'CommitController'
    printout = 'Committing Changes'
    description = '''
    Commits changes to a git branch.

    This object has a ``commit_msg`` attribute that can be set from command line using the ``-m`` argument.

    If a commit message is not provided the commit message defaults to 'Updating  <name of branch>'

    '''

    commit_msg = Unicode(config=True)
    count = Int(config=True)

    @default('commit_msg')
    def commit_msg_default(self) -> str:
        return f'Updating {self.active_branch.name}'

    def add_and_commit(self, commit_msg=None):
        self.git.add(".")
        try:
            self.git.commit("-m", commit_msg if commit_msg else self.commit_msg)
        except GitCommandError:
            print("nothing to commit, working tree clean")

    def start(self) -> None:
        self.add_and_commit()
        self.config.CommitController.count = self.count + 1
