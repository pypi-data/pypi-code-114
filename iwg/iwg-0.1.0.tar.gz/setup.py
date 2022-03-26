import setuptools
import sitegenlib 

try:
    with open("README.md", encoding="utf-8") as fp:
        LONG_DESCRIPTION = fp.read()
except IOError:
    LONG_DESCRIPTION = ""


if __name__ == "__main__":
    setuptools.setup(
        name="iwg",
        version=sitegenlib.VERSION,
        description="An in-house website generator",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author="Bora Ozdogan",
        author_email="boraozdogan99@gmail.com",
        url="http://github.com/bozdogan/iwg",
        license="MIT",
        packages=setuptools.find_packages(),
        install_requires=["toml", "pyyaml", "markdown~=3.3.6"],
        extras_require={
            "dev": [
            ]
        },
        classifiers=[
            "Development Status :: 1 - Planning",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.8",
            "Topic :: Software Development :: Code Generators",
        ],
    )
