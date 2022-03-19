from dscreate import apps, pipeline
import inspect
import os
from types import FunctionType
from dscreate import apps, pipeline

def create_class_docs(dsobject):
    name = dsobject.__name__
    description = dsobject.description
    configs = dsobject.class_config_rst_doc()
    
    doc = f'''{name}\n----------------------------\n\n{description}\n\n**CONFIGURABLE VARIABLES:**\n\n{configs}'''
                      
                      
    return doc

def create_method_docs(dsobject):
    name = dsobject.__name__
    args = str(inspect.signature(dsobject))
    doc = dsobject.__doc__
    if not doc:
        doc = 'No description'
    
    return f".. admonition:: {name}{args}:\n\n   {doc}\n\n"
    

def create_dsobject_docs():
    modules = {apps: apps.__all__,
              pipeline: pipeline.__all__}
    
    docs = 'Code Documentation\n=================='
    group = None
    for module in modules:
        objects = modules[module]
        for obj_name in objects:
            obj = getattr(module, obj_name)
            obj_group = obj.__module__.split('.')[-2]
            if obj_group != group:
                group = obj_group
                docs += f'\n--------------\n{group.title()}\n--------------\n\n'
            obj_docs = create_class_docs(obj)
            docs += obj_docs
            docs += '\n\n**METHODS**\n\n'
            methods = []
            for key in obj.__dict__:
                if type(obj.__dict__[key]) == FunctionType:
                    methods.append(obj.__dict__[key])
            for method in methods:
                docs += create_method_docs(method)
    return docs

if __name__ == '__main__':
    docs  = create_dsobject_docs()
    doc_path = os.path.join('source', 'pages', 'code_documentation.rst')
    file = open(doc_path, 'w+')
    file.write(docs)
    file.close()

    config_options = apps.DsCreate().document_config_options()
    doc_path = os.path.join('source', 'pages', 'config_options.rst')
    file = open(doc_path, 'w+')
    file.write(config_options)
    file.close()


