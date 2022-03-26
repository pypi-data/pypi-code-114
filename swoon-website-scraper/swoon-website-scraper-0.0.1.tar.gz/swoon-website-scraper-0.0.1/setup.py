from setuptools import setup
from setuptools import find_packages

setup(
    name="swoon-website-scraper",
    version="0.0.1",
    description="A webscraper for the swoon wesite",
    long_description="",
    url="",
    author="Barney Morgan",
    license="MIT",
    packages=find_packages(),
    install_requires=["webdriver_manager", "selenium"]
)
