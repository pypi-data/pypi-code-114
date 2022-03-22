from setuptools import setup, find_packages


setup(
    name='convbaspy',
    version='1.0.1',
    license='MIT',
    author="D Penilla",
    author_email='dpenillac@correo.usbcali.edu.co',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/etensor/baseconvpy',
    keywords='convertidor de bases',
    install_requires=[
          'rich',
          'textual',
          'pyfiglet',
          'pyperclip'
      ],

)
