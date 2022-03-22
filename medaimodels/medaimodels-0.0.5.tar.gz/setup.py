import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="medaimodels",
    version="0.0.5",
    description="A libarary for creating med-ai models",
    long_description=README,
    long_description_content_type="text/markdown",
    author=["Travis Clarke","Jacob Clarke"],
    author_email="travisjonathanclarke@gmail.com",
    license="Apache-1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pylint", "sphinx", "scikit-image"]
)
