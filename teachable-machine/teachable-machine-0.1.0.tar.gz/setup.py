from setuptools import setup, find_packages


VERSION = '0.1.0'
DESCRIPTION = 'A Python package to simplify the deployment process of exported Teachable Machine models.'
LONG_DESCRIPTION = 'A Python package to simplify the deployment process of exported Teachable Machine models \
into different environments like Windows, Linux and so on. Find source code at https://github.com/MeqdadDev/teachable-machine'

# Setting up
setup(
    name="teachable-machine",
    version=VERSION,
    author="Meqdad Dev (Meqdad Darwish)",
    author_email="meqdad.darweesh@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'Pillow', 'tensorflow'],
    url='https://github.com/MeqdadDev/teachable-machine',
    download_url='https://github.com/MeqdadDev/teachable-machine',
    keywords=['python', 'teachable machine', 'ai', 'computer vision',
              'camera', 'opencv', 'image classification'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License"
    ]
)
