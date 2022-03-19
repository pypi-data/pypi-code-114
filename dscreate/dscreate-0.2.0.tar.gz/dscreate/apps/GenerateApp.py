from .BaseApp import DsCreate, dscreate_aliases, dscreate_flags
from traitlets import Bool, default, List, Unicode
from traitlets.config import Config
from typing import List as TypingList
from traitlets.traitlets import MetaHasTraits
from ..pipeline import *
from .. import pipeline

generate_flags = {}
generate_flags.update(dscreate_flags)

generate_aliases = {}
generate_aliases.update(dscreate_aliases)


class GenerateApp(DsCreate):

    name = u'generate'
    description = u'''
    Splits an nbgrader assignment into student facing and teacher facing files
    and uses the arguments to determine which sub application should be activated.

    **Behavior:**

    GenerateApp uses three major variables.

    1. ``pipeline_steps``
        * This variable is a list containing the converters and controllers that are applied to the repository.
    2. ``branches``
        * This variable is a list containing the name of git branches and is used by CheckoutControllers (included in the ``pipeline_steps`` list) to move sequentially across the branches.
        * *It is worth noting that the ``pipeline_steps`` list cannot contain more CheckoutControllers than the length of ``branches``.
    
    This app uses nbgrader's preprocessors to create student facing and and teacher facing versions for the README markdown files. 
    The curriculum notebook is saved to each branch. 
    '''
    flags = generate_flags
    aliases = generate_aliases


    edit_branch = Unicode('master',
                          help="""
                          Sets the name of the git branch used for curriculum development.
                          Default: 'curriculum'
                          """).tag(config=True)

    pipeline_steps = List([
            CollectCurriculum,
            ReleaseConverter,
            Commit,
            Push,

            Checkout,
            BaseConverter,
            SourceConverter,
            Commit,
            Push,
            CheckoutEditBranch,
            ]).tag(config=True)



    branches = List(['master', 'solution'],
                    help="""
                    Sets the branches used for the notebook  split.
                    Default: ['master', 'solution']
                    """).tag(config=True)

    
    def start(self) -> None:
        """
        Activates the application.

        * Adds the name of the edit branch to the application configuration object.
        * Configures the DsPipeline object
        * Adds the branches to the controller objects
        * Initializes a DsPipeline
        * Activates thee pipeline
        """
        super().start()

        c = Config()
        c.edit_branch = self.edit_branch
        c.DsPipeline.steps = self.pipeline_steps
        c.BaseController.branches = self.branches
        self.config.merge(c)
        pipeline = DsPipeline(config=self.config)
        pipeline.start()