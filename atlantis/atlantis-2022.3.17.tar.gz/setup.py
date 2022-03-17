from setuptools import setup, find_packages


def readme():
	with open('./README.md') as f:
		return f.read()


setup(
	name='atlantis',
	version='2022.3.17',
	description='Python library for simplifying data science',
	long_description=readme(),
	long_description_content_type='text/markdown',
	url='https://github.com/idin/atlantis',
	author='Idin',
	author_email='py@idin.ca',
	license='MIT',
	packages=find_packages(exclude=("jupyter", ".idea", ".git", "data_files")),
	install_requires=[
		'base32hex', 'geopy', 'pandas', 'joblib', 'numpy', 'sklearn', 'multiprocess', 'pyspark', 'matplotlib',
		'scipy', 'tldextract', 'validators'
	],
	package_data={'atlantis': ['data_files/*.pickle']},
	python_requires='~=3.6',
	zip_safe=False
)
