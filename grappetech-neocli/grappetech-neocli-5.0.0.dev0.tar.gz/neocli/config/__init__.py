"""Module for setting up system and respective neocli configurations"""


def env():
	from jinja2 import Environment, PackageLoader
	return Environment(loader=PackageLoader('neocli.config'))
