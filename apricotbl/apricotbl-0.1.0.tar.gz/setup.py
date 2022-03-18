from setuptools import setup, find_packages

setup(
    name='apricotbl',
    version='0.1.0',
    license='GPL',
    author="Ali Can Canbay",
    author_email='ali.c.canbay@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/lcnby/apricot',
    keywords=['apricot', 'particle', 'tracking', 'beamline'],
    install_requires=[
          'numpy', 'scipy', 'matplotlib'
      ],
)