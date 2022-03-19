from setuptools import setup

setup(
    name='no_init',
    version='v0.1.3',
    description='tool that checks that there are no __init__.py in your modules (or they are empty)',
    long_description_content_type="text/markdown",
    url='https://github.com/tandav/no_init',
    # packages=find_packages(),
    py_modules=['no_init'],
    include_package_data=True,
)
