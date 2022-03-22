import click, os

@click.command()
@click.argument('name', required=True)
def prepack(name):
    os.system(f'mkdir {name}_package; cd {name}_package; mkdir {name}')
    with open(f'{name}_package/setup.py', 'w') as set:
        set.write(f'from setuptools import setup\n\nsetup(\n    name=\'{name}\',\n    author=\'\',\n    version=\'0.0.0\',\n    packages=[\'{name}\'],\n    entry_points=\'\'\'\'\'\'\n)')

    with open(f'{name}_package/{name}/__init__.py', 'w') as ini:
        ini.write(f'from .{name} import *')

    with open(f'{name}_package/{name}/{name}.py', 'w') as file:
        file.write('')

@click.command()
def build():
    os.system('pip install .')
    try:
        os.system('python setup.py sdist bdist_wheel')
    except:
        os.system('python3 setup.py sdist bdist_wheel')

@click.command()
def pypi():
    try:
        os.system('python -m twine upload dist/*')
    except:
        os.system('python3 -m twine upload dist/*')