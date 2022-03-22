from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()
  
setup(
    name='ditolo',
    description="discord extension package ditolo",
    version='0.1.3',
    packages=find_packages(),
    author="Za",
    url="https://github.com/zearakun/discord-token-login-packege",
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown'
)
