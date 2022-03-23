import setuptools

DESCRIPTION = "Securely serialize model object"
LONG_DESCRIPTION = "This package aims to attach a secret-key to the model object to add security and serialize the " \
                   "model object to a byte stream. "

setuptools.setup(
    name="secure-model-serialization",
    version="0.2",
    author="Srujana Subramanya",
    author_email="ssubramanya@ripple.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://gitlab.ops.ripple.com/data-team/data-science/monorepo-python-packages",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "secure_serialization"},
    packages=setuptools.find_packages(where="secure_serialization"),
    python_requires="==3.9.7",
    test_suite='nose.collector',
    tests_require=['nose'],
)
