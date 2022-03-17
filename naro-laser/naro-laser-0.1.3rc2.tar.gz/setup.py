import time

from setuptools import find_packages, setup

about = {}
with open("flaskr/__about__.py") as fp:
    exec(fp.read(), about)
# later on we use: version['__version__']
print("\n\n")
print(about)

if True:
    setup(
        # name='naro-flaskr', 이미 다른 프로젝트에서 사용했다.
        name='naro-laser',
        # version='0.0.1.3',  # 21.0917
        # version='0.0.1.4',  # 21.0920
        # version='0.0.1.5',  # 21.1126
        # version='0.0.2',  # 21.1126
        # version='0.0.2.1',  # 21.1207, beta, local install test

        version=about['__version__'],
        # build_date=time.asctime(),  # NO!!!

        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'flask',
        ],
    )
