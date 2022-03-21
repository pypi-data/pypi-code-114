import setuptools


setuptools.setup(
    name="igi_file_transformation_contract",
    version="0.0.7",
    author="IGI",
    author_email="chris.prosser@igiltd.com",
    description="Interface and helpers for file transformations.",
    long_description="Specifies methods and properties required to implement a standard IGI file transformation service.",
    long_description_content_type="text/markdown",
    url="https://github.com/IGILtd/data_transformation_scripts/tree/master/import_file_formats/gc",
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Pre-processors",
        "Topic :: Text Processing",
        "Typing :: Typed",
    ],
    python_requires='>=3.7',
    packages=['igi_file_transformation_contract'],
    install_requires=[]
)
