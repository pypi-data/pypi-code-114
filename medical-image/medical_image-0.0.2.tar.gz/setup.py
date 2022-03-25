from setuptools import setup, find_packages
import medical_image

setup(
    name="medical_image",
    version=medical_image.__version__,
    license='MIT',
    author="Hwa Pyung Kim",
    author_email="hpkim0512@deepnoid.com",
    description="DICOM Networking Library for AI Apps",
    long_description=open('README.md').read(),
    url="https://gl.deepnoid.com:9443/deep-ai/general/medical-image",
    packages=find_packages(),
    python_requires='>=3',
    install_requires=[
        'opencv-python',
        'pydicom',
        'numpy',
        'pillow'
    ]
)