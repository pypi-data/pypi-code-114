from setuptools import setup, find_packages


name = u'dscreate'
version = '0.2.0'
description = 'Flatiron Iron School Data Science Tools'
setup_args = dict(
    name=name,
    version=version,
    description=description,
    author='Joel Collins',
    author_email='joelsewhere@gmail.com',
    license='MIT',
    url='http://github.com/learn-co-curriculum/dscreate',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['ds=dscreate.apps.DsCreateApp:main']
    },
install_requires=['argparse==1.1', 
                 'pyperclip==1.8.2', 
                 'traitlets==5.1.0', 
                  'nbgrader==0.6.1', 
                  'nbformat==5.1.3', 
                  'nbconvert==6.2.0', 
                  'GitPython==3.1.24',
                  'appdirs==1.4.4'],
)

if __name__ == "__main__":
    setup(**setup_args)