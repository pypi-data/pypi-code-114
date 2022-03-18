from distutils.core import setup

setup(
  name='featureOfPPGsignal',
  packages = ['featureOfPPGsignal'],
  version='v0.0.1',
  license='MIT',
  description='extract features of the photoplethysmographic signal',
  author='Nikoleta Dimitra Bena',
  author_email='nd_bena@hotmail.com',
  url='https://github.com/NikoletaMpena/featurePPGsignal.git',
  download_url='https://github.com/NikoletaMpena/featurePPGsignal/archive/refs/tags/v0.0.1.tar.gz',
  keywords=['PPG', 'features'],
  install_requires=[
          'numpy',
          'scipy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
  ],
)
