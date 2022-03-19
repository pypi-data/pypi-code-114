import os
from . import CollectCurriculum
from traitlets.config import Configurable
from traitlets import List

class DsPipeline(Configurable):
        
    name = 'DsPipeline'
    description = '''
    The primary pipeline for dscreate

    DsPipeline's primary variable is ``steps`` containing converter and controller objects.
    Every object included in steps must have ``enabled`` and ``printout`` attributes, and a ``.start``  method
    '''
    steps = List(config=True)
    branches = List(config=True)

    def __init__(self, **kwargs) -> None:
        """
        Set up configuration file.
        """
        super(DsPipeline, self).__init__(**kwargs)

    
    def start(self) -> None:
        for step in self.steps:
            pipeline_step = step(config=self.config)
            if pipeline_step.enabled:
                print(pipeline_step.printout)
                pipeline_step.start()
                self.update_config(pipeline_step.config)
        if self.config.inline.enabled:
            os.remove(self.config.CollectCurriculum.edit_file)