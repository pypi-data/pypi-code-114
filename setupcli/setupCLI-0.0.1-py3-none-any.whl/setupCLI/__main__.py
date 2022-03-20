from colored import stylize, fg
import click

def color_print(text):
    color = "green"
    colored_text = stylize(text, fg(color))
    click.echo(colored_text)

@click.group()
def setupCLI():
    '''
    Initialise the setupCLI
    '''
    pass

@click.command(name="project")
@click.argument("name")
def project(name):
    '''
    command for initialising project
    '''
    color_print(name)

setupCLI.add_command(project)