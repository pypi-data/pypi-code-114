"""Provide templating capability."""

# import os
from typing import TYPE_CHECKING, Any, Dict

from invoke import task
from jinja2 import Environment, FileSystemLoader

if TYPE_CHECKING:
    from invoke import Context


@task
def render(
    ctx, data, template_name
):  # type: (Context, Dict[str, Any], str) -> str
    """Render template."""
    loader = FileSystemLoader(ctx.templates_dir)
    env = Environment(loader=loader, autoescape=True)
    template = env.get_template(f"{template_name}.j2")
    content = template.render(**data)
    return content
