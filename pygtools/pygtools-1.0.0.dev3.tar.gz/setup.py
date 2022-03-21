from setuptools import setup

with open('README.md', 'r', encoding='UTF-8') as fh:
    readme = fh.read()

description = u'This is a small plugin for pygame, which provides some tools to make creating games with pygame easier. The package is still incomplete as just one module, the screenmanager which makes it easier to create scenes in pygame.'

setup(
    name='pygtools',
    version='1.0.0dev3',
    url='https://github.com/Jefferson5286/PygTools.git',
    license='MIT License',
    author='Jefferson Lima',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='jeffersonlima5286@gmail.com',
    keywords='screen for pygame',
    description=description,
    packages=['pygtools'],
    install_requires=['pygame'],
)
