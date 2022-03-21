import click
import os

from ocean import api, code, utils
from ocean.main import pass_env
from ocean.utils import sprint, PrintType


@click.command()
@click.argument("name")
@pass_env
def cli(ctx, name):
    host = ctx.get_url().split("/")[-1].split(":")[0]
    port = None

    res = api.get(ctx, code.API_INSTANCE)
    body = utils.dict_to_namespace(res.json())

    for inst in body.pods:
        if inst.name == name:
            port = inst.nodePort
            break
    else:
        sprint(f"Instance `{name}` is not found.", PrintType.FAILED)
        return

    cmd = f"ssh root@{host} -p {port}"

    sprint(f"Attach to `{name}` instance via `{cmd}`.", PrintType.SUCCESS)
    os.system(cmd)
