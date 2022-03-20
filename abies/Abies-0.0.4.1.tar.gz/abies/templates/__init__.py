import dataclasses
from pathlib import Path
import importlib.resources
from dataclasses import dataclass
from cookiecutter.main import cookiecutter

from dataclasses import fields


@dataclass
class TemplateConfig:
    """Configuration parameters for templates."""

    module_name: str
    version: str = "1.0.0"


def template_dir(name: str) -> str:
    """Get the directory of a specific template"""
    template_subdir = importlib.resources.files("abies.templates") / name

    return Path(template_subdir).as_posix()


def create_from_template(template: str, config: TemplateConfig = None):
    """Create a project from a config. If no config is given, it will prompt the user."""
    tdir = template_dir(template)
    if config is None:
        cookiecutter(tdir)
    else:
        cookiecutter(tdir, extra_context=dataclasses.asdict(config), no_input=True)
