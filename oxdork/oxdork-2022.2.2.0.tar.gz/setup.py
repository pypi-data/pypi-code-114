import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="oxdork",
    version="2022.2.2.0",
    author="Richard Mwewa",
    author_email="richardmwewa@duck.com",
    packages=["oxdork"],
    description="Google dorking tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rly0nheart/oxdork",
    license="MIT License",
    install_requires=["google","requests"],
    classifiers=[
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
        ],
    entry_points={
        "console_scripts": [
            "oxdork=oxdork.main:main",
        ]
    },
)