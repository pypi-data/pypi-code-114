# """Build python modules/plugins from source files. """

# import importlib
# from pathlib import Path
# import importlib.resources
# from importlib.resources import files, as_file
# from . import templates


# def get_template_dir(name: str) -> Path:
#     """Get the path of the template dir by name."""

#     templates_root_dir = importlib.resources.files("abies.builder.templates")
#     template_dir = templates_root_dir.joinpath(name)

#     if template_dir.is_dir():
#         print(template_dir)
#     return template_dir

#     # return importlib.resources.contents(templates)
#     # source = files(templates)
#     # with as_file(source) as s:
#     #     print(s)
#     # return source


# def create_from_template():
#     """"""
