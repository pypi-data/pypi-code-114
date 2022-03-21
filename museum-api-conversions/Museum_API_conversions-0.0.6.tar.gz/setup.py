import setuptools

with open("Readme.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Museum_API_conversions',
    version='0.0.6',
    description='Museum_API objects which converts in json form and then json to pdf,html,xml,csv formats',
    author='Affan',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),

    keywords=['API conversion', 'python API conversions', 'Museum_API_conversions'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    py_modules=['Museum_API_conversions'],
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'requests',
        'flatten_json',
        'pdfkit',
        'lxml'
    ]

)
