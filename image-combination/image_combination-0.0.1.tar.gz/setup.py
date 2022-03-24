from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="image_combination",
    version="0.0.1",
    author="Everton Vaz",
    author_email="etovaz.web@gmail.com",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url='https://github.com/EvertonVaz/bootcamps/tree/main/cognizant/IMAGE_PROCESSING-PACKAGE',
    packages=find_packages(),
    install_requirements=requirements
)
