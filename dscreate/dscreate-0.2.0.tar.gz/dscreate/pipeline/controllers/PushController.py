from git import GitCommandError
from traitlets import Bool, Unicode, default

from .. import DsPipeline
from . import CommitController, BaseController


class PushController(BaseController):

    name = 'PushController'
    printout = 'Pushing to remote...'
    description = '''
    Pushing changes to the remote.

    Remote is a configurable variables that defaults to 'origin'
    '''

    remote = Unicode(config=True)
    @default('remote')
    def branch_default(self) -> str:
        return u'origin'

    def get_branch(self):
        if not isinstance(self.config.CommitController.count, int):
            return self.config.BaseController.branches[0]

        return self.config.BaseController.branches[self.config.CommitController.count - 1]

    def start(self) -> None:
        branch = self.get_branch()
        self.git.push(self.remote, branch)