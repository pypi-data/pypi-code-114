import setuptools

setuptools.setup(
    name='ImagetoSketch',
    version='0.1.2',
    author='Asif Ahmed Neloy',
    author_email='neloyn@myumanitoba.ca',
    description='Python open-source library to convert color or B&W image to pencil sketch',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    License='MIT',
    long_description_content_type="text/markdown",
    url='https://github.com/aaneloy/Image_to_sketch',
    keywords='scaler',
    py_module=["ImagetoSketch"],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)