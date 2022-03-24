import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="basicplaycard",
    version="0.0.2",
    author="Chris Chankyo Kim",
    author_email="chankyo@stanford.edu",
    description="A simple abstraction class for playing cards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kimchankyo/BasicPlayingCard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)