from ._{{cookiecutter.module_name}} import register_with, framework_version

__version__ = "{{cookiecutter.version}}"

__all__ = [
    "framework_version",
    "register_with",
]
