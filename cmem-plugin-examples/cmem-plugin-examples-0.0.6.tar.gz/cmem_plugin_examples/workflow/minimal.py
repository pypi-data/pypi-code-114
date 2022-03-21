"""minimal workflow plugin"""
from cmem_plugin_base.dataintegration.description import Plugin
from cmem_plugin_base.dataintegration.plugins import WorkflowPlugin


@Plugin(label="Minimal Example")
class Minimal(WorkflowPlugin):
    """Example Minimal Workflow Plugin"""

    def execute(self, inputs=None):
        # config can be retrieved like this
        config = self.config.get()
        # plugins can also write in the DI log
        self.log.info(f"Config length: {len(config)}")
