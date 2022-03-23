from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='c_out',
    description='Colored Output - c_out. Python print with a style!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.2',
    license='GPL-3.0',
    author="Gautam Rajeev Singh",
    author_email='gautamsingh1997@gmail.com',
    url='https://github.com/singhgautam7/Python-GoldMine/tree/master/color_print',
    keywords='pyton print color styles',
    install_requires=[],
)
