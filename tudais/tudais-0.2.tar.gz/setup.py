""" Setup script for tudais """

from setuptools import setup

setup(name='tudais',
      version='0.2',
      description='Supplemental material for the lecture Angewandte '
                  'Intelligente Signalverarbeitung at TU Dresden',
      url='http://github.com/TUD-STKS/tud-ais-package',
      author='Simon Stone',
      author_email='simon.stone@tu-dresden.de',
      license='MIT',
      packages=['tudais'],
      include_package_data=True,
      install_requires=[
          'jupyterlab',
          'pandas',
          'scikit-learn',
          'tudthemes'
      ],
      entry_points={
          'console_scripts': [
              'tud-ais-start = tudais.__main__:start_jupyter_server',
              'tud-ais-prepare-submission = tudais.__main__:prepare_submission'
          ]
      }
      )
