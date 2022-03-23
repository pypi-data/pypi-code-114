import setuptools
from setuptools import setup

setup(
    name='windshield',
    version='0.0.2',
    packages=setuptools.find_packages(),
    url='https://github.com/pypa/sampleproject',
    license='MIT',
    author='Yang Xiaoyu',
    author_email='yangxiaoyu@flashexpress.com',
    description='Predict point in distrct',
    # long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['Shapely==1.8.1', 'geopandas==0.10.2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
# from Cython.Build import cythonize

# setup(name="paser", ext_modules=cythonize(["./geocode/paser.py"]))
