import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument()
@click.option()
def cli():
    """
    The Command Line Interface.
    """
    pass
    
