from .BaseApp import DsCreate
from traitlets import List
from traitlets.config import Config
from ..pipeline import ReadmeConverter, DsPipeline

aliases = {
    'notebook':'ReadmeConverter.notebook_path',
    'output': 'ReadmeConverter.output'
    }

class MarkdownApp(DsCreate):

    name = 'MarkdownApp'
    description ="""
    Converts a notebook to markdown.

    The name of notebook must be provided as an argument or via `--notebook`
    The output file defaults to `README.md` but can be set via `--output`
    """

    pipeline_steps = List([

        ReadmeConverter,

        ]).tag(config=True)

    def start(self) -> None:
        super().start()

        if len(self.extra_args) > 1:
            raise ValueError("Only one argument (the notebook path) may be specified")
        elif len(self.extra_args) == 0:
            raise ValueError("A notebook path must be specified, either as an argument or with --notebook")
    
        c = Config()
        c.DsPipeline.steps = self.pipeline_steps
        c.ReadmeConverter.notebook_path = self.extra_args[0]
        self.config.merge(c)
        pipeline = DsPipeline(config=self.config)
        pipeline.start()