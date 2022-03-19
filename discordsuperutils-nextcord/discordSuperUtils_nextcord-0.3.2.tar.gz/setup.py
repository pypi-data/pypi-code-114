from setuptools import setup

f = open("README.md", "r")
README = f.read()

setup(
    name="discordSuperUtils_nextcord",
    packages=["discordSuperUtils_nextcord"],
    package_data={
        "discordSuperUtils_nextcord.assets": ["assets"],
        "": ["*.png", "*.ttf"],
        "discordSuperUtils_nextcord.music": ["music"],
        "discordSuperUtils_nextcord.music.lavalink": ["lavalink"],
    },
    include_package_data=True,
    version="0.3.2",
    license="MIT",
    description="Discord Bot Development made easy!",
    long_description=README,
    long_description_content_type="text/markdown",
    author="koyashie07 and adam7100. converted by i-dan-mi-i",
    url="https://github.com/I-dan-mi-I/nextcord-super-utils",
    download_url="https://github.com/I-dan-mi-I/nextcord-super-utils/releases/download/0.3.1/discordSuperUtils_nextcord-0.3.1.tar.gz",
    keywords=[
        "nextcord",
        "easy",
        "music",
        "download",
        "links",
        "images",
        "videos",
        "audio",
        "bot",
        "paginator",
        "economy",
        "reaction",
        "reaction roles",
        "database",
        "database manager",
    ],
    install_requires=[
        "nextcord",
        "Pillow",
        "requests",
        "spotipy",
        "aiosqlite",
        "motor",
        "aiopg",
        "aiomysql",
        "pytz",
        "wavelink",
        "youtube_dl",
    ],
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
