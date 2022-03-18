import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Patch-Drive-Simulator-cbutler112358",
    version="0.0.1",
    author="Cole Butler",
    author_email="cbutler5@ncsu.edu",
    description="A spatially explicit, patch-based gene drive simulator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cbutler112358/course-projects-w2022",
    project_urls={
        "Patch Drive Simulator": "https://github.com/cbutler112358/course-projects-w2022",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # package_dir={"": "src"},
    packages=setuptools.find_packages(where="patch_drive_simulator"),
    python_requires=">=3.6",
)