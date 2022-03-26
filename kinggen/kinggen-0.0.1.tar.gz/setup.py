from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
]

setup(
    name='kinggen',
    version='0.0.1',
    description='Kinggen wrapper in python',
    long_description= 'KingGen is a wrapper of KingGen in Python',
    url='',
    author='yeeter',
    license='MIT',
    classifiers=classifiers,
    keywords='kinggen',
    packages=find_packages(),
    install_requires=['requests'],
)