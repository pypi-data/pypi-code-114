from setuptools import setup

setup(name='Beautifly_B',
    version='0.1.6.1',  # DTest= release
    description='Beautifly_B team B packages',
    url='https://github.com/azmidri/Beautifly_B',
    author='IE TeamB',
    author_email='azmidri@student.ie.edu',
    license='MIT',
    packages=['Beautifly_B'],
    keywords="pandas data-science data-analysis python eda",
    install_requires=['hvplot','bokeh>=2.4.2','holoviews>=1.14.8','datetime','scikit_learn','numpy','pandas'],
    python_requires='>=3',
    zip_safe=False)