from setuptools import setup, find_packages

long_description = '''
Bibliothèque python visant à faciliter l'usage de l'api Helloasso. Compatible de python3.6 jusqu'à python 3.10

La bibliothèque permet de gérér l'authentification et l'authorization auprès de l'api Helloasso

Documentation: https://github.com/HelloAsso/HaApiV5

'''

setup(
    name="helloasso_apiv5",
    version="1.0.0",
    description="Python wrapper for Helloasso APIV5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/HelloAsso/HaApiV5',
    author="Helloasso",
    author_email="api.support@helloasso.org",
    maintainer='Helloasso',
    license='MIT License',
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=[
        "requests>=2.23.0",
        "oauthlib~=3.1.0",
        "requests-oauthlib~=1.3.0",
        "typing_extensions>=3.7.4.2",
    ],
    python_requires=">=3.6",
)
