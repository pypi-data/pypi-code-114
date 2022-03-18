"""
Packaging Python Projects: https://packaging.python.org/en/latest/tutorials/packaging-projects/
markdown guide: https://www.markdownguide.org/cheat-sheet/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Earthquakedetection",
    version="0.0.3",
    author="wahyukmr",
    author_email="maryu9292@gmail.com",
    description="This package will detect the latest earthquakes from BMKG (Meteorology, Climatology, and "
                "Geophysical Agency)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wahyukmr/Earthquake-detection",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Framework :: Scrapy",
        "Development Status :: 5 - Production/Stable"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
