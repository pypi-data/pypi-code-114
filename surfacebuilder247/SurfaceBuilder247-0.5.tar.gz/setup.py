from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='SurfaceBuilder247',
      version='0.5',
      description='Surface Builder 24/7',
      packages=['SurfaceBuilder247'],
      author_email='geodata@soton.ac.uk',
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)
