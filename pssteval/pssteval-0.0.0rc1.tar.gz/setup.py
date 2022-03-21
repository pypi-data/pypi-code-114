import setuptools

setuptools.setup(
    name='pssteval',
    version='0.0.0rc1',
    author='Robert Gale',
    author_email='galer@ohsu.edu',
    packages=['pssteval'],
    url='https://github.com/PSST-Challenge/pssteval',
    description='',
    install_requires=[
        'phonologic==0.0.0rc3',
        'psstdata',
        'regex',
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'pssteval-asr = pssteval.asr:main',
            'pssteval-correctness = pssteval.correctness:main',
            'pssteval-viewer = pssteval.viewer:main',
        ],
    },
    include_package_data=True,
    package_data={
        'phonologic': [
            '**/*.py',
            '**/*.txt',
            '**/*.json',
        ]
    },

)
