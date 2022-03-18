"""
The setup file. To install as a developer (only do this in a venv):

python setup.py develop

Otherwise, just:

python setup.py install
"""

from setuptools import setup

setup(name='local_stats',
      version='0.0.1',
      license='MIT License',
      description='A python package for using local statistics to cluster " + \
          "significant signal in scientific images.',
      author='Richard Brearton',
      author_email='richardbrearton@gmail.com',
      package_dir={'': 'src'},
      include_package_data=True,
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: Implementation :: CPython',
      ],
      # The bare minimum for installation.
      install_requires=["pillow >= 9.0.1",
                        "scipy >= 1.8.0",
                        "scikit-learn >= 1.0.2",
                        "pywavelets >= 1.3.0"]
      )
