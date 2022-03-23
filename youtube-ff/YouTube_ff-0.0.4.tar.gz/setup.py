from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.4'
DESCRIPTION = 'A library which can be used to search youtube videos with ease.'
LONG_DESCRIPTION = 'A package that allows to search youtube videos using python along with the video information (likes, dislikes, etc.).'

# Setting up
setup(
    name="YouTube_ff",
    version=VERSION,
    author="Srinath-N-Gudi",
    author_email="srinathngudi11@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pytube', 'requests'],
    keywords=['python', 'video', 'youtube', 'youtube video', 'youtube video search'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
