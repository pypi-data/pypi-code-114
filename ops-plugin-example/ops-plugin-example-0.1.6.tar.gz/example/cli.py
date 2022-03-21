import click

@click.group(name='example')
def cli():
    """This is an example OPS plugin."""
    pass

@cli.command()
@click.option('--name', help="Your name", required=True)
def hello(name):
    """This is an example 'hello' command."""
    click.secho(f'Hello {name}! 👋', fg='green', bold=True)


if __name__ == '__main__':
    cli()
