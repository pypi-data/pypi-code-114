from distutils.core import setup

setup(
    name="simple-fast-python",
    version="1.0",
    description="An implementation of the SiMPle-Fast algorithm",
    author="Anthony Miyaguchi",
    author_email="acmiyaguchi@gmail.com",
    url="https://github.com/acmiyaguchi/simple-fast-python",
    packages=["simple"],
    install_requires=[
        "numpy",
    ],
)
