from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='ev-audio-streaming-transcription-py',
    version='0.0.2',
    description='Quick test package for RingCenTral Engage Voice Audio Streaming feature.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DaKingKong/ev-audio-streaming-transcription-py',
    author='Da Kong',
    author_email='da.kong@ringcentral.com',
    license='MIT',
    python_requires='>=3.0',
    install_requires=[
        'google.cloud',
        'six.moves'
    ],
    packages=find_packages()
)
