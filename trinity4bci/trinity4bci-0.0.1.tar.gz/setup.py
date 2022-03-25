from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Operating System :: Unix',
    'License :: OSI Approved',
    'Programming Language :: Python :: 3',
    'Topic :: Adaptive Technologies',
    'Topic :: Scientific/Engineering'
]

setup(
    name='trinity4bci',
    version='0.0.1',
    description='A package for quickly developing and prototyping Neurotechnology projects',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Leonardo Ferrisi',
    author_email='ferrisil@union.edu',
    license='Creative Commons Public License',
    classifiers=classifiers,
    keywords='neurotechnology',
    packages=find_packages(),
    install_requires=['brainflow','zmq','numpy']
)