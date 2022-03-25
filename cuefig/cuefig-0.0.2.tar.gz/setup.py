from setuptools import setup, find_packages

with open('requirements.txt', mode="r", encoding="utf8") as f:
    required = f.read().splitlines()

setup(
    name='cuefig',
    version='0.0.2',
    url='https://github.com/FavorMylikes/cuefig',
    license='MIT License',
    author='麦丽素',
    author_email='l786112323@gmail.com',
    description='A config framework that you can cue and hint quickly.',
    package_data={"": ["*.yaml"], },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    packages=find_packages(),
    python_requires=">=3.7",
)
