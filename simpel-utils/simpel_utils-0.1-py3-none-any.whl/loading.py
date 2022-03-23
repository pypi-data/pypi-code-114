from importlib import import_module

from django.apps import apps
from django.utils.module_loading import module_has_submodule


def extract_contenttype(contenttype_format):
    contenttype_id, app_name, model_name = contenttype_format.split(".")
    result = dict()
    result["model_name"] = model_name
    result["contenttype_model"] = apps.get_model(app_name, model_name)
    result["contenttype_slug"] = ".".join([app_name, model_name])
    result["contenttype_id"] = contenttype_id
    result["app_name"] = app_name
    return result


def get_app_modules():
    """
    Generator function that yields a module object for each installed app
    yields tuples of (app_name, module)
    """
    for app in apps.get_app_configs():
        yield app.name, app.module


def get_app_submodules(submodule_name):
    """
    Searches each app module for the specified submodule
    yields tuples of (app_name, module)
    """
    for name, module in get_app_modules():
        if module_has_submodule(module, submodule_name):
            yield name, import_module("%s.%s" % (name, submodule_name))
