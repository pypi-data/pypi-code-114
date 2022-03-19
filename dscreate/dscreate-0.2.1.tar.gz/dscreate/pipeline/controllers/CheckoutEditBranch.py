from .BaseController import BaseController
from .. import DsPipeline
from git import GitCommandError
from traitlets import Bool
from . import CommitController

class CheckoutEditBranch(BaseController):

    name = 'CheckoutEditBranch'
    printout = 'Checking out the edit branch...'
    description = '''
    This controller checkouts the first branch of the branches configuration variable.
    '''

    def start(self) -> None:
        edit_branch = self.config.traversed_branches[0]
        self.git.checkout(edit_branch)
