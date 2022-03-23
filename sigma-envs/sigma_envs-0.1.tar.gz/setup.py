import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name='sigma_envs',
        version='0.1',
        packages=['learning-to-rationalize'],
        author="Gustavo Moreira",
        author_email="gm2qb@virginia.edu",
        description="OpenAI Gym Environments from the SIGMA lab at UVA",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/lab-sigma/learning-to-rationalize",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
)
