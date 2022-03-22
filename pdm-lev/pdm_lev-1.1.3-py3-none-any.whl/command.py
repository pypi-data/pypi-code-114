import hashlib
import json
import pathlib
import re
from argparse import ArgumentParser, Namespace

import click
import httpx
from pdm import termui
from pdm.cli import actions
from pdm.cli.commands.base import BaseCommand
from pdm.cli.options import verbose_option
from pdm.project.core import Project
from pdm.utils import get_user_email_from_git

PYTHON_VERSION = "3.10"

GITIGNORE = """\
**/__pycache__/
__pypackages__/
build/
dist/

.pdm.toml

.DS_Store
"""

PYPROJECT = {
    "project": {
        "version": "0.1.0",
        "description": "",
        "license": {
            "text": "MIT"
        },
        "requires-python": ">=" + PYTHON_VERSION,
        "dynamic": ["classifiers"],
    },
    "build-system": {
        "requires": ["pdm-pep517"],
        "build-backend": "pdm.pep517.api"
    },
    "tool": {
        "pdm": {
            "editable-backend":
            "path",
            "source": [{
                "name":
                "levhub",
                "url":
                "https://__key__:${LEVHUB_KEY}@pypi.lev.zone/simple/"
            }],
            "includes": ["lev"]
        }
    }
}

ERROR = click.style("error:", fg="red", bold=True)


class Command(BaseCommand):

    name = "lev"
    arguments = [verbose_option]

    def add_arguments(self, parser: ArgumentParser) -> None:
        subparsers = parser.add_subparsers(title="Sub commands")
        NewCommand.register_to(subparsers)
        CheckCommand.register_to(subparsers)
        UploadCommand.register_to(subparsers)
        parser.set_defaults(search_parent=False)
        self.parser = parser

    def handle(self, project: Project, options: Namespace) -> None:
        self.parser.print_help()


def check_fullname(fullname):
    try:
        space, name = fullname.split(".", 1)
    except ValueError:
        raise Exception("namespace needed <namespace>.<module_name>")

    if not re.match(r"[a-zA-Z]\w*$", name):
        error = f"invalid name `{name}`, the first character must be a letter, only contain letters number or `_`"
        raise Exception(error)

    return space, name


class NewCommand(BaseCommand):

    name = "new"

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument("name", help="Specify the project name")

    def handle(self, project: Project, options: Namespace) -> None:
        ui = project.core.ui

        try:
            space, name = check_fullname(options.name)
        except Exception as e:
            ui.echo(f"{ERROR} {e}", err=True)
            return

        project.root = pathlib.Path(options.name)
        if project.root.exists():
            error = f"{ERROR} destination `{project.root.resolve()}` already exists"
            ui.echo(error, err=True)
            return

        actions.do_use(project, PYTHON_VERSION)

        author, email = get_user_email_from_git()
        PYPROJECT["project"]["name"] = "lev." + options.name
        PYPROJECT["project"]["authors"] = [{"name": author, "email": email}]
        project._pyproject = PYPROJECT
        project.write_pyproject()

        with open(project.root / ".gitignore", "w") as f:
            f.write(GITIGNORE)


class CheckCommand(BaseCommand):

    name = "check"

    def handle(self, project: Project, options: Namespace) -> None:
        meta = project.meta
        ui = project.core.ui
        assert meta.name

        if not meta.name.startswith("lev."):
            ui.echo(f"{ERROR} project name should starts with `lev.`")
            return

        try:
            space, name = check_fullname(meta.name[4:])
        except Exception as e:
            ui.echo(f"{ERROR} {e}", err=True)
            return

        from .parser import parse
        meta = parse(project)
        print(json.dumps(meta, ensure_ascii=False))


class UploadCommand(BaseCommand):

    name = "upload"

    def handle(self, project: Project, options: Namespace) -> None:
        meta = project.meta
        ui = project.core.ui

        try:
            sources = filter(lambda s: s["name"] == "levhub", project.sources)
            url = httpx.URL(next(sources)["url"])
        except:
            ui.echo(f"{ERROR} levhub source url not set")
            return

        if not url.password or url.password.startswith("${"):
            ui.echo(f"{ERROR} levhub credentials needed")
            return

        try:
            assert meta.name
            lev, space, name = meta.name.split('.')
            assert lev == "lev"
        except:
            ui.echo(f"{ERROR} Invalid project name")
            return

        from .parser import parse
        release_meta = parse(project)

        from pdm.builders.wheel import WheelBuilder
        with ui.open_spinner(f"Building wheel...") as spin:
            dist = str(project.root / "dist")
            loc = WheelBuilder(project.root, project.environment).build(dist)
            spin.succeed(f"Built wheel at `{loc}`")

        with open(loc, "rb") as f:
            sha256 = hashlib.sha256(f.read()).hexdigest()

        data = {
            "id": {
                "space": space,
                "name": name
            },
            "release": {
                "version": meta.version,
                "sha256": sha256,
                "meta": release_meta
            }
        }

        def show_resp(resp: httpx.Response):
            phrase = resp.reason_phrase
            ui.echo(termui.red(f"{resp.status_code} {phrase}"), err=True)
            ui.echo(resp.text, err=True)

        resp = httpx.post(url, json=data)
        if not resp.is_success:
            ui.echo("Create release failed", err=True)
            show_resp(resp)
            return

        with ui.open_spinner("Uploading...") as spin:
            with open(loc, "rb") as f:
                resp = httpx.put(resp.json()["url"], content=f)
            if not resp.is_success:
                spin.fail("Upload failed")
                show_resp(resp)
                return

            spin.succeed("Upload successful")
