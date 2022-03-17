import setuptools

with open('ReadMe.md', 'r') as f:
    long_description = f.read()
    
with open('requirements.txt', 'r', encoding='UTF-16') as f:
    required = f.readlines()


setuptools.setup(
    name="rmdirs",
    version="0.1.0",
    
    author="A-Bak",
    author_email="adam.bak753@gmail.com",
    
    description="Python utility for removing all subdirectories of a directory while preserving all the files located in the subdirectories.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='utility util file-system file-structure remove-directories remove-dirs',
    url='https://github.com/A-Bak/remove-dirs',
    
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=required,
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)