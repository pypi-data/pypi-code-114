from setuptools import setup, find_packages


LONGDESCRIPTION = """# Reddit Scraper\n-----\n# NOT FOR PUBLIC USE"""

VERSION = "0.0.4"
DESCRIPTION = "Scrapes subreddit, meant for internal use in https://github.com/TheOnlyWayUp/writingSite"

# Setting up
setup(
    name="subreddit_scraper",
    version=VERSION,
    author="TheOnlyWayUp",
    author_email="thedarkdraconian@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONGDESCRIPTION,
    packages=find_packages(),
    install_requires=["aiohttp", "rich", "asyncpraw", "prisma"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)