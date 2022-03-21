import os
import inspect

def getpath():
        print(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))