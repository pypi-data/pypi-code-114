
from .IExecuteScripts import IExecuteScripts

handlers={}

def Register(requires_connection:bool, produces:str):
    """
    Registers a class as a script executor. The class must implement IExecuteScripts.

    Note: only one IExecuteScripts class in your script can be registered.

    requires_connection - indicates that your script handler expects a Connector Connection Id.
    
    produces - indicates the mime type that the script handler produces.
    """
    def wrap(cls):
        if handlers.get(cls.__module__):
            raise Exception("A script executor was already registered in your module.")

        if not issubclass(cls, IExecuteScripts):
            raise Exception("'{name}' does not implement IExecuteScripts interface.".format(name=cls.__name__))
        
        # map the module name to the executor name.
        handlers[cls.__module__]={ 'class' : cls.__name__, 'requiresConnection' : requires_connection, 'content-type' : produces }
        return cls
    return wrap

# this works because the app handler is registered upon definition-time/import,
# not runtime. otherwise, it would not.
# class App:
#     handler:IExecuteScripts = None
#     def Handler(cls):
#         """
#         Decorates a class as function executor. Only 1 executor is allowed.
#         """
#         if App.handler != None:
#             raise Exception("Only 1 Handler can be registered.")

#         App.handler = cls
#         #App.handlers.append(cls.__name__)
#         return cls

# not sure how exactly to make thhis stateful with a class
# class Handler:
#     def __init__(self):
#         self.handler:IExecuteScripts = None

#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         pass
#     """
#     Decorates a class as function executor. Only 1 executor is allowed.
#     """
#     def Handler(self):
#         print("in handler")
#         def decorator(cls):
#             if self.handler != None:
#                 raise Exception("Only 1 Handler can be registered.")
#             print(cls.__name__)
#             self.handler = cls
#             return cls
#         #App.handlers.append(cls.__name__)
#         return decorator

