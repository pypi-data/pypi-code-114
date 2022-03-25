from setuptools import setup, find_packages

setup(
    name='FeaSel-Net',
    version='0.0.1',
    license='MIT',
    author="Felix Fischer",
    author_email='felix.fischer@ito.uni-stuttgart.de',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.tik.uni-stuttgart.de/FelixFischer/FeaSel-Net',
    keywords=['feature selection', 'neural networks', 'machine learning'],
    install_requires=[
          'tensorflow',
	  'keras',
	  'numpy',
      ],

)