import setuptools

setuptools.setup(
    name="jiesu-python-service",
    version="1.7",
    description="A Python Service",
    author="Jie Su",
    install_requires=["Flask", "py-eureka-client"],
    packages=setuptools.find_packages(),
    zip_safe=False,
)
