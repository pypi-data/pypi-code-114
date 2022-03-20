import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
        name = "bibchk",
        version = "0.1.2",
        author = "Doug Keller",
        author_email = "dg.kllr.jr@gmail.com",
        description = "Simple command line program to return the BibTeX string of a given DOI or ISBN.",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "https://github.com/BibTheque/bibchk",
        entry_points={'console_scripts': ['bibchk=bibchk:main']},
        classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
            "Operating System :: OS Independent",
            ],
        package_dir={"": "bibchk"},
        packages=setuptools.find_packages(where="bibchk"),
        python_requires = ">=3.9",
        )
