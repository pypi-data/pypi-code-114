import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "ecs-dist",
    "version": "0.0.1",
    "description": "This package is for Projen Demo",
    "license": "Apache-2.0",
    "url": "https://github.com/AymanZahran/projen-cdk-tutorial-part-1.git",
    "long_description_content_type": "text/markdown",
    "author": "Ayman Zahran<ah.zahran@outlook.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/AymanZahran/projen-cdk-tutorial-part-1.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "ecs-mod",
        "ecs-mod._jsii"
    ],
    "package_data": {
        "ecs-mod._jsii": [
            "ecs-package@0.0.1.jsii.tgz"
        ],
        "ecs-mod": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk-lib>=2.1.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.55.1, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
