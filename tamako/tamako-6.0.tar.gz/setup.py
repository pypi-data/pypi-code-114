from distutils.core import setup
with open("README.rst", "r") as f:
  long_description = f.read()

setup(
        name='tamako',
        version='6.0',
        description='张力元',
        long_description=long_description,
        author='tamako',
        author_email='2415075961@qq.com',
        py_modules=['debug.print']
)

