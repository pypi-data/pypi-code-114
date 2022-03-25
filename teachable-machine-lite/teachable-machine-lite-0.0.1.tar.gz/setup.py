from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

VERSION = '0.0.1'
DESCRIPTION = 'A Python package to simplify the deployment process of exported Teachable Machine models into different embedded systems environments like Raspberry Pi and other SBCs using TensorFlowLite.'
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="teachable-machine-lite",
    version=VERSION,
    author="Meqdad Dev (Meqdad Darwish)",
    author_email="meqdad.darweesh@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'tflite-runtime'],
    url='https://github.com/MeqdadDev/teachable-machine-lite',
    download_url='https://github.com/MeqdadDev/teachable-machine-lite',
    keywords=['python', 'teachable machine', 'ai', 'computer vision',
              'camera', 'opencv', 'image classification', 'tensorflowlite'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License"
    ]
)
