from distutils.core import setup

setup(
    name = 'snowiest',
    version = '1.2.0',
    py_modules=['snowiest'],
    author='SnowyFu',
    author_email='fuxingxue@hotmail.com',
    url='https://github.com/pypa/sampleproject',
    package_dir={'snowiest': 'snowiest'},
    package_data={'snowiest': ['*.*', 'snowiest/*']},
)