# Author: Snow Yang
# Date  : 2022/03/21

import os
from typing import Union, Any

import click

@click.command()
@click.option(
    "--create-only", 
    "-c", 
    is_flag=True, 
    show_default=True, 
    help="Create a program without fetching mxos."
)
@click.argument("path", type=click.Path(resolve_path=True))
def new(path: str, create_only: bool) -> None:
    """Creates a new MXOS project at the specified path.

    Arguments:

        PATH: Path to the destination directory for the project. Will be created if it does not exist.

    Example:

        $ mdev new helloworld
    """
    # click.echo(f"Creating a new MXOS program at path '{path}'.")
    # if not create_only:
    #     click.echo("Downloading mxos and adding it to the project.")
    click.echo("TBD.")
    
@click.command()
@click.argument("url")
@click.argument("path", type=click.Path(), default="")
@click.option(
    "--skip-resolve-libs",
    "-s",
    is_flag=True,
    show_default=True,
    help="Skip resolving program component dependencies after cloning.",
)
def import_(url: str, path: Any, skip_resolve_libs: bool) -> None:
    """Clone an MXOS project and component dependencies.

    Arguments:

        URL : The git url of the remote project to clone.

        PATH: Destination path for the clone. If not given the destination path is set to the project name in the cwd.

    Example:

        $ mdev import helloworld
    """
    click.echo("TBD.")

@click.command()
@click.argument("path", type=click.Path(), default=os.getcwd())
@click.option(
    "--force",
    "-f",
    is_flag=True,
    show_default=True,
    help="Forces checkout of all component repositories at specified commit in the .component file, overwrites local changes.",
)
def deploy(path: str, force: bool) -> None:
    """Checks out MXOS program component dependencies at the revision specified in the ".component" files.

    Ensures all dependencies are resolved and the versions are synchronised to the version specified in the component
    reference.

    Arguments:
    
        PATH: Path to the MXOS project [default: CWD]

    Example:

        $ mxos deploy
    """
    # click.echo("Checking out all libraries to revisions specified in .component files. Resolving any unresolved libraries.")
    click.echo("TBD.")

@click.command()
@click.argument("path", type=click.Path(), default=os.getcwd())
def sync(path: str, force: bool) -> None:
    """Synchronize component references

    Synchronizes all component and dependency references (.component files) in the current program or component.

    Note that this will remove all invalid component references.

    Arguments:
    
        PATH: Path to the MXOS project [default: CWD]

    Example:

        $ mxos sync
    """
    click.echo("TBD.")
