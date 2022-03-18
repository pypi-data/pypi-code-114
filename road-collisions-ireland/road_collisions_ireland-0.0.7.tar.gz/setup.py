from setuptools import (
    find_packages,
    setup
)

INSTALL_REQUIRES = (
    'road-collisions-base'
)

setup(
    name='road_collisions_ireland',
    version='0.0.7',
    python_requires='>=3.6',
    description='Road collision data for Ireland',
    author='Robert Lucey',
    url='https://github.com/RobertLucey/road-collisions-ireland',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=INSTALL_REQUIRES,
    package_data={
        'road_collisions_ireland': [
            'resources/ireland/ireland.csv.tgz'
        ]
    },
    entry_points={
        'console_scripts': [
            'raw_cleaner = road_collisions_ireland.bin.raw_cleaner:main',
            'load_road_collisions_ireland = road_collisions_ireland.bin.load:main',
        ]
    }
)
