import click

from freedomrobotics_api.cli.commands.setup import setup


@click.group()
@click.version_option(version='1.0.0', prog_name='Freedom CLI')
def cli(args=None):
    pass


cli.add_command(setup)

if __name__ == '__main__':
    cli()
