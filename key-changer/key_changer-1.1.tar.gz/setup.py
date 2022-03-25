from setuptools import setup,find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='key_changer',
      version='1.1',
      description="change keyboard character",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/keegang6705/en-th-keyboard-translator',
      author='keegang_6705',
      author_email='darunphobwi@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires= [''],
      python_requires='>=3.0',
      zip_safe=False)