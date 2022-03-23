"""
https://packaging.python.org/en/latest/tutorials/packaging-projects/
Markdown guide: https://www.markdownguide.org/cheat-sheet/
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="earthquake-IDN",
    version="0.4",
    author="Muhammad Shaufi Imanulhaq",
    author_email="imanshaufi14@gmail.com",
    description="This package will scrape data from [BMKG](https://www.bmkg.go.id) to get the latest quake happened "
                "in Indonesia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/student-of-remoteworkerid/latest-indonesia-earthquake",
    project_urls={
        "Website": "https://remoteworker.id",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
