from setuptools import setup, find_packages

setup(
    name="simonzhaoms",
    version="0.0.2",
    author="Simon Zhao",
    author_email="simonyansenzhao@gmail.com",
    description="Simon's toy Python package",
    package_dir={"": "simonzhaoms"},
    packages=find_packages(where="simonzhaoms"),
)
