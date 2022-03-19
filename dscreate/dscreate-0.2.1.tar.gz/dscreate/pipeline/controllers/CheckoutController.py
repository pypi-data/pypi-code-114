from .BaseController import BaseController
from .. import DsPipeline
from git import GitCommandError
from traitlets import Bool, Unicode, default
from . import CommitController

class CheckoutController(BaseController):

    name = 'CheckoutController'
    description = '''
    Checkout branches set by the running application.

    This controller relies on a configuration object that contains the following variables

    * ``BaseController.branches``
    * ``CommitController.count

    The commit controller count is added to the config object if it does not exist, but does not increment the count. 
    The count variable is used to identify the next branch in the BaseController.branches sequence.

    dscreate uses a "force" merge strategy which overwrites each branch with the most recent edit branch commit.
    It is equivalent to running ``git merge <name of branch> -X theirs``
    '''
    printout = Unicode(config=True)
    @default('printout')
    def printout_default(self) -> str:
        return 'Checking out {}...'.format(self.get_branch())

    def get_branch(self):
        if not isinstance(self.config.CommitController.count, int):
            self.config.CommitController.count = 0
        return self.config.BaseController.branches[self.config.CommitController.count]

    def merge_edit_branch(self):
        self.git.merge(self.config.traversed_branches[0], X='theirs')

    def start(self) -> None:
        active_branch = self.active_branch.name
        if not isinstance(self.config.traversed_branches, list):
            self.config.traversed_branches = []
        self.config.traversed_branches.append(active_branch)
        
        branch = self.get_branch()
        self.git.checkout(branch)
        self.merge_edit_branch()
