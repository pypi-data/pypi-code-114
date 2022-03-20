import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
VERSION = '0.0.3'

setuptools.setup(
    name="data_handler_csv",
    version=VERSION,
    description="useful function for my work",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    project_urls={
        "Source Code": "https://github.com/lalapopa/data_handler_csv",
    },
    author="LALAPOPA",
    install_requires=["numpy", "pandas", "scipy"],
    author_email="la_la_popa@vk.com",
    packages=setuptools.find_packages(),
    keywords=['csv', 'column', 'interpolation', 'data taker'],
    classifiers=[
    'Development Status :: 1 - Planning',
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: MIT License',
    ],
)
