import setuptools

with open("Readme.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ArtCollection',
    version='0.0.2',
    description='Metropolian MuseumAPI objects which converts in json form and then json to html,xml,csv formats and '
                'html to pdf',
    author='Affan',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),

    keywords=['ArtCollection', 'Metropolian Art Collection', 'Art Collection API'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    py_modules=['ArtCollection'],
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'requests',
        'flatten_json',
        'pdfkit',
        'lxml'
    ]

)
