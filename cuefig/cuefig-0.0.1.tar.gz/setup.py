from setuptools import setup, find_packages

setup(
    name='cuefig',
    version='0.0.1',
    url='https://github.com/FavorMylikes/cuefig',
    license='MIT License',
    author='麦丽素',
    author_email='l786112323@gmail.com',
    description='A config framework that you can cue and hint quickly.',
    data_files=[('cuefig/logger', ['cuefig/logger/logging.yaml'])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
)


