import click

import loci_checkmarx.utils as lcu
from loci_checkmarx.run import run
from loci_checkmarx.summary import summary


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    lcu.print_version()
    ctx.exit()


@click.group()
@click.option("-v", "--version", is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def loci_checkmarx():
    pass


loci_checkmarx.add_command(run)
loci_checkmarx.add_command(summary)


if __name__ == "__main__":
    loci_checkmarx()
