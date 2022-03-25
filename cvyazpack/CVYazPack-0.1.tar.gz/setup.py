from distutils.core import setup
setup(
    name='CVYazPack',
    packages=['CVYazPack'],
    version='0.1',
    license='MIT',
    description='This is a ComputerVision Package Created by Yazdan',
    author='Yazdan Ghanavati',
    author_email='y.ghanavati79@gmail.com',

    keywords=['ComputerVision', 'HandTracking', 'FaceTracking', 'PoseEstimation'],
    install_requires=[
        'opencv-python',
        'numpy',
        'mediapipe'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)