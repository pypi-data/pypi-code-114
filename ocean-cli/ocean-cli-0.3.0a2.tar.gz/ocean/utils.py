import json
import subprocess
import sys
from enum import Enum
from types import SimpleNamespace

import click
import requests
from dateutil.parser import parse
from pyfiglet import Figlet
from ocean import code


class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx) if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail(f"Too many matches: {', '.join(sorted(matches))}")

    def resolve_command(self, ctx, args):
        # always return the full command name
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name, cmd, args


class NotRequiredIf(click.Option):
    def __init__(self, *args, **kwargs):
        self.not_required_if = kwargs.pop("not_required_if")
        assert self.not_required_if, "'not_required_if' parameter required"
        kwargs["help"] = (
            kwargs.get("help", "")
            + " NOTE: This argument is mutually exclusive with %s"
            % self.not_required_if
        ).strip()
        super(NotRequiredIf, self).__init__(*args, **kwargs)

    def handle_parse_result(self, ctx, opts, args):
        we_are_present = self.name in opts
        other_present = self.not_required_if in opts and opts[self.not_required_if]

        if other_present:
            if we_are_present:
                raise click.UsageError(
                    "Illegal usage: `%s` is mutually exclusive with `%s`"
                    % (self.name, self.not_required_if)
                )
            else:
                self.prompt = None

        return super(NotRequiredIf, self).handle_parse_result(ctx, opts, args)


class JSONObjects(SimpleNamespace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            if isinstance(value, dict):
                self.__setattr__(key, JSONObjects(value))
            elif isinstance(value, list):
                self.__setattr__(
                    key,
                    [
                        JSONObjects(v)
                        if isinstance(v, dict)
                        else JSONObjects()
                        if v is None
                        else v
                        for v in value
                    ],
                )
            elif value is None:
                self.__setattr__(key, JSONObjects())
            else:
                self.__setattr__(key, value)

    def __getattribute__(self, value):
        try:
            return super().__getattribute__(value)
        except AttributeError:
            return ""

    def __str__(self) -> str:
        if self.__dict__ == {}:
            return ""
        return super().__str__()

    def __format__(self, format):
        return str(self).__format__(format)


def dict_to_namespace(dictionary):
    return json.loads(
        json.dumps(dictionary), object_hook=lambda item: JSONObjects(**item)
    )


def convert_time(time_str):
    if time_str:
        date = parse(time_str)
        # date = date.replace(tzinfo=None)
        return date


def date_format(date, second=False):
    format = "%y-%m-%d %H:%M"
    if second:
        format += ":%S"

    if date:
        return date.strftime(format)


def api_health_check(url):
    try:
        res = requests.get(url + "/api/healthz")
        if res.status_code != 404:
            raise ValueError()

    except (requests.exceptions.ConnectionError, ValueError):
        sprint(
            f"Server is not responding. Please check url({url}) is correct.",
            PrintType.FAILED,
        )
        sprint("\n\tSetup `url` with `ocean init --url <url>`.")
        return False

    return True


class PrintType(Enum):
    NORMAL = 0
    SUCCESS = 1
    FAILED = 2
    WORNING = 3


def sprint(msg="", type=PrintType.NORMAL, nl=True):
    if type == PrintType.NORMAL:
        click.echo(msg, nl=nl)
    elif type == PrintType.SUCCESS:
        click.secho("\u2713" + f" {msg}", fg="green", bold=True, nl=nl)
    elif type == PrintType.FAILED:
        click.secho("\u2717" + f" {msg}", fg="red", bold=True, nl=nl)
    elif type == PrintType.WORNING:
        click.secho("\u26A0" + f" {msg}", fg="yellow", bold=True, nl=nl)


def version_check():
    name = "ocean-cli"
    latest_version = str(
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "{}==random".format(name)],
            capture_output=True,
            text=True,
        )
    )
    latest_version = latest_version[latest_version.find("(from versions:") + 15 :]
    latest_version = latest_version[: latest_version.find(")")]
    latest_version = latest_version.replace(" ", "").split(",")[-1]

    # current_version = str(
    #     subprocess.run(
    #         [sys.executable, "-m", "pip", "show", "{}".format(name)],
    #         capture_output=True,
    #         text=True,
    #     )
    # )
    # current_version = current_version[current_version.find("Version:") + 8 :]
    # current_version = current_version[: current_version.find("\\n")].replace(" ", "")
    current_version = code.VERSION

    if latest_version == current_version:
        return True, latest_version, current_version
    else:
        return False, latest_version, current_version


def print_ocean_logo():
    f = Figlet(font="slant")
    print(f.renderText("Ocean"))
