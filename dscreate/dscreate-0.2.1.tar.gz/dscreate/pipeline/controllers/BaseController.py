from traitlets import Unicode, Bool, default, List
from traitlets.config import Configurable, Config
import typing
from git import Repo

class BaseController(Configurable, Repo):

    name = 'BaseController'
    description = """
    The base controller object. 

    **Behavior:**

    This object is used to configure git repository controller objects.

    Primarily, controllers inherit ``enabled`` and ``branches`` attributes from the BaseController.

    ``enabled``
    * When enabled is true, the controller is used during the notebook split
    """
    branches = List(['curriculum', 'master', 'solution']).tag(config=True)

    enabled = Bool(config=True)
    @default('enabled')
    def enabled_default(self) -> bool:
        return True

    def __init__(self, **kwargs) -> None:
        """
        1. Set up configuration file.
        2. Inherit git repo attributes
        """
        Configurable.__init__(self, **kwargs)
        Repo.__init__(self, '.')




    
