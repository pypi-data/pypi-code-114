import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NaroNet", 
    version="1.0.17",
    author="Daniel Jiménez-Sánchez",
    author_email="danijimnzs@gmail.com",
    description="NaroNet: discovery of tumor microenvironment elements from multiplex images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djimenezsanchez/NaroNet",
    project_urls={
        "Bug Tracker": "https://github.com/djimenezsanchez/NaroNet/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
		"License :: OSI Approved :: BSD License",
    ],
	license='BSD 3-Clause License',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires = [                                     
        'aicspylibczi>=3.0.5','czifile>=2019.7.2','imageio>=2.16.0',
        'hyperopt>=0.2.3','imgaug','matplotlib>=3.2.1',
        'numpy>=1.21.2','opencv-python>=4.5.5','pandas','imblearn',
        'torch','tensorboard>=2.8.0','scikit-learn','scikit-image',
        'Pillow','tifffile>=2020.2.9','xlsxwriter>=3.0.2','tqdm>=4.50.2','xlrd>=1.2.0',
        'argparse>=1.1','seaborn>=0.11.0','scipy>=1.5.4','openTSNE'
    ]
)


# Upload your package to PyPi
# Now, we create a source distribution with the following command:
# python setup.py sdist

# To upload to pypi test
# twine upload --repository testpypi dist/*
# To upload to pypi
# twine upload dist/*
# You will be asked to provide your username and password. Provide the credentials you used to register to PyPi earlier.