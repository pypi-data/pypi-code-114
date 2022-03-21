from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='ttscorpus',
    version='0.0.1',
    description='collection of different source of tts api for generating corpus.',
    url='https://github.com/voidful/tts-corpus-creator',
    author='Voidful',
    author_email='voidful.stack@gmail.com',
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    setup_requires=['setuptools-git'],
    classifiers=[
        'Development Status :: 4 - Beta',
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python :: 3.6'
    ],
    license="Apache",
    keywords='tts google tts gtts mac android tts',
    packages=find_packages(),
    install_requires=required,
    python_requires=">=3.5.0",
    zip_safe=False,
)
