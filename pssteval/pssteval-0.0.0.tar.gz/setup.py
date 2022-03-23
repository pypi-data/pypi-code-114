import setuptools

setuptools.setup(
    name='pssteval',
    version='0.0.0',
    author='Portland Allied Labs for Aphasia Technology (PALAT)',
    author_email='galer@ohsu.edu',
    packages=['pssteval'],
    url='https://github.com/PSST-Challenge/pssteval',
    description='',
    install_requires=[
        'phonologic',
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
        'pssteval': [
            '**/*.py',
            '**/*.html',
            '**/*.css',
            '**/*.js',
            'web/components/*.js',
        ],
        'pssteval.web': [
            '**/*.js',
        ],
        'pssteval.web.components': [
            '**/*.js',
        ],
    },
)
