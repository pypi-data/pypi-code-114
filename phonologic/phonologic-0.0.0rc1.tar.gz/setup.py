import setuptools

setuptools.setup(
    name='phonologic',
    version='0.0.0pre1',
    author='Robert Gale',
    author_email='galer@ohsu.edu',
    packages=[
        'phonologic'
    ],
    url='https://github.com/rcgale/phonologic',
    description='',
    install_requires=[
        ""
    ],
    package_data={'phonologic': ['*.txt']},
    include_package_data=True,
)

