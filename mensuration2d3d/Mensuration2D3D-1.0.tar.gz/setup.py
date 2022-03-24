from setuptools import setup, find_packages

setup(
    name = 'Mensuration2D3D',
    version = '1.0',
    author = 'Sifar',
    author_email = 'cnn.gtm.hero@gmail.com',
    description = 'A mensuration package to calculate the area, perimeter, volume, etc. of various 2D (Square, Rectangle, etc.) & 3D (Cube, Cuboid, etc.) shapes.',
    long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    url = '',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'],
    keywords = ['mensuration', 'area', 'perimeter', 'volume', 'total surface area', 'curved surface area', 'slant height'],
    packages = find_packages(),
    install_requires=['']
)