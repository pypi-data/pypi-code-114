from setuptools import setup, find_packages

setup(
    name = 'MLmodule',
    version = '0.0.2',
    author = 'Ana Belisario',
    author_email = 'ana.belisario@alchemy.cloud',
    packages = find_packages(),
    install_requires = [
        'numpy',
        'pandas',
        'scikit-learn',
        'scipy',
        'xgboost',
    ],
    # dependency_links = [],
    description = 'Alchmey Cloud\'s compiled machine learning module',
    # license = '', #?
    keywords = "automated machine learning",
    # url = "",
    classifiers = ['Development Status :: 3 - Alpha',
                   'Topic :: Scientific/Engineering :: Physics',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python :: 3.8'],
)

# End of file