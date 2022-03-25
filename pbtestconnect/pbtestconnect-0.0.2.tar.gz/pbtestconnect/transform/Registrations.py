
import sys
from .IExecuteScripts import IExecuteScripts

def Register(requires_connection:bool, produces:str):
    """
    Registers a class as a script executor. The class must implement IExecuteScripts.

    Note: only one IExecuteScripts class in your script can be registered.

    requires_connection - indicates that your script handler expects a Connector Connection Id.
    
    produces - indicates the mime type that the script handler produces.
    """
    def wrap(cls):
        if not issubclass(cls, IExecuteScripts):
            raise Exception("'{name}' does not implement IExecuteScripts interface.".format(name=cls.__name__))

        # at the module level...register the class.
        module = sys.modules[cls.__module__]
        if not hasattr(module, '_EXECUTOR'):
            # module._EXECUTOR = {}
            module._EXECUTOR = { 'class' : cls.__name__, 'requiresConnection' : requires_connection, 'content-type' : produces }
        else: 
            raise Exception("Only one script executor is allowed to be registered in your module.")
        
        # # map the module name to the executor name.
        # handlers[cls.__module__]={ 'class' : cls.__name__, 'requiresConnection' : requires_connection, 'content-type' : produces }
        return cls
    return wrap

