# following this
# https://medium.com/@thucnc/how-to-publish-your-own-python-package-to-pypi-4318868210f9

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='vennsketch',
    version='0.1.0',
    description='Tool for creating a small sketch that can be ' \
                'used to check the intersection between sets in a time saving and ' \
                'secure way',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    author='David Johnston',
    author_email='dave31415@gmail.com',
    keywords=['machine learning'],
    url='https://github.com/dave31415/vennsketch',
    download_url='https://pypi.org/project/vennsketch/'
)

install_requires = []

if __name__ == '__main__':
    setup(install_requires=install_requires, **setup_args)
