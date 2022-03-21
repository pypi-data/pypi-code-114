import click

@click.group(name='example')
def cli():
    """This is an example OPS plugin."""
    pass

@cli.command()
def foo():
    """This is an example 'foo' command."""
    click.secho('hello foo', fg='green', bold=True)

@cli.command()
def bar():
    """This is an example 'bar' command."""
    click.secho('hello bar', fg='green', bold=True)

if __name__ == '__main__':
    cli()