from distutils.core import setup
with open("README.rst", "r") as f:
  long_description = f.read()

setup(
        name='Tamako',
        version='8.8',
        description='张力元 Only one',
        long_description=long_description,
        author='Tamako',
        author_email='2415075961@qq.com',
        py_modules=['debug.print']
)

