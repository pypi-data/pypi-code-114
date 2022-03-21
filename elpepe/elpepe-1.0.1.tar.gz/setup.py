import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='elpepe',
    version="1.0.0",
    author="Mathyslol",
    description="el pepe",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    url="https://mathyslolbot.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'BenBotAsync',
        'FortniteAPIAsync',
        'aiohttp',
        'colorama',
        'crayons',
        'fortnitepy',
        'requests',
        'sanic (==21.6.2)',
        'uvloop'
    ],
)