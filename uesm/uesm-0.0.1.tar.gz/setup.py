from setuptools import setup, find_namespace_packages

setup(
    name="uesm",
    version="0.0.1",
    packages=['uesm'],
    python_requires=">=3.9",
    install_requires=["GitPython"],
    test_requires=["pytest", "pytest-cov"],
    entry_points={
        'console_scripts': ['uesm=uesm.cmdline:main']
    }
)
