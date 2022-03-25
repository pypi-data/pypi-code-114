# Author: Snow Yang
# Date  : 2022/03/21

import subprocess
import shutil
import click

from mdev.env import get_env, get_cmake, get_ninja
from mdev import log

@click.command()
@click.argument("project", type=click.Path())
@click.argument("module")
@click.option(
    "--flash",
    "-f",
    type=click.Choice(["APP", "ALL", "None"], case_sensitive=False),
    help="Download firmware to flash after built.",
)
@click.option(
    "--clean",
    "-c",
    is_flag=True,
    help="Rebuild the project.",
)
def build(project: str, module: str, flash: str, clean: bool) -> None:
    """
    Build a MXOS project.

    Arguments:

        PROJECT : Path to the MXOS project

        MODULE  : Module name

    Example:

        $ mdev build demos/helloworld emc3080
    """

    env_path = get_env()
    build_diretory = f'build/{project}-{module}'

    if clean:
        log.dbg(f'Removing {build_diretory} ...')
        shutil.rmtree(build_diretory, ignore_errors=True)

    command = f'{get_cmake()} -B {build_diretory} -GNinja -DAPP={project} -DMODULE={module} -DFLASH={flash} -DMXOS_ENV={env_path}'
    log.dbg(command)
    ret = subprocess.run(command, shell=True)
    if ret.returncode != 0:
        exit(ret.returncode)

    command = f'{get_ninja()} -C {build_diretory}'
    log.dbg(command)
    subprocess.run(command, shell=True)