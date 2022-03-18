import setuptools

def get_long_description(filename: str):
    """
    Load package long description from a markdown file.
    """
    with open(filename, encoding="utf-8") as description_file:
        return description_file.read()

setuptools.setup(
    name="dockerhub-client",
    description="Client library for dockerhub API, provides a CLI interface.",
    version="0.0.4",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "dockerhub=dockerhub.__main__:CLI"
        ]
    },
    install_requires=[
        "click==8.0.4",
        "pydantic==1.9.0",
        "requests==2.27.1"
    ],
    long_description=get_long_description("README.md"),
    long_description_content_type='text/markdown',
)
