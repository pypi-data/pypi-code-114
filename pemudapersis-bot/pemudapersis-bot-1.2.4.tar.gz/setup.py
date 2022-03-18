# -*- coding: utf-8 -*-
""" Pemuda Persis bot """
from setuptools import setup, find_packages

requirements = [
    x.strip() for x in open('requirements.txt').readlines() if not x.startswith('#')]


setup(
    name="pemudapersis-bot",
    version="1.2.4",
    description="The official chatbot of Pemuda Persatuan Islam (PERSIS)",
    long_description=open("README.md").read().strip(),
    author="zamzambadruzaman",
    author_email="azzambz@pm.me",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "pemudapersis-bot = pemudapersis_bot.cli.cli:handle_commands",
        ],
    },
    python_requires=">=3.8",
)
