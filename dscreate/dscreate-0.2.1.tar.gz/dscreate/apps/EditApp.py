from .BaseApp import DsCreate
from traitlets import Bool, List
from ..pipeline import MergeConverter, DsPipeline

edit_flags = {
    'old': (
    {'MergeConverter': {'old': True}}, "Merge notebooks using deprecated merge technique.")
}

edit_aliases = {
    'output': 'MergeConverter.out',
    'solution_dir':'BaseConverter.solution_dir',
    'concat': 'SortCells.enabled',
    }

class EditApp(DsCreate):

    name = u'edit'
    description = u'''
    Generates an edit file for an in directory notebook split.
    
    **Behavior:**

    1. Notebook filenames and the solution dir are set via BaseConverter traits
    2. Lesson and solution notebooks are read in
    3. Lesson cells and solution cells are concatenated into a single list
    4. Cells are sorted according to cell.metadata.index

    '''
    
    aliases = edit_aliases
    flags = edit_flags

    pipeline_steps = List([MergeConverter]).tag(config=True)
          
    def start(self) -> None:
        super(EditApp, self).start()
        self.config.DsPipeline.steps = self.pipeline_steps
        self.config.DsPipeline.branches = []
        pipeline = DsPipeline(config=self.config)
        pipeline.start()