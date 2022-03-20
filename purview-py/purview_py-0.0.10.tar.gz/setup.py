import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'purview_py',
    version = '0.0.10',
    license='MIT',
    description = 'Python wrapper for MSFT Purview and Apache Atlas APIs',
    author = 'Nathaniel Vala',
    author_email = 'nathanielvala@hotmail.com',
    url = 'https://github.com/spydernaz/purview_py',
    keywords = ['API', 'Data Management', 'Purview', 'Apache', 'Atlas', 'Metadata'],
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    # package_dir={"": "purview_py"},
    # packages=setuptools.find_packages(where="purview_py"),
    python_requires=">=3.6"

)