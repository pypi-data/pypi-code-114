import setuptools
# from Cython.Build import cythonize
from setuptools import setup

setup(
    name='windshield',
    version='0.0.10',
    packages=setuptools.find_packages(),
    url='https://github.com/pypa/sampleproject',
    license='MIT',
    author='Yang Xiaoyu',
    author_email='yangxiaoyu@flashexpress.com',
    description='Predict point in distrct',

    # long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['Shapely==1.8.0', 'geopandas==0.10.2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    # package_data={
    #     # 任何包中含有.txt文件，都包含它
    #     '': ['*.so'],
    # }
)
