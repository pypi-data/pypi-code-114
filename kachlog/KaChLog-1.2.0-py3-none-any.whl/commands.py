import click

from ._version import __version__ as v
from .exceptions import ChangelogDoesNotExistError, InvalidSemanticVersion
from .utils import ChangelogUtils


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
        else:
            colored_matches = ", ".join(
                click.style(i, fg="bright_green", bold=True) for i in sorted(matches)
            )
            click.echo(f"Too many command matches. Did you mean: {colored_matches}")
            ctx.abort()

    def resolve_command(self, ctx, args):
        # always return the full command name
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name, cmd, args


def print_version(ctx, _, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(v)
    ctx.exit()


@click.command(
    cls=AliasedGroup,
    epilog="It is possible to call commands in shorter way"
    " eg. `cl add` => changelog added",
)
@click.option(
    "-v",
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
)
def cli() -> None:
    """
    Utility for managing CHANGELOG.md
    """


@cli.command(help="Create CHANGELOG.md with some basic documentation")
@click.option(
    "--sections", "sections", is_flag=True, help="Add empty sections in [Unreleased]"
)
def init(sections: bool = False) -> None:
    click.echo("Initializing Changelog")
    CL = ChangelogUtils()
    outcome = CL.initialize_changelog_file(sections)
    click.echo(outcome)


def bind_section_command(name):
    @click.argument("message")
    def section_command(message: str) -> None:
        CL = ChangelogUtils()
        try:
            CL.update_section(name, message)
        except ChangelogDoesNotExistError:
            if click.confirm("No CHANGELOG.md found, do you want to create one?"):
                CL.initialize_changelog_file()
                CL.update_section(name, message)

    section_command.__name__ = name
    return section_command


for change_type in ChangelogUtils.TYPES_OF_CHANGE:
    section_command_func = bind_section_command(change_type)
    cli.command(
        name=change_type,
        help=f"Add a line to the '{click.style(change_type.capitalize(), fg='red', bold=True)}' section",
    )(section_command_func)


@cli.command(help="cut a release and update the changelog accordingly")
@click.option("--patch", "release_type", flag_value="patch")
@click.option("--minor", "release_type", flag_value="minor")
@click.option("--major", "release_type", flag_value="major")
@click.option("--suggest", "release_type", flag_value="suggest", default=True)
@click.option("--custom", "version", type=str, default=None, help="Force your version")
@click.option("--yes", "auto_confirm", is_flag=True)
@click.option(
    "--sections", "sections", is_flag=True, help="Add empty sections in [Unreleased]"
)
def release(
    release_type: str, auto_confirm: bool, version: str, sections: bool
) -> None:
    CL = ChangelogUtils()
    try:
        if version and release_type != "suggest":
            click.echo("WARNING: custom version precedes release_type flag")
        new_version = version or CL.get_new_release_version(release_type)
        if auto_confirm:
            click.echo(CL.cut_release(new_version, sections))
        else:
            if click.confirm(f"Planning on releasing version {new_version}. Proceed?"):
                click.echo(CL.cut_release(new_version, sections))
    except ChangelogDoesNotExistError:
        if click.confirm("No CHANGELOG.md found, do you want to create one?"):
            CL.initialize_changelog_file()
    except InvalidSemanticVersion as exc:
        click.echo(exc)


@cli.command(
    help="returns the suggested next version based on the current logged changes"
)
@click.option("--type", "release_type", is_flag=True)
def suggest(release_type: str) -> None:
    CL = ChangelogUtils()
    try:
        if release_type:
            click.echo(CL.get_release_suggestion())
        else:
            new_version = CL.get_new_release_version("suggest")
            click.echo(new_version)
    except ChangelogDoesNotExistError:
        pass


@cli.command(help="returns the current application version based on the changelog")
def current() -> None:
    CL = ChangelogUtils()
    try:
        version = CL.get_current_version()
        click.echo(version)
    except ChangelogDoesNotExistError:
        pass


@cli.command(help="view the current and unreleased portion of the changelog")
def view() -> None:
    CL = ChangelogUtils()
    try:
        output = CL.get_changes("unreleased")
        current_version = CL.get_current_version()
        if current_version in CL.data:
            output += CL.get_changes(current_version)
        click.echo(output)
    except ChangelogDoesNotExistError:
        if click.confirm("No CHANGELOG.md found, do you want to create one?"):
            CL.initialize_changelog_file()
