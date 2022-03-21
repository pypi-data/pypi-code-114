import click

@click.group(name='example')
def cli():
    pass

@cli.command()
def foo():
    print('hello foo')

@cli.command()
def bar():
    print('hello bar')

if __name__ == '__main__':
    cli()