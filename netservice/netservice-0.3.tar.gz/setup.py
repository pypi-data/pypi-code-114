import setuptools

setuptools.setup(
    name="netservice",
    version="0.3",
    author="NetService Co",
    author_email="sup@netservice.shop",
    description="Python NetService Library",
    long_description=open('README').read(),
    long_description_content_type="text/markdown",
    url="https://netservice.shop",
    download_url='https://github.com/mostafa-vn/netservice.git',
    packages=setuptools.find_packages(),
    keywords="netservice netservice.shop library python v3",
    install_requires=['requests', 'pyqrcode', 'dnspython', 'autopy'],
    license='MIT',
    platforms=['any'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    	'Environment :: Console',
    	'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
