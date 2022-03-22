import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='algoritmika_quiz_package',
    version='0.0.1',
    author='Buynichenko Mikhail',
    description="My unique package with unique functionality, which wasn't on https://pypi.org/",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    py_modules=['algoritmika_quiz_package'],
    install_requires=[
    ]
)
